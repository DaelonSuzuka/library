PIC18F06/16Q41 Silicon Errata and Data Sheet
Clarifications


Introduction
The PIC18F06/16Q41 devices you have received conform functionally to the current device data sheet
(DS40002214G), except for the anomalies described in this document.
The silicon issues discussed in the following pages are for silicon revisions with the Device and Revision IDs
listed in the table below.
The errata described in this document will be addressed in future revisions of the PIC18F06/16Q41 silicon.
Note: This document summarizes all silicon errata issues from all revisions of silicon, previous as well as
current.

Table 1. Silicon Device Identification
                                                                                              Revision ID
          Part Number                     Device ID
                                                                    A4                 A5                    A6           B1
          PIC18F06Q41                      0x7580                0xA004              0xA005                 0xA006      0xA041
          PIC18F16Q41                      0x7560                0xA004              0xA005                 0xA006      0xA041


       Important: Refer to the Device/Revision ID section in the current “PIC18-Q41 Family
       Programming Specification” (DS40002143) for more detailed information on Device
       Identification and Revision IDs for a specific device.


                                                                   Errata                                            DS80000901G - 1


Table 2. Silicon Issue Summary
                                                                                                                           Affected Revisions
         Module                     Feature            Item No.                     Issue Summary
                                                                                                                           A4   A5   A6    B1
     Analog-to-Digital               ADCC               1.1.1     ADC cannot operate in certain low-power conditions        X
      Converter with                                    1.1.2                 Double Sample Conversions                     X    X   X
       Computation
                                    XT mode             1.2.1      Maximum clock frequency limited to 2 MHz for XT          X
                                                                                      mode
                             Fail-Safe Clock Monitor    1.2.2     Enabling the FOSC Fail-Safe Clock Monitor alongside       X
        Oscillator                                                 the Primary or Secondary Oscillator Clock Monitor
                                                                                 causes issues in Sleep
                                    EC mode             1.2.3     Maximum clock frequency for EC mode is 32 MHz for         X
                                                                                     VDD < 2.0V
            I2C                        I2C              1.3.1     I2CxADR0/1/2/3 registers have incorrect Reset value       X
                                                        1.3.2       I2C Start and/or Stop Flags may be set when I2C is      X    X
                                                                                        enabled
                                                        1.3.3           MDR bit is not cleared after bus time-out           X    X   X     X
                                                        1.3.4      Bus time-out not detected properly when External         X    X   X     X
                                                                                 Host Clock stretches
                                                        1.3.5          Clock Stretch Disable not working properly           X    X   X     X
                                                        1.3.6             Bus time-out causes false Start/Stop              X    X   X     X
                                                        1.3.7           CSTR bit is not cleared after bus time-out          X    X   X     X
                                Multi-Host Mode         1.3.8     Operating in Multi-Host Mode will cause bus failures      X    X   X     X
  Operational Amplifier               OPA               1.4.1       Charge Pump On Control (CPON) bit is reserved           X
                                                        1.4.2     Internal resistor ladder does not disconnect in Unity     X
                                                                                        Gain mode
 Universal Asynchronous              UART               1.5.1     UART TXDE signal may go low before the STOP bit has       X    X   X
  Receiver Transmitter                                                         been entirely transmitted
                                                        1.5.2       Asynchronous 9-bit UART Address mode address            X    X   X
                                                                                      mismatch
   Signal Measurement                 SMT               1.6.1                           Reset Bit                           X    X   X
          TImer
        PIC18 CPU            FSR Shadow Registers       1.7.1            FSR Shadow Registers are not writable              X    X   X

          ICSP™                  Low-Voltage            1.8.1     Low-Voltage Programming is not possible when VDD is       X    X   X
                              Programming (LVP)                            below BORV while BOR is enabled
      Instruction Set          PUSHL Instruction        1.9.1          The PUSHL instruction incorrectly executes           X    X   X     X
Note: Only those issues indicated in the last column apply to the current silicon revision.


                                                                    Errata                                                   DS80000901G - 2


1.      Silicon Errata Issues

                    This document summarizes all silicon errata issues from all revisions of silicon,
                    previous and current. Only the issues indicated by the bold font in the following
                    tables apply to the current silicon revision.


1.1     Module: Analog-to-Digital Converter with Computation (ADCC)
1.1.1   ADC Cannot Operate in Certain Low-Power Conditions
        The ADC will not function when all of the following conditions exist: When the MCU system clock is
        sourced from LFINTOSC or SOSC and when both the BOR and FVR features are disabled.
        Work around
        •   Method 1: Use a system clock other than LFINTOSC or SOSC.
        •   Method 2: Enable the BOR feature.
        •   Method 3: Enable the FVR feature.

        Affected Silicon Revisions
                    A4                         A5                             A6                B1
                    X


1.1.2   Double Sample Conversions
        When enabling a Double Sample Conversion (DSEN = 1) with no precharge time (ADPRE = 0) and no
        Acquisition time (ADACQ = 0), the maximum number of cycles of acquisition time is inserted prior
        to the second conversion. The first conversion will be performed as expected with no precharge
        time and no Acquisition time. It is only between the first and second conversions where a maximum
        number of cycles of Acquisition time is performed unexpectedly.
        Work around
        Method 1:
        Disable Double Sample Conversion (DSEN = 0) and perform two single conversions back to back.
        Method 2:
        If adding acquisition time is acceptable, then select no precharge time along with the desired
        Acquisition time.

        Affected Silicon Revisions
                    A4                         A5                             A6                B1
                    X                           X                             X


1.2     Module: Oscillator (OSC)
1.2.1   Maximum Clock Frequency Limited to 2 MHz for XT Mode
        The maximum clock frequency for the intermediate gain setting that supports quartz crystal and
        ceramic resonator operation (XT mode) is being reduced from 4 MHz to 2 MHz.
        Work around
        For crystal or resonator frequencies above 2 MHz, use HS mode.


                                                           Errata                                    DS80000901G - 3

        Affected Silicon Revisions
                   A4                          A5                             A6                 B1
                    X


1.2.2   Enabling the FOSC Fail-Safe Clock Monitor Alongside the Primary or Secondary Oscillator
        Clock Monitor Causes Issues with Sleep
        When the FOSC Fail-Safe Clock Monitor is enabled (FCMEN Configuration bit = 1) and either the
        Primary or Secondary Fail-Safe Clock Monitor is also enabled (FCMENS and/or FCMENP = 1), putting
        the device to Sleep will cause a Fail-Safe condition to trigger. This has the effect of erroneously
        triggering Fail-Safe interrupts when there has not been a clock interruption. This can also cause the
        Watchdog Timer to not properly wake up the part from Sleep.
        Work around
        If proper functionality in Sleep is required, do not enable the Primary or Secondary Fail-Safe Clock
        Monitor while the FOSC Fail-Safe Clock Monitor is enabled. If Primary or Secondary Clock Monitoring
        in Sleep is desired, disable the FOSC Fail-Safe Clock Monitor before the device goes to Sleep.

        Affected Silicon Revisions
                   A4                          A5                             A6                 B1
                    X


1.2.3   Maximum Clock Frequency for EC Mode Is 32 MHz for VDD < 2.0V
        When configured in External Clock High-Power (ECH) mode and operating at VDD < 2.0V, the
        maximum input clock frequency is 32 MHz.
        Work around
        To obtain a system clock frequency of 64 MHz in ECH mode at VDD < 2.0V, use a 16 MHz external
        clock in conjunction with the 4x Phase-Locked Loop (PLL) circuit (i.e., either RSTOSC Configuration
        bits = 0b010 or OSCCON1bits.NOSC = 0b010).

        Affected Silicon Revisions
                   A4                          A5                             A6                 B1
                    X


1.3     Module: Inter-Integrated Circuit (I2C)
1.3.1   The I2CxADR0/1/2/3 Registers Have Incorrect Reset Value
        The I2CxADR0/2 registers reset to 0xFF when the I2CxMD is enabled instead of 0x00. The
        I2CxADR1/3 registers reset to 0xFE when the I2CxMD is enabled instead of 0x00.
        Work around
        None.

        Affected Silicon Revisions
                   A4                          A5                             A6                 B1
                    X


1.3.2   The I2C Start and/or Stop Flags May Be Set When I2C Is Enabled
        When I2C is enabled, erroneous Start and/or Stop conditions may be detected. This can generate
        erroneous I2C interrupts if enabled.
        Work around
        Use the following procedure to correctly detect the Start and Stop conditions:


                                                           Errata                                     DS80000901G - 4

        1. Disable the Start and Stop conditions interrupt functions.
        2. Enable the I2C module.
        3. Wait 250 ns + six instruction cycles (FOSC/4).
        4. Clear the Start and Stop conditions interrupt flags.
        5. Enable the Start and Stop conditions interrupt functions if used.

         I2CxPIEbits.SCIE = 0;           // Disable Start condition interrupt
         I2CxPIEbits.PCIE = 0;           // Disable Stop condition interrupt
         I2CxCON0bits.EN = 1;            // Enable I2C
         Delay();                        // Wait for 250 ns + 6 instruction cycles (FOSC/4)
         I2CxPIRbits.SCIF = 0;           // Clear the Start condition interrupt flags
         I2CxPIRbits.PCIF = 0;           // Clear the Stop condition interrupt flags
         I2CxPIEbits.SCIE = 1;           // Enable Start condition interrupt if used
         I2CxPIEbits.PCIE = 1;           // Enable Stop condition interrupt if used

        Affected Silicon Revisions
                    A4                          A5                             A6                B1
                    X                            X


1.3.3   MDR Bit Is Not Cleared after Bus Time-Out
        In the Host mode of the I2C module, when a bus time-out occurs during clock stretching and TOREC
        = 1, the MDR bit will not be cleared and a Stop will not be transmitted on the bus.
        Work around
        Force a Stop on the bus by setting the P bit upon bus time-out in Host mode. Forcing a Stop on the
        bus clears the MDR bit.

        Affected Silicon Revisions
                    A4                          A5                             A6                B1
                    X                            X                             X                  X


1.3.4   Bus Time-Out Not Detected Properly When External Host Clock Stretches
        When the module is operating in Client mode and an external Host device is clock stretching after
        the 8th SCL clock and a bus time-out occurs, the bus time-out is not detected properly. When the
        external Host times out before the Client and releases SCL to generate a Stop condition, the module
        continues to stretch SDA as if to generate an ACK and hangs the bus, and a Stop is never seen on
        the bus.
        Work around
        Reset the module by toggling the EN bit.

        Affected Silicon Revisions
                    A4                          A5                             A6                B1
                    X                            X                             X                  X


1.3.5   Clock Stretch Disable Not Working Properly
        When the CSD bit is set between a Start condition and the 8th falling SCL edge, the I2C module
        enters a state where the module clock stretches indefinitely after the next Start until a bus time-out
        occurs.
        Work around
        Force a reset of the module by toggling the EN bit.


                                                            Errata                                    DS80000901G - 5

        Affected Silicon Revisions
                    A4                         A5                             A6                 B1
                    X                           X                             X                  X


1.3.6   Bus Time-Out Causes False Start/Stop
        When the module is operating in Client mode and an external Host device is clock stretching, and
        a bus time-out occurs in the Client, the Client releases SDA and goes into the idle state. After the
        external Host generates a Stop condition on the bus by releasing SCL, the module can erroneously
        drive a low pulse on the SDA line, which acts as a false Start and Stop on the bus.
        Work around
        None.

        Affected Silicon Revisions
                    A4                         A5                             A6                 B1
                    X                           X                             X                  X


1.3.7   CSTR Bit Is Not Cleared after Bus Time-Out
        When the module is operating in Client mode and TOREC = 1, and a bus time-out occurs during
        clock stretching, the CSTR bit will not be cleared, and the module continues to clock stretch and
        hang the bus.
        Work around
        Reset the I2C module by toggling the EN bit.

        Affected Silicon Revisions
                    A4                         A5                             A6                 B1
                    X                           X                             X                  X


1.3.8   Operating in Multi-Host Mode Will Cause Bus Failures
        If operating in Multi-Host mode and a second host drives SDA low at the same time the Start bit is
        generated, the module will fail to go into Host mode but will continue to send an address and data
        as if it won arbitration. I2CCNT fails to decrement, and the module will remain in this state until a
        bus time-out occurs or the device is reset.
        Work around
        None.

        Affected Silicon Revisions
                    A4                         A5                             A6                 B1
                    X                           X                             X                  X


1.4     Module: Operational Amplifier
1.4.1   The Charge Pump On Control (CPON) Bit Is Reserved
        When not operating the OPA near the rails, the Charge Pump On Control (CPON) bit can be used
        to disable the charge pump in order to save on current consumption. This feature is currently not
        available, and the charge pump is always enabled whenever the OPA module is in operation.
        Work around
        None.


                                                           Errata                                     DS80000901G - 6

        Affected Silicon Revisions
                           A4                              A5                                   A6                  B1
                           X


1.4.2   Internal Resistor Ladder Does Not Disconnect in Unity Gain Mode
        When using the OPA module in a unity gain configuration, the internal resistor ladder will not
        automatically disconnect from the operational amplifier, which may adversely affect the gain of the
        circuit. This applies when the peripheral has been configured to operate in Unity Gain mode in
        software by setting the UG bit, or in hardware using the hardware controlled override feature.
        Work around
        Disconnect the internal resistor ladder from the operational amplifier by writing to the Inverting
        Input Channel Selection (NCH) bits. All signals can be disconnected from the operational amplifier by
        writing 0b000 to the NCH bits.

        Affected Silicon Revisions
                           A4                              A5                                   A6                  B1
                           X


1.5     Module: Universal Asynchronous Receiver Transmitter (UART)
1.5.1   UART TXDE Signal May Go Low Before the STOP Bit Has Been Entirely Transmitted
        The UART Transmit Drive Enable (TXDE) signal could potentially transition into a low state before the
        UART STOP bit has been entirely transmitted due to the effects of parasitic capacitance on the TX
        line. In some applications, this could result in communication being prematurely terminated due to
        the TXDE signal going low before the STOP bit has had enough time to settle.
        Work around
        To ensure that the STOP bit settles into its final logic state before the TXDE signal transitions low,
        a biasing circuit can be implemented. A biasing circuit allows the TX line to either be driven high or
        low, rather than being left in a floating tri-state mode where prolonged rise or fall times could lead
        to communication being disrupted. This bias circuit should only be implemented on one end of the
        serial bus, and a termination resistor should be used on the other end. The figure below shows an
        example of a bias circuit that can be used to achieve this.
        Please note that the resistor values used in this circuit are recommendations and that the actual
        resistor values required may vary based on the application.
                                                           VCC
          MCU Controller              RS485 Interface IC                 Device 1              Device 3
                                                                 562 W
                           RX           R
                                                    A
                                        RE
                      TXDE                                      133 W                                     120 W
                                        DE
                                                    B
                           TX
                                        D
                                                                562 W
                                                                                    Device 2
                                GND
                                                           GND


        Affected Silicon Revisions
                           A4                              A5                                   A6                  B1
                           X                               X                                     X


                                                                         Errata                                          DS80000901G - 7

1.5.2   Asynchronous 9-bit UART Address Mode Address Mismatch
        In Asynchronous 9-bit UART Address mode, there is the possibility that a false address mismatch
        may occur even when the address of both devices match, or that a false address match may occur
        when there is an address mismatch between the devices.
        Work around
        None. Do not use the UART modules in Asynchronous 9-bit Address Mode.

        Affected Silicon Revisions
                    A4                         A5                             A6                B1
                    X                           X                             X


1.6     Module: Signal Measurement Timer (SMT)
1.6.1   Reset Bit
        If the SMT clock prescaler is set to any value other than '00', setting the RST bit will cause the
        module to stop working. The RST bit will remain at the value '1', the counter will not increment,
        and no interrupts will be generated. The problem is cleared by turning the module off and on or by
        performing a device reset.
        Work around
        Method 1:
        Do not set the RST bit; manual reset is usually not required for typical operation because the
        measurement logic will reset the counter automatically.
        Method 2:
        Write zero to the counter manually. Either disable the module or the clock before using this method.
        Method 3:
        Use 1:1 prescaler (PS = 00).
        Method 4:
        Use the CLKREF subsystem to provide a prescaled clock and set PS = 00.

        Affected Silicon Revisions
                    A4                         A5                             A6                B1
                    X                           X                             X


1.7     Module: PIC18 Core
1.7.1   FSR Shadow Registers Are Not Writable
        Writing to the FSR Shadow Registers does not result in accurate values being stored in the registers.
        Consequently, reading the FSR Shadow Registers after they have been written will return inaccurate
        data.
        Work around
        Writes to the FSR shadow registers can be performed safely using the following steps:
        1. Save regular FSR2 value into RAM.
        2. Write the regular FSR2 with the targeted value minus the computed offset (IR[6:0] + 1, see
           below).
        3. Write the shadow FSRxL (data doesn't matter); this will clock the shadow FSR with the FSR
           computed offset value.


                                                           Errata                                    DS80000901G - 8

        4. Decrement FSR2 value by 1 since FSRxH increments the address by 1 (IR[6:0]).
        5. Write FSRxH.
        6. Restore the regular FSR2 from the stored RAM value.
        The FSR shadow should have the value desired and the regular FSR should have the original value.

        Affected Silicon Revisions
                    A4                        A5                             A6                B1
                    X                          X                             X


1.8     Module: Low-Voltage In-Circuit Serial Programming™ (LVP)
1.8.1   Low-Voltage Programming Not Possible
        Low-Voltage Programming is not possible when VDD is below the selected BORV voltage level while
        BOR is enabled.

        Work around
        Method 1:
        Disable BOR to use Low-Voltage Programming.
        Method 2:
        Raise VDD above the selected BORV level while using Low-Voltage Programming.

        Affected Silicon Revisions
                    A4                        A5                             A6                B1
                    X                          X                             X


1.9     Module: Instruction Set
1.9.1   The PUSHL Instruction Incorrectly Executes
        The PUSHL instruction of the PIC18 Extended Instruction Set incorrectly executes when FSR2 is
        loaded with certain values.
        Work around
        Do not use PUSHL when FSR2 is loaded with any of the following values:
        •   0xDB
        •   0xDC
        •   0xDE
        •   0xE3
        •   0xE4
        •   0xE6
        •   0xEB
        •   0xEC
        •   0xEE

        Affected Silicon Revisions
                    A4                        A5                             A6                B1
                    X                          X                             X                 X


                                                          Errata                                    DS80000901G - 9


2.          Data Sheet Clarifications
            The following typographic corrections and clarifications are to be noted for the latest version of the
            device data sheet (DS40002214G):
            Note:
            Corrections are shown in bold. Where possible, the original bold text formatting has been removed
            for clarity.

2.1         Interrupt Vector Priority Table
            Table 11-2 incorrectly states the vector numbers for CWG1, NCO1, DMA2SCNT, DMA2DCNT,
            DMA2OR, and DMA2A. The corrected values are shown below with changes highlighted in bold:

     Table 2-1. Interrupt Vector Priority Table
                                                                   Vector                              Interrupt
         Vector                       Interrupt                   Number                                source
        Number                         source
                                                                   (cont.)                              (cont.)
          0x0                    Software Interrupt                 0x2D                             CLC2
          0x1             HLVD (High/Low-Voltage Detect)            0x2E                           PWM2PR
          0x2                   OSF (Oscillator Fail)               0x2F                            PWM2
          0x3                  CSW (Clock Switching)                0x30                              INT1
          0x4                            NVM                        0x31                                -
          0x5              CLC1 (Configurable Logic Cell)           0x32           CWG1 (Complementary Waveform Generator)
          0x6             CRC (Cyclic Redundancy Check)             0x33             NCO1 (Numerically Controlled Oscillator)
          0x7                IOC (Interrupt-On-Change)              0x34                         DMA2SCNT
          0x8                            INT0                       0x35                         DMA2DCNT
          0x9                ZCD (Zero-Cross Detection)             0x36                           DMA2OR
          0xA             AD (ADC Conversion Complete)              0x37                            DMA2A
          0xB                 ACT (Active Clock Tuning)             0x38                            I2C1RX
          0xC                    CM1 (Comparator)                   0x39                            I2C1TX
          0xD            SMT1 (Signal Measurement Timer)            0x3A                              I2C1
          0xE                              -                        0x3B                             I2C1E
          0xF                         SMT1PWA                       0x3C                                -
         0x10                            ADT                        0x3D                             CLC3
      0x11 - 0x13                          -                        0x3E                           PWM3PR
         0x14            DMA1SCNT (Direct Memory Access)            0x3F                            PWM3
         0x15                        DMA1DCNT                       0x40                             U2RX
         0x16                         DMA1OR                        0x41                             U2TX
         0x17                          DMA1A                        0x42                               U2E
         0x18            SPI1RX (Serial Peripheral Interface)       0x43                               U2
         0x19                           SPI1TX                      0x44                                -
         0x1A                            SPI1                       0x45                             CLC4
         0x1B                           TMR2                        0x46                                -
         0x1C                           TMR1                        0x47                             SCAN
         0x1D                          TMR1G                        0x48                             U3RX
         0x1E             CCP1 (Capture/Compare/PWM)                0x49                             U3TX
         0x1F                           TMR0                        0x4A                               U3E
         0x20                            U1RX                       0x4B                               U3
         0x21                            U1TX                       0x4C                          DMA3SCNT
         0x22                             U1E                       0x4D                          DMA3DCNT
         0x23                             U1                        0x4E                           DMA3OR
         0x24                           TMR3                        0x4F                            DMA3A
         0x25                          TMR3G                        0x50                              INT2
         0x26                         PWM1PR                        0x51                                -
         0x27                           PWM1                        0x52                                -


                                                                    Errata                                                  DS80000901G - 10

Table 2-1. Interrupt Vector Priority Table (continued)
                                                             Vector                              Interrupt
    Vector                      Interrupt                   Number                                source
   Number                        source
                                                             (cont.)                              (cont.)
     0x28                        SPI2RX                       0x53                                  TMR4
     0x29                        SPI2TX                       0x54                               DMA4SCNT
     0x2A                         SPI2                        0x55                               DMA4DCNT
     0x2B                           -                         0x56                                DMA4OR
     0x2C                   CM2 (Comparator)                  0x57                                 DMA4A


                                                              Errata                                                  DS80000901G - 11


3.   Appendix A: Revision History
     Doc Rev. Date    Comments
     G       03/2025 Added silicon errata issue 1.9.1; added DS Clarifications 2.1; updated DS revision letter.
     F       08/2023 Added Silicon Revision B1. Added silicon errata items 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8 and 1.8.1.
     E       04/2022 Updated the flash memory cell endurance specification data sheet clarification. Added silicon errata item
                     1.7.1.
     D       02/2022 Added silicon revision A6. Added silicon errata items 1.1.2, 1.3.2, 1.5.1 and 1.6.1.
     C       11/2020 Added silicon revision A5.
     B       08/2020 Added silicon errata item 1.5.1.
     A       06/2020 Initial document release.


                                                              Errata                                                  DS80000901G - 12


Microchip Information
Trademarks
The “Microchip” name and logo, the “M” logo, and other names, logos, and brands are registered
and unregistered trademarks of Microchip Technology Incorporated or its affiliates and/or
subsidiaries in the United States and/or other countries (“Microchip Trademarks”). Information
regarding Microchip Trademarks can be found at https://www.microchip.com/en-us/about/legal-
information/microchip-trademarks.
ISBN: 979-8-3371-0741-7

Legal Notice
This publication and the information herein may be used only with Microchip products, including
to design, test, and integrate Microchip products with your application. Use of this information
in any other manner violates these terms. Information regarding device applications is provided
only for your convenience and may be superseded by updates. It is your responsibility to ensure
that your application meets with your specifications. Contact your local Microchip sales office for
additional support or, obtain additional support at www.microchip.com/en-us/support/design-help/
client-support-services.
THIS INFORMATION IS PROVIDED BY MICROCHIP “AS IS”. MICROCHIP MAKES NO REPRESENTATIONS
OR WARRANTIES OF ANY KIND WHETHER EXPRESS OR IMPLIED, WRITTEN OR ORAL, STATUTORY
OR OTHERWISE, RELATED TO THE INFORMATION INCLUDING BUT NOT LIMITED TO ANY IMPLIED
WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
PURPOSE, OR WARRANTIES RELATED TO ITS CONDITION, QUALITY, OR PERFORMANCE.
IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, INCIDENTAL, OR
CONSEQUENTIAL LOSS, DAMAGE, COST, OR EXPENSE OF ANY KIND WHATSOEVER RELATED TO THE
INFORMATION OR ITS USE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS BEEN ADVISED OF THE
POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE FULLEST EXTENT ALLOWED BY LAW,
MICROCHIP’S TOTAL LIABILITY ON ALL CLAIMS IN ANY WAY RELATED TO THE INFORMATION OR
ITS USE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO
MICROCHIP FOR THE INFORMATION.
Use of Microchip devices in life support and/or safety applications is entirely at the buyer’s risk,
and the buyer agrees to defend, indemnify and hold harmless Microchip from any and all damages,
claims, suits, or expenses resulting from such use. No licenses are conveyed, implicitly or otherwise,
under any Microchip intellectual property rights unless otherwise stated.

Microchip Devices Code Protection Feature
Note the following details of the code protection feature on Microchip products:
•   Microchip products meet the specifications contained in their particular Microchip Data Sheet.
•   Microchip believes that its family of products is secure when used in the intended manner, within
    operating specifications, and under normal conditions.
•   Microchip values and aggressively protects its intellectual property rights. Attempts to breach the
    code protection features of Microchip products are strictly prohibited and may violate the Digital
    Millennium Copyright Act.
•   Neither Microchip nor any other semiconductor manufacturer can guarantee the security of its
    code. Code protection does not mean that we are guaranteeing the product is “unbreakable”.
    Code protection is constantly evolving. Microchip is committed to continuously improving the
    code protection features of our products.


                                                    Errata                                  DS80000901G - 13
