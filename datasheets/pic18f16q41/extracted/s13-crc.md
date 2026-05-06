13.    CRC - Cyclic Redundancy Check Module with Memory Scanner
       The Cyclic Redundancy Check (CRC) module provides a software-configurable hardware-
       implemented CRC checksum generator. This module includes the following features:
       •   Any standard CRC up to 32 bits can be used
       •   Configurable polynomial
       •   Any seed value up to 32 bits can be used
       •   Standard and reversed bit order available
       •   Augmented zeros can be added automatically or by the user
       •   Memory scanner for core-independent CRC calculations on any program memory locations
       •   Software configurable data registers for communication CRCs

13.1   Module Overview
       The CRC module is coupled with a memory scanner that provides a means of performing CRC
       calculations in hardware, without CPU intervention. The memory scanner can automatically provide
       data from program Flash memory to the CRC module. The CRC module can also be operated by
       directly writing data to SFRs, without using a scanner.
       The CRC module can be used to detect bit errors in the Flash memory using the built-in memory
       scanner or through user input RAM. The CRC module can accept up to a 32-bit polynomial with up
       to a 32-bit seed value. A CRC calculated check value (or checksum) will then be generated into the
       CRCOUT registers for user storage. The CRC module uses an XOR shift register implementation
       to perform the polynomial division required for the CRC calculation. This feature is useful for
       calculating CRC values of data being transmitted or received using communications peripherals such
       as the SPI, UART or I2C.

13.2   Polynomial Implementation
       The CRC polynomial equation is user configurable, allowing any polynomial equation to be used for
       the CRC checksum calculation. The polynomial and accumulator sizes are determined by the PLEN
       bits. For an n-bit accumulator, PLEN = n-1 and the corresponding polynomial is n+1 bits. This allows
       the accumulator to be any size up to 32 bits with a corresponding polynomial up to 33 bits. The
       MSb and LSb of the polynomial are always ‘1’ which is forced by hardware. Therefore, the LSb of the
       CRCXOR Low Byte register is hardwired high and always reads as ‘1’.
       All polynomial bits between the MSb and LSb are specified by the CRCXOR registers.
       For example, when using the standard CRC32, the polynomial is defined as 0x4C11DB7
        x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1 . In this polynomial, the
       X32 and X0 terms are the MSb and LSb controlled by hardware. The X31 and X1 terms are specified
       by setting the CRCXOR[31:0] bits with the corresponding polynomial value, which in this example is
       0x04C11DB6. Reading the CRCXOR registers will return 0x04C11DB7 because the LSb is always ‘1’.
       Refer to the following example for more details.

               Example 13-1. CRC32 Example
               Standard CRC32 Polynomial (33 bits):

                x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1
               Standard 32-bit Polynomial Representation: 0x04C11DB7
               CRCXORT = 0x04 = 0b00000100
               CRCXORU = 0xC1 = 0b11000001
               CRCXORH = 0x1D = 0b00011101


--- p203 ---
              CRCXORL = 0xB7 = 0b1011011- (1)
              Data Sequence: 0x55, 0x66, 0x77, 0x88
              DLEN = 0b00111 // Number of bits written to CRCDATA registers
              (Data Length)
              PLEN = 0b11111 // MSb position of the polynomial (Polynomial
              Length)
              Data passed into the CRC:
              // SHIFTM = 0(Shift Mode: MSb first)
              0x55 0x66 0x77 0x88 = 01010101 01100110 01110111 10001000

              // SHIFTM = 1(Shift Mode: LSb first)
              0x55 0x66 0x77 0x88 = 10101010 01100110 11101110 00010001

              CRC Check Value (ACCM = 1, data is augmented with zeros)
              // When SHIFTM = 0, CRC Result = 0xC60D8323
              CRCOUTT = 0xC6 = 0b11000110
              CRCOUTU = 0x0D = 0b00001101
              CRCOUTH = 0x83 = 0b10000011
              CRCOUTL = 0x23 = 0b00100011
              // When SHIFTM = 1, CRC Result = 0x843529CC
              CRCOUTT = 0x84 = 0b10000100
              CRCOUTU = 0x35 = 0b00110101
              CRCOUTH = 0x29 = 0b00101001
              CRCOUTL = 0xCC = 0b11001100
              Note:
              1. Bit 0 is unimplemented. The LSb of any CRC polynomial is always ‘1’ and will
                 always be treated as a ‘1’ by the CRC for calculating the CRC check value. This bit
                 will be read in software as a ‘0’.


13.3   Data Sources
       Data is supplied to the CRC module using the CRCDATA registers and can either be loaded manually
       or automatically by using the scanner module. The length of the data word being supplied to the
       CRC module is specified by the DLEN bits and can be configured for data words up to 32 bits in
       length. The DLEN field indicates how many bits in the CRCDATA registers are valid and any bits
       outside of the specified data word size will be ignored. Data is moved into the CRCSHIFT registers as
       an intermediate to calculate the check value located in the CRCOUT registers. The SHIFTM bit is used
       to determine the bit order of the data being shifted into the accumulator and the bit order of the
       result.


--- p204 ---
       Figure 13-1. CRC Process

         MSb first (SHIFTM = 0)
         MSb           LSb                                                                                             MSb         LSb
                                                                                                       CRC Feedback       Input Data


           Accumulator
           After n sums


         Industry standard LSb first
         MSb           LSb                                                                                             MSb         LSb
             Input Data                CRC Feedback


                                                                                                                         Accumulator
                                                                                                                         After n sums


         LSb first (SHIFTM = 1)
         LSb          MSb
                                                                                                      CRC Feedback


            Accumulator                                                                               MSb        LSb
           After n sums
                                                                                                        Input Data
           (bit reversed)


       When the SHIFTM bit is not set, data will be shifted into the CRC, MSb first and the result will be
       big-endian. When the SHIFTM bit is set, data will be shifted into the accumulator in the reverse order
       (LSb first) and the result will be little-endian. The CRC module can be seeded with an initial value by
       setting the CRCOUT registers to the appropriate value before beginning the CRC process.

13.3.1 CRC from User Data
       Data can be supplied to the CRC module by writing to the CRCDATA registers. Once data has been
       loaded into the CRCDATA registers, it will then be latched onto the CRC Shift (CRCSHIFT) registers.
       If data is still being shifted from an earlier write to the CRCDATA registers and the user attempts
       to write more data, the most recently written data will be held in the CRCDATA registers until the
       previous shift has completed.

13.3.2 CRC from Flash
       Data can also be supplied to the CRC module using the memory scanner, as opposed to writing
       the data manually using the CRCDATA registers, allowing users to automate CRC calculations. An
       automated scan of Program Flash Memory or Data EEPROM can be performed by configuring the
       scanner accordingly, to copy data into the CRCDATA registers. The user can initialize the program
       memory scanner as defined in Scanner Module Overview and Configuring the Scanner.

13.4   CRC Check Value
       The CRC check value can be accessed using the CRCOUT registers after a CRC calculation has
       completed. The check value is dependent on the configuration of the ACCM and SHIFTM mode
       settings. When the ACCM bit is set, the CRC module will augment the data with a number of zeros
       equal to the length of the polynomial to align the final check value. When the ACCM bit is not set, the
       CRC will stop at the end of the data and no additional zeroes will be augmented to the final value.
       The user can manually augment a number of additional zeroes equal to the length of the polynomial
       by entering them into the CRCDATA register, which will yield the same check value as Augmented
       mode. Alternatively, the expected check value can be entered at this point to make the final result
       equal zero.


--- p205 ---
       When the CRC check value is computed with the SHIFTM (LSb first) and ACCM bits set, the final value
       in the CRCOUT registers will be reversed such that the LSb will be in the MSb position and vice versa
       (Figure 13-1).
       When creating a check value to be appended to a data stream, then a reversal must be performed
       on the final value to achieve the correct checksum. The CRC can be used to do this reversal by
       following the steps below.
       1. Save CRCOUT value in user RAM space.
       2. Clear the CRCOUT registers.
       3. Clear the CRCXOR registers.
       4. Write the saved CRCOUT value to the CRCDATA input.
       If the steps listed above were followed completely, the properly orientated check value will be in the
       CRCOUT registers.

13.5   CRC Interrupt
       The CRC module will generate an interrupt when the BUSY bit transitions from ‘1’ to ‘0’. The CRC
       Interrupt Flag (CRCIF) bit of the corresponding PIR register will be set every time the BUSY bit
       transitions, whether or not the CRC Interrupt Enable (CRCIE) has been set. The CRCIF bit must be
       cleared by software by the user. If the user has the CRCIE bit set, then the CPU will jump to the
       Interrupt Service Routine (ISR) every time that the CRCIF bit is set.

13.6   Configuring the CRC Module
       The following steps illustrate how to properly configure the CRC:
       1. Determine if the automatic program memory scan will be used with the scanner or if manual
          calculation will take place through the SFR interface and perform the actions specified in the CRC
          Data Sources section.
          a. To configure the scanner module to be used with CRC, refer to the Configuring the Scanner
               section for more information.
       2. When applicable, seed a starting CRC value into the CRCOUT registers.
       3. Program the CRCXOR registers with the desired generator polynomial.
       4. Program the DLEN bits with the length of the data word (refer to Figure 13-1). This value
          determines how many times the shifter will shift into the accumulator for each data word.
       5. Program the PLEN bits with the length of the polynomial (refer to Figure 13-1).
       6. Determine whether shifting in trailing zeroes is desired, and set the ACCM bit accordingly.
       7. Determine whether the MSb or LSb first shifting is desired, and write the SHIFTM bit accordingly.
       8. Set the GO bit to begin the shifting process.
       9. If manual SFR entry is used, monitor the FULL bit.
          a. When FULL = 0, another word of data can be written to the CRCDATA registers. It is important
              to note that the Most Significant Byte (CRCDATAH) must be written first if the data has more
              than eight bits, as the shifter will begin upon the CRCDATAL register being written.
          b. If the scanner is used, it will automatically load words into the CRCDATA registers as needed,
             as long as the GO bit is set.
       10. If using the Flash memory scanner, monitor the SCANIF bit of the corresponding PIR register to
           determine when the scanner has finished pushing data into the CRCDATA registers.
           a. After the scan is completed, monitor the SGO bit to determine that the CRC has been
               completed and the check value can be read from the CRCOUT registers.
          b. When both the interrupt flags are set (or both BUSY and SGO bits are cleared), the completed
             CRC calculation can be read from the CRCOUT registers.


--- p206 ---
       11. If manual entry is used, monitor the BUSY bit to determine when the CRCOUT registers hold the
           valid check value.

13.6.1 Register Overlay
       The CRCOUT, CRCSHIFT and CRCXOR registers are grouped together and share SFR space. Since
       these register groups are located within the same addresses, the SETUP bits must be configured
       accordingly to access any of these registers. Refer to the CRCCON2 register for more information
       about how the SETUP bits can be configured to access each of the available CRC registers.

13.7   Scanner Module Overview
       The scanner allows segments of the Program Flash Memory or Data EEPROM to be read out
       (scanned) to the CRC peripheral. The scanner module interacts with the CRC module and supplies
       it with data, one word at a time. Data is fetched from the address range defined by SCANLADR
       registers up to the SCANHADR registers. The scanner begins operation when the SGO bit is set and
       ends when either SGO is cleared by the user or when SCANLADR increments past SCANHADR. The
       SGO bit is also cleared when the EN bit in the CRCCON0 register is cleared.

13.8   Scanning Modes
       The interaction of the scanner with the system operation is controlled by the priority selection in
       the system arbiter (refer to the “Memory Access Scheme” section for more details). When using
       the scanner module in conjunction with the CRC module, the system arbiter needs to be configured
       such that the scanner has a higher priority than the CPU to ensure that a memory access request is
       granted when it occurs. Additionally, BURSTMD and TRIGEN bits also determine the operation of the
       scanner.

13.8.1 TRIGEN = 0, BURSTMD = 0
       In this case, the memory access request is granted to the scanner if no other higher priority source
       is requesting access. All sources with lower priority than the scanner will get the memory access
       cycles that are not utilized by the scanner.

13.8.2 TRIGEN = 1, BURSTMD = 0
       In this case, the memory access request is generated when the CRC module is ready to accept. The
       memory access request is granted to the scanner if no other higher priority source is requesting
       access. All sources with lower priority than the scanner will get the memory access cycles that are
       not utilized by the scanner.

13.8.3 TRIGEN = x, BURSTMD = 1
       In this case, the memory access is always requested by the scanner. The memory access request is
       granted to the scanner if no other higher priority source is requesting access. The memory access
       cycles will not be granted to lower priority sources than the scanner until it completes operation, i.e.
       SGO = 0.


                   Important: If TRIGEN = 1 and BURSTMD = 1, the user needs to ensure that the trigger
                   source is active for the scanner operation to complete.


13.8.4 WWDT Interaction
       The Windowed Watch Dog Timer (WWDT) operates in the background during scanner activity. It is
       possible that long scans, particularly in Burst mode, may exceed the WWDT time-out period and
       result in an undesired device Reset. This must be considered when performing memory scans with
       an application that also utilizes WWDT.


--- p207 ---
13.9   Configuring the Scanner
       The scanner module may be used in conjunction with the CRC module to perform a CRC calculation
       over a range of program memory or Data EEPROM addresses. To set up the scanner to work with
       the CRC, perform the following steps:
       1. Set up the CRC module (see the Configuring the CRC Module section) and enable the scanner
           module by setting the EN bit in the SCANCON0 register.
       2. Choose which memory region the scanner module needs to operate on and set the MREG bit
          appropriately.
       3. If trigger is used for scanner operation, set the TRIGEN bit and select the trigger source using
          the SCANTRIG register. Select the trigger source using the SCANTRIG register and then set the
          TRIGEN bit.
       4. If Burst mode of operation is desired, set the BURSTMD bit.
       5. Set the SCANLADR and SCANHADR registers with the beginning and ending locations in memory
          that are to be scanned.
       6. Select the priority level for the scanner module (refer to the “System Arbitration” and the
          “Priority Lock” sections for more details).
          Note: The default priority levels of the system arbiter may need to be changed to ensure the
          scanner operates as intended and that a memory access request is granted when it occurs.
       7. Both EN and GO bits in the CRCCON0 register must be enabled to use the scanner. Setting the
          SGO bit will start the scanner operation.

13.10 Scanner Interrupt
       The scanner will trigger an interrupt when the SGO bit transitions from ‘1’ to ‘0’. The SCANIF
       interrupt flag of one of the PIR registers is set when the last memory location is reached and the
       data is entered into the CRCDATA registers. The SCANIF bit must be cleared by software. The SCAN
       interrupt enable is the SCANIE bit of the corresponding PIE register.

13.11 Peripheral Module Disable
       Both the CRC and scanner module can be disabled individually by setting the CRCMD and SCANMD
       bits of one of the PMD registers (see the “Peripheral Module Disable” chapter for more details).
       The SCANMD bit can be used to enable or disable the scanner module only if the SCANE
       Configuration bit is set. If the SCANE bit is cleared, then the scanner module is not available for
       use and the SCANMD bit is ignored.

13.12 Register Definitions: CRC and Scanner Control
       Long bit name prefixes for the CRC are shown in the table below. Refer to the “Long Bit Names”
       section in the “Register and Bit Naming Conventions” chapter for more information.

       Table 13-1. CRC Long Bit Name Prefixes
                         Peripheral                                              Bit Name Prefix
                            CRC                                                          CRC


--- p208 ---
13.12.1 CRCCON0

            Name:       CRCCON0
            Address:    0x356

            CRC Control Register 0

      Bit        7              6                 5             4                 3               2         1            0
                EN             GO                BUSY         ACCM                  SETUP[1:0]           SHIFTM         FULL
  Access        R/W            R/W                R            R/W               R/W                      R/W            R
   Reset         0              0                 0             0                 0                         0            0

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
            1          Data is augmented with zeros
            0          Data is not augmented with zeros

Bits 4:3 – SETUP[1:0]
          Register Overlay Setup
            Value      Description
            11         CRC Register Overlay Selection; Read / Write access to CRCOUT
            10         CRC Register Overlay Selection; Read / Write access to CRCXOR
            01         CRC Register Overlay Selection; Read / Write access to CRCSHIFT
            00         CRC Register Overlay Selection; Read / Write access to CRCOUT

Bit 1 – SHIFTM Shift Mode
            Value      Description
            1          Shift right (LSb first)
            0          Shift left (MSb first)

Bit 0 – FULL Data Path Full Indicator
            Value      Description
            1          CRCDATAT/U/H/L registers are full
            0          CRCDATAT/U/H/L registers have shifted their data into the shifter


--- p209 ---
13.12.2 CRCCON1

            Name:      CRCCON1
            Address:   0x357

            CRC Control Register 1

      Bit        7           6          5              4                   3        2               1             0
                                                                                 PLEN[4:0]
  Access                                             R/W                  R/W      R/W            R/W            R/W
   Reset                                              0                    0        0              0              0

Bits 4:0 – PLEN[4:0] Polynomial Length
          Denotes the length of the polynomial (n-1)


--- p210 ---
13.12.3 CRCCON2

            Name:      CRCCON2
            Address:   0x358

            CRC Control Register 2

      Bit        7           6          5              4                   3        2               1             0
                                                                                 DLEN[4:0]
  Access                                              R/W                 R/W      R/W            R/W            R/W
   Reset                                               0                   0        0              0              0

Bits 4:0 – DLEN[4:0] Data Length
          Denotes the length of the data word (n-1)


--- p211 ---
13.12.4 CRCDATA

           Name:      CRCDATA
           Address:   0x34E

           CRC Data Registers

     Bit       31          30       29             28          27                26           25            24
                                                    CRCDATAT[7:0]
  Access       R/W         R/W      R/W           R/W         R/W               R/W          R/W            R/W
   Reset        0           0        0              0           0                0            0              0

     Bit       23          22       21             20          19                18           17            16
                                                    CRCDATAU[7:0]
  Access       R/W         R/W      R/W           R/W         R/W               R/W          R/W            R/W
   Reset        0           0        0              0           0                0            0              0

     Bit       15          14       13             12         11                 10            9             8
                                                   CRCDATAH[7:0]
  Access       R/W         R/W      R/W           R/W        R/W                R/W          R/W            R/W
   Reset        0           0        0              0          0                 0            0              0

     Bit        7           6        5             4           3                     2         1             0
                                                   CRCDATAL[7:0]
  Access       R/W         R/W      R/W           R/W        R/W                R/W          R/W            R/W
   Reset        0           0        0             0           0                 0            0              0

Bits 31:24 – CRCDATAT[7:0] CRC Data Top Byte

Bits 23:16 – CRCDATAU[7:0] CRC Data Upper Byte

Bits 15:8 – CRCDATAH[7:0] CRC Data High Byte

Bits 7:0 – CRCDATAL[7:0] CRC Data Low Byte


--- p212 ---
13.12.5 CRCOUT

            Name:      CRCOUT
            Address:   0x352

            CRC Output Registers

      Bit       31          30           29            28          27                26           25            24
                                                        CRCOUTT[7:0]
  Access        R/W        R/W          R/W           R/W         R/W               R/W          R/W            R/W
   Reset         0          0            0             0           0                 0            0              0

      Bit       23          22           21            20         19                 18           17            16
                                                        CRCOUTU[7:0]
  Access        R/W        R/W          R/W           R/W        R/W                R/W          R/W            R/W
   Reset         0          0            0             0           0                 0            0              0

      Bit       15          14           13            12         11                 10            9             8
                                                        CRCOUTH[7:0]
  Access        R/W        R/W          R/W           R/W        R/W                R/W          R/W            R/W
   Reset         0          0            0              0          0                 0            0              0

      Bit        7           6           5             4           3                     2         1             0
                                                        CRCOUTL[7:0]
  Access        R/W        R/W          R/W           R/W         R/W               R/W          R/W            R/W
   Reset         0          0            0             0           0                 0            0              0

Bits 31:24 – CRCOUTT[7:0] CRC Output Register Top Byte
         Writing to this register writes the Most Significant Byte of the CRC output register. Reading from this
         register reads the Most Significant Byte of the CRC output.

Bits 23:16 – CRCOUTU[7:0] CRC Output Register Upper Byte

Bits 15:8 – CRCOUTH[7:0] CRC Output Register High Byte

Bits 7:0 – CRCOUTL[7:0] CRC Output Register Low Byte
          Writing to this register writes the Least Significant Byte of the CRC output register. Reading from this
          register reads the Least Significant Byte of the CRC output.


--- p213 ---
13.12.6 CRCSHIFT

            Name:       CRCSHIFT
            Address:    0x352

            CRC Shift Registers

      Bit        31          30          29            28          27                26           25            24
                                                       CRCSHIFTT[7:0]
  Access         R            R          R             R           R                     R         R             R
   Reset         0            0          0              0           0                    0         0             0

      Bit        23          22          21            20          19                18           17            16
                                                       CRCSHIFTU[7:0]
  Access         R            R          R             R           R                     R         R             R
   Reset         0            0          0              0           0                    0         0             0

      Bit        15          14          13            12          11                10            9             8
                                                       CRCSHIFTH[7:0]
  Access         R            R          R             R           R                     R         R             R
   Reset         0            0          0              0           0                    0         0             0

      Bit        7            6          5              4            3                   2         1             0
                                                        CRCSHIFTL[7:0]
  Access         R            R          R              R            R                   R         R             R
   Reset         0            0          0              0            0                   0         0             0

Bits 31:24 – CRCSHIFTT[7:0] CRC Shift Register Top Byte
         Reading from this register reads the Most Significant Byte of the CRC Shifter.

Bits 23:16 – CRCSHIFTU[7:0] CRC Shift Register Upper Byte

Bits 15:8 – CRCSHIFTH[7:0] CRC Shift Register High Byte

Bits 7:0 – CRCSHIFTL[7:0] CRC Shift Register Low Byte
          Reading from this register reads the Least Significant Byte of the CRC Shifter.


--- p214 ---
13.12.7 CRCXOR

           Name:      CRCXOR
           Address:   0x352

           CRC XOR Registers

     Bit       31          30       29             28          27                26           25            24
                                                    CRCXORT[7:0]
  Access       R/W        R/W       R/W           R/W         R/W               R/W          R/W            R/W
   Reset        0          0         0             0           0                 0            0              0

     Bit       23          22       21             20          19                18           17            16
                                                    CRCXORU[7:0]
  Access       R/W        R/W       R/W           R/W         R/W               R/W          R/W            R/W
   Reset        0          0         0              0           0                0            0              0

     Bit       15          14       13             12          11                10            9             8
                                                    CRCXORH[7:0]
  Access       R/W        R/W       R/W           R/W         R/W               R/W          R/W            R/W
   Reset        0          0         0              0           0                0            0              0

     Bit        7          6         5             4           3                     2         1             0
                                                    CRCXORL[7:0]
  Access       R/W        R/W       R/W           R/W         R/W               R/W          R/W            R/W
   Reset        0          0         0             0           0                 0            0              0

Bits 31:24 – CRCXORT[7:0] XOR of Polynomial Term XN Enable Top Byte

Bits 23:16 – CRCXORU[7:0] XOR of Polynomial Term XN Enable Upper Byte

Bits 15:8 – CRCXORH[7:0] XOR of Polynomial Term XN Enable High Byte

Bits 7:0 – CRCXORL[7:0] XOR of Polynomial Term XN Enable Low Byte


--- p215 ---
13.12.8 SCANCON0

            Name:       SCANCON0
            Address:    0x360

            Scanner Access Control Register 0

      Bit        7             6                5              4                  3         2             1               0
                EN          TRIGEN            SGO                                          MREG        BURSTMD           BUSY
  Access        R/W          R/W             R/W/HC                                        R/W           R/W             R/W
   Reset         0             0                0                                           1             0               0

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
            1          When the CRC is ready, the Memory region set by the MREG bit will be accessed and data is passed to the CRC
                       peripheral
            0          Scanner operations will not occur

Bit 2 – MREG Scanner Memory Region Select(2)
            Value      Description
            1          Scanner address points to Data EEPROM
            0          Scanner address points to Program Flash Memory

Bit 1 – BURSTMD Scanner Burst Mode(5)
            Value      Description
            1          Memory access request to the CPU Arbiter is always true
            0          Memory access request to the CPU Arbiter is dependent on the CRC request and trigger

Bit 0 – BUSY Scanner Busy Indicator
            Value      Description
            1          Scanner cycle is in process
            0          Scanner cycle is compete (or never started)


--- p216 ---
Notes:
1. Setting EN = 0 does not affect any other register content.
2. Scanner trigger selection can be set using the SCANTRIG register.
3. This bit can be cleared in software. It is cleared in hardware when LADR > HADR (and a data cycle
   is not occurring) or when CRCGO = 0.
4. The CRCEN and CRCGO bits must be set before setting the SGO bit.
5. See Table 13-2.

Table 13-2. Scanner Operating Modes
    TRIGEN          BURSTMD                                          Scanner Operation
                                   Memory access is requested when the CRC module is ready to accept data; the request
       0                0
                                             is granted if no other higher priority source request is pending.
                                   Memory access is requested when the CRC module is ready to accept data and trigger
       1                0           selection is true; the request is granted if no other higher priority source request is
                                                                           pending.
                                    Memory access is always requested; the request is granted if no other higher priority
       x                1
                                                               source request is pending.
Note: Refer to the “System Arbitration” and the “Memory Access Scheme” sections for more details about Priority
selection and Memory Access Scheme.


--- p217 ---
13.12.9 SCANLADR

            Name:       SCANLADR
            Address:    0x35A

            Scan Low Address Registers

      Bit        23           22           21            20                 19        18             17            16
                                                                           SCANLADRU[5:0]
  Access                                  R/W           R/W                R/W       R/W            R/W            R/W
   Reset                                   0             0                   0         0             0              0

      Bit        15           14           13            12        11                  10             9             8
                                                        SCANLADRH[7:0]
  Access        R/W          R/W          R/W           R/W       R/W                 R/W           R/W            R/W
   Reset         0            0            0              0         0                  0             0              0

      Bit        7             6            5             4          3                     2          1             0
                                                         SCANLADRL[7:0]
  Access        R/W          R/W          R/W           R/W        R/W                R/W           R/W            R/W
   Reset         0            0            0              0          0                 0             0              0

Bits 21:16 – SCANLADRU[5:0] Scan Start/Current Address upper byte
         Upper bits of the current address to be fetched from, value increments on each fetch of memory.

Bits 15:8 – SCANLADRH[7:0] Scan Start/Current Address high byte
         High byte of the current address to be fetched from, value increments on each fetch of memory.

Bits 7:0 – SCANLADRL[7:0] Scan Start/Current Address low byte
          Low byte of the current address to be fetched from, value increments on each fetch of memory.

            Notes:
            1. Registers SCANLADRU/H/L form a 22-bit value, but are not guarded for atomic or asynchronous
               access; registers may only be read or written while SGO = 0.
            2. While SGO = 1, writing to this register is ignored.


--- p218 ---
13.12.10 SCANHADR

            Name:       SCANHADR
            Address:    0x35D

            Scan High Address Registers

      Bit        23           22           21            20                 19        18             17            16
                                                                           SCANHADRU[5:0]
  Access                                  R/W           R/W                R/W       R/W            R/W            R/W
   Reset                                   1             1                   1         1             1              1

      Bit        15           14           13            12        11                  10             9             8
                                                        SCANHADRH[7:0]
  Access        R/W          R/W          R/W           R/W       R/W                 R/W           R/W            R/W
   Reset         1            1            1              1         1                  1             1              1

      Bit        7             6            5            4          3                      2          1             0
                                                        SCANHADRL[7:0]
  Access        R/W          R/W          R/W           R/W       R/W                 R/W           R/W            R/W
   Reset         1            1            1             1          1                  1             1              1

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


--- p219 ---
13.12.11 SCANTRIG

            Name:        SCANTRIG
            Address:     0x361

            SCAN Trigger Selection Register

      Bit         7             6             5              4                   3             2                1         0
                                                                                                   TSEL[3:0]
  Access                                                                        R/W          R/W               R/W      R/W
   Reset                                                                         0            0                 0        0

Bits 3:0 – TSEL[3:0] Scanner Data Trigger Input Selection

            Table 13-3. Scanner Data Trigger Input Sources
                            TSEL Value                                                Trigger Input Sources
                           1111 - 1100                                                          —
                              1011                                                          CLC4_OUT
                               1010                                                         CLC3_OUT
                               1001                                                         CLC2_OUT
                               1000                                                         CLC1_OUT
                               0111                                                        SMT1_OUT
                               0110                                                   TMR4_Postscaler_OUT
                               0101                                                        TMR3_OUT
                               0100                                                   TMR2_Postscaler_OUT
                               0011                                                        TMR1_OUT
                               0010                                                        TMR0_OUT
                               0001                                                       CLCKREF_OUT
                               0000                                                        LFINTOSC(1)

            Note:
            1. The number of implemented bits varies by device.


--- p220 ---
13.13 Register Summary - CRC
Address    Name      Bit Pos.   7         6           5             4           3          2          1            0
 0x00
  ...     Reserved
0x034D
                       7:0                                        CRCDATAL[7:0]
                       15:8                                       CRCDATAH[7:0]
 0x034E   CRCDATA
                      23:16                                       CRCDATAU[7:0]
                      31:24                                       CRCDATAT[7:0]
                       7:0                                         CRCOUTL[7:0]
                       15:8                                       CRCOUTH[7:0]
 0x0352    CRCOUT
                      23:16                                       CRCOUTU[7:0]
                      31:24                                        CRCOUTT[7:0]
                       7:0                                        CRCSHIFTL[7:0]
                       15:8                                       CRCSHIFTH[7:0]
 0x0352   CRCSHIFT
                      23:16                                       CRCSHIFTU[7:0]
                      31:24                                       CRCSHIFTT[7:0]
                       7:0                                         CRCXORL[7:0]
                       15:8                                        CRCXORH[7:0]
 0x0352    CRCXOR
                      23:16                                        CRCXORU[7:0]
                      31:24                                        CRCXORT[7:0]
 0x0356   CRCCON0      7:0      EN       GO         BUSY        ACCM             SETUP[1:0]        SHIFTM        FULL
 0x0357   CRCCON1      7:0                                                             PLEN[4:0]
 0x0358   CRCCON2      7:0                                                             DLEN[4:0]
 0x0359   Reserved
                       7:0                                          SCANLADRL[7:0]
 0x035A   SCANLADR    15:8                                          SCANLADRH[7:0]
                      23:16                                                    SCANLADRU[5:0]
                       7:0                                          SCANHADRL[7:0]
0x035D    SCANHADR    15:8                                          SCANHADRH[7:0]
                      23:16                                                    SCANHADRU[5:0]
 0x0360   SCANCON0     7:0      EN     TRIGEN        SGO                                MREG        BURSTMD      BUSY
 0x0361   SCANTRIG     7:0                                                                    TSEL[3:0]


--- p221 ---
