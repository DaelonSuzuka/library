                                                                                                                 PIC18F27/47/57Q43
                                                                                                       FVR - Fixed Voltage Reference


38.    FVR - Fixed Voltage Reference
       The Fixed Voltage Reference (FVR) is a stable voltage reference, independent of VDD, with 1.024V,
       2.048V or 4.096V selectable output levels. The output of the FVR can be configured to supply a
       reference voltage to analog peripherals such as those listed below.
       •   ADC input channel
       •   ADC positive reference
       •   Comparator input
       •   Digital-to-Analog Converter (DAC)
       The FVR can be enabled by setting the EN bit to ‘1’.
       Note: Fixed Voltage Reference output cannot exceed VDD.

38.1   Independent Gain Amplifiers
       The output of the FVR is routed through two independent programmable gain amplifiers. Each
       amplifier can be programmed for a gain of 1x, 2x or 4x, to produce the three possible voltage levels.
       The ADFVR bits are used to enable and configure the gain amplifier settings for the reference
       supplied to the ADC module. Refer to the “ADC - Analog-to-Digital Converter with Computation
       Module” chapter for additional information.
       The CDAFVR bits are used to enable and configure the gain amplifier settings for the reference
       supplied to the DAC and comparator modules. Refer to the “DAC - Digital-to-Analog Converter
       Module” and “CMP - Comparator Module” chapters for additional information.
       Refer to the figure below for the block diagram of the FVR module.

       Figure 38-1. Fixed Voltage Reference Block Diagram

                                            ADFVR

                                                                  1x                To ADC module
                                                                  2x                as reference and
                                                                  4x                input channel
                                                                  FVR Buffer 1
                                           CDAFVR
                                                                                    To DAC and
                                                                  1x
                                                                                    Comparator modules,
                                                                  2x
                                                                  4x                To ADC module as
                                                                                    input channel only
                                                                  FVR Buffer 2

                                           EN                 +
                                                              _         RDY
                                Any peripheral
                                requiring Fixed
                                    Reference


38.2   FVR Stabilization Period
       When the Fixed Voltage Reference module is enabled, it requires time for the reference and
       amplifier circuits to stabilize. Once the circuits stabilize and are ready for use, the RDY bit will be
       set.

38.3   Register Definitions: FVR
       Long bit name prefixes for the FVR peripherals are shown in the following table. Refer to the “Long
       Bit Names” section in the “Register and Bits Naming Conventions” chapter for more information.


--- p719 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                        FVR - Fixed Voltage Reference

Table 38-1. FVR Long Bit Name Prefixes
                  Peripheral                                              Bit Name Prefix
                     FVR                                                          FVR


--- p720 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                                   FVR - Fixed Voltage Reference

38.3.1 FVRCON

            Name:       FVRCON
            Address:    0x3D7

            FVR Control Register


                        Important: This register is shared between the Fixed Voltage Reference (FVR)
                        module and the temperature indicator module.


      Bit        7             6                5               4                3             2       1           0
                EN            RDY             TSEN            TSRNG                CDAFVR[1:0]          ADFVR[1:0]
  Access        R/W            R              R/W              R/W              R/W          R/W     R/W         R/W
   Reset         0             q                0               0                0             0      0            0

Bit 7 – EN Fixed Voltage Reference Enable
            Value      Description
            1          Enables module
            0          Disables module

Bit 6 – RDY Fixed Voltage Reference Ready Flag
            Value      Description
            1          Fixed Voltage Reference output is ready for use
            0          Fixed Voltage Reference output is not ready for use or not enabled

Bit 5 – TSEN Temperature Indicator Enable
            Value      Description
            1          Temperature Indicator is enabled
            0          Temperature Indicator is disabled

Bit 4 – TSRNG Temperature Indicator Range Selection
            Value      Description
            1          VOUT = 3VT (High Range)
            0          VOUT = 2VT (Low Range)

Bits 3:2 – CDAFVR[1:0] FVR Buffer 2 Gain Selection(1)
            Value      Description
            11         FVR Buffer 2 Gain is 4x, (4.096V)(3)
            10         FVR Buffer 2 Gain is 2x, (2.048V)(3)
            01         FVR Buffer 2 Gain is 1x, (1.024V)
            00         FVR Buffer 2 is OFF

Bits 1:0 – ADFVR[1:0] FVR Buffer 1 Gain Selection(2)
            Value      Description
            11         FVR Buffer 1 Gain is 4x, (4.096V)(3)
            10         FVR Buffer 1 Gain is 2x, (2.048V)(3)
            01         FVR Buffer 1 Gain is 1x, (1.024V)
            00         FVR Buffer 1 is OFF

            Notes:
            1. This output goes to the DAC and comparator modules and to the ADC module as an input
               channel only.
            2. This output goes to the ADC module as a reference and as an input channel.
            3. Fixed Voltage Reference output cannot exceed VDD.


--- p721 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                                 FVR - Fixed Voltage Reference

38.4      Register Summary - FVR
Address     Name     Bit Pos.   7         6           5             4         3              2            1                0
0x03D7      FVRCON     7:0      EN       RDY        TSEN        TSRNG          CDAFVR[1:0]                    ADFVR[1:0]


--- p722 ---
