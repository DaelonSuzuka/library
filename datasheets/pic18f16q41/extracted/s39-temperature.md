39.    Temperature Indicator Module
       This family of devices is equipped with a temperature circuit designed to measure the operating
       temperature of the silicon die. The temperature indicator module provides a temperature-
       dependent voltage that can be measured by the internal Analog-to-Digital Converter.
       The circuit’s range of operating temperature falls between -40℃ and +125℃. The circuit may be used
       as a temperature threshold detector or a more accurate temperature indicator, depending on the
       level of calibration performed. A one-point calibration allows the circuit to indicate a temperature
       closely surrounding that point. A two-point calibration allows the circuit to sense the entire range of
       temperature more accurately.

39.1   Module Operation
       The temperature indicator module consists of a temperature-sensing circuit that provides a
       corresponding voltage to the device ADC. The analog voltage output varies inversely to the device
       temperature. The output of the temperature indicator is referred to as VMEAS.
       The following figure shows a simplified block diagram of the temperature indicator module.

       Figure 39-1. Temperature Indicator Module Block Diagram

                                                             VDD                     Rev. 10-000069D
                                                                                           11/13/2017


                                         TSRNG                               VMEAS
                                                     Temperature Indicator
                                                           Module
                                                                                     To ADC
                                           TSEN


                                                            GND


       The output of the circuit is measured using the internal Analog-to-Digital Converter. A channel is
       reserved for the temperature circuit output. Refer to the “ADC - Analog-to-Digital Converter with
       Computation Module” chapter for more details.
       The ON/OFF bit for the module is located in the FVRCON register. The circuit is enabled by setting
       the TSEN bit. When the module is disabled, the circuit draws no current. Refer to the “FVR - Fixed
       Reference Voltage” chapter for more details.

39.1.1 Temperature Indicator Range
       The temperature indicator circuit operates in either high or low range. The high range, selected
       by setting the TSRNG bit, provides a wider output voltage. This provides more resolution over the
       temperature range. High range requires a higher bias voltage to operate and thus, a higher VDD is
       needed. The low range is selected by clearing the TSRNG bit. The low range generates a lower sensor
       voltage and thus, a lower VDD voltage is needed to operate the circuit.
       The output voltage of the sensor is the highest value at -40℃ and the lowest value at +125℃.
       • High Range: The high range is used in applications with the reference for the ADC, VREF = 2.048V.
         This range may not be suitable for battery-powered applications.
       •   Low Range: This mode is useful in applications in which the VDD is too low for high-range
           operation. The VDD in this mode can be as low as 1.8V. However, VDD must be at least 0.5V higher
           than the maximum sensor voltage depending on the expected low operating temperature.


--- p705 ---
                    Important: The standard parameters for the Temperature Sensor for both high range and
                    low range are stored in the DIA table. Refer to the DIA table in the “Memory Organization”
                    chapter for more details.


39.1.2 Minimum Operating VDD
       When the temperature circuit is operated in low range, the device may be operated at any operating
       voltage that is within the device specifications. When the temperature circuit is operated in high
       range, the device operating voltage, VDD, must be high enough to ensure that the temperature circuit
       is correctly biased.
       The following table shows the recommended minimum VDD vs. Range setting.

       Table 39-1. Recommended VDD vs. Range
                   Min. VDD, TSRNG = 1 (High Range)                             Min. VDD, TSRNG = 0 (Low Range)
                                  ≥ 2.5                                                      ≥ 1.8


39.2   Temperature Calculation
       This section describes the steps involved in calculating the die temperature, TMEAS:
       1. Obtain the ADC count value of the measured analog voltage: The analog output voltage, VMEAS, is
           converted to a digital count value by the Analog-to-Digital Converter (ADC) and is referred to as
           ADCMEAS.
       2. Obtain the Gain value from the DIA table. This parameter is TSLR1 for the low range setting or
          TSHR1 for the high range setting of the temperature indicator module. Refer to the DIA table in
          the “Memory Organization” chapter for more details.
       3. Obtain the Offset value from the DIA table. This parameter is TSLR3 for the low range setting or
          TSHR3 for the high range setting of the temperature indicator module. Refer to the DIA table in
          the “Memory Organization” chapter for more details.
       The following equation provides an estimate for the die temperature based on the above
       parameters:

       Equation 39-1. Sensor Temperature (in ℃)
                 ADCMEAS × Gain
                     256           + Offset
       TMEAS =
                            10

       Where:
       ADCMEAS = ADC reading at temperature being estimated
       Gain = Gain value stored in the DIA table
       Offset = Offset value stored in the DIA table
       Note: It is recommended to take the average of ten measurements of ADCMEAS to reduce noise and
       improve accuracy.

               Example 39-1. Temperature Calculation (C)

                 // offset is int16_t data type
                 // gain is int16_t data type
                 // ADC_MEAS is uint16_t data type
                 // Temp_in_C is int24_t data type

                 ADC_MEAS = ((ADRESH << 8) + ADRESL);               // Store the ADC Result
                 Temp_in_C = (int24_t)(ADC_MEAS) * gain;            // Multiply the ADC Result by
                                                                    // Gain and store the result in a
                                                                    // signed variable


--- p706 ---
                Temp_in_C = Temp_in_C / 256;                   // Divide (ADC Result * Gain) by 256
                Temp_in_C = Temp_in_C + offset;                // Add (Offset) to the result
                Temp_in_C = Temp_in_C / 10;                    // Divide the result by 10 and store
                                                               // the calculated temperature


39.2.1 Higher-Order Calibration
       If the application requires more precise temperature measurement, additional calibrations steps
       will be necessary. For these applications, two-point or three-point calibration is recommended. For
       additional information on two-point calibration method, refer to the following Microchip application
       note, available at the corporate website (www.microchip.com):
       • AN2798, “Using the PIC16F/PIC18F Ground Referenced Temperature Indicator Module”

39.3   ADC Acquisition Time
       To ensure accurate temperature measurements, the user must wait a certain minimum acquisition
       time (parameter TS01) after the temperature indicator output is selected as ADC input. This is
       required for the ADC sampling circuit to settle before the conversion is performed.
       Note: Parameter TS01 can be found in the Temperature Indicator Requirements table of the
       “Electrical Specifications” chapter.

39.4   Register Definitions: Temperature Indicator


--- p707 ---
39.4.1 FVRCON

            Name:       FVRCON
            Address:    0x3D7

            FVR Control Register


                        Important: This register is shared between the Fixed Voltage Reference (FVR) module and
                        the temperature indicator module.


      Bit        7             6                5               4                3             2        1           0
                EN            RDY             TSEN            TSRNG                CDAFVR[1:0]           ADFVR[1:0]
  Access        R/W            R              R/W              R/W              R/W          R/W      R/W         R/W
   Reset         0             q                0               0                0             0       0            0

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


--- p708 ---
Notes:
1. This output goes to the DAC and comparator modules and to the ADC module as an input
   channel only.
2. This output goes to the ADC module as a reference and as an input channel.
3. Fixed Voltage Reference output cannot exceed VDD.


--- p709 ---
39.5      Register Summary - Temperature Indicator
Address     Name      Bit Pos.   7         6           5             4         3              2            1                0
 0x00
  ...      Reserved
0x03D6
0x03D7      FVRCON      7:0      EN       RDY        TSEN        TSRNG          CDAFVR[1:0]                    ADFVR[1:0]


--- p710 ---
