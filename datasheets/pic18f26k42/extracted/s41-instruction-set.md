                        PIC18(L)F26/27/45/46/47/55/56/57K42
41.0      INSTRUCTION SET SUMMARY                            The literal instructions may use some of the following
                                                             operands:
PIC18(L)F26/27/45/46/47/55/56/57K42 devices incor-
                                                             • A literal value to be loaded into a file register
porate the standard set of PIC18 core instructions, as
                                                               (specified by ‘k’)
well as an extended set of instructions, for the optimi-
zation of code that is recursive or that utilizes a soft-    • The desired FSR register to load the literal value
ware stack. The extended set is discussed later in this        into (specified by ‘f’)
section.                                                     • No operand required
                                                               (specified by ‘—’)
41.1      Standard Instruction Set                           The control instructions may use some of the following
                                                             operands:
The standard PIC18 instruction set adds many
enhancements to the previous PIC® MCU instruction            • A program memory address (specified by ‘n’)
sets, while maintaining an easy migration from these         • The mode of the CALL or RETURN instructions
PIC® MCU instruction sets. Most instructions are a             (specified by ‘s’)
single program memory word (16 bits), but there are          • The mode of the table read and table write
few instructions that require two- or three-program            instructions (specified by ‘m’)
memory locations and two that require three-program          • No operand required
memory locations.                                              (specified by ‘—’)
Each single-word instruction is a 16-bit word divided        All instructions are a single word, except for few two or
into an opcode, which specifies the instruction type and     three word instructions. These instructions were made
one or more operands, which further specify the              two- or three-word to contain the required information
operation of the instruction.                                in 32 or 48 bits. In the second word and third words, the
                                                             four MSbs are ‘1’s. If this second or third word is
The instruction set is highly orthogonal and is grouped
                                                             executed as an instruction (by itself), it will execute as
into four basic categories:
                                                             a NOP.
• Byte-oriented operations
                                                             All single-word instructions are executed in a single
• Bit-oriented operations                                    instruction cycle, unless a conditional test is true or the
• Literal operations                                         program counter is changed as a result of the
• Control operations                                         instruction. In these cases, the execution takes two
The PIC18 instruction set summary in Table 41-3 lists        instruction cycles, with the additional instruction
byte-oriented, bit-oriented, literal and control             cycle(s) executed as a NOP.
operations. Table 41-1 shows the opcode field                The two-word instructions execute in two instruction
descriptions.                                                cycles and three-word instructions execute in three
Most byte-oriented instructions have three operands:         instruction cycles.

1.   The file register (specified by ‘f’)                    One instruction cycle consists of four oscillator periods.
                                                             Thus, for an oscillator frequency of 4 MHz, the normal
2.   The destination of the result (specified by ‘d’)
                                                             instruction execution time is 1 s. If a conditional test is
3.   The accessed memory (specified by ‘a’)
                                                             true, or the program counter is changed as a result of
The file register designator ‘f’ specifies which file        an instruction, the instruction execution time is 2 s.
register is to be used by the instruction. The destination   Two-word branch instructions (if true) would take 3 s.
designator ‘d’ specifies where the result of the
                                                             Figure 41-1 shows the general formats that the
operation is to be placed. If ‘d’ is zero, the result is
                                                             instructions can have. All examples use the convention
placed in the WREG register. If ‘d’ is one, the result is
                                                             ‘nnh’ to represent a hexadecimal number.
placed in the file register specified in the instruction.
                                                             The Instruction Set Summary, shown in Table 41-3,
All bit-oriented instructions have three operands:
                                                             lists the standard instructions recognized by the
1.   The file register (specified by ‘f’)                    Microchip Assembler (MPASMTM).
2.   The bit in the file register (specified by ‘b’)         Section 41.1.1 “Standard Instruction Set” provides
3.   The accessed memory (specified by ‘a’)                  a description of each instruction.
The bit field designator ‘b’ selects the number of the bit
affected by the operation, while the file register
designator ‘f’ represents the number of the file in which
the bit is located.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 663
                      PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 41-1:       OPCODE FIELD DESCRIPTIONS
          Field                                                                   Description

a                     RAM access bit
                      a = 0: RAM location in Access RAM (BSR register is ignored)
                      a = 1: RAM bank is specified by BSR register
ACCESS                ACCESS = 0: RAM access bit symbol
BANKED                BANKED = 1: RAM access bit symbol
bbb                   Bit address within an 8-bit file register (0 to 7)
BSR                   Bank Select Register. Used to select the current RAM bank.
d                     Destination select bit;
                      d = 0: store result in WREG,
                      d = 1: store result in file register f.
dest                  Destination either the WREG register or the specified register file location
f                     8-bit Register file address (00h to FFh)
fn                    FSR Number (0 to 2)
fs                    12-bit Register file address (000h to FFFh) or 14-bit Register file address (0000h to 3FFFh). This is the source address.
fd                    12-bit Register file address (000h to FFFh) or 14-bit Register file address (0000h to 3FFFh). This is the destination address.
zs                    7-bit literal offset for FSR2 to used as register file address (000h to FFFh). This is the source address.
zd                    7-bit literal offset for FSR2 to used as register file address (000h to FFFh). This is the destination address.
k                     Literal field, constant data or label (may be a 6-bit, 8-bit, 12-bit or a 20-bit value)
label                 Label name
mm                    The mode of the TBLPTR register for the Table Read and Table Write instructions
                      Only used with Table Read and Table Write instructions:
*                     No Change to register (such as TBLPTR with Table reads and writes)
*+                    Post-Increment register (such as TBLPTR with Table reads and writes)
*-                    Post-Decrement register (such as TBLPTR with Table reads and writes)
+*                    Pre-Increment register (such as TBLPTR with Table reads and writes)
n                     The relative address (2’s complement number) for relative branch instructions, or the direct address for Call/Branch and
                      Return instructions
PRODH                 Product of Multiply high byte
PRODL                 Product of Multiply low byte
s                     Fast Call / Return mode select bit.
                      s = 0: do not update into/from shadow registers
                      s = 1: certain registers loaded into/from shadow registers (Fast mode)
u                     Unused or Unchanged
W                     W = 0: Destination select bit symbol
WREG                  Working register (accumulator)
x                     Don't care (0 or 1)
                      The assembler will generate code with x = 0. It is the recommended form of use for compatibility with all Microchip software
                      tools.
TBLPTR                21-bit Table Pointer (points to a Program Memory location)
TABLAT                8-bit Table Latch
TOS                   Top of Stack
PC                    Program Counter
PCL                   Program Counter Low Byte
PCH                   Program Counter High Byte
PCLATH                Program Counter High Byte Latch
PCLATU                Program Counter Upper Byte Latch
GIE                   Global Interrupt Enable bit
WDT                   Watchdog Timer
TO                    Time-out bit
PD                    Power-down bit
C, DC, Z, OV, N       ALU status bits Carry, Digit Carry, Zero, Overflow, Negative
[     ]               Indexed address
(     )               Contents
                     Assigned to


 2017-2021 Microchip Technology Inc.                                                                                    DS40001919G-page 664
                       PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 41-1:       OPCODE FIELD DESCRIPTIONS (CONTINUED)
          Field                                                                        Description

                Optional argument
[expr]<n>             Specifies bit n of the register indicated by the pointer expr
< >                   Register bit field
                     In the set of
italics               User defined term (font is courier)


FIGURE 41-1:              General Format for Instructions (1/2)

                  Byte-oriented file register operations                                              Example Instruction

                     15               10    9        8 7                          0
                            OPCODE         d         a         f (FILE #)                            ADDWF MYREG, W, B

                           d = 0 for result destination to be WREG register
                           d = 1 for result destination to be file register (f)
                           a = 0 to force Access Bank
                           a = 1 for BSR to select bank
                           f = 8-bit file register address

                  Byte to Byte move operations (2-word)

                     15        12 11                                          0
                      OPCODE                         f (Source FILE #)                               MOVFF MYREG1, MYREG2

                     15        12 11                                          0
                          1111                      f (Destination FILE #)

                           f = 12-bit file register address

                  Byte to Byte move operations (3-word)

                     15                                                 4 3            0
                                                    OPCODE                    FILE #                 MOVFFL MYREG1, MYREG2

                     15          12 11                                                 0
                           1111                               FILE #

                     15           12 11                                                0
                           1111                               FILE #


                  Bit-oriented file register operations

                     15        12 11           9 8 7                              0
                      OPCODE b (BIT #) a                   f (FILE #)                                BSF MYREG, bit, B

                           b = 3-bit position of bit in file register (f)
                           a = 0 to force Access Bank
                           a = 1 for BSR to select bank
                           f = 8-bit file register address

                  Literal operations

                     15                         8     7                           0
                             OPCODE                         k (literal)                              MOVLW 7Fh

                          k = 8-bit immediate value


 2017-2021 Microchip Technology Inc.                                                                                       DS40001919G-page 665
                         PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 41-2:             General Format for Instructions (2/2)
                  Control operations

                  CALL, GOTO and Branch operations
                    15                            8 7                           0
                                  OPCODE                     n[7:0] (literal)        GOTO Label

                    15             12 11                                     0
                           1111                    n[19:8] (literal)

                         n = 20-bit immediate value

                    15                            8 7                            0
                              OPCODE                    S n[7:0] (literal)           CALL MYFUNC

                    15             12 11                                        0
                            1111                   n[19:8] (literal)
                                   S = Fast bit


                    15                 11 10                                    0
                     OPCODE                 n[10:0] (literal)                        BRA MYFUNC


                    15                     8 7                                   0
                      OPCODE                      n[7:0] (literal)                   BC MYFUNC


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 666
                          PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 41-2:             INSTRUCTION SET
     Mnemonic,                                                                     16-Bit Instruction Word              Status
                                        Description                  Cycles                                                           Notes
     Operands                                                                   MSb                         LSb        Affected

BYTE-ORIENTED FILE REGISTER INSTRUCTIONS
ADDWF          f, d ,a   Add WREG and f                             1           0010    01da      ffff     ffff    C, DC, Z, OV, N
ADDWFC         f, d, a   Add WREG and Carry bit to f                1           0010    00da      ffff     ffff    C, DC, Z, OV, N
ANDWF          f, d, a   AND WREG with f                            1           0001    01da      ffff     ffff    Z, N
CLRF           f, a      Clear f                                    1           0110    101a      ffff     ffff    Z
COMF           f, d, a   Complement f                               1           0001    11da      ffff     ffff    Z, N
DECF           f, d, a   Decrement f                                1           0000    01da      ffff     ffff    C, DC, Z, OV, N
INCF           f, d, a   Increment f                                1           0010    10da      ffff     ffff    C, DC, Z, OV, N
IORWF          f, d, a   Inclusive OR WREG with f                   1           0001    00da      ffff     ffff    Z, N
MOVF           f, d, a   Move f to WREG or f                        1           0101    00da      ffff     ffff    Z, N
MOVFF          fs, fd    Move fs (source) to        1st word        2           1100    ffff      ffff     ffff    None            2, 3
                               fd (destination)     2nd word                    1111    ffff      ffff     ffff
MOVFFL         fs, fd    Move fs (source) to                        3           0000    0000      0110     ffff    None               2
                               g (full destination)                             1111    ffff      ffff     ffgg
                               fd (full destination)3rd word                    1111    gggg      gggg     gggg
MOVWF          f, a      Move WREG to f                             1           0110    111a      ffff     ffff    None
MULWF          f, a      Multiply WREG with f                       1           0000    001a      ffff     ffff    None
NEGF           f, a      Negate f                                   1           0110    110a      ffff     ffff    C, DC, Z, OV, N
RLCF           f, d, a   Rotate Left f through Carry                1           0011    01da      ffff     ffff    C, Z, N
RLNCF          f, d, a   Rotate Left f (No Carry)                   1           0100    01da      ffff     ffff    Z, N
RRCF           f, d, a   Rotate Right f through Carry               1           0011    00da      ffff     ffff    C, Z, N
RRNCF          f, d, a   Rotate Right f (No Carry)                  1           0100    00da      ffff     ffff    Z, N
SETF           f, a      Set f                                      1           0110    100a      ffff     ffff    None
SUBFWB         f, d, a   Subtract f from WREG with                  1           0101    01da      ffff     ffff    C, DC, Z, OV, N
                           borrow
SUBWF          f, d, a   Subtract WREG from f                       1           0101    11da      ffff     ffff C, DC, Z, OV, N
SUBWFB         f, d, a   Subtract WREG from f with                  1           0101    10da      ffff     ffff C, DC, Z, OV, N
                           borrow
SWAPF          f, d, a   Swap nibbles in f                          1           0011    10da      ffff     ffff None
XORWF          f, d, a   Exclusive OR WREG with f                   1           0001    10da      ffff     ffff Z, N
BYTE-ORIENTED SKIP INSTRUCTIONS
CPFSEQ         f, a      Compare f with WREG, skip =                1-4         0110    001a      ffff     ffff    None               1
CPFSGT         f, a      Compare f with WREG, skip >                1-4         0110    010a      ffff     ffff    None               1
CPFSLT         f, a      Compare f with WREG, skip <                1-4         0110    000a      ffff     ffff    None               1
DECFSZ         f, d, a   Decrement f, Skip if 0                     1-4         0010    11da      ffff     ffff    None               1
DCFSNZ         f, d, a   Decrement f, Skip if Not 0                 1-4         0100    11da      ffff     ffff    None               1
INCFSZ         f, d, a   Increment f, Skip if 0                     1-4         0011    11da      ffff     ffff    None               1
INFSNZ         f, d, a   Increment f, Skip if Not 0                 1-4         0100    10da      ffff     ffff    None               1
TSTFSZ         f, a      Test f, skip if 0                          1-4         0110    011a      ffff     ffff    None               1
BIT-ORIENTED FILE REGISTER INSTRUCTIONS
BCF            f, b, a   Bit Clear f                                1           1001 bbba       ffff      ffff     None
BSF            f, b, a   Bit Set f                                  1           1000 bbba       ffff      ffff     None
BTG            f, b, a   Bit Toggle f                               1           0111 bbba       ffff      ffff     None
BIT-ORIENTED SKIP INSTRUCTIONS
BTFSC          f, b, a   Bit Test f, Skip if Clear                  1-4         1011 bbba       ffff      ffff     None               1
BTFSS          f, b, a   Bit Test f, Skip if Set                    1-4         1010 bbba       ffff      ffff     None               1
Note 1: If Program Counter (PC) is modified or a conditional test is true, the instruction requires an additional cycle. The extra cycle is
        executed as a NOP.
     2: Some instructions are multi word instructions. The second/third words of these instructions will be decoded as a NOP, unless the
        first word of the instruction retrieves the information embedded in these 16-bits. This ensures that all program memory locations
        have a valid instruction.
     3: fs and fd do not cover the full memory range. 2 MSBs of bank selection are forced to ‘b00 to limit the range of these instructions to
        lower 4k addressing space.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 667
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 41-2:           INSTRUCTION SET (CONTINUED)
     Mnemonic,                                                                     16-Bit Instruction Word              Status
                                      Description                    Cycles                                                           Notes
     Operands                                                                   MSb                         LSb        Affected

CONTROL INSTRUCTIONS
BC             n       Branch if Carry                              1 (2)       1110    0010    nnnn      nnnn     None               1
BN             n       Branch if Negative                           1 (2)       1110    0110    nnnn      nnnn     None               1
BNC            n       Branch if Not Carry                          1 (2)       1110    0011    nnnn      nnnn     None               1
BNN            n       Branch if Not Negative                       1 (2)       1110    0111    nnnn      nnnn     None               1
BNOV           n       Branch if Not Overflow                       1 (2)       1110    0101    nnnn      nnnn     None               1
BNZ            n       Branch if Not Zero                           1 (2)       1110    0001    nnnn      nnnn     None               1
BOV            n       Branch if Overflow                           1 (2)       1110    0100    nnnn      nnnn     None               1
BRA            n       Branch Unconditionally                       2           1101    0nnn    nnnn      nnnn     None
BZ             n       Branch if Zero                               1 (2)       1110    0000    nnnn      nnnn     None               1
CALL           k, s    Call subroutine       1st word               2           1110    110s    kkkk      kkkk     None               2
                                             2nd word                           1111    kkkk    kkkk      kkkk
CALLW          —       Call subroutine using WREG                   2           0000    0000    0001      0100     None               1
GOTO           k       Go to address         1st word               2           1110    1111    kkkk      kkkk     None               2
               —                             2nd word                           1111    kkkk    kkkk      kkkk
RCALL          n       Relative Call                                2           1101    1nnn    nnnn      nnnn     None               1
RETFIE         s       Return from interrupt enable                 2           0000    0000    0001      000s     None               1
RETLW          k       Return with literal in WREG                  2           0000    1100    kkkk      kkkk     None               1
RETURN         s       Return from Subroutine                       2           0000    0000    0001      001s     None               1
INHERENT INSTRUCTIONS
CLRWDT         —       Clear Watchdog Timer                         1           0000    0000    0000      0100     None
DAW            —       Decimal Adjust WREG                          1           0000    0000    0000      0111     C
NOP            —       No Operation                                 1           0000    0000    0000      0000     None
NOP            —       No Operation                                 1           1111    xxxx    xxxx      xxxx     None               2
POP            —       Pop top of return stack (TOS)                1           0000    0000    0000      0110     None
PUSH           —       Push top of return stack (TOS)               1           0000    0000    0000      0101     None
RESET                  Software device Reset                        1           0000    0000    1111      1111     All
SLEEP          —       Go into Standby mode                         1           0000    0000    0000      0011     None
Note 1: If Program Counter (PC) is modified or a conditional test is true, the instruction requires an additional cycle. The extra cycle is
        executed as a NOP.
     2: Some instructions are multi word instructions. The second/third words of these instructions will be decoded as a NOP, unless the
        first word of the instruction retrieves the information embedded in these 16-bits. This ensures that all program memory locations
        have a valid instruction.
     3: fs and fd do not cover the full memory range. 2 MSBs of bank selection are forced to ‘b00 to limit the range of these instructions to
        lower 4k addressing space.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 668
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 41-2:            INSTRUCTION SET (CONTINUED)
     Mnemonic,                                                                     16-Bit Instruction Word              Status
                                      Description                    Cycles                                                           Notes
     Operands                                                                   MSb                         LSb        Affected

LITERAL INSTRUCTIONS
ADDLW          k        Add literal and WREG                        1           0000    1111    kkkk      kkkk     C, DC, Z, OV, N
ANDLW          k        AND literal with WREG                       1           0000    1011    kkkk      kkkk     Z, N
IORLW          k        Inclusive OR literal with WREG              1           0000    1001    kkkk      kkkk     Z, N
LFSR           fn, k    Load FSR(fn) with a 14-bit                  2           1110    1110    00ff      kkkk     None
                          literal (k)                                           1111    00kk    kkkk      kkkk
ADDFSR         fn, k    Add FSR(fn) with (k)                        1           1110    1000    ffkk      kkkk     None
SUBFSR         fn, k    Subtract (k) from FSR(fn)                   1           1110    1001    ffkk      kkkk     None
MOVLB          k        Move literal to BSR[5:0]                    1           0000    0001    00kk      kkkk     None
MOVLW          k        Move literal to WREG                        1           0000    1110    kkkk      kkkk     None
MULLW          k        Multiply literal with WREG                  1           0000    1101    kkkk      kkkk     None
RETLW          k        Return with literal in WREG                 2           0000    1100    kkkk      kkkk     None
SUBLW          k        Subtract WREG from literal                  1           0000    1000    kkkk      kkkk     C, DC, Z, OV, N
XORLW          k        Exclusive OR literal with WREG              1           0000    1010    kkkk      kkkk     Z, N
DATA MEMORY  PROGRAM MEMORY INSTRUCTIONS
TBLRD*                  Table Read                                  2-5         0000    0000    0000      1000     None
TBLRD*+                 Table Read with post-increment                          0000    0000    0000      1001     None
TBLRD*-                 Table Read with post-decrement                          0000    0000    0000      1010     None
TBLRD+*                 Table Read with pre-increment                           0000    0000    0000      1011     None
TBLWT*                  Table Write                                 2-5         0000    0000    0000      1100     None
TBLWT*+                 Table Write with post-increment                         0000    0000    0000      1101     None
TBLWT*-                 Table Write with post-decrement                         0000    0000    0000      1110     None
TBLWT+*                 Table Write with pre-increment                          0000    0000    0000      1111     None
Note 1: If Program Counter (PC) is modified or a conditional test is true, the instruction requires an additional cycle. The extra cycle is
        executed as a NOP.
     2: Some instructions are multi word instructions. The second/third words of these instructions will be decoded as a NOP, unless the
        first word of the instruction retrieves the information embedded in these 16-bits. This ensures that all program memory locations
        have a valid instruction.
     3: fs and fd do not cover the full memory range. 2 MSBs of bank selection are forced to ‘b00 to limit the range of these instructions to
        lower 4k addressing space.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 669
                               PIC18(L)F26/27/45/46/47/55/56/57K42
41.1.1         STANDARD INSTRUCTION SET
                                                                          Example:                  ADDLW      15h
                                                                               Before Instruction
                                                                                     W     = 10h
ADDFSR                     Add Literal to FSR
                                                                               After Instruction
Syntax:                    ADDFSR f, k
                                                                                      W     =   25h
Operands:                  0  k  63
                           f  [ 0, 1, 2 ]
Operation:                 FSR(f) + k  FSR(f)
Status Affected:           None                                           ADDWF                     ADD W to f
Encoding:                     1110       1000         ffkk      kkkk      Syntax:                   ADDWF         f {,d {,a}}
Description:               The 6-bit literal ‘k’ is added to the          Operands:                 0  f  255
                           contents of the FSR specified by ‘f’.                                    d  [0,1]
Words:                     1                                                                        a  [0,1]
Cycles:                    1                                              Operation:                (W) + (f)  dest
Q Cycle Activity:
                                                                          Status Affected:          N, OV, C, DC, Z
                               Q1           Q2         Q3        Q4
                                                                          Encoding:                     0010      01da          ffff    ffff
                              Decode       Read       Pro-     Write to
                                        literal ‘k’   cess      FSR       Description:              Add W to register ‘f’. If ‘d’ is ‘0’, the
                                                      Data                                          result is stored in W. If ‘d’ is ‘1’, the
                                                                                                    result is stored back in register ‘f’
                                                                                                    (default).
Example:                  ADDFSR 2, 23h                                                             If ‘a’ is ‘0’, the Access Bank is selected.
                                                                                                    If ‘a’ is ‘1’, the BSR is used to select the
     Before Instruction
                                                                                                    GPR bank.
          FSR2       =         03FFh
                                                                                                    If ‘a’ is ‘0’ and the extended instruction
     After Instruction                                                                              set is enabled, this instruction operates
           FSR2       =        0422h                                                                in Indexed Literal Offset Addressing
                                                                                                    mode whenever f 95 (5Fh). See Sec-
                                                                                                    tion 41.2.3 “Byte-Oriented and Bit-
ADDLW                     ADD literal to W                                                          Oriented Instructions in Indexed Lit-
                                                                                                    eral Offset Mode” for details.
Syntax:                   ADDLW         k
                                                                          Words:                    1
Operands:                 0  k  255
                                                                          Cycles:                   1
Operation:                (W) + k  W
Status Affected:          N, OV, C, DC, Z
Encoding:                      0000         1111      kkkk       kkkk     Q Cycle Activity:

Description:              The contents of W are added to the                           Q1               Q2              Q3             Q4
                          8-bit literal ‘k’ and the result is placed in             Decode        Read              Process         Write to
                          W.                                                                    register ‘f’         Data          destination
Words:                    1
Cycles:                   1                                               Example:                  ADDWF         REG, 0, 0

Q Cycle Activity:                                                              Before Instruction
             Q1                Q2                Q3             Q4                   W          =       17h
                                                                                     REG        =       0C2h
          Decode             Read            Process         Write to W
                                                                               After Instruction
                          literal ‘k’         Data
                                                                                      W         =       0D9h
                                                                                      REG       =       0C2h


  Note:        All PIC18 instructions may take an optional label argument preceding the instruction mnemonic for use in
               symbolic addressing. If a label is used, the instruction format then becomes: {label} instruction argument(s).


 2017-2021 Microchip Technology Inc.                                                                               DS40001919G-page 670
                           PIC18(L)F26/27/45/46/47/55/56/57K42

ADDWFC                ADD W and CARRY bit to f                         ANDLW                     AND literal with W
Syntax:               ADDWFC          f {,d {,a}}                      Syntax:                   ANDLW         k
Operands:             0  f  255                                      Operands:                 0  k  255
                      d [0,1]
                                                                       Operation:                (W) .AND. k  W
                      a [0,1]
                                                                       Status Affected:          N, Z
Operation:            (W) + (f) + (C)  dest
                                                                       Encoding:                     0000          1011    kkkk      kkkk
Status Affected:      N,OV, C, DC, Z
                                                                       Description:              The contents of W are AND’ed with the
Encoding:                  0010      00da       ffff      ffff
                                                                                                 8-bit literal ‘k’. The result is placed in W.
Description:          Add W, the CARRY flag and data mem-
                                                                       Words:                    1
                      ory location ‘f’. If ‘d’ is ‘0’, the result is
                      placed in W. If ‘d’ is ‘1’, the result is        Cycles:                   1
                      placed in data memory location ‘f’.              Q Cycle Activity:
                      If ‘a’ is ‘0’, the Access Bank is selected.
                                                                                    Q1               Q2               Q3            Q4
                      If ‘a’ is ‘1’, the BSR is used to select the
                      GPR bank.                                                  Decode     Read literal            Process     Write to W
                      If ‘a’ is ‘0’ and the extended instruction                               ‘k’                   Data
                      set is enabled, this instruction operates
                      in Indexed Literal Offset Addressing             Example:                  ANDLW             05Fh
                      mode whenever f 95 (5Fh). See Sec-
                      tion 41.2.3 “Byte-Oriented and Bit-                   Before Instruction
                      Oriented Instructions in Indexed Lit-                       W          =       A3h
                      eral Offset Mode” for details.                        After Instruction
Words:                1                                                            W        =        03h
Cycles:               1
Q Cycle Activity:
             Q1            Q2            Q3              Q4
          Decode        Read          Process        Write to
                      register ‘f’     Data         destination


Example:              ADDWFC          REG, 0, 1
     Before Instruction
           CARRY bit =      1
           REG         =    02h
           W           =    4Dh
     After Instruction
           CARRY bit =      0
           REG         =    02h
           W           =    50h


 2017-2021 Microchip Technology Inc.                                                                               DS40001919G-page 671
                              PIC18(L)F26/27/45/46/47/55/56/57K42

ANDWF                     AND W with f                                        BC                     Branch if Carry
Syntax:                   ANDWF         f {,d {,a}}                           Syntax:                BC       n
Operands:                 0  f  255                                         Operands:              -128  n  127
                          d [0,1]
                                                                              Operation:             if CARRY bit is ‘1’
                          a [0,1]
                                                                                                     (PC) + 2 + 2n  PC
Operation:                (W) .AND. (f)  dest
                                                                              Status Affected:       None
Status Affected:          N, Z                                                Encoding:                  1110       0010        nnnn      nnnn
Encoding:                     0001       01da         ffff       ffff
                                                                              Description:           If the CARRY bit is ‘1’, then the program
Description:              The contents of W are AND’ed with                                          will branch.
                          register ‘f’. If ‘d’ is ‘0’, the result is stored                          The 2’s complement number ‘2n’ is
                          in W. If ‘d’ is ‘1’, the result is stored back                             added to the PC. Since the PC will have
                          in register ‘f’ (default).                                                 incremented to fetch the next
                          If ‘a’ is ‘0’, the Access Bank is selected.                                instruction, the new address will be
                          If ‘a’ is ‘1’, the BSR is used to select the                               PC + 2 + 2n. This instruction is then a
                          GPR bank.                                                                  2-cycle instruction.
                          If ‘a’ is ‘0’ and the extended instruction
                                                                              Words:                 1
                          set is enabled, this instruction operates
                          in Indexed Literal Offset Addressing                Cycles:                1(2)
                          mode whenever f 95 (5Fh). See Sec-                Q Cycle Activity:
                          tion 41.2.3 “Byte-Oriented and Bit-                 If Jump:
                          Oriented Instructions in Indexed Lit-
                                                                                           Q1            Q2                Q3             Q4
                          eral Offset Mode” for details.
                                                                                        Decode      Read literal      Process      Write to PC
Words:                    1                                                                            ‘n’             Data
Cycles:                   1                                                                No           No               No               No
                                                                                        operation    operation        operation        operation
Q Cycle Activity:
                                                                              If No Jump:
             Q1               Q2               Q3               Q4
                                                                                           Q1            Q2                Q3             Q4
          Decode        Read               Process          Write to
                                                                                        Decode      Read literal      Process             No
                      register ‘f’          Data           destination
                                                                                                       ‘n’             Data            operation

Example:                  ANDWF          REG, 0, 0
                                                                              Example:               HERE             BC    5
     Before Instruction
                                                                                   Before Instruction
           W          =       17h                                                        PC               =       address (HERE)
           REG        =       C2h
                                                                                   After Instruction
     After Instruction
                                                                                         If CARRY         =       1;
            W        =        02h                                                             PC          =       address (HERE + 12)
            REG      =        C2h                                                        If CARRY         =       0;
                                                                                              PC          =       address (HERE + 2)


 2017-2021 Microchip Technology Inc.                                                                                 DS40001919G-page 672
                          PIC18(L)F26/27/45/46/47/55/56/57K42

BCF                 Bit Clear f                                       BN                     Branch if Negative
Syntax:             BCF        f, b {,a}                              Syntax:                BN       n
Operands:           0  f  255                                       Operands:              -128  n  127
                    0b7
                                                                      Operation:             if NEGATIVE bit is ‘1’
                    a [0,1]
                                                                                             (PC) + 2 + 2n  PC
Operation:          0  f<b>
                                                                      Status Affected:       None
Status Affected:    None                                              Encoding:                  1110        0110       nnnn      nnnn
Encoding:                 1001      bbba        ffff        ffff
                                                                      Description:           If the NEGATIVE bit is ‘1’, then the
Description:        Bit ‘b’ in register ‘f’ is cleared.                                      program will branch.
                    If ‘a’ is ‘0’, the Access Bank is selected.                              The 2’s complement number ‘2n’ is
                    If ‘a’ is ‘1’, the BSR is used to select the                             added to the PC. Since the PC will have
                    GPR bank.                                                                incremented to fetch the next
                    If ‘a’ is ‘0’ and the extended instruction                               instruction, the new address will be
                    set is enabled, this instruction operates                                PC + 2 + 2n. This instruction is then a
                    in Indexed Literal Offset Addressing                                     2-cycle instruction.
                    mode whenever f 95 (5Fh). See Sec-
                                                                      Words:                 1
                    tion 41.2.3 “Byte-Oriented and Bit-
                    Oriented Instructions in Indexed Lit-             Cycles:                1(2)
                    eral Offset Mode” for details.                    Q Cycle Activity:
Words:              1                                                 If Jump:
                                                                                   Q1            Q2                Q3             Q4
Cycles:             1
                                                                                Decode      Read literal      Process      Write to PC
Q Cycle Activity:
                                                                                               ‘n’             Data
             Q1           Q2               Q3              Q4                      No           No               No               No
          Decode      Read             Process           Write                  operation    operation        operation        operation
                    register ‘f’        Data           register ‘f’   If No Jump:
                                                                                   Q1            Q2                Q3             Q4
Example:            BCF            FLAG_REG,      7, 0                          Decode      Read literal      Process             No
     Before Instruction                                                                        ‘n’             Data            operation
           FLAG_REG =            C7h
     After Instruction                                                Example:               HERE             BN    Jump
           FLAG_REG =            47h
                                                                           Before Instruction
                                                                                 PC               =       address (HERE)
                                                                           After Instruction
                                                                                 If NEGATIVE      =       1;
                                                                                      PC          =       address (Jump)
                                                                                 If NEGATIVE      =       0;
                                                                                      PC          =       address (HERE + 2)


 2017-2021 Microchip Technology Inc.                                                                         DS40001919G-page 673
                           PIC18(L)F26/27/45/46/47/55/56/57K42

BNC                    Branch if Not Carry                           BNN                    Branch if Not Negative
Syntax:                BNC      n                                    Syntax:                BNN      n
Operands:              -128  n  127                                Operands:              -128  n  127
Operation:             if CARRY bit is ‘0’                           Operation:             if NEGATIVE bit is ‘0’
                       (PC) + 2 + 2n  PC                                                   (PC) + 2 + 2n  PC
Status Affected:       None                                          Status Affected:       None
Encoding:                  1110       0011        nnnn      nnnn     Encoding:                  1110       0111      nnnn      nnnn
Description:           If the CARRY bit is ‘0’, then the program     Description:           If the NEGATIVE bit is ‘0’, then the
                       will branch.                                                         program will branch.
                       The 2’s complement number ‘2n’ is                                    The 2’s complement number ‘2n’ is
                       added to the PC. Since the PC will have                              added to the PC. Since the PC will have
                       incremented to fetch the next                                        incremented to fetch the next
                       instruction, the new address will be                                 instruction, the new address will be
                       PC + 2 + 2n. This instruction is then a                              PC + 2 + 2n. This instruction is then a
                       2-cycle instruction.                                                 2-cycle instruction.
Words:                 1                                             Words:                 1
Cycles:                1(2)                                          Cycles:                1(2)
Q Cycle Activity:                                                    Q Cycle Activity:
If Jump:                                                             If Jump:
             Q1            Q2                Q3             Q4                    Q1            Q2              Q3             Q4
          Decode      Read literal      Process      Write to PC               Decode      Read literal      Process      Write to PC
                         ‘n’             Data                                                 ‘n’             Data
             No           No               No               No                    No           No               No             No
          operation    operation        operation        operation             operation    operation        operation      operation
If No Jump:                                                          If No Jump:
             Q1            Q2                Q3             Q4                    Q1            Q2              Q3             Q4
          Decode      Read literal      Process             No                 Decode      Read literal      Process           No
                         ‘n’             Data            operation                            ‘n’             Data          operation


Example:               HERE            BNC    Jump                   Example:               HERE            BNN   Jump
     Before Instruction                                                   Before Instruction
           PC              =        address (HERE)                              PC              =        address (HERE)
     After Instruction                                                    After Instruction
           If CARRY        =        0;                                          If NEGATIVE     =        0;
                PC         =        address (Jump)                                   PC         =        address (Jump)
           If CARRY        =        1;                                          If NEGATIVE     =        1;
                PC         =        address (HERE + 2)                               PC         =        address (HERE + 2)


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 674
                           PIC18(L)F26/27/45/46/47/55/56/57K42

BNOV                   Branch if Not Overflow                     BNZ                    Branch if Not Zero
Syntax:                BNOV       n                               Syntax:                BNZ      n
Operands:              -128  n  127                             Operands:              -128  n  127
Operation:             if OVERFLOW bit is ‘0’                     Operation:             if ZERO bit is ‘0’
                       (PC) + 2 + 2n  PC                                                (PC) + 2 + 2n  PC
Status Affected:       None                                       Status Affected:       None
Encoding:                  1110       0101     nnnn      nnnn     Encoding:                  1110        0001     nnnn      nnnn
Description:           If the OVERFLOW bit is ‘0’, then the       Description:           If the ZERO bit is ‘0’, then the program
                       program will branch.                                              will branch.
                       The 2’s complement number ‘2n’ is                                 The 2’s complement number ‘2n’ is
                       added to the PC. Since the PC will have                           added to the PC. Since the PC will have
                       incremented to fetch the next                                     incremented to fetch the next
                       instruction, the new address will be                              instruction, the new address will be
                       PC + 2 + 2n. This instruction is then a                           PC + 2 + 2n. This instruction is then a
                       2-cycle instruction.                                              2-cycle instruction.
Words:                 1                                          Words:                 1
Cycles:                1(2)                                       Cycles:                1(2)
Q Cycle Activity:                                                 Q Cycle Activity:
If Jump:                                                          If Jump:
             Q1            Q2             Q3             Q4                    Q1            Q2              Q3             Q4
          Decode      Read literal      Process    Write to PC              Decode      Read literal      Process      Write to PC
                         ‘n’             Data                                              ‘n’             Data
             No           No              No             No                    No           No               No             No
          operation    operation       operation      operation             operation    operation        operation      operation
If No Jump:                                                       If No Jump:
             Q1            Q2             Q3             Q4                    Q1            Q2              Q3             Q4
          Decode      Read literal      Process          No                 Decode      Read literal      Process           No
                         ‘n’             Data         operation                            ‘n’             Data          operation


Example:               HERE           BNOV Jump                   Example:               HERE            BNZ    Jump
     Before Instruction                                                Before Instruction
           PC           =         address (HERE)                             PC              =        address (HERE)
     After Instruction                                                 After Instruction
           If OVERFLOW =          0;                                         If ZERO         =        0;
                PC      =         address (Jump)                                  PC         =        address (Jump)
           If OVERFLOW =          1;                                         If ZERO         =        1;
                PC      =         address (HERE + 2)                              PC         =        address (HERE + 2)


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 675
                              PIC18(L)F26/27/45/46/47/55/56/57K42

BRA                   Unconditional Branch                                BSF                    Bit Set f
Syntax:               BRA      n                                          Syntax:                BSF      f, b {,a}
Operands:             -1024  n  1023                                    Operands:              0  f  255
                                                                                                 0b7
Operation:            (PC) + 2 + 2n  PC
                                                                                                 a [0,1]
Status Affected:      None
                                                                          Operation:             1  f[b>
Encoding:                  1101          0nnn        nnnn       nnnn
                                                                          Status Affected:       None
Description:          Add the 2’s complement number ‘2n’ to
                                                                          Encoding:                  1000       bbba         ffff        ffff
                      the PC. Since the PC will have incre-
                      mented to fetch the next instruction, the           Description:           Bit ‘b’ in register ‘f’ is set.
                      new address will be PC + 2 + 2n. This                                      If ‘a’ is ‘0’, the Access Bank is selected.
                      instruction is a 2-cycle instruction.                                      If ‘a’ is ‘1’, the BSR is used to select the
                                                                                                 GPR bank.
Words:                1
                                                                                                 If ‘a’ is ‘0’ and the extended instruction
Cycles:               2                                                                          set is enabled, this instruction operates
Q Cycle Activity:                                                                                in Indexed Literal Offset Addressing
                                                                                                 mode whenever f 95 (5Fh). See Sec-
             Q1               Q2                Q3              Q4
                                                                                                 tion 41.2.3 “Byte-Oriented and Bit-
          Decode          Read literal     Process          Write to PC                          Oriented Instructions in Indexed Lit-
                             ‘n’            Data                                                 eral Offset Mode” for details.
             No               No              No               No
                                                                          Words:                 1
          operation        operation       operation        operation
                                                                          Cycles:                1
                                                                          Q Cycle Activity:
Example:                   HERE           BRA    Jump
                                                                                       Q1            Q2                 Q3              Q4
     Before Instruction
                                                                                    Decode        Read                Process         Write
           PC                  =    address (HERE)
                                                                                                register ‘f’           Data         register ‘f’
     After Instruction
           PC                  =    address (Jump)
                                                                          Example:               BSF           FLAG_REG, 7, 1
                                                                                Before Instruction
                                                                                      FLAG_REG       =      0Ah
                                                                                After Instruction
                                                                                      FLAG_REG       =      8Ah


 2017-2021 Microchip Technology Inc.                                                                             DS40001919G-page 676
                           PIC18(L)F26/27/45/46/47/55/56/57K42

BTFSC                  Bit Test File, Skip if Clear                       BTFSS                  Bit Test File, Skip if Set
Syntax:                BTFSC f, b {,a}                                    Syntax:                BTFSS f, b {,a}
Operands:              0  f  255                                        Operands:              0  f  255
                       0b7                                                                     0b<7
                       a [0,1]                                                                 a [0,1]
Operation:             skip if (f<b>) = 0                                 Operation:             skip if (f<b>) = 1
Status Affected:       None                                               Status Affected:       None
Encoding:                  1011         bbba        ffff       ffff       Encoding:                   1010          bbba         ffff      ffff
Description:           If bit ‘b’ in register ‘f’ is ‘0’, then the next   Description:           If bit ‘b’ in register ‘f’ is ‘1’, then the next
                       instruction is skipped. If bit ‘b’ is ‘0’, then                           instruction is skipped. If bit ‘b’ is ‘1’, then
                       the next instruction fetched during the                                   the next instruction fetched during the
                       current instruction execution is discarded                                current instruction execution is discarded
                       and a NOP is executed instead, making                                     and a NOP is executed instead, making
                       this a 2-cycle instruction.                                               this a 2-cycle instruction.
                       If ‘a’ is ‘0’, the Access Bank is selected. If                            If ‘a’ is ‘0’, the Access Bank is selected. If
                       ‘a’ is ‘1’, the BSR is used to select the                                 ‘a’ is ‘1’, the BSR is used to select the
                       GPR bank.                                                                 GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction                                If ‘a’ is ‘0’ and the extended instruction
                       set is enabled, this instruction operates in                              set is enabled, this instruction operates
                       Indexed Literal Offset Addressing                                         in Indexed Literal Offset Addressing
                       mode whenever f 95 (5Fh).                                               mode whenever f 95 (5Fh).
                       See Section 41.2.3 “Byte-Oriented and                                     See Section 41.2.3 “Byte-Oriented and
                       Bit-Oriented Instructions in Indexed                                      Bit-Oriented Instructions in Indexed
                       Literal Offset Mode” for details.                                         Literal Offset Mode” for details.
Words:                 1                                                  Words:                 1
Cycles:                1(2)                                               Cycles:                1(2)
                       Note: 3 cycles if skip and followed                                       Note: 3 cycles if skip and followed
                             by a 2-word instruction. 4 cycles if                                      by a 2-word instruction. 4 cycles if
                             skip and followed by a 3-word                                             skip and followed by a 3-word
                             instruction.                                                              instruction.
Q Cycle Activity:                                                         Q Cycle Activity:
              Q1           Q2                 Q3              Q4                        Q1               Q2                 Q3             Q4
           Decode        Read             Process             No                     Decode            Read            Process             No
                       register ‘f’        Data            operation                                 register ‘f’       Data            operation
If skip:                                                                  If skip:
              Q1           Q2                 Q3              Q4                        Q1               Q2                Q3              Q4
              No          No                No                No                        No              No               No                No
           operation   operation         operation         operation                 operation       operation        operation         operation
If skip and followed by 2-word instruction:                               If skip and followed by 2-word instruction:
              Q1           Q2                 Q3              Q4                        Q1               Q2                Q3              Q4
              No          No                No                No                        No              No               No                No
           operation   operation         operation         operation                 operation       operation        operation         operation
              No          No                No                No                        No              No               No                No
           operation   operation         operation         operation                 operation       operation        operation         operation


Example:               HERE           BTFSC        FLAG, 1, 0             Example:                   HERE           BTFSS        FLAG, 1, 0
                       FALSE          :                                                              FALSE          :
                       TRUE           :                                                              TRUE           :
     Before Instruction                                                        Before Instruction
           PC              =      address (HERE)                                     PC                  =      address (HERE)
     After Instruction                                                         After Instruction
           If FLAG<1>      =      0;                                                 If FLAG<1>          =      0;
                PC         =      address (TRUE)                                          PC             =      address (FALSE)
           If FLAG<1>      =      1;                                                 If FLAG<1>          =      1;
                PC         =      address (FALSE)                                         PC             =      address (TRUE)


 2017-2021 Microchip Technology Inc.                                                                                 DS40001919G-page 677
                        PIC18(L)F26/27/45/46/47/55/56/57K42

BTG                 Bit Toggle f                                   BOV                    Branch if Overflow
Syntax:             BTG f, b {,a}                                  Syntax:                BOV      n
Operands:           0  f  255                                    Operands:              -128  n  127
                    0b7
                                                                   Operation:             if OVERFLOW bit is ‘1’
                    a [0,1]
                                                                                          (PC) + 2 + 2n  PC
Operation:          (f<b>)  f<b>
                                                                   Status Affected:       None
Status Affected:    None                                           Encoding:                  1110       0100      nnnn      nnnn
Encoding:               0111         bbba       ffff     ffff      Description:           If the OVERFLOW bit is ‘1’, then the
Description:        Bit ‘b’ in data memory location ‘f’ is                                program will branch.
                    inverted.                                                             The 2’s complement number ‘2n’ is
                    If ‘a’ is ‘0’, the Access Bank is selected.                           added to the PC. Since the PC will have
                    If ‘a’ is ‘1’, the BSR is used to select the                          incremented to fetch the next
                    GPR bank.                                                             instruction, the new address will be
                    If ‘a’ is ‘0’ and the extended instruction                            PC + 2 + 2n. This instruction is then a
                    set is enabled, this instruction operates                             2-cycle instruction.
                    in Indexed Literal Offset Addressing           Words:                 1
                    mode whenever f 95 (5Fh). See Sec-
                    tion 41.2.3 “Byte-Oriented and Bit-            Cycles:                1(2)
                    Oriented Instructions in Indexed Lit-          Q Cycle Activity:
                    eral Offset Mode” for details.                 If Jump:
Words:              1                                                           Q1            Q2              Q3             Q4
Cycles:             1                                                        Decode      Read literal      Process      Write to PC
                                                                                            ‘n’             Data
Q Cycle Activity:
                                                                                No           No               No             No
             Q1         Q2              Q3              Q4                   operation    operation        operation      operation
          Decode      Read            Process         Write        If No Jump:
                    register ‘f’       Data         register ‘f’
                                                                                Q1            Q2              Q3             Q4
                                                                             Decode      Read literal      Process           No
Example:            BTG            PORTC,    4, 0                                           ‘n’             Data          operation
     Before Instruction:
           PORTC =       0111 0101 [75h]
                                                                   Example:               HERE            BOV   Jump
     After Instruction:
           PORTC =       0110 0101 [65h]                                Before Instruction
                                                                              PC           =           address (HERE)
                                                                        After Instruction
                                                                              If OVERFLOW =            1;
                                                                                   PC      =           address (Jump)
                                                                              If OVERFLOW =            0;
                                                                                   PC      =           address (HERE + 2)


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 678
                           PIC18(L)F26/27/45/46/47/55/56/57K42

BZ                     Branch if Zero                               CALL                   Subroutine Call
Syntax:                BZ       n                                   Syntax:                CALL k {,s}
Operands:              -128  n  127                               Operands:              0  k  1048575
                                                                                           s [0,1]
Operation:             if ZERO bit is ‘1’
                       (PC) + 2 + 2n  PC                           Operation:             (PC) + 4  TOS,
                                                                                           k  PC<20:1>,
Status Affected:       None
                                                                                           if s = 1
Encoding:                  1110       0000       nnnn      nnnn                            (W)  WREG_CSHAD,
Description:           If the ZERO bit is ‘1’, then the program                            (Status)  STATUS_CSHAD,
                       will branch.                                                        (BSR)  BSR_CSHAD
                       The 2’s complement number ‘2n’ is            Status Affected:       None
                       added to the PC. Since the PC will
                       have incremented to fetch the next           Encoding:
                                                                    1st word (k<7:0>)          1110    110s       k7kkk     kkkk0
                       instruction, the new address will be
                                                                    2nd word(k<19:8>)          1111   k19kkk      kkkk      kkkk8
                       PC + 2 + 2n. This instruction is then a
                       2-cycle instruction.                         Description:           Subroutine call of entire 2-Mbyte
                                                                                           memory range. First, return address
Words:                 1
                                                                                           (PC + 4) is pushed onto the return
Cycles:                1(2)                                                                stack. If ‘s’ = 1, the W, Status and BSR
Q Cycle Activity:                                                                          registers are also pushed into their
If Jump:                                                                                   respective shadow registers,
                                                                                           WREG_CSHAD, STATUS_CSHAD and
             Q1             Q2              Q3             Q4
                                                                                           BSR_CSHAD. If ‘s’ = 0, no update
          Decode      Read literal      Process      Write to PC                           occurs (default). Then, the
                         ‘n’             Data                                              20-bit value ‘k’ is loaded into PC<20:1>.
             No           No               No              No                              CALL is a 2-cycle instruction.
          operation    operation        operation       operation
                                                                    Words:                 2
If No Jump:
                                                                    Cycles:                2
             Q1             Q2              Q3             Q4
          Decode      Read literal      Process            No       Q Cycle Activity:
                         ‘n’             Data           operation                Q1            Q2            Q3            Q4
                                                                              Decode      Read literal PUSH PC to      Read literal
Example:               HERE            BZ    Jump                                          ‘k’<7:0>,     stack          ‘k’<19:8>,
                                                                                                                       Write to PC
     Before Instruction
           PC               =       address (HERE)                               No          No             No             No
     After Instruction                                                        operation   operation      operation      operation
           If ZERO          =       1;
                PC          =       address (Jump)
           If ZERO          =       0;                              Example:               HERE        CALL       THERE, 1
                PC          =       address (HERE + 2)
                                                                         Before Instruction
                                                                              PC         =  address (HERE)
                                                                      After Instruction
                                                                              PC                = address (THERE)
                                                                              TOS               = address (HERE + 4)
                                                                              WREG_CSHAD = W
                                                                              BSR_CSHAD         = BSR
                                                                              STATUS_CSHAD = Status


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 679
                           PIC18(L)F26/27/45/46/47/55/56/57K42

                                                                CLRF                  Clear f
CALLW                 Subroutine Call Using WREG
                                                                Syntax:               CLRF       f {,a}
Syntax:               CALLW
                                                                Operands:             0  f  255
Operands:             None                                                            a [0,1]
Operation:            (PC + 2)  TOS,                           Operation:            000h  f
                      (W)  PCL,                                                      1Z
                      (PCLATH)  PCH,
                                                                Status Affected:      Z
                      (PCLATU)  PCU
                                                                Encoding:                 0110        101a       ffff        ffff
Status Affected:      None
                                                                Description:          Clears the contents of the specified
Encoding:                 0000     0000     0001     0100
                                                                                      register.
Description           First, the return address (PC + 2) is                           If ‘a’ is ‘0’, the Access Bank is selected.
                      pushed onto the return stack. Next, the                         If ‘a’ is ‘1’, the BSR is used to select the
                      contents of W are written to PCL; the                           GPR bank.
                      existing value is discarded. Then, the                          If ‘a’ is ‘0’ and the extended instruction
                      contents of PCLATH and PCLATU are                               set is enabled, this instruction operates
                      latched into PCH and PCU,                                       in Indexed Literal Offset Addressing
                      respectively. The second cycle is                               mode whenever f 95 (5Fh). See Sec-
                      executed as a NOP instruction while the                         tion 41.2.3 “Byte-Oriented and Bit-
                      new next instruction is fetched.                                Oriented Instructions in Indexed Lit-
                      Unlike CALL, there is no option to                              eral Offset Mode” for details.
                      update W, Status or BSR.
                                                                Words:                1
Words:                1
                                                                Cycles:               1
Cycles:               2
                                                                Q Cycle Activity:
Q Cycle Activity:
                                                                             Q1           Q2                Q3              Q4
                           Q1       Q2       Q3        Q4                 Decode       Read               Process         Write
                          Decode   Read PUSH PC     No                               register ‘f’          Data         register ‘f’
                                   WREG to stack operation
                         No       No      No        No          Example:              CLRF             FLAG_REG, 1
                      operation opera- operation operation           Before Instruction
                                 tion                                      FLAG_REG       =      5Ah
                                                                     After Instruction
                                                                           FLAG_REG       =      00h
Example:              HERE         CALLW
     Before Instruction
           PC         =    address (HERE)
           PCLATH =        10h
           PCLATU =        00h
           W          =    06h
     After Instruction
           PC         =    001006h
           TOS        =    address (HERE + 2)
           PCLATH =        10h
           PCLATU =        00h
           W          =    06h


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 680
                        PIC18(L)F26/27/45/46/47/55/56/57K42

CLRWDT              Clear Watchdog Timer                        COMF                  Complement f
Syntax:             CLRWDT                                      Syntax:               COMF          f {,d {,a}}
Operands:           None                                        Operands:             0  f  255
                                                                                      d  [0,1]
Operation:          000h  WDT,
                                                                                      a  [0,1]
                    000h  WDT postscaler,
                    1  TO,                                     Operation:            (f)  dest
                    1  PD                                      Status Affected:      N, Z
Status Affected:    TO, PD
                                                                Encoding:                 0001         11da       ffff   ffff
Encoding:               0000       0000      0000      0100     Description:          The contents of register ‘f’ are
Description:        CLRWDT instruction resets the                                     complemented. If ‘d’ is ‘0’, the result is
                    Watchdog Timer. It also resets the post-                          stored in W. If ‘d’ is ‘1’, the result is
                    scaler of the WDT. Status bits, TO and                            stored back in register ‘f’ (default).
                    PD, are set.                                                      If ‘a’ is ‘0’, the Access Bank is selected.
                                                                                      If ‘a’ is ‘1’, the BSR is used to select the
Words:              1
                                                                                      GPR bank.
Cycles:             1                                                                 If ‘a’ is ‘0’ and the extended instruction
Q Cycle Activity:                                                                     set is enabled, this instruction operates
                                                                                      in Indexed Literal Offset Addressing
             Q1         Q2              Q3             Q4
                                                                                      mode whenever f 95 (5Fh). See Sec-
          Decode       No           Process            No                             tion 41.2.3 “Byte-Oriented and Bit-
                    operation        Data           operation                         Oriented Instructions in Indexed Lit-
                                                                                      eral Offset Mode” for details.
Example:            CLRWDT                                      Words:                1
     Before Instruction                                         Cycles:               1
           WDT Counter         =    ?
                                                                Q Cycle Activity:
     After Instruction
           WDT Counter         =    00h                                      Q1           Q2                 Q3          Q4
           WDT Postscaler      =    0                                     Decode       Read               Process     Write to
           TO                  =    1                                                register ‘f’          Data      destination
           PD                  =    1

                                                                Example:              COMF             REG, 0, 0
                                                                     Before Instruction
                                                                           REG        =   13h
                                                                     After Instruction
                                                                           REG        =   13h
                                                                           W          =   ECh


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 681
                          PIC18(L)F26/27/45/46/47/55/56/57K42

CPFSEQ                Compare f with W, skip if f = W                 CPFSGT                Compare f with W, skip if f > W
Syntax:               CPFSEQ         f {,a}                           Syntax:               CPFSGT         f {,a}
Operands:             0  f  255                                     Operands:             0  f  255
                      a  [0,1]                                                             a  [0,1]
Operation:            (f) – (W),                                      Operation:            (f) –W),
                      skip if (f) = (W)                                                     skip if (f) > (W)
                      (unsigned comparison)                                                 (unsigned comparison)
Status Affected:      None                                            Status Affected:      None
Encoding:                 0110       001a          ffff      ffff     Encoding:                 0110       010a     ffff       ffff
Description:          Compares the contents of data memory            Description:          Compares the contents of data memory
                      location ‘f’ to the contents of W by                                  location ‘f’ to the contents of the W by
                      performing an unsigned subtraction.                                   performing an unsigned subtraction.
                      If ‘f’ = W, then the fetched instruction is                           If the contents of ‘f’ are greater than the
                      discarded and a NOP is executed                                       contents of WREG, then the fetched
                      instead, making this a 2-cycle                                        instruction is discarded and a NOP is
                      instruction.                                                          executed instead, making this a
                      If ‘a’ is ‘0’, the Access Bank is selected.                           2-cycle instruction.
                      If ‘a’ is ‘1’, the BSR is used to select the                          If ‘a’ is ‘0’, the Access Bank is selected.
                      GPR bank.                                                             If ‘a’ is ‘1’, the BSR is used to select the
                      If ‘a’ is ‘0’ and the extended instruction                            GPR bank.
                      set is enabled, this instruction operates                             If ‘a’ is ‘0’ and the extended instruction
                      in Indexed Literal Offset Addressing                                  set is enabled, this instruction operates
                      mode whenever f 95 (5Fh). See Sec-                                  in Indexed Literal Offset Addressing
                      tion 41.2.3 “Byte-Oriented and Bit-                                   mode whenever f 95 (5Fh). See Sec-
                      Oriented Instructions in Indexed Lit-                                 tion 41.2.3 “Byte-Oriented and Bit-
                      eral Offset Mode” for details.                                        Oriented Instructions in Indexed Lit-
Words:                1                                                                     eral Offset Mode” for details.
Cycles:               1(2)                                            Words:                1
                      Note: 3 cycles if skip and followed             Cycles:               1(2)
                            by a 2-word instruction. 4                                      Note: 3 cycles if skip and followed
                            cycles if skip and followed by a                                      by a 2-word instruction.
                            3-word instruction.                       Q Cycle Activity:
Q Cycle Activity:                                                                  Q1          Q2               Q3            Q4
             Q1           Q2                  Q3             Q4                  Decode       Read            Process         No
           Decode       Read            Process              No                             register ‘f’       Data        operation
                      register ‘f’       Data             operation   If skip:
If skip:                                                                         Q1            Q2             Q3              Q4
           Q1            Q2             Q3                   Q4                  No            No             No              No
           No            No             No                   No               operation     operation     operation        operation
        operation     operation     operation             operation   If skip and followed by 2-word instruction:
If skip and followed by 2-word instruction:                                      Q1            Q2             Q3              Q4
           Q1            Q2             Q3                   Q4                  No            No             No              No
           No            No             No                   No               operation     operation     operation        operation
        operation     operation     operation             operation              No            No             No              No
           No            No             No                   No               operation     operation     operation        operation
        operation     operation     operation             operation
                                                                      Example:              HERE             CPFSGT REG, 0
Example:              HERE           CPFSEQ REG, 0
                                                                                            NGREATER         :
                      NEQUAL         :
                                                                                            GREATER          :
                      EQUAL          :
                                                                           Before Instruction
     Before Instruction
                                                                                 PC             =      Address (HERE)
           PC Address     =      Address (HERE)
                                                                                 W              =      ?
           W              =      ?
                                                                           After Instruction
           REG            =      ?
     After Instruction                                                            If REG              W;
                                                                                       PC       =      Address (GREATER)
            If REG        =      W;
                 PC       =      Address (EQUAL)                                  If REG              W;
                                                                                       PC       =      Address (NGREATER)
            If REG              W;
                 PC       =      Address (NEQUAL)


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 682
                           PIC18(L)F26/27/45/46/47/55/56/57K42

CPFSLT                 Compare f with W, skip if f < W                 DAW                       Decimal Adjust W Register
Syntax:                CPFSLT         f {,a}                           Syntax:                   DAW
Operands:              0  f  255                                     Operands:                 None
                       a  [0,1]
                                                                       Operation:                If (W<3:0>) > 9] or [DC = 1] then
Operation:             (f) –W),                                                                (W<3:0>) + 6  W<3:0>;
                       skip if (f) < (W)                                                         else
                       (unsigned comparison)                                                     (W<3:0>)  W[3:0>;
Status Affected:       None
                                                                                                 If [(W<7:4>) + DC > 9] or [C = 1] then
Encoding:                  0110        000a         ffff      ffff                               (W<7:4>) + 6 + DC  W<7:4>;
Description:           Compares the contents of data memory                                      else
                       location ‘f’ to the contents of W by                                      (W<7:4>) + DC  W<7:4>
                       performing an unsigned subtraction.             Status Affected:          C
                       If the contents of ‘f’ are less than the
                       contents of W, then the fetched                 Encoding:                     0000    0000       0000      0111
                       instruction is discarded and a NOP is           Description:              DAW adjusts the 8-bit value in W, result-
                       executed instead, making this a                                           ing from the earlier addition of two vari-
                       2-cycle instruction.                                                      ables (each in packed BCD format) and
                       If ‘a’ is ‘0’, the Access Bank is selected.                               produces a correct packed BCD result.
                       If ‘a’ is ‘1’, the BSR is used to select the    Words:                    1
                       GPR bank.
                                                                       Cycles:                   1
Words:                 1
                                                                       Q Cycle Activity:
Cycles:                1(2)
                       Note:      3 cycles if skip and followed                     Q1               Q2           Q3             Q4
                                  by a 2-word instruction. 4                     Decode        Read             Process         Write
                                  cycles if skip and followed by a                           register W          Data            W
                                  3-word instruction.                  Example1:
Q Cycle Activity:                                                                                DAW
              Q1           Q2                  Q3             Q4            Before Instruction
           Decode        Read             Process             No                  W          =       A5h
                       register ‘f’        Data            operation              C          =       0
                                                                                  DC         =       0
If skip:
                                                                            After Instruction
              Q1           Q2                  Q3             Q4
                                                                                W           =        05h
              No          No                No                No                C           =        1
           operation   operation         operation         operation            DC          =        0
If skip and followed by 2-word instruction:                            Example 2:
              Q1           Q2                  Q3             Q4            Before Instruction
              No          No                No                No                  W          =       CEh
           operation   operation         operation         operation              C          =       0
                                                                                  DC         =       0
              No          No                No                No            After Instruction
           operation   operation         operation         operation
                                                                                   W        =        34h
                                                                                   C        =        1
Example:               HERE           CPFSLT REG, 1                                DC       =        0
                       NLESS          :
                       LESS           :
     Before Instruction
           PC              =      Address (HERE)
           W               =      ?
     After Instruction
             If REG        <      W;
             PC            =      Address (LESS)
             If REG              W;
             PC            =      Address (NLESS)


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 683
                          PIC18(L)F26/27/45/46/47/55/56/57K42

DECF                  Decrement f                                    DECFSZ                Decrement f, skip if 0
Syntax:               DECF f {,d {,a}}                               Syntax:               DECFSZ f {,d {,a}}
Operands:             0  f  255                                    Operands:             0  f  255
                      d  [0,1]                                                            d  [0,1]
                      a  [0,1]                                                            a  [0,1]
Operation:            (f) – 1  dest                                 Operation:            (f) – 1  dest,
                                                                                           skip if result = 0
Status Affected:      C, DC, N, OV, Z
                                                                     Status Affected:      None
Encoding:                 0000       01da       ffff     ffff
                                                                     Encoding:                 0010       11da       ffff       ffff
Description:          Decrement register ‘f’. If ‘d’ is ‘0’, the
                      result is stored in W. If ‘d’ is ‘1’, the      Description:          The contents of register ‘f’ are
                      result is stored back in register ‘f’                                decremented. If ‘d’ is ‘0’, the result is
                      (default).                                                           placed in W. If ‘d’ is ‘1’, the result is
                      If ‘a’ is ‘0’, the Access Bank is selected.                          placed back in register ‘f’ (default).
                      If ‘a’ is ‘1’, the BSR is used to select the                         If the result is ‘0’, the next instruction,
                      GPR bank.                                                            which is already fetched, is discarded
                      If ‘a’ is ‘0’ and the extended instruction                           and a NOP is executed instead, making
                      set is enabled, this instruction operates                            it a 2-cycle instruction.
                      in Indexed Literal Offset Addressing                                 If ‘a’ is ‘0’, the Access Bank is selected.
                      mode whenever f 95 (5Fh). See Sec-                                 If ‘a’ is ‘1’, the BSR is used to select the
                      tion 41.2.3 “Byte-Oriented and Bit-                                  GPR bank.
                      Oriented Instructions in Indexed Lit-                                If ‘a’ is ‘0’ and the extended instruction
                      eral Offset Mode” for details.                                       set is enabled, this instruction operates
                                                                                           in Indexed Literal Offset Addressing
Words:                1
                                                                                           mode whenever f 95 (5Fh). See Sec-
Cycles:               1                                                                    tion 41.2.3 “Byte-Oriented and Bit-
Q Cycle Activity:                                                                          Oriented Instructions in Indexed Lit-
                                                                                           eral Offset Mode” for details.
             Q1           Q2               Q3           Q4
          Decode       Read            Process       Write to        Words:                1
                     register ‘f’       Data        destination      Cycles:               1(2)
                                                                                           Note:      3 cycles if skip and followed
                                                                                                      by a 2-word instruction. 4
Example:              DECF          CNT,    1, 0
                                                                                                      cycles if skip and followed by a
     Before Instruction                                                                               3-word instruction.
           CNT        =   01h
           Z          =   0                                          Q Cycle Activity:
     After Instruction                                                            Q1           Q2               Q3              Q4
           CNT        =   00h                                                   Decode      Read            Process          Write to
           Z          =   1
                                                                                          register ‘f’       Data           destination
                                                                     If skip:
                                                                                 Q1            Q2               Q3             Q4
                                                                                 No          No               No               No
                                                                              operation   operation        operation        operation
                                                                     If skip and followed by 2-word instruction:
                                                                                 Q1            Q2               Q3             Q4
                                                                                 No          No               No               No
                                                                              operation   operation        operation        operation
                                                                                 No          No               No               No
                                                                              operation   operation        operation        operation

                                                                     Example:              HERE            DECFSZ       CNT, 1, 1
                                                                                                           GOTO         LOOP
                                                                                           CONTINUE
                                                                          Before Instruction
                                                                                PC         =   Address (HERE)
                                                                          After Instruction
                                                                                CNT        =   CNT - 1
                                                                                If CNT     =   0;
                                                                                     PC =      Address (CONTINUE)
                                                                                If CNT        0;
                                                                                     PC =      Address (HERE + 2)


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 684
                           PIC18(L)F26/27/45/46/47/55/56/57K42

DCFSNZ                 Decrement f, skip if not 0                        GOTO                   Unconditional Branch
Syntax:                DCFSNZ         f {,d {,a}}                        Syntax:                GOTO k
Operands:              0  f  255
                                                                         Operands:              0  k  1048575
                       d  [0,1]
                       a  [0,1]                                         Operation:             k  PC<20:1>
Operation:             (f) – 1  dest,                                   Status Affected:       None
                       skip if result  0
                                                                         Encoding:
Status Affected:       None                                              1st word (k[7:0>)          1110       1111     k7kkk   kkkk0
Encoding:                  0100        11da         ffff       ffff      2nd word(k[19:8>)          1111      k19kkk    kkkk    kkkk8
Description:           The contents of register ‘f’ are                  Description:           GOTO allows an unconditional branch
                       decremented. If ‘d’ is ‘0’, the result is
                                                                                                anywhere within entire
                       placed in W. If ‘d’ is ‘1’, the result is                                2-Mbyte memory range. The 20-bit
                       placed back in register ‘f’ (default).                                   value ‘k’ is loaded into PC<20:1>.
                       If the result is not ‘0’, the next
                                                                                                GOTO is always a 2-cycle
                       instruction, which is already fetched, is                                instruction.
                       discarded and a NOP is executed
                       instead, making it a 2-cycle                      Words:                 2
                       instruction.                                      Cycles:                2
                       If ‘a’ is ‘0’, the Access Bank is selected.
                                                                         Q Cycle Activity:
                       If ‘a’ is ‘1’, the BSR is used to select the
                       GPR bank.                                                      Q1            Q2             Q3           Q4
                       If ‘a’ is ‘0’ and the extended instruction                  Decode      Read literal        No       Read literal
                       set is enabled, this instruction operates                                ‘k’<7:0>,       operation    ‘k’<19:8>,
                       in Indexed Literal Offset Addressing                                                                 Write to PC
                       mode whenever f 95 (5Fh). See Sec-                           No           No              No           No
                       tion 41.2.3 “Byte-Oriented and Bit-                         operation    operation       operation    operation
                       Oriented Instructions in Indexed Lit-
                       eral Offset Mode” for details.
                                                                         Example:               GOTO THERE
Words:                 1
Cycles:                1(2)                                                   After Instruction
                       Note:      3 cycles if skip and followed                     PC =       Address (THERE)
                                  by a 2-word instruction. 4
                                  cycles if skip and followed by a
                                  3-word instruction.
Q Cycle Activity:
              Q1           Q2               Q3                 Q4
           Decode        Read            Process            Write to
                       register ‘f’       Data             destination
If skip:
              Q1           Q2               Q3                 Q4
              No          No               No                 No
           operation   operation        operation          operation
If skip and followed by 2-word instruction:
              Q1           Q2               Q3                 Q4
              No          No               No                 No
           operation   operation        operation          operation
              No          No               No                 No
           operation   operation        operation          operation

Example:               HERE           DCFSNZ        TEMP, 1, 0
                       ZERO           :
                       NZERO          :
     Before Instruction
           TEMP                   =     ?
     After Instruction
           TEMP                   =     TEMP – 1,
           If TEMP                =     0;
                PC                =     Address (ZERO)
           If TEMP                     0;
                PC                =     Address (NZERO)


 2017-2021 Microchip Technology Inc.                                                                           DS40001919G-page 685
                          PIC18(L)F26/27/45/46/47/55/56/57K42

INCF                  Increment f                                    INCFSZ                 Increment f, skip if 0
Syntax:               INCF       f {,d {,a}}                         Syntax:                INCFSZ         f {,d {,a}}
Operands:             0  f  255                                    Operands:              0  f  255
                      d  [0,1]                                                             d  [0,1]
                      a  [0,1]                                                             a  [0,1]
Operation:            (f) + 1  dest                                 Operation:             (f) + 1  dest,
                                                                                            skip if result = 0
Status Affected:      C, DC, N, OV, Z
                                                                     Status Affected:       None
Encoding:                 0010        10da          ffff   ffff
                                                                     Encoding:                  0011         11da        ffff      ffff
Description:          The contents of register ‘f’ are
                      incremented. If ‘d’ is ‘0’, the result is      Description:           The contents of register ‘f’ are
                      placed in W. If ‘d’ is ‘1’, the result is                             incremented. If ‘d’ is ‘0’, the result is
                      placed back in register ‘f’ (default).                                placed in W. If ‘d’ is ‘1’, the result is
                      If ‘a’ is ‘0’, the Access Bank is selected.                           placed back in register ‘f’ (default).
                      If ‘a’ is ‘1’, the BSR is used to select the                          If the result is ‘0’, the next instruction,
                      GPR bank.                                                             which is already fetched, is discarded
                      If ‘a’ is ‘0’ and the extended instruction                            and a NOP is executed instead, making
                      set is enabled, this instruction operates                             it a 2-cycle instruction.
                      in Indexed Literal Offset Addressing                                  If ‘a’ is ‘0’, the Access Bank is selected.
                      mode whenever f 95 (5Fh). See Sec-                                  If ‘a’ is ‘1’, the BSR is used to select the
                      tion 41.2.3 “Byte-Oriented and Bit-                                   GPR bank.
                      Oriented Instructions in Indexed Lit-                                 If ‘a’ is ‘0’ and the extended instruction
                      eral Offset Mode” for details.                                        set is enabled, this instruction operates
                                                                                            in Indexed Literal Offset Addressing
Words:                1
                                                                                            mode whenever f 95 (5Fh). See Sec-
Cycles:               1                                                                     tion 41.2.3 “Byte-Oriented and Bit-
Q Cycle Activity:                                                                           Oriented Instructions in Indexed Lit-
                                                                                            eral Offset Mode” for details.
             Q1           Q2                   Q3          Q4
          Decode       Read              Process        Write to     Words:                 1
                     register ‘f’         Data         destination   Cycles:                1(2)
                                                                                            Note:      3 cycles if skip and followed
                                                                                                       by a 2-word instruction. 4
Example:              INCF            CNT, 1, 0
                                                                                                       cycles if skip and followed by a
     Before Instruction                                                                                3-word instruction.
           CNT        =    FFh
           Z          =    0                                         Q Cycle Activity:
           C          =    ?                                                       Q1           Q2                 Q3              Q4
           DC         =    ?
     After Instruction                                                          Decode        Read             Process       Write to
           CNT        =    00h                                                              register ‘f’        Data        destination
           Z          =    1                                         If skip:
           C          =    1
           DC         =    1                                                       Q1           Q2                 Q3              Q4
                                                                                   No          No                 No               No
                                                                                operation   operation          operation        operation
                                                                     If skip and followed by 2-word instruction:
                                                                                   Q1           Q2                 Q3              Q4
                                                                                   No          No                 No               No
                                                                                operation   operation          operation        operation
                                                                                   No          No                 No               No
                                                                                operation   operation          operation        operation

                                                                     Example:               HERE           INCFSZ        CNT, 1, 0
                                                                                            NZERO          :
                                                                                            ZERO           :
                                                                          Before Instruction
                                                                                PC         =    Address (HERE)
                                                                          After Instruction
                                                                                CNT        =    CNT + 1
                                                                                If CNT     =    0;
                                                                                PC         =    Address (ZERO)
                                                                                If CNT         0;
                                                                                PC         =    Address (NZERO)


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 686
                           PIC18(L)F26/27/45/46/47/55/56/57K42

INFSNZ                 Increment f, skip if not 0                      IORLW                     Inclusive OR literal with W
Syntax:                INFSNZ         f {,d {,a}}                      Syntax:                   IORLW k
Operands:              0  f  255                                     Operands:                 0  k  255
                       d  [0,1]
                       a  [0,1]                                       Operation:                (W) .OR. k  W

Operation:             (f) + 1  dest,                                 Status Affected:          N, Z
                       skip if result  0                              Encoding:                     0000      1001     kkkk       kkkk
Status Affected:       None                                            Description:              The contents of W are ORed with the 8-
Encoding:                  0100         10da        ffff       ffff                              bit literal ‘k’. The result is placed in W.
Description:           The contents of register ‘f’ are                Words:                    1
                       incremented. If ‘d’ is ‘0’, the result is
                                                                       Cycles:                   1
                       placed in W. If ‘d’ is ‘1’, the result is
                       placed back in register ‘f’ (default).          Q Cycle Activity:
                       If the result is not ‘0’, the next                           Q1               Q2            Q3             Q4
                       instruction, which is already fetched, is                 Decode             Read        Process       Write to W
                       discarded and a NOP is executed
                                                                                                 literal ‘k’     Data
                       instead, making it a 2-cycle
                       instruction.
                       If ‘a’ is ‘0’, the Access Bank is selected.     Example:                  IORLW         35h
                       If ‘a’ is ‘1’, the BSR is used to select the         Before Instruction
                       GPR bank.
                                                                                  W          =       9Ah
                       If ‘a’ is ‘0’ and the extended instruction
                       set is enabled, this instruction operates            After Instruction
                       in Indexed Literal Offset Addressing                        W        =        BFh
                       mode whenever f 95 (5Fh). See Sec-
                       tion 41.2.3 “Byte-Oriented and Bit-
                       Oriented Instructions in Indexed Lit-
                       eral Offset Mode” for details.
Words:                 1
Cycles:                1(2)
                       Note:      3 cycles if skip and followed
                                  by a 2-word instruction. 4
                                  cycles if skip and followed by a
                                  3-word instruction.
Q Cycle Activity:
              Q1           Q2                 Q3              Q4
           Decode        Read             Process        Write to
                       register ‘f’        Data         destination
If skip:
              Q1           Q2                 Q3              Q4
              No          No                 No               No
           operation   operation          operation        operation
If skip and followed by 2-word instruction:
              Q1           Q2                 Q3              Q4
          No              No                No                No
       operation       operation         operation         operation
          No              No                No                No
       operation       operation         operation         operation

Example:               HERE           INFSNZ        REG, 1, 0
                       ZERO
                       NZERO
     Before Instruction
           PC         =    Address (HERE)
     After Instruction
           REG        =    REG + 1
           If REG         0;
           PC         =    Address (NZERO)
           If REG     =    0;
           PC         =    Address (ZERO)


 2017-2021 Microchip Technology Inc.                                                                           DS40001919G-page 687
                          PIC18(L)F26/27/45/46/47/55/56/57K42

IORWF                 Inclusive OR W with f                            LFSR                     Load FSR
Syntax:               IORWF         f {,d {,a}}                        Syntax:                  LFSR f, k
Operands:             0  f  255                                      Operands:                0f2
                      d  [0,1]                                                                 0  k  16383
                      a  [0,1]
                                                                       Operation:               k  FSRf
Operation:           (W) .OR. (f)  dest
                                                                       Status Affected:         None
Status Affected:      N, Z                                             Encoding:                    1110     1110       00ff      k13kkk
Encoding:                 0001        00da        ffff     ffff                                     1111    00k9k8      kkkk       kkkk
Description:          Inclusive OR W with register ‘f’. If ‘d’ is      Description:             The 14-bit literal ‘k’ is loaded into the
                      ‘0’, the result is placed in W. If ‘d’ is ‘1’,                            File Select Register pointed to by ‘f’.
                      the result is placed back in register ‘f’
                                                                       Words:                   2
                      (default).
                      If ‘a’ is ‘0’, the Access Bank is selected.      Cycles:                  2
                      If ‘a’ is ‘1’, the BSR is used to select the     Q Cycle Activity:
                      GPR bank.
                                                                                    Q1              Q2             Q3             Q4
                      If ‘a’ is ‘0’ and the extended instruction
                      set is enabled, this instruction operates                  Decode     Read literal         Process          Write
                      in Indexed Literal Offset Addressing                                   ‘k’ MSB              Data         literal ‘k’
                      mode whenever f 95 (5Fh). See Sec-                                                                      MSB to
                      tion 41.2.3 “Byte-Oriented and Bit-                                                                       FSRfH
                      Oriented Instructions in Indexed Lit-                      Decode     Read literal         Process     Write literal
                      eral Offset Mode” for details.                                         ‘k’ LSB              Data       ‘k’ to FSRfL
Words:                1
Cycles:               1                                                Example:                 LFSR 2, 3ABh
                                                                            After Instruction
Q Cycle Activity:
                                                                                  FSR2H             =      03h
             Q1           Q2                Q3            Q4                      FSR2L             =      ABh
          Decode       Read             Process       Write to
                     register ‘f’        Data        destination


Example:              IORWF         RESULT, 0, 1
     Before Instruction
           RESULT =       13h
           W          =   91h
     After Instruction
           RESULT =       13h
           W          =   93h


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 688
                          PIC18(L)F26/27/45/46/47/55/56/57K42

MOVF                  Move f                                         MOVFF                 Move f to f
Syntax:               MOVF       f {,d {,a}}                         Syntax:               MOVFF fs,fd
Operands:             0  f  255                                    Operands:             0  fs  4095
                      d  [0,1]                                                            0  fd  4095
                      a  [0,1]
                                                                     Operation:            (fs)  fd
Operation:            (f)  dest
                                                                     Status Affected:      None
Status Affected:      N, Z
                                                                     Encoding:
Encoding:                 0101        00da      ffff     ffff        1st word (source)         1100       ffff       ffff       ffffs
Description:          The contents of register ‘f’ are moved to      2nd word (destin.)        1111       ffff       ffff       ffffd
                      a destination dependent upon the               Description:         The contents of source register ‘fs’ are
                      status of ‘d’. If ‘d’ is ‘0’, the result is                         moved to destination register ‘fd’.
                      placed in W. If ‘d’ is ‘1’, the result is                           Location of source ‘fs’ can be anywhere
                      placed back in register ‘f’ (default).                              in the 4096-byte data space (000h to
                      Location ‘f’ can be anywhere in the                                 FFFh) and location of destination ‘fd’
                      256-byte bank.                                                      can also be anywhere from 000h to
                      If ‘a’ is ‘0’, the Access Bank is selected.                         FFFh.
                      If ‘a’ is ‘1’, the BSR is used to select the                        MOVFF has curtailed the
                      GPR bank.                                                           source and destination range to the
                      If ‘a’ is ‘0’ and the extended instruction                          lower 4 Kbyte space of memory (Banks
                      set is enabled, this instruction operates                           1 through 15). For everything else, use
                      in Indexed Literal Offset Addressing                                MOVFFL.
                      mode whenever f 95 (5Fh). See Sec-           Words:                2
                      tion 41.2.3 “Byte-Oriented and Bit-
                      Oriented Instructions in Indexed Lit-          Cycles:               2 (3)
                      eral Offset Mode” for details.                 Q Cycle Activity:
Words:                1                                                           Q1           Q2               Q3              Q4
Cycles:               1                                                        Decode       Read             Process           No
                                                                                          register ‘f’        Data          operation
Q Cycle Activity:
                                                                                            (src)
             Q1           Q2               Q3           Q4                     Decode        No                 No            Write
          Decode       Read            Process       Write to                             operation          operation      register ‘f’
                     register ‘f’       Data        destination                                                               (dest)
                                                                                          No dummy
                                                                                            read
Example:              MOVF          REG, 0, 0
     Before Instruction                                              Example:              MOVFF         REG1, REG2
           REG            =      22h                                      Before Instruction
           W              =      FFh                                            REG1           =       33h
     After Instruction                                                          REG2           =       11h
           REG            =      22h                                      After Instruction
           W              =      22h                                            REG1           =       33h
                                                                                REG2           =       33h


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 689
                          PIC18(L)F26/27/45/46/47/55/56/57K42

                                                                       MOVLB               Move literal to BSR
MOVFFL               Move f to f (Long Range)
                                                                       Syntax:             MOVLB k
Syntax:              MOVFFL fs,fd
                                                                       Operands:           0  k  63
Operands:            0  fs  16383
                                                                       Operation:          k  BSR
                     0  fd  16383
                                                                       Status Affected:    None
Operation:           (fs)  fd
                                                                       Encoding:               0000        0001         00kk    kkkk
Status Affected:     None
                                                                       Description:        The 6-bit literal ‘k’ is loaded into the
Encoding:
                                                                                           Bank Select Register (BSR<5:0>). The
1st word                  0000       0000       0110     fs fs fs fs
                                                                                           value of BSR<7:6> always remains ‘0’.
2nd word                  1111     fsfsfsfs   fsfsfsfs   fs fs fd fd
3rd word                  1111     fdfdfdfd   fdfdfdfd   fd fd fd fd   Words:              1
Description:         The contents of source register ‘fs’ are          Cycles:             1
                     moved to destination register ‘fd’.               Q Cycle Activity:
                     Location of source ‘fs’ and destination ‘fd’
                     can be anywhere in the 16 Kbyte data                           Q1         Q2                  Q3          Q4
                     space (0000h to 3FFFh).                                     Decode       Read             Process     Write literal
                     Either source or destination can be W                                 literal ‘k’          Data       ‘k’ to BSR
                     (a useful special situation).
                     MOVFFL is particularly useful for                 Example:            MOVLB               5
                     transferring a data memory location to a
                     peripheral register (such as the transmit              Before Instruction
                     buffer or an I/O port).                                      BSR Register =         02h
                     The MOVFFL instruction cannot use the                  After Instruction
                     PCL, TOSU, TOSH or TOSL as the                               BSR Register =         05h
                     destination register.
Words:               3
Cycles:              3
Q Cycle Activity:
                          Q1          Q2        Q3          Q4
                         Decode      No        No        No
                                  operation operation operation
                         Decode Read reg- Process           No
                                 ister ‘fs’ data         operation
                                   (src)

                         Decode       No       No        Write
                                  operation operation register ‘fd’
                                  No dummy              (dest)
                                     read


Example:             MOVFFL        2000h, 200Ah
     Before Instruction
           Contents of 2000h      = 33h
           Contents of 200Ah      = 11h
     After Instruction
           Contents of 2000h      = 33h
           Contents of 200Ah      = 33h


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 690
                             PIC18(L)F26/27/45/46/47/55/56/57K42

MOVLW                    Move literal to W                          MOVWF                     Move W to f
Syntax:                  MOVLW k                                    Syntax:                   MOVWF         f {,a}
Operands:                0  k  255                                Operands:                 0  f  255
                                                                                              a  [0,1]
Operation:               kW
                                                                    Operation:                (W)  f
Status Affected:         None
Encoding:                    0000      1110      kkkk       kkkk    Status Affected:          None
                                                                    Encoding:                     0110      111a          ffff        ffff
Description:             The 8-bit literal ‘k’ is loaded into W.
Words:                   1                                          Description:              Move data from W to register ‘f’.
                                                                                              Location ‘f’ can be anywhere in the
Cycles:                  1                                                                    256-byte bank.
Q Cycle Activity:                                                                             If ‘a’ is ‘0’, the Access Bank is selected.
                                                                                              If ‘a’ is ‘1’, the BSR is used to select the
             Q1              Q2             Q3             Q4
                                                                                              GPR bank.
          Decode            Read         Process       Write to W                             If ‘a’ is ‘0’ and the extended instruction
                         literal ‘k’      Data                                                set is enabled, this instruction operates
                                                                                              in Indexed Literal Offset Addressing
Example:                 MOVLW         5Ah                                                    mode whenever f 95 (5Fh). See Sec-
                                                                                              tion 41.2.3 “Byte-Oriented and Bit-
     After Instruction
                                                                                              Oriented Instructions in Indexed Lit-
            W        =       5Ah                                                              eral Offset Mode” for details.
                                                                    Words:                    1
                                                                    Cycles:                   1
                                                                    Q Cycle Activity:
                                                                                 Q1               Q2                 Q3              Q4
                                                                              Decode          Read W           Process             Write
                                                                                                                Data             register ‘f’


                                                                    Example:                  MOVWF         REG, 0
                                                                         Before Instruction
                                                                               W          =        4Fh
                                                                               REG        =        FFh
                                                                         After Instruction
                                                                                W        =         4Fh
                                                                                REG      =         4Fh


 2017-2021 Microchip Technology Inc.                                                                         DS40001919G-page 691
                             PIC18(L)F26/27/45/46/47/55/56/57K42

MULLW                    Multiply literal with W                       MULWF                     Multiply W with f
Syntax:                  MULLW          k                              Syntax:                   MULWF         f {,a}
Operands:                0  k  255                                   Operands:                 0  f  255
                                                                                                 a  [0,1]
Operation:               (W) x k  PRODH:PRODL
                                                                       Operation:                (W) x (f)  PRODH:PRODL
Status Affected:         None
Encoding:                    0000        1101       kkkk      kkkk     Status Affected:          None
                                                                       Encoding:                     0000      001a      ffff      ffff
Description:             An unsigned multiplication is carried
                         out between the contents of W and the         Description:              An unsigned multiplication is carried
                         8-bit literal ‘k’. The 16-bit result is                                 out between the contents of W and the
                         placed in the PRODH:PRODL register                                      register file location ‘f’. The 16-bit
                         pair. PRODH contains the high byte.                                     result is stored in the PRODH:PRODL
                         W is unchanged.                                                         register pair. PRODH contains the
                         None of the Status flags are affected.                                  high byte. Both W and ‘f’ are
                         Note that neither overflow nor carry is                                 unchanged.
                         possible in this operation. A zero result                               None of the Status flags are affected.
                         is possible but not detected.                                           Note that neither overflow nor carry is
                                                                                                 possible in this operation. A zero
Words:                   1
                                                                                                 result is possible but not detected.
Cycles:                  1                                                                       If ‘a’ is ‘0’, the Access Bank is
Q Cycle Activity:                                                                                selected. If ‘a’ is ‘1’, the BSR is used
                                                                                                 to select the GPR bank.
             Q1              Q2                Q3            Q4
                                                                                                 If ‘a’ is ‘0’ and the extended instruction
          Decode            Read             Process         Write                               set is enabled, this instruction
                         literal ‘k’          Data         registers                             operates in Indexed Literal Offset
                                                           PRODH:                                Addressing mode whenever
                                                            PRODL                                f 95 (5Fh). See Section
                                                                                                 41.2.3 “Byte-Oriented and Bit-Ori-
Example:                  MULLW          0C4h                                                    ented Instructions in Indexed Literal
                                                                                                 Offset Mode” for details.
     Before Instruction
                                                                       Words:                    1
           W                 =         E2h
           PRODH             =         ?                               Cycles:                   1
           PRODL             =         ?
                                                                       Q Cycle Activity:
     After Instruction
            W                =         E2h                                          Q1               Q2             Q3            Q4
            PRODH            =         ADh                                       Decode           Read            Process         Write
            PRODL            =         08h                                                      register ‘f’       Data         registers
                                                                                                                                PRODH:
                                                                                                                                 PRODL


                                                                       Example:                  MULWF         REG, 1
                                                                            Before Instruction
                                                                                  W                  =      C4h
                                                                                  REG                =      B5h
                                                                                  PRODH              =      ?
                                                                                  PRODL              =      ?
                                                                            After Instruction
                                                                                   W                 =      C4h
                                                                                   REG               =      B5h
                                                                                   PRODH             =      8Ah
                                                                                   PRODL             =      94h


 2017-2021 Microchip Technology Inc.                                                                             DS40001919G-page 692
                          PIC18(L)F26/27/45/46/47/55/56/57K42

NEGF                 Negate f                                          NOP                 No Operation
Syntax:              NEGF        f {,a}                                Syntax:             NOP
Operands:            0  f  255                                       Operands:           None
                     a  [0,1]
                                                                       Operation:          No operation
Operation:           (f)+1f
                                                                       Status Affected:    None
Status Affected:     N, OV, C, DC, Z                                   Encoding:               0000    0000        0000      0000
Encoding:                 0110       110a        ffff        ffff                              1111    xxxx        xxxx      xxxx
Description:         Location ‘f’ is negated using two’s               Description:        No operation.
                     complement. The result is placed in the
                                                                       Words:              1
                     data memory location ‘f’.
                     If ‘a’ is ‘0’, the Access Bank is selected.       Cycles:             1
                     If ‘a’ is ‘1’, the BSR is used to select the      Q Cycle Activity:
                     GPR bank.
                                                                                    Q1         Q2             Q3             Q4
                     If ‘a’ is ‘0’ and the extended instruction
                     set is enabled, this instruction operates                   Decode       No              No             No
                     in Indexed Literal Offset Addressing                                  operation       operation      operation
                     mode whenever f 95 (5Fh). See Sec-
                     tion 41.2.3 “Byte-Oriented and Bit-               Example:
                     Oriented Instructions in Indexed Lit-
                                                                       None.
                     eral Offset Mode” for details.
Words:               1
Cycles:              1
Q Cycle Activity:
             Q1           Q2                Q3              Q4
          Decode       Read               Process         Write
                     register ‘f’          Data         register ‘f’


Example:              NEGF          REG, 1
     Before Instruction
           REG        =   0011 1010 [3Ah]
     After Instruction
           REG        =   1100 0110 [C6h]


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 693
                             PIC18(L)F26/27/45/46/47/55/56/57K42

POP                      Pop Top of Return Stack                   PUSH                  Push Top of Return Stack
Syntax:                  POP                                       Syntax:               PUSH
Operands:                None                                      Operands:             None
Operation:               (TOS)  bit bucket                        Operation:            (PC) + 2  TOS
Status Affected:         None                                      Status Affected:      None
Encoding:                    0000    0000       0000      0110     Encoding:                 0000     0000      0000      0101
Description:             The TOS value is pulled off the return    Description:          The PC + 2 is pushed onto the top of
                         stack and is discarded. The TOS value                           the return stack. The previous TOS
                         then becomes the previous value that                            value is pushed down on the stack.
                         was pushed onto the return stack.                               This instruction allows implementing a
                         This instruction is provided to enable                          software stack by modifying TOS and
                         the user to properly manage the return                          then pushing it onto the return stack.
                         stack to incorporate a software stack.
                                                                   Words:                1
Words:                   1
                                                                   Cycles:               1
Cycles:                  1                                         Q Cycle Activity:
Q Cycle Activity:                                                               Q1           Q2            Q3             Q4
             Q1              Q2            Q3             Q4                 Decode       PUSH            No              No
          Decode            No        POP TOS             No                           PC + 2 onto     operation       operation
                         operation     value           operation                       return stack

Example:                 POP                                       Example:              PUSH
                         GOTO        NEW
                                                                        Before Instruction
     Before Instruction                                                      TOS                       =     345Ah
          TOS                         =     0031A2h                          PC                        =     0124h
          Stack (1 level down)        =     014332h
                                                                        After Instruction
     After Instruction                                                        PC                       =     0126h
           TOS                        =     014332h                           TOS                      =     0126h
           PC                         =     NEW                               Stack (1 level down)     =     345Ah


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 694
                           PIC18(L)F26/27/45/46/47/55/56/57K42

RCALL                  Relative Call                               RESET                     Reset
Syntax:                RCALL       n                               Syntax:                   RESET
Operands:              -1024  n  1023                            Operands:                 None
Operation:             (PC) + 2  TOS,                             Operation:                Reset all registers and flags that are
                       (PC) + 2 + 2n  PC                                                    affected by a MCLR Reset.
Status Affected:       None                                        Status Affected:          All
Encoding:                  1101        1nnn     nnnn      nnnn     Encoding:                     0000     0000        1111      1111
Description:           Subroutine call with a jump up to 1K        Description:              This instruction provides a way to
                       from the current location. First, return                              execute a MCLR Reset by software.
                       address (PC + 2) is pushed onto the
                                                                   Words:                    1
                       stack. Then, add the 2’s complement
                       number ‘2n’ to the PC. Since the PC will    Cycles:                   1
                       have incremented to fetch the next          Q Cycle Activity:
                       instruction, the new address will be
                                                                                Q1                 Q2            Q3             Q4
                       PC + 2 + 2n. This instruction is a
                       2-cycle instruction.                                  Decode              Start         No               No
                                                                                                 Reset      operation        operation
Words:                 1
Cycles:                2
                                                                   Example:                  RESET
Q Cycle Activity:
                                                                        After Instruction
             Q1            Q2              Q3             Q4                  Registers =          Reset Value
          Decode      Read literal       Process    Write to PC               Flags*     =         Reset Value
                         ‘n’              Data
                      PUSH PC to
                        stack
             No           No               No             No
          operation    operation        operation      operation


Example:               HERE            RCALL Jump
     Before Instruction
           PC =       Address (HERE)
     After Instruction
           PC =       Address (Jump)
           TOS =      Address (HERE + 2)


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 695
                            PIC18(L)F26/27/45/46/47/55/56/57K42

RETFIE                 Return from Interrupt                          RETLW                 Return literal to W
Syntax:                RETFIE {s}                                     Syntax:               RETLW k
Operands:              s  [0,1]                                      Operands:             0  k  255
Operation:             (TOS)  PC,                                    Operation:            k  W,
                       if s = 1, context is restored into WREG,                             (TOS)  PC,
                       STATUS, BSR, FSR0H, FSR0L,                                           PCLATU, PCLATH are unchanged
                       FSR1H, FSR1L, FSR2H, FSR2L,
                                                                      Status Affected:      None
                       PRODH, PRODL, PCLATH and
                       PCLATU registers from the                      Encoding:                 0000      1100      kkkk       kkkk
                       corresponding shadow registers.                Description:          W is loaded with the 8-bit literal ‘k’. The
                                                                                            program counter is loaded from the top
                       if s = 0, there is no change in status of                            of the stack (the return address). The
                       any register.                                                        upper and high address latches
Status Affected:       STAT<1:0> in INTCON1 register                                        (PCLATU/H) remains unchanged.

Encoding:                  0000         0000     0001        000s     Words:                1

Description:           Return from interrupt. Stack is popped         Cycles:               2
                       and Top-of-Stack (TOS) is loaded into          Q Cycle Activity:
                       the PC. Interrupts are enabled by
                                                                                   Q1           Q2            Q3              Q4
                       setting either the high or low priority
                       global interrupt enable bit. If 's' = 1, the             Decode         Read        Process         POP PC
                       contents of the shadow registers,                                    literal ‘k’     Data         from stack,
                       WREG, STATUS, BSR, FSR0H,                                                                         Write to W
                       FSR0L, FSR1H, FSR1L, FSR2H,                                 No          No             No              No
                       FSR2L, PRODH, PRODL, PCLATH and                          operation   operation      operation       operation
                       PCLATU, are loaded into corresponding
                       registers. There are two sets of shadow        Example:
                       registers, main context and low context.
                       The set retrieved on RETFIE instruction
                                                                          CALL TABLE ; W contains table
                       execution depends on what the state of
                                                                                     ; offset value
                       operation of the CPU was when RET-
                                                                                     ; W now has
                       FIE was executed. If ‘s’ = 0, no update
                                                                                     ; table value
                       of these registers occurs (default).
                                                                         :
Words:                 1                                              TABLE
Cycles:                2                                                  ADDWF PCL ; W = offset
                                                                          RETLW k0   ; Begin table
Q Cycle Activity:                                                         RETLW k1   ;
           Q1          Q2            Q3                 Q4               :
         Decode        No            No          POP PC from             :
                    operation     operation         stack                 RETLW kn   ; End of table
                                                  Set INT-
                                                CONx.STAT bits             Before Instruction
                                                 and restore                     W          =   07h
                                                   context                 After Instruction
         No            No            No              No                          W          =   value of kn
      operation     operation     operation       operation


Example:               RETFIE       1
     After Interrupt
           PC                            =     TOS
           WREG                          =     WREG_SHAD
           BSR                           =     BSR_SHAD
           STATUS                        =     STATUS_SHAD
           FSR0L/H                       =     FSR0L/H_SHAD
           FSR1L/H                       =     FSR1L/H_SHAD
           FSR2L/H                       =     FSR2L/H_SHAD
           PRODL/H                       =     PRODL/H_SHAD
           PCLATH/U                      =     PCLATH/U_SHAD


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 696
                           PIC18(L)F26/27/45/46/47/55/56/57K42

RETURN                Return from Subroutine                    RLCF                  Rotate Left f through Carry
Syntax:               RETURN {s}                                Syntax:                   RLCF        f {,d {,a}}
Operands:             s  [0,1]                                 Operands:             0  f  255
                                                                                      d  [0,1]
Operation:            (TOS)  PC,
                                                                                      a  [0,1]
                      if s = 1
                      (WREG_CSHAD)  W,                         Operation:            (f<n>)  dest<n + 1>,
                      (STATUS_CSHAD)  Status,                                        (f<7>)  C,
                      (BSR_CSHAD)  BSR,                                              (C)  dest<0>
                      PCLATU, PCLATH are unchanged
                                                                Status Affected:      C, N, Z
Status Affected:      None
                                                                Encoding:                  0011         01da        ffff     ffff
Encoding:                  0000    0000     0001       001s     Description:          The contents of register ‘f’ are rotated
Description:          Return from subroutine. The stack is                            one bit to the left through the CARRY
                      popped and the top of the stack (TOS)                           flag. If ‘d’ is ‘0’, the result is placed in
                      is loaded into the program counter. If                          W. If ‘d’ is ‘1’, the result is stored back
                      ‘s’= 1, the contents of the shadow                              in register ‘f’ (default).
                      registers, WREG_CSHAD,                                          If ‘a’ is ‘0’, the Access Bank is
                      STATUS_CSHAD and BSR_CSHAD,                                     selected. If ‘a’ is ‘1’, the BSR is used to
                      are loaded into their corresponding                             select the GPR bank.
                      registers, W, Status and BSR. If                                If ‘a’ is ‘0’ and the extended instruction
                      ‘s’ = 0, no update of these registers                           set is enabled, this instruction
                      occurs (default).                                               operates in Indexed Literal Offset
Words:                1                                                               Addressing mode whenever
                                                                                      f 95 (5Fh). See Section
Cycles:               2                                                               41.2.3 “Byte-Oriented and Bit-Ori-
Q Cycle Activity:                                                                     ented Instructions in Indexed Literal
                                                                                      Offset Mode” for details.
             Q1             Q2         Q3             Q4
          Decode         No         Process         POP PC                                        C             register f
                      operation      Data          from stack
             No          No            No             No        Words:                1
          operation   operation     operation      operation    Cycles:               1
                                                                Q Cycle Activity:
                                                                             Q1            Q2                 Q3             Q4
Example:                  RETURN
                                                                          Decode       Read                Process        Write to
     After Instruction:                                                              register ‘f’           Data         destination
           PC = TOS
                                                                Example:                  RLCF              REG, 0, 0
                                                                     Before Instruction
                                                                           REG        =    1110 0110
                                                                           C          =    0
                                                                     After Instruction
                                                                           REG        =    1110 0110
                                                                           W          =    1100 1100
                                                                           C          =    1


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 697
                           PIC18(L)F26/27/45/46/47/55/56/57K42

RLNCF                 Rotate Left f (No Carry)                         RRCF                  Rotate Right f through Carry
Syntax:                   RLNCF     f {,d {,a}}                        Syntax:               RRCF       f {,d {,a}}
Operands:             0  f  255                                      Operands:             0  f  255
                      d  [0,1]                                                              d  [0,1]
                      a  [0,1]                                                              a  [0,1]
Operation:            (f<n>)  dest<n + 1>,                            Operation:            (f<n>)  dest<n – 1>,
                      (f<7>)  dest<0>                                                       (f<0>)  C,
Status Affected:      N, Z                                                                   (C)  dest<7>
                                                                       Status Affected:      C, N, Z
Encoding:                  0100      01da         ffff     ffff
                                                                       Encoding:                 0011       00da          ffff         ffff
Description:          The contents of register ‘f’ are rotated
                      one bit to the left. If ‘d’ is ‘0’, the result   Description:          The contents of register ‘f’ are rotated
                      is placed in W. If ‘d’ is ‘1’, the result is                           one bit to the right through the CARRY
                      stored back in register ‘f’ (default).                                 flag. If ‘d’ is ‘0’, the result is placed in W.
                      If ‘a’ is ‘0’, the Access Bank is selected.                            If ‘d’ is ‘1’, the result is placed back in
                      If ‘a’ is ‘1’, the BSR is used to select the                           register ‘f’ (default).
                      GPR bank.                                                              If ‘a’ is ‘0’, the Access Bank is selected.
                      If ‘a’ is ‘0’ and the extended instruction                             If ‘a’ is ‘1’, the BSR is used to select the
                      set is enabled, this instruction operates                              GPR bank.
                      in Indexed Literal Offset Addressing                                   If ‘a’ is ‘0’ and the extended instruction
                      mode whenever f 95 (5Fh). See Sec-                                   set is enabled, this instruction operates
                      tion 41.2.3 “Byte-Oriented and Bit-                                    in Indexed Literal Offset Addressing
                      Oriented Instructions in Indexed Lit-                                  mode whenever f 95 (5Fh). See Sec-
                      eral Offset Mode” for details.                                         tion 41.2.3 “Byte-Oriented and Bit-
                                                                                             Oriented Instructions in Indexed Lit-
                                          register f
                                                                                             eral Offset Mode” for details.

Words:                1                                                                                 C             register f
Cycles:               1
                                                                       Words:                1
Q Cycle Activity:
                                                                       Cycles:               1
             Q1            Q2             Q3               Q4
          Decode       Read            Process          Write to       Q Cycle Activity:
                     register ‘f’       Data           destination                  Q1           Q2               Q3                   Q4
                                                                                 Decode       Read             Process              Write to
Example:                  RLNCF         REG, 1, 0                                           register ‘f’        Data               destination

     Before Instruction
           REG        =    1010 1011                                   Example:              RRCF             REG, 0, 0
     After Instruction                                                      Before Instruction
           REG        =    0101 0111                                              REG        =   1110 0110
                                                                                  C          =   0
                                                                            After Instruction
                                                                                  REG        =   1110 0110
                                                                                  W          =   0111 0011
                                                                                  C          =   0


 2017-2021 Microchip Technology Inc.                                                                         DS40001919G-page 698
                              PIC18(L)F26/27/45/46/47/55/56/57K42

RRNCF                     Rotate Right f (No Carry)                         SETF                  Set f
Syntax:                   RRNCF       f {,d {,a}}                           Syntax:               SETF       f {,a}
Operands:                 0  f  255                                       Operands:             0  f  255
                          d  [0,1]                                                               a [0,1]
                          a  [0,1]
                                                                            Operation:            FFh  f
Operation:                (f<n>)  dest<n – 1>,
                                                                            Status Affected:      None
                          (f<0>)  dest<7>
                                                                            Encoding:                 0110        100a       ffff        ffff
Status Affected:          N, Z
                                                                            Description:          The contents of the specified register
Encoding:                     0100       00da       ffff         ffff
                                                                                                  are set to FFh.
Description:              The contents of register ‘f’ are rotated                                If ‘a’ is ‘0’, the Access Bank is selected.
                          one bit to the right. If ‘d’ is ‘0’, the result                         If ‘a’ is ‘1’, the BSR is used to select the
                          is placed in W. If ‘d’ is ‘1’, the result is                            GPR bank.
                          placed back in register ‘f’ (default).                                  If ‘a’ is ‘0’ and the extended instruction
                          If ‘a’ is ‘0’, the Access Bank will be                                  set is enabled, this instruction operates
                          selected (default), overriding the BSR                                  in Indexed Literal Offset Addressing
                          value. If ‘a’ is ‘1’, then the bank will be                             mode whenever f 95 (5Fh). See Sec-
                          selected as per the BSR value.                                          tion 41.2.3 “Byte-Oriented and Bit-
                          If ‘a’ is ‘0’ and the extended instruction                              Oriented Instructions in Indexed Lit-
                          set is enabled, this instruction operates                               eral Offset Mode” for details.
                          in Indexed Literal Offset Addressing
                                                                            Words:                1
                          mode whenever f 95 (5Fh). See Sec-
                          tion 41.2.3 “Byte-Oriented and Bit-               Cycles:               1
                          Oriented Instructions in Indexed Lit-             Q Cycle Activity:
                          eral Offset Mode” for details.
                                                                                         Q1           Q2                Q3              Q4
                                                register f                            Decode       Read               Process         Write
                                                                                                 register ‘f’          Data         register ‘f’
Words:                    1
Cycles:                   1                                                 Example:              SETF                 REG, 1
Q Cycle Activity:                                                                Before Instruction
             Q1               Q2              Q3                 Q4                    REG            =      5Ah
                                                                                 After Instruction
          Decode        Read               Process            Write to
                                                                                       REG            =      FFh
                      register ‘f’          Data             destination


Example 1:                RRNCF         REG, 1, 0
     Before Instruction
           REG        =       1101 0111
     After Instruction
           REG        =       1110 1011

Example 2:                RRNCF         REG, 0, 0
     Before Instruction
           W          =       ?
           REG        =       1101 0111
     After Instruction
            W        =        1110 1011
            REG      =        1101 0111


 2017-2021 Microchip Technology Inc.                                                                                 DS40001919G-page 699
                              PIC18(L)F26/27/45/46/47/55/56/57K42

SLEEP                     Enter Sleep mode                        SUBFSR                    Subtract Literal from FSR
Syntax:                    SLEEP                                  Syntax:                   SUBFSR f, k

Operands:                 None                                    Operands:                 0  k  63
                                                                                            f  [ 0, 1, 2 ]
Operation:                00h  WDT,
                          0  WDT postscaler,                     Operation:                (FSRf) – k  FSRf
                          1  TO,                                 Status Affected:          None
                          0  PD                                  Encoding:                  1110        1001        ffkk      kkkk
Status Affected:          TO, PD                                  Description:              The 6-bit literal ‘k’ is subtracted from
                                                                                            the contents of the FSR specified by
Encoding:                     0000   0000     0000      0011
                                                                                            ‘f’.
Description:              The Power-down Status bit (PD) is       Words:                    1
                          cleared. The Time-out Status bit (TO)
                                                                  Cycles:                   1
                          is set. Watchdog Timer and its
                          postscaler are cleared.                 Q Cycle Activity:
                          The processor is put into Sleep mode                 Q1               Q2              Q3              Q4
                          with the oscillator stopped.                      Decode        Read                Process        Write to
Words:                    1                                                             register ‘f’           Data         destination

Cycles:                   1
Q Cycle Activity:
                                                                  Example:                  SUBFSR 2, 23h
             Q1               Q2         Q3            Q4
                                                                       Before Instruction
          Decode         No            Process        Go to
                                                                            FSR2       =        03FFh
                      operation         Data          Sleep
                                                                       After Instruction
                                                                             FSR2       =       03DCh
Example:                  SLEEP
     Before Instruction
          TO =       ?
          PD =       ?
     After Instruction
           TO =       1†
           PD =       0

† If WWDT causes wake-up, this bit is cleared.


 2017-2021 Microchip Technology Inc.                                                                         DS40001919G-page 700
                          PIC18(L)F26/27/45/46/47/55/56/57K42

SUBFWB                Subtract f from W with borrow                  SUBLW                     Subtract W from literal
Syntax:                SUBFWB       f {,d {,a}}                      Syntax:                   SUBLW k
Operands:             0 f 255                                    Operands:                 0 k 255
                      d  [0,1]
                                                                     Operation:                k – (W) W
                      a  [0,1]
                                                                     Status Affected:          N, OV, C, DC, Z
Operation:            (W) – (f) – (C) dest
                                                                     Encoding:                     0000      1000     kkkk        kkkk
Status Affected:      N, OV, C, DC, Z
                                                                     Description               W is subtracted from the 8-bit
Encoding:                 0101      01da      ffff       ffff                                  literal ‘k’. The result is placed in W.
Description:          Subtract register ‘f’ and CARRY flag
                                                                     Words:                    1
                      (borrow) from W (2’s complement
                      method). If ‘d’ is ‘0’, the result is stored   Cycles:                   1
                      in W. If ‘d’ is ‘1’, the result is stored in   Q Cycle Activity:
                      register ‘f’ (default).
                                                                                  Q1               Q2            Q3              Q4
                      If ‘a’ is ‘0’, the Access Bank is
                      selected. If ‘a’ is ‘1’, the BSR is used                 Decode         Read            Process         Write to W
                      to select the GPR bank.                                              literal ‘k’         Data
                      If ‘a’ is ‘0’ and the extended instruction
                                                                     Example 1:                SUBLW      02h
                      set is enabled, this instruction
                      operates in Indexed Literal Offset                  Before Instruction
                      Addressing mode whenever                                  W          =       01h
                                                                                C          =       ?
                      f 95 (5Fh). See Section
                                                                          After Instruction
                      41.2.3 “Byte-Oriented and Bit-Ori-                        W          =       01h
                      ented Instructions in Indexed Literal                     C          =       1   ; result is positive
                      Offset Mode” for details.                                 Z          =       0
                                                                                N          =       0
Words:                1
                                                                     Example 2:                SUBLW      02h
Cycles:               1
                                                                          Before Instruction
Q Cycle Activity:                                                               W          =       02h
                                                                                C          =       ?
             Q1           Q2            Q3               Q4
                                                                          After Instruction
          Decode      Read           Process         Write to                   W          =       00h
                    register ‘f’      Data          destination                 C          =       1   ; result is zero
                                                                                Z          =       1
Example 1:             SUBFWB    REG, 1, 0                                      N          =       0
    Before Instruction                                               Example 3:                SUBLW      02h
          REG        =   03h
          W          =   02h                                              Before Instruction
          C          =   1                                                      W          =       03h
    After Instruction                                                           C          =       ?
          REG        =   FFh                                              After Instruction
          W          =   02h                                                    W          =       FFh ; (2’s complement)
          C          =   0                                                      C          =       0   ; result is negative
          Z          =   0                                                      Z          =       0
          N          =   1 ; result is negative                                 N          =       1
Example 2:             SUBFWB    REG, 0, 0
    Before Instruction
          REG        =   02h
          W          =   05h
          C          =   1
    After Instruction
          REG        =   02h
          W          =   03h
          C          =   1
          Z          =   0
          N          =   0 ; result is positive
Example 3:             SUBFWB    REG, 1, 0
    Before Instruction
          REG        =   01h
          W          =   02h
          C          =   0
    After Instruction
          REG        =   00h
          W          =   02h
          C          =   1
          Z          =   1 ; result is zero
          N          =   0


 2017-2021 Microchip Technology Inc.                                                                         DS40001919G-page 701
                              PIC18(L)F26/27/45/46/47/55/56/57K42

SUBWF                     Subtract W from f                            SUBWFB               Subtract W from f with Borrow
Syntax:                   SUBWF         f {,d {,a}}                    Syntax:              SUBWFB         f {,d {,a}}
Operands:                 0 f 255                                  Operands:            0  f  255
                          d  [0,1]                                                         d  [0,1]
                          a  [0,1]                                                         a  [0,1]

Operation:                (f) – (W) dest                             Operation:           (f) – (W) – (C) dest
                                                                       Status Affected:     N, OV, C, DC, Z
Status Affected:          N, OV, C, DC, Z
                                                                       Encoding:                 0101      10da          ffff       ffff
Encoding:                     0101       11da         ffff   ffff
                                                                       Description:         Subtract W and the CARRY flag
Description:              Subtract W from register ‘f’ (2’s                                 (borrow) from register ‘f’ (2’s comple-
                          complement method). If ‘d’ is ‘0’, the                            ment method). If ‘d’ is ‘0’, the result is
                          result is stored in W. If ‘d’ is ‘1’, the                         stored in W. If ‘d’ is ‘1’, the result is
                          result is stored back in register ‘f’                             stored back in register ‘f’ (default).
                          (default).                                                        If ‘a’ is ‘0’, the Access Bank is selected.
                          If ‘a’ is ‘0’, the Access Bank is                                 If ‘a’ is ‘1’, the BSR is used to select the
                          selected. If ‘a’ is ‘1’, the BSR is used                          GPR bank.
                          to select the GPR bank.                                           If ‘a’ is ‘0’ and the extended instruction
                          If ‘a’ is ‘0’ and the extended instruction                        set is enabled, this instruction operates
                          set is enabled, this instruction                                  in Indexed Literal Offset Addressing
                          operates in Indexed Literal Offset                                mode whenever f 95 (5Fh). See Sec-
                          Addressing mode whenever                                          tion 41.2.3 “Byte-Oriented and Bit-
                          f 95 (5Fh). See Section                                         Oriented Instructions in Indexed Lit-
                          41.2.3 “Byte-Oriented and Bit-Ori-                                eral Offset Mode” for details.
                          ented Instructions in Indexed Literal
                          Offset Mode” for details.                    Words:               1
                                                                       Cycles:              1
Words:                    1
                                                                       Q Cycle Activity:
Cycles:                   1
                                                                                   Q1          Q2              Q3                  Q4
Q Cycle Activity:                                                                Decode       Read           Process             Write to
             Q1               Q2              Q3             Q4                             register ‘f’      Data              destination
          Decode       Read                Process        Write to     Example 1:                SUBWFB    REG, 1, 0
                     register ‘f’           Data         destination
                                                                            Before Instruction
Example 1:                SUBWF         REG, 1, 0                                 REG        =    19h       (0001 1001)
                                                                                  W          =    0Dh       (0000 1101)
     Before Instruction                                                           C          =    1
           REG        =       03h                                           After Instruction
           W          =       02h                                                 REG        =    0Ch       (0000 1100)
           C          =       ?                                                   W          =    0Dh       (0000 1101)
     After Instruction                                                            C          =    1
           REG        =       01h                                                 Z          =    0
           W          =       02h                                                 N          =    0         ; result is positive
           C          =       1   ; result is positive
           Z          =       0                                        Example 2:                SUBWFB REG, 0, 0
           N          =       0                                             Before Instruction
Example 2:                SUBWF         REG, 0, 0                                 REG        =    1Bh       (0001 1011)
                                                                                  W          =    1Ah       (0001 1010)
     Before Instruction                                                           C          =    0
           REG        =       02h                                           After Instruction
           W          =       02h                                                 REG        =    1Bh       (0001 1011)
           C          =       ?                                                   W          =    00h
     After Instruction                                                            C          =    1
           REG        =       02h                                                 Z          =    1         ; result is zero
           W          =       00h                                                 N          =    0
           C          =       1   ; result is zero
           Z          =       1                                        Example 3:                SUBWFB    REG, 1, 0
           N          =       0                                             Before Instruction
Example 3:                SUBWF         REG, 1, 0                                 REG        =    03h       (0000 0011)
                                                                                  W          =    0Eh       (0000 1110)
     Before Instruction                                                           C          =    1
           REG        =       01h                                           After Instruction
           W          =       02h                                                 REG        =    F5h       (1111 0101)
           C          =       ?                                                                             ; [2’s comp]
     After Instruction                                                             W       =      0Eh       (0000 1110)
           REG        =       FFh ;(2’s complement)                                C       =      0
           W          =       02h                                                  Z       =      0
           C          =       0   ; result is negative                             N       =      1         ; result is negative
           Z          =       0
           N          =       1


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 702
                          PIC18(L)F26/27/45/46/47/55/56/57K42

SWAPF                 Swap f
Syntax:               SWAPF f {,d {,a}}
Operands:             0  f  255
                      d  [0,1]
                      a  [0,1]
Operation:            (f[3:0])  dest[7:4],
                      (f[7:4])  dest[3:0]
Status Affected:      None
Encoding:                 0011       10da     ffff       ffff
Description:          The upper and lower nibbles of register
                      ‘f’ are exchanged. If ‘d’ is ‘0’, the result
                      is placed in W. If ‘d’ is ‘1’, the result is
                      placed in register ‘f’ (default).
                      If ‘a’ is ‘0’, the Access Bank is selected.
                      If ‘a’ is ‘1’, the BSR is used to select the
                      GPR bank.
                      If ‘a’ is ‘0’ and the extended instruction
                      set is enabled, this instruction operates
                      in Indexed Literal Offset Addressing
                      mode whenever f 95 (5Fh). See Sec-
                      tion 41.2.3 “Byte-Oriented and Bit-
                      Oriented Instructions in Indexed Lit-
                      eral Offset Mode” for details.
Words:                1
Cycles:               1
Q Cycle Activity:
             Q1           Q2             Q3             Q4
          Decode       Read            Process       Write to
                     register ‘f’       Data        destination


Example:              SWAPF         REG, 1, 0
     Before Instruction
           REG        =   53h
     After Instruction
           REG        =   35h


 2017-2021 Microchip Technology Inc.                                DS40001919G-page 703
                           PIC18(L)F26/27/45/46/47/55/56/57K42

TBLRD             Table Read                                        TBLRD            Table Read (Continued)
Syntax:           TBLRD ( *; *+; *-; +*)                            Example1:        TBLRD   *+ ;
Operands:         None                                                  Before Instruction
                                                                              TABLAT             =   55h
Operation:        if TBLRD *,
                                                                              TBLPTR             =   00A356h
                  (Prog Mem (TBLPTR))  TABLAT;                               MEMORY (00A356h)   =   34h
                  TBLPTR – No Change;                                   After Instruction
                  if TBLRD *+,                                                TABLAT             =   34h
                  (Prog Mem (TBLPTR))  TABLAT;                               TBLPTR             =   00A357h
                  (TBLPTR) + 1  TBLPTR;
                                                                    Example2:        TBLRD   +* ;
                  if TBLRD *-,
                  (Prog Mem (TBLPTR))  TABLAT;                         Before Instruction
                  (TBLPTR) – 1  TBLPTR;                                      TABLAT             =   AAh
                                                                              TBLPTR             =   01A357h
                  if TBLRD +*,
                                                                              MEMORY (01A357h)   =   12h
                  (TBLPTR) + 1  TBLPTR;                                      MEMORY (01A358h)   =   34h
                  (Prog Mem (TBLPTR))  TABLAT;                         After Instruction
Status Affected: None                                                         TABLAT             =   34h
                                                                              TBLPTR             =   01A358h
Encoding:              0000         0000    0000       10nn
                                                      nn=0 *
                                                        =1 *+
                                                        =2 *-
                                                        =3 +*
Description:      This instruction is used to read the contents
                  of Program Memory (P.M.). To address the
                  program memory, a pointer called Table
                  Pointer (TBLPTR) is used.
                  The TBLPTR (a 21-bit pointer) points to
                  each byte in the program memory. TBLPTR
                  has a 2-Mbyte address range.
                       TBLPTR[0] = 0: Least Significant Byte
                                          of Program Memory
                                          Word
                       TBLPTR[0] = 1: Most Significant Byte
                                          of Program Memory
                                          Word
                  The TBLRD instruction can modify the value
                  of TBLPTR as follows:
                  • no change
                  • post-increment
                  • post-decrement
                  • pre-increment
Words:            1
Cycles:           2
Q Cycle Activity:
          Q1               Q2              Q3           Q4
         Decode            No             No            No
                        operation      operation     operation
         No            No operation       No        No operation
      operation       (Read Program    operation   (Write TABLAT)
                         Memory)


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 704
                           PIC18(L)F26/27/45/46/47/55/56/57K42

TBLWT               Table Write                                   TBLWT            Table Write (Continued)
Syntax:             TBLWT ( *; *+; *-; +*)                        Example1:        TBLWT *+;
Operands:           None                                              Before Instruction
Operation:          if TBLWT*,                                              TABLAT                     =   55h
                    (TABLAT)  Holding Register;                            TBLPTR                     =   00A356h
                    TBLPTR – No Change;                                     HOLDING REGISTER
                                                                             (00A356h)                 =   FFh
                    if TBLWT*+,
                                                                      After Instructions (table write completion)
                    (TABLAT)  Holding Register;
                                                                            TABLAT                     =   55h
                    (TBLPTR) + 1  TBLPTR;                                  TBLPTR                     =   00A357h
                    if TBLWT*-,                                             HOLDING REGISTER
                    (TABLAT)  Holding Register;                             (00A356h)                 =   55h
                    (TBLPTR) – 1  TBLPTR;                        Example 2:       TBLWT +*;
                    if TBLWT+*,
                    (TBLPTR) + 1  TBLPTR;                            Before Instruction
                    (TABLAT)  Holding Register;                            TABLAT                     =   34h
                                                                            TBLPTR                     =   01389Ah
Status Affected:    None                                                    HOLDING REGISTER
                                                                             (01389Ah)                 =   FFh
Encoding:               0000     0000        0000     11nn
                                                                            HOLDING REGISTER
                                                    nn=0 *                   (01389Bh)                 =   FFh
                                                      =1 *+           After Instruction (table write completion)
                                                      =2 *-                 TABLAT                     =   34h
                                                      =3 +*                 TBLPTR                     =   01389Bh
                                                                            HOLDING REGISTER
Description:        This instruction uses the LSBs of TBLPTR                 (01389Ah)                 =   FFh
                    to determine which of the holding registers             HOLDING REGISTER
                    the TABLAT is written to. The holding reg-               (01389Bh)                 =   34h
                    isters are used to program the contents of
                    Program Memory. (Refer to Section
                    13.1 “Program Flash Memory” for addi-
                    tional details on programming Flash mem-
                    ory.)
                    The TBLPTR (a 21-bit pointer) points to
                    each byte in the program memory.
                    TBLPTR has a 2-MByte address range.
                    The LSb of the TBLPTR selects which
                    byte of the program memory location to
                    access.
                          TBLPTR[0] = 0: Least Significant
                                            Byte of Program
                                            Memory Word
                          TBLPTR[0] = 1: Most Significant
                                            Byte of Program
                                            Memory Word
                    The TBLWT instruction can modify the
                    value of TBLPTR as follows:
                    • no change
                    • post-increment
                    • post-decrement
                    • pre-increment
Words:              1
Cycles:             2
Q Cycle Activity:
                        Q1        Q2         Q3       Q4
                     Decode       No        No        No
                               operation operation operation
                       No        No        No        No
                    operation operation operation operation
                               (Read              (Write to
                              TABLAT)              Holding
                                                  Register)


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 705
                           PIC18(L)F26/27/45/46/47/55/56/57K42

TSTFSZ                 Test f, skip if 0                              XORLW                     Exclusive OR literal with W
Syntax:                TSTFSZ f {,a}                                  Syntax:                   XORLW k
Operands:              0  f  255                                    Operands:                 0 k 255
                       a  [0,1]
                                                                      Operation:                (W) .XOR. k W
Operation:             skip if f = 0
                                                                      Status Affected:          N, Z
Status Affected:       None                                           Encoding:                     0000      1010      kkkk       kkkk
Encoding:                  0110        011a     ffff      ffff
                                                                      Description:              The contents of W are XORed with
Description:           If ‘f’ = 0, the next instruction fetched                                 the 8-bit literal ‘k’. The result is placed
                       during the current instruction execution                                 in W.
                       is discarded and a NOP is executed,            Words:                    1
                       making this a 2-cycle instruction.
                       If ‘a’ is ‘0’, the Access Bank is selected.    Cycles:                   1
                       If ‘a’ is ‘1’, the BSR is used to select the   Q Cycle Activity:
                       GPR bank.
                                                                                   Q1               Q2            Q3              Q4
                       If ‘a’ is ‘0’ and the extended instruction
                       set is enabled, this instruction operates                Decode             Read        Process        Write to W
                       in Indexed Literal Offset Addressing                                     literal ‘k’     Data
                       mode whenever f 95 (5Fh). See Sec-
                       tion 41.2.3 “Byte-Oriented and Bit-            Example:                  XORLW         0AFh
                       Oriented Instructions in Indexed Lit-
                       eral Offset Mode” for details.                      Before Instruction
                                                                                 W          =       B5h
Words:                 1
                                                                           After Instruction
Cycles:                1(2)
                                                                                  W        =        1Ah
                       Note: 3 cycles if skip and followed
                             by a 2-word instruction. 4 cycles
                             if skip and followed by a 3-word
                             instruction.
Q Cycle Activity:
              Q1           Q2              Q3             Q4
           Decode        Read           Process           No
                       register ‘f’      Data          operation
If skip:
              Q1           Q2              Q3             Q4
              No          No               No             No
           operation   operation        operation      operation
If skip and followed by 2-word instruction:
              Q1           Q2              Q3             Q4
              No          No               No             No
           operation   operation        operation      operation
              No          No               No             No
           operation   operation        operation      operation


Example:               HERE           TSTFSZ    CNT, 1
                       NZERO          :
                       ZERO           :
     Before Instruction
           PC              =      Address (HERE)
     After Instruction
           If CNT          =      00h,
           PC              =      Address (ZERO)
           If CNT                00h,
           PC              =      Address (NZERO)


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 706
                          PIC18(L)F26/27/45/46/47/55/56/57K42

XORWF                 Exclusive OR W with f
Syntax:               XORWF         f {,d {,a}}
Operands:             0  f  255
                      d  [0,1]
                      a  [0,1]
Operation:           (W) .XOR. (f) dest
Status Affected:      N, Z
Encoding:                 0001       10da         ffff       ffff
Description:          Exclusive OR the contents of W with
                      register ‘f’. If ‘d’ is ‘0’, the result is stored
                      in W. If ‘d’ is ‘1’, the result is stored back
                      in the register ‘f’ (default).
                      If ‘a’ is ‘0’, the Access Bank is selected.
                      If ‘a’ is ‘1’, the BSR is used to select the
                      GPR bank.
                      If ‘a’ is ‘0’ and the extended instruction
                      set is enabled, this instruction operates
                      in Indexed Literal Offset Addressing
                      mode whenever f 95 (5Fh). See Sec-
                      tion 41.2.3 “Byte-Oriented and Bit-
                      Oriented Instructions in Indexed Lit-
                      eral Offset Mode” for details.
Words:                1
Cycles:               1
Q Cycle Activity:
             Q1           Q2               Q3               Q4
          Decode       Read            Process          Write to
                     register ‘f’       Data           destination


Example:              XORWF         REG, 1, 0
     Before Instruction
           REG        =   AFh
           W          =   B5h
     After Instruction
           REG        =   1Ah
           W          =   B5h


 2017-2021 Microchip Technology Inc.                                     DS40001919G-page 707
                      PIC18(L)F26/27/45/46/47/55/56/57K42
41.2     Extended Instruction Set                           A summary of the instructions in the extended instruc-
                                                            tion set is provided in Table 41-3. Detailed descriptions
In addition to the standard instructions of the PIC18       are provided in Section 41.2.2 “Extended Instruction
instruction set, PIC18(L)F26/27/45/46/47/55/56/57K42        Set”. The opcode field descriptions in Table 41-1 apply
devices also provide an optional extension to the core      to both the standard and extended PIC18 instruction
CPU functionality. The added features include               sets.
additional instructions that augment indirect and
indexed addressing operations and the implementation          Note:     The instruction set extension and the
of Indexed Literal Offset Addressing mode for many of                   Indexed Literal Offset Addressing mode
the standard PIC18 instructions.                                        were designed for optimizing applications
                                                                        written in C; the user may likely never use
The additional features of the extended instruction set
                                                                        these instructions directly in assembler.
are disabled by default. To enable them, users must set
                                                                        The syntax for these commands is pro-
the XINST Configuration bit.
                                                                        vided as a reference for users who may be
The instructions in the extended set can all be                         reviewing code that has been generated
classified as literal operations, which either manipulate               by a compiler.
the File Select Registers, or use them for indexed
addressing. Two of the standard instructions, ADDFSR        41.2.1      EXTENDED INSTRUCTION SYNTAX
and SUBFSR, each have an additional special
                                                            Most of the extended instructions use indexed
instantiation for using FSR2 as extended instructions.
                                                            arguments, using one of the File Select Registers and
These versions (ADDULNK and SUBULNK) allow for
                                                            some offset to specify a source or destination register.
automatic return after execution.
                                                            When an argument for an instruction serves as part of
The extended instructions are specifically implemented      indexed addressing, it is enclosed in square brackets
to optimize re-entrant program code (that is, code that     (“[ ]”). This is done to indicate that the argument is used
is recursive or that uses a software stack) written in      as an index or offset. MPASM™ Assembler will flag an
high-level languages, particularly C. Among other           error if it determines that an index or offset value is not
things, they allow users working in high-level              bracketed.
languages to perform certain operations on data
                                                            When the extended instruction set is enabled, brackets
structures more efficiently. These include:
                                                            are also used to indicate index arguments in byte-
• dynamic allocation and deallocation of software           oriented and bit-oriented instructions. This is in addition
  stack space when entering and leaving                     to other changes in their syntax. For more details, see
  subroutines                                               Section 41.2.3.1 “Extended Instruction Syntax with
• function pointer invocation                               Standard PIC18 Commands”.
• software Stack Pointer manipulation                         Note:     In the past, square brackets have been
• manipulation of variables located in a software                       used to denote optional arguments in the
  stack                                                                 PIC18 and earlier instruction sets. In this
                                                                        text and going forward, optional
                                                                        arguments are denoted by braces (“{ }”).


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 708
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 41-3:        EXTENSIONS TO THE PIC18 INSTRUCTION SET

     Mnemonic,                                                                 16-Bit Instruction Word                Status
                                    Description                  Cycles
     Operands                                                                MSb                         LSb         Affected

ADDULNK        k        Add FSR2 with (k) & return                  2       1110     1000     11kk     kkkk            None
MOVSF          zs, fd   Move zs (source) to        1st word         2       1110     1011     0zzz     zzzz            None
                             fd (destination)      2nd word         2       1111     ffff     ffff     ffff
MOVSFL         zs, fd   Opcode                     1st word                 0000     0000     0000     0010            None
                        Move zs (source) to        2nd word         3       1111     xxxz     zzzz     zzff
                             fd (full destination) 3rd word                 1111     ffff     ffff     ffff
MOVSS          zs, zd   Move zs (source) to        1st word                 1110     1011     1zzz     zzzz            None
                             zd (destination)      2nd word         2       1111     xxxx     xzzz     zzzz
PUSHL          k        Store Literal at FSR2, Decrement            1       1110     1010     kkkk     kkkk            None
                        FSR2
SUBULNK        k        Subtract (k) from FSR2 & return             2       1110     1001     11kk     kkkk            None
Note 1: If Program Counter (PC) is modified or a conditional test is true, the instruction requires an additional cycle. The extra
        cycle is executed as a NOP.
     2: Some instructions are multi word instructions. The second/third words of these instructions will be decoded as a NOP,
        unless the first word of the instruction retrieves the information embedded in these 16-bits. This ensures that all program
        memory locations have a valid instruction.
     3: Only available when extended instruction set is enabled.
     4: fs and fd do not cover the full memory range. 2 MSBs of bank selection are forced to ‘b00 to limit the range of these
        instructions to lower 4k addressing space.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 709
                               PIC18(L)F26/27/45/46/47/55/56/57K42
41.2.2         EXTENDED INSTRUCTION SET


ADDULNK                    Add Literal to FSR2 and Return
Syntax:                    ADDULNK k
Operands:                  0  k  63
Operation:                 FSR2 + k  FSR2,
                           (TOS) PC
Status Affected:           None
Encoding:                   1110        1000     11kk      kkkk
Description:               The 6-bit literal ‘k’ is added to the
                           contents of FSR2. A RETURN is then
                           executed by loading the PC with the
                           TOS.
                           The instruction takes two cycles to
                           execute; a NOP is performed during
                           the second cycle.
                           This may be thought of as a special
                           case of the ADDFSR instruction,
                           where f = 3 (binary ‘11’); it operates
                           only on FSR2.
Words:                     1
Cycles:                    2


Q Cycle Activity:
             Q1                Q2           Q3             Q4
          Decode             Read        Process        Write to
                          literal ‘k’     Data           FSR
           No           No                 No             No
         Operation    Operation          Operation      Operation


Example:                  ADDULNK 23h
     Before Instruction
          FSR2       =         03FFh
          PC         =         0100h
     After Instruction
           FSR2       =        0422h
           PC         =        (TOS)


  Note:        All PIC18 instructions may take an optional label argument preceding the instruction mnemonic for use in
               symbolic addressing. If a label is used, the instruction syntax then becomes: {label} instruction argument(s).


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 710
                          PIC18(L)F26/27/45/46/47/55/56/57K42

MOVSF                 Move Indexed to f
Syntax:               MOVSF [zs], fd                                  MOVSFL                    Move Indexed to f (Long Range)
Operands:             0  zs  127                                    Syntax:                   MOVSFL [zs], fd
                      0  fd  4095                                   Operands:                 0  zs  127
Operation:            ((FSR2) + zs)  fd                                                        0  fd  16383
Status Affected:      None                                            Operation:                ((FSR2) + zs)  fd
Encoding:                                                             Status Affected:          None
1st word (source)         1110      1011       0zzz       zzzzs       Encoding:
2nd word (destin.)        1111      ffff       ffff       ffffd       1st word (opcode)             0000      0000       0110       0010
Description:          The contents of the source register are         2nd word (source)             1111      xxxz       zzzz       zzsff
                      moved to destination register ‘fd’. The         3rd word (full destin.)       1111      ffff       ffff       ffffd
                      actual address of the source register is        Description:              The contents of the source register are
                      determined by adding the 7-bit literal                                    moved to destination register ‘fd’. The
                      offset ‘zs’ in the first word to the value of                             actual address of the source register is
                      FSR2. The address of the destination                                      determined by adding the 7-bit literal
                      register is specified by the 12-bit literal                               offset ‘zs’ in the first word to the value of
                      ‘fd’ in the second word. Both addresses                                   FSR2 (14 bits). The address of the
                      can be anywhere in the 4096-byte data                                     destination register is specified by the
                      space (000h to FFFh).                                                     14-bit literal ‘fd’ in the second word.
                      MOVSF has curtailed the destination                                       Both addresses can be anywhere in the
                      range to the lower 4 Kbyte space in                                       16 Kbyte data space (0000h to 3FFFh).
                      memory (Banks 1 through 15). For                                          The MOVSFL instruction cannot use the
                      everything else, use MOVSFL.                                              PCL, TOSU, TOSH or TOSL as the
Words:                2                                                                         destination register. If the resultant
                                                                                                source address points to an indirect
Cycles:               2
                                                                                                addressing register, the value returned
Q Cycle Activity:                                                                               will be 00h.
             Q1           Q2              Q3              Q4          Words:                    3
          Decode      Determine   Determine            Read
                                                                      Cycles:                   3
                     source addr source addr         source reg
                                                                      Q Cycle Activity:
          Decode         No               No            Write
                      operation        operation      register ‘f’                                   Q1          Q2       Q3          Q4
                     No dummy                           (dest)
                                                                                                    Decode     No      No        No
                        read                                                                                 opera- operation operation
                                                                                                              tion
                                                                                                    Decode     Read Process     No
Example:              MOVSF       [05h], REG2                                                                 register  data operation
     Before Instruction                                                                                      “z” (src.)
           FSR2           =      80h                                                                Decode     No      No       Write
           Contents                                                                                          opera- operation register
           of 85h         =      33h
           REG2           =      11h                                                                          tion           “f” (dest.)
     After Instruction                                                                                         No
           FSR2           =      80h                                                                         dummy
           Contents                                                                                           read
           of 85h         =      33h
           REG2           =      33h

                                                                      Example:                  MOVSFL        [05h], REG2
                                                                           Before Instruction
                                                                                 FSR2            =         80h
                                                                                 Contents of 85h =         33h
                                                                                 REG2            =         11h
                                                                           After Instruction
                                                                                 FSR2            =         80h
                                                                                 Contents of 85h =         33h


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 711
                          PIC18(L)F26/27/45/46/47/55/56/57K42

MOVSS                 Move Indexed to Indexed                     PUSHL               Store Literal at FSR2, Decrement FSR2
Syntax:               MOVSS [zs], [zd]                            Syntax:             PUSHL k
Operands:             0  zs  127                                Operands:           0k  255
                      0  zd  127
                                                                  Operation:          k  (FSR2),
Operation:            ((FSR2) + zs)  ((FSR2) + zd)                                   FSR2 – 1  FSR2
Status Affected:      None
                                                                  Status Affected:    None
Encoding:
                                                                  Encoding:               1111        1010        kkkk       kkkk
1st word (source)         1110         1011    1zzz    zzzzs
2nd word (dest.)          1111         xxxx    xzzz    zzzzd      Description:        The 8-bit literal ‘k’ is written to the data
                                                                                      memory address specified by FSR2. FSR2
Description           The contents of the source register are
                                                                                      is decremented by 1 after the operation.
                      moved to the destination register. The
                                                                                      This instruction allows users to push values
                      addresses of the source and destination
                                                                                      onto a software stack.
                      registers are determined by adding the
                      7-bit literal offsets ‘zs’ or ‘zd’,         Words:              1
                      respectively, to the value of FSR2. Both
                                                                  Cycles:             1
                      registers can be located anywhere in
                      the 16 Kbyte data space (0000h to           Q Cycle Activity:
                      3FFFh).                                                  Q1            Q2              Q3              Q4
                      The MOVSS instruction cannot use the                  Decode         Read ‘k’      Process          Write to
                      PCL, TOSU, TOSH or TOSL as the                                                       data          destination
                      destination register.
                      If the resultant source address points to
                      an indirect addressing register, the        Example:                PUSHL 08h
                      value returned will be 00h. If the
                      resultant destination address points to          Before Instruction
                      an indirect addressing register, the                  FSR2H:FSR2L                  =    01ECh
                                                                            Memory (01ECh)               =    00h
                      instruction will execute as a NOP.
Words:                2                                                After Instruction
Cycles:               2                                                      FSR2H:FSR2L                 =    01EBh
                                                                             Memory (01ECh)              =    08h
Q Cycle Activity:
             Q1           Q2              Q3          Q4
          Decode     Determine   Determine           Read
                    source addr source addr        source reg
          Decode     Determine         Determine      Write
                     dest addr         dest addr   to dest reg


Example:              MOVSS [05h], [06h]
     Before Instruction
           FSR2           =      80h
           Contents
           of 85h         =      33h
           Contents
           of 86h         =      11h
     After Instruction
           FSR2           =      80h
           Contents
           of 85h         =      33h
           Contents
           of 86h         =      33h


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 712
                              PIC18(L)F26/27/45/46/47/55/56/57K42

SUBULNK            Subtract Literal from FSR2 and Return
Syntax:            SUBULNK k
Operands:          0  k  63
Operation:         FSR2 – k  FSR2
                   (TOS) PC
Status Affected: None
Encoding:              1110         1001        11kk      kkkk
Description:       The 6-bit literal ‘k’ is subtracted from the
                   contents of the FSR2. A RETURN is then
                   executed by loading the PC with the TOS.
                   The instruction takes two cycles to
                   execute; a NOP is performed during the
                   second cycle.
                   This may be thought of as a special case of
                   the SUBFSR instruction, where f = 3 (binary
                   ‘11’); it operates only on FSR2.
Words:             1
Cycles:            2
Q Cycle Activity:
             Q1               Q2              Q3           Q4
          Decode             Read          Process      Write to
                          literal ‘k’       Data       destination
           No             No                 No          No
         Operation      Operation          Operation   Operation


Example:                  SUBULNK 23h
     Before Instruction
          FSR2       =        03FFh
          PC         =        0100h
     After Instruction
           FSR2       =       03DCh
           PC         =       (TOS)


 2017-2021 Microchip Technology Inc.                                DS40001919G-page 713
                       PIC18(L)F26/27/45/46/47/55/56/57K42
41.2.3      BYTE-ORIENTED AND                                41.2.3.1      Extended Instruction Syntax with
            BIT-ORIENTED INSTRUCTIONS IN                                   Standard PIC18 Commands
            INDEXED LITERAL OFFSET MODE                      When the extended instruction set is enabled, the file
  Note:     Enabling the PIC18 instruction set               register argument, ‘f’, in the standard byte-oriented and
            extension may cause legacy applications          bit-oriented commands is replaced with the literal offset
            to behave erratically or fail entirely.          value, ‘k’. As already noted, this occurs only when ‘f’ is
                                                             less than or equal to 5Fh. When an offset value is used,
In addition to eight new commands in the extended set,       it must be indicated by square brackets (“[ ]”). As with
enabling the extended instruction set also enables           the extended instructions, the use of brackets indicates
Indexed Literal Offset Addressing mode (Section              to the compiler that the value is to be interpreted as an
4.8.1 “Indexed Addressing with Literal Offset”).             index or an offset. Omitting the brackets, or using a
This has a significant impact on the way that many           value greater than 5Fh within brackets, will generate an
commands of the standard PIC18 instruction set are           error in the MPASM assembler.
interpreted.
                                                             If the index argument is properly bracketed for Indexed
When the extended set is disabled, addresses                 Literal Offset Addressing, the Access RAM argument is
embedded in opcodes are treated as literal memory            never specified; it will automatically be assumed to be
locations: either as a location in the Access Bank (‘a’ =    ‘0’. This is in contrast to standard operation (extended
0), or in a GPR bank designated by the BSR (‘a’ = 1).        instruction set disabled) when ‘a’ is set on the basis of
When the extended instruction set is enabled and ‘a’ =       the target address. Declaring the Access RAM bit in
0, however, a file register argument of 5Fh or less is       this mode will also generate an error in the MPASM
interpreted as an offset from the pointer value in FSR2      assembler.
and not as a literal address. For practical purposes, this
                                                             The destination argument, ‘d’, functions as before.
means that all instructions that use the Access RAM bit
as an argument – that is, all byte-oriented and bit-         In the latest versions of the MPASM™ assembler,
oriented instructions, or almost half of the core PIC18      language support for the extended instruction set must
instructions – may behave differently when the               be explicitly invoked. This is done with either the
extended instruction set is enabled.                         command line option, /y, or the PE directive in the
                                                             source listing.
When the content of FSR2 is 00h, the boundaries of the
Access RAM are essentially remapped to their original
                                                             41.2.4      CONSIDERATIONS WHEN
values. This may be useful in creating backward
                                                                         ENABLING THE EXTENDED
compatible code. If this technique is used, it may be
necessary to save the value of FSR2 and restore it                       INSTRUCTION SET
when moving back and forth between C and assembly            It is important to note that the extensions to the
routines in order to preserve the Stack Pointer. Users       instruction set may not be beneficial to all users. In
must also keep in mind the syntax requirements of the        particular, users who are not writing code that uses a
extended       instruction    set    (see     Section        software stack may not benefit from using the
41.2.3.1 “Extended       Instruction   Syntax     with       extensions to the instruction set.
Standard PIC18 Commands”).                                   Additionally, the Indexed Literal Offset Addressing
Although the Indexed Literal Offset Addressing mode          mode may create issues with legacy applications
can be very useful for dynamic stack and pointer             written to the PIC18 assembler. This is because
manipulation, it can also be very annoying if a simple       instructions in the legacy code may attempt to address
arithmetic operation is carried out on the wrong             registers in the Access Bank below 5Fh. Since these
register. Users who are accustomed to the PIC18              addresses are interpreted as literal offsets to FSR2
programming must keep in mind that, when the                 when the instruction set extension is enabled, the
extended instruction set is enabled, register addresses      application may read or write to the wrong data
of 5Fh or less are used for Indexed Literal Offset           addresses.
Addressing.                                                  When porting an application to the PIC18(L)F2x/
Representative examples of typical byte-oriented and         4xK42, it is very important to consider the type of code.
bit-oriented instructions in the Indexed Literal Offset      A large, re-entrant application that is written in ‘C’ and
Addressing mode are provided on the following page to        would benefit from efficient compilation will do well
show how execution is affected. The operand                  when using the instruction set extensions. Legacy
conditions shown in the examples are applicable to all       applications that heavily use the Access Bank will most
instructions of these types.                                 likely not benefit from using the extended instruction
                                                             set.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 714
                             PIC18(L)F26/27/45/46/47/55/56/57K42

                         ADD W to Indexed                                                          Bit Set Indexed
ADDWF                                                                       BSF
                         (Indexed Literal Offset mode)                                             (Indexed Literal Offset mode)
Syntax:                  ADDWF          [k] {,d}                            Syntax:                BSF [k], b
Operands:                0  k  95                                         Operands:              0  k  95
                         d  [0,1]                                                                 0b7
Operation:               (W) + ((FSR2) + k)  dest                          Operation:             1  ((FSR2) + k)<b>
Status Affected:         N, OV, C, DC, Z                                    Status Affected:       None
Encoding:                    0010        01d0       kkkk        kkkk        Encoding:                  1000           bbb0     kkkk      kkkk
Description:             The contents of W are added to the                 Description:           Bit ‘b’ of the register indicated by FSR2,
                         contents of the register indicated by                                     offset by the value ‘k’, is set.
                         FSR2, offset by the value ‘k’.
                                                                            Words:                 1
                         If ‘d’ is ‘0’, the result is stored in W. If ‘d’
                         is ‘1’, the result is stored back in               Cycles:                1
                         register ‘f’ (default).                            Q Cycle Activity:
Words:                   1                                                               Q1            Q2                 Q3            Q4
Cycles:                  1                                                            Decode          Read             Process     Write to
                                                                                                   literal ‘k’          Data      destination
Q Cycle Activity:
             Q1              Q2               Q3               Q4
                                                                            Example:              BSF                [FLAG_OFST], 7
          Decode         Read ‘k’          Process         Write to
                                                                                  Before Instruction
                                            Data          destination
                                                                                        FLAG_OFST                =     0Ah
                                                                                        FSR2                     =     0A00h
Example:                 ADDWF          [OFST] , 0                                      Contents
                                                                                        of 0A0Ah                 =     55h
     Before Instruction
                                                                                  After Instruction
           W                        =     17h                                           Contents
           OFST                     =     2Ch                                           of 0A0Ah                 =     D5h
           FSR2                     =     0A00h
           Contents
           of 0A2Ch                 =     20h
     After Instruction
            W                       =     37h
            Contents
                                                                                                   Set Indexed
                                                                            SETF
            of 0A2Ch                =     20h                                                      (Indexed Literal Offset mode)
                                                                            Syntax:                SETF [k]
                                                                            Operands:              0  k  95
                                                                            Operation:             FFh  ((FSR2) + k)
                                                                            Status Affected:       None
                                                                            Encoding:                  0110           1000     kkkk      kkkk
                                                                            Description:           The contents of the register indicated by
                                                                                                   FSR2, offset by ‘k’, are set to FFh.
                                                                            Words:                 1
                                                                            Cycles:                1
                                                                            Q Cycle Activity:
                                                                                         Q1            Q2                 Q3            Q4
                                                                                      Decode       Read ‘k’             Process        Write
                                                                                                                         Data         register


                                                                            Example:               SETF              [OFST]
                                                                                  Before Instruction
                                                                                        OFST            =        2Ch
                                                                                        FSR2            =        0A00h
                                                                                        Contents
                                                                                        of 0A2Ch        =        00h
                                                                                  After Instruction
                                                                                        Contents
                                                                                        of 0A2Ch        =        FFh


 2017-2021 Microchip Technology Inc.                                                                                  DS40001919G-page 715
                      PIC18(L)F26/27/45/46/47/55/56/57K42
41.2.5      SPECIAL CONSIDERATIONS WITH
            MICROCHIP MPLAB® IDE TOOLS
The latest versions of Microchip’s software tools have
been designed to fully support the extended instruction
set of the PIC18(L)F2x/4xK42 family of devices. This
includes the MPLAB XC8 C compiler, MPASM
assembler and MPLAB X Integrated Development
Environment (IDE).
When selecting a target device for software
development, MPLAB X IDE will automatically set
default Configuration bits for that device. The default
setting for the XINST Configuration bit is ‘0’, disabling
the extended instruction set and Indexed Literal Offset
Addressing mode. For proper execution of applications
developed to take advantage of the extended
instruction set, XINST must be set during
programming.
To develop software for the extended instruction set,
the user must enable support for the instructions and
the Indexed Addressing mode in their language tool(s).
Depending on the environment being used, this may be
done in several ways:
• A menu option, or dialog box within the
  environment, that allows the user to configure the
  language tool and its settings for the project
• A command line option
• A directive in the source code
These options vary between different compilers,
assemblers and development environments. Users are
encouraged to review the documentation accompanying
their development systems for the appropriate
information.


 2017-2021 Microchip Technology Inc.                       DS40001919G-page 716
