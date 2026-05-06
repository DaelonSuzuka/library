41.   DAC - Digital-to-Analog Converter Module
      The Digital-to-Analog Converter (DAC) supplies a variable voltage reference, ratiometric with the
      input source, with programmable selectable output levels.
      The positive and negative input references (VREF+ and VREF-) can each be selected from several
      sources.
      The output of the DAC (DACx_output) can be selected as a reference voltage to several other
      peripherals or routed to output pins.
      The Digital-to-Analog Converter (DAC) is enabled by setting the EN bit.


                  Important: This family of devices has two DAC modules. The DAC1 module has a buffered
                  output that can be connected to any of the designated DAC output pins. The DAC2 module
                  has no output pins or buffer, and the output is only connected internally to the CMP and
                  OPA modules.


--- p756 ---
       Figure 41-1. Digital-to-Analog Converter Block Diagram


                                                 VSOURCE+                                                  DACxR
             Positive
             Reference
                                                          R
             Sources


                                                          R
                PSS


                                                          R


                                                          R


                                             2n                             2n to 1      DACx_output
                                                                                                          To Peripherals
                                            Steps                           MUX
                  EN

                                                          R


                                                          R                                                             DACxOUTn(2)


                                                                                                            OEn (1,2)
                                                          R


             Negative                       VSOURCE-
             Reference
             Sources


                NSS
             Notes:      1. The output enable bits are configured so that they act as a “one-hot” system, meaning only one DAC
                            output can be enabled at a time.
                         2. DAC2 has no output buffer; the output from DAC2 is only connected internally to the specified peripherals.


41.1   Output Voltage Selection
       The DAC has 2n voltage level ranges, where n is the number of bits in DACR. Each level is determined
       by the DACxR bits. The DAC output voltage can be determined by using Equation 41-1.

       Equation 41-1. DAC Output Equation

       DACx_output =          VREF + − VREF − × DACR + VREF −
                                                 2n

41.2   Ratiometric Output Level
       The DAC output value is derived using a resistor ladder with each end of the ladder tied to a positive
       and negative voltage reference input source. If the voltage of either input source fluctuates, a similar
       fluctuation will result in the DAC output value.
       The value of the individual resistors within the ladder can be found in the “Electrical
       Specifications” chapter for each respective device.


--- p757 ---
41.3   Operation During Sleep
       When the device wakes from Sleep through an interrupt or a WWDT Time-out Reset, the contents of
       the DACxCON and DACxDATL registers are not affected. To minimize current consumption in Sleep
       mode, the voltage reference will be disabled.

41.4   Effects of a Reset
       A device Reset affects the following:
       •   The DAC module is disabled
       •   The DAC output voltage is removed from the DACxOUTn pin(s)
       •   The DACxR bits are cleared

41.5   Register Definitions: DAC Control
       Long bit name prefixes for the DAC are shown in the table below. Refer to the “Long Bit Names”
       section in the “Register and Bit Naming Conventions” chapter for more information.

       Table 41-1. DAC Long Bit Name Prefixes
                         Peripheral                                             Bit Name Prefix
                           DAC1                                                         DAC1
                           DAC2                                                         DAC2


--- p758 ---
41.5.1 DACxCON

            Name:       DACxCON
            Address:    0x7F

            Digital-to-Analog Converter Control Register

      Bit        7             6                5               4                   3                2              1             0
                EN                                   OE[1:0]                             PSS[1:0]                                NSS
  Access        R/W                            R/W             R/W                 R/W              R/W                          R/W
   Reset         0                              0               0                   0                0                            0

Bit 7 – EN DAC Enable
            Value      Description
            1          DAC is enabled
            0          DAC is disabled

Bits 5:4 – OE[1:0] DAC Output Enable
                                         OE                                                                DAC1
                                         11                                                     DACxOUT is disabled
                                         10                                               DACxOUT is enabled on pin RA2 only
                                         01                                               DACxOUT is enabled on pin RA0 only
                                         00                                                     DACxOUT is disabled

Bits 3:2 – PSS[1:0] DAC Positive Reference Selection
                                         PSS                                                    DAC Positive Reference
                                         11                                                         Reserved, do not use
                                         10                                                             FVR Buffer 2
                                         01                                                                VREF+
                                         00                                                                 VDD

Bit 0 – NSS DAC Negative Reference Selection
                                     NSS                                                        DAC Negative Reference
                                         1                                                                 VREF-
                                         0                                                                  VSS


--- p759 ---
41.5.2 DACxCON

            Name:       DACxCON
            Address:    0xA2


                        Important: This instance of the DAC module has no output pins or buffer; the output of
                        this DAC is only connected internally to be used with the Comparator and OPAMP modules.


            Digital-to-Analog Converter Control Register

      Bit        7             6               5              4                   3                2              1             0
                EN                                                                     PSS[1:0]                                NSS
  Access        R/W                                                              R/W              R/W                          R/W
   Reset         0                                                                0                0                            0

Bit 7 – EN DAC Enable
            Value      Description
            1          DAC is enabled
            0          DAC is disabled

Bits 3:2 – PSS[1:0] DAC Positive Reference Selection
                                         PSS                                                  DAC Positive Reference
                                         11                                                       Reserved, do not use
                                         10                                                           FVR Buffer 2
                                         01                                                              VREF+
                                         00                                                               VDD

Bit 0 – NSS DAC Negative Reference Selection
                                     NSS                                                      DAC Negative Reference
                                         1                                                               VREF-
                                         0                                                                VSS


--- p760 ---
41.5.3 DACxDATL

            Name:       DACxDATL
            Address:    0x7D

            Digital-to-Analog Converter Data Register

      Bit        7            6           5              4            3                   2           1              0
                                                           DACxR[7:0]
  Access        R/W         R/W          R/W            R/W         R/W              R/W            R/W            R/W
   Reset         0           0            0              0            0               0              0              0

Bits 7:0 – DACxR[7:0] Data Input Bits for DAC Value


--- p761 ---
41.5.4 DACxDATL

            Name:       DACxDATL
            Address:    0xA0

            Digital-to-Analog Converter Data Register

      Bit        7            6           5              4            3                   2           1              0
                                                           DACxR[7:0]
  Access        R/W         R/W          R/W            R/W         R/W              R/W            R/W            R/W
   Reset         0           0            0              0            0               0              0              0

Bits 7:0 – DACxR[7:0] Data Input Bits for DAC Value


--- p762 ---
41.6      Register Summary - DAC
Address     Name      Bit Pos.   7         6           5             4                3              2         1          0
 0x00
  ...      Reserved
 0x7C
 0x7D      DAC1DATL     7:0                                              DAC1R[7:0]
 0x7E      Reserved
 0x7F      DAC1CON      7:0      EN                        OE[1:0]                        PSS[1:0]                       NSS
 0x80
  ...      Reserved
 0x9F
 0xA0      DAC2DATL     7:0                                              DAC2R[7:0]
 0xA1      Reserved
 0xA2      DAC2CON      7:0      EN                                                       PSS[1:0]                       NSS


--- p763 ---
