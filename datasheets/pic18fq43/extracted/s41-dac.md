                                                                                                             PIC18F27/47/57Q43
                                                                                      DAC - Digital-to-Analog Converter Module -
                                                                                                                           8-Bit

41.   DAC - Digital-to-Analog Converter Module - 8-Bit
      The Digital-to-Analog Converter (DAC) supplies a variable voltage reference, ratiometric with the
      input source, with programmable selectable output levels.
      The positive and negative input references (VSOURCE+ and VSOURCE-) can each be selected from several
      sources.
      The output of the DAC (DACx_output) can be selected as a reference voltage to several other
      peripherals or routed to output pins.
      The Digital-to-Analog Converter (DAC) is enabled by setting the EN bit.

      Figure 41-1. Digital-to-Analog Converter Block Diagram


                                            VSO URCE +                                           DACxR
            Positive
            Reference
                                                    R
            Sources


                                                    R
               PSS


                                                    R


                                                    R


                                         2n                         2n to 1     DACx_output
                                                                                                To Peripherals
                                       Steps                        MUX
                  EN
                                                    R


                                                    R                                                      DACxOUTn


                                                                                                  OEn(1)
                                                    R


            Negative                   VSO URCE-
            Reference
            Sources


               NSS

          Note:   1. The output enable bits are configured so that they act as a one-hot system, meaning only one DAC output
                     can be enabled at a time.


--- p774 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                   DAC - Digital-to-Analog Converter Module -
                                                                                                                        8-Bit
41.1   Output Voltage Selection
       The DAC has 2n voltage level ranges, where n is the number of bits in DACR. Each level is determined
       by the DACxR bits. The DAC output voltage can be determined by using Equation 41-1.

       Equation 41-1. DAC Output Equation

       DACx_output =      VREF + − VREF − × DACR + VREF −
                                             2n

41.2   Ratiometric Output Level
       The DAC output value is derived using a resistor ladder with each end of the ladder tied to a positive
       and negative voltage reference input source. If the voltage of either input source fluctuates, a similar
       fluctuation will result in the DAC output value.
       The value of the individual resistors within the ladder can be found in the “Electrical
       Specifications” chapter for each respective device.

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


--- p775 ---
                                                                                                                           PIC18F27/47/57Q43
                                                                                                    DAC - Digital-to-Analog Converter Module -
                                                                                                                                         8-Bit
41.5.1 DACxCON

            Name:       DACxCON
            Address:    0x7F

            Digital-to-Analog Converter Control Register

      Bit        7             6                5               4                   3                 2                 1           0
                EN                                   OE[1:0]                             PSS[1:0]                                  NSS
  Access        R/W                            R/W             R/W                 R/W              R/W                            R/W
   Reset         0                              0               0                   0                0                              0

Bit 7 – EN DAC Enable
            Value      Description
            1          DAC is enabled
            0          DAC is disabled

Bits 5:4 – OE[1:0] DAC Output Enable
                                         OE                                                               DAC Outputs
                                         11                                                     DACxOUT is disabled
                                         10                                               DACxOUT is enabled on pin RA2 only
                                         01                                               DACxOUT is enabled on pin RB7 only
                                         00                                                     DACxOUT is disabled

Bits 3:2 – PSS[1:0] DAC Positive Reference Selection
                                         PSS                                                    DAC Positive Reference
                                         11                                                         Reserved, do not use
                                         10                                                             FVR Buffer 2
                                         01                                                                VREF+
                                         00                                                                 VDD

Bit 0 – NSS DAC Negative Reference Selection
                                     NSS                                                        DAC Negative Reference
                                         1                                                                   VREF-
                                         0                                                                    VSS


--- p776 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                     DAC - Digital-to-Analog Converter Module -
                                                                                                                          8-Bit
41.5.2 DACxDATL

            Name:       DACxDATL
            Address:    0x7D

            Digital-to-Analog Converter Data Register

      Bit        7            6           5              4            3                   2           1              0
                                                           DACxR[7:0]
  Access        R/W         R/W          R/W            R/W         R/W              R/W             R/W            R/W
   Reset         0           0            0              0            0               0               0              0

Bits 7:0 – DACxR[7:0] Data Input Bits for DAC Value


--- p777 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                          DAC - Digital-to-Analog Converter Module -
                                                                                                                               8-Bit
41.6      Register Summary - DAC
Address     Name      Bit Pos.   7         6           5             4                3               2         1           0
 0x7D      DAC1DATL     7:0                                              DAC1R[7:0]
 0x7E      Reserved
 0x7F      DAC1CON      7:0      EN                        OE[1:0]                         PSS[1:0]                        NSS


--- p778 ---
