                          PIC18(L)F26/27/45/46/47/55/56/57K42
37.0     5-BIT DIGITAL-TO-ANALOG                          The output of the DAC (DAC1_output) can be selected
                                                          as a reference voltage to the following:
         CONVERTER (DAC) MODULE
                                                          • Comparator positive input
The Digital-to-Analog Converter supplies a variable
                                                          • ADC input channel
voltage reference, ratiometric with the input source,
with 32 selectable output levels.                         • DAC1OUT1 pin
                                                          • DAC1OUT2 pin
The positive input source (VSOURCE+) of the DAC can
be connected to:                                          The Digital-to-Analog Converter (DAC) can be enabled
                                                          by setting the EN bit of the DAC1CON0 register.
• FVR Buffer
• External VREF+ pin
• VDD supply voltage
The negative input source (VSOURCE-) of the DAC can
be connected to:
• External VREF- pin
• Vss

FIGURE 37-1:              DIGITAL-TO-ANALOG CONVERTER BLOCK DIAGRAM
                                                                                                          Rev. 10-000026H
                                                                                                                10/12/2016


        Reserved          11
                                            VSOURCE+                                       DATA<4:0>
       FVR Buffer         10                                                   5
    VREF+                 01                       R

             AVDD         00

                                                   R
               PSS


                                                   R


                                                   R
                                                             32-to-1 MUX


                                         32                                DACx_output
                                                                                         To Peripherals
                                        Steps
                EN

                                                   R


                                                   R                                              DACxOUT1(1)


                                                                                          OE1
                                                   R
                                                                                                  DACxOUT2(1)


            VREF-              1        VSOURCE-                                          OE2
                AVSS           0

                    NSS


         Note 1: The unbuffered DACx_output is provided on the DACxOUT pin(s).


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 640
                         PIC18(L)F26/27/45/46/47/55/56/57K42
37.1      Output Voltage Selection                                              Reading the DAC1OUTn pin when it has been
                                                                                configured for DAC reference voltage output will
The DAC has 32 voltage level ranges. The 32 levels                              always return a ‘0’.
are set with the DATA[4:0] bits of the DAC1CON1
register.                                                                          Note:     The unbuffered DAC output (DAC1OUTn)
                                                                                             is not intended to drive an external load.
The DAC output voltage can be determined by using
Equation 37-1.
                                                                                37.4       Operation During Sleep
37.2      Ratiometric Output Level                                              When the device wakes up from Sleep through an
The DAC output value is derived using a resistor ladder                         interrupt or a Windowed Watchdog Timer Time-out, the
with each end of the ladder tied to a positive and                              contents of the DAC1CON0 register are not affected.
negative voltage reference input source. If the voltage                         To minimize current consumption in Sleep mode, the
of either input source fluctuates, a similar fluctuation                        voltage reference may be disabled.
will result in the DAC output value.
                                                                                37.5       Effects of a Reset
The value of the individual resistors within the ladder
can be found in Table 44-17.                                                    A device Reset affects the following:
                                                                                • DAC1 is disabled.
37.3      DAC Voltage Reference Output                                          • DAC1 output voltage is removed from the
The unbuffered DAC voltage can be output to the                                   DAC1OUTn pin(s).
DAC1OUTn pin(s) by setting the respective DACOEn                                • The DAC1R[4:0] range select bits are cleared.
bit(s) of the DAC1CON0 register. Selecting the DAC
reference voltage for output on either DAC1OUTn pin
automatically overrides the digital output buffer, the
weak pull-up and digital input threshold detector
functions of that pin.

EQUATION 37-1:            DAC OUTPUT VOLTAGE
  IF DACEN = 1

                                                  D ATA  4:0
           D ACx_output =   V REF+ – V REF-  ----------------
                                                                 ------------ + V REF-
                                                                 5
                                                              2

       Note:    See the DAC1CON0 register for the available VSOURCE+ and VSOURCE- selections.


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 641
                        PIC18(L)F26/27/45/46/47/55/56/57K42
37.6      Register Definitions: DAC Control
Long bit name prefixes for the DAC peripheral is shown
below. Refer to Section 1.3.2.2 “Long Bit Names” for
more information.


          Peripheral               Bit Name Prefix
             DAC1                        DAC1
                                                                     l
REGISTER 37-1:           DAC1CON0: DAC CONTROL REGISTER
    R/W-0/0            U-0          R/W-0/0             R/W-0/0     R/W-0/0        R/W-0/0             U-0       R/W-0/0
        EN              —             OE1                OE2                PSS[1:0]                   —           NSS
bit 7                                                                                                                     bit 0


Legend:
R = Readable bit                 W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              EN: DAC Enable bit
                   1 = DAC is enabled
                   0 = DAC is disabled(1)
bit 6              Unimplemented: Read as ‘0’
bit 5              OE1: DAC Voltage Output Enable bit
                   1 = DAC voltage level is output on the DAC1OUT1 pin
                   0 = DAC voltage level is disconnected from the DAC1OUT1 pin
bit 4              OE2: DAC Voltage Output Enable bit
                   1 = DAC voltage level is output on the DAC1OUT2 pin
                   0 = DAC voltage level is disconnected from the DAC1OUT2 pin
bit 3-2            PSS[1:0]: DAC Positive Source Select bit
                   11 = Reserved
                   10 = FVR buffer 2
                   01 = VREF+
                   00 = VDD
bit 1              Unimplemented: Read as ‘0’
bit 0              NSS: DAC Negative Source Select bit
                   1 = VREF-
                   0 = VSS
Note 1:      DAC1OUTx output pins are still active.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 642
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 37-2:              DAC1CON1: DAC DATA REGISTER
        U-0              U-0            U-0             R/W-0/0      R/W-0/0          R/W-0/0             R/W-0/0       R/W-0/0
          —               —             —                                             DATA[4:0]
bit 7                                                                                                                        bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            DATA[4:0]: Data Input Register for DAC bits


TABLE 37-1:         SUMMARY OF REGISTERS ASSOCIATED WITH THE DAC MODULE
                                                                                                                         Register
    Name            Bit 7       Bit 6         Bit 5        Bit 4       Bit 3       Bit 2          Bit 1         Bit 0
                                                                                                                         on page
DAC1CON0             EN          —            OE1           OE2            PSS[1:0]                —            NSS        643
DAC1CON1             —           —             —                                 DATA[4:0]                                 644
Legend:       — = Unimplemented location, read as ‘0’. Shaded cells are not used with the DAC module.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 643
