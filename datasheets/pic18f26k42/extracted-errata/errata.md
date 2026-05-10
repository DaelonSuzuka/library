                                                                     PIC18(L)F27/47/57K42
                           PIC18(L)F27/47/57K42 Family
                     Silicon Errata and Data Sheet Clarification

The PIC18(L)F27/47/57K42 family devices that you                             For example, to identify the silicon revision level
have received conform functionally to the current                            using MPLAB IDE in conjunction with a hardware
Device Data Sheet (DS40001919G), except for the                              debugger:
anomalies described in this document.                                        1.    Using the appropriate interface, connect the
The silicon issues discussed in the following pages are                            device to the hardware debugger.
for silicon revisions with the Device and Revision IDs                       2.    Open an MPLAB IDE project.
listed in Table 1. The silicon issues are summarized in                      3.    Configure the MPLAB IDE project for the
Table 2.                                                                           appropriate device and hardware debugger.
The errata described in this document will be addressed                      4.    For MPLAB X IDE, select Window > Dashboard
in future revisions of the PIC18(L)F27/47/57K42 silicon.                           and click the Refresh Debug Tool Status icon
  Note:       This document summarizes all silicon                                 (    ).
              errata issues from all revisions of silicon,                   5.    Depending on the development tool used, the
              previous as well as current. Only the                                part number and Device Revision ID value
              issues indicated in the last column of                               appear in the Output window.
              Table 2 apply to the current silicon
                                                                                  Note:   If you are unable to extract the silicon
              revision (A3).
                                                                                          revision level, contact your local Microchip
Data Sheet clarifications and corrections start on page                                   sales office for assistance.
9, following the discussion of silicon issues.
                                                                             The DEVREV/REVID values for the various
The silicon revision level can be identified using the                       PIC18(L)F27/47/57K42 silicon revisions are shown in
current version of MPLAB® IDE and Microchip’s                                Table 1.
programmers, debuggers, and emulation tools, which
are available at the Microchip corporate website
(www.microchip.com).


TABLE 1:            SILICON DEVREV VALUES
                                                                                              Revision ID for Silicon Revision
                Part Number                                  Device ID<13:0>(1), (2)
                                                                                                    A1                    A3
PIC18F27K42                                                          6C40h                         A001                 A003
PIC18F47K42                                                          6BE0h                         A001                 A003
PIC18F57K42                                                          6B80h                         A001                 A003
PIC18LF27K42                                                         6D80h                         A001                 A003
PIC18LF47K42                                                         6D20h                         A001                 A003
PIC18LF57K42                                                        6CC0h                          A001                 A003
Note 1:       The Revision ID is located in addresses 3FFFFCh-3FFFFDh and Device ID is located in addresses
              3FFFFEh-3FFFFFh.
        2:    Refer to the “PIC18(L)F27/47/57K42 Memory Programming Specification” (DS40001886) for detailed
              information on Device and Revision IDs for your specific device.


 2018-2023 Microchip Technology Inc. and its subsidiaries                                                          DS80000773H-page 1
                                                                                       PIC18(L)F27/47/57K42


TABLE 2:            SILICON ISSUE SUMMARY
                                                                                                                             Affected
                                                         Item                                                               Revisions(1)
      Module                       Feature                                         Issue Summary
                                                          No.
                                                                                                                             A1       A3
                        SMBus 3.0                            1.1   SMBus 3.0 logic levels.                                   X        X
                        Minimum VDD                                Device may not work properly at certain voltage
                                                             1.2                                                             X
                        specification (rev A1)                     levels and temperatures in this silicon revision.
Electrical
Specifications          Minimum VDD                                Device may not work properly at certain voltage
                                                             1.3                                                                      X
                        specification (rev A3)                     levels and temperatures in this silicon revision.
                        Fixed Voltage Reference                    FVR output tolerance may be higher than
                                                             1.4                                                             X        X
                        (FVR) accuracy                             specified at temperatures below -20°C.
                        DMA reads from data                        DMA reads from data EEPROM do not
                                                             2.1                                                             X
Direct Memory           EEPROM                                     operate.
Access (DMA)                                                       DMA transfers may not work when CPU is in
                        DMA in Doze mode                     2.2                                                             X
                                                                   Doze mode.
                        ADC Conversion in                          ADC does not complete conversion
                                                             3.1                                                             X
                        FOSC mode                                  successfully in FOSC mode.
Analog-to-Digital
                                                                   The ADC2 does not trigger the second
Converter with          Burst Average mode
                                                             3.2   conversion when operated in non-continuous                X
Computation             Double Sampling
                                                                   double-sampling Burst Average mode.
(ADC2)
                        Double Sample                              An unexpected acquisition time is added
                                                             3.3                                                             X        X
                        Conversions                                between the first and second conversions.
Universal                                                          BRGS Select feature not functional in DALI
                        BRGS Select                          4.1                                                                      X
Asynchronous                                                       mode.
Receiver                Stop bit interrupt flag              4.2   Stop bit interrupt flag functionality not available.      X
Transmitter                                                        The first character after auto-baud may be
(UART)                  Auto-Baud                            4.3                                                             X        X
                                                                   corrupted.
                                                                   Received data are transferred into the
                        I2C Receive Buffer                   5.1                                                             X        X
                                                                   I2CxRXB buffer on an incorrect clock edge.
I2C
                                                                   I2C Start and/or Stop flags maybe set when I2C
                        I2C Start/Stop Flags                 5.2                                                             X        X
                                                                   is enabled.
Nonvolatile
                                                                   The WRERR bit cannot be cleared in hardware
Memory (NVM)            WRERR bit functionality              6.1                                                             X
                                                                   after being set once.
Control
Windowed
                        WWDT operation in                          Window violation occurs when WWDT
Watchdog Timer                                               7.1                                                             X
                        Doze mode                                  operated in Doze mode.
(WWDT)
Power-Saving                                                       Low-Power Sleep mode does not operate at
                Low-Power Sleep mode                         8.1                                                             X
Operation Modes                                                    3.1V < VDD < 3.3V.
Program Flash
                        Endurance of PFM                     9.1   Endurance of PFM is lower than specified.                 X        X
Memory (PFM)
                        MOVFF/MOVSF
Instruction Set                                          10.1 MOVFF/MOVSF may corrupt destination.                           X        X
                        instruction
In-Circuit
                Software breakpoints                         11.1 Software breakpoints are not available.                    X        X
Debugging (ICD)
Central
Processing Unit         FSR Shadow Registers             12.1 FSR Shadow Registers are not writable.                         X        X
(CPU)
Note 1:       Only those issues indicated in the last column apply to the current silicon revision.


 2018-2023 Microchip Technology Inc. and its subsidiaries                                                                DS80000773H-page 2
                                                                               PIC18(L)F27/47/57K42

Silicon Errata Issues
  Note:       This document summarizes all silicon
              errata issues from all revisions of silicon,
              previous as well as current. Only the
              issues indicated by the shaded column in
              the following tables apply to the current
              silicon revision (A3).

1. Module: Electrical Specifications
1.1 SMBus 3.0
     The SMBus 3.0 VIL specification (Parameter                         1.2 Minimum VDD Specification (Silicon Revision
     D305) is temperature and VDD dependent. Refer                          A1)
     to the table below.                                                     VDDMIN for silicon revision A1 has changed for
                                    D305 SMBus 3.0 VIL                       temperatures below +25°C, as shown in the
 Temperature           VDD                                                   excerpt of Table 44-1 below (in bold).
                                       Specification
     -40°C            1.8V                     0.6V                          Work around
     -40°C            5.5V                     0.8V                          None.
      25°C            1.8V                     0.6V                          Affected Silicon Revisions
      25°C            5.5V                     0.8V
                                                                              A1       A3
      85°C            1.8V                     0.6V
                                                                               X
      85°C            5.5V                     0.7V
     125°C            1.8V                     0.5V
     125°C            5.5V                     0.7V

     Work around
     None.
     Affected Silicon Revisions

       A1      A3
        X       X


TABLE 44-1:           SUPPLY VOLTAGE (EXCERPT)
PIC18LF27/47/57K42                                    Standard Operating Conditions (unless otherwise stated)

PIC18F27/47/57K42

 Param.
              Sym.           Characteristic            Min.   Typ.†   Max.     Units                Conditions
  No.
Supply Voltage
D002         VDD                                        2.5     —      3.6         V    FOSC  16 MHz (-40°C to <+25°C)
                                                        1.8     —      3.6         V    FOSC  16 MHz (≥+25°C to +125°C)
                                                        2.5     —      3.6         V    FOSC  16 MHz and FOSC  32 MHz
                                                        2.7     —      3.6         V    FOSC  32 MHz
D002         VDD                                        2.5     —      5.5         V    FOSC  16 MHz (-40°C to <+25°C)
                                                        2.3     —      5.5         V    FOSC  16 MHz (≥+25°C to +125°C)
                                                        2.5     —      5.5         V    FOSC  16 MHz and FOSC  32 MHz
                                                        2.7     —      5.5         V    FOSC  32 MHz


 2018-2023 Microchip Technology Inc. and its subsidiaries                                                  DS80000773H-page 3
                                                                                  PIC18(L)F27/47/57K42

1.3 Minimum VDD Specification (Silicon Revision                               Work around
    A3)                                                                       None.
     VDDMIN for silicon revision A3 devices has
                                                                              Affected Silicon Revisions
     changed for the temperature ranges between
     40°C to +25°C and +25°C to +125°C, as shown                                  A1      A3
     in the excerpt of Table 44-1 below (in bold).
                                                                                          X


                                                                              .
TABLE 44-1:           SUPPLY VOLTAGE (EXCERPT)
PIC18LF27/47/57K42                                     Standard Operating Conditions (unless otherwise stated)

PIC18F27/47/57K42

 Param.
              Sym.           Characteristic             Min.   Typ.†   Max.       Units                Conditions
  No.
Supply Voltage
D002        VDD                                          2.7    —       3.6        V       FOSC  32 MHz (-40°C to <+25°C)
                                                         2.5    —       3.6        V       FOSC  32 MHz (≥+25°C to +125°C)
                                                         2.7    —       3.6        V       FOSC  32 MHz
D002        VDD                                          3.0    —       5.5        V       FOSC  32 MHz (-40°C to <+25°C)
                                                         3.0    —       5.5        V       FOSC  32 MHz (≥+25°C to +125°C)
                                                         3.0    —       5.5        V       FOSC  32 MHz


1.4 Fixed Voltage Reference (FVR) Accuracy
     At temperatures below -20°C, the output voltage
     for the FVR may be greater than the levels
     specified in the data sheet. This will apply to all
     three gain amplifier settings (1X, 2X, 4X). The
     affected parameter numbers found in the data
     sheet are: FVR01 (1X gain setting), FVR02 (2X
     gain setting), and FVR03 (4X gain setting).
     Work around
     At temperatures above -20°C, the stated
     tolerances in the data sheet remain in effect.
     Operate the FVR only at temperatures above
     -20°C.
     Affected Silicon Revisions

       A1      A3
        X       X


 2018-2023 Microchip Technology Inc. and its subsidiaries                                                    DS80000773H-page 4
                                                                   PIC18(L)F27/47/57K42

2. Module: Direct Memory Access (DMA)                        3. Module: Analog-to-Digital Converter with
                                                                        Computation (ADC2)
2.1 DMA Reads from Data EEPROM
     The DMA modules do not operate when                     3.1 ADC Conversion in Fosc Mode
     configured to access the data EEPROM (i.e.,                The ADCON0.GO bit remains set and the
     SMR[1:0] = 1x). The destination gets written to            conversion does not complete successfully
     0x00.                                                      when configured to operate in FOSC mode
                                                                (ADCON0.CS = 0) with FOSC > 40 MHz.
     Work around
     None. NVMCON reads work as described.                      Work around
                                                                Use ADCRC as the ADC            clock   source
     Affected Silicon Revisions
                                                                (ADCON0.CS = 1).
       A1      A3                                               Affected Silicon Revisions
        X
                                                                  A1   A3
2.2 DMA in Doze Mode
                                                                  X
     When the CPU is operated in Doze mode, DMA
     transfers may not work as expected.                     3.2 Burst Average Mode Double Sampling
                                                                When the ADC2 is operated in Burst Average
     Work around
                                                                mode (MD = 0b011 in the ADCON2 register)
     None.                                                      while enabling non-continuous operation and
     Affected Silicon Revisions                                 double-sampling (CONT = 0 in the ADCON0
                                                                register and DSEN = 1 in the ADCON1 register),
       A1      A3                                               the value in the ADCNT register does not
                                                                increment beyond 0b1 toward the value in the
        X
                                                                ADRPT register.
                                                                Work around
                                                                When operating the ADC2 in Burst Average
                                                                mode with double-sampling, enable continuous
                                                                operation of the module (CONT = 1 in the
                                                                ADCON0 register) and set the Stop-On-Interrupt
                                                                bit (SOI in the ADCON3 register). After the
                                                                interrupt occurs, perform appropriate threshold
                                                                calculations in the software and retrigger ADC2
                                                                as necessary.
                                                                Alternatively, if the CPU is in Low-Power Sleep
                                                                mode, the ADC2 in non-continuous Burst
                                                                Average mode can be operated with single ADC
                                                                conversion (DSEN = 0 in the ADCON1 register)
                                                                compromising noise immunity for lower power
                                                                consumption by preventing the device from
                                                                waking up to perform threshold calculations in
                                                                the software.
                                                                Affected Silicon Revisions

                                                                  A1   A3
                                                                  X


 2018-2023 Microchip Technology Inc. and its subsidiaries                                     DS80000773H-page 5
                                                                    PIC18(L)F27/47/57K42

3.3 Double Sample Conversions                                4.2 Stop Bit Interrupt Flag
     When enabling a Double Sample Conversion                     Stop bit interrupt flag functionality is not
     (DSEN = 1), with no Precharge time (ADPRE = 0)               available in the CERIF bit in revision A1.
     and no Acquisition time (ADACQ = 0), the
                                                                  Work around
     maximum number of cycles of acquisition time is
     inserted prior to the second conversion.                     Use Timer2 with HLT and connect the UART RX
                                                                  port to the timer Reset trigger. Set the time-out
     The first conversion will be performed as
                                                                  period to the desired Stop bit time (for DALI
     expected with no Precharge time and no
                                                                  mode, this is equivalent to two Stop bits at 1200
     Acquisition time. It is only between the first and
                                                                  baud = 1.66 ms). When the Stop bit is received,
     second conversions where a maximum number
                                                                  the timer times out notifying end of data.
     of cycles of Acquisition time is performed
     unexpectedly.                                                Affected Silicon Revisions
     Work around                                                   A1     A3
     Method 1: Disable double conversion (DSEN = 0)                 X
     and perform two single conversions back to
     back.                                                   4.3 Auto-Baud
     Method 2: If adding acquisition time is                      When the UART is configured as follows, then
     acceptable, then select no Precharge time,                   the first character received after auto-baud may
     along with the desired Acquisition time.                     be corrupted:

     Affected Silicon Revisions                                   • The UBRG registers are cleared.
                                                                  • The BRGS bit is set (Fast Baud Rate mode).
       A1      A3
                                                                  • The Stop bits are configured for two Stop bits
        X       X                                                   (STP = 0b1x).
                                                                  Work around
4. Module: Universal Asynchronous
           Receiver Transmitter (UART)                       a)   In asynchronous modes other than LIN: The
                                                                  transmitter may delay the first character by at
4.1 Baud Rate Generator Speed Select                              least one character period after sending auto-
     The Baud Rate Generator Speed Select feature                 baud.
     (the BRGS bit in the UxCON0 register) in DALI           b)   In all asynchronous modes including LIN: Clear
     mode is not functional. The Baud Rate                        the BRGS bit to select the normal baud rate
     Generator always operates at normal speed                    mode.
     with 16 baud clocks per bit in DALI mode.
                                                                  Affected Silicon Revisions
     Work around
                                                                   A1     A3
     None.
                                                                    X     X
     Affected Silicon Revisions

       A1      A3
                X


 2018-2023 Microchip Technology Inc. and its subsidiaries                                         DS80000773H-page 6
                                                                    PIC18(L)F27/47/57K42

5. Module: I2C                                               5.2 I2C Start and/or Stop Flags May Be Set When
                                                                 I2C Is Enabled
5.1 I2C Receive Buffer
                                                                  When I2C is enabled, erroneous Start and/or
     When receiving data into the receive buffer                  Stop conditions may be detected. This can
     I2CxRXB, the byte is transferred into the buffer             generate erroneous I2C interrupts if enabled.
     on the 9th rising clock edge rather than the
     expected 8th falling edge. This causes both the              Work around
     Receive Buffer Full (RXBF) status bit and the                Use the following procedure to correctly detect
     Receive Buffer Interrupt Flag (I2CxRXIF) to also             the Start and Stop conditions:
     be set on the 9th rising clock edge. The Data
     Write Interrupt (WRIF) and Address Interrupt            1.   Disable Start and Stop conditions interrupt
     Flag (ADRIF) will still be set on the 8th falling            functions.
     clock edge. If user software is configured to           2.   Enable I2C module.
     interrupt (or poll) when either the WRIF bit or the     3.   Wait 250 ns + 6 instruction cycles (Fosc/4).
     ADRIF bit is set, hardware will read an empty           4.   Clear the Start and Stop conditions interrupt
     receive buffer, set the Receive Read Error                   flags.
     (RXRE) status flag, and a NACK will be issued.          5.   Enable Start and Stop conditions interrupt
     Work around                                                  functions if used.
     Do not use WRIF or ADRIF to determine when
     the receive buffer has received data. Instead,                I2CxPIEbits.SCIE = 0;
     interrupt/poll using the I2CxRXIF interrupt bit or            I2CxPIEbits.PCIE = 0;
     poll the RXBF bit. These bits are correctly set               I2CxCON0bits.EN = 1;
     once the address/data byte has been                           Delay();
     transferred into I2CxRXB.                                     I2CxPIRbits.SCIF = 0;
     Affected Silicon Revisions                                    I2CxPIRbits.PCIF = 0;
                                                                   I2CxPIEbits.SCIE = 1;
       A1      A3                                                  I2CxPIEbits.PCIE = 1;
        X       X

                                                                  Affected Silicon Revisions

                                                                   A1     A3
                                                                    X     X

                                                             6. Module: Nonvolatile Memory (NVM)
                                                                        Control
                                                             6.1 WRERR Bit Functionality
                                                                  When a Reset is issued while an NVM high-
                                                                  voltage operation is in progress, the WRERR bit
                                                                  in the NVMCON1 register is set as expected.
                                                                  After clearing the WRERR bit, if a Reset
                                                                  reoccurs, the WRERR bit is set again regardless
                                                                  of whether an NVM operation is in progress or
                                                                  not.
                                                                  Work around
                                                                  None.
                                                                  Affected Silicon Revisions

                                                                   A1     A3
                                                                    X


 2018-2023 Microchip Technology Inc. and its subsidiaries                                       DS80000773H-page 7
                                                                   PIC18(L)F27/47/57K42

7. Module: Windowed Watchdog Timer                           9. Module: Program Flash Memory (PFM)
           (WWDT)
                                                             9.1 Endurance of PFM
7.1 WWDT Operation in Doze Mode                                  The Flash memory cell endurance specification
     When the CLRWDT instruction is issued in Doze               (Parameter MEM30) is 1K cycles.
     mode, a window violation error occurs in WWDT
                                                                 Work around
     even though the window is open and armed.
                                                                 None.
     Work around
                                                                 Affected Silicon Revisions
     Do not operate the WWDT in Doze mode.
     Affected Silicon Revisions                                   A1     A3
                                                                   X     X
       A1      A3
        X                                                    10. Module: Instruction Set
                                                             10.1 MOVFF/MOVSF Instruction
8. Module: Power-Saving Operation Modes
                                                                 When the BSR points to the last bank of the SFR
8.1 Low-Power Sleep Mode in F Devices                            region (BSR = 0x3F) and the low byte of the
     The F device resets when waking up from Sleep               source or destination address of a MOVFF/
     while in Low-Power mode (VREGPM = 1 in the                  MOVSF instruction equals the low byte of an
     VREGCON register) at 3.1V < VDD < 3.3V.                     indirect addressing operation register address
                                                                 (INDFx, POSTINCx, POSTDECx, PREINCx,
     Work around                                                 PLUSWx), the operation will not be completed
a)   If wake-up from Sleep is needed at 3.1V < VDD               as expected. Either one or more of the
     < 3.3V, operate the F device in Normal Power                destination, FSR value, or location pointed to by
     mode (VREGPM = 0).                                          the FSR will be corrupted, or the move will
b)   If wake-up from Sleep is needed at 3.1V < VDD               simply not occur.
     < 3.3V, enable the Fixed Voltage Reference (EN              Work around
     = 1 in the FVRCON register). This increases the
     current in Sleep mode by typically 7 µA.                    Ensure that the BSR does not point to the last
                                                                 bank of the SFR region (BSR = 0x3F) when the
     Affected Silicon Revisions                                  MOVFF/MOVSF instruction is being executed.
       A1      A3                                                Affected Silicon Revisions
        X                                                         A1     A3
                                                                   X     X

                                                             11. Module: In-Circuit Debugging (ICD)
                                                             11.1 Software Breakpoints
                                                                 When debugging code, software breakpoints
                                                                 will not be available.
                                                                 Work around
                                                                 None.
                                                                 Affected Silicon Revisions

                                                                  A1     A3
                                                                   X     X


 2018-2023 Microchip Technology Inc. and its subsidiaries                                        DS80000773H-page 8
                                                                     PIC18(L)F27/47/57K42

12. Module: Central Processing Unit (CPU)                    Data Sheet Clarifications
12.1 FSR Shadow Registers                                    The following typographic corrections and clarifications
     Writing to the FSR Shadow Registers does not            are to be noted for the latest version of the device data
     result in accurate values being stored in the           sheet (DS40001919G):
     registers. Consequently, reading the FSR                  Note:     Corrections are shown in bold. Where
     Shadow Registers after they have been written                       possible, the original bold text formatting
     will return inaccurate data.                                        has been removed for clarity.
     Work around                                             None.
     Writes to the FSR shadow registers can be
     performed safely using the following steps:
1.   Save regular FSR2 value into RAM.
2.   Write the regular FSR2 with the targeted value
     minus the computed offset (IR[6:0] + 1, see
     below).
3.   Write the shadow FSRxL (data doesn't matter).
     This will clock the shadow FSR with the FSR
     computed offset value.
4.   Decrement FSR2 value by 1 since FSRxH
     increments the address by 1 (IR[6:0]).
5.   Write FSRxH.
6.   Restore the regular FSR2 from the stored RAM
     value.
     The FSR shadow should have the desired value
     and the regular FSR should have the original
     value.
     Affected Silicon Revisions

       A1      A3
        X       X


 2018-2023 Microchip Technology Inc. and its subsidiaries                                         DS80000773H-page 9
                                                             PIC18(L)F27/47/57K42

APPENDIX A:                 DOCUMENT
                            REVISION HISTORY

Rev H Document (10/2023)
Updated Module 1.2 Minimum VDD Specification for
silicon revision A3.

Rev G Document (01/2023)
Updated Module 1.3 Minimum VDD Specification for
silicon revision A3.

Rev F Document (04/2022)
Added Module 3.3 Double Sample Conversions,
12 Central Processing Unit (CPU), and 12.1 FSR
Shadow Registers.

Rev E Document (09/2021)
Added Module 5.2 I2C Start/Stop Flags.

Rev D Document (02/2021)
Added Module 11.1 Software Breakpoints. Minor
corrections.

Rev C Document (06/2019)
Added Modules 1.4 Fixed Voltage Reference (FVR)
Accuracy and 5.1 I2C Receive Buffer.

Rev B Document (03/2019)
Added silicon rev A3. Added Modules 1.3: Min VDD
Specification for LF Devices for A3 Rev, 2.2: DMA in
Doze mode, 4: UART, 5: NVM Control, 6: WWDT, 7:
Power-Saving Operation Modes, 8: PFM, and 9:
Instruction Set.
Updated Module 1.2: Min VDD Specification for A1 Rev.
Updated Table 2.
Data Sheet Clarifications: Removed Module 1.

Rev A Document (01/2018)
Initial release of this document.


 2018-2023 Microchip Technology Inc. and its subsidiaries               DS80000773H-page 10
Note the following details of the code protection feature on Microchip products:
•    Microchip products meet the specifications contained in their particular Microchip Data Sheet.

•    Microchip believes that its family of products is secure when used in the intended manner, within operating specifications, and
     under normal conditions.

•    Microchip values and aggressively protects its intellectual property rights. Attempts to breach the code protection features of
     Microchip product is strictly prohibited and may violate the Digital Millennium Copyright Act.

•    Neither Microchip nor any other semiconductor manufacturer can guarantee the security of its code. Code protection does not
     mean that we are guaranteeing the product is "unbreakable" Code protection is constantly evolving. Microchip is committed to
     continuously improving the code protection features of our products.

This publication and the information herein may be used only            Trademarks
with Microchip products, including to design, test, and integrate       The Microchip name and logo, the Microchip logo, Adaptec, AVR, AVR
Microchip products with your application. Use of this informa-          logo, AVR Freaks, BesTime, BitCloud, CryptoMemory, CryptoRF,
tion in any other manner violates these terms. Information              dsPIC, flexPWR, HELDO, IGLOO, JukeBlox, KeeLoq, Kleer,
regarding device applications is provided only for your conve-          LANCheck, LinkMD, maXStylus, maXTouch, MediaLB, megaAVR,
nience and may be superseded by updates. It is your responsi-           Microsemi, Microsemi logo, MOST, MOST logo, MPLAB, OptoLyzer,
                                                                        PIC, picoPower, PICSTART, PIC32 logo, PolarFire, Prochip Designer,
bility to ensure that your application meets with your
                                                                        QTouch, SAM-BA, SenGenuity, SpyNIC, SST, SST Logo, SuperFlash,
specifications. Contact your local Microchip sales office for           Symmetricom, SyncServer, Tachyon, TimeSource, tinyAVR, UNI/O,
additional support or, obtain additional support at https://            Vectron, and XMEGA are registered trademarks of Microchip
www.microchip.com/en-us/support/design-help/client-support-             Technology Incorporated in the U.S.A. and other countries.
services.
                                                                        AgileSwitch, ClockWorks, The Embedded Control Solutions Company,
THIS INFORMATION IS PROVIDED BY MICROCHIP "AS IS".                      EtherSynch, Flashtec, Hyper Speed Control, HyperLight Load, Libero,
MICROCHIP MAKES NO REPRESENTATIONS OR WAR-                              motorBench, mTouch, Powermite 3, Precision Edge, ProASIC,
RANTIES OF ANY KIND WHETHER EXPRESS OR IMPLIED,                         ProASIC Plus, ProASIC Plus logo, Quiet-Wire, SmartFusion,
                                                                        SyncWorld, TimeCesium, TimeHub, TimePictra, TimeProvider, and ZL
WRITTEN OR ORAL, STATUTORY OR OTHERWISE,
                                                                        are registered trademarks of Microchip Technology Incorporated in the
RELATED TO THE INFORMATION INCLUDING BUT NOT                            U.S.A.
LIMITED TO ANY IMPLIED WARRANTIES OF NON-
INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A                        Adjacent Key Suppression, AKS, Analog-for-the-Digital Age, Any
PARTICULAR PURPOSE, OR WARRANTIES RELATED TO                            Capacitor, AnyIn, AnyOut, Augmented Switching, BlueSky, BodyCom,
ITS CONDITION, QUALITY, OR PERFORMANCE.                                 Clockstudio, CodeGuard, CryptoAuthentication, CryptoAutomotive,
                                                                        CryptoCompanion, CryptoController, dsPICDEM, dsPICDEM.net,
IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDI-                      Dynamic Average Matching, DAM, ECAN, Espresso T1S,
RECT, SPECIAL, PUNITIVE, INCIDENTAL, OR CONSE-                          EtherGREEN, EyeOpen, GridTime, IdealBridge, IGaT, In-Circuit Serial
                                                                        Programming, ICSP, INICnet, Intelligent Paralleling, IntelliMOS, Inter-
QUENTIAL LOSS, DAMAGE, COST, OR EXPENSE OF ANY
                                                                        Chip Connectivity, JitterBlocker, Knob-on-Display, MarginLink,
KIND WHATSOEVER RELATED TO THE INFORMATION OR                           maxCrypto, maxView, memBrain, Mindi, MiWi, MPASM, MPF, MPLAB
ITS USE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS                          Certified logo, MPLIB, MPLINK, mSiC, MultiTRAK, NetDetach,
BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES                          Omniscient Code Generation, PICDEM, PICDEM.net, PICkit, PICtail,
ARE FORESEEABLE. TO THE FULLEST EXTENT                                  Power MOS IV, Power MOS 7, PowerSmart, PureSilicon, QMatrix,
ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON                          REAL ICE, Ripple Blocker, RTAX, RTG4, SAM-ICE, Serial
ALL CLAIMS IN ANY WAY RELATED TO THE INFORMATION                        Quad I/O, simpleMAP, SimpliPHY, SmartBuffer, SmartHLS, SMART-
                                                                        I.S., storClad, SQI, SuperSwitcher, SuperSwitcher II, Switchtec,
OR ITS USE WILL NOT EXCEED THE AMOUNT OF FEES, IF
                                                                        SynchroPHY, Total Endurance, Trusted Time, TSHARC, Turing,
ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP
                                                                        USBCheck, VariSense, VectorBlox, VeriPHY, ViewSpan, WiperLock,
FOR THE INFORMATION.                                                    XpressConnect, and ZENA are trademarks of Microchip Technology
                                                                        Incorporated in the U.S.A. and other countries.
Use of Microchip devices in life support and/or safety applica-
tions is entirely at the buyer's risk, and the buyer agrees to          SQTP is a service mark of Microchip Technology Incorporated in the
defend, indemnify and hold harmless Microchip from any and              U.S.A.
all damages, claims, suits, or expenses resulting from such
use. No licenses are conveyed, implicitly or otherwise, under           The Adaptec logo, Frequency on Demand, Silicon Storage
any Microchip intellectual property rights unless otherwise             Technology, and Symmcom are registered trademarks of Microchip
                                                                        Technology Inc. in other countries.
stated.
                                                                        GestIC is a registered trademark of Microchip Technology Germany II
                                                                        GmbH & Co. KG, a subsidiary of Microchip Technology Inc., in other
                                                                        countries.

                                                                        All other trademarks mentioned herein are property of their respective
                                                                        companies.

                                                                        All Rights Reserved.


                                                                        ISBN: 978-1-6683-3160-6
For information regarding Microchip’s Quality Management Systems,
please visit www.microchip.com/quality.


 2018-2023 Microchip Technology Inc. and its subsidiaries                                                            DS80000773H-page 11
                            Worldwide Sales and Service
AMERICAS                    ASIA/PACIFIC            ASIA/PACIFIC                        EUROPE
Corporate Office            Australia - Sydney      India - Bangalore                   Austria - Wels
2355 West Chandler Blvd.    Tel: 61-2-9868-6733     Tel: 91-80-3090-4444                Tel: 43-7242-2244-39
Chandler, AZ 85224-6199     China - Beijing         India - New Delhi                   Fax: 43-7242-2244-393
Tel: 480-792-7200           Tel: 86-10-8569-7000    Tel: 91-11-4160-8631                Denmark - Copenhagen
Fax: 480-792-7277                                                                       Tel: 45-4485-5910
                            China - Chengdu         India - Pune
Technical Support:                                                                      Fax: 45-4485-2829
                            Tel: 86-28-8665-5511    Tel: 91-20-4121-0141
http://www.microchip.com/
                            China - Chongqing       Japan - Osaka                       Finland - Espoo
support
                            Tel: 86-23-8980-9588    Tel: 81-6-6152-7160                 Tel: 358-9-4520-820
Web Address:
www.microchip.com           China - Dongguan        Japan - Tokyo                       France - Paris
                            Tel: 86-769-8702-9880   Tel: 81-3-6880- 3770                Tel: 33-1-69-53-63-20
Atlanta                                                                                 Fax: 33-1-69-30-90-79
Duluth, GA                  China - Guangzhou       Korea - Daegu
Tel: 678-957-9614           Tel: 86-20-8755-8029    Tel: 82-53-744-4301                 Germany - Garching
                                                                                        Tel: 49-8931-9700
Fax: 678-957-1455           China - Hangzhou        Korea - Seoul
Austin, TX                  Tel: 86-571-8792-8115   Tel: 82-2-554-7200                  Germany - Haan
Tel: 512-257-3370                                                                       Tel: 49-2129-3766400
                            China - Hong Kong SAR   Malaysia - Kuala Lumpur
                            Tel: 852-2943-5100      Tel: 60-3-7651-7906                 Germany - Heilbronn
Boston
                                                                                        Tel: 49-7131-72400
Westborough, MA             China - Nanjing         Malaysia - Penang
Tel: 774-760-0087           Tel: 86-25-8473-2460    Tel: 60-4-227-8870                  Germany - Karlsruhe
Fax: 774-760-0088                                                                       Tel: 49-721-625370
                            China - Qingdao         Philippines - Manila
Chicago                     Tel: 86-532-8502-7355   Tel: 63-2-634-9065                  Germany - Munich
Itasca, IL                                                                              Tel: 49-89-627-144-0
                            China - Shanghai        Singapore
Tel: 630-285-0071                                                                       Fax: 49-89-627-144-44
                            Tel: 86-21-3326-8000    Tel: 65-6334-8870
Fax: 630-285-0075                                                                       Germany - Rosenheim
                            China - Shenyang        Taiwan - Hsin Chu
Dallas                                                                                  Tel: 49-8031-354-560
                            Tel: 86-24-2334-2829    Tel: 886-3-577-8366
Addison, TX                                                                             Israel - Ra’anana
                            China - Shenzhen        Taiwan - Kaohsiung
Tel: 972-818-7423           Tel: 86-755-8864-2200   Tel: 886-7-213-7830                 Tel: 972-9-744-7705
Fax: 972-818-2924                                                                       Italy - Milan
                            China - Suzhou          Taiwan - Taipei
Detroit                                                                                 Tel: 39-0331-742611
                            Tel: 86-186-6233-1526   Tel: 886-2-2508-8600
Novi, MI                                                                                Fax: 39-0331-466781
Tel: 248-848-4000           China - Wuhan           Thailand - Bangkok
                            Tel: 86-27-5980-5300    Tel: 66-2-694-1351                  Italy - Padova
Houston, TX                                                                             Tel: 39-049-7625286
Tel: 281-894-5983           China - Xian            Vietnam - Ho Chi Minh
                            Tel: 86-29-8833-7252    Tel: 84-28-5448-2100                Netherlands - Drunen
Indianapolis                                                                            Tel: 31-416-690399
Noblesville, IN             China - Xiamen                                              Fax: 31-416-690340
                            Tel: 86-592-2388138
Tel: 317-773-8323                                                                       Norway - Trondheim
Fax: 317-773-5453           China - Zhuhai                                              Tel: 47-7288-4388
Tel: 317-536-2380           Tel: 86-756-3210040
                                                                                        Poland - Warsaw
Los Angeles                                                                             Tel: 48-22-3325737
Mission Viejo, CA
                                                                                        Romania - Bucharest
Tel: 949-462-9523                                                                       Tel: 40-21-407-87-50
Fax: 949-462-9608
Tel: 951-273-7800                                                                       Spain - Madrid
                                                                                        Tel: 34-91-708-08-90
Raleigh, NC                                                                             Fax: 34-91-708-08-91
Tel: 919-844-7510
                                                                                        Sweden - Gothenberg
New York, NY                                                                            Tel: 46-31-704-60-40
Tel: 631-435-6000
                                                                                        Sweden - Stockholm
San Jose, CA                                                                            Tel: 46-8-5090-4654
Tel: 408-735-9110
Tel: 408-436-4270                                                                       UK - Wokingham
                                                                                        Tel: 44-118-921-5800
Canada - Toronto                                                                        Fax: 44-118-921-5820
Tel: 905-695-1980
Fax: 905-695-2078


DS80000773H-page 12                                             2018-2023 Microchip Technology Inc. and its subsidiaries
                                                                                                               09/14/21
