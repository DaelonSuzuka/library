                       PIC18(L)F26/27/45/46/47/55/56/57K42
19.0     PERIPHERAL MODULE                                  19.3     Effects of a Reset
         DISABLE (PMD)                                      Following any Reset, each control bit is set to ‘0’,
Sleep, Idle and Doze modes allow users to                   enabling all modules.
substantially reduce power consumption by slowing or
stopping the CPU clock. Even so, peripheral modules         19.4     System Clock Disable
still remain clocked, and thus, consume some amount
                                                            Setting SYSCMD (PMD0, Register 19-1) disables the
of power. There may be cases where the application
                                                            system clock (FOSC) distribution network to the
needs what these modes do not provide: the ability to
                                                            peripherals. Not all peripherals make use of SYSCLK,
allocate limited power resources to the CPU while
                                                            so not all peripherals are affected. Refer to the specific
eliminating power consumption from the peripherals.
                                                            peripheral description to see if it will be affected by this
The PIC18F26/27/45/46/47/55/56/57K42 microcontrol-          bit.
lers address this requirement by allowing peripheral
modules to be selectively enabled or disabled, placing
them into the lowest possible power mode.
All modules are ON by default following any Reset.

19.1     Disabling a Module
Disabling a module has the following effects:
• All clock and control inputs to the module are
  suspended; there are no logic transitions, and the
  module will not function.
• The module is held in Reset.
• Any SFR becomes “unimplemented”
  - Writing is disabled
  - Reading returns 00h
• I/O functionality is prioritized as per Section 16.1,
  I/O Priorities
• All associated Input Selection registers are also
  disabled

19.2     Enabling a Module
When the PMD register bit is cleared, the module is
re-enabled and will be in its Reset state (Power-on
Reset). SFR data will reflect the POR Reset values.
Depending on the module, it may take up to one full
instruction cycle for the module to become active.
There may be no interaction with the module
(e.g., writing to registers) for at least one instruction
after it has been re-enabled.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 290
                         PIC18(L)F26/27/45/46/47/55/56/57K42
19.5     Register Definitions: Peripheral Module Disable

REGISTER 19-1:            PMD0: PMD CONTROL REGISTER 0
    R/W-0/0          R/W-0/0       R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0          R/W-0/0      R/W-0/0
    SYSCMD           FVRMD         HLVDMD           CRCMD       SCANMD        NVMMD         CLKRMD           IOCMD
7                                                                                                                     0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         q = Value depends on condition


bit 7              SYSCMD: Disable Peripheral System Clock Network bit(1)
                   See description in Section 19.4 “System Clock Disable”.
                   1 = System clock network disabled (FOSC)
                   0 = System clock network enabled
bit 6              FVRMD: Disable Fixed Voltage Reference bit
                   1 = FVR module disabled
                   0 = FVR module enabled
bit 5              HLVDMD: Disable High/Low-Voltage Detect bit
                   1 = HLVD module disabled
                   0 = HLVD module enabled
bit 4              CRCMD: Disable CRC Engine bit
                   1 = CRC module disabled
                   0 = CRC module enabled
bit 3              SCANMD: Disable NVM Memory Scanner bit(2)
                   1 = NVM Memory Scan module disabled
                   0 = NVM Memory Scan module enabled
bit 2              NVMMD: NVM Module Disable bit(3)
                   1 = All Memory reading and writing is disabled; NVMCON registers cannot be written
                   0 = NVM module enabled
bit 1              CLKRMD: Disable Clock Reference bit
                   1 = CLKR module disabled
                   0 = CLKR module enabled
bit 0              IOCMD: Disable Interrupt-on-Change bit, All Ports
                   1 = IOC module(s) disabled
                   0 = IOC module(s) enabled

Note 1:       Clearing the SYSCMD bit disables the system clock (FOSC) to peripherals, however peripherals clocked
              by FOSC/4 are not affected.
        2:    Subject to SCANE bit in CONFIG4H.
        3:    When enabling NVM, a delay of up to 1 µs may be required before accessing data.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 291
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 19-2:           PMD1: PMD CONTROL REGISTER 1
   R/W-0/0           R/W-0/0     R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0          R/W-0/0      R/W-0/0
  NCO1MD            TMR6MD       TMR5MD           TMR4MD     TMR3MD         TMR2MD        TMR1MD          TMR0MD
bit 7                                                                                                           bit 0


Legend:
R = Readable bit               W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged           x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set               ‘0’ = Bit is cleared         q = Value depends on condition


bit 7              NCO1MD: Disable NCO1 Module bit
                   1 = NCO1 module disabled
                   0 = NCO1 module enabled
bit 6              TMR6MD: Disable Timer TMR6 bit
                   1 = TMR6 module disabled
                   0 = TMR6 module enabled
bit 5              TMR5MD: Disable Timer TMR5 bit
                   1 = TMR5 module disabled
                   0 = TMR5 module enabled
bit 4              TMR4MD: Disable Timer TMR4 bit
                   1 = TMR4 module disabled
                   0 = TMR4 module enabled
bit 3              TMR3MD: Disable Timer TMR3 bit
                   1 = TMR3 module disabled
                   0 = TMR3 module enabled
bit 2              TMR2MD: Disable Timer TMR2 bit
                   1 = TMR2 module disabled
                   0 = TMR2 module enabled
bit 1              TMR1MD: Disable Timer TMR1 bit
                   1 = TMR1 module disabled
                   0 = TMR1 module enabled
bit 0              TMR0MD: Disable Timer TMR0 bit
                   1 = TMR0 module disabled
                   0 = TMR0 module enabled


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 292
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 19-3:           PMD2: PMD CONTROL REGISTER 2
        U-0          R/W-0/0       R/W-0/0             U-0       U-0         R/W-0/0          R/W-0/0      R/W-0/0
        —            DACMD         ADCMD               —            —        CMP2MD        CMP1MD         ZCDMD(1)
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared         q = Value depends on condition


bit 7              Unimplemented: Read as ‘0’
bit 6              DACMD: Disable DAC bit
                   1 = DAC module disabled
                   0 = DAC module enabled
bit 5              ADCMD: Disable ADCC bit
                   1 = ADCC module disabled
                   0 = ADCC module enabled
bit 4-3            Unimplemented: Read as ‘0’
bit 2              CMP2MD: Disable Comparator CMP2 bit
                   1 = CMP2 module disabled
                   0 = CMP2 module enabled
bit 1              CMP1MD: Disable Comparator CMP1 bit
                   1 = CMP1 module disabled
                   0 = CMP1 module enabled
bit 0              ZCDMD: Disable Zero-Cross Detect module bit(1)
                   1 = ZCD module disabled
                   0 = ZCD module enabled

Note 1:       Subject to ZCD bit in CONFIG2H.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 293
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 19-4:           PMD3: PMD CONTROL REGISTER 3
   R/W-0/0           R/W-0/0     R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0          R/W-0/0      R/W-0/0
  PWM8MD            PWM7MD       PWM6MD           PWM5MD     CCP4MD         CCP3MD        CCP2MD          CCP1MD
bit 7                                                                                                           bit 0


Legend:
R = Readable bit               W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged           x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set               ‘0’ = Bit is cleared         q = Value depends on condition


bit 7              PWM8MD: Disable Pulse-Width Modulator PWM8 bit
                   1 = PWM8 module disabled
                   0 = PWM8 module enabled
bit 6              PWM7MD: Disable Pulse-Width Modulator PWM7 bit
                   1 = PWM7 module disabled
                   0 = PWM7 module enabled
bit 5              PWM6MD: Disable Pulse-Width Modulator PWM6 bit
                   1 = PWM6 module disabled
                   0 = PWM6 module enabled
bit 4              PWM5MD: Disable Pulse-Width Modulator PWM5 bit
                   1 = PWM5 module disabled
                   0 = PWM5 module enabled
bit 3              CCP4MD: Disable Capture/Compare/PWM CCP4 bit
                   1 = CCP4 module disabled
                   0 = CCP4 module enabled
bit 2              CCP3MD: Disable Capture/Compare/PWM CCP3 bit
                   1 = CCP3 module disabled
                   0 = CCP3 module enabled
bit 1              CCP2MD: Disable Capture/Compare/PWM CCP2 bit
                   1 = CCP2 module disabled
                   0 = CCP2 module enabled
bit 0              CCP1MD: Disable Capture/Compare/PWM CCP1 bit
                   1 = CCP1 module disabled
                   0 = CCP1 module enabled


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 294
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 19-5:           PMD4: PMD CONTROL REGISTER 4
   R/W-0/0           R/W-0/0      R/W-0/0             U-0       U-0            U-0           U-0            U-0
  CWG3MD            CWG2MD       CWG1MD               —          —             —                 —           —
bit 7                                                                                                             bit 0


Legend:
R = Readable bit               W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged           x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set               ‘0’ = Bit is cleared         q = Value depends on condition


bit 7              CWG3MD: Disable CWG3 Module bit
                   1 = CWG3 module disabled
                   0 = CWG3 module enabled
bit 6              CWG2MD: Disable CWG2 Module bit
                   1 = CWG2 module disabled
                   0 = CWG2 module enabled
bit 5              CWG1MD: Disable CWG1 Module bit
                   1 = CWG1 module disabled
                   0 = CWG1 module enabled
bit 4-0            Unimplemented: Read as ‘0’


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 295
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 19-6:           PMD5: PMD CONTROL REGISTER 5
        U-0            U-0         R/W-0/0         R/W-0/0        U-0          R/W-0/0         R/W-0/0      R/W-0/0
        —               —           U2MD               U1MD        —           SPI1MD          I2C2MD       I2C1MD
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared          q = Value depends on condition


bit 7-6            Unimplemented: Read as ‘0’
bit 5              U2MD: Disable UART2 bit
                   1 = UART2 module disabled
                   0 = UART2 module enabled
bit 4              U1MD: Disable UART1 bit
                   1 = UART1 module disabled
                   0 = UART1 module enabled
bit 3              Unimplemented: Read as ‘0’
bit 2              SPI1MD: Disable SPI1 Module bit
                   1 = SPI1 module disabled
                   0 = SPI1 module enabled
bit 1              I2C2MD: Disable I2C2 Module bit
                   1 = I2C2 module disabled
                   0 = I2C2 module enabled
bit 0              I2C1MD: Disable I2C1 Module bit
                   1 = I2C1 module disabled
                   0 = I2C1 module enabled


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 296
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 19-7:           PMD6: PMD CONTROL REGISTER 6
        U-0            U-0        R/W-0/0          R/W-0/0      R/W-0/0       R/W-0/0          R/W-0/0      R/W-0/0
        —               —         SMT1MD           CLC4MD      CLC3MD         CLC2MD        CLC1MD          DSMMD
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared          q = Value depends on condition


bit 7-6            Unimplemented: Read as ‘0’
bit 5              SMT1MD: Disable SMT1 Module bit
                   1 = SMT1 module disabled
                   0 = SMT1 module enabled
bit 4              CLC1MD: Disable CLC4 Module bit
                   1 = CLC4 module disabled
                   0 = CLC4 module enabled
bit 3              CLC3MD: Disable CLC3 Module bit
                   1 = CLC3 module disabled
                   0 = CLC3 module enabled
bit 2              CLC2MD: Disable CLC2 Module bit
                   1 = CLC2 module disabled
                   0 = CLC2 module enabled
bit 1              CLC1MD: Disable CLC1 Module bit
                   1 = CLC1 module disabled
                   0 = CLC1 module enabled
bit 0              DSMMD: Disable Data Signal Modulator bit
                   1 = DSM module disabled
                   0 = DSM module enabled


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 297
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 19-8:             PMD7: PMD CONTROL REGISTER 7
        U-0            U-0                U-0            U-0             U-0             U-0             R/W-0/0      R/W-0/0
        —               —                 —              —                —                 —         DMA2MD          DMA1MD
bit 7                                                                                                                       bit 0


Legend:
R = Readable bit                  W = Writable bit                   U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown                 -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared               q = Value depends on condition


bit 7-2            Unimplemented: Read as ‘0’
bit 1              DMA2MD: Disable DMA2 Module bit
                   1 = DMA2 module disabled
                   0 = DMA2 module enabled
bit 0              DMA1MD: Disable DMA1 Module bit
                   1 = DMA1 module disabled
                   0 = DMA1 module enabled


TABLE 19-1:          SUMMARY OF REGISTERS ASSOCIATED WITH PERIPHERAL MODULE DISABLE
                                                                                                                       Register
     Name             Bit 7       Bit 6          Bit 5       Bit 4       Bit 3      Bit 2        Bit 1        Bit 0
                                                                                                                       on Page
PMD0                SYSCMD      FVRMD           HLVDMD    CRCMD        SCANMD     NVMMD         CLKRMD       IOCMD       292
PMD1                NCO1MD      TMR6MD          TMR5MD   TMR4MD        TMR3MD     TMR2MD        TMR1MD      TMR0MD       293
PMD2                   —        DACMD           ADCMD          —          —       CMP2MD        CMP1MD       ZCDMD       294
PMD3                PWM8MD     PWM7MD           PWM6MD   PWM5MD        CCP4MD     CCP3MD        CCP2MD      CCP1MD       295
PMD4                CWG3MD     CWG2MD           CWG1MD         —          —          —            —              —       296
PMD5                   —           —             U2MD      U1MD           —       SPI1MD        I2C2MD       I2C1MD      297
PMD6                   —           —            SMT1MD    CLC4MD       CLC3MD     CLC2MD        CLC1MD       DSMMD       297
PMD7                   —           —              —            —          —          —          DMA2MD      DMA1MD       299
Legend:       — = unimplemented location, read as ‘0’. Shaded cells are not used by peripheral module disable.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 298
