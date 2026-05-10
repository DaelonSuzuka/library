PIC18F27/47/57Q43 Silicon Errata and Data Sheet
Clarifications
PIC18F27/47/57Q43


The PIC18F27/47/57Q43 devices you have received conform functionally to the current device data sheet
(DS40002147G), except for the anomalies described in this document.
The silicon issues discussed in the following pages are for silicon revisions with the Device and Revision IDs
listed in the table below.
The errata described in this document will be addressed in future revisions of the PIC18F27/47/57Q43 silicon.
Note: This document summarizes all silicon errata issues from all revisions of silicon, previous as well as
current.

Table 1. Silicon Device Identification
                                                                                           Revision ID
          Part Number                    Device ID
                                                                 B0                 B2                    B3           C0
          PIC18F27Q43                    0x7480                0xA040             0xA042                 0xA043      0xA080
          PIC18F47Q43                    0x74A0                0xA040             0xA042                 0xA043      0xA080
          PIC18F57Q43                    0x74C0                0xA040             0xA042                 0xA043      0xA080


       Important: Refer to the Device/Revision ID section in the current “PIC18FXXQ43 Family
       Programming Specification” (DS40002079) for more detailed information on Device
       Identification and Revision IDs for your specific device.


                                                                 Errata                                           DS80000870M - 1
                                                                                                           PIC18F27/47/57Q43


Table 2. Silicon Issue Summary
                                                                                                     Affected Revisions
     Module               Feature           Item No.              Issue Summary
                                                                                                B0    B2        B3        C0
                                            Capacitive
                     Capacitive Voltage        Voltage CVD is only functional on PORTA[2:0]
                                                                                                X
                         Divider               Divider  and PORTB[4:0]
                                                (CVD)
      ADCC
                                               Double
                                                        An unexpected acquisition time is
                      Double Sample            Sample
                                                        added between the first and second      X     X         X         X
                       Conversions         Conversion
                                                        conversions.
                                                   s
                                            Maximum Maximum clock frequency limited to 2
                                                Clock   MHz for XT mode
                                            Frequency
    Oscillator           XT mode                                                                X     X
                                           Limited to 2
                                            MHz for XT
                                                Mode
                                                 The    The I2CxADR0/1/2/3 registers have
                                           I2CxADR0/1 incorrect Reset value
                                                 /2/3
                            I2C              Registers                                          X     X         X
                                                Have
                                             Incorrect
                                           Reset Value
                                               The I2C The I2C Start and/or Stop flags may be
                                           Start and/or set when I2C is enabled
                                            Stop Flags
                            I2C                                                                 X     X         X
                                            May Be Set
                                           When I2C Is
                                              Enabled
                                            Operating Multi-Master mode will cause bus
                                              in Multi- failures
                    Multi-Master mode       Host Mode                                           X     X         X         X
                                            Will Cause
       I2C                                 Bus Failures
                                            MDR Bit Is MDR bit is not cleared after Bus
                                           Not Cleared Timeout
                            I2C                                                                 X     X         X         X
                                             after Bus
                                             Time-Out
                                            Bus Time- Bus Timeout not Detected Properly
                                              Out Not when External Host Clock Stretches
                                             Detected
                                             Properly
                            I2C                                                                 X     X         X         X
                                                When
                                              External
                                            Host Clock
                                             Stretches
                                                Clock   Clock Stretch Disable not working
                                               Stretch  properly
                   Clock Stretch Disable   Disable Not                                          X     X         X         X
                                              Working
                                             Properly


                                                                 Errata                                          DS80000870M - 2
                                                                                                                PIC18F27/47/57Q43


...........continued
                                                                                                          Affected Revisions
     Module                 Feature             Item No.               Issue Summary
                                                                                                     B0    B2        B3        C0
                                                Bus Time- Bus Timeout causes False Start/Stop
                               2               Out Causes
                              I C                                                                    X     X         X         X
                                               False Start/
                                                    Stop
                                                  The Bus I2C - The Bus Free Divider Ratio
                                              Free Divider BFREDR = 1 value is not functional.
                                                    Ratio
                        Bus Free Time                                                                X     X         X         X
                                               BFREDR = 1
                                              Value Is Not
                                                Functional
                                                CSTR Bit Is CSTR bit is not cleared after Bus
                                               Not Cleared Timeout
                              I2C                                                                    X     X         X         X
                                                 after Bus
                                                 Time-Out
                                                     Bus    Bus Collision Followed By a Stop
         I2C                                     Collision Condition During a Transaction by an
                                               Followed by External Host Device May Hang the
                                                   a Stop   Bus
                                                Condition
                                                 during a
                         Bus Collision                                                               X     X         X         X
                                               Transaction
                                                   by an
                                                 External
                                               Host Device
                                                May Hang
                                                  the Bus
                                               I2C Module I2C Module May Hang the Bus During
                                                May Hang Multi-Host Arbitration
                                                  the Bus
                    Multi-Host Arbitration                                                           X     X         X         X
                                                   during
                                                Multi-Host
                                               Arbitration
                                              SRAM Read- SRAM read-back can be incorrect
       SRAM            SRAM read-back                                                                X
                                                    Back
                                                 Software Software breakpoints are not
                                              Breakpoints available
 In-Circuit Debug   Software breakpoints                                                             X     X         X         X
                                                  Are Not
                                                 Available
                                                            Module stops working if RST bit is set
        SMT                Reset Bit             Reset Bit                                           X     X         X         X
                                                            while prescaler setting is not zero
                                               UART TXDE UART TXDE signal may go low before
                                                Signal May the STOP bit has been entirely
     Universal                                    Go Low transmitted
  Asynchronous                                  before the
                             UART                                                                    X     X         X         X
     Receiver                                    STOP Bit
   Transmitter                                   Has Been
                                                  Entirely
                                              Transmitted
Note: Only those issues indicated in the last column apply to the current silicon revision.


                                                                     Errata                                           DS80000870M - 3
                                                                                                   PIC18F27/47/57Q43
                                                                                                   Silicon Errata Issues


1.      Silicon Errata Issues

                         This document summarizes all silicon errata issues from all revisions of silicon,
                         previous and current. Only the issues indicated by the bold font in the following
                         tables apply to the current silicon revision.


1.1     Module: Analog-to-Digital Converter with Computation (ADCC)
1.1.1   Capacitive Voltage Divider (CVD)
        The CVD feature is only functional on PORTA[2:0] and PORTB[4:0]. This feature is not recommended
        for use on any other pins.
        Work around
        None.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X


1.1.2   Double Sample Conversions
        When enabling a Double Sample Conversion (DSEN = 1) with no Pre-charge time (ADPRE = 0) and no
        Acquisition time (ADACQ = 0), the maximum number of cycles of acquisition time is inserted prior
        to the second conversion. The first conversion will be performed as expected with no Pre-charge
        time and no Acquisition time. It is only between the first and second conversions where a maximum
        number of cycles of Acquisition time is performed unexpectedly.
        Work around
        Method 1:
        Disable Double Sample Conversion (DSEN = 0) and perform two single conversions back to back.
        Method 2:
        If adding acquisition time is acceptable, then select no Precharge time, along with the desired
        Acquisition time.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X   X


1.2     Module: Oscillator (OSC)
1.2.1   Maximum Clock Frequency Limited to 2 MHz for XT Mode
        The maximum clock frequency for the intermediate gain setting that supports quartz crystal and
        ceramic resonator operation (XT mode) is being reduced from 4 MHz to 2 MHz.
        Work around
        For crystal or resonator frequencies above 2 MHz, use HS mode.

        Affected Silicon Revisions
        B0 B2 B3 C0


                                                              Errata                                     DS80000870M - 4
                                                                                              PIC18F27/47/57Q43
                                                                                              Silicon Errata Issues

         X   X


1.3     Module: Inter-Integrated Circuit (I2C)
1.3.1   The I2CxADR0/1/2/3 Registers Have Incorrect Reset Value
        The I2CxADR0/2 registers reset to 0xFF when the I2CxMD is enabled instead of 0x00. The
        I2CxADR1/3 registers reset to 0xFE when the I2CxMD is enabled instead of 0x00.
        Work around
        None.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X


1.3.2   The I2C Start and/or Stop Flags May Be Set When I2C Is Enabled
        When I2C is enabled, erroneous Start and/or Stop conditions may be detected. This can generate
        erroneous I2C interrupts if enabled.
        Work around
        Use the following procedure to correctly detect the Start and Stop conditions:
        1. Disable the Start and Stop conditions interrupt functions.
        2. Enable the I2C module.
        3. Wait 250 ns + six instruction cycles (FOSC/4).
        4. Clear the Start and Stop conditions interrupt flags.
        5. Enable the Start and Stop conditions interrupt functions if used.

         I2CxPIEbits.SCIE = 0;          // Disable Start condition interrupt
         I2CxPIEbits.PCIE = 0;          // Disable Stop condition interrupt
         I2CxCON0bits.EN = 1;           // Enable I2C
         Delay();                       // Wait for 250 ns + 6 instruction cycles (FOSC/4)
         I2CxPIRbits.SCIF = 0;          // Clear the Start condition interrupt flags
         I2CxPIRbits.PCIF = 0;          // Clear the Stop condition interrupt flags
         I2CxPIEbits.SCIE = 1;          // Enable Start condition interrupt if used
         I2CxPIEbits.PCIE = 1;          // Enable Stop condition interrupt if used

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X


1.3.3   Operating in Multi-Host Mode Will Cause Bus Failures
        If operating in Multi-Host mode and a second host drives SDA low at the same time the Start bit is
        generated, the module will fail to go into Host mode, but will continue to send an address and data
        as if it won arbitration. I2CCNT fails to decrement, and the module will remain in this state until a
        bus time-out occurs or the device is reset.
        Work around
        None.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X   X


                                                            Errata                                  DS80000870M - 5
                                                                                               PIC18F27/47/57Q43
                                                                                               Silicon Errata Issues

1.3.4   MDR Bit Is Not Cleared after Bus Time-Out
        In the Host mode of the I2C module, when a bus time-out occurs during clock stretching and TOREC
        = 1, the MDR bit will not be cleared and a Stop will not be transmitted on the bus.
        Work around
        Force a Stop on the bus by setting the P bit upon bus time-out in Host mode. Forcing a Stop on the
        bus clears the MDR bit.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X   X


1.3.5   Bus Time-Out Not Detected Properly When External Host Clock Stretches
        When the module is operating in Client mode and an external Host device is clock stretching after
        the 8th SCL clock and a bus time-out occurs, the bus time-out is not detected properly. When the
        external Host times out before the Client and releases SCL to generate a Stop condition, the module
        continues to stretch SDA as if to generate an ACK and hangs the bus, and a Stop is never seen on
        the bus.
        Work around
        Reset the module by toggling the EN bit.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X   X


1.3.6   Clock Stretch Disable Not Working Properly
        When the CSD bit is set between a Start condition and the 8th falling SCL edge, the I2C module
        enters a state where the module clock stretches indefinitely after the next Start until a bus time-out
        occurs.
        Work around
        Force a reset of the module by toggling the EN bit.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X   X


1.3.7   Bus Time-Out Causes False Start/Stop
        When the module is operating in Client mode and an external Host device is clock stretching and
        a bus time-out occurs in the Client, the Client releases SDA and goes into the idle state. After the
        external Host generates a Stop condition on the bus by releasing SCL, the module can erroneously
        drive a low pulse on the SDA line, which acts as a false Start and Stop on the bus.
        Work around
        None.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X   X


1.3.8   The Bus Free Divider Ratio BFREDR = 1 Value Is Not Functional
        Setting the Bus Free Divider Ratio bit (BFREDR = 1) has no effect on the Bus Free Time Divider ratio.


                                                          Errata                                     DS80000870M - 6
                                                                                               PIC18F27/47/57Q43
                                                                                               Silicon Errata Issues

        Work around
        Maintain BFREDR = 0 at all times.

        Affected Silicon Revisions
         B0 B2 B3 C0
         X   X   X   X


1.3.9   CSTR Bit Is Not Cleared after Bus Time-Out
        When the module is operating in Client mode and TOREC = 1, and a bus time-out occurs during
        clock stretching, the CSTR bit will not be cleared, and the module continues to clock stretch and
        hang the bus.
        Work around
        Reset the I2C module by toggling the EN bit.

        Affected Silicon Revisions
         B0 B2 B3 C0
         X   X   X   X


1.3.10 Bus Collision Followed by a Stop Condition during a Transaction by an External Host Device
       May Hang the Bus
        In a Multi-Host environment, when another Host device on the bus causes a collision (BCLIF bit) and
        forces a Stop during a transaction, the I2C module may not respond appropriately and hang the bus.
        Work around
        When a Bus Collision (BCLIF) is detected along with a Stop condition (PCIF), reset the I2C module by
        toggling the EN bit.

        Affected Silicon Revisions
         B0 B2 B3 C0
         X   X   X   X


1.3.11 I2C Module May Hang the Bus during Multi-Host Arbitration
        The I2C module may hang the bus in a Multi-Host environment when another Host device initiates a
        transaction on the bus by issuing the Start condition before the I2C module pulls down the SDA line,
        and the most significant bit of the address header starts with a '0' in FME=0 or FME=1 mode.
        Work around
        When using FME=0 or FME=1 modes, the user can choose to assign addresses such that the most
        significant bit of the address header starts with a '1'. Alternatively, the user can select the FME=2
        mode of operation.

        Affected Silicon Revisions
         B0 B2 B3 C0
         X   X   X   X


1.4     Module: SRAM
1.4.1   SRAM Read-Back
        Following a device power-up sequence, there is a possibility that some SRAM locations will not
        return the expected written value but will read back ‘00’ instead.


                                                          Errata                                     DS80000870M - 7
                                                                                              PIC18F27/47/57Q43
                                                                                              Silicon Errata Issues

        Work around
        None. The device can only recover by power cycling.
        This erroneous condition can be detected by running the following code that writes nonzero values
        to SRAM and then verifies that the returned read values are not ‘00’. If a returned value is ‘00’,
        the application code has to be put into a safe state until a POR event occurs. This code has to be
        executed immediately after power-up. If the test passes, the device operation will be normal.
         // SRAM test

         FSR0 = 0xcff;         // Write data into RAM address for devices up to 2K RAM
         INDF0 = 0x55;
         PROD = INDF0;         // Read back data
         if (PROD == 0){
             SAFE_STATE();     // RAM incorrectly read, suspend operation and go to Safe state
         }

         //For devices with more than 2K of SRAM, add the following code
         FSR0 = 0x14ff;       // Write data into RAM
         INDF0 = 0x55;
         PROD = INDF0;        // Read back data
         if (PROD == 0){
             SAFE_STATE();    // RAM incorrectly read, suspend operation and go to Safe state
         }

         //For devices with more than 4K of SRAM, add the following code
         FSR0 = 0x24ff;       // Write data into RAM
         INDF0 = 0x55;
         PROD = INDF0;        // Read back data
         if (PROD == 0){
             SAFE_STATE();    // RAM incorrectly read, suspend operation and go to Safe state
         }


        Affected Silicon Revisions
        B0 B2 B3 C0
         X


1.5     Module: In-Circuit Debug
1.5.1   Software Breakpoints Are Not Available
        When debugging code, software breakpoints will not be available.
        Work around
        None.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X   X   X


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


                                                          Errata                                    DS80000870M - 8
                                                                                                                    PIC18F27/47/57Q43
                                                                                                                    Silicon Errata Issues

        Method 2:
        Write zero to the counter manually. Either disable the module or the clock before using this method.
        Method 3:
        Use 1:1 prescaler (PS = 00).
        Method 4:
        Use the CLKREF subsystem to provide a prescaled clock and set PS = 00.

        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X    X   X


1.7     Module: Universal Asynchronous Receiver Transmitter (UART)
1.7.1   UART TXDE Signal May Go Low before the STOP Bit Has Been Entirely Transmitted
        The UART Transmit Drive Enable (TXDE) signal could potentially transition into a low state before the
        UART STOP bit has been entirely transmitted due to the effects of parasitic capacitance on the TX
        line. In some applications, this could result in communication being prematurely terminated due to
        the TXDE bit going low before the STOP bit has had enough time to settle.
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
          MCU Controller              RS485 Interface IC                   Device 1              Device 3
                                                                 562 W
                           RX           R
                                                    A
                                        RE
                      TXDE                                   133 W                                          120 W
                                        DE
                                                    B
                           TX
                                        D
                                                             562 W
                                                                                      Device 2
                                GND
                                                           GND


        Affected Silicon Revisions
        B0 B2 B3 C0
         X   X    X   X


                                                                            Errata                                        DS80000870M - 9
                                                                                                       PIC18F27/47/57Q43
                                                                                                   Data Sheet Clarifications


2.    Data Sheet Clarifications
      The following typographic corrections and clarifications are to be noted for the latest version of the
      device data sheet (DS40002147G):
      Note:
      Corrections are shown in bold. Where possible, the original bold text formatting has been removed
      for clarity.

2.1   NVM-Nonvolatile Memory Module (Writing to DFM)
      In Section 10.4.2 Writing to DFM, the stepwise process is clarified to provide specific instructions on
      when to enable interrupts during the NVM Write sequence. The code example in Example 10-10 is
      also amended with an additional line. The changes are shown below in bold.
      1. Set NVMADR registers with the target byte address.
      2. Load NVMDATL register with desired byte.
      3. Set the NVMCMD control bits to ‘b011 (Byte Write).
      4. Disable all interrupts.
      5. Perform the unlock sequence as described in the Unlock Sequence section.
      6. Set the GO bit to start the DFM byte write.
      7. Interrupts can be enabled after the GO bit is set. If it is not desired to have interrupts
         during DFM write, then enable interrupts after the next step when the GO bit is cleared.
      8. Monitor the GO bit or NVMIF interrupt flag to determine when the write has been completed.
      9. Set the NVMCMD control bits to ‘b000.
      Example 10-10. Writing a Byte to Data Flash Memory in C
       // Code sequence to write one byte to a DFM
       // DFM target address is specified by DFM_ADDR
       // Target data are specified by ByteValue

       // Save interrupt enable bit value
       uint8_t GIEBitValue = INTCON0bits.GIE;

       // Load NVMADR with the target address of the byte
       NVMADR = DFM_ADDR;
       NVMDATL = ByteValue;                    // Load NVMDAT with the desired value
       NVMCON1bits.CMD = 0x03;                 // Set the byte write command
       INTCON0bits.GIE = 0;                    // Disable interrupts
       //––––––––– Required Unlock Sequence –––––––––
       NVMLOCK = 0x55;
       NVMLOCK = 0xAA;
       NVMCON0bits.GO = 1;                     // Start byte write
       //–––––––––––––––––––––––––––––––––––––––––––––––
       INTCON0bits.GIE = GIEBitValue; // Restore interrupt enable bit value (if interrupts are desired during DFM write)
       while (NVMCON0bits.GO);                 // Wait for the write operation to complete

       // Verify byte write operation success and call the recovery function if needed
       if (NVMCON1bits.WRERR){
          WRITE_FAULT_RECOVERY();
       }

       NVMCON1bits.CMD = 0;                     // Disable writes to memory


                                                            Errata                                          DS80000870M - 10
                                                                                           PIC18F27/47/57Q43
                                                                                       Data Sheet Clarifications

2.2   PIC18 CPU (System Arbitration)
      The following note has been added after the existing text of Section 7.1 System Arbitration, to
      clarify the interaction of the System Arbiter, the PRLOCKED bit and system interrupts.


            Important: When the PRLOCKED bit is set, the Non Volatile Memory (NVM)
            module has a fixed priority of 0 that cannot be changed. If an interrupt
            is desired when an NVM read/write operation is in progress, then the ISR
            priority level must be set to 0. The NVM module priority is ignored when
            PRLOCKED bit is cleared.


                                                       Errata                                   DS80000870M - 11
                                                                                                             PIC18F27/47/57Q43
                                                                                                      Appendix A: Revision History


3.   Appendix A: Revision History
     Doc Rev. Date    Comments
     M       08/2024 Added silicon errata items 1.3.4 through 1.3.11 and data sheet clarifications 2.1 and 2.2.
     L       03/2023 Added silicon revision C0 and silicon errata item 1.3.3. Updated data sheet revision to revision G and
                     removed previous clarification issues.
     K       03/2022 Added silicon errata items 1.1.2, 1.6.1, 17.1 and data sheet clarifications 2.1 and 2.2.
     J       07/2021 Added silicon errata item 1.3.2.
     H       03/2021 Added silicon errata item 1.5.1; deleted data sheet clarification 2.1.
     G       10/2020 Added silicon revision B3 and UART Transmit Collision Interrupt data sheet clarification; updated silicon
                     errata item 1.3.1.
     F       08/2020 Added silicon revision B2
     E       06/2020 Added silicon errata item 1.4.1.
     D       06/2020 Added silicon errata item 1.3.1.
     C       04/2020 Added XT mode errata and Temperature Indicator data sheet clarification.
     B       02/2020 Added working pins for CVD.
     A       12/2019 Initial document release


                                                              Errata                                               DS80000870M - 12
                                                                                        PIC18F27/47/57Q43


Microchip Information
The Microchip Website
Microchip provides online support via our website at www.microchip.com/. This website is used to
make files and information easily available to customers. Some of the content available includes:
•   Product Support – Data sheets and errata, application notes and sample programs, design
    resources, user’s guides and hardware support documents, latest software releases and archived
    software
•   General Technical Support – Frequently Asked Questions (FAQs), technical support requests,
    online discussion groups, Microchip design partner program member listing
•   Business of Microchip – Product selector and ordering guides, latest Microchip press releases,
    listing of seminars and events, listings of Microchip sales offices, distributors and factory
    representatives

Product Change Notification Service
Microchip’s product change notification service helps keep customers current on Microchip
products. Subscribers will receive email notification whenever there are changes, updates, revisions
or errata related to a specified product family or development tool of interest.
To register, go to www.microchip.com/pcn and follow the registration instructions.

Customer Support
Users of Microchip products can receive assistance through several channels:
•   Distributor or Representative
•   Local Sales Office
•   Embedded Solutions Engineer (ESE)
•   Technical Support
Customers should contact their distributor, representative or ESE for support. Local sales offices are
also available to help customers. A listing of sales offices and locations is included in this document.
Technical support is available through the website at: www.microchip.com/support

Microchip Devices Code Protection Feature
Note the following details of the code protection feature on Microchip products:
•   Microchip products meet the specifications contained in their particular Microchip Data Sheet.
•   Microchip believes that its family of products is secure when used in the intended manner, within
    operating specifications, and under normal conditions.
•   Microchip values and aggressively protects its intellectual property rights. Attempts to breach the
    code protection features of Microchip product is strictly prohibited and may violate the Digital
    Millennium Copyright Act.
•   Neither Microchip nor any other semiconductor manufacturer can guarantee the security of its
    code. Code protection does not mean that we are guaranteeing the product is “unbreakable”.
    Code protection is constantly evolving. Microchip is committed to continuously improving the
    code protection features of our products.

Legal Notice
This publication and the information herein may be used only with Microchip products, including
to design, test, and integrate Microchip products with your application. Use of this information
in any other manner violates these terms. Information regarding device applications is provided
only for your convenience and may be superseded by updates. It is your responsibility to ensure


                                                   Errata                                   DS80000870M - 13
                                                                                      PIC18F27/47/57Q43


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

Trademarks
The Microchip name and logo, the Microchip logo, Adaptec, AVR, AVR logo, AVR Freaks, BesTime,
BitCloud, CryptoMemory, CryptoRF, dsPIC, flexPWR, HELDO, IGLOO, JukeBlox, KeeLoq, Kleer,
LANCheck, LinkMD, maXStylus, maXTouch, MediaLB, megaAVR, Microsemi, Microsemi logo, MOST,
MOST logo, MPLAB, OptoLyzer, PIC, picoPower, PICSTART, PIC32 logo, PolarFire, Prochip Designer,
QTouch, SAM-BA, SenGenuity, SpyNIC, SST, SST Logo, SuperFlash, Symmetricom, SyncServer,
Tachyon, TimeSource, tinyAVR, UNI/O, Vectron, and XMEGA are registered trademarks of Microchip
Technology Incorporated in the U.S.A. and other countries.
AgileSwitch, ClockWorks, The Embedded Control Solutions Company, EtherSynch, Flashtec, Hyper
Speed Control, HyperLight Load, Libero, motorBench, mTouch, Powermite 3, Precision Edge,
ProASIC, ProASIC Plus, ProASIC Plus logo, Quiet-Wire, SmartFusion, SyncWorld, TimeCesium,
TimeHub, TimePictra, TimeProvider, and ZL are registered trademarks of Microchip Technology
Incorporated in the U.S.A.
Adjacent Key Suppression, AKS, Analog-for-the-Digital Age, Any Capacitor, AnyIn, AnyOut,
Augmented Switching, BlueSky, BodyCom, Clockstudio, CodeGuard, CryptoAuthentication,
CryptoAutomotive, CryptoCompanion, CryptoController, dsPICDEM, dsPICDEM.net, Dynamic
Average Matching, DAM, ECAN, Espresso T1S, EtherGREEN, EyeOpen, GridTime, IdealBridge,
IGaT, In-Circuit Serial Programming, ICSP, INICnet, Intelligent Paralleling, IntelliMOS, Inter-Chip
Connectivity, JitterBlocker, Knob-on-Display, MarginLink, maxCrypto, maxView, memBrain, Mindi,
MiWi, MPASM, MPF, MPLAB Certified logo, MPLIB, MPLINK, mSiC, MultiTRAK, NetDetach, Omniscient
Code Generation, PICDEM, PICDEM.net, PICkit, PICtail, Power MOS IV, Power MOS 7, PowerSmart,
PureSilicon, QMatrix, REAL ICE, Ripple Blocker, RTAX, RTG4, SAM-ICE, Serial Quad I/O, simpleMAP,
SimpliPHY, SmartBuffer, SmartHLS, SMART-I.S., storClad, SQI, SuperSwitcher, SuperSwitcher II,
Switchtec, SynchroPHY, Total Endurance, Trusted Time, TSHARC, Turing, USBCheck, VariSense,
VectorBlox, VeriPHY, ViewSpan, WiperLock, XpressConnect, and ZENA are trademarks of Microchip
Technology Incorporated in the U.S.A. and other countries.
SQTP is a service mark of Microchip Technology Incorporated in the U.S.A.
The Adaptec logo, Frequency on Demand, Silicon Storage Technology, and Symmcom are registered
trademarks of Microchip Technology Inc. in other countries.
GestIC is a registered trademark of Microchip Technology Germany II GmbH & Co. KG, a subsidiary
of Microchip Technology Inc., in other countries.


                                                  Errata                                   DS80000870M - 14
                                                                                    PIC18F27/47/57Q43


All other trademarks mentioned herein are property of their respective companies.

ISBN: 978-1-6683-3425-6

Quality Management System
For information regarding Microchip’s Quality Management Systems, please visit
www.microchip.com/quality.


                                                 Errata                                 DS80000870M - 15
Worldwide Sales and Service
AMERICAS                    ASIA/PACIFIC                   ASIA/PACIFIC              EUROPE

Corporate Office            Australia - Sydney             India - Bangalore         Austria - Wels
2355 West Chandler Blvd.    Tel: 61-2-9868-6733            Tel: 91-80-3090-4444      Tel: 43-7242-2244-39
Chandler, AZ 85224-6199     China - Beijing                India - New Delhi         Fax: 43-7242-2244-393
Tel: 480-792-7200                                                                    Denmark - Copenhagen
                            Tel: 86-10-8569-7000           Tel: 91-11-4160-8631
Fax: 480-792-7277
                            China - Chengdu                India - Pune              Tel: 45-4485-5910
Technical Support:                                                                   Fax: 45-4485-2829
                            Tel: 86-28-8665-5511           Tel: 91-20-4121-0141
www.microchip.com/support
                                                                                     Finland - Espoo
                            China - Chongqing              Japan - Osaka
Web Address:
                                                                                     Tel: 358-9-4520-820
www.microchip.com           Tel: 86-23-8980-9588           Tel: 81-6-6152-7160
                                                                                     France - Paris
Atlanta                     China - Dongguan               Japan - Tokyo
                                                                                     Tel: 33-1-69-53-63-20
Duluth, GA                  Tel: 86-769-8702-9880          Tel: 81-3-6880- 3770
                                                                                     Fax: 33-1-69-30-90-79
Tel: 678-957-9614           China - Guangzhou              Korea - Daegu
                                                                                     Germany - Garching
Fax: 678-957-1455           Tel: 86-20-8755-8029           Tel: 82-53-744-4301
                                                                                     Tel: 49-8931-9700
Austin, TX                  China - Hangzhou               Korea - Seoul
                                                                                     Germany - Haan
Tel: 512-257-3370           Tel: 86-571-8792-8115          Tel: 82-2-554-7200
                                                                                     Tel: 49-2129-3766400
Boston                      China - Hong Kong SAR          Malaysia - Kuala Lumpur
                                                                                     Germany - Heilbronn
Westborough, MA             Tel: 852-2943-5100             Tel: 60-3-7651-7906
Tel: 774-760-0087                                                                    Tel: 49-7131-72400
                            China - Nanjing                Malaysia - Penang
Fax: 774-760-0088                                                                    Germany - Karlsruhe
                            Tel: 86-25-8473-2460           Tel: 60-4-227-8870
Chicago                                                                              Tel: 49-721-625370
                            China - Qingdao                Philippines - Manila
Itasca, IL                                                                           Germany - Munich
                            Tel: 86-532-8502-7355          Tel: 63-2-634-9065
Tel: 630-285-0071                                                                    Tel: 49-89-627-144-0
Fax: 630-285-0075           China - Shanghai               Singapore
                                                                                     Fax: 49-89-627-144-44
Dallas                      Tel: 86-21-3326-8000           Tel: 65-6334-8870
                                                                                     Germany - Rosenheim
Addison, TX                 China - Shenyang               Taiwan - Hsin Chu
                                                                                     Tel: 49-8031-354-560
Tel: 972-818-7423           Tel: 86-24-2334-2829           Tel: 886-3-577-8366
                                                                                     Israel - Hod Hasharon
Fax: 972-818-2924           China - Shenzhen               Taiwan - Kaohsiung
                                                                                     Tel: 972-9-775-5100
Detroit                     Tel: 86-755-8864-2200          Tel: 886-7-213-7830
                                                                                     Italy - Milan
Novi, MI                    China - Suzhou                 Taiwan - Taipei
                                                                                     Tel: 39-0331-742611
Tel: 248-848-4000
                            Tel: 86-186-6233-1526          Tel: 886-2-2508-8600      Fax: 39-0331-466781
Houston, TX
                            China - Wuhan                  Thailand - Bangkok        Italy - Padova
Tel: 281-894-5983
                            Tel: 86-27-5980-5300           Tel: 66-2-694-1351        Tel: 39-049-7625286
Indianapolis
                            China - Xian                   Vietnam - Ho Chi Minh     Netherlands - Drunen
Noblesville, IN
                            Tel: 86-29-8833-7252           Tel: 84-28-5448-2100      Tel: 31-416-690399
Tel: 317-773-8323
                            China - Xiamen                                           Fax: 31-416-690340
Fax: 317-773-5453
Tel: 317-536-2380           Tel: 86-592-2388138                                      Norway - Trondheim

Los Angeles                 China - Zhuhai                                           Tel: 47-72884388

Mission Viejo, CA           Tel: 86-756-3210040                                      Poland - Warsaw
Tel: 949-462-9523                                                                    Tel: 48-22-3325737
Fax: 949-462-9608                                                                    Romania - Bucharest
Tel: 951-273-7800
                                                                                     Tel: 40-21-407-87-50
Raleigh, NC
                                                                                     Spain - Madrid
Tel: 919-844-7510
                                                                                     Tel: 34-91-708-08-90
New York, NY                                                                         Fax: 34-91-708-08-91
Tel: 631-435-6000                                                                    Sweden - Gothenberg
San Jose, CA                                                                         Tel: 46-31-704-60-40
Tel: 408-735-9110                                                                    Sweden - Stockholm
Tel: 408-436-4270
                                                                                     Tel: 46-8-5090-4654
Canada - Toronto
                                                                                     UK - Wokingham
Tel: 905-695-1980
                                                                                     Tel: 44-118-921-5800
Fax: 905-695-2078
                                                                                     Fax: 44-118-921-5820


                                                       Errata                                              DS80000870M - 16
