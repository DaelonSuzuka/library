                      PIC18(L)F26/27/45/46/47/55/56/57K42
5.0      DEVICE CONFIGURATION
Device configuration consists of the C2017-2021onfig-
uration Words, User ID, Device ID, Rev ID, Device
Information Area (DIA), (see Section 5.7 “Device
Information Area”), and the Device Configuration
Information (DCI) regions, (see Section 5.8 “Device
Configuration Information”).

5.1      Configuration Words
There are six Configuration Word bits that allow the
user to setup the device with several choices of
oscillators, Resets and memory protection options.
These are implemented as Configuration Word 1
through Configuration Word 6 at 300000h through
30000Bh.


 2017-2021 Microchip Technology Inc.                   DS40001919G-page 65
                      PIC18(L)F26/27/45/46/47/55/56/57K42
5.2       Register Definitions: Configuration Words

REGISTER 5-1:          CONFIGURATION WORD 1L (30 0000h)
        U-1          R/W-1              R/W-1       R/W-1       U-1            R/W-1       R/W-1          R/W-1
        —                       RSTOSC[2:0]                      —                     FEXTOSC[2:0]
bit 7                                                                                                          bit 0


Legend:
R = Readable bit                 W = Writable bit           U = Unimplemented bit, read as ‘1’
-n = Value for blank device      ‘1’ = Bit is set           ‘0’ = Bit is cleared        x = Bit is unknown


bit 7            Unimplemented: Read as ‘1’
bit 6-4          RSTOSC[2:0]: Power-up Default Value for COSC bits
                 111 = EXTOSC operating per FEXTOSC[2:0] bits
                 110 = HFINTOSC with HFFRQ = 4 MHz and CDIV = 4:1
                 101 = LFINTOSC
                 100 = SOSC
                 011 = Reserved
                 010 = EXTOSC with 4x PLL, with EXTOSC operating per FEXTOSC[2:0] bits
                 001 = Reserved
                 000 = HFINTOSC with HFFRQ = 64 MHz and CDIV = 1:1; resets COSC/NOSC to 3’b110
bit 3            Unimplemented: Read as ‘1’
bit 2-0          FEXTOSC[2:0]: FEXTOSC External Oscillator Mode Selection bits
                 111 = ECH (External Clock High Power)(1)
                 110 = ECM (External Clock Medium Power)(1)
                 101 = ECL (External Clock Low Power)(1)
                 100 = Oscillator is not enabled
                 011 = Reserved (do not use)
                 010 = HS (crystal oscillator) above 8 MHz
                 001 = XT (crystal oscillator) above 500 kHz, below 8 MHz
                 000 = LP (crystal oscillator) optimized for 32.768 kHz
   Note 1: Refer to Table 44-8 for External Clock/Oscillator Timing Requirements.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 66
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-2:          CONFIGURATION WORD 1H (30 0001h)
        U-1            U-1              R/W-1       U-1         R/W-1               U-1      R/W-1         R/W-1
        —              —            FCMEN           —          CSWEN                —      PR1WAY        CLKOUTEN
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                 W = Writable bit            U = Unimplemented bit, read as ‘1’
-n = Value for blank device      ‘1’ = Bit is set            ‘0’ = Bit is cleared         x = Bit is unknown


bit 7-6          Unimplemented: Read as ‘1’
bit 5            FCMEN: Fail-Safe Clock Monitor Enable bit
                 1 = FSCM timer is enabled
                 0 = FSCM timer is disabled
bit 4            Unimplemented: Read as ‘1’
bit 3            CSWEN: Clock Switch Enable bit
                 1 = Writing to NOSC and NDIV is allowed
                 0 = The NOSC and NDIV bits cannot be changed by user software
bit 2            Unimplemented: Read as ‘1’
bit 1            PR1WAY: PRLOCKED One-Way Set Enable bit
                 1 = PRLOCKED bit can be cleared and set only once; Priority registers remain locked after one
                     clear/set cycle
                 0 = PRLOCKED bit can be set and cleared multiple times (subject to the unlock sequence)
bit 0            CLKOUTEN: Clock Out Enable bit
                 If FEXTOSC[2:0] = EC (high, mid or low) or Not Enabled:
                 1 = CLKOUT function is disabled; I/O or oscillator function on OSC2
                 0 = CLKOUT function is enabled; FOSC/4 clock appears at OSC2
                 Otherwise:
                 This bit is ignored.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 67
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-3:           CONFIGURATION WORD 2L (30 0002h)
        R/W-1         R/W-1             R/W-1         R/W-1       R/W-1           R/W-1       R/W-1         R/W-1
           BOREN[1:0]              LPBOREN           IVT1WAY    MVECEN                PWRTS[1:0]            MCLRE
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘1’
-n = Value for blank device       ‘1’ = Bit is set             ‘0’ = Bit is cleared        x = Bit is unknown


bit 7-6          BOREN[1:0]: Brown-out Reset Enable bits
                 When enabled, Brown-out Reset Voltage (VBOR) is set by the BORV bit.
                 11 = Brown-out Reset is enabled, SBOREN bit is ignored
                 10 = Brown-out Reset is enabled while running, disabled in Sleep; SBOREN is ignored
                 01 = Brown-out Reset is enabled according to SBOREN
                 00 = Brown-out Reset is disabled
bit 5            LPBOREN: Low-Power BOR Enable bit
                 1 = Low-Power BOR is disabled
                 0 = Low-Power BOR is enabled
bit 4            IVT1WAY: IVTLOCK bit One-Way Set Enable bit
                 1 = IVTLOCKED bit can be cleared and set only once; IVT registers remain locked after one clear/set
                     cycle
                 0 = IVTLOCK ED bit can be set and cleared multiple times (subject to the unlock sequence)
bit 3            MVECEN: Multi-vector Enable bit
                 1 = Multi-vector enabled; Vector table used for interrupts
                 0 = Legacy interrupt behavior
bit 2-1          PWRTS[1:0]: Power-up Timer Selection bits
                 11 = PWRT is disabled
                 10 = PWRT set at 64 ms (2048 LFINTOSC Cycles)
                 01 = PWRT set at 16 ms (512 LFINTOSC Cycles)
                 00 = PWRT set at 1 ms (32 LFINTOSC Cycles)
bit 0            MCLRE: Master Clear (MCLR) Enable bit
                 If LVP = 1:
                 RE3 pin function is MCLR
                 If LVP = 0:
                 1 = MCLR pin is MCLR
                 0 = MCLR pin function is a port defined function


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 68
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-4:          CONFIGURATION WORD 2H (30 0003h)
    R/W-1             U-1            R/W-1          R/W-1       R/W-1               R/W-1      R/W-1         R/W-1
    XINST             —             DEBUG           STVREN   PPS1WAY                ZCD            BORV[1:0](1)
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit            U = Unimplemented bit, read as ‘1’
-n = Value for blank device      ‘1’ = Bit is set            ‘0’ = Bit is cleared           x = Bit is unknown


bit 7           XINST: Extended Instruction Set Enable bit
                1 = Extended instruction set and Indexed Addressing mode are disabled (Legacy mode)
                0 = Extended instruction set and Indexed Addressing mode are enabled
bit 6           Unimplemented: Read as ‘1’
bit 5           DEBUG: Debugger Enable bit
                1 = Background debugger is disabled
                0 = Background debugger is enabled
bit 4           STVREN: Stack Overflow/Underflow Reset Enable bit
                1 = Stack Overflow or Underflow will cause a Reset
                0 = Stack Overflow or Underflow will not cause a Reset
bit 3           PPS1WAY: PPSLOCKED One-Way Set Enable bit
                1 = PPSLOCKED bit can be cleared and set only once; PPS registers remain locked after one clear/set
                    cycle
                0 = PPSLOCKED bit can be set and cleared multiple times (subject to the unlock sequence)
bit 2           ZCD: Zero-Cross Detect Enable bit
                1 = ZCD is disabled; ZCD can be enabled by setting the bit SEN of the ZCDCON register
                0 = ZCD is always enabled
bit 1-0         BORV[1:0]: Brown-out Reset Voltage Selection bits(1)
                PIC18FXXK42 Devices:
                11 = Brown-out Reset Voltage (VBOR) is set to 2.45V
                10 = Brown-out Reset Voltage (VBOR) is set to 2.45V
                01 = Brown-out Reset Voltage (VBOR) is set to 2.7V
                00 = Brown-out Reset Voltage (VBOR) is set to 2.85V
                PIC18LFXXK42 Device:
                11 = Brown-out Reset Voltage (VBOR) is set to 1.90V
                10 = Brown-out Reset Voltage (VBOR) is set to 2.45V
                01 = Brown-out Reset Voltage (VBOR) is set to 2.7V
                00 = Brown-out Reset Voltage (VBOR) is set to 2.85V

Note 1: The higher voltage setting is recommended for operation at or above 16 MHz.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 69
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-5:          CONFIGURATION WORD 3L (30 0004h)
        U-1          R/W-1              R/W-1       R/W-1         R/W-1           R/W-1           R/W-1         R/W-1
        —                 WDTE[1:0]                                            WDTCPS[4:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘1’
-n = Value for blank device      ‘1’ = Bit is set              ‘0’ = Bit is cleared            x = Bit is unknown


bit 7            Unimplemented: Read as ‘1’
bit 6-5          WDTE[1:0]: WDT Operating Mode bits
                 00 = WDT is disabled, SWDTEN is ignored
                 01 = WDT is enabled/disabled by the SWDTEN bit in WDTCON0
                 10 = WDT is enabled while Sleep = 0, suspended when Sleep = 1; SWDTEN is ignored
                 11 = WDT is enabled regardless of Sleep; SWDTEN is ignored
bit 4-0          WDTCPS[4:0]: WDT Period Select bits

                                                            WDTPS at POR
                                                                                                     Software Control
                  WDTCPS[4:0]                                                   Typical Time-out
                                         Value         Divider Ratio                                   of WDTPS?
                                                                                 (FIN = 31 kHz)
                      00000              00000                1:32     25             1 ms
                      00001              00001                1:64     26             2 ms
                      00010              00010               1:128     27             4 ms
                                                                          8
                      00011              00011               1:256     2              8 ms
                      00100              00100               1:512     29             16 ms
                      00101              00101              1:1024    210             32 ms
                      00110              00110              1:2048    211             64 ms
                      00111              00111              1:4096    212             128 ms
                      01000              01000              1:8192    213             256 ms
                                                                          14
                      01001              01001          1:16384       2               512 ms                 No
                      01010              01010          1:32768       215             1s
                      01011              01011          1:65536       216             2s
                      01100              01100         1:131072       217             4s
                      01101              01101         1:262144       218             8s
                      01110              01110         1:524299       219             16s
                                                                          20
                      01111              01111        1:1048576       2               32s
                      10000              10000        1:2097152       221             64s
                      10001              10001        1:4194304       222             128s
                      10010              10010        1:8388608       223             256s
                      10011              10011
                        ...                ...                1:32     25             1 ms                   No
                      11110              11110
                      11111              01011          1:65536       216             2s                     Yes


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 70
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-6:          CONFIGURATION WORD 3H (30 0005h)
        U-1            U-1              R/W-1        R/W-1         R/W-1           R/W-1       R/W-1          R/W-1
        —              —                         WDTCCS[2:0]                               WDTCWS[2:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘1’
-n = Value for blank device      ‘1’ = Bit is set               ‘0’ = Bit is cleared        x = Bit is unknown


bit 7-6          Unimplemented: Read as ‘1’
bit 5-3          WDTCCS[2:0]: WDT Input Clock Selector bits
                 If WDTE[1:0] Fuses = 2’b00:
                 These bits are ignored.
                 Otherwise:
                 000 = WDT reference clock is the 31.0 kHz LFINTOSC
                 001 = WDT reference clock is the 31.25 kHz MFINTOSC
                 010 = WDT reference clock is SOSC
                 011 = Reserved (default to LFINTOSC)
                 •
                 •
                 110 = Reserved (default to LFINTOSC)
                 111 = Software control
bit 2-0          WDTCWS[2:0]: WDT Window Select bits

                                                       Window at POR                       Software         Keyed
                   WDTCWS[2:0]                       Window Delay       Window Opening     Control of       Access
                                         Value                                              Window         Required?
                                                    Percent of Time     Percent of Time
                        000               000            87.5                   12.5
                        001               001             75                     25
                        010               010            62.5                   37.5
                        011               011             50                     50            No             Yes
                        100               100            37.5                   62.5
                        101               101             25                     75
                        110               111             n/a                    100
                        111               111             n/a                    100           Yes            No


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 71
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-7:          CONFIGURATION WORD 4L (30 0006h)
     R/W-1             U-1              U-1               R/W-1      R/W-1           R/W-1           R/W-1         R/W-1
  WRTAPP (1)           —                —             SAFEN (1)    BBEN (1)                   BBSIZE[2:0] (2)
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit                U = Unimplemented bit, read as ‘1’
-n = Value for blank device       ‘1’ = Bit is set                ‘0’ = Bit is cleared          x = Bit is unknown


bit 7            WRTAPP: Application Block Write Protection bit(1)
                 1 = Application Block is NOT write-protected
                 0 = Application Block is write-protected
bit 6-5          Unimplemented: Read as ‘1’
bit 4            SAFEN: Storage Area Flash Enable bit(1)
                 1 = SAF is disabled
                 0 = SAF is enabled
bit 3            BBEN: Boot Block Enable bit(1)
                 1 = Boot Block disabled
                 0 = Boot Block enabled
bit 2-0          BBSIZE[2:0]: Boot Block Size Selection bits(2)
                 Refer to Table 5-1.

Note 1: Bits are implemented as sticky bits. Once protection is enabled through ICSP™ or a self-write, it can only be
        reset through a Bulk Erase.
     2: BBSIZE[2:0] bits can only be changed when BBEN = 1. Once BBEN = 0, BBSIZE[2:0] can only be changed
        through a Bulk Erase.

TABLE 5-1:         BOOT BLOCK SIZE BITS
                                          Boot Block Size                                             Device Size(1)
    BBEN            BBSIZE[2:0]                                   END_ADDRESS_BOOT
                                             (words)                                            16k          32k       64k
        1                xxx                          0                        —                 X           X          X
        0                111                         512                  00 03FFh               X           X          X
        0                110                         1024                 00 07FFh               X           X          X
        0                101                         2048                 00 0FFFh               X           X          X
        0                100                         4096                 00 1FFFh               X           X          X
        0                011                         8192                 00 3FFFh               X           X          X
        0                010                     16384                    00 7FFFh               —           X          X
        0                001                     32768                    00 FFFFh                       Note 2         X
        0                000                     32768                    00 FFFFh               —           —         —
Note 1: For each device, the quoted device size specification is listed in Table 4-1.
     2: The maximum boot block size is half the user program memory size. All selections higher than the maximum size default
        to maximum boot block size of half PFM. For example, all settings of BBSIZE = 000 through BBSIZE = 011, default to a
        boot block size of 8 kW on a 16 kW device.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 72
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-8:          CONFIGURATION WORD 4H (30 0007h)
        U-1            U-1              R/W-1       U-1           R/W-1              R/W-1       R/W-1         R/W-1

        —              —                LVP(2)      —         WRTSAF (1,3)       WRTD (1,4)    WRTC (1)      WRTB(1,5)
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘1’
-n = Value for blank device      ‘1’ = Bit is set             ‘0’ = Bit is cleared            x = Bit is unknown


bit 7-6          Unimplemented: Read as ‘1’
bit 5            LVP: Low-Voltage Programming Enable bit(2)
                 1 = Low-voltage programming enabled. MCLR/VPP pin function is MCLR. MCLRE (Register 5-3) is
                      ignored.
                 0 = HV on MCLR/VPP must be used for programming.
bit 4            Unimplemented: Read as ‘1’
bit 3            WRTSAF: Storage Area Flash (SAF) Write Protection bit(1,3)
                 1 = SAF is NOT write-protected
                 0 = SAF is write-protected
bit 2            WRTD: Data EEPROM Write Protection bit(1,4)
                 1 = Data EEPROM NOT write-protected
                 0 = Data EEPROM write-protected
bit 1            WRTC: Configuration Register Write Protection bit(1)
                 1 = Configuration Register NOT write-protected
                 0 = Configuration Register write-protected
bit 0            WRTB: Boot Block Write Protection bit(1,5)
                 1 = Boot Block NOT write-protected
                 0 = Boot Block write-protected
Note 1: Bits are implemented as sticky bits. Once protection is enabled through ICSP or a self write, it can only be
        reset through a Bulk Erase.
      2: The LVP bit cannot be written (to zero) while operating from the LVP programming interface. The purpose of
          this rule is to prevent the user from dropping out of LVP mode while programming from LVP mode, or acci-
          dentally eliminating LVP mode from the configuration state.
      3: Unimplemented if SAF is not present and only applicable if SAFEN = 0.
      4: Unimplemented if data EEPROM is not present.
      5: Only applicable if BBEN = 0.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 73
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-9:          CONFIGURATION WORD 5L (30 0008h)
        U-1            U-1                U-1               U-1                U-1                 U-1             U-1                R/W-1
        —              —                     —                 —                —                  —                —                  CP
bit 7                                                                                                                                        bit 0


Legend:
R = Readable bit                   W = Writable bit                        U = Unimplemented bit, read as ‘1’
-n = Value for blank device        ‘1’ = Bit is set                        ‘0’ = Bit is cleared                x = Bit is unknown


bit 7-1          Unimplemented: Read as ‘1’
bit 0            CP: User Program Flash Memory and Data EEPROM Code Protection bit
                 1 = User Program Flash Memory and Data EEPROM code protection is disabled
                 0 = User Program Flash Memory and Data EEPROM code protection is enabled


REGISTER 5-10:         CONFIGURATION WORD 5H (30 0009h)
        U-1            U-1                U-1               U-1                U-1                 U-1             U-1                 U-1
        —              —                     —                 —                —                  —                —                  —
bit 7                                                                                                                                        bit 0


Legend:
R = Readable bit                   W = Writable bit                        U = Unimplemented bit, read as ‘1’
-n = Value for blank device        ‘1’ = Bit is set                        ‘0’ = Bit is cleared                x = Bit is unknown


bit 7-0          Unimplemented: Read as ‘1’


TABLE 5-2:           SUMMARY OF CONFIGURATION WORDS
                                                                                                                                              Default/
 Address      Name      Bit 7        Bit 6          Bit 5          Bit 4       Bit 3       Bit 2          Bit 1               Bit 0        Unprogrammed
                                                                                                                                               Value

30 0000h CONFIG1L        —                       RSTOSC[2:0]                    —                        FEXTOSC[2:0]                         1111 1111

30 0001h CONFIG1H        —            —            FCMEN            —         CSWEN         —            PR1WAY          CLKOUTEN             1111 1111

30 0002h CONFIG2L            BOREN[1:0]           LPBOREN      IVT1WAY       MVECEN               PWRTS[1:0]               MCLRE              1111 1111

30 0003h CONFIG2H       XINST         —            DEBUG       STVREN        PPS1WAY       ZCD                    BORV[1:0]                   1111 1111

30 0004h CONFIG3L        —                WDTE[1:0]                                        WDTCPS[4:0]                                        1111 1111

30 0005h CONFIG3H        —            —                     WDTCCS[2:0]                                  WDTCWS[2:0]                          1111 1111

30 0006h CONFIG4L      WRTAPP         —              —         SAFEN           BBEN                       BBSIZE[2:0]                         1111 1111

30 0007h CONFIG4H        —            —             LVP             —        WRTSAF       WRTD            WRTC             WRTB               1111 1111

30 0008h CONFIG5L        —            —              —              —           —           —               —                 CP              1111 1111

30 0009h CONFIG5H        —            —              —              —           —           —               —                  —              1111 1111


 2017-2021 Microchip Technology Inc.                                                                                   DS40001919G-page 74
                      PIC18(L)F26/27/45/46/47/55/56/57K42
5.3         Code Protection
Code protection allows the device to be protected from
external access. Program memory protection and data
memory are controlled through the CP Configuration
bit. Internal access to the program memory is
unaffected by code protection setting.
The entire program memory space and Data
EEPROM is protected from external reads and writes
by the CP bit in Configuration Words. When CP = 0,
external reads and writes of memory are inhibited and
a read will return all ‘0’s. The CPU can continue to
read program memory and data EEPROM, regardless
of the protection bit settings. Self-writing the program
memory or Data EEPROM is dependent upon the
write protection settings.

5.4      User ID
Eight words in the memory space (200000h-20000Fh)
are designated as ID locations where the user can
store checksum or other code identification numbers.
These locations are readable and writable during
normal execution. See Section 13.2 “Device
Information Area, Device Configuration Area, User
ID, Device ID and Configuration Word Access” for
more information on accessing these memory
locations. For more information on checksum
calculation, see the “PIC18(L)F26/27/45/46/47/55/56/
57K42      Memory      Programming      Specification”
(DS40001886).


 2017-2021 Microchip Technology Inc.                      DS40001919G-page 75
                      PIC18(L)F26/27/45/46/47/55/56/57K42
5.5          Device ID and Revision ID
The 16-bit device ID word is located at 3F FFFEh and
the 16-bit revision ID is located at 3F FFFCh. These
locations are read-only and cannot be erased or
modified.
Development tools, such as device programmers and
debuggers, may be used to read the Device ID,
Revision ID and Configuration Words. Refer to 13.0
“Nonvolatile Memory (NVM) Control” for more
information on accessing these locations.

5.6          Register Definitions: Device ID and Revision ID

REGISTER 5-11:         DEVICE ID: DEVICE ID REGISTER
         R              R               R           R              R               R        R               R
                                                    DEV[15:8]
bit 15                                                                                                          bit 8


         R              R               R           R              R               R        R               R
                                                        DEV[7:0]
bit 7                                                                                                           bit 0


Legend:
R = Readable bit                 ‘1’ = Bit is set            0’ = Bit is cleared       x = Bit is unknown


bit 15-0          DEV[15:0]: Device ID bits

                                Device                                 Device ID
                            PIC18F26K42                                 6C60h
                            PIC18F27K42                                 6C40h
                            PIC18F45K42                                 6C20h
                            PIC18F46K42                                 6C00h
                            PIC18F47K42                                 6BE0h
                            PIC18F55K42                                 6BC0h
                            PIC18F56K42                                 6BA0h
                            PIC18F57K42                                 6B80h
                            PIC18LF26K42                                6DA0h
                            PIC18LF27K42                                6D80h
                            PIC18LF45K42                                6D60h
                            PIC18LF46K42                                6D40h
                            PIC18LF47K42                                6D20h
                            PIC18LF55K42                                6D00h
                            PIC18LF56K42                                6CE0h
                            PIC18LF57K42                                6CC0h


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 76
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 5-12:            REVISION ID: REVISION ID REGISTER
          R                 R             R              R              R               R             R              R
          1                 0             1               0                               MJRREV[5:2]
bit 15                                                                                                                   bit 8


          R                 R             R              R              R               R             R              R
              MJRREV[1:0]                                                   MNRREV[5:0]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                    ‘1’ = Bit is set              0’ = Bit is cleared           x = Bit is unknown


bit 15-12           Read as ‘1010’
                    These bits are fixed with value ‘1010’ for all devices in this family.
bit 11-6            MJRREV[5:0]: Major Revision ID bits
                    These bits are used to identify a major revision. A major revision is indicated by revision (A0, B0, C0,
                    etc.)
                    Revision A = 0b00 0000
bit 5-0             MNRREV[5:0]: Minor Revision ID bits
                    These bits are used to identify a minor revision.
                    Revision A0 = 0b00 0000


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 77
                      PIC18(L)F26/27/45/46/47/55/56/57K42
5.7      Device Information Area
The Device Information Area (DIA) is a dedicated
region in the Program memory space. The DIA
contains the calibration data for the internal
temperature indicator module, stores the Microchip
Unique Identifier words and the Fixed Voltage
Reference voltage readings measured in mV.
The complete DIA table is shown in Table 5-3: Device
Information Area, followed by a description of each
region and its functionality. The data is mapped from
3F0000h to 3F003Fh in the PIC18(L)F26/27/45/46/47/
55/56/57K42 family. These locations are read-only and
cannot be erased or modified by the user. The data is
programmed into the device during manufacturing.

TABLE 5-3:        DEVICE INFORMATION AREA
   Address Range           Name of Region                             Standard Device Information
                                MUI0
                                MUI1
                                MUI2
3F0000h-3F000Bh                                Microchip Unique Identifier (6 Words)
                                MUI3
                                MUI4
                                MUI5
                                MUI6
3F000Ch-3F000Fh                                Unassigned (2 Words)
                                MUI7
                                 EUI0
                                 EUI1
                                 EUI2
                                 EUI3
                                 EUI4
3F0010h-3F0023h                                Optional External Unique Identifier (10 Words)
                                 EUI5
                                 EUI6
                                 EUI7
                                 EUI8
                                 EUI9
3F0024h-3F0025h                                                Reserved (1 Word)
3F0026h-3F0027h                 TSLR2          Temperature Indicator ADC reading at @ 90°C (low range setting)
3F0028h-3F0029h                                                Reserved (1 Word)
3F002Ah-3F002Bh                                                Reserved (1 Word)
3F002Ch-3F002Dh                TSHR2           Temperature Indicator ADC reading at @ 90°C (high range setting)
3F002Eh-3F002Fh                                                Reserved (1 Word)
3F0030h-3F0031h                FVRA1X          ADC FVR1 Output voltage for 1x setting (in mV)
3F0032h-3F0033h                FVRA2X          ADC FVR1 Output Voltage for 2x setting (in mV)
3F0034h-3F0035h                FVRA4X          ADC FVR1 Output Voltage for 4x setting (in mV)
3F0036h-3F0037h                FVRC1X          Comparator FVR2 output voltage for 1x setting (in mV)
3F0038h-3F0039h                FVRC2X          Comparator FVR2 output voltage for 2x setting (in mV)
3F003Ah-3F003Bh               FVRC4X(1)        Comparator FVR2 output voltage for 4x setting (in mV)
3F003Ch-3F003Fh                                Unassigned (2 Words)
Note 1:     Value not present on LF devices.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 78
                      PIC18(L)F26/27/45/46/47/55/56/57K42
5.7.1       MICROCHIP UNIQUE IDENTIFIER                    5.7.3      ANALOG-TO-DIGITAL
            (MUI)                                                     CONVERSION DATA OF THE
The PIC18(L)F26/27/45/46/47/55/56/57K42 devices                       TEMPERATURE SENSOR
are individually encoded during final manufacturing        The purpose of the Temperature Sensor module is to
with a Microchip Unique Identifier, or MUI. The MUI        provide a temperature-dependent voltage that can be
cannot be user-erased. This feature allows for             measured by an analog module, see Section
manufacturing traceability of Microchip Technology         35.0 “Temperature Indicator Module”.
devices in applications where this is a required. It may
                                                           The DIA table contains the internal ADC measurement
also be used by the application manufacturer for a
                                                           values of the Temperature sensor for Low and High
number of functions that require unverified unique
                                                           range at fixed points of reference. The values are
identification, such as:
                                                           measured during test and are unique to each device.
• Tracking the device                                      The measurement data is stored in the DIA memory
• Unique serial number                                     region as hexadecimal numbers corresponding to the
                                                           ADC conversion result. The calibration data can be
The MUI consists of six program words. When read
                                                           used to plot the approximate sensor output voltage,
together, these fields form a unique identifier. The MUI
                                                           VTSENSE vs. Temperature curve without having to
is stored in nine read-only locations, located between
                                                           make calibration measurements in the application. For
3F0000h to 3F000Fh in the DIA space. Table 5-3 lists
                                                           more information on the operation of the Temperature
the addresses of the identifier words.
                                                           Sensor, refer to Section 35.0 “Temperature Indicator
  Note:     For applications that require verified         Module”.
            unique identification, contact your            • TSLR2: Address 3F0026h to 3F0027h store the
            Microchip Technology sales office to             measurements for the low-range setting of the
            create a Serialized Quick Turn                   Temperature Sensor at VDD = 3V.
            ProgrammingSM option.                          • TSHR2: Address 3F002Ch to 3F002Dh store the
                                                             measurements for the High Range setting of the
5.7.2       EXTERNAL UNIQUE IDENTIFIER                       Temperature Sensor at VDD = 3V.
            (EUI)                                          • The stored measurements are made by the
The EUI data is stored at locations 3F0010h to               device ADC using the internal VREF = 2.048V.
3F0023h in the Program Memory region. This region is
an optional space for placing application specific
information. The data is coded per customer
requirements during manufacturing.


  Note:     Data is stored in this address range on
            receiving a request from the customer.
            The customer may contact the local sales
            representative, or Field Applications
            Engineer, and provide them the unique
            identifier information that is supposed to
            be stored in this region.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 79
                          PIC18(L)F26/27/45/46/47/55/56/57K42
5.7.4        FIXED VOLTAGE REFERENCE                                        5.8      Device Configuration Information
             DATA
                                                                            The Device Configuration Information (DCI) is a
The DIA stores measured FVR voltages for this device                        dedicated region in the Program memory space
in mV for the different buffer settings of 1x, 2x or 4x at                  mapped from 3FFF00h to 3FFF09h. The data stored in
Program Memory locations 3F0030h to 3F003Bh. For                            these locations is read-only and cannot be erased.
more information on the FVR, refer to Section 34.0
                                                                            Refer to Table 5-4: Device Configuration Information
“Fixed Voltage Reference (FVR)”.
                                                                            for PIC18(L)F26/27/45/55/46/47/56/57K42 for the
• FVRA1X stores the value of ADC FVR1 Output                                complete DCI table address and description. The DCI
  voltage for 1x setting (in mV)                                            holds information about the device which is useful for
• FVRA2X stores the value of ADC FVR1 Output                                programming and Bootloader applications.
  Voltage for 2x setting (in mV)
                                                                            The erase size is the minimum erasable unit in the
• FVRA4X stores the value of ADC FVR1 Output
                                                                            PFM, expressed as rows. The total device Flash
  Voltage for 4x setting (in mV)
                                                                            memory capacity is (Row Size * Number of rows)
• FVRC1X stores the value of Comparator FVR2
  output voltage for 2x setting (in mV)
• FVRC2X stores the value of Comparator FVR2
  output voltage for 2x setting (in mV)
• FVRC4X stores the value of Comparator FVR2
  output voltage for 4x setting (in mV)
TABLE 5-4:           DEVICE CONFIGURATION INFORMATION FOR PIC18(L)F26/27/45/55/46/47/56/57K42
                                                                                                VALUE
       ADDRESS           Name                DESCRIPTION                                                                               UNITS
                                                                     PIC18(L)F45/55K42   PIC18(L)F26/46/56K42   PIC18(L)F27/47/57K42

 3F FF00h-3F FF01h       ERSIZ     Erase Row Size                           64                    64                     64            Words
 3F FF02h-3F FF03h      WLSIZ      Number of write latches per row          128                  128                    128            Bytes
 3F FF04h-3F FF05h       URSIZ     Number of User Rows                      256                  512                   1024            Rows
 3F FF06h-3F FF07h       EESIZ     Data EEPROM memory size                  256                  1024                  1024            Bytes
 3F FF08h-3F FF09h       PCNT      Pin Count                              40(1)/48            28/40(1)/48            28/40(1)/48       Pins
Note    1:   Pin count of 40 is also used for 44-pin part.


 2017-2021 Microchip Technology Inc.                                                                           DS40001919G-page 80
