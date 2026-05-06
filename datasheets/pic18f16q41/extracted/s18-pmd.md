18.    PMD - Peripheral Module Disable
18.1   Overview
       This module provides the ability to selectively enable or disable a peripheral. Disabling a peripheral
       places it in its lowest possible Power state. The user can selectively disable unused modules to
       reduce the overall power consumption.


                    Important: All modules are ON by default following any system Reset.


18.2   Disabling a Module
       A peripheral can be disabled by setting the corresponding peripheral disable bit in the PMDx
       register. Disabling a module has the following effects:
       •   The module is held in Reset and does not function.
       •   All the SFRs pertaining to that peripheral become “unimplemented”
            – Writing is disabled
            – Reading returns 0x00
       •   Module outputs are disabled

18.3   Enabling a Module
       Clearing the corresponding module disable bit in the PMDx register, re-enables the module and the
       SFRs will reflect the Power-on Reset values.


                    Important: There will be no reads/writes to the module SFRs for at least two instruction
                    cycles after it has been re-enabled.


18.4   Register Definitions: Peripheral Module Disable


--- p292 ---
18.4.1 PMD0

           Name:       PMD0
           Address:    0x063

           PMD Control Register 0

     Bit        7            6              5              4               3                 2         1               0
             SYSCMD        FVRMD         HLVDMD          CRCMD          SCANMD                      CLKRMD          IOCMD
  Access       R/W          R/W            R/W            R/W             R/W                         R/W             R/W
   Reset        0            0              0              0               0                           0               0

Bit 7 – SYSCMD Disable Peripheral System Clock Network(1)
           Value      Description
           1          System clock network disabled (FOSC)
           0          System clock network enabled

Bit 6 – FVRMD Disable Fixed Voltage Reference
          Disable Fixed Voltage Reference
           Value      Description
           1          FVR module disabled
           0          FVR module enabled

Bit 5 – HLVDMD Disable High/Low-Voltage Detect
           Value      Description
           1          HLVD module disabled
           0          HLVD module enabled

Bit 4 – CRCMD Disable CRC Module
           Value      Description
           1          CRC module disabled
           0          CRC module enabled

Bit 3 – SCANMD Disable NVM Memory Scanner
           Value      Description
           1          NVM memory scanner module disabled
           0          NVM memory scanner module enabled

Bit 1 – CLKRMD Disable Clock Reference
           Value      Description
           1          Clock reference module disabled
           0          Clock reference module enabled

Bit 0 – IOCMD Disable Interrupt-on-Change
           Value      Description
           1          Interrupt-on-change module is disabled
           0          Interrupt-on-change module is enabled

           Note:
           1. Clearing the SYSCMD bit disables the system clock (FOSC) to peripherals, however peripherals
              clocked by FOSC/4 are not affected.


--- p293 ---
18.4.2 PMD1

           Name:       PMD1
           Address:    0x064

           PMD Control Register 1

     Bit        7           6             5                4              3              2           1              0
              C1MD        ZCDMD        SMT1MD           TMR4MD         TMR3MD         TMR2MD      TMR1MD         TMR0MD
  Access       R/W         R/W           R/W              R/W            R/W            R/W         R/W            R/W
   Reset        0           0             0                0              0              0           0              0

Bit 7 – C1MD Disable Comparator 1
           Value      Description
           1          CM1 module disabled
           0          CM1 module enabled

Bit 6 – ZCDMD Disable Zero-Cross Detect(1)
           Value      Description
           1          ZCD module disabled
           0          ZCD module enabled

Bit 5 – SMT1MD Disable SMT1 Module
           Value      Description
           1          SMT1 module disabled
           0          SMT1 module enabled

Bits 0, 1, 2, 3, 4 – TMRnMD Disable Timer TMRn
           Value      Description
           1          TMRn module disabled
           0          TMRn module enabled

           Note:
           1. Subject to the value of ZCD Configuration bit.


--- p294 ---
18.4.3 PMD2

           Name:       PMD2
           Address:    0x065

           PMD Control Register 2

     Bit        7            6              5             4               3              2           1              0
             CCP1MD       CWG1MD         DSM1MD        NCO1MD           ACTMD         DAC1MD       ADCMD          C2MD
  Access       R/W          R/W            R/W           R/W             R/W            R/W         R/W            R/W
   Reset        0            0              0             0               0              0           0              0

Bit 7 – CCP1MD Disable Capture Compare 1
           Value      Description
           1          CCP1 module disabled
           0          CCP1 module enabled

Bit 6 – CWG1MD Disable Complimentary Waveform Generator 1
           Value      Description
           1          CWG1 module disabled
           0          CWG1 module enabled

Bit 5 – DSM1MD Disable Digital Signal Modulator
           Value      Description
           1          DSM module disabled
           0          DSM module enabled

Bit 4 – NCO1MD Disable Numerically Controlled Oscillator 1
           Value      Description
           1          NCO1 module disabled
           0          NCO1 module enabled

Bit 3 – ACTMD Disable Active Clock Tuning
           Value      Description
           1          Active Clock Tuning disabled
           0          Active Clock Tuning enabled

Bit 2 – DAC1MD Disable Digital-to-Analog Converter
           Value      Description
           1          DAC module disabled
           0          DAC module enabled

Bit 1 – ADCMD Disable Analog-to-Digital Converter
           Value      Description
           1          ADC module disabled
           0          ADC module enabled

Bit 0 – C2MD Disable Comparator 2
           Value      Description
           1          CM2 module disabled
           0          CM2 module enabled


--- p295 ---
18.4.4 PMD3

            Name:       PMD3
            Address:    0x066

            PMD Control Register 3

      Bit        7            6              5               4              3             2           1             0
               U2MD         U1MD          SPI2MD          SPI1MD         I2C1MD        PWM3MD      PWM2MD        PWM1MD
  Access        R/W          R/W            R/W             R/W            R/W           R/W         R/W           R/W
   Reset         0            0              0               0              0             0           0             0

Bits 6, 7 – UnMD Disable UART Un
            Value      Description
            1          UARTn module disabled
            0          UARTn module enabled

Bit 5 – SPI2MD Disable Serial Peripheral Interface 2
            Value      Description
            1          SPI2 module disabled
            0          SPI2 module enabled

Bit 4 – SPI1MD Disable Serial Peripheral Interface 1
            Value      Description
            1          SPI1 module disabled
            0          SPI1 module enabled

Bit 3 – I2C1MD Disable I2C
            Value      Description
            1          I2C1 module disabled
            0          I2C1 module enabled

Bit 2 – PWM3MD Disable Pulse-Width Modulator 3
            Value      Description
            1          PWM3 module disabled
            0          PWM3 module enabled

Bit 1 – PWM2MD Disable Pulse-Width Modulator 2
            Value      Description
            1          PWM2 module disabled
            0          PWM2 module enabled

Bit 0 – PWM1MD Disable Pulse-Width Modulator 1
            Value      Description
            1          PWM1 module disabled
            0          PWM1 module enabled


--- p296 ---
18.4.5 PMD4

           Name:       PMD4
           Address:    0x067

           PMD Control Register 4

     Bit       7            6             5                 4              3              2           1              0
            DMA3MD       DMA2MD        DMA1MD            CLC4MD         CLC3MD         CLC2MD      CLC1MD          U3MD
  Access      R/W          R/W           R/W               R/W            R/W            R/W         R/W            R/W
   Reset       0            0             0                 0              0              0           0              0

Bits 5, 6, 7 – DMAnMD Disable DMAn
           Value      Description
           1          DMAn module disabled
           0          DMAn module enabled

Bits 1, 2, 3, 4 – CLCnMD Disable CLCn
           Value      Description
           1          CLCn module disabled
           0          CLCn module enabled

Bit 0 – UnMD Disable UART Un
           Value      Description
           1          UARTn module disabled
           0          UARTn module enabled


--- p297 ---
18.4.6 PMD5

           Name:        PMD5
           Address:     0x068

           PMD Control Register 5

     Bit           7            6             5              4                  3         2           1             0
                                                                                       OPA1MD      DAC2MD        DMA4MD
  Access                                                                                 R/W         R/W           R/W
   Reset                                                                                  0           0             0

Bit 2 – OPA1MD Disable Operational Amplifier
           Value       Description
           1           OPA module disabled
           0           OPA module enabled

Bit 1 – DAC2MD Disable Digital-to-Analog Converter
           Value       Description
           1           DAC module disabled
           0           DAC module enabled

Bit 0 – DMAnMD Disable DMAn
           Value       Description
           1           DMAn module disabled
           0           DMAn module enabled


--- p298 ---
18.5      Register Summary - PMD
Address     Name      Bit Pos.     7           6           5             4         3         2          1           0
 0x00
  ...      Reserved
 0x62
 0x63       PMD0        7:0      SYSCMD      FVRMD      HLVDMD       CRCMD      SCANMD               CLKRMD      IOCMD
 0x64       PMD1        7:0       C1MD       ZCDMD      SMT1MD      TMR4MD      TMR3MD    TMR2MD    TMR1MD      TMR0MD
 0x65       PMD2        7:0      CCP1MD     CWG1MD      DSM1MD      NCO1MD       ACTMD    DAC1MD     ADCMD        C2MD
 0x66       PMD3        7:0       U2MD        U1MD       SPI2MD      SPI1MD      I2C1MD   PWM3MD    PWM2MD      PWM1MD
 0x67       PMD4        7:0      DMA3MD     DMA2MD      DMA1MD      CLC4MD      CLC3MD     CLC2MD    CLC1MD       U3MD
 0x68       PMD5        7:0                                                               OPA1MD    DAC2MD      DMA4MD


--- p299 ---
