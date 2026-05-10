                                                                                                       PIC18F27/47/57Q43
                                                                                CRC - Cyclic Redundancy Check Module with
                                                                                                          Memory Scanner

13.    CRC - Cyclic Redundancy Check Module with Memory Scanner
       The Cyclic Redundancy Check (CRC) module provides a software-configurable hardware-
       implemented CRC checksum generator. This module includes the following features:
       •   Any standard CRC up to 16 bits can be used
       •   Configurable polynomial
       •   Any seed value up to 16 bits can be used
       •   Standard and reversed bit order available
       •   Augmented zeros can be added automatically or by the user
       •   Memory scanner for fast CRC calculations on program memory user data
       •   Software loadable data registers for communication CRCs

13.1   CRC Module Overview
       The CRC module provides a means for calculating a check value of program memory. The CRC
       module is coupled with a memory scanner for faster CRC calculations. The memory scanner can
       automatically provide data to the CRC module. The CRC module can also be operated by directly
       writing data to SFRs, without using a scanner.

13.2   CRC Functional Overview
       The CRC module can be used to detect bit errors in the Flash memory using the built-in
       memory scanner or through user input RAM memory. The CRC module can accept up to a 16-bit
       polynomial with up to a 16-bit seed value. A CRC calculated check value (or checksum) will then be
       generated into the CRCACC register for user storage. The CRC module uses an XOR shift register
       implementation to perform the polynomial division required for the CRC calculation.

13.3   CRC Polynomial Implementation
       Any polynomial can be used. The polynomial and accumulator sizes are determined by the PLEN
       bits. For an n-bit accumulator, PLEN = n-1 and the corresponding polynomial is n+1 bits. Therefore,
       the accumulator can be any size up to 16 bits with a corresponding polynomial up to 17 bits. The
       MSb and LSb of the polynomial are always ‘1’ which is forced by hardware. Therefore, the LSb of the
       CRCXORL register is hardwired high and always reads as ‘1’.
       All polynomial bits between the MSb and LSb are specified by the CRCXOR registers. For example,
       when using CRC16-ANSI, the polynomial is defined as X16+X15+X2+1. The X16 and X0 = 1 terms
       are the MSb and LSb controlled by hardware. The X15 and X2 terms are specified by setting the
       corresponding CRCXOR[15:0] bits with the value of 0x8004. Reading the CRCXOR registers will return
       0x8005 because the LSb is hardwired high. Refer to the following example.


--- p222 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                CRC - Cyclic Redundancy Check Module with
                                                                                                          Memory Scanner
       Figure 13-1. CRC Example

                                                                                  Rev. 10-000206B
                                                                                         12/3/2018


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
                                  be treated as a ‘1’ by the CRC for
                                  calculating the CRC check value. This bit will
                                  be read in software as a ‘0’.


13.4   CRC Data Sources
       Data can be input to the CRC module in two ways:
       •   User data using the CRCDATA registers
       •   From Flash memory using the program memory scanner
       Up to 16 bits of data per word are specified with the DLEN bits. Only the number of data bits in
       the CRCDATA registers specified by DLEN will be used, other data bits in CRCDATA registers will be
       ignored.


--- p223 ---
                                                                                                                         PIC18F27/47/57Q43
                                                                                                  CRC - Cyclic Redundancy Check Module with
                                                                                                                            Memory Scanner
          Data are moved into the CRCSHIFT as an intermediate to calculate the check value located in the
          CRCACC registers.
          The SHIFTM bit is used to determine the bit order of the data being shifted into the accumulator and
          the bit order of the result. The value of DLEN will determine which bit in CRCDATA is the MSb.

          Figure 13-2. CRC Process
          MSb first (SHIFTM = 0)
          MSb           LSb                                                                                                       MSb        LSb
                                                                                                             CRC Feedback           Input Data


            Accumulator
            After n sums


          Industry standard LSb first
          MSb           LSb                                                                                                       MSb        LSb
              Input Data                CRC Feedback


                                                                                                                                   Accumulator
                                                                                                                                   After n sums


          LSb first (SHIFTM = 1)
          LSb          MSb
                                                                                                            CRC Feedback


             Accumulator                                                                                    MSb        LSb
            After n sums
                                                                                                              Input Data
            (bit reversed)


          When SHIFTM is not set, the data will be shifted in MSb first and the result will be big-endian. When
          SHIFTM bit is set, the data will be shifted into the accumulator in reversed order, LSb first and the
          result will be little-endian.
          The CRC module can be seeded with an initial value by setting the CRCACC registers to the
          appropriate value before beginning the CRC.

          Figure 13-3. CRC LFSR Example

                                                                                                                                                   Rev. 10-000207B
                                                Linear Feedback Shift Register for CRC-16-ANSI                                                            12/3/2018


                                                                     x16 + x15 + x2 + 1
Data in
                                                              Augmentation Mode ON

           b15                b14         b13    b12   b11     b10      b9     b8      b7    b6        b5     b4      b3     b2                   b1          b0


                                                                                                                                                              Data in
                                                              Augmentation Mode OFF

   b15               b14      b13         b12    b11   b10     b9       b8     b7      b6    b5        b4     b3      b2                b1        b0


--- p224 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                 CRC - Cyclic Redundancy Check Module with
                                                                                                           Memory Scanner
13.4.1 CRC from User Data
       To use the CRC module on data input from the user, the user must write the data to the CRCDATA
       register. The data from both the CRCDATH and CRCDATL registers will be latched into the shift
       registers when the CRCDATL register is written.

13.4.2 CRC from Flash
       To use the CRC module on data located in Flash memory, the user can initialize the program
       memory scanner as defined in the Scanner Module Overview section.

13.5   CRC Check Value
       The CRC check value will be located in the CRCACC registers after the CRC calculation has finished.
       The check value will depend on the ACCM and SHIFTM mode settings.
       When the ACCM bit is set, the CRC module augments the data with a number of zeros equal to the
       length of the polynomial to align the final check value. When the ACCM bit is not set, the CRC will
       stop at the end of the data. A number of zeros equal to the length of the polynomial can then be
       entered into CRCDATA to find the same check value as Augmented mode. Alternatively, the expected
       check value can be entered at this point to make the final result equal zero.
       When the CRC check value is computed with the SHIFTM bit set, selecting LSb first, and the ACCM
       bit is set, then the final value in the CRCACC registers will be reversed such that the LSb will be in
       the MSb position and vice versa (see Figure 13-2). This is the expected check value in bit reversed
       form. When creating a check value to be appended to a data stream, then a bit reversal must be
       performed on the final value to achieve the correct checksum. The CRC can be used to do this
       reversal by following the steps below:
       1. Save CRCACC value in user RAM space.
       2. Clear the CRCACC registers.
       3. Clear the CRCXOR registers.
       4. Write the saved CRCACC value to the CRCDATA input.
       The properly oriented check value will be in the CRCACC registers as the result.

13.6   CRC Interrupt
       The CRC will generate an interrupt when the BUSY bit transitions from ‘1’ to ‘0’. The CRCIF Interrupt
       Flag bit of one of the PIR registers is set every time the BUSY bit transitions, regardless of whether
       or not the CRC interrupt is enabled. The CRCIF bit can only be cleared by software. The CRC interrupt
       enable is the CRCIE bit of the corresponding PIE register.

13.7   Configuring the CRC
       The following steps illustrate how to properly configure the CRC:
       1. Determine if the automatic program memory scan will be used with the scanner or manual
          calculation through the SFR interface and perform the actions specified in CRC Data Sources,
          depending on which decision was made.
       2. If desired, seed a starting CRC value into the CRCACC registers.
       3. Program the CRCXOR registers with the desired generator polynomial.
       4. Program the DLEN bits with the length of the data word - 1 (refer to Figure 13-1). This determines
          how many times the shifter will shift into the accumulator for each data word.
       5. Program the PLEN bits with the length of the polynomial - 2 (refer to Figure 13-1).
       6. Determine whether shifting in trailing zeros is desired and set the ACCM bit accordingly.
       7. Likewise, determine whether the MSb or LSb first shifting is desired and write the SHIFTM bit
          accordingly.


--- p225 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                CRC - Cyclic Redundancy Check Module with
                                                                                                          Memory Scanner
       8. Set the GO bit to begin the shifting process.
       9. If manual SFR entry is used, monitor the FULL bit.
          a. When FULL = 0, another word of data can be written to the CRCDATA registers, keeping in
              mind that the Most Significant Byte (CRCDATH) must be written first if the data has more
              than eight bits, as the shifter will begin upon the CRCDATL register being written.
          b. If the scanner is used, the scanner will automatically load words into the CRCDATA registers
             as needed, as long as the GO bit is set.
       10. If using the Flash memory scanner, monitor the PIRx SCANIF bit for the scanner to finish pushing
           information into the CRCDATA registers.
           a. After the scan is completed, monitor the SGO bit to determine that the CRC has been
               completed and the check value can be read from the CRCACC registers.
          b. When both the interrupt flags are set (or both BUSY and SCANGO bits are cleared), the
             completed CRC calculation can be read from the CRCACC registers.
       11. If manual entry is used, monitor the BUSY bit to determine when the CRCACC registers hold the
           valid check value.

13.8   Scanner Module Overview
       The Scanner allows segments of the Program Flash Memory or Data EEPROM, to be read out
       (scanned) to the CRC Peripheral. The scanner module interacts with the CRC module and supplies it
       data one word at a time. Data are fetched from the address range defined by SCANLADR registers
       up to the SCANHADR registers.
       The Scanner begins operation when the SGO bit is set and ends when either SGO is cleared by the
       user or when SCANLADR increments past SCANHADR. The SGO bit is also cleared by clearing the EN
       bit in the CRCCON0 register.

13.9   Configuring the Scanner
       The scanner module may be used in conjunction with the CRC module to perform a CRC calculation
       over a range of program memory or Data EEPROM addresses. In order to set up the scanner to work
       with the CRC, perform the following steps:
       1. Set up the CRC module (See Configuring the CRC) and enable the scanner module by setting the
          EN bit in the SCANCON0 register.
       2. Choose which memory region the scanner module will operate on and set the MREG bit
          appropriately.
       3. If trigger is used for scanner operation, set the TRIGEN bit and select the trigger source using
          SCANTRIG register. Select the trigger source using SCANTRIG register and then set the TRIGEN
          bit.
       4. If Burst mode of operation is desired, set the BURSTMD bit.
       5. Set the SCANLADR and SCANHADR registers with the beginning and ending locations in memory
          that are to be scanned.
       6. Select the priority level for the scanner module (Refer to the “System Arbitration” and the
          “Priority Lock” sections in the “PIC18 CPU” chapter for more details.)
       7. Both EN and GO bits in the CRCCON0 register must be enabled to use the scanner. Setting the
          SGO bit will start the scanner operation.

13.10 Scanner Interrupt
       The scanner will trigger an interrupt when the SCANGO bit transitions from ‘1’ to ‘0’. The SCANIF
       interrupt flag of one of the PIR registers is set when the last memory location is reached and the
       data are entered into the CRCDATA registers. The SCANIF bit must be cleared by software. The SCAN
       interrupt enable is the SCANIE bit of the corresponding PIE register.


--- p226 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                    CRC - Cyclic Redundancy Check Module with
                                                                                                              Memory Scanner
13.11 Scanning Modes
        The interaction of the scanner with the system operation is controlled by the priority selection in
        the System Arbiter (Refer to the “Memory Access Scheme” section for more details.) Additionally,
        BURSTMD and TRIGEN bits also determine the operation of the Scanner.

13.11.1 TRIGEN = 0, BURSTMD = 0
        In this case, the memory access request is granted to the scanner if no other higher priority source
        is requesting access. All sources with lower priority than the scanner will get the memory access
        cycles that are not utilized by the scanner.

13.11.2 TRIGEN = 1, BURSTMD = 0
        In this case, the memory access request is generated when the CRC module is ready to accept. The
        memory access request is granted to the scanner if no other higher priority source is requesting
        access. All sources with lower priority than the scanner will get the memory access cycles that are
        not utilized by the scanner.

13.11.3 TRIGEN = x, BURSTMD = 1
        In this case, the memory access is always requested by the scanner. The memory access request is
        granted to the scanner if no other higher priority source is requesting access. The memory access
        cycles will not be granted to lower priority sources than the scanner until it completes operation i.e.,
        SGO = 0.


                     Important: If TRIGEN = 1 and BURSTMD = 1, the user need to ensure that the
                     trigger source is active for the Scanner operation to complete.


13.11.4 WWDT interaction
        The Windowed Watchdog Timer (WWDT) operates in the background during scanner activity. It is
        possible that long scans, particularly in Burst mode, may exceed the WWDT time-out period and
        result in an undesired device Reset. This must be considered when performing memory scans with
        an application that also utilizes WWDT.

13.11.5 Peripheral Module Disable
        Both the CRC and scanner module can be disabled individually by setting the CRCMD and SCANMD
        bits of one of the PMD registers (see the “PMD - Peripheral Module Disable” chapter for more
        details).

13.12 Register Definitions: CRC and Scanner Control
        Long bit name prefixes for the CRC are shown in the table below. Refer to the "Long Bit Names"
        section in the "Register and Bit Naming Conventions" chapter for more information.

        Table 13-1. CRC Long Bit Name Prefixes
                          Peripheral                                              Bit Name Prefix
                             CRC                                                          CRC


--- p227 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                            CRC - Cyclic Redundancy Check Module with
                                                                                                                      Memory Scanner
13.12.1 CRCCON0

            Name:       CRCCON0
            Address:    0x357

            CRC Control Register 0

      Bit        7              6                 5             4                3                2          1             0
                EN             GO                BUSY         ACCM                                        SHIFTM          FULL
  Access        R/W            R/W                R            R/W                                         R/W             R
   Reset         0              0                 0             0                                            0             0

Bit 7 – EN CRC Enable
            Value      Description
            1          CRC module is released from Reset
            0          CRC is disabled and consumes no operating current

Bit 6 – GO CRC Start
            Value      Description
            1          Start CRC serial shifter
            0          CRC serial shifter turned off

Bit 5 – BUSY CRC Busy
            Value      Description
            1          Shifting in progress or pending
            0          All valid bits in shifter have been shifted into accumulator and EMPTY = 1


Bit 4 – ACCM Accumulator Mode
            Value      Description
            1          Data are augmented with zeros
            0          Data are not augmented with zeros

Bit 1 – SHIFTM Shift Mode
            Value      Description
            1          Shift right (LSb first)
            0          Shift left (MSb first)

Bit 0 – FULL Data Path Full Indicator
            Value      Description
            1          CRCDATH/L registers are full
            0          CRCDATH/L registers have shifted their data into the shifter


--- p228 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                  CRC - Cyclic Redundancy Check Module with
                                                                                                            Memory Scanner
13.12.2 CRCCON1

            Name:      CRCCON1
            Address:   0x358

            CRC Control Register 1

      Bit        7           6           5             4                   3            2                1         0
                               DLEN[3:0]                                                    PLEN[3:0]
  Access        R/W         R/W         R/W          R/W                  R/W      R/W                  R/W       R/W
   Reset         0           0           0            0                    0        0                    0         0

Bits 7:4 – DLEN[3:0] Data Length
          Denotes the length of the data word -1 (See Figure 13-1)

Bits 3:0 – PLEN[3:0] Polynomial Length
          Denotes the length of the polynomial -1 (See Figure 13-1)


--- p229 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                    CRC - Cyclic Redundancy Check Module with
                                                                                                              Memory Scanner
13.12.3 CRCDATA

           Name:       CRCDATA
           Address:    0x34F

           CRC Data Register

     Bit         15          14          13             12           11               10             9              8
                                                          DATA[15:8]
  Access        R/W         R/W          R/W           R/W         R/W               R/W            R/W           R/W
   Reset         x           x            x             x             x               x              x             x

     Bit         7             6          5              4                   3            2          1              0
                                                              DATA[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W            R/W           R/W
   Reset         x           x            x             x                    x        x              x             x

Bits 15:0 – DATA[15:0] CRC Input/Output Data

           Notes: The individual bytes in this multi-byte register can be accessed with the following register
           names:
           • CRCDATH: Accesses the high byte DATA[15:8]
           •   CRCDATL: Accesses the low byte DATA[7:0]


--- p230 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                    CRC - Cyclic Redundancy Check Module with
                                                                                                              Memory Scanner
13.12.4 CRCACC

           Name:       CRCACC
           Address:    0x351

           CRC Accumulator Register

     Bit         15          14          13             12                  11        10             9              8
                                                              ACC[15:8]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W            R/W           R/W
   Reset         0           0            0             0                    0        0              0             0

     Bit         7           6            5              4                   3            2          1              0
                                                               ACC[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W            R/W           R/W
   Reset         0           0            0             0                    0        0              0             0

Bits 15:0 – ACC[15:0] CRC Accumulator Data

           Notes: The individual bytes in this multi-byte register can be accessed with the following register
           names:
           • CRCACCH: Accesses the high byte ACC[15:8]
           •   CRCACCL: Accesses the low byte ACC[7:0]


--- p231 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                     CRC - Cyclic Redundancy Check Module with
                                                                                                               Memory Scanner
13.12.5 CRCSHIFT

            Name:       CRCSHFT
            Address:    0x353

            CRC Shift Register

      Bit         15          14          13             12                  11        10             9              8
                                                               SHFT[15:8]
  Access          R              R         R              R                  R             R          R              R
   Reset          0              0         0              0                  0             0          0              0

      Bit         7              6         5              4                  3             2          1              0
                                                               SHFT[7:0]
  Access          R              R         R              R                  R             R          R              R
   Reset          0              0         0              0                  0             0          0              0

Bits 15:0 – SHFT[15:0] CRC Shifter Register Data

            Notes: The individual bytes in this multi-byte register can be accessed with the following register
            names:
            • CRCSHIFTH: Accesses the high byte SHFT[15:8]
            •   CRCSHIFTL: Accesses the low byte SHFT[7:0]


--- p232 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                    CRC - Cyclic Redundancy Check Module with
                                                                                                              Memory Scanner
13.12.6 CRCXOR

           Name:       CRCXOR
           Address:    0x355

           CRC XOR Register

     Bit         15           14         13             12                  11        10             9              8
                                                                X[15:8]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W            R/W           R/W
   Reset         x           x            x             x                    x        x              x             x

     Bit         7            6           5              4                   3            2          1              0
                                                                X[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W            R/W           R/W
   Reset         x           x            x             x                    x        x              x             1

Bits 15:0 – X[15:0] XOR of Polynomial Term XN Enable


                       Important: Bit 0 is not user accessible and is always set to the value of ‘1’.


           Notes: The individual bytes in this multi-byte register can be accessed with the following register
           names:
           • CRCXORH: Accesses the high byte X[15:8]
           •   CRCXORL: Accesses the low byte X[7:0]


--- p233 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                         CRC - Cyclic Redundancy Check Module with
                                                                                                                   Memory Scanner
13.12.7 SCANCON0

            Name:       SCANCON0
            Address:    0x360

            Scanner Access Control Register 0

      Bit        7             6                5              4                  3        2              1              0
                EN          TRIGEN            SGO                                         MREG         BURSTMD          BUSY
  Access        R/W          R/W             R/W/HC                                       R/W            R/W            R/W
   Reset         0             0                0                                          0              0              0

Bit 7 – EN Scanner Enable(1)
            Value      Description
            1          Scanner is enabled
            0          Scanner is disabled

Bit 6 – TRIGEN Scanner Trigger Enable(2,5)
            Value      Description
            1          Scanner trigger is enabled
            0          Scanner trigger is disabled

Bit 5 – SGO Scanner GO(3,4)
            Value      Description
            1          When the CRC is ready, the Memory region set by the MREG bit will be accessed and data are passed to the
                       CRC peripheral.
            0          Scanner operations will not occur

Bit 2 – MREG Scanner Memory Region Select(2)
            Value      Description
            1          Scanner address points to Data EEPROM
            0          Scanner address points to Program Flash Memory

Bit 1 – BURSTMD Scanner Burst Mode(5)
            Value      Description
            1          Memory access request to the CPU Arbiter is always true
            0          Memory access request to the CPU Arbiter is dependent on the CRC request and Trigger

Bit 0 – BUSY Scanner Busy Indicator
            Value      Description
            1          Scanner cycle is in process
            0          Scanner cycle is compete (or never started)

            Notes:
            1. Setting EN = 0 does not affect any other register content.
            2. Scanner trigger selection can be set using SCANTRIG register.
            3. This bit can be cleared in software. It is cleared in hardware when LADR > HADR (and a data cycle
               is not occurring) or when CRCGO = 0.
            4. CRCEN and CRCGO bits must be set before setting the SGO bit.
            5. Refer to Scanning Modes.


--- p234 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                     CRC - Cyclic Redundancy Check Module with
                                                                                                               Memory Scanner
13.12.8 SCANLADR

            Name:       SCANLADR
            Address:    0x35A

            Scan Low Address Register

      Bit        23           22           21            20                 19        18              17            16
                                                                           SCANLADRU[5:0]
  Access                                  R/W           R/W                R/W       R/W             R/W           R/W
   Reset                                   0             0                   0         0              0             0

      Bit        15           14           13            12        11                  10             9              8
                                                        SCANLADRH[7:0]
  Access        R/W          R/W          R/W           R/W       R/W                 R/W            R/W           R/W
   Reset         0            0            0              0         0                  0              0             0

      Bit        7             6            5             4          3                     2          1              0
                                                         SCANLADRL[7:0]
  Access        R/W          R/W          R/W           R/W        R/W                R/W            R/W           R/W
   Reset         0            0            0              0          0                 0              0             0

Bits 21:16 – SCANLADRU[5:0] Scan Start/Current Address Upper Byte
         Upper bits of the current address to be fetched from, value increments on each fetch of memory.

Bits 15:8 – SCANLADRH[7:0] Scan Start/Current Address High Byte
         High byte of the current address to be fetched from, value increments on each fetch of memory.

Bits 7:0 – SCANLADRL[7:0] Scan Start/Current Address Low Byte
          Low byte of the current address to be fetched from, value increments on each fetch of memory.

            Notes:
            1. Registers SCANLADRU/H/L form a 22-bit value but are not guarded for atomic or asynchronous
               access; registers may only be read or written while SGO = 0.
            2. While SGO = 1, writing to this register is ignored.


--- p235 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                     CRC - Cyclic Redundancy Check Module with
                                                                                                               Memory Scanner
13.12.9 SCANHADR

            Name:       SCANHADR
            Address:    0x35D

            Scan High Address Register

      Bit        23           22           21            20                 19        18              17            16
                                                                           SCANHADRU[5:0]
  Access                                  R/W           R/W                R/W       R/W             R/W           R/W
   Reset                                   1             1                  1         1               1             1

      Bit        15           14           13            12        11                  10             9              8
                                                        SCANHADRH[7:0]
  Access        R/W          R/W          R/W           R/W       R/W                 R/W            R/W           R/W
   Reset         1            1            1              1         1                  1              1             1

      Bit        7             6            5            4          3                      2          1              0
                                                        SCANHADRL[7:0]
  Access        R/W          R/W          R/W           R/W       R/W                 R/W            R/W           R/W
   Reset         1            1            1             1          1                  1              1             1

Bits 21:16 – SCANHADRU[5:0] Scan End Address
         Upper bits of the address at the end of the designated scan

Bits 15:8 – SCANHADRH[7:0] Scan End Address
         High byte of the address at the end of the designated scan

Bits 7:0 – SCANHADRL[7:0] Scan End Address
          Low byte of the address at the end of the designated scan

            Notes:
            1. Registers SCANHADRU/H/L form a 22-bit value but are not guarded for atomic or asynchronous
               access; registers may only be read or written while SGO = 0.
            2. While SGO = 1, writing to this register is ignored.


--- p236 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                             CRC - Cyclic Redundancy Check Module with
                                                                                                                       Memory Scanner
13.12.10 SCANTRIG

            Name:        SCANTRIG
            Address:     0x361

            SCAN Trigger Selection Register

      Bit         7             6             5               4                   3            2               1             0
                                                                                            TSEL[4:0]
  Access                                                     R/W                 R/W          R/W            R/W           R/W
   Reset                                                      0                   0            0              0             0

Bits 4:0 – TSEL[4:0] Scanner Data Trigger Input Selection

            Table 13-2. Scanner Data Trigger Input Sources
                            TSEL Value                                                 Trigger Input Sources
                           11111-10110                                                            —
                              10110                                                          CLC8_OUT
                              10101                                                          CLC7_OUT
                              10100                                                          CLC6_OUT
                              10011                                                          CLC5_OUT
                              10010                                                          CLC4_OUT
                              10001                                                          CLC3_OUT
                              10000                                                          CLC2_OUT
                              01111                                                          CLC1_OUT
                              01110                                                          SMT1_OUT
                           01101-01001                                                            —
                              01000                                                    TMR6_Postscaler_OUT
                              00111                                                          TMR5_OUT
                              00110                                                    TMR4_Postscaler_OUT
                              00101                                                          TMR3_OUT
                              00100                                                    TMR2_Postscaler_OUT
                              00011                                                          TMR1_OUT
                              00010                                                          TMR0_OUT
                              00001                                                         CLKREF_OUT
                              00000                                                           LFINTOSC


--- p237 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                      CRC - Cyclic Redundancy Check Module with
                                                                                                                Memory Scanner
13.13 Register Summary - CRC
Address    Name      Bit Pos.   7         6            5             4                3          2            1             0
                      7:0                                                DATA[7:0]
 0x034F   CRCDATA
                      15:8                                               DATA[15:8]
                      7:0                                                 ACC[7:0]
 0x0351    CRCACC
                      15:8                                           ACC[15:8]
                      7:0                                            SHFT[7:0]
 0x0353   CRCSHFT
                      15:8                                          SHFT[15:8]
                      7:0                                              X[7:0]
 0x0355    CRCXOR
                      15:8                                            X[15:8]
 0x0357   CRCCON0     7:0       EN       GO           BUSY       ACCM                                       SHIFTM        FULL
 0x0358   CRCCON1     7:0                     DLEN[3:0]                                              PLEN[3:0]
 0x0359   Reserved
                       7:0                                           SCANLADRL[7:0]
 0x035A   SCANLADR    15:8                                           SCANLADRH[7:0]
                      23:16                                                     SCANLADRU[5:0]
                       7:0                                           SCANHADRL[7:0]
0x035D    SCANHADR    15:8                                           SCANHADRH[7:0]
                      23:16                                                     SCANHADRU[5:0]
 0x0360   SCANCON0     7:0      EN     TRIGEN         SGO                                MREG             BURSTMD         BUSY
 0x0361   SCANTRIG     7:0                                                              TSEL[4:0]


--- p238 ---
