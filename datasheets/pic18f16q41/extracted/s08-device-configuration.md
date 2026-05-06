8.    Device Configuration
8.1   Configuration Settings
      The Configuration settings allow the user to set up the device with several choices of oscillators,
      Resets and memory protection options. These are implemented at 0x300000 - 0x300009.


                  Important: The DEBUG Configuration bit is managed automatically by device
                  development tools including debuggers and programmers. For normal device operation,
                  this bit needs to be maintained as a ‘1’.


8.2   Code Protection
      Code protection allows the device to be protected from unauthorized access. Internal access to the
      program memory is unaffected by any code protection setting. A single code-protect bit controls the
      access for both program memory and data EEPROM memory.
      The entire program memory and Data EEPROM space is protected from external reads and writes
      by the CP bit. When CP = 0, external reads and writes are inhibited and a read will return all ‘0’s.
      The CPU can continue to read the memory, regardless of the protection bit settings. Self-writing the
      program memory is dependent upon the write protection setting.

8.3   User ID
      32 words in the memory space (0x200000 - 0x20003F) are designated as ID locations where the
      user can store checksum or other code identification numbers. These locations are readable and
      writable during normal execution. See the “User ID, Device ID and Configuration Settings Access,
      DIA and DCI” section in the "NVM - Nonvolatile Memory Module" chapter for more information
      on accessing these memory locations. For more information on checksum calculation, see the
      “PIC18-Q41 Family Programming Specification” (DS40002143).

8.4   Device ID and Revision ID
      The 16-bit device ID word is located at 0x3FFFFE and the 16-bit revision ID is located at 0x3FFFFC.
      These locations are read-only and cannot be erased or modified.
      Development tools, such as device programmers and debuggers, may be used to read the Device ID,
      Revision ID and Configuration bits. Refer to the “NVM - Nonvolatile Memory Module” chapter for
      more information on accessing these locations.

8.5   Register Definitions: Configuration Settings


--- p43 ---
8.5.1         CONFIG1

              Name:        CONFIG1
              Address:     0x300000

              Configuration Byte 1

        Bit           7            6            5                 4                  3            2        1             0
                                            RSTOSC[2:0]                                               FEXTOSC[2:0]
  Access                         R/W           R/W              R/W                          R/W          R/W          R/W
   Reset                          1             1                1                            1            1            1

Bits 6:4 – RSTOSC[2:0] Power-Up Default Value for COSC
          This value is the Reset default value for COSC and selects the oscillator first used by user software.
          Refer to COSC operation.
              Value       Description
              111         EXTOSC operating per FEXTOSC bits
              110         HFINTOSC with HFFRQ = 4 MHz and CDIV = 4:1. Resets COSC/NOSC to b'110'.
              101         LFINTOSC
              100         SOSC
              011         Reserved
              010         EXTOSC with 4x PLL, with EXTOSC operating per FEXTOSC bits
              001         Reserved
              000         HFINTOSC with HFFRQ = 64 MHz and CDIV = 1:1. Resets COSC/NOSC to b'110'.


Bits 2:0 – FEXTOSC[2:0] External Oscillator Mode Selection
              Value       Description
              111         ECH (external clock) above 8 MHz
              110         ECM (external clock) for 500 kHz to 8 MHz
              101         ECL (external clock) below 500 kHz
              100         Oscillator not enabled
              011         Reserved (do not use)
              010         HS (crystal oscillator) above 4 MHz
              001         XT (crystal oscillator) above 500 kHz, below 4 MHz
              000         LP (crystal oscillator) optimized for 32.768 kHz


--- p44 ---
8.5.2         CONFIG2

              Name:       CONFIG2
              Address:    0x300001

              Configuration Byte 2

        Bit        7             6              5                4               3               2              1              0
                FCMENS        FCMENP          FCMEN                            CSWEN                         PR1WAY        CLKOUTEN
  Access          R/W           R/W            R/W                              R/W                            R/W            R/W
   Reset           1             1              1                                1                              1              1

Bit 7 – FCMENS Fail-Safe Clock Monitor Enable - Secondary XTAL Enable
              Value      Description
              1          Fail-Safe Clock Monitor enabled; the timer will flag the FSCMS bit and OSFIF interrupt on SOSC failure
              0          Fail-Safe Clock Monitor disabled

Bit 6 – FCMENP Fail-Safe Clock Monitor Enable - Primary XTAL Enable
              Value      Description
              1          Fail-Safe Clock Monitor enabled; the timer will flag the FSCMP bit and OSFIF interrupt on EXTOSC failure
              0          Fail-Safe Clock Monitor disabled

Bit 5 – FCMEN Fail-Safe Clock Monitor Enable
              Value      Description
              1          Fail-Safe Clock Monitor enabled
              0          Fail-Safe Clock Monitor disabled

Bit 3 – CSWEN Clock Switch Enable
              Value      Description
              1          Writing to NOSC and NDIV is allowed
              0          The NOSC and NDIV bits cannot be changed by user software

Bit 1 – PR1WAY PRLOCKED One-Way Set Enable
              Value      Description
              1          The PRLOCKED bit can be cleared and set only once; Priority registers remain locked after one clear/set cycle
              0          The PRLOCKED bit can be set and cleared repeatedly (subject to the unlock sequence)

Bit 0 – CLKOUTEN Clock Out Enable
          If FEXTOSC = HS, XT, LP, then this bit is ignored.
          Otherwise:
              Value      Description
              1          CLKOUT function is disabled; I/O function on OSC2
              0          CLKOUT function is enabled; FOSC/4 clock appears at OSC2


--- p45 ---
8.5.3         CONFIG3

              Name:        CONFIG3
              Address:     0x300002

              Configuration Byte 3

        Bit           7         6                5                4             3                  2          1                 0
                     BOREN[1:0]               LPBOREN         IVT1WAY         MVECEN               PWRTS[1:0]                 MCLRE
  Access          R/W         R/W               R/W             R/W            R/W              R/W         R/W                R/W
   Reset           0            1                1                1             1                1            1                 1

Bits 7:6 – BOREN[1:0] Brown-out Reset Enable
          When enabled, Brown-out Reset Voltage (VBOR) is set by the BORV bit.
              Value       Description
              11          Brown-out Reset enabled, the SBOREN bit is ignored
              10          Brown-out Reset enabled while running, disabled in Sleep; SBOREN is ignored
              01          Brown-out Reset enabled according to SBOREN
              00          Brown-out Reset disabled

Bit 5 – LPBOREN Low-Power BOR Enable
              Value       Description
              1           Low-Power Brown-out Reset is disabled
              0           Low-Power Brown-out Reset is enabled

Bit 4 – IVT1WAY IVTLOCK One-Way Set Enable
              Value       Description
              1           The IVTLOCK bit can be cleared and set only once; IVT registers remain locked after one clear/set cycle
              0           The IVTLOCK bit can be set and cleared repeatedly (subject to the unlock sequence)

Bit 3 – MVECEN Multivector Enable
              Value       Description
              1           Multivector is enabled; vector table used for interrupts
              0           Legacy interrupt behavior

Bits 2:1 – PWRTS[1:0] Power-up Timer Selection
              Value       Description
              11          PWRT is disabled
              10          PWRT is set at 64 ms
              01          PWRT is set at 16 ms
              00          PWRT is set at 1 ms

Bit 0 – MCLRE Master Clear (MCLR) Enable
              Value       Condition              Description
              x           If LVP = 1             RA3 pin function is MCLR
              1           If LVP = 0             RA3 pin function is MCLR
              0           If LVP = 0             RA3 pin function is a port-defined function


--- p46 ---
8.5.4         CONFIG4

              Name:        CONFIG4
              Address:     0x300003

              Configuration Byte 4

        Bit         7             6              5               4                3            2               1           0
                  XINST                         LVP           STVREN           PPS1WAY        ZCD                BORV[1:0]
  Access           R/W                          R/W             R/W              R/W          R/W             R/W         R/W
   Reset            1                            1               1                1            1               1           1

Bit 7 – XINST Extended Instruction Set Enable
              Value       Description
              1           Extended Instruction Set and Indexed Addressing mode disabled (Legacy mode)
              0           Extended Instruction Set and Indexed Addressing mode enabled

Bit 5 – LVP Low-Voltage Programming Enable
          The LVP bit cannot be written (to zero) while operating from the LVP programming interface. The
          purpose of this rule is to prevent the user from dropping out of LVP mode while programming from
          LVP mode, or accidentally eliminating LVP mode from the Configuration state.
              Value       Description
              1           Low-Voltage Programming enabled. MCLR/VPP pin function is MCLR. The MCLRE Configuration bit is ignored.
              0           HV on MCLR/VPP must be used for programming

Bit 4 – STVREN Stack Overflow/Underflow Reset Enable
              Value       Description
              1           Stack Overflow or Underflow will cause a Reset
              0           Stack Overflow or Underflow will not cause a Reset

Bit 3 – PPS1WAY PPSLOCKED One-Way Set Enable
              Value       Description
              1           The PPSLOCKED bit can only be set once after an unlocking sequence is executed; once PPSLOCK is set, all
                          future changes to PPS registers are prevented
              0           The PPSLOCKED bit can be set and cleared as needed (unlocking sequence is required)

Bit 2 – ZCD ZCD Disable
              Value       Description
              1           ZCD disabled, ZCD can be enabled by setting the ZCDSEN bit of ZCDCON
              0           ZCD always enabled, PMDx[ZCDMD] bit is ignored

Bits 1:0 – BORV[1:0] Brown-out Reset Voltage Selection
              Value       Description
              11          Brown-out Reset Voltage (VBOR) set to 1.90V
              10          Brown-out Reset Voltage (VBOR) set to 2.45V
              01          Brown-out Reset Voltage (VBOR) set to 2.7V
              00          Brown-out Reset Voltage (VBOR) set to 2.85V


--- p47 ---
8.5.5         CONFIG5

              Name:           CONFIG5
              Address:        0x300004

              Configuration Byte 5

        Bit           7            6           5                 4                   3              2            1              0
                                     WDTE[1:0]                                                  WDTCPS[4:0]
  Access                          R/W         R/W             R/W                   R/W            R/W         R/W            R/W
   Reset                           1           1               1                     1              1           1              1

Bits 6:5 – WDTE[1:0] WDT Operating Mode
              Value       Description
              11          WDT enabled regardless of Sleep; the SEN bit in WDTCON0 is ignored
              10          WDT enabled while Sleep = 0, suspended when Sleep = 1; the SEN bit in WDTCON0 is ignored
              01           WDT enabled/disabled by the SEN bit in WDTCON0
              00           WDT disabled, the SEN bit in WDTCON0 is ignored

Bits 4:0 – WDTCPS[4:0] WDT Period Select
                                                  WDTCON0[WDTPS] at POR
                      WDTCPS                                        Typical Time-Out                    Software Control of WDTPS?
                                         Value        Divider Ratio   (FIN = 31 kHz)
                      11111              01011           1:65536        216               2s                         Yes
               11110 to 10011      11110 to 10011         1:32          25               1 ms                        No
                      10010              10010         1:8388608        223           256s                           No
                      10001              10001         1:4194304        222           128s                           No
                      10000              10000         1:2097152        221            64s                           No
                      01111              01111         1:1048576        220            32s                           No
                      01110              01110          1:524288        219            16s                           No
                      01101              01101          1:262144        218             8s                           No
                      01100              01100          1:131072        217             4s                           No
                      01011              01011          1:65536         216             2s                           No
                      01010              01010          1:32768         215             1s                           No
                      01001              01001          1:16384         214          512 ms                          No
                      01000              01000           1:8192         213          256 ms                          No
                      00111              00111           1:4096         212          128 ms                          No
                      00110              00110           1:2048         211           64 ms                          No
                      00101              00101           1:1024         210           32 ms                          No
                      00100              00100            1:512         29            16 ms                          No
                      00011              00011            1:256         28             8 ms                          No
                      00010              00010            1:128         27             4 ms                          No
                      00001              00001             1:64         26             2 ms                          No
                      00000              00000             1:32         25             1 ms                          No


--- p48 ---
8.5.6         CONFIG6

              Name:          CONFIG6
              Address:       0x300005

              Configuration Byte 6

        Bit           7            6               5            4                   3              2          1                0
                                                            WDTCCS[2:0]                                   WDTCWS[2:0]
  Access                                          R/W          R/W                 R/W          R/W          R/W              R/W
   Reset                                           1            1                   1            1            1                1

Bits 5:3 – WDTCCS[2:0] WDT Input Clock Selector
              Value         Condition            Description
              x             WDTE = 00            These bits have no effect
              111           WDTE ≠ 00            Software control
              110 to        WDTE ≠ 00            Reserved
              011
              010           WDTE ≠ 00            WDT reference clock is the SOSC
              001           WDTE ≠ 00            WDT reference clock is the 31.25 kHz MFINTOSC
              000           WDTE ≠ 00            WDT reference clock is the 31.0 kHz LFINTOSC


Bits 2:0 – WDTCWS[2:0] WDT Window Select
                                        WDTCON1[WINDOW] at POR
                                                                                         Software Control of
              WDTCWS            Window Delay Percent of        Window Opening                                  Keyed Access Required?
                          Value                                                               WINDOW
                                        Time                   Percent of Time
                111       111             n/a                        100                         Yes                    No
                110       110             n/a                        100
                101       101              25                         75
                100       100             37.5                       62.5
                011       011              50                         50                         No                     Yes
                010       010             62.5                       37.5
                001       001              75                         25
                000       000             87.5                       12.5


--- p49 ---
8.5.7         CONFIG7

              Name:            CONFIG7
              Address:         0x300006

              Configuration Byte 7

        Bit           7               6                 5            4                 3               2                1               0
                                                      DEBUG        SAFEN             BBEN                           BBSIZE[2:0]
  Access                                               R/W          R/W               R/W         R/W                  R/W             R/W
   Reset                                                1            1                 1           1                    1               1

Bit 5 – DEBUG Debugger Enable
              Value           Description
              1               Background debugger disabled
              0               Background debugger enabled

Bit 4 – SAFEN Storage Area Flash (SAF) Enable(1)
              Value           Description
              1               SAF is disabled
              0               SAF is enabled

Bit 3 – BBEN Boot Block Enable(1)
              Value           Description
              1               Boot Block is disabled
              0               Boot Block is enabled

Bits 2:0 – BBSIZE[2:0] Boot Block Size Selection(2)

              Table 8-1. Boot Block Size
                                                              End Address of                     Boot Block Size (words)
                      BBEN                  BBSIZE
                                                                Boot Block        PIC18Fx4Q41              PIC18Fx5Q41            PIC18Fx6Q41
                          1                     xxx                 –                                           –
                          0                     111             00 03FFh                                       512
                          0                     110             00 07FFh                                      1024
                          0                     101             00 0FFFh                                      2048
                          0                     100             00 1FFFh                                      4096
                          0                     011             00 3FFFh                –                                8192
                          0                     010             00 7FFFh                          –                                 16384
                          0                     001             00 FFFFh                                        –
                          0                     000             01 FFFFh                                        –

              Notes:
              1. Once protection is enabled through ICSP™ or a self-write, it can only be reset through a Bulk
                 Erase.
              2. BBSIZE[2:0] bits can only be changed when BBEN = 1. Once BBEN = 0, BBSIZE[2:0] can only be
                 changed through a Bulk Erase.


--- p50 ---
8.5.8         CONFIG8

              Name:       CONFIG8
              Address:    0x300007

              Configuration Byte 8

        Bit       7               6              5                  4               3       2      1              0
                WRTAPP                                                            WRTSAF   WRTD   WRTC           WRTB
  Access         R/W                                                               R/W     R/W    R/W            R/W
   Reset          1                                                                 1       1      1              1

Bit 7 – WRTAPP Application Block Write Protection(1)
              Value      Description
              1          Application Block is not write-protected
              0          Application Block is write-protected

Bit 3 – WRTSAF Storage Area Flash (SAF) Write Protection(1,2)
              Value      Description
              1          SAF is not write-protected
              0          SAF is write-protected

Bit 2 – WRTD Data EEPROM Write Protection(1)
              Value      Description
              1          Data EEPROM is not write-protected
              0          Data EEPROM is write-protected

Bit 1 – WRTC Configuration Register Write Protection(1)
              Value      Description
              1          Configuration registers are not write-protected
              0          Configuration registers are write-protected

Bit 0 – WRTB Boot Block Write Protection(1,3)
              Value      Description
              1          Boot Block is not write-protected
              0          Boot Block is write-protected

              Notes:
              1. Once protection is enabled through ICSP™ or a self-write, it can only be reset through a Bulk
                 Erase.
              2. Applicable only if SAFEN = 0.
              3. Applicable only if BBEN = 0.


--- p51 ---
8.5.9         CONFIG9

              Name:        CONFIG9
              Address:     0x300008

              Configuration Byte 9

        Bit           7           6             5              4                  3             2   1              0
                                                                                                                  CP
  Access                                                                                                         R/W
   Reset                                                                                                           1

Bit 0 – CP User Program Flash Memory and Data EEPROM Code Protection
              Value       Description
              1           User Program Flash Memory and Data EEPROM code protection are disabled
              0           User Program Flash Memory and Data EEPROM code protection are enabled


--- p52 ---
8.6        Register Summary - Configuration Settings
Address       Name      Bit Pos.      7          6           5             4          3          2           1           0
  0x00
   ...       Reserved
0x2FFFFF
0x300000     CONFIG1      7:0                          RSTOSC[2:0]                                       FEXTOSC[2:0]
0x300001     CONFIG2      7:0      FCMENS      FCMENP     FCMEN                     CSWEN                  PR1WAY     CLKOUTEN
0x300002     CONFIG3      7:0           BOREN[1:0]       LPBOREN      IVT1WAY      MVECEN          PWRTS[1:0]           MCLRE
0x300003     CONFIG4      7:0       XINST                    LVP       STVREN      PPS1WAY      ZCD              BORV[1:0]
0x300004     CONFIG5      7:0                      WDTE[1:0]                                 WDTCPS[4:0]
0x300005     CONFIG6      7:0                                        WDTCCS[2:0]                         WDTCWS[2:0]
0x300006     CONFIG7      7:0                             DEBUG        SAFEN        BBEN                  BBSIZE[2:0]
0x300007     CONFIG8      7:0      WRTAPP                                          WRTSAF      WRTD         WRTC         WRTB
0x300008     CONFIG9      7:0                                                                                              CP


8.7        Register Definitions: Device ID and Revision ID


--- p53 ---
8.7.1         Device ID

              Name:       DEVICEID
              Address:    0x3FFFFE

              Device ID Register

        Bit        15          14            13             12                  11        10            9                8
                                                                  DEV[15:8]
  Access           R               R          R              R                  R             R         R               R
   Reset           q               q          q              q                  q             q         q               q

        Bit        7               6          5              4                  3             2         1                0
                                                                   DEV[7:0]
  Access           R               R          R              R                  R             R         R               R
   Reset           q               q          q              q                  q             q         q               q

Bits 15:0 – DEV[15:0] Device ID
                                         Device                                                   Device ID
                                       PIC18F04Q41                                                 7540h
                                       PIC18F05Q41                                                 7500h
                                       PIC18F06Q41                                                 7580h
                                       PIC18F14Q41                                                 7520h
                                       PIC18F15Q41                                                 74E0h
                                       PIC18F16Q41                                                 7560h


--- p54 ---
8.7.2         Revision ID

              Name:         REVISIONID
              Address:      0x3FFFFC

              Revision ID Register

        Bit        15            14                  13            12                  11         10            9              8
                                         1010[3:0]                                                  MJRREV[5:2]
  Access           R                 R               R              R                  R          R             R             R
   Reset           1                 0               1              0                  q          q             q             q

        Bit        7                 6               5              4                  3           2           1               0
                       MJRREV[1:0]                                                      MNRREV[5:0]
  Access           R                 R               R              R                  R           R           R              R
   Reset           q                 q               q              q                  q           q           q              q

Bits 15:12 – 1010[3:0] Read as ‘b1010
         These bits are fixed with value ‘b1010 for all devices in this family.

Bits 11:6 – MJRREV[5:0] Major Revision ID
         These bits are used to identify a major revision (A0, B0, C0, etc.).
         Revision A = ‘b00 0000
         Revision B = ‘b00 0001

Bits 5:0 – MNRREV[5:0] Minor Revision ID
          These bits are used to identify a minor revision.
          Revision A0 = ‘b00 0000
          Revision B0 = ‘b00 0000
          Revision B1 = ‘b00 0001


                            Tip: For example, the REVISIONID register value for revision B1 will be 0xA041.


--- p55 ---
8.8        Register Summary - DEVID/REVID
Address       Name       Bit Pos.   7                 6                5             4               3             2                 1         0
  0x00
   ...       Reserved
0x3FFFFB
                           7:0          MJRREV[1:0]                                                  MNRREV[5:0]
0x3FFFFC    REVISIONID
                          15:8                            1010[3:0]                                                    MJRREV[5:2]
                           7:0                                                           DEV[7:0]
0x3FFFFE    DEVICEID
                          15:8                                                           DEV[15:8]


--- p56 ---
