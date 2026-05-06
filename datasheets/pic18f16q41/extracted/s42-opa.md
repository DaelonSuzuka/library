42.   OPA - Operational Amplifier
      The Operational Amplifier (OPA) module features a standard general purpose three-terminal device
      with programmable gain options, adjustable input offset voltage and hardware override control
      capabilities. The OPA module has the following features:
      •     5.5 MHz Gain Bandwidth
              – Dedicated external output (OPAxOUT)
               – Multiple noninverting input pins available (OPAxIN+)
               – Multiple inverting input pins available (OPAxIN-)
      •     Programmable Gain Options Using Built-in Internal Resistor Ladder
      •     Configurable Positive and Negative Source Selections
      •     Hardware Controlled Drive with Override Controls
             – Forced Unity Gain mode
               – Forced Rail Drive mode
      •     Programmable Input Offset Voltage Calibration
      •     Internal Connection to the ADC Module
              – Allows OPA to be used as programmable gain amplifier for the ADC Input

      Figure 42-1. Operational Amplifier Module Block Diagram
                                                           R1         R2


                                                                      NCH


                                                                                                     FMS
                                                                 Reserved     111
                  VSS         111
                                            RESON = 1


                                                                 Reserved     110
            Reserved          110                                                           00       No Connection
                                                                DAC2_OUT      101
            Reserved          101                                                           01       VDD
                                                                DAC1_OUT      100
            Reserved          100                                                           10
                                                                 Reserved     011
          OPAxIN3- (1)        011                                                           11       Reserved
                                                                              010
          OPAxIN2- (1)        010         RESON = 0
                                                                              001
          OPAxIN1- (1)        001
                                                           No Connection      000
                     (1)
          OPAxIN0-            000

                      NSS                                                                        1         OPAxIN-   -
                                                                                                 0
                                                                 Reserved     111                                        OPAx                 OPAxOUT
                                                                 Reserved     110                          OPAxIN+
                                    PSS                                                      UG
                                                                                                                     +
                                                                DAC2_OUT      101
                                                                DAC1_OUT      100                                        EN
                       OPAxIN3+ (1)       11
                                  (1)
                                                                   VDD / 2    011
                       OPAxIN2+           10
                                                                              010
                       OPAxIN1+ (1)       01
                                                                              001
                       OPAxIN0+   (1)     00
                                                                      VSS     000


                                                                       PCH

      Note:
      1. Refer to the “Pin Allocation Table” for details about OPAxIN- and OPAxIN+ availability per port.


--- p764 ---
42.1   OPA Module Control
       The OPA module is enabled by setting the EN bit of the corresponding operational amplifier
       Configuration register. Once enabled, the OPA module forces the output driver of the output pin
       (OPAxOUT) into tri-state. Forcing the output pin into tri-state prevents contention between the
       digital PORT driver of the pin and the output of the OPA during operation. The Software Output
       Control (SOC) bits are used to select the OPA mode of operation when hardware controlled override
       is not being used (OREN = 0).

42.1.1 Programmable Source Selection
       The noninverting input source of the OPA module is selected using the PCH bits and can be
       connected to multiple internal sources or to an external input pin (OPAxIN+). If an external pin is
       chosen as the noninverting input source, the PSS bits may then be used to select from the available
       OPA noninverting input pins for the device.
       The inverting input source of the OPA module is selected using the NCH bits and can be connected
       to multiple internal sources or to an external input pin (OPAxIN-). If an external pin is chosen as
       the inverting input source, the NSS bits may then be used to select from the available inverting OPA
       input pins for the device.

42.1.2 Programmable Gain Options
       The gain of the OPA module can be controlled either using external components to provide
       feedback, or internally using a built-in resistor ladder. When using the built-in programmable gain
       options of the OPA module, the internal resistor ladder must be enabled by setting the RESON bit.
       Once enabled, the nominal gain of the amplifier can be selected using the GSEL bits.
       The internal sources to the operational amplifier must be configured based on the OPA mode of
       operation, when using the built-in programmable gain options. The PCH and NCH bits can be used
       to connect the internal resistor ladder to the positive or negative input of the operational amplifier,
       respectively, creating the feedback network needed to control the gain of the circuit.

42.1.3 Unity Gain Mode
       The OPA module can be configured to operate in Unity Gain mode either in software or hardware,
       depending on the configuration of the Override Enable (OREN) bit. If the OREN bit has not been set,
       Unity Gain mode can be enabled in software by setting the Unity Gain Enable (UG) bit. Once Unity
       Gain mode has been enabled, the output of the OPA will be connected internally to the inverting
       input and the OPA will operate with unity gain feedback. If hardware-controlled override has been
       enabled by setting the OREN bit, the OPAxHWC register might be used to configure the OPA mode of
       operation, depending on the status of the override source. Refer to the Hardware Override Control
       section for more information.


                   Tip: Operating the OPA module in Unity Gain mode (software-controlled or hardware-
                   controlled) relinquishes the need for an external inverting input pin (OPAxIN-), since it
                   connects internally to the OPA output, which allows that pin to be used for general purpose
                   I/O.


42.2   Hardware Override Control
       The OPA mode of operation can be switched core independently, using the hardware override
       control feature built into the peripheral. Hardware override control is enabled by setting the OREN
       bit and selecting an override source using the ORS bits. The OPA mode of operation is determined
       based on the level of the selected override signal. The Hardware Override Control Configuration bits
       (HWCH and HWCL) are used to select the OPA mode of operation, when the override source is high
       or low, respectively. The ORPOL bit can be used to invert the hardware controlled override input,


--- p765 ---
        meaning that when ORPOL = 1, the HWCH bits will determine the OPA mode of operation when
        the override source is low, and the HWCL bits will determine the OPA mode of operation when the
        override source is high. The hardware override control can be used to switch between the following
        OPA configurations:
        •   Basic Operation with User Defined Feedback(1)
        •   Unity Gain Mode
        •   Rail Drive Mode
             – Forces the operational amplifier output to be driven to VDD or VSS, depending on the status of
                 the override source and the configured override polarity.
        Note:
        1. Feedback is based on the configuration of the internal gain options (GSEL) or external
           components, depending upon peripheral setup.

42.3    Input Offset Voltage
        Input offset voltage is a measure of the voltage difference between the noninverting and inverting
        input sources in a closed loop circuit, with the operational amplifier operating in its linear region.
        The offset voltage will appear as a DC offset in the output equal to the input offset voltage,
        multiplied by the gain of the circuit. The input offset voltage is also affected by the Common-mode
        voltage. The OPA module is factory calibrated to minimize the input offset voltage.

42.3.1 Offset Calibration
        The OPAxOFFSET register can be used to recalibrate or adjust the input offset voltage from
        the factory calibration. This can be accomplished by using the DAC module or an external
        constant-voltage source, in conjunction with the ADC module. The OPA input offset voltage can
        be recalibrated using the following steps:
        •   Configure the DAC module to be used as a constant voltage reference connected to the
            noninverting input (OPAxIN+) of the OPA module.
             – An external constant voltage reference can be used, instead of the DAC, by connecting it to
                one of the external noninverting input pins.
        •   Configure the OPA module to operate in Unity Gain mode by setting the UG bit.
             – Use the PCH bits to connect the calibration source (either the DAC module or an external
               voltage reference) to the noninverting input (OPAxIN+) of the OPA.
             – If using an external voltage reference, the PSS must also be used to select which OPAxIN+ pin
               will be connected to the noninverting input.
        •   Perform an ADC conversion to measure the voltage of the selected calibration source. The value
            read by the ADC during this conversion will serve as the calibration target.
        •   Use the ADC Positive Channel Selection (ADPCH) register to select the OPA output (OPAxOUT),
            and then measure the output voltage of the OPA module using the ADC.
        •   The difference between the measured value of the calibration target and the measured value of
            the OPA output can be used to determine the value needed to calibrate the OPA input offset
            voltage using the OPAxOFFSET register.


--- p766 ---
                    Important:
                    1. The OPA input offset voltage is factory calibrated, and any data written to the
                       OPAxOFFSET register will adjust the input offset voltage from the factory calibrated
                       value. The factory calibrated input offset voltage will be restored on a Reset event,
                       overwriting any previous data that may have been written to the register.
                    2. The OPAxOFFSET register stores an unsigned value which can be use to optimize both
                       positive and negative offset voltages.


42.4   OPA Operation with ADC
       The OPA module provides internal connections directly to the ADC, allowing it to be used for analog
       signal conditioning before a signal is converted by the ADC. In this mode of operation, the output
       of the OPA (OPAxOUT) will connect internally to the input of the ADC, and any ADC conversions will
       be performed on that signal. When using this mode of operation, the ADPCH register of the ADC
       module may be used to select one of the available noninverting OPA input pins (OPAxIN+) Both the
       ADC and the OPA module must be configured accordingly to use this mode of operation.


                    Tip:
                    1. When using the OPA module with the ADC in this mode of operation, the OPA input
                        pin selection determined using the ADC input channel selection registers will take
                        precedence over the input pin selection using the NSS and PSS bits.
                    2. Although the output of the OPA (OPAxOUT) is connected internally to the ADC in this
                       mode of operation, the OPAxOUT pin cannot be used as a general purpose I/O at this
                       time.


42.5   Register Definitions: Operational Amplifier
       Long bit name prefixes for the OPA peripherals are shown in the table below. Refer to the “Long Bit
       Names” section in the “Register and Bit Naming Conventions” chapter for more information.

       Table 42-1. Operational Amplifier Long Bit Name Prefixes
                         Peripheral                                              Bit Name Prefix
                           OPA1                                                          OPA1


--- p767 ---
42.5.1 OPAxCON0

            Name:       OPAxCON0
            Address:    0xA3

            Operational Amplifier Control Register 0

      Bit        7              6              5               4                   3           2               1               0
                EN                           CPON                                 UG                               SOC[1:0]
  Access        R/W                           R/W                                 R/W                        R/W              R/W
   Reset         0                             0                                   0                          0                0

Bit 7 – EN Operational Amplifier Enable
            Value      Description
            1          Operational amplifier is enabled
            0          Operational amplifier is disabled and consumes no active power

Bit 5 – CPON Charge Pump On Control
            Value      Description
            1          OPA Charge Pump on
            0          OPA Charge Pump off (Low Power mode)

Bit 3 – UG Operational Amplifier Unity Gain Select
            Value      Description
            1          Operational amplifier output is connected to inverting input, OPAxIN- input pins are available for general
                       purpose I/O.
            0          Inverting input is connected to designated OPAxIN- pin.

Bits 1:0 – SOC[1:0] Software Output Control
            Value      Description
            11         Reserved
            10         Drive output to VDD
            01         Drive output to VSS
            00         Basic Operation; Operational amplifier configuration with user-defined or unity-gain feedback


--- p768 ---
42.5.2 OPAxCON1

            Name:              OPAxCON1
            Address:           0xA4

            Operational Amplifier Control Register 1

      Bit           7                  6               5                4                3                2               1                0
                                                    GSEL[2:0]                          RESON                           NSS[2:0]
  Access                             R/W              R/W            R/W                R/W              R/W            R/W               R/W
   Reset                              0                0              0                  0                0               0                0

Bits 6:4 – GSEL[2:0] Operational Amplifier Gain Selection

            Table 42-2. Operational Amplifier Internal Resistor Ladder Selections
                 GSEL[2:0]                    R1                   R2                      Inverting (R2/R1)           Noninverting (1 + R2/R1)
                        111                   1R                  15R                             15                               16
                        110                   2R                  14R                              7                                8
                        101                   4R                  12R                              3                                4
                        100                   6R                  10R                             5/3                              8/3
                        011                   8R                   8R                              1                                2
                        010                  12R                   4R                            1/3                               4/3
                        001                  14R                   2R                            1/7                               8/7
                        000                  15R                   1R                            1/15                             16/15
            Note: R = 20 kΩ nominal

Bit 3 – RESON Resistor Ladder Enable
            Value             Description
            1                 Internal Resistor Ladder is enabled; OPA input is connected to the resistor ladder allowing GSEL to be used to
                              control programmable gain.
            0                 Internal Resistor Ladder is disabled. External feedback to the OPA is required unless operating in Unity Gain
                              mode.

Bits 2:0 – NSS[2:0] Negative Source Selection
                                             Value                                                             Description
                                              111                                                                  VSS
                                              110                                                               Reserved
                                              101                                                               Reserved
                                              100                                                               Reserved
                                              011                                                               OPAxIN3-
                                              010                                                               OPAxIN2-
                                              001                                                               OPAxIN1-
                                              000                                                               OPAxIN0-


--- p769 ---
42.5.3 OPAxCON2

            Name:       OPAxCON2
            Address:    0xA5

            Operational Amplifier Control Register 2

      Bit        7            6             5              4                  3             2             1               0
                                         NCH[2:0]                                                      PCH[2:0]
  Access                    R/W            R/W           R/W                            R/W              R/W             R/W
   Reset                     0              0             0                              0                0               0

Bits 6:4 – NCH[2:0] Operational Amplifier Inverting Input Channel Selection
                                   Value                                                        Description
                                   111                                                        Reserved
                                   110                                                        Reserved
                                   101                                                       DAC2_OUT
                                   100                                                       DAC1_OUT
                                   011                                                        Reserved
                                   010                                                      OPAxIN- (NSS)
                                   001                                             Internal Resistor Ladder (GSEL)
                                   000                                                     No Connection

Bits 2:0 – PCH[2:0] Operational Amplifier Noninverting Input Channel Selection
                                   Value                                                        Description
                                   111                                                        Reserved
                                   110                                                        Reserved
                                   101                                                       DAC2_OUT
                                   100                                                       DAC1_OUT
                                   011                                                          VDD/2
                                   010                                                      OPAxIN+ (PSS)
                                   001                                             Internal Resistor Ladder (GSEL)
                                   000                                                            VSS


--- p770 ---
42.5.4 OPAxCON3

            Name:          OPAxCON3
            Address:       0xA6

            Operational Amplifier Control Register 3

      Bit           7               6            5              4                  3             2                 1               0
                        FMS[1:0]                                                                                       PSS[1:0]
  Access        R/W                R/W                                                                          R/W               R/W
   Reset         0                  0                                                                            0                 0

Bits 7:6 – FMS[1:0] Feedback Mode Selection
            Value         Description
            11            Reserved
            10            Operational Amplifier Output Pin (OPAxOUT)
            01            VDD
            00            No Connection

Bits 1:0 – PSS[1:0] Positive Source Selection
                                         Value                                                       Description
                                          11                                                         OPAxIN3+
                                          10                                                         OPAxIN2+
                                          01                                                         OPAxIN1+
                                          00                                                         OPAxIN0+


--- p771 ---
42.5.5 OPAxHWC

           Name:       OPAxHWC
           Address:    0xA7

           Operational Amplifier Hardware Control Options Register

     Bit        7              6            5                 4                3                 2             1               0
              OREN                       HWCH[2:0]                           ORPOL                          HWCL[2:0]
  Access       R/W           R/W           R/W              R/W               R/W              R/W            R/W             R/W
   Reset        0             0             0                0                 0                0              0               0

Bit 7 – OREN Override Enable
           Value      Description
           1          Hardware Override Control is enabled. OPA mode of operation is configured using the HWCH / HWCL bits.
           0          Hardware Override Control is disabled. OPA mode of operation must be configured in software.

Bits 6:4 – HWCH[2:0] Hardware Control Configuration High
                                    Value                                                            Description
                                     111                                                          Rail Drive to VDD
                                     110                                                              Reserved
                                     101                                                              Reserved
                                     100                                          Basic OPA configuration with unity gain feedback
                                     011                                                              Reserved
                                     010                                                              Reserved
                                     001                                                              Reserved
                                     000                                         Basic OPA configuration with user-defined feedback

Bit 3 – ORPOL Override Source Polarity
           Value      Description
           1          Hardware Control Input is Inverted (Active-Low)
           0          Hardware Control Input is not Inverted (Active-High)

Bits 2:0 – HWCL[2:0] Hardware Control Configuration Low
                                    Value                                                            Description
                                     111                                                          Rail Drive to VSS
                                     110                                                              Reserved
                                     101                                                              Reserved
                                     100                                          Basic OPA configuration with unity gain feedback
                                     011                                                              Reserved
                                     010                                                              Reserved
                                     001                                                              Reserved
                                     000                                         Basic OPA configuration with user-defined feedback


--- p772 ---
42.5.6 OPAxOFFSET

            Name:       OPAxOFFSET
            Address:    0xA8

            Operational Amplifier Input Offset Adjustment Register

      Bit        7            6            5              4            3                   2     1              0
                                                           OFFSET[7:0]
  Access        R/W          R/W          R/W           R/W          R/W              R/W       R/W            R/W
   Reset         m            m            m             m             m               m         m              m

Bits 7:0 – OFFSET[7:0] Operational Amplifier Input Offset Calibration


                        Important: If written by the user, the factory calibrated value of this register will be
                        replaced and can only be restored on a Reset.


            Note: The Reset value ‘m’ is determined by device default locations for that input.


--- p773 ---
42.5.7 OPAxORS

            Name:      OPAxORS
            Address:   0xA9

            Operational Amplifier Override Source Selection Register

      Bit        7            6           5              4                   3        2                 1           0
                                                                                   ORS[4:0]
  Access                                               R/W                  R/W     R/W             R/W            R/W
   Reset                                                0                    0        0              0              0

Bits 4:0 – ORS[4:0] Operational Amplifier Output Override Source Selection
                                  Value                                                   Description
                              10110 - 11111                                                 Reserved
                                  10101                                                    CLC4_OUT
                                  10100                                                    CLC3_OUT
                                  10011                                                    CLC2_OUT
                                  10010                                                    CLC1_OUT
                                  10001                                                    ZCD_OUT
                                  10000                                                    CM2_OUT
                                  01111                                                    CM1_OUT
                                  01110                                                   NCO1_OUT
                                  01101                                                   PWM3_S1P2
                                  01100                                                   PWM3_S1P1
                                  01011                                                   PWM2_S1P2
                                  01010                                                   PWM2_S1P1
                                  01001                                                   PWM1_S1P2
                                  01000                                                   PWM1_S1P1
                                  00111                                                    CCP1_OUT
                                  00110                                                   TMR4_OUT
                                  00101                                                   TMR3_OUT
                                  00100                                                   TMR2_OUT
                                  00011                                                   TMR1_OUT
                                  00010                                                   TMR0_OUT
                                  00001                                                      SOSC
                                  00000                                                    LFINTOSC


--- p774 ---
42.6      Register Summary - Operational Amplifier
Address     Name       Bit Pos.     7            6          5             4            3         2              1              0
 0x00
  ...      Reserved
 0xA2
 0xA3     OPA1CON0       7:0       EN                    CPON                          UG                          SOC[1:0]
 0xA4     OPA1CON1       7:0                            GSEL[2:0]                    RESON                   NSS[2:0]
 0xA5     OPA1CON2       7:0                            NCH[2:0]                                             PCH[2:0]
 0xA6     OPA1CON3       7:0          FMS[1:0]                                                                      PSS[1:0]
 0xA7      OPA1HWC       7:0      OREN                 HWCH[2:0]                      ORPOL                 HWCL[2:0]
 0xA8     OPA1OFFSET     7:0                                                  OFFSET[7:0]
 0xA9      OPA1ORS       7:0                                                                  ORS[4:0]


--- p775 ---
