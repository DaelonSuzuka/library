                      PIC18(L)F26/27/45/46/47/55/56/57K42
14.0     CYCLIC REDUNDANCY CHECK
         (CRC) MODULE WITH MEMORY
         SCANNER
The Cyclic Redundancy Check (CRC) module provides
a software-configurable hardware-implemented CRC
checksum generator. This module includes the following
features:
• Any standard CRC up to 16 bits can be used
• Configurable Polynomial
• Any seed value up to 16 bits can be used
• Standard and reversed bit order available
• Augmented zeros can be added automatically or
  by the user
• Memory scanner for fast CRC calculations on
  program/Data EEPROM memory user data
• Software loadable data registers for
  communication CRC’s

14.1     CRC Module Overview
The CRC module provides a means for calculating a
check value of program/Data EEPROM memory. The
CRC module is coupled with a memory scanner for
faster CRC calculations. The memory scanner can
automatically provide data to the CRC module. The
CRC module can also be operated by directly writing
data to SFRs, without using a scanner.


 2017-2021 Microchip Technology Inc.                    DS40001919G-page 213
                       PIC18(L)F26/27/45/46/47/55/56/57K42
14.2     CRC Functional Overview
The CRC module can be used to detect bit errors in the
program memory using the built-in memory scanner or
through user input RAM memory. The CRC module can
accept up to a 16-bit polynomial with up to a 16-bit seed
value. A CRC calculated check value (or checksum)
will then be generated into the CRCACC[15:0] registers
for user storage. The CRC module uses an XOR shift
register implementation to perform the polynomial
division required for the CRC calculation.

EXAMPLE 14-1:           CRC EXAMPLE
                                                Rev. 10-000206A
                                                        1/8/2014


                       CRC-16-ANSI
                 x16 + x15 + x2 + 1 (17 bits)
          Standard 16-bit representation = 0x8005
                CRCXORH = 0b10000000
                CRCXORL = 0b0000010- (1)
                     Data Sequence:
                  0x55, 0x66, 0x77, 0x88
                     DLEN = 0b0111
                     PLEN = 0b1111

              Data entered into the CRC:
                    SHIFTM = 0:
       01010101 01100110 01110111 10001000
                    SHIFTM = 1:
       10101010 01100110 11101110 00010001

                Check Value (ACCM = 1):
                 SHIFTM = 0: 0x32D6
                CRCACCH = 0b00110010
                CRCACCL = 0b11010110
                 SHIFTM = 1: 0x6BA2
                CRCACCH = 0b01101011
                CRCACCL = 0b10100010

    Note 1: Bit 0 is unimplemented. The LSb of any
         CRC polynomial is always ‘1’ and will always
         be treated as a ‘1’ by the CRC for calculating
         the CRC check value. This bit will be read in
         software as a ‘0’.


 2017-2021 Microchip Technology Inc.                              DS40001919G-page 214
                        PIC18(L)F26/27/45/46/47/55/56/57K42
14.3      CRC Polynomial Implementation                                     The X16 and X0 = 1 terms are the MSb and LSb
                                                                            controlled by hardware. The X15 and X2 terms are
Any polynomial can be used. The polynomial and                              specified by setting the corresponding CRCXOR[15:0]
accumulator sizes are determined by the PLEN[3:0]                           bits with the value of ‘0x8004’. The actual value is
bits. For an n-bit accumulator, PLEN = n-1 and the                          ‘0x8005’ because the hardware sets the LSb to 1.
corresponding polynomial is n+1 bits. Therefore the                         However, the LSb of the CRCXORL register is
accumulator can be any size up to 16 bits with a                            unimplemented and always reads as ‘0’. Refer to
corresponding polynomial up to 17 bits. The MSb and                         Example 14-1.
LSb of the polynomial are always ‘1’ which is forced by
hardware. All polynomial bits between the MSb and
LSb are specified by the CRCXOR registers. For
example, when using CRC-16-ANSI, the polynomial is
defined as X16+X15+X2+1.


EXAMPLE 14-2:              CRC LFSR EXAMPLE


                                                                                                                   Rev. 10-000207A
                                        Linear Feedback Shift Register for CRC-16-ANSI                                    5/27/2014


                                                           x16 + x15 + x2 + 1
     Data in
                                                     Augmentation Mode ON

               b15          b14   b13    b12   b11   b10      b9     b8    b7    b6   b5    b4   b3    b2         b1          b0


                                                                                                                              Data in
                                                     Augmentation Mode OFF

        b15          b14    b13   b12    b11   b10    b9      b8     b7    b6    b5   b4    b3   b2         b1    b0


14.4      CRC Data Sources                                                  14.4.1     CRC FROM USER DATA
Data can be input to the CRC module in two ways:                            To use the CRC module on data input from the user, the
                                                                            user must write the data to the CRCDAT registers. The
  - User data using the CRCDAT registers                                    data from the CRCDAT registers will be latched into the
    (CRCDATH and CRCDATL)                                                   shift registers on any write to the CRCDATL register.
  - Program memory using the Program Memory
    Scanner                                                                 14.4.2     CRC FROM FLASH
To set the number of bits of data, up to 16 bits, the                       To use the CRC module on data located in Program
DLEN bits of CRCCON1 must be set accordingly. Only                          memory, the user can initialize the Program Memory
data bits in CRCDAT registers up to DLEN will be used,                      Scanner as defined in Section 14.8, Scanner Module
other data bits in CRCDAT registers will be ignored.                        Overview.
Data is moved into the CRCSHIFT as an intermediate
to calculate the check value located in the CRCACC
registers.
The SHIFTM bit is used to determine the bit order of the
data being shifted into the accumulator. If SHIFTM is
not set, the data will be shifted in MSb first (Big Endian).
The value of DLEN will determine the MSb. If SHIFTM
bit is set, the data will be shifted into the accumulator in
reversed order, LSb first (Little Endian).
The CRC module can be seeded with an initial value by
setting the CRCACC[15:0] registers to the appropriate
value before beginning the CRC.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 215
                      PIC18(L)F26/27/45/46/47/55/56/57K42
14.5     CRC Check Value                                   14.7     Configuring the CRC
The CRC check value will be located in the CRCACC          The following steps illustrate how to properly configure
registers after the CRC calculation has finished. The      the CRC.
check value will depend on two mode settings of the        1.  Determine if the automatic program memory
CRCCON0 register: ACCM and SHIFTM. When the                    scan will be used with the scanner or manual
ACCM bit is set, the CRC module augments the data              calculation through the SFR interface and
with a number of zeros equal to the length of the              perform the actions specified in Section
polynomial to align the final check value. When the            14.4 “CRC Data Sources”, depending on which
ACCM bit is not set, the CRC will stop at the end of the       decision was made.
data. A number of zeros equal to the length of the
                                                           2. If desired, seed a starting CRC value into the
polynomial can then be entered into CRCDAT to find
                                                               CRCACCH/L registers.
the same check value as augmented mode.
Alternatively, the expected check value can be entered     3. Program the CRCXORH/L registers with the
at this point to make the final result equal ‘0’.              desired generator polynomial.
                                                           4. Program the DLEN[3:0] bits of the CRCCON1
When the CRC check value is computed with the
                                                               register with the length of the data word - 1 (refer
SHIFTM bit set, selecting LSb first, and the ACCM bit
                                                               to Example 14-1). This determines how many
is also set, then the final value in the CRCACC
                                                               times the shifter will shift into the accumulator for
registers will be reversed such that the LSb will be in
                                                               each data word.
the MSb position and vice versa. This is the expected
check value in bit reversed form. If you are creating a    5. Program the PLEN[3:0] bits of the CRCCON1
check value to be appended to a data stream, then a bit        register with the length of the polynomial -2
reversal must be performed on the final value to               (refer to Example 14-1).
achieve the correct checksum. You can use the CRC to       6. Determine whether shifting in trailing zeros is
do this reversal by the following method:                      desired and set the ACCM bit of the CRCCON0
                                                               register appropriately.
• Save the CRCACC value in user RAM space
• Clear the CRCACC registers                               7. Likewise, determine whether the MSb or LSb
• Clear the CRCXOR registers                                   may be shifted first and write the SHIFTM bit of
• Write the saved CRCACC value to the CRCDAT                   the CRCCON0 register appropriately.
  input.                                                   8. Write the GO bit of the CRCCON0 register to
                                                               begin the shifting process.
The properly oriented check value will be in the
CRCACC registers as the result.                            9a. If manual SFR entry is used, monitor the FULL bit
                                                               of the CRCCON0 register. When FULL = 0,
                                                               another word of data can be written to the
14.6     CRC Interrupt
                                                               CRCDATH/L registers, keeping in mind that
The CRC will generate an interrupt when the BUSY bit           CRCDATH may be written first if the data has
transitions from 1 to 0. The CRCIF Interrupt Flag is set       more than eight bits, as the shifter will begin upon
every time the BUSY bit transitions, regardless of             the CRCDATL register being written.
whether or not the CRC interrupt is enabled. The           9b. If the scanner is used, the scanner will
CRCIF bit can only be cleared in software.                     automatically load words into the CRCDATH/L
                                                               registers as needed, as long as the GO bit is set.
                                                           10a.If manual entry is used, monitor the CRCIF (and
                                                               BUSY bit to determine when the completed
                                                               CRC calculation can be read from CRCACCH/L
                                                               registers.
                                                           10b.If using the memory scanner, monitor the
                                                               SCANIF (or the GO bit) for the scanner to finish
                                                               pushing information into the CRCDAT registers.
                                                               After the scanner is completed, monitor the
                                                               BUSY bit to determine that the CRC has been
                                                               completed and the check value can be read
                                                               from the CRCACC registers. If both the interrupt
                                                               flags are set and the BUSY and GO bits are
                                                               cleared, the completed CRC calculation can be
                                                               read from the CRCACCH/L registers.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 216
                       PIC18(L)F26/27/45/46/47/55/56/57K42
14.8     Scanner Module Overview                          14.11 Scanning Modes
The Scanner allows segments of the Program Flash          The interaction of the scanner with the system
Memory or Data EEPROM, to be read out (scanned) to        operation is controlled by the priority selection in the
the CRC Peripheral. The Scanner module interacts          System Arbiter (see Section 3.2 “Memory Access
with the CRC module and supplies it data one word at      Scheme”). Additionally, BURSTMD and TRIGEN also
a time. Data is fetched from the address range defined    determine the operation of the Scanner.
by SCANLADR registers up to the SCANHADR
registers.                                                14.11.1     TRIGEN = 0, BURSTMD = 0
The Scanner begins operation when the SGO bit is set      In this case, the memory access request is granted to
(SCANCON0 Register) and ends when either SGO is           the scanner if no other higher priority source is
cleared by the user or when SCANLADR increments           requesting access.
past SCANHADR. The SGO bit is also cleared by             All sources with lower priority than the scanner will get
clearing the EN bit (CRCCON0 register).                   the memory access cycles that are not utilized by the
                                                          scanner.
14.9     Configuring the Scanner
                                                          14.11.2     TRIGEN = 1, BURSTMD = 0
The scanner module may be used in conjunction with
the CRC module to perform a CRC calculation over a        In this case, the memory access request is generated
range of program memory or Data EEPROM                    when the CRC module is ready to accept.
addresses. In order to set up the scanner to work with    The memory access request is granted to the scanner
the CRC, perform the following steps:                     if no other higher priority source is requesting access.
1.   Set up the CRC module (See Section 14.7              All sources with lower priority than the scanner will get
     “Configuring     the CRC”) and enable the            the memory access cycles that are not utilized by the
     Scanner module by setting the EN bit in the          scanner.
     SCANCON0 register.                                   The memory access request is granted to the scanner
2.   Choose which memory region the Scanner               if no other higher priority source is requesting access.
     module may operate on and set the MREG bit of        All sources with lower priority than the scanner will get
     the SCANCON0 register appropriately.
                                                          the memory access cycles that are not utilized by the
3.   If trigger is used for scanner operation, set the    scanner.
     TRIGEN bit of the SCANCON0 register and
     select the trigger source using SCANTRIG             14.11.3     TRIGEN = x, BURSTMD = 1
     register. Select the trigger source using
                                                          In this case, the memory access is always requested
     SCANTRIG register and then set the TRIGEN
                                                          by the scanner.
     bit of the SCANCON0 register. See Table 14-1
     for Scanner Operation.                               The memory access request is granted to the scanner
4.   If Burst mode of operation is desired, set the       if no other higher priority source is requesting access.
     BURSTMD bit (SCANCON0 register). See                 The memory access cycles will not be granted to lower
     Table 14-1 for Scanner Operation.                    priority sources than the scanner until it completes
                                                          operation i.e. SGO = 0 (SCANCON0 register)
5.   Set the SCANLADRL/H/U and SCANHADRL/H/
     U registers with the beginning and ending
     locations in memory that are to be scanned.
                                                            Note:     If TRIGEN = 1 and BURSTMD = 1, the
6.   Select the priority level for the Scanner module                 user may ensure that the trigger source is
     (See Section 3.1 “System Arbitration”) and                       active for the Scanner operation to
     lock the priorities (See Section 3.1.1 “Priority                 complete.
     Lock”).
7.   Both CRCEN and CRCGO bits must be enabled
     to use the scanner. Setting the SGO bit will start
     the scanner operation.

14.10 Scanner Interrupt
The scanner will trigger an interrupt when the
SCANLADR increments past SCANHADR. The
SCANIF bit can only be cleared in software.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 217
                         PIC18(L)F26/27/45/46/47/55/56/57K42
14.12 Register Definitions: CRC and Scanner Control
Long bit name prefixes for the CRC and Scanner
peripherals are shown below. Refer to Section
1.3.2.2 “Long Bit Names” for more information.

          Peripheral                  Bit Name Prefix
              CRC                             CRC


REGISTER 14-1:            CRCCON0: CRC CONTROL REGISTER 0
    R/W-0/0            R/W-0/0            R-0              R/W-0/0          U-0            U-0             R/W-0/0        R-0
        EN              GO               BUSY              ACCM              —             —               SHIFTM        FULL
bit 7                                                                                                                           bit 0


Legend:
R = Readable bit                    W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                    ‘0’ = Bit is cleared


bit 7              EN: CRC Enable bit
                   1 = CRC module is enabled
                   0 = CRC is disabled
bit 6              GO: CRC Go bit
                   1 = Start CRC serial shifter
                   0 = CRC serial shifter turned off
bit 5              BUSY: CRC Busy bit
                   1 = Shifting in progress or pending
                   0 = All valid bits in shifter have been shifted into accumulator
bit 4              ACCM: Accumulator Mode bit
                   1 = Data is concatenated with zeros
                   0 = Data is not concatenated with zeros
bit 3-2            Unimplemented: Read as ‘0’
bit 1              SHIFTM: Shift Mode bit
                   1 = Shift right (LSb)
                   0 = Shift left (MSb)
bit 0              FULL: Data Path Full Indicator bit
                   1 = CRCDATH/L registers are full
                   0 = CRCDATH/L registers have shifted their data into the shifter


REGISTER 14-2:            CRCCON1: CRC CONTROL REGISTER 1
    R/W-0/0            R/W-0/0         R/W-0/0             R/W-0/0       R/W-0/0        R/W-0/0            R/W-0/0      R/W-0/0
                             DLEN[3:0]                                                           PLEN[3:0]
bit 7                                                                                                                           bit 0


Legend:
R = Readable bit                    W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                    ‘0’ = Bit is cleared


bit 7-4            DLEN[3:0]: Data Length bits
                   Denotes the length of the data word -1 (See Example 14-1)
bit 3-0            PLEN[3:0]: Polynomial Length bits
                   Denotes the length of the polynomial -1 (See Example 14-1)


 2017-2021 Microchip Technology Inc.                                                                         DS40001919G-page 218
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 14-3:           CRCDATH: CRC DATA HIGH BYTE REGISTER
    R/W-xx           R/W-x/x         R/W-x/x         R/W-x/x       R/W-x/x       R/W-x/x        R/W-x/x         R/W-x/x
                                                          DATA[15:8]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            DATA[15:8]: CRC Input/Output Data bits


REGISTER 14-4:           CRCDATL: CRC DATA LOW BYTE REGISTER
    R/W-xx           R/W-x/x         R/W-x/x         R/W-x/x       R/W-x/x       R/W-x/x        R/W-x/x         R/W-x/x
                                                           DATA[7:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            DATA[7:0]: CRC Input/Output Data bits
                   Writing to this register fills the shifter.


REGISTER 14-5:           CRCACCH: CRC ACCUMULATOR HIGH BYTE REGISTER
   R/W-0/0           R/W-0/0         R/W-0/0         R/W-0/0       R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                           ACC[15:8]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            ACC[15:8]: CRC Accumulator Register bits


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 219
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 14-6:           CRCACCL: CRC ACCUMULATOR LOW BYTE REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0          R/W-0/0         R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                              ACC[7:0]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            ACC[7:0]: CRC Accumulator Register bits


REGISTER 14-7:           CRCSHIFTH: CRC SHIFT HIGH BYTE REGISTER
        R-0            R-0              R-0             R-0              R-0        R-0            R-0             R-0
                                                          SHIFT[15:8]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            SHIFT[15:8]: CRC Shifter Register bits
                   Reading from this register reads the CRC Shifter.


REGISTER 14-8:           CRCSHIFTL: CRC SHIFT LOW BYTE REGISTER
        R-0            R-0              R-0             R-0              R-0        R-0            R-0             R-0
                                                          SHIFT[7:0]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            SHIFT[7:0]: CRC Shifter Register bits
                   Reading from this register reads the CRC Shifter.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 220
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 14-9:          CRCXORH: CRC XOR HIGH BYTE REGISTER
    R/W-x/x          R/W-x/x       R/W-x/x         R/W-x/x        R/W-x/x       R/W-x/x        R/W-x/x         R/W-x/x
                                                            X[15:8]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            X[15:8]: XOR of Polynomial Term Xn Enable bits


REGISTER 14-10: CRCXORL: CRC XOR LOW BYTE REGISTER
    R/W-x/x          R/W-x/x       R/W-x/x         R/W-x/x        R/W-x/x       R/W-x/x        R/W-x/x           U-1
                                                   X[7:1]                                                        —
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                W = Writable bit                U = Unimplemented bit
u = Bit is unchanged            x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-1            X[7:1]: XOR of Polynomial Term Xn Enable bits
bit 0              Unimplemented: Read as ‘1’


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 221
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 14-11: SCANCON0: SCANNER ACCESS CONTROL REGISTER 0
   R/W-0/0            R/W-0/0     R/W/HC-0/0             U-0         U-0        R/W-0/0          R/W-0/0       R-0/0
        EN           TRIGEN           SGO                —           —           MREG        BURSTMD          BUSY
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         HC = Bit is cleared by hardware


bit 7              EN: Scanner Enable bit(1)
                   1 = Scanner is enabled
                   0 = Scanner is disabled
bit 6              TRIGEN: Scanner Trigger Enable bit(2)
                   1 = Scanner trigger is enabled
                   0 = Scanner trigger is disabled
                   Refer Table 14-1.
bit 5              SGO: Scanner GO bit(3, 4)
                   1 = When the CRC is ready, the Memory region set by the MREG bit will be accessed and data is passed
                       to the CRC peripheral.
                   0 = Scanner operations will not occur
bit 4-3            Unimplemented: Read as ‘0’
bit 2              MREG: Scanner Memory Region Select bit(2)
                   1 = Scanner address points to Data EEPROM
                   0 = Scanner address points to Program Flash Memory
bit 1              BURSTMD: Scanner Burst Mode bit
                   1 = Memory access request to the CPU Arbiter is always true
                   0 = Memory access request to the CPU Arbiter is dependent on the CRC request and Trigger
                   Refer Table 14-1.
bit 0              BUSY: Scanner Busy Indicator bit
                   1 = Scanner cycle is in process
                   0 = Scanner cycle is compete (or never started)

Note 1:        Setting EN = 1 (SCANCON0 register) does not affect any other register content.
     2:        Scanner trigger selection can be set using the SCANTRIG register.
     3:        This bit can be cleared in software. It is cleared in hardware when LADR>HADR (and a data cycle is not
               occurring) or when CRCGO = 0 (CRCCON0 register).
          4:   CRCEN and CRCGO bits (CRCCON0 register) must be set before setting the SGO bit.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 222
                        PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 14-1:          SCANNER OPERATING MODES(1)
   TRIGEN           BURSTMD                                            Scanner Operation
        0               0        Memory access is requested when the CRC module is ready to accept data; the
                                 request is granted if no other higher priority source request is pending.
        1               0        Memory access is requested when the CRC module is ready to accept data and trigger
                                 selection is true; the request is granted if no other higher priority source request is
                                 pending.
        x               1        Memory access is always requested, the request is granted if no other higher priority
                                 source request is pending.
Note 1:        See Section 3.1 “System Arbitration” for Priority selection and Section 3.2 “Memory Access Scheme” for
               Memory Access Scheme.


REGISTER 14-12: SCANLADRU: SCAN LOW ADDRESS UPPER BYTE REGISTER
        U-0             U-0         R/W-0/0          R/W-0/0      R/W-0/0           R/W-0/0    R/W-0/0        R/W-0/0
        —                —                                                LADR[21:16](1,2)
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            LADR[21:16]: Scan Start/Current Address bits(1,2)
                   Upper bits of the current address to be fetched from, value increments on each fetch of memory.

Note 1:        Registers SCANLADRU/H/L form a 22-bit value, but are not guarded for atomic or asynchronous access;
               registers may only be read or written while SGO = 0 (SCANCON0 register).
          2:   While SGO = 1 (SCANCON0 register), writing to this register is ignored.


REGISTER 14-13: SCANLADRH: SCAN LOW ADDRESS HIGH BYTE REGISTER
   R/W-0/0            R/W-0/0       R/W-0/0          R/W-0/0      R/W-0/0           R/W-0/0    R/W-0/0        R/W-0/0
                                                                      (1, 2)
                                                         LADR[15:8]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            LADR[15:8]: Scan Start/Current Address bits(1, 2)
                   Most Significant bits of the current address to be fetched from, value increments on each fetch of
                   memory.
Note 1:        Registers SCANLADRU/H/L form a 22-bit value, but are not guarded for atomic or asynchronous access;
               registers may only be read or written while SGO = 0 (SCANCON0 register).
          2:   While SGO = 1 (SCANCON0 register), writing to this register is ignored.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 223
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 14-14: SCANLADRL: SCAN LOW ADDRESS LOW BYTE REGISTER
   R/W-0/0           R/W-0/0        R/W-0/0         R/W-0/0       R/W-0/0        R/W-0/0       R/W-0/0        R/W-0/0
                                                        LADR[7:0](1, 2)
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            LADR[7:0]: Scan Start/Current Address bits(1, 2)
                   Least Significant bits of the current address to be fetched from, value increments on each fetch of
                   memory
Note 1:        Registers SCANLADRU/H/L form a 22-bit value, but are not guarded for atomic or asynchronous access;
               registers may only be read or written while SGO = 0 (SCANCON0 register).
          2:   While SGO = 1 (SCANCON0 register), writing to this register is ignored.


REGISTER 14-15: SCANHADRU: SCAN HIGH ADDRESS UPPER BYTE REGISTER
        U-0             U-0         R/W-1/1         R/W-1/1       R/W-1/1        R/W-1/1       R/W-1/1        R/W-1/1
        —               —                                                 HADR[21:16]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            HADR[21:16]: Scan End Address bits(1, 2)
                   Upper bits of the address at the end of the designated scan

Note 1:        Registers SCANHADRU/H/L form a 22-bit value but are not guarded for atomic or asynchronous access;
               registers may only be read or written while SGO = 0 (SCANCON0 register).
          2:   While SGO = 1 (SCANCON0 register), writing to this register is ignored.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 224
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 14-16: SCANHADRH: SCAN HIGH ADDRESS HIGH BYTE REGISTER
    R/W-1/1           R/W-1/1          R/W-1/1             R/W-1/1        R/W-1/1       R/W-1/1           R/W-1/1      R/W-1/1
                                                             HADR[15:8](1, 2)
bit 7                                                                                                                        bit 0


Legend:
R = Readable bit                    W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                    ‘0’ = Bit is cleared


bit 7-0             HADR[15:8]: Scan End Address bits(1, 2)
                    Most Significant bits of the address at the end of the designated scan
Note 1:        Registers SCANHADRU/H/L form a 22-bit value, but are not guarded for atomic or asynchronous access;
               registers may only be read or written while SGO = 0 (SCANCON0 register).
          2:   While SGO = 1 (SCANCON0 register), writing to this register is ignored.


REGISTER 14-17: SCANHADRL: SCAN HIGH ADDRESS LOW BYTE REGISTER
    R/W-1/1            R/W-1/1          R/W-1/1            R/W-1/1        R/W-1/1        R/W-1/1          R/W-1/1      R/W-1/1
                                                                          (1, 2)
                                                              HADR[7:0]
bit 7                                                                                                                        bit 0


Legend:
R = Readable bit                    W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                    ‘0’ = Bit is cleared


bit 7-0             HADR[7:0]: Scan End Address bits(1, 2)
                    Least Significant bits of the address at the end of the designated scan

Note 1:        Registers SCANHADRU/H/L form a 22-bit value, but are not guarded for atomic or asynchronous access; registers may
               only be read or written while SGO = 0 (SCANCON0 register).
          2:   While SGO = 1 (SCANCON0 register), writing to this register is ignored.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 225
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 14-18: SCANTRIG: SCAN TRIGGER SELECTION REGISTER
        U-0            U-0              U-0             U-0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
        —               —               —               —                           TSEL[3:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-4            Unimplemented: Read as ‘0’
bit 3-0            TSEL[3:0]: Scanner Data Trigger Input Selection bits
                   1111 = Reserved
                      •
                      •
                      •

                   1010 =    Reserved
                   1001 =    SMT1_output
                   1000 =    TMR6_postscaled
                   0111 =    TMR5_output
                   0110 =    TMR4_postscaled
                   0101 =    TMR3_output
                   0100 =    TMR2_postscaled
                   0011 =    TMR1_output
                   0010 =    TMR0_output
                   0001 =    CLKREF_output
                   0000 =    LFINTOSC


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 226
                      PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 14-2:       SUMMARY OF REGISTERS ASSOCIATED WITH CRC
                                                                                                                Register
     Name          Bit 7        Bit 6       Bit 5      Bit 4         Bit 3      Bit 2       Bit 1       Bit 0
                                                                                                                on Page
CRCACCH                                                    ACC[15:8]                                               220
CRCACCL                                                      ACC[7:0]                                              221
CRCCON0             EN           GO         BUSY      ACCM               —       —        SHIFTM        FULL       219
CRCCON1                           DLEN[3:0]                                          PLEN[3:0]                     219
CRCDATH                                                   DATA[15:8]                                               220
CRCDATL                                                    DATA[7:0]                                               220
CRCSHIFTH                                                 SHIFT[15:8]                                              221
CRCSHIFTL                                                 SHIFT[7:0]                                               221
CRCXORH                                                        X[15:8]                                             222
CRCXORL                                               X[7:1]                                             —         222
SCANCON0            EN        TRIGEN        SGO          —               —     MREG      BURSTMD        BUSY       223
SCANHADRU            —           —                                       HADR[21:16]                               225
SCANHADRH                                                 HADR[15:8]                                               226
SCANHADRL                                                 HADR[7:0]                                                226
SCANLADRU            —           —                                       LADR[21:16]                               224
SCANLADRH                                                 LADR[15:8]                                               224
SCANLADRL                                                  LADR[7:0]                                               225
SCANTRIG             —           —            —          —                           TSEL[3:0]                     227
Legend:     — = unimplemented location, read as ‘0’. Shaded cells are not used for the CRC module.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 227
