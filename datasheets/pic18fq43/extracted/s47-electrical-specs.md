                                                                                                       PIC18F27/47/57Q43
                                                                                                    Electrical Specifications


47.    Electrical Specifications
47.1   Absolute Maximum Ratings(†)
       Parameter                                                                         Rating
       Ambient temperature under bias                                                    -40°C to +125°C
       Storage temperature                                                               -65°C to +150°C
       Voltage on pins with respect to VSS
       •   on VDD pin:                                                                   -0.3V to +6.5V

       •   on MCLR pin:                                                                  -0.3V to +9.0V

       •   on all other pins:                                                            -0.3V to (VDD + 0.3V)

       Maximum current(1)
       •   on VSS pin                                      -40°C ≤ TA ≤ +85°C            350 mA
                                                           85°C < TA ≤ +125°C            120 mA
       •   on VDD pin (28-pin devices)                     -40°C ≤ TA ≤ +85°C            250 mA
                                                           85°C < TA ≤ +125°C            85 mA
       •   on VDD pin (40-pin devices)                     -40°C ≤ TA ≤ +85°C            350 mA
                                                           85°C < TA ≤ +125°C            120 mA
       •   on any standard I/O pin                                                       ±50 mA

       Clamp current, IK (VPIN < 0 or VPIN > VDD)                                        ±20 mA
       Total power dissipation(2)                                                        800 mW

       Notes:
       1. Maximum current rating requires even load distribution across I/O pins. Maximum current rating
          may be limited by the device package power dissipation characterizations. See the Thermal
          Characteristics section to calculate device specifications.
       2. Power dissipation is calculated as follows:
          PDIS = VDD x {IDD - Σ IOH} + Σ {(VDD - VOH) x IOH} + Σ (VOI x IOL)
       3. Internal Power Dissipation is calculated as follows:
          PINTERNAL = IDD x VDD

           where IDD is current to run the chip alone without driving any load on the output pins.
       4. I/O Power Dissipation is calculated as follows:
          PI/O = Σ(IOL*VOL)+Σ(IOH*(VDD-VOH))
       5. Derated Power is calculated as follows:
          PDER = PDMAX(TJ-TA)/θJA

           where TA = Ambient Temperature, TJ = Junction Temperature.


                    Stresses above those listed under the “Absolute Maximum Ratings” section may
                    cause permanent damage to the device. This is a stress rating only and functional
                    operation of the device at those or any other conditions above those indicated
                    in the operation listings of this specification is not implied. Exposure above
                    maximum rating conditions for extended periods may affect device reliability.


--- p891 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                                    Electrical Specifications

47.2   Standard Operating Conditions
       The standard operating conditions for any device are defined as:
       Operating Voltage:                                           VDDMIN ≤ VDD ≤ VDDMAX
       Operating Temperature:                                       TA_MIN ≤ TA ≤ TA_MAX

       Parameter                                                                                       Ratings
       VDD — Operating Supply Voltage(1)                                                   VDDMIN      +1.8V
                                                                                           VDDMAX      +5.5V
       TA — Operating Ambient Temperature Range
       Industrial Temperature                                                              TA_MIN      -40°C
                                                                                           TA_MAX      +85°C
       Extended Temperature                                                                TA_MIN      -40°C
                                                                                           TA_MAX      +125°C

       Note:
       1. See the Parameter Supply Voltage for more details.

       Figure 47-1. Voltage Frequency Graph, -40°C ≤ TA ≤ +125°C


       Notes:
       • The shaded region indicates the permissible combinations of voltage and frequency.
       •   Refer to the “External Clock/Oscillator Timing Requirements” table for each Oscillator mode’s
           supported frequencies.


--- p892 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                               Electrical Specifications

47.3   DC Characteristics
47.3.1 Supply Voltage
       Table 47-1. Supply Voltage
        Standard Operating Conditions (unless otherwise stated)
         Param. No.           Sym.         Characteristic       Min.          Typ.†       Max.         Units          Conditions
        Supply Voltage
        D002            VDD                                     1.8            —           5.5             V

        RAM Data Retention(1)
        D003            VDR                                     1.7            —           —               V      Device in Sleep
                                                                                                                  mode
        Power-on Reset Release Voltage(2)
        D004            VPOR                                     —             1.6         —               V      BOR and LPBOR
                                                                                                                  disabled(3)
        Power-on Reset Rearm Voltage(2)
        D005            VPORR                                    —             1           —               V      BOR and LPBOR
                                                                                                                  disabled(3)
        VDD Rise Rate to ensure internal Power-on Reset signal(2)
        D006            SVDD                                    0.05           —           —           V/ms       BOR and LPBOR
                                                                                                                  disabled(3)
        † Data in “Typ.” column is at 3.0V, 25℃ unless otherwise stated. These parameters are for design guidance only and are not
        tested.
        Notes:
        1.   This is the limit to which VDD can be lowered in Sleep mode without losing RAM data.
        2.   See the following figure, POR and POR REARM with Slow Rising VDD.
        3.   See Reset, WDT, Oscillator Start-up Timer, Brown-Out Reset and Low-Power Brown-Out Reset Specifications for BOR and
             LPBOR trip point information.


       Figure 47-2. POR and POR Rearm with Slow Rising VDD
                                     VDD


                                 VPOR
                                VPORR
                                                                                                    SVDD

                                  VSS
                               NPOR(1)


                                                                       POR REARM


                                     VSS


                                                                 TVLOW(3)               TPOR(2)
       Notes:
       1. When NPOR is low, the device is held in Reset.
       2. TPOR 1 μs typical.
       3. TVLOW 2.7 μs typical.


--- p893 ---
                                                                                                                            PIC18F27/47/57Q43
                                                                                                                         Electrical Specifications

47.3.2 Supply Current (IDD)(1)
        Table 47-2. Supply Current
         Standard Operating Conditions (unless otherwise stated)
         Param. No.            Sym.               Device             Min.           Typ.†           Max.        Units           Conditions
                                               Characteristics
                                                                                                                           VDD          Note
         D100             IDDXT4           XT = 4 MHz                  —            640             870          μA        3.0V
         D100A            IDDXT4           XT = 4 MHz                  —            490             700          μA        3.0V      All PMD
                                                                                                                                     bits are
                                                                                                                                     '1'
         D101             IDDHFO16         HFINTOSC = 16 MHz           —             2              2.5         mA         3.0V
         D101A            IDDHFO16         HFINTOSC = 16 MHz           —             1.5            1.9         mA         3.0V      All PMD
                                                                                                                                     bits are
                                                                                                                                     '1'
         D102             IDDHFO64         HFINTOSC = 64 MHz           —             6.7            8.2         mA         3.0V
         D102A            IDDHFO64         HFINTOSC = 64 MHz           —             4.5            5.4         mA         3.0V      All PMD
                                                                                                                                     bits are
                                                                                                                                     '1'
         D103             IDDHSPLL64       HS+PLL = 64 MHz             —             5.6            13.8        mA         3.0V
         D103A            IDDHSPLL64       HS+PLL = 64 MHz             —             3.8            11.5        mA         3.0V      All PMD
                                                                                                                                     bits are
                                                                                                                                     '1'
         D104             IDDIDLE          Idle mode, HFINTOSC         —             1.4            1.8         mA         3.0V
                                           = 16 MHz
         D105             IDDDOZE(3)       Doze mode,                  —             1.5            1.9         mA         3.0V
                                           HFINTOSC = 16 MHz,
                                           Doze Ratio = 16
         † Data in “Typ.” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
         tested.
         Notes:
         1.   The test conditions for all IDD measurements in Active Operation mode are: OSC1 = external square wave, from
              rail-to-rail; all I/O pins are outputs driven low; MCLR = VDD; WDT disabled.
         2.   The supply current is mainly a function of the operating voltage and frequency. Other factors, such as I/O pin loading
              and switching rate, oscillator type, internal code execution pattern and temperature, also have an impact on the current
              consumption.
         3.   IDDDOZE = [IDDIDLE*(N-1)/N] + IDDHFO16/N where N = Doze Ratio (see CPUDOZE register).
         4.   PMD bits are all in the Default state, no modules are disabled.


47.3.3 Power-Down Current (IPD)(1, 2,3)
        Table 47-3. Power Down Current
         Standard Operating Conditions (unless otherwise stated)
          Param.          Sym.             Device           Min.    Typ.†   Max.            Max.      Units              Conditions
           No.                          Characteristics                     +85°C          +125°C               VDD     VREGPM         Note
         D200       IPD                IPD Base              —       1.2      3.8           4.6            μA   3.0V     ‘b11
                                                             —       0.9     12.1           43             μA   3.0V     ‘b10
                                                             —      29.5     45.5           68.9           μA   3.0V     ‘b01
                                                             —      157      222            240            μA   3.0V     ‘b00
         D201       IPD_WDT            Low-Frequency         —       1.5      4             5.1            μA   3.0V     ‘b11
                                       Internal
                                       Oscillator/WDT
         D202       IPD_SOSC           Secondary             —       2.1      4.8           7.9            μA   3.0V     ‘b11
                                       Oscillator (SOSC)


--- p894 ---
                                                                                                                       PIC18F27/47/57Q43
                                                                                                                    Electrical Specifications

       ...........continued
        Standard Operating Conditions (unless otherwise stated)
         Param.        Sym.              Device           Min.   Typ.†    Max.       Max.          Units            Conditions
          No.                         Characteristics                     +85°C     +125°C                  VDD    VREGPM         Note
        D203       IPD_LPBOR      Low-Power                —      1.3       4          6            μA      3.0V    ‘b11
                                  Brown-out Reset
                                  (LPBOR)
        D204       IPD_FVR_BUF1   FVR Buffer 1             —     180       281       285            μA      3.0V    ‘b11
                                  (ADC)
        D204A      IPD_FVR_BUF2   FVR Buffer 2             —     49.4      77         93            μA      3.0V   ‘bx1 or
                                  (DAC/CMP)                                                                         ‘b10
        D205       IPD_BOR        Brown-out Reset          —      17       24         25            μA      3.0V    ‘b11
                                  (BOR)
        D206       IPD_HLVD       High/Low-Voltage         —      17       25         27            μA      3.0V    ‘b11
                                  Detect (HLVD)
        D207       IPD_ADCA       ADC - Active             —     483       813       819            μA      3.0V   ‘bx1 or    ADC is
                                                                                                                    ‘b10      converting
                                                                                                                              (Note 4)
        D208       IPD_CMP        Comparator               —      55       95        105            μA      3.0V    ‘b11
        * These parameters are characterized but not tested.
        † Data in “Typ.” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
        tested.
        Notes:
        1.   The peripheral current is the sum of the base IDD and the additional current consumed when this peripheral is enabled.
             The peripheral ∆ current can be determined by subtracting the base IDD or IPDcurrent from this limit. Max. values will be
             used when calculating total current consumption.
        2.   The power-down current in Sleep mode does not depend on the oscillator type. Power-down current is measured with
             the part in Sleep mode with all I/O pins in high-impedance state and tied to VSS.
        3.   All peripheral currents listed are on a per-peripheral basis if more than one instance of a peripheral is available.
        4.   ADC clock source is ADCRC.


47.3.4 I/O Ports
       Table 47-4. I/O Ports
       Standard Operating Conditions (unless otherwise stated)
       Param. No.   Sym.           Device          Min.       Typ.†                         Max.           Units        Conditions
                              Characteristics
       Input Low-Voltage
                  VIL             I/O PORT:
       D300                       •     with TTL buffer          —              —         0.8               V      4.5V ≤ VDD ≤ 5.5V
       D301                                                      —              —      0.15 VDD             V      1.8V ≤ VDD < 4.5V
       D302                       •     with Schmitt             —              —      0.2 VDD              V      2.0V ≤ VDD ≤ 5.5V
                                        Trigger buffer

       D303                       •     with I2C levels          —              —          0.3 VDD          V      2.0V ≤ VDD ≤ 5.5V

       D304                       •     with SMBus 2.0           —              —            0.8            V      2.7V ≤ VDD ≤ 5.5V

       D305                       •     with SMBus 3.0           —              —            0.8            V

       D306                       MCLR                           —              —          0.2 VDD          V
       High/Low-Voltage


--- p895 ---
                                                                                               PIC18F27/47/57Q43
                                                                                            Electrical Specifications

...........continued
Standard Operating Conditions (unless otherwise stated)
Param. No.    Sym.          Device          Min.       Typ.†              Max.     Units        Conditions
                        Characteristics
           VIH       I/O PORT:
D320                    •   with TTL buffer        2.0            —        —        V      4.5V ≤ VDD ≤ 5.5V
D321                                            0.25 VDD          —        —        V      1.8V ≤ VDD < 4.5V
                                                  + 0.8
D322                    •   with Schmitt         0.8 VDD          —        —        V      2.0V ≤ VDD ≤ 5.5V
                            Trigger buffer

D323                    •   with I2C levels      0.7 VDD          —        —        V

D324                    •   with SMBus 2.0         2.1            —        —        V      2.7V ≤ VDD ≤ 5.5V

D325                    •   with SMBus 3.0        1.35            —        —        V      25°C
                                                                                           ≤ TA ≤ +125°C
                                                                                           1.8V ≤ VDD ≤ 5.5V
                                                  1.45            —        —        V      -40°C
                                                                                           ≤ TA ≤ +25°C
                                                                                           1.8V ≤ VDD ≤ 5.5V
D326                MCLR                         0.7 VDD          —        —        V
Input Leakage Current(1)
D340       IIL      I/O PORTS                       —             ±5      ±125      nA     VSS ≤ VPIN ≤ VDD,
                                                                                           Pin at high-
                                                                                           impedance, 85°C
D341                                                —             ±5     ±1000      nA     VSS ≤ VPIN ≤ VDD,
                                                                                           Pin at high-
                                                                                           impedance, 125°C
D342                    MCLR(2)                     —         ±50         ±200      nA     VSS ≤ VPIN ≤ VDD,
                                                                                           Pin at high-
                                                                                           impedance, 85°C
Weak Pull-up Current
D350       IPUR                                    80         140          200      μA     VDD = 3.0V,
                                                                                           VPIN = VSS
Output Low-Voltage
D360      VOL      I/O PORTS                        —             —        0.6      V      IOL = 10.0 mA,
                                                                                           VPIN = 3.0V
Output High-Voltage
D370       VOH      I/O PORTS                   VDD - 0.7         —        —        V      IOH = 6.0 mA,
                                                                                           VPIN = 3.0V
All I/O Pins
D380         CIO                                   —          5         50         pF
† Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only
and are not tested.
Notes:
1.   Negative current is defined as current sourced by the pin.
2.   The leakage current on the MCLR pin is strongly dependent on the applied voltage level. The specified
     levels represent normal operating conditions. Higher leakage current may be measured at different input
     voltages.


--- p896 ---
                                                                                                                         PIC18F27/47/57Q43
                                                                                                                      Electrical Specifications

47.3.5 Memory Programming Specifications
        Table 47-5. Memory Programming
        Standard Operating Conditions (unless otherwise stated)
         Param   Sym.             Device Characteristics              Min.    Typ†   Max.     Units                Conditions
          No.
        Data EEPROM Memory Specifications
        MEM20 ED         DataEE Byte Endurance                       100k      —       —      E/W -40°C ≤ TA ≤ +85°C
        MEM21 TD_RET Characteristic Retention                                                         Provided no other specifications are
                                                                       —      40       —      Year
                                                                                                      violated
        MEM22 ND_REF Total Erase/Write Cycles before Refresh          1M      4M       —      E/W -40°C ≤ TA ≤ +85°C
        MEM23 VD_RW VDD for Read or Erase/Write operation            VDDMIN    —     VDDMAX    V
        MEM24 TD_BEW Byte Erase and Write Cycle Time                   —       —      11       ms
        Program Flash Memory Specifications
        MEM30 EP         Flash Memory Cell Endurance                                              -40°C ≤ TA ≤ +85°C
                                                                       1k      —       —      E/W (Note 1)

        MEM32 TP_RET Characteristic Retention                                                         Provided no other specifications are
                                                                       —      40       —      Year
                                                                                                      violated
        MEM33 VP_RD      VDD for Read operation                      VDDMIN    —     VDDMAX    V
        MEM34 VP_REW VDD for Row Erase or Write operation            VDDMIN    —     VDDMAX    V
        MEM35 TP_REW Self-Timed Page Write                             —       —      10       ms
        MEM36 TSE        Self-Timed Page Erase                         —       —      11       ms
        MEM37 TP_WRD Self-Timed Word Write                             —       —      75       μs
        † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
        tested.
        Note:
        1.   Flash Memory Cell Endurance for the Flash memory is defined as: One Row Erase operation and one Self-Timed Write.


47.3.6 Thermal Characteristics
        Table 47-6. Thermal Considerations
        Standard Operating Conditions (unless otherwise stated)
         Param No.      Sym.                      Characteristic                       Typ.   Units                 Conditions
        TH01            θJA     Thermal Resistance Junction to Ambient                 60      °C/W 28-pin SPDIP package
                                                                                       80      °C/W 28-pin SOIC package
                                                                                       90      °C/W 28-pin SSOP package
                                                                                       27.5    °C/W 28-pin VQFN 4x4 mm package
                                                                                       47.2    °C/W 40-pin PDIP package
                                                                                       29      °C/W 40-pin QFN package
                                                                                       46      °C/W 44-pin TQFP package
                                                                                       62.8    °C/W 48-pin TQFP package
                                                                                       24.8    °C/W 48-pin VQFN package
        TH02            TJMAX   Maximum Junction Temperature                           150      °C
        Note:
        1.   See “Absolute Maximum Ratings” for total power dissipation.


--- p897 ---
                                                                                                                            PIC18F27/47/57Q43
                                                                                                                         Electrical Specifications

47.4    AC Characteristics
        Figure 47-3. Load Conditions

                                                                       Load Condition

                                                              Pin

                                                                                            CL

                                                                                               VSS


                                                          Legend: CL = 50 pF for all pins


47.4.1 External Clock/Oscillator Timing Requirements
        Figure 47-4. Clock Timing
                                      Q4                Q1                   Q2                 Q3          Q4                 Q1


                   CLKIN

                                                   OS1/OS3/OS5/OS20                OS2/OS4/OS6                     OS2/OS4/OS6
                                                                                  OS21

           CLKOUT
           (CLKOUT Mode)

        Note: See the table below.

        Table 47-7. External Clock Oscillator
        Standard Operating Conditions (unless otherwise stated)
          Param No.            Sym.           Characteristic           Min.              Typ. †      Max.        Units           Conditions
        ECL Oscillator
        OS1             FECL               Clock Frequency              —                  —          1          MHz
        OS2             TECL_DC            Clock Duty Cycle             40                 —          60          %
        ECM Oscillator
        OS3             FECM               Clock Frequency              —                  —          16         MHz
        OS4             TECM_DC            Clock Duty Cycle             40                 —          60          %
        ECH Oscillator
        OS5             FECH               Clock Frequency              —                  —          64         MHz         VDD ≥ 2.7V
                                                                        —                  —          32         MHz         VDD < 2.7V
        OS6             TECH_DC            Clock Duty Cycle             40                 —          60          %
        LP Oscillator
        OS7             FLP                Clock Frequency              —                  —         100         kHz         (Note 4)
        XT Oscillator
        OS8             FXT                Clock Frequency              —                  —          4          MHz         (Note 4)
        HS Oscillator
        OS9             FHS                Clock Frequency              —                  —          20         MHz         VDD > 2.5V (Note
                                                                                                                             4)
        Secondary Oscillator
        OS10            FSEC               Clock Frequency             32.4              32.768      33.1        kHz         (Note 4)
        System Oscillator


--- p898 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                                   Electrical Specifications

        ...........continued
         Standard Operating Conditions (unless otherwise stated)
          Param No.            Sym.        Characteristic         Min.           Typ. †       Max.         Units           Conditions
         OS20           FOSC           System Clock                —               —            64         MHz         (Note 2, Note 3)
                                       Frequency
         OS21           FCY            Instruction                 —             FOSC/4         —          MHz
                                       Frequency
         OS22           TCY            Instruction Period         62.5            1/FCY         —             ns
         Notes:
         1.   Instruction cycle period (TCY) equals four times the input oscillator time base period. All specified values are based on
              characterization data for that particular oscillator type under standard operating conditions with the device executing
              code. Exceeding these specified limits may result in an unstable oscillator operation and/or higher than expected
              current consumption. All devices are tested to operate at “min” values with an external clock applied to OSC1 pin. When
              an external clock input is used, the “max” cycle time limit is “DC” (no clock) for all devices.
         2.   The system clock frequency (FOSC) is selected by the “main clock switch controls” as described in the “Power Saving
              Operation Modes” section.
         3.   The system clock frequency (FOSC) must meet the voltage requirements defined in the “Standard Operating
              Conditions” section.
         4.   LP, XT and HS oscillator modes require an appropriate crystal or resonator to be connected to the device. For clocking
              the device with the external square wave, one of the EC mode selections must be used.


47.4.2 Internal Oscillator Parameters(1)
        Table 47-8. Internal Oscillator
         Standard Operating Conditions (unless otherwise stated)
         Param No.            Sym.         Characteristic         Min.          Typ. †    Max.         Units            Conditions
         OS50          FHFOSC         Precision Calibrated         —              4         —          MHz         (Note 2)
                                      HFINTOSC Frequency                          8
                                                                                 12
                                                                                 16
                                                                                 32
                                                                                 48
                                                                                 64

         OS51          FHFOSCLP       Low-Power Optimized         0.92            1        1.08        MHz         -40°C ≤ TA ≤ 85°C
                                      HFINTOSC Frequency          1.84            2        2.16        MHz         -40°C ≤ TA ≤ 85°C
                                                                  0.88            1        1.12        MHz         85°C ≤ TA ≤ 125°C
                                                                  1.76            2        2.24        MHz         85°C ≤ TA ≤ 125°C

         OS52          FMFOSC         Internal Calibrated          —             500        —           kHz
                                      MFINTOSC Frequency
         OS53          FLFOSC         Internal LFINTOSC           24.8           31        37.2         kHz
                                      Frequency


--- p899 ---
                                                                                                                                  PIC18F27/47/57Q43
                                                                                                                               Electrical Specifications

...........continued
Standard Operating Conditions (unless otherwise stated)
 Param No.                        Sym.             Characteristic           Min.          Typ. †         Max.         Units         Conditions
OS54                        THFOSCST           HFINTOSC Wake-up              —             13             20           μs      VREGPM = 00
                                               from Sleep Start-up                                                             System Clock at 4
                                               Time                                                                            MHz
                                                                                                                               VDD = 3.0V

                                                                             —             30             48           μs      VREGPM = 01
                                                                                                                               System Clock at 4
                                                                                                                               MHz
                                                                                                                               VDD = 3.0V

                                                                             —             115           210           μs      VREGPM = 10
                                                                                                                               System Clock at 4
                                                                                                                               MHz
                                                                                                                               VDD = 3.0V

                                                                             —             120           220           μs      VREGPM = 11
                                                                                                                               System Clock at 4
                                                                                                                               MHz
                                                                                                                               VDD = 3.0V

OS56                        TLFOSCST           LFINTOSC Wake-up              —             292           420           μs      25ºC ≤ TA ≤ 125ºC
                                               from Sleep Start-up                                                             VDD = 3.0V
                                               Time
                                                                                                                               VREGPM = xx

* These parameters are characterized but not tested.
† Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
tested.
Notes:
1.   To ensure these oscillator frequency tolerances, VDD and VSS must be capacitively decoupled as close to the device as
     possible. 0.1 μF and 0.01 μF values in parallel are recommended.
2.   See the figure below.


Figure 47-5. Precision Calibrated HFINTOSC Frequency Accuracy Over Device VDD and Temperature
                            125

                                                                                         ± 5%

                             85

                                                                                         ± 3%
         Temperature (°C)


                             60


                                                                                     ± 2%


                              0
                                                                                     ± 5%

                            -40
                               1.8       2.0          2.3            3.0           3.5             4.0          4.5           5.0           5.5

                                                                                          VDD (V)


--- p900 ---
                                                                                                                            PIC18F27/47/57Q43
                                                                                                                         Electrical Specifications

47.4.3 PLL Specifications
        Table 47-9. PLL Specifications
        Standard Operating Conditions (unless otherwise stated)
             Param No.            Sym.                Characteristic              Min.         Typ. †      Max.        Units          Conditions
        PLL01               FPLLIN           PLL Input Frequency Range             4            —           16         MHz
        PLL02               FPLLOUT          PLL Output Frequency Range            16           —           64         MHz       (Note 1)
        PLL03*              FPLLST           PLL Lock Time                         —            200         —           μs
        PLL04*              FPLLJIT          PLL Output Frequency                -0.25          —          0.25         %
                                             Stability
        * These parameters are characterized but not tested.
        † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
        tested.
        Note:
        1.    The output frequency of the PLL must meet the FOSC requirements listed in Parameter D002.


47.4.4 I/O and CLKOUT Timing Specifications
        Figure 47-6. CLKOUT and I/O Timing
                Cycle                    Write                      Fetch                        Read                         Execute
                                          Q4                         Q1                             Q2                          Q3
                 FOSC
                                                                 IO1                                                     IO2
                                                                                                IO10
             CLKOUT
                                                                    IO8                         IO4                            IO7
                                                                                         IO5
                I/O pin
                (Input)
                                                              IO3
               I/O pin                Old Value                                                                               New Value
               (Output)
                                                                          IO7, IO8

        Table 47-10. I/O and CLKOUT Timing Specifications
        Standard Operating Conditions (unless otherwise stated)
        Param No.         Sym.                                 Characteristic                              Min. Typ. † Max. Units Conditions
        IO1*          TCLKOUTH        CLKOUT rising edge delay (rising edge FOSC (Q1 cycle) to falling      —     —      70      ns
                                      edge CLKOUT
        IO2*          TCLKOUTL        CLKOUT falling edge delay (rising edge FOSC (Q3 cycle) to rising      —     —      72      ns
                                      edge CLKOUT
        IO3*          TIO_VALID       Port output valid time (rising edge FOSC (Q1 cycle) to port valid)    —     50     70      ns
        IO4*          TIO_SETUP       Port input setup time (Setup time before rising edge FOSC – Q2       20     —      —       ns
                                      cycle)
        IO5*          TIO_HOLD        Port input hold time (Hold time after rising edge FOSC – Q2          50     —      —       ns
                                      cycle)
        IO6*          TIOR_SLREN Port I/O rise time, slew rate enabled                                      —     25     —       ns     VDD = 3.0V
        IO7*          TIOR_SLRDIS Port I/O rise time, slew rate disabled                                    —     5      —       ns     VDD = 3.0V
        IO8*          TIOF_SLREN Port I/O fall time, slew rate enabled                                      —     25     —       ns     VDD = 3.0V
        IO9*          TIOF_SLRDIS Port I/O fall time, slew rate disabled                                    —     5      —       ns     VDD = 3.0V


--- p901 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                            Electrical Specifications

        ...........continued
        Standard Operating Conditions (unless otherwise stated)
        Param No.       Sym.                            Characteristic                         Min. Typ. † Max. Units Conditions
        IO10*       TINT       INT pin high or low time to trigger an interrupt                25     —     —     ns
        IO11*       TIOC       Interrupt-on-Change minimum high or low time to trigger         25     —     —     ns
                               interrupt
        * These parameters are characterized but not tested.


47.4.5 Reset, WDT, Oscillator Start-Up Timer, Power-Up Timer, Brown-Out Reset and Low-Power
       Brown-Out Reset Specifications
       Figure 47-7. Reset, Watchdog Timer, Oscillator Start-Up Timer and Power-Up Timer Timing


                     VDD

                  MCLR

                                                                                    RST01
                 Internal
                    POR

                                        RST04
                  PWRT
                Time-out                          RST05
                    OSC
           Start-up Time


         Internal Reset(1)

         Watchdog Timer
               Reset(1)
                                                                                                    RST03
                                                                                  RST02
                                                                                                                 RST02
                 I/O pins

       Note:
       1. Asserted low.

       Figure 47-8. Brown-out Reset Timing and Characteristics
                    VDD
                                                                                   VBOR and VHYST
                               VBOR


                                             (Device in Brown-out Reset)                        (Device not in Brown-out Reset)


                             RST08


                Reset
                                                                                    RST04(1)
        (due to BOR)
       Note:
       1. Only if the PWRTE Configuration bit is programmed to ‘1’; 2 ms delay if PWRTE = 0.


--- p902 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                               Electrical Specifications

Table 47-11. Resets
Standard Operating Conditions (unless otherwise stated)
 Param No.     Sym.         Characteristic       Min.             Typ. †      Max.     Units         Conditions
RST01*     TMCLR        MCLR Pulse Width          —                 —          —        μs
                        Low to ensure Reset
RST02*        TIOZ          I/O high-impedance          —          —               2     μs
                            from Reset detection
RST03         TWDT          Watchdog Timer              —          16              —    ms        WDTCPS =
                            Time-out Period                                                       00100
RST04*        TPWRT         Power-up Timer              —          65              —    ms
                            Period
RST05         TOST          Oscillator Start-up         —         1024             —    TOSC
                            Timer Period(1,2)
RST06         VBOR          Brown-out Reset            2.7        2.85         3.0       V        BORV = 00
                            Voltage                    2.55        2.7        2.85       V        BORV = 01
                                                       2.3        2.45         2.6       V        BORV = 10
                                                       1.8         1.9         2.1       V        BORV = 11
RST07         VBORHYS    Brown-out Reset             —             60              —    mV        BORV = 00
                         Hysteresis
RST08       TBORDC       Brown-out Reset             —              3              —     μs
                         Response Time
RST09       VLPBOR       Low-Power Brown-           1.8            1.9         2.2       V
                         out Reset Voltage
* These parameters are characterized but not tested.
† Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only
and are not tested.
Notes:
1.   By design, the Oscillator Start-up Timer (OST) counts the first 1024 cycles, independent of frequency.
2.   To ensure these voltage tolerances, VDD and VSS must be capacitively decoupled as close to the device as
     possible. 0.1 μF and 0.01 μF values in parallel are recommended.


--- p903 ---
                                                                                                                        PIC18F27/47/57Q43
                                                                                                                     Electrical Specifications

47.4.6 High/Low-Voltage Detect Characteristics
        Table 47-12. High/Low-Voltage Detect
        Standard Operating Conditions (unless otherwise stated)
         Param No.     Sym.       Characteristic       Min.                       Typ.          Max.        Units           Conditions
        HLVD01          VDET        Voltage Detect                 1.73(1)        1.90          2.07            V     HLVDSEL = 0000
                                                                    1.91          2.10          2.29            V     HLVDSEL = 0001
                                                                    2.05          2.25          2.45            V     HLVDSEL = 0010
                                                                    2.28          2.50          2.73            V     HLVDSEL = 0011
                                                                    2.37          2.60          2.83            V     HLVDSEL = 0100
                                                                     2.5          2.75          3.00            V     HLVDSEL = 0101
                                                                    2.64          2.90          3.16            V     HLVDSEL = 0110
                                                                    2.87          3.15          3.43            V     HLVDSEL = 0111
                                                                    3.05          3.35          3.65            V     HLVDSEL = 1000
                                                                    3.28          3.60          3.92            V     HLVDSEL = 1001
                                                                    3.41          3.75          4.09            V     HLVDSEL = 1010
                                                                    3.64          4.00          4.36            V     HLVDSEL = 1011
                                                                    3.82          4.20          4.58            V     HLVDSEL = 1100
                                                                    3.96          4.35          4.74            V     HLVDSEL = 1101
                                                                    4.23          4.65          5.07            V     HLVDSEL = 1110
        * These parameters are characterized but not tested.
        † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only
        and are not tested.
        Note:
        1.   Device operation below VDD = 1.8 V is not recommended.


47.4.7 Analog-to-Digital Converter (ADC) Accuracy Specifications(1,2)
        Table 47-13. ADC Accuracy Specifications
         Standard Operating Conditions (unless otherwise stated)
         VDD = 3.0V, TA = 25°C, TAD = 500 ns

         Param No.     Sym.                       Characteristic                         Min.    Typ. †   Max.      Units     Conditions
         AD01         NR       Resolution                                                 —       —        12        bit
         AD02         EIL      Integral Nonlinearity Error                                —      ±0.1      ±2.0     LSb     ADCREF+ = 3.0V,
                                                                                                                            ADCREF- = 0V

         AD03         EDL      Differential Nonlinearity Error                           -0.5    ±0.1      +1.0     LSb     ADCREF+ = 3.0V,
                                                                                                                            ADCREF- = 0V

         AD04         EOFF     Offset Error                                               —       0.5      6.0      LSb     ADCREF+ = 3.0V,
                                                                                                                            ADCREF- = 0V

         AD05         EGN      Gain Error                                                 —      ±0.2      ±6.0     LSb     ADCREF+ = 3.0V,
                                                                                                                            ADCREF- = 0V

         AD06         VADREF   ADC Reference Voltage (ADREF+ - ADREF-)                   1.8      —        VDD       V
         AD07         VAIN     Full-Scale Range                                      ADREF-       —       ADREF+     V
         AD08         ZAIN     Recommended Impedance of Analog Voltage                    —        1        —        kΩ
                               Source
         AD09         RVREF    ADC Voltage Reference Ladder Impedance                     —       50        —        kΩ     (Note 3)


--- p904 ---
                                                                                                                                PIC18F27/47/57Q43
                                                                                                                             Electrical Specifications

        ...........continued
        Standard Operating Conditions (unless otherwise stated)
        VDD = 3.0V, TA = 25°C, TAD = 500 ns

         Param No.        Sym.                     Characteristic                        Min.        Typ. †   Max.      Units         Conditions
        * These parameters are characterized but not tested.
        † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
        tested.
        Notes:
        1.   Total Absolute Error is the sum of the offset, gain and integral nonlinearity (INL) errors.
        2.   The ADC conversion result never decreases with an increase in the input and has no missing codes.
        3.   This is the impedance seen by the VREF pads when the external reference pads are selected.


47.4.8 Analog-to-Digital Converter (ADC) Conversion Timing Specifications
        Table 47-14. ADC Conversion Timing
        Standard Operating Conditions (unless otherwise stated)
        Param No. Sym.                 Characteristic         Min.         Typ. †   Max. Units                        Conditions
        AD20            TAD   ADC Clock Period                 0.5          —        9          μs    Using FOSC as the ADC clock source
                                                                                                      ADOCS = 0
                                                                —            2       —          μs    Using ADCRC as the ADC clock source
                                                                                                      ADOCS = 1
        AD21            TCNV Conversion Time                    —     14 TAD+2TCY    —          —     Using FOSC as the ADC clock source
                                                                                                      ADOCS = 0
                                                                —     16 TAD+2TCY    —          —     Using ADCRC as the ADC clock source
                                                                                                      ADOCS = 1
        AD22            THCD Sample-and-Hold Capacitor          —      2 TAD+1TCY    —          —     Using FOSC as the ADC clock source
                             Disconnect Time                                                          ADOCS = 0
                                                                —      3 TAD+2TCY    —          —     Using ADCRC as the ADC clock source
                                                                                                      ADOCS = 1
        * These parameters are characterized but not tested.
        † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
        tested.


        Figure 47-9. ADC Conversion Timing (ADC Clock FOSC-Based)

             BSF ADCON0, GO
                                                                                                                     1 TCY
                                                                    AD21
                                       AD22                                                                                   1 TCY
                               1 TCY                                                       AD20

             ADC_clk


             ADRES                                                   OLD DATA                                                      NEW DATA


                 ADIF


                  GO                                                                                                            DONE


             Sample                                      Sampling Stopped


--- p905 ---
                                                                                                                                      PIC18F27/47/57Q43
                                                                                                                                   Electrical Specifications

        Figure 47-10. ADC Conversion Timing (ADC Clock from ADCRC)

               BSF ADCON0, GO
                                                                                                                                       1 TCY
                                                                               AD21
                                              AD22
                                  2 TCY(1)                                                                     AD20

               ADC_clk


                ADRES                                                           OLD DATA                                                    NEW DATA


                  ADIF


                   GO                                                                                                                    DONE


                Sample                                                   Sampling Stopped


                  Note 1: If the ADC clock source is selected as ADCRC, a time of 1 TCY is added before the ADC clock starts. This allows
                  the SLEEP instruction to be executed, if any.


47.4.9 Comparator Specifications
        Table 47-15. Comparator Specifications
         Standard Operating Conditions (unless otherwise stated)
         VDD = 3.0V, TA = 25°C

              Param No.           Sym.                  Characteristic                    Min.        Typ. †          Max.       Units         Conditions
         CM01                VIOFF           Input Offset Voltage                           —           —             ±50        mV         VICM = VDD/2
         CM02                VICM            Input Common Mode Range                      GND           —             VDD         V
         CM03                CMRR            Common Mode Input Rejection                    —           50             —          dB
                                             Ratio
         CM04                VHYST           Comparator Hysteresis                         10           25             50        mV
         CM05                TRESP   (1)     Response Time, Rising Edge                     —          300            600         ns
                                             Response Time, Falling Edge                    —          220            500         ns
         * These parameters are characterized but not tested.
         † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
         tested.
         Note:
         1.     Response time measured with one comparator input at VDD/2, while the other input transitions from VSS to VDD.


47.4.10 8-Bit DAC Specifications
        Table 47-16. 8-bit Digital-to-Analog Converter
         Standard Operating Conditions (unless otherwise stated)
         VDD = 3.0V, TA = 25°C

          Param No.         Sym.             Characteristic            Min.              Typ. †              Max.       Units            Conditions
         DSB01             VLSB        Step Size                        —      (VDACREF+-VDACREF-)/256         —            V
         DSB02             VACC        Absolute Accuracy(1)            -2.5               1.9                  7        LSb
         DSB03*            RUNIT       Unit Resistor Value              —                 20                   —            kΩ


--- p906 ---
                                                                                                                                        PIC18F27/47/57Q43
                                                                                                                                     Electrical Specifications

        ...........continued
         Standard Operating Conditions (unless otherwise stated)
         VDD = 3.0V, TA = 25°C

          Param No.        Sym.            Characteristic          Min.               Typ. †                   Max.       Units           Conditions
         DSB04*           TST        Settling Time(2)                —                   10                       —          μs
         DSB05            VDBO       DAC Buffer Offset               —                   20                       45        mV
         DSB06            INL        Integral Nonlinearity          -1.7                 1                       1.9        LSb   0x09 ≤ DACxDATL ≥
                                                                                                                                  0x246
         DSB07            DNL        Differential Nonlinearity      -0.5                 0.4                     1.2        LSb   0x09 ≤ DACxDATL ≥
                                                                                                                                  0x246
         DSB08            EOFF       Offset Error                   -0.8                 1.4                     2.5        LSb   0x09 ≤ DACxDATL ≥
                                                                                                                                  0x246
         DSB09            EGN        Gain Error                     -1.7                -1.2                     0.8        LSb   0x09 ≤ DACxDATL ≥
                                                                                                                                  0x246
         * These parameters are characterized but not tested.
         † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
         tested.
         Notes:
         1.    Absolute accuracy = Offset Error + Gain Error + DAC Buffer Error (EOFF + EGN + VDBO)
         2.    Settling time measured while DACR[7:0] transitions from ‘b00000000 to ‘b11111111


47.4.11 Fixed Voltage Reference (FVR) Specifications
        Table 47-17. FVR Specifications
         Standard Operating Conditions (unless otherwise stated)
              Param No.         Sym.          Characteristic         Min.       Typ. †         Max.         Units                  Conditions
         FVR01              VFVR1        1x Gain (1.024V)                -4       —             +4           %         VDD ≥ 2.5V, -40°C to 85°C
         FVR02              VFVR2        2x Gain (2.048V)                -4       —             +4           %         VDD ≥ 2.5V, -40°C to 85°C
         FVR03              VFVR4        4x Gain (4.096V)                -5       —             +5           %         VDD ≥ 4.75V, -40°C to 85°C
         FVR04              TFVRST       FVR Start-up Time               —       260            —            μs


47.4.12 Zero-Cross Detect (ZCD) Specifications
        Table 47-18. ZCD Specifications
         Standard Operating Conditions (unless otherwise stated)
         VDD = 3.0V, TA = 25°C

              Param No.           Sym.                  Characteristic                Min.            Typ. †           Max.       Units       Conditions
         ZC01               VPINZC           Voltage on Zero Cross Pin                  —              0.9              —           V
         ZC02               IZCD_MAX         Maximum source or sink                     —              —               600         μA
                                             current
         ZC03               TRESPH           Response Time, Rising Edge                 —               1               —          μs
                            TRESPL           Response Time, Falling Edge                —               1               —           μs
         † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
         tested.


--- p907 ---
                                                                                                                     PIC18F27/47/57Q43
                                                                                                                  Electrical Specifications

47.4.13 Timer0 and Timer1 External Clock Requirements
       Table 47-19. TMR0 and TMR1 Requirements
        Standard Operating Conditions (unless otherwise stated)
        Operating Temperature: -40°C≤TA≤+125°C

        Param No.      Sym.                    Characteristic                        Min.          Typ. † Max. Units      Conditions
        40*         TT0H        T0CKI High Pulse No Prescaler                     0.5TCY+20         —        —    ns
                                Width            With Prescaler                        10           —        —    ns
        41*         TT0L        T0CKI Low Pulse No Prescaler                      0.5TCY+20         —        —    ns
                                Width           With Prescaler                         10           —        —    ns
        42*         TT0P        T0CKI Period                                   Greater of: 20 or    —        —    ns   N = Prescale
                                                                                  (TCY+40)/N                           value
        45*         TT1H        T1CKI High Time Synchronous, No                   0.5TCY+20         —        —    ns
                                                Prescaler
                                                   Synchronous, with                   15           —        —    ns
                                                   Prescaler
                                                   Asynchronous                        30           —        —    ns
        46*         TT1L        T1CKI Low Time     Synchronous, No                0.5TCY+20         —        —    ns
                                                   Prescaler
                                                   Synchronous, with                   15           —        —    ns
                                                   Prescaler
                                                   Asynchronous                        30           —        —    ns
        47*         TT1P        T1CKI Input        Synchronous                 Greater of: 30 or    —        —    ns   N = Prescale
                                Period                                            (TCY+40)/N                           value
                                                   Asynchronous                        60           —        —    ns
        49*         TCKEZTMR1 Delay from External Clock Edge to Timer               2 TOSC          —    7 TOSC   —    Timers in Sync
                              Increment                                                                                mode
        * These parameters are characterized but not tested.
        † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
        tested.


       Figure 47-11. Timer0 and Timing1 External Clock Timings


                    T0CKI

                                                         40                       41


                                                                     42


                    T1CKI
                                                          45                      46


                                                                     47                                 49


                    TMR0 or
                    TMR1


--- p908 ---
                                                                                                                               PIC18F27/47/57Q43
                                                                                                                            Electrical Specifications

47.4.14 Capture/Compare/PWM Requirements (CCP)
       Table 47-20. CCP Requirements
        Standard Operating Conditions (unless otherwise stated)
        Operating Temperature: -40°C ≤ TA ≤ +125°C

         Param No.     Sym.                Characteristic                     Min.             Typ. †     Max.     Units          Conditions
        CC01*         TCCL       CCPx Input Low       No Prescaler        0.5TCY+20             —             —   ns
                                 Time
                                                     With Prescaler              20             —             —   ns
        CC02*         TCCH       CCPx Input High      No Prescaler        0.5TCY+20             —             —   ns
                                 Time
                                                     With Prescaler              20             —             —   ns
        CC03*         TCCP       CCPx Input Period                       (3TCY+40)/N            —             —   ns         N = Prescale value
        * These parameters are characterized but not tested.
        † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
        tested.


       Figure 47-12. Capture/Compare/PWM Timings (CCP)
                               CCPx
                      (Capture mode)


                                                                      CC01                    CC02

                                                                                  CC03
       Note: Refer to the Load Conditions figure for more details.

47.4.15 SPI Mode Requirements
       Table 47-21. SPI Host Mode
        Standard Operating Conditions (unless otherwise stated)
        Param No.            Sym.            Characteristic            Min.           Typ. †            Max.       Units           Conditions
                                                                        61             —                 —             ns      Transmit only
                                                                                                                               mode
                                        SCK Cycle Time (2x              —             16(1)              —         MHz
                     TSCK
                                        Prescaled)                      95             —                 —             ns      Full-Duplex mode
                                                                        —             10(1)              —         MHz
        SP70*        TSSL2SCH,          SDO to SCK↓ or SCK↑            TSCK            —                 —             ns      FST = 0
                     TSSL2SCL           input
                                                                         0             —                 —             ns      FST = 1
        SP71*        TSCH               SCK output high time         0.5 TSCK -        —           0.5 TSCK +          ns
                                                                        12                             12
        SP72*        TSCL               SCK output low time          0.5 TSCK -        —           0.5 TSCK +          ns
                                                                        12                             12
        SP73*        TDIV2SCH,          Setup time of SDI data          85             —                 —             ns
                     TDIV2SCL           input to SCK edge

        SP74*        TSCH2DIL,          Hold time of SDI data            0             —                 —             ns
                     TSCL2DIL           input to SCK edge
                                        Hold time of SDI data         0.5 TSCK                                         ns      CKE = 0,
                                        input to final SCK                                                                     SMP = 1

        SP75*        TDOR               SDO data output rise            —              10                25            ns      CL = 50 pF
                                        time
        SP76*        TDOF               SDO data output fall            —              10                25            ns      CL = 50 pF
                                        time
        SP78*        TSCR               SCK output rise time            —              10                25            ns      CL = 50 pF


--- p909 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                       Electrical Specifications

...........continued
Standard Operating Conditions (unless otherwise stated)
 Param No.           Sym.           Characteristic            Min.      Typ. †     Max.        Units          Conditions
SP79*        TSCF              SCK output fall time            —         10          25          ns       CL = 50 pF
SP80*        TSCH2DOV,         SDO data output valid           -15       —           15          ns       CL = 50 pF
             TSCL2DOV          after SCK edge

SP81*        TDOV2SCH,         SDO data output valid to     TSCK - 10    —           —           ns       CL = 50 pF
             TDOV2SCL          first SCK edge                                                             CKE = 1

SP82*        TSSL2DOV          SDO data output valid           —         —           50          ns       CL = 20 pF
                               after SS↓ edge
SP83*        TSCH2SSH,         SS ↑ after last SCK edge     TSCK - 10    —           —           ns
             TSCL2SSH

SP84*        TSSH2SSL          SS ↑ to SS↓ edge             TSCK - 10    —           —           ns

* These parameters are characterized but not tested.
† Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
tested.
Note:
1.   SMP bit in the SPIxCON1 register must be set and the slew rate control must be disabled on the clock and data pins
     (clear the corresponding bits in SLRCONx register) for SPI to operate over 4 MHz.


Table 47-22. SPI Client Mode
Standard Operating Conditions (unless otherwise stated)
 Param No.           Sym.            Characteristic           Min.      Typ. †       Max.       Units          Conditions
              TSCK             SCK Total Cycle Time            47         —           —           ns       Receive Only
                                                                                                           mode
                                                                —        20(1)        —          MHz
                                                               95         —           —           ns       Full-Duplex mode
                                                                —        10(1)        —          MHz
SP70*         TSSL2SCH,        SS↓ to SCK↓ or SCK↑              0         —           —           ns       CKE = 0
              TSSL2SCL         input
                                                               25         —           —           ns       CKE = 1
SP71*         TSCH             SCK input high time             20         —           —           ns
SP72*         TSCL             SCK input low time              20         —           —           ns
SP73*         TDIV2SCH,        Setup time of SDI data          10         —           —           ns
              TDIV2SCL         input to SCK edge

SP74*         TSCH2DIL,        Hold time of SDI data            0         —           —           ns
              TSCL2DIL         input to SCK edge

SP75*         TDOR             SDO data output rise             —         10          25          ns       CL = 50 pF
                               time
SP76*         TDOF             SDO data output fall             —         10          25          ns       CL = 50 pF
                               time
SP77*         TSSH2DOZ         SS↑ to SDO output high-          —         —           85          ns
                               impedance
SP80*         TSCH2DOV,        SDO data output valid            —         —           85          ns
              TSCL2DOV         after SCK edge

SP82*         TSSL2DOV         SDO data output valid            —         —           85          ns
                               after SS↓ edge
SP83*         TSCH2SSH,        SS ↑ after SCK edge             20         —           —           ns
              TSCL2SSH

SP84*         TSSH2SSL         SS ↑ to SS↓ edge                47         —           —           ns


--- p910 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                                         Electrical Specifications

...........continued
Standard Operating Conditions (unless otherwise stated)
 Param No.           Sym.              Characteristic           Min.             Typ. †      Max.    Units       Conditions
* These parameters are characterized but not tested.
† Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
tested.
Note:
1.     SMP bit in the SPIxCON1 register must be set and the slew rate control must be disabled on the clock and data pins
       (clear the corresponding bits in SLRCONx register) for SPI to operate over 4 MHz.


Figure 47-13. SPI Host Mode Timing (CKE = 0, SMP = 0)
     SS
                       SP81
     SCK
     (CKP = 0)
                                SP71      SP72
                                                                           SP78           SP79

     SCK
     (CKP = 1)


                                                                              SP79        SP78
                        SP80

     SDO                                 MSb                bit 6 - - - - - -1             LSb


                                                 SP75, SP76

     SDI                               MSb In                bit 6 - - - -1                 LSb In

                                                  SP74
                               SP73
Note: Refer to the Load Conditions figure for more details.


--- p911 ---
                                                                                                                         PIC18F27/47/57Q43
                                                                                                                      Electrical Specifications

Figure 47-14. SPI Host Mode Timing (CKE = 1, SMP = 1)
  SS

                   SP81
  SCK
  (CKP = 0)
                             SP71       SP72
                                                                                               SP79
                             SP73
  SCK
  (CKP = 1)

                                           SP80
                                                                                               SP78


  SDO                      MSb                  bit 6 - - - - - -1                    LSb


                                    SP75, SP76

  SDI                     MSb In                 bit 6 - - - -1                       LSb In

                             SP74
Note: Refer to the Load Conditions figure for more details.

Figure 47-15. SPI Client Mode Timing (CKE = 0)

    SS

                     SP70

    SCK                                                                                                 SP83
    (CKP = 0)
                               SP71        SP72
                                                                                      SP78      SP79

    SCK
    (CKP = 1)


                                                                                      SP79       SP78
                      SP80

    SDO                                  MSb                         bit 6 - - - - - -1          LSb


                                                    SP75, SP76                                                 SP77

    SDI                                MSb In                        bit 6 - - - -1                   LSb In

                                          SP74

                                         SP73
Note: Refer to the Load Conditions figure for more details.


--- p912 ---
                                                                                                                               PIC18F27/47/57Q43
                                                                                                                            Electrical Specifications

        Figure 47-16. SPI Client Mode Timing (CKE = 1)

                                  SP82
           SS

                               SP70
           SCK                                                                                             SP83
           (CKP = 0)


                                           SP71        SP72

           SCK
           (CKP = 1)

                                                                                     SP80


           SDO                             MSb              bit 6 - - - - - -1              LSb

                                                                                                                         SP77
                                                  SP75, SP76

           SDI
                                      MSb In                  bit 6 - - - -1                LSb In

                                           SP74


        Note: Refer to the Load Conditions figure for more details.

47.4.16 I2C Bus Start/Stop Bits Requirements
        Table 47-23. I2C Start/Stop Requirements
        Standard Operating Conditions (unless otherwise stated)
        Param. No.     Sym.           Characteristic               Min. Typ. † Max. Units                            Conditions
        SP90*        TSU:STA Start condition 100 kHz mode 4700                 —     —      ns    Only relevant for Repeated Start condition
                              Setup time         400 kHz mode 600              —     —
                                                 1 MHz mode        260         —     —
        SP91*        THD:STA Start condition 100 kHz mode 4000                 —     —      ns    After this period, the first clock pulse is
                              Hold time                                                           generated
                                                 400 kHz mode 600              —     —
                                                 1 MHz mode        260         —     —
        SP92*        TSU:STO Stop condition 100 kHz mode 4000                  —     —      ns
                              Setup time         400 kHz mode 600              —     —
                                                 1 MHz mode        260         —     —
        SP93*        THD:STO Stop condition 100 kHz mode 4700                  —     —      ns
                              Hold time          400 kHz mode 1300             —     —
                                                 1 MHz mode        500         —     —
        * These parameters are characterized but not tested.


--- p913 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                              Electrical Specifications

       Figure 47-17. I2C Bus Start/Stop Bits Timing


           SCL
                                               SP91                                                                 SP93
                      SP90                                                                     SP92

           SDA


                                    Start                                                                Stop
                                  Condition                                                            Condition
       Note: Refer to the Load Conditions figure for more details.

47.4.17 I2C Bus Data Requirements
       Table 47-24. I2C Bus Data Requirements
        Standard Operating Conditions (unless otherwise stated)
         Param. No.        Sym.                 Characteristic                  Min.    Max.          Units        Conditions
        SP100*        THIGH            Clock high time    100 kHz               4000     —             ns     Device must operate
                                                          mode                                                at a minimum of 1.5
                                                                                                              MHz
                                                          400 kHz               600      —             ns     Device must operate
                                                          mode                                                at a minimum of 10
                                                                                                              MHz
                                                          1 MHz mode            260      —             ns     Device must operate
                                                                                                              at a minimum of 10
                                                                                                              MHz
        SP101*        TLOW             Clock low time     100 kHz               4700     —             ns     Device must operate
                                                          mode                                                at a minimum of 1.5
                                                                                                              MHz
                                                          400 kHz               1300     —             ns     Device must operate
                                                          mode                                                at a minimum of 10
                                                                                                              MHz
                                                          1 MHz mode            500      —             ns     Device must operate
                                                                                                              at a minimum of 10
                                                                                                              MHz
        SP102*        TR               SDA and SCL rise   100 kHz                —      1000           ns
                                       time               mode
                                                          400 kHz               20      300            ns     CB is specified to be
                                                          mode                                                from 10-400 pF
                                                          1 MHz mode             —      120
        SP103*        TF               SDA and SCL fall   100 kHz                —      250            ns
                                       time               mode
                                                          400 kHz          20 × (VDD/   250            ns     CB is specified to be
                                                          mode               5.5V)                            from 10-400 pF
                                                          1 MHz mode       20 × (VDD/   120            ns
                                                                             5.5V)
        SP106*        THD:DAT          Data input hold    100 kHz                0       —             ns
                                       time               mode
                                                          400 kHz                0       —             ns
                                                          mode
                                                          1 MHz mode             0       —             ns


--- p914 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                                         Electrical Specifications

...........continued
Standard Operating Conditions (unless otherwise stated)
 Param. No.          Sym.               Characteristic                  Min.      Max.         Units             Conditions
SP107*         TSU:DAT        Data input setup     100 kHz              250         —            ns      (Note 2)
                              time                 mode
                                                   400 kHz              100         —            ns
                                                   mode
                                                   1 MHz mode           50          —            ns
SP109*         TAA            Output valid from 100 kHz                  —        3450           ns      (Note 1)
                              clock             mode
                                                   400 kHz               —         900           ns
                                                   mode
                                                   1 MHz mode                      450           ns
SP110*         TBUF           Bus free time        100 kHz              4700        —            ns      Time the bus must
                                                   mode                                                  be free before a new
                                                                                                         transmission can start
                                                   400 kHz              1300        —            ns
                                                   mode
                                                   1 MHz mode           500         —            ns
SP111          CB             Bus capacitive       100 kHz               —         400           pF
                              loading              mode
                                                   400 kHz               —         400           pF
                                                   mode
                                                   1 MHz mode            —          26           pF      (Note 3)
* These parameters are characterized but not tested.
Notes:
1.   As a transmitter, the device must provide this internal minimum delay time to bridge the undefined region (min. 300 ns)
     of the falling edge of SCL to avoid unintended generation of Start or Stop conditions.
2.   A Fast mode (400 kHz) I2C bus device can be used in a Standard mode (100 kHz) I2C bus system, but the requirement
     TSU:DAT ≥ 250 ns must then be met. This will automatically be the case if the device does not stretch the low period of the
     SCL signal. If such a device does stretch the low period of the SCL signal, it must output the next data bit to the SDA line
     TR max. + TSU:DAT = 1000 + 250 = 1250 ns (according to the Standard mode I2C bus specification), before the SCL line is
     released.
3.   Using internal I2C pull-ups. For greater bus capacitance use external pull-ups.


Figure 47-18. I2C Bus Data Timing

                                       SP103       SP100                                              SP102
                                                               SP101

         SCL
                                SP90
                                                      SP106
                                                                          SP107
                             SP91                                                                         SP92
         SDA
         In
                                                                                                         SP110
                                                              SP109
                                              SP109
         SDA
         Out

Note: Refer to the Load Conditions figure for more details.


--- p915 ---
                                                                                                                                PIC18F27/47/57Q43
                                                                                                                             Electrical Specifications

47.4.18 Configurable Logic Cell (CLC) Characteristics
        Table 47-25. CLC Characteristics
         Standard Operating Conditions (unless otherwise stated)
         Operating Temperature: -40°C≤TA≤+125°C

          Param No.        Sym.                       Characteristic                      Min.      Typ. †      Max.         Units     Conditions
         CLC01*          TCLCIN      CLC input time                                         —            7       IO5     ns          (Note 1)
         CLC02*          TCLC        CLC module input to output propagation time            —          24          —     ns          VDD = 1.8V
                                                                                            —          12          —     ns          VDD > 3.6V
         CLC03*          TCLCOUT     CLC output time                   Rise Time            —          IO6         —     —           (Note 1)
                                                                        Fall Time           —          IO8         —     —           (Note 1)
         CLC04*          FCLCMAX     CLC maximum switching frequency                        —          —        OS20     —
         * These parameters are characterized but not tested.
         † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
         tested.
         Note:
         1.   See the “I/O and CLKOUT Timing Specifications” section for IO5, IO6 and IO8 rise and fall times.


        Figure 47-19. CLC Propagation Timing


                                           CLC         LCx_in[n](1)        CLC                               CLC
               CLCxINn
                                        Input time                        Module                          Output time
                                                                                                                                      CLCx
                                                                                      LCx_out(1)


                                           CLC                             CLC                               CLC
               CLCxINn                                                                                                                CLCx
                                        Input time     LCx_in[n](1)       Module      LCx_out(1)          Output time


                                         CLC01                             CLC02                             CLC03


47.4.19 Temperature Indicator Requirements
        Table 47-26. Temperature Indicator Requirements
         Standard Operating Conditions (unless otherwise stated)

          Param No.           Sym.                   Characteristic                  Min.        Typ. †       Max.       Units        Conditions
         TS01*           TACQMIN      Minimum ADC Acquisition Time Delay              —           25           —        µs
         TS02*           MV           Voltage Sensitivity         High Range          —          -3.75         —        mV/℃         TSRNG = 1
                                                                  Low Range           —          -2.75         —        mV/℃         TSRNG = 0
         * These parameters are characterized but not tested.
         † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
         tested.


--- p916 ---
