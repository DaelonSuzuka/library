                       PIC18(L)F26/27/45/46/47/55/56/57K42
35.0     TEMPERATURE INDICATOR                                   35.1.1      TEMPERATURE INDICATOR
         MODULE                                                              RANGE
                                                                 The temperature indicator circuit operates in either high
This family of devices is equipped with a temperature
                                                                 or low range. The high range, selected by setting the
circuit designed to measure the operating temperature
                                                                 TSRNG bit of the FVRCON register, provides a wider
of the silicon die.
                                                                 output voltage. This provides more resolution over the
The circuit’s range of operating temperature falls               temperature range. High range requires a higher-bias
between -40°C and +125°C. A one-point calibration                voltage to operate and thus, a higher VDD is needed.
allows the circuit to indicate a temperature closely             The low range is selected by clearing the TSRNG bit of
surrounding that point. A two-point calibration allows           the FVRCON register. The low range generates a lower
the circuit to sense the entire range of temperature             sensor voltage and thus, a lower VDD voltage is needed
more accurately.                                                 to operate the circuit.
                                                                 The output voltage of the sensor is the highest value at
35.1     Module Operation                                        -40°C and the lowest value at +125°C.
The temperature indicator module consists of a                   High Range: The High range is used in applications
temperature-sensing circuit that provides a voltage to           with the reference for the ADC, VREF = 2.048V. This
the device ADC. The analog voltage output, VMEAS,                range may not be suitable for battery-powered
varies inversely to the device temperature. The output of        applications. The ADC reading (in counts) at 90°C for
the temperature indicator is referred to as VMEAS.               the high range setting is stored in the DIA Table
Figure 35-1 shows a simplified block diagram of the              (Table 5-3) as parameter TSHR2.
temperature indicator module.                                    Low Range: This mode is useful in applications in
                                                                 which the VDD is too low for high-range operation. The
FIGURE 35-1:             TEMPERATURE                             VDD in this mode can be as low as 1.8V. VDD must,
                         INDICATOR MODULE                        however, be at least 0.5V higher than the maximum
                         BLOCK DIAGRAM                           sensor voltage depending on the expected low
                                                                 operating temperature. The ADC reading (in counts) at
                                                                 90°C for the Low range setting is stored in the DIA
                                              5HY'
                                                    


                                                                 Table (Table 5-3) as parameter TSLR2.
                         9''
                                                                 35.1.2      MINIMUM OPERATING VDD
                                                                 When the temperature circuit is operated in low range,
  7651*                                   90($6                  the device may be operated at any operating voltage
                 7HPSHUDWXUH,QGLFDWRU
                      0RGXOH
                                                      7R$'&     that is within specifications. When the temperature
    76(1                                                         circuit is operated in high range, the device operating
                                                                 voltage, VDD, must be high enough to ensure that the
                                                                 temperature circuit is correctly biased.

                         *1'                                     Table 35-1 shows the recommended minimum VDD vs.
                                                                 Range setting.
The output of the circuit is measured using the internal         TABLE 35-1:       RECOMMENDED VDD vs.
Analog-to-Digital Converter. A channel is reserved for                             RANGE
the temperature circuit output. Refer to Section
                                                                   Min.VDD, TSRNG = 1          Min. VDD, TSRNG = 0
36.0 “Analog-to-Digital          Converter         with
                                                                      (High Range)                 (Low Range)
Computation (ADC2) Module” for detailed
information.                                                                2.5                         1.8
The ON/OFF bit for the module is located in the
FVRCON register. See Section 34.0 “Fixed Voltage
Reference (FVR)” for more information. The circuit is
enabled by setting the TSEN bit of the FVRCON
register. When the module is disabled, the circuit draws
no current.
The circuit operates in either High or Low range. Refer
to the next section for more details on the range
settings.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 600
                                          PIC18(L)F26/27/45/46/47/55/56/57K42
35.2            Temperature Calculation                                                                        35.2.1     CALIBRATION
This section describes the steps involved in calculating                                                       35.2.1.1     Higher-Order Calibration
the die temperature, TMEAS:
                                                                                                               If the application requires more precise temperature
1.     Obtain the ADC count value of the measured                                                              measurement, additional calibrations steps will be
       analog voltage: The analog output voltage,                                                              necessary. For these applications, two-point or three-
       VMEAS is converted to a digital count value by                                                          point calibration is recommended.
       the Analog to Digital Converter (ADC) and is
       referred to as ADCMEAS.                                                                                 35.2.2     TEMPERATURE RESOLUTION
2.     Obtain the ADC count value, ADCDIA at 90                                                                The resolution of the ADC reading, Ma (°C/count),
       degrees, from the DIA table. This parameter is                                                          depends on both the ADC resolution N and the
       TSLR2 for the low range setting or TSHR2 for                                                            reference voltage used for conversion, as shown in
       the high range setting of the temperature                                                               Equation 35-1. It is recommended to use the smallest
       indicator module.                                                                                       VREF value, such as the ADC FVR1 Output Voltage for
3.     Obtain the output analog voltage (in mV) value                                                          2x setting (FVRA2X) value from the DIA. Refer to
       of the Fixed Reference Voltage (FVR) for 2x                                                             Table 5-3 for DIA location.
       setting, from the DIA Table. This parameter is
       FVRA2X in the DIA table (Table 5-3).                                                                      Note:    Refer to Table 44-18 for FVR reference
                                                                                                                          voltage accuracy.
4.     Obtain the value of the temperature indicator
       voltage sensitivity, parameter Mv, from Table 44-
       26 for the corresponding range setting.                                                                 35.3      ADC Acquisition Time
Equation 35-1 provides an estimate for the die                                                                 To ensure accurate temperature measurements, the
temperature based on the above parameters.                                                                     user must wait a certain minimum acquisition time
                                                                                                               (parameter TS01 in Table 44-26) for the ADC value to
EQUATION 35-1:                          SENSOR TEMPERATURE                                                     settle, after the ADC input multiplexer is connected to
                                   AD C       – AD C        FVRA2X                                          the temperature indicator output, before the conversion
                                         M EAS        D IA                                                     is performed.
 TM EAS = 90 + --------------------------------------------------------------------------------------------
                                                 N
                                            2 – 1  M v

Where:
ADCMEAS = ADC reading at temperature being
estimated
ADCDIA = ADC reading stored in the DIA
FVRA2X = FVR value stored in the DIA for 2x setting
N = Resolution of the ADC
Mv = Temperature Indicator voltage sensitivity (mV/°C)


     Note:            It is recommended to take the average of
                      10 measurements of ADCmeas to reduce
                      noise and improve accuracy.


TABLE 35-2:                        SUMMARY OF REGISTERS ASSOCIATED WITH THE TEMPERATURE INDICATOR(1)
                                                                                                                                                           Register
      Name                      Bit 7                   Bit 6                   Bit 5                  Bit 4   Bit 3      Bit 2       Bit 1      Bit 0
                                                                                                                                                           on page
FVRCON                            EN                    RDY                    TSEN                 TSRNG       CDAFVR[1:0]             ADFVR[1:0]            600
Legend: — = Unimplemented location, read as ‘0’. Shaded cells are unused by the temperature indicator module.
Note 1: It is recommended to take the average of ten measurements of ADCMEAS to reduce noise and improve
        accuracy.


 2017-2021 Microchip Technology Inc.                                                                                                          DS40001919G-page 601
