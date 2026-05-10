                      PIC18(L)F26/27/45/46/47/55/56/57K42
34.0       FIXED VOLTAGE REFERENCE                         The ADFVR[1:0] bits of the FVRCON register are used
                                                           to enable and configure the gain amplifier settings for
          (FVR)
                                                           the reference supplied to the ADC module. Reference
The Fixed Voltage Reference, or FVR, is a stable           Section 36.0 “Analog-to-Digital Converter with
voltage reference, independent of VDD, with 1.024V,        Computation (ADC2) Module” for additional
2.048V or 4.096V selectable output levels. The output      information.
of the FVR can be configured to supply a reference         The CDAFVR[1:0] bits of the FVRCON register are
voltage to the following:                                  used to enable and configure the gain amplifier settings
• ADC input channel                                        for the reference supplied to the DAC and comparator
• ADC positive reference                                   module. Reference Section 37.0 “5-Bit Digital-to-
                                                           Analog Converter (DAC) Module” and Section
• Comparator input
                                                           38.0 “Comparator Module” for additional information.
• Digital-to-Analog Converter (DAC)
The FVR can be enabled by setting the EN bit of the        34.2      FVR Stabilization Period
FVRCON register.
                                                           When the Fixed Voltage Reference module is enabled, it
  Note:     Fixed Voltage Reference output cannot          requires time for the reference and amplifier circuits to
            exceed VDD.                                    stabilize. Once the circuits stabilize and are ready for use,
                                                           the RDY bit of the FVRCON register will be set.

34.1      Independent Gain Amplifiers
The output of the FVR, which is connected to the ADC,
Comparators, and DAC, is routed through two
independent programmable gain amplifiers. Each
amplifier can be programmed for a gain of 1x, 2x or 4x,
to produce the three possible voltage levels.


FIGURE 34-1:           VOLTAGE REFERENCE BLOCK DIAGRAM

                                                                                                            Rev. 10-000053E
                                                                                                                   1/27/2017


                                        2
              ADFVR<1:0>

                                                     1x
                                                                            FVR Buffer 1
                                                     2x
                                                     4x                     (To ADC Module)

                                        2
              CDAFVR<1:0>

                                                     1x                     FVR Buffer 2
                                                     2x                     (To ADC, Comparator
                                                     4x                     and DAC Modules)


               EN
                                               +
                                               _          RDY
   Any peripheral
  requiring Fixed
      Reference


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 598
                        PIC18(L)F26/27/45/46/47/55/56/57K42
34.3      Register Definitions: FVR Control

REGISTER 34-1:            FVRCON: FIXED VOLTAGE REFERENCE CONTROL REGISTER
   R/W-0/0            R-q/q             R/W-0/0        R/W-0/0         R/W-0/0       R/W-0/0          R/W-0/0      R/W-0/0
                            (1)                (3)             (3)
        EN           RDY                TSEN           TSRNG                 CDAFVR[1:0]                   ADFVR[1:0]
bit 7                                                                                                                     bit 0


Legend:
R = Readable bit                    W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                    ‘0’ = Bit is cleared             q = Value depends on condition


bit 7              EN: Fixed Voltage Reference Enable bit
                   1 = Fixed Voltage Reference is enabled
                   0 = Fixed Voltage Reference is disabled
bit 6              RDY: Fixed Voltage Reference Ready Flag bit(1)
                   1 = Fixed Voltage Reference output is ready for use
                   0 = Fixed Voltage Reference output is not ready or not enabled
bit 5              TSEN: Temperature Indicator Enable bit(3)
                   1 = Temperature Indicator is enabled
                   0 = Temperature Indicator is disabled
bit 4              TSRNG: Temperature Indicator Range Selection bit(3)
                   1 = VOUT = 3VT (High Range)
                   0 = VOUT = 2VT (Low Range)
bit 3-2            CDAFVR[1:0]: FVR Buffer 2 Gain Selection bits
                   11 = FVR Buffer 2 Gain is 4x, (4.096V)(2)
                   10 = FVR Buffer 2 Gain is 2x, (2.048V)(2)
                   01 = FVR Buffer 2 Gain is 1x, (1.024V)
                   00 = FVR Buffer 2 is off
bit 1-0            ADFVR[1:0]: FVR Buffer 1 Gain Selection bit
                   11 = FVR Buffer 1 Gain is 4x, (4.096V)(2)
                   10 = FVR Buffer 1 Gain is 2x, (2.048V)(2)
                   01 = FVR Buffer 1 Gain is 1x, (1.024V)
                   00 = FVR Buffer 1 is off

Note 1:      RDY is always ‘1’.
     2:      Fixed Voltage Reference output cannot exceed VDD.
     3:      See Section 35.0 “Temperature Indicator Module” for additional information.


TABLE 34-1:         SUMMARY OF REGISTERS ASSOCIATED WITH FIXED VOLTAGE REFERENCE
                                                                                                                    Register
    Name            Bit 7         Bit 6        Bit 5       Bit 4     Bit 3       Bit 2       Bit 1         Bit 0
                                                                                                                    on page
FVRCON               EN           RDY        TSEN      TSRNG           CDAFVR[1:0]              ADFVR[1:0]              600
Legend: — = Unimplemented location, read as ‘0’. Shaded cells are not used with the Fixed Voltage Reference.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 599
