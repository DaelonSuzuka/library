                              PIC18(L)F26/27/45/46/47/55/56/57K42
44.0        ELECTRICAL SPECIFICATIONS
44.1        Absolute Maximum Ratings(†)
Ambient temperature under bias...................................................................................................... -40°C to +125°C
Storage temperature ........................................................................................................................ -65°C to +150°C
Voltage on pins with respect to VSS
      on VDD pin
                      PIC18F26/27/45/46/47/55/56/57K42 ........................................................................ -0.3V to +6.5V
                      PIC18LF26/27/45/46/47/55/56/57K42 ...................................................................... -0.3V to +4.0V
         on MCLR pin ........................................................................................................................... -0.3V to +9.0V
         on all other pins ............................................................................................................ -0.3V to (VDD + 0.3V)
Maximum current
     on VSS pin(1)
                      -40°C  TA  +85°C .............................................................................................................. 350 mA
                      85°C  TA  +125°C ............................................................................................................. 120 mA
      on VDD pin for 28-Pin devices(1)
                      -40°C  TA  +85°C .............................................................................................................. 250 mA
                      85°C  TA  +125°C ............................................................................................................... 85 mA
      on VDD pin for 40-Pin devices(1)
                      -40°C  TA  +85°C .............................................................................................................. 350 mA
                      85°C  TA  +125°C ............................................................................................................. 120 mA
     on any standard I/O pin ...................................................................................................................... 50 mA
Clamp current, IK (VPIN < 0 or VPIN > VDD) ................................................................................................... 20 mA
Total power dissipation(2)................................................................................................................................ 800 mW


 Note 1:        Maximum current rating requires even load distribution across I/O pins. Maximum current rating may be
                limited by the device package power dissipation characterizations, see Table 44-7 to calculate device
                specifications.
         2:     Power dissipation is calculated as follows:
               PDIS = VDD x {IDD - IOH} + VDD - VOH) x IOH} + VOI x IOL


 † NOTICE: Stresses above those listed under “Absolute Maximum Ratings” may cause permanent damage to the
 device. This is a stress rating only and functional operation of the device at those or any other conditions above those
 indicated in the operation listings of this specification is not implied. Exposure above maximum rating conditions for
 extended periods may affect device reliability.


 2017-2021 Microchip Technology Inc.                                                                                                DS40001919G-page 738
                              PIC18(L)F26/27/45/46/47/55/56/57K42
44.2        Standard Operating Conditions
The standard operating conditions for any device are defined as:
Operating Voltage:                    VDDMIN VDD VDDMAX
Operating Temperature:                TA_MIN TA TA_MAX
VDD — Operating Supply Voltage(1)
     PIC18LF26/27/45/46/47/55/56/57K42
                      VDDMIN (Fosc  16 MHz) ......................................................................................................... +1.8V
                      VDDMIN (Fosc  32 MHz) ......................................................................................................... +2.5V
                      VDDMIN (Fosc  64 MHz) ......................................................................................................... +2.7V
                      VDDMAX .................................................................................................................................... +3.6V
         PIC18F26/27/45/46/47/55/56/57K42
                VDDMIN (Fosc  16 MHz) ......................................................................................................... +2.3V
                      VDDMIN (Fosc  32 MHz) ......................................................................................................... +2.5V
                      VDDMIN (Fosc  64 MHz) ......................................................................................................... +2.7V
             VDDMAX .................................................................................................................................... +5.5V
TA — Operating Ambient Temperature Range
         Industrial Temperature
                   TA_MIN ..................................................................................................................................... -40°C
                 TA_MAX.................................................................................................................................... +85°C
         Extended Temperature
                      TA_MIN ..................................................................................................................................... -40°C
                      TA_MAX.................................................................................................................................. +125°C
 Note 1:        See Parameter Supply Voltage, DS Characteristics: Supply Voltage.


 2017-2021 Microchip Technology Inc.                                                                                                      DS40001919G-page 739
                                  PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-1:                      VOLTAGE FREQUENCY GRAPH, -40°C  TA +125°C, PIC18F26/27/45/46/47/55/
                                  56/57K42 ONLY


                    5.5


                    2.7
     VDD (V)


                    2.5


                    2.3


                          0             4                    10                    16              32                      64
                                                             Frequency (MHz)

                   Note 1: The shaded region indicates the permissible combinations of voltage and frequency.
                        2: Refer to Table 44-8 for each Oscillator mode’s supported frequencies.


FIGURE 44-2:                      VOLTAGE FREQUENCY GRAPH, -40°C  TA +125°C, PIC18LF26/27/45/46/47/55/
                                  56/57K42 ONLY


                      3.6
         VDD (V)


                      2.7

                      2.5


                      1.8

                              0             4                  10                    16             32                    64
                                                               Frequency (MHz)


      Note 1: The shaded region indicates the permissible combinations of voltage and frequency.
           2: Refer to Table 44-8 for each Oscillator mode’s supported frequencies.


 2017-2021 Microchip Technology Inc.                                                                           DS40001919G-page 740
                      PIC18(L)F26/27/45/46/47/55/56/57K42
44.3       DC Characteristics
TABLE 44-1:        SUPPLY VOLTAGE
PIC18LF26/27/45/46/47/55/56/57K42             Standard Operating Conditions (unless otherwise stated)

PIC18F26/27/45/46/47/55/56/57K42

 Param.
            Sym.          Characteristic       Min.    Typ.†   Max.    Units              Conditions
  No.
Supply Voltage
D002       VDD                                  1.8     —       3.6      V     FOSC  16 MHz
                                                2.5     —       3.6      V     FOSC  16 MHz
                                                2.7     —       3.6      V     FOSC  32 MHz
D002       VDD                                  2.3     —       5.5      V     FOSC  16 MHz
                                                2.5     —       5.5      V     FOSC 16 MHz
                                                2.7     —       5.5      V     FOSC  32 MHz
RAM Data Retention(1)
D003       VDR                                  1.5     —        —       V     Device in Sleep mode
D003       VDR                                  1.7     —        —       V     Device in Sleep mode
Power-on Reset Release Voltage(2)
D004       VPOR                                 —       1.6      —       V     BOR or LPBOR disabled(3)
D004       VPOR                                 —       1.6      —       V     BOR or LPBOR disabled(3)
Power-on Reset Rearm Voltage(2)
D005       VPORR                                —       0.8      —       V     BOR or LPBOR disabled(3)
D005       VPORR                                —       1.5      —       V     BOR or LPBOR disabled(3)
VDD Rise Rate to ensure internal Power-on Reset signal(2)
D006       SVDD                                0.05     —        —      V/ms BOR or LPBOR disabled(3)
D006       SVDD                                0.05     —        —      V/ms BOR or LPBOR disabled(3)
       †
       Data in “Typ.” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance
       only and are not tested.
Note 1: This is the limit to which VDD can be lowered in Sleep mode without losing RAM data.
     2: See Figure 44-3, POR and POR REARM with Slow Rising VDD.
     3: See Table 44-12 for BOR and LPBOR trip point information.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 741
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-3:           POR AND POR REARM WITH SLOW RISING VDD

               VDD


             VPOR
            VPORR
                                                                                SVDD

             VSS
          NPOR(1)


                                                    POR REARM


              VSS


                                              TVLOW(3)                TPOR(2)

             Note 1:     When NPOR is low, the device is held in Reset.
                  2:     TPOR 1 s typical.
                  3:     TVLOW 2.7 s typical.


 2017-2021 Microchip Technology Inc.                                                  DS40001919G-page 742
                         PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 44-2:           SUPPLY CURRENT (IDD)(1,2,4)
PIC18LF26/45/46/55/56K42                                                    Standard Operating Conditions (unless otherwise stated)

PIC18F26/45/46/55/56K42

Param.                                                                                                              Conditions
           Symbol                    Device Characteristics                 Min.   Typ.† Max. Units
 No.                                                                                                      VDD               Note
D100     IDDXT4         XT = 4 MHz                                           —      620   1000     A     3.0V
D100     IDDXT4         XT = 4 MHz                                           —      680    1100    A     3.0V
D100A    IDDXT4         XT = 4 MHz                                           —      400     —      A     3.0V     PMD’s all 1’s
D100A    IDDXT4         XT = 4 MHz                                           —      460     —      A     3.0V     PMD’s all 1’s
D101     IDDHFO16       HFINTOSC = 16 MHz                                    —      2.9    4.1    mA      3.0V
D101     IDDHFO16       HFINTOSC = 16 MHz                                    —       3     4.2    mA      3.0V
D101A    IDDHFO16       HFINTOSC = 16 MHz                                    —       2      —     mA      3.0V     PMD’s all 1’s
D101A    IDDHFO16       HFINTOSC = 16 MHz                                    —      2.1     —     mA      3.0V     PMD’s all 1’s
D102     IDDHFOPLL      HFINTOSC = 64 MHz                                    —     11.5    13.9   mA      3.0V
D102     IDDHFOPLL      HFINTOSC = 64 MHz                                    —     11.6     14    mA      3.0V
D102A    IDDHFOPLL      HFINTOSC = 64 MHz                                    —      7.5     —     mA      3.0V     PMD’s all 1’s
D102A    IDDHFOPLL      HFINTOSC = 64 MHz                                    —      7.6     —     mA      3.0V     PMD’s all 1’s
D103     IDDHSPLL64     HS+PLL = 64 MHz                                      —      9.8    12.9   mA      3.0V
D103     IDDHSPLL64     HS+PLL = 64 MHz                                      —      9.9     13    mA      3.0V
D103A    IDDHSPLL64     HS+PLL = 64 MHz                                      —      6.3     —     mA      3.0V     PMD’s all 1’s
D103A    IDDHSPLL64     HS+PLL = 64 MHz                                      —      6.4     —     mA      3.0V     PMD’s all 1’s
D104     IDDIDLE        Idle mode, HFINTOSC = 16 MHz                         —      1.8    2.8    mA      3.0V
D104     IDDIDLE        Idle mode, HFINTOSC = 16 MHz                         —      1.9    2.9    mA      3.0V
D105     IDDDOZE(3)     Doze mode, HFINTOSC = 16 MHz, Doze Ratio = 16        —      1.8     —     mA      3.0V
D105     IDDDOZE(3)     Doze mode, HFINTOSC = 16 MHz, Doze Ratio = 16        —      1.9     —     mA      3.0V
     † Data in “Typ.” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not tested.
Note 1:  The test conditions for all IDD measurements in active operation mode are: OSC1 = external square wave, from
         rail-to-rail; all I/O pins are outputs driven low; MCLR = VDD; WDT disabled.
      2: The supply current is mainly a function of the operating voltage and frequency. Other factors, such as I/O pin loading and
         switching rate, oscillator type, internal code execution pattern and temperature, also have an impact on the current consumption.
      3: IDDDOZE = [IDDIDLE*(N-1)/N] + IDDHFO16/N where N = Doze Ratio (Register 10-2).
      4: PMD bits are all in the default state, no modules are disabled.


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 743
                         PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 44-3:           SUPPLY CURRENT (IDD)(1,2,4,5)
PIC18LF27/47/57K42                                                          Standard Operating Conditions (unless otherwise stated)

PIC18F27/47/57K42

Param.                                                                                                             Conditions
           Symbol                    Device Characteristics                 Min.   Typ.† Max. Units
 No.                                                                                                      VDD              Note
D100     IDDXT4         XT = 4 MHz                                           —      750    1300    A     3.0V
D100     IDDXT4         XT = 4 MHz                                           —      810    1400    A     3.0V
D100A    IDDXT4         XT = 4 MHz                                           —      515     —      A     3.0V    PMD’s all 1’s
D100A    IDDXT4         XT = 4 MHz                                           —      575     —      A     3.0V    PMD’s all 1’s
D101     IDDHFO16       HFINTOSC = 16 MHz                                    —      3.4    4.7    mA      3.0V
D101     IDDHFO16       HFINTOSC = 16 MHz                                    —      3.5    4.8    mA      3.0V
D101A    IDDHFO16       HFINTOSC = 16 MHz                                    —      2.5     —     mA      3.0V    PMD’s all 1’s
D101A    IDDHFO16       HFINTOSC = 16 MHz                                    —      2.6     —     mA      3.0V    PMD’s all 1’s
D102     IDDHFOPLL      HFINTOSC = 64 MHz                                    —     12.5    18.5   mA      3.0V
D102     IDDHFOPLL      HFINTOSC = 64 MHz                                    —     12.6    18.6   mA      3.0V
D102A    IDDHFOPLL      HFINTOSC = 64 MHz                                    —      9.1     —     mA      3.0V    PMD’s all 1’s
D102A    IDDHFOPLL      HFINTOSC = 64 MHz                                    —      9.2     —     mA      3.0V    PMD’s all 1’s
D103     IDDHSPLL64     HS+PLL = 64 MHz                                      —     11.7    17.5   mA      3.0V
D103     IDDHSPLL64     HS+PLL = 64 MHz                                      —     11.8    17.6   mA      3.0V
D103A    IDDHSPLL64     HS+PLL = 64 MHz                                      —      8.2     —     mA      3.0V    PMD’s all 1’s
D103A    IDDHSPLL64     HS+PLL = 64 MHz                                      —      8.3     —     mA      3.0V    PMD’s all 1’s
D104     IDDIDLE        Idle mode, HFINTOSC = 16 MHz                         —      1.9    2.9    mA      3.0V
D104     IDDIDLE        Idle mode, HFINTOSC = 16 MHz                         —      2.0    3.0    mA      3.0V
D105     IDDDOZE(3)     Doze mode, HFINTOSC = 16 MHz, Doze Ratio = 16        —      1.6     —     mA      3.0V
D105     IDDDOZE(3)     Doze mode, HFINTOSC = 16 MHz, Doze Ratio = 16        —      1.7     —     mA      3.0V
     † Data in “Typ.” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not tested.
Note 1:  The test conditions for all IDD measurements in active operation mode are: OSC1 = external square wave, from
         rail-to-rail; all I/O pins are outputs driven low; MCLR = VDD; WDT disabled.
      2: The supply current is mainly a function of the operating voltage and frequency. Other factors, such as I/O pin loading and
         switching rate, oscillator type, internal code execution pattern and temperature, also have an impact on the current consumption.
      3: IDDDOZE = [IDDIDLE*(N-1)/N] + IDDHFO16/N where N = Doze Ratio (Register 10-2).
      4: PMD bits are all in the default state, no modules are disabled.
      5: Data in this table is Preliminary data.


 2017-2021 Microchip Technology Inc.                                                                           DS40001919G-page 744
                               PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 44-4:               POWER-DOWN CURRENT (IPD)(1,2)
PIC18LF26/27/45/46/47/55/56/57K42                                           Standard Operating Conditions (unless otherwise stated)

                                                                            Standard Operating Conditions (unless otherwise stated)
PIC18F26/27/45/46/47/55/56/57K42
                                                                            VREGPM = 1


Param.                                                                                Max.     Max.                        Conditions
              Symbol               Device Characteristics            Min.    Typ.†                      Units
 No.                                                                                 +85°C    +125°C             VDD               Note
D200         IPD            IPD Base                                  —       0.04     2.6      9.7      A      3.0V

D200         IPD            IPD Base                                  —       0.4       4        14      A      3.0V
D200A                                                                 —        20      32        42      A      3.0V   VREGPM = 0
D201         IPD_WDT        Low-Frequency Internal Oscillator/        —       0.8      3.6       12      A      3.0V
                            WDT
D201         IPD_WDT        Low-Frequency Internal Oscillator/        —        1       4.8       14      A      3.0V
                            WDT
D202         IPD_SOSC       Secondary Oscillator (SOSC)               —       0.9      5.6       18      A      3.0V   LP mode
D202         IPD_SOSC       Secondary Oscillator (SOSC)               —        1        6        19      A      3.0V   LP mode
D203         IPD_FVR        FVR                                       —        39      81        85      A      3.0V   FVRCON = 0x81 or 0x84
D203         IPD_FVR        FVR                                       —        33      76        81      A      3.0V   FVRCON = 0x81 or 0x84
D204         IPD_BOR        Brown-out Reset (BOR)                     —       9.4      15       20.6     A      3.0V
D204         IPD_BOR        Brown-out Reset (BOR)                     —       9.8      16       21.2     A      3.0V
D205         IPD_LPBOR      Low-Power Brown-out Reset (LPBOR)         —       0.1       3       10.8     A      3.0V
D206         IPD_HLVD       High/Low Voltage Detect (HLVD)            —       9.3     13.4      21.4     A      3.0V
D206         IPD_HLVD       High/Low Voltage Detect (HLVD)            —       9.5      14        22      A      3.0V
D207         IPD_ADCA       ADC - Nonconverting                       —       0.3      2.6      9.7      A      3.0V   ADC not converting (4)
D207         IPD_ADCA       ADC - Nonconverting                       —       0.4       4        14      A      3.0V   ADC not converting (4)
D208         IPD_CMP        Comparator                                —        25      48        56      A      3.0V
D208         IPD_CMP        Comparator                                —        26      49        57      A      3.0V
         †         Data in “Typ.” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
                   tested.
Note    1:         The peripheral current is the sum of the base IDD and the additional current consumed when this peripheral is enabled. The
                   peripheral ∆ current can be determined by subtracting the base IDD or IPD current from this limit. Max. values may be used when
                   calculating total current consumption.
        2:         The power-down current in Sleep mode does not depend on the oscillator type. Power-down current is measured with the part
                   in Sleep mode with all I/O pins in high-impedance state and tied to VSS.
        3:         All peripheral currents listed are on a per-peripheral basis if more than one instance of a peripheral is available.
        4:         ADC clock source is ADCRC.


 2017-2021 Microchip Technology Inc.                                                                                   DS40001919G-page 745
                       PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 44-5:        I/O PORTS
Standard Operating Conditions (unless otherwise stated)

 Param
            Sym.           Characteristic              Min.      Typ†       Max.     Units              Conditions
  No.

           VIL     Input Low Voltage
                   I/O PORT:
D300                  with TTL buffer                   —         —          0.8       V     4.5V  VDD  5.5V
D301                                                    —         —       0.15 VDD     V     1.8V  VDD < 4.5V
D302                  with Schmitt Trigger buffer       —         —        0.2 VDD     V     2.0V  VDD  5.5V
                               2
D303                  with I C levels                   —         —        0.3 VDD     V     2.0V  VDD  5.5V
D304                  with SMBus 2.0                    —         —          0.8       V     2.7V  VDD  5.5V
D305                  with SMBus 3.0                    —         —          0.8       V     1.8V  VDD  5.5V
D306               MCLR                                 —         —        0.2 VDD     V
           VIH     Input High Voltage
                   I/O PORT:
D320                  with TTL buffer                  2.0        —          —         V     4.5V  VDD 5.5V
D321                                                0.25 VDD +    —          —         V     1.8V  VDD < 4.5V
                                                        0.8
D322                  with Schmitt Trigger buffer    0.8 VDD      —          —         V     2.0V  VDD  5.5V
D323                  with I2C levels                0.7 VDD      —          —         V
D324                  with SMBus 2.0                   2.1        —          —         V     2.7V  VDD  5.5V
D325                  with SMBus 3.0                   1.35       —          —         V     1.8V  VDD  5.5V
D326               MCLR                              0.7 VDD      —          —         V
           IIL     Input Leakage Current(1)
D340               I/O Ports                            —         ±5        ± 125     nA     VSS  VPIN  VDD,
                                                                                             Pin at high-impedance, 85°C
D341                                                    —         ±5       ± 1000     nA     VSS  VPIN  VDD,
                                                                                             Pin at high-impedance, 125°C
D342               MCLR(2)                              —        ± 50       ± 200     nA     VSS  VPIN  VDD,
                                                                                             Pin at high-impedance, 85°C
           IPUR    Weak Pull-up Current
D350                                                   25         120        200      A     VDD = 3.0V, VPIN = VSS
           VOL     Output Low Voltage
D360               I/O ports                            —         —          0.6       V     IOL = 10.0 mA, VDD = 3.0V
           VOH     Output High Voltage
D370               I/O ports                        VDD - 0.7     —          —         V     IOH = 6.0 mA, VDD = 3.0V
D380       CIO     All I/O pins                         —          5         50        pF
       †Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are
        not tested.
Note 1: Negative current is defined as current sourced by the pin.
     2: The leakage current on the MCLR pin is strongly dependent on the applied voltage level. The specified levels represent
        normal operating conditions. Higher leakage current may be measured at different input voltages.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 746
                        PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 44-6:         MEMORY PROGRAMMING SPECIFICATIONS
Standard Operating Conditions (unless otherwise stated)
 Param
             Sym.              Characteristic                 Min.       Typ†       Max.     Units           Conditions
  No.
Data EEPROM Memory Specifications
MEM20 ED            DataEE Byte Endurance                    100k          —         —       E/W     -40C  TA  +85C
MEM21 TD_RET        Characteristic Retention                   —          40         —       Year    Provided no other
                                                                                                     specifications are violated
MEM22 ND_REF        Total Erase/Write Cycles before           1M          10M        —        E/W    -40C  TA  +60C
                    Refresh                                  500k          —         —               -40C  TA  +85C
MEM23 VD_RW         VDD for Read or Erase/Write             VDDMIN         —      VDDMAX       V
                    operation
MEM24 TD_BEW Byte Erase and Write Cycle Time                   —          4.0        5.0      ms
Program Flash Memory Specifications
MEM30 EP            Memory Cell Endurance                     10k          —         —       E/W     -40C  TA  +85C
                                                                                                     (Note 1)
MEM32 TP_RET        Characteristic Retention                   —          40         —       Year    Provided no other
                                                                                                     specifications are violated

MEM33 VP_RD         VDD for Read operation                  VDDMIN         —      VDDMAX       V
MEM34 VP_REW VDD for Row Erase or Write                     VDDMIN         —      VDDMAX       V
             operation
MEM35 TP_REW Self-Timed Row Erase or Self-Timed                —          2.0        2.5      ms
             Write
         †   Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are
             not tested.
Note 1:      Memory Cell Endurance for the Program memory is defined as: One Row Erase operation and one Self-Timed Write.


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 747
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-7:         THERMAL CHARACTERISTICS
Standard Operating Conditions (unless otherwise stated)

 Param
            Sym.                   Characteristic                   Typ.        Units                       Conditions
  No.

TH01         JA     Thermal Resistance Junction to Ambient          60         C/W        28-pin SPDIP package
                                                                     80         C/W        28-pin SOIC package
                                                                     90         C/W        28-pin SSOP package
                                                                    27.5        C/W        28-pin UQFN 4x4 mm package
                                                                    27.5        C/W        28-pin QFN 6x6mm package
                                                                    47.2        C/W        40-pin PDIP package
                                                                    28.1        C/W        40-pin UQFN package
                                                                     46         C/W        44-pin TQFP package
                                                                    24.4        C/W        44-pin QFN 8x8mm package
                                                                    58.6        C/W        48-pin TQFP package
                                                                    21.7        C/W        48-pin UQFN package
                                                                    21.8        C/W        48-pin VQFN package
                                                                    21.8        C/W        48-pin VQFN package with Wettable
                                                                                            Flanks package
TH02         JC     Thermal Resistance Junction to Case            31.4        C/W        28-pin SPDIP package
                                                                     24         C/W        28-pin SOIC package
                                                                     24         C/W        28-pin SSOP package
                                                                     24         C/W        28-pin UQFN 4x4mm package
                                                                     24         C/W        28-pin QFN 6x6mm package
                                                                    24.7        C/W        40-pin PDIP package
                                                                    14.5        C/W        40-pin UQFN package
                                                                    14.5        C/W        40-pin TQFP package
                                                                     20         C/W        44-pin QFN 8x8mm package
                                                                    16.1        C/W        48-pin TQFP package
                                                                    6.44        C/W        48-pin UQFN package
                                                                    9.94        C/W        48-pin VQFN package
                                                                    9.94        C/W        48-pin VQFN package with Wettable
                                                                                            Flanks package
TH03       TJMAX     Maximum Junction Temperature                   150          C
TH04         PD      Power Dissipation                               —           W          PD = PINTERNAL + PI/O(3)
TH05     PINTERNAL Internal Power Dissipation                        —           W          PINTERNAL = IDD x VDD(1)
TH06        PI/O     I/O Power Dissipation                           —           W          PI/O =  (IOL * VOL) +  (IOH * (VDD - VOH))
TH07        PDER     Derated Power                                   —           W          PDER = PDMAX (TJ - TA)/JA(2)
Note 1: IDD is current to run the chip alone without driving any load on the output pins.
     2: TA = Ambient Temperature, TJ = Junction Temperature
     3: See absolute maximum ratings for total power dissipation.


 2017-2021 Microchip Technology Inc.                                                                         DS40001919G-page 748
                        PIC18(L)F26/27/45/46/47/55/56/57K42
44.4     AC Characteristics

FIGURE 44-4:             LOAD CONDITIONS


                                                Rev. 10-000133A
                                                        8/1/2013


                     Load Condition

          Pin

                                      CL

                                      VSS


                Legend: CL=50 pF for all pins


 2017-2021 Microchip Technology Inc.                              DS40001919G-page 749
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-5:                CLOCK TIMING
                                Q4                Q1                Q2            Q3             Q4                 Q1


             CLKIN
                                                             OS2/OS4/OS6                       OS2/OS4/OS6
                                            OS1/OS3/OS5/
                                            OS7/OS8/OS9/
                                            OS10/OS20/OS21
   CLKOUT                                                                 OS21
   (CLKOUT Mode)


    Note    1:     See Table 44-8.


TABLE 44-8:             EXTERNAL CLOCK/OSCILLATOR TIMING REQUIREMENTS
Standard Operating Conditions (unless otherwise stated)

 Param
                 Sym.                Characteristic          Min.        Typ†     Max.   Units               Conditions
  No.
ECL Clock
OS1         FECL          Clock Frequency                    —             —      500    kHz
OS2         TECL_DC       Clock Duty Cycle                   40            —       60     %
ECM Clock
OS3         FECM          Clock Frequency                    —             —       8     MHz
OS4         TECM_DC       Clock Duty Cycle                   40            —       60     %
ECH Clock
OS5         FECH          Clock Frequency                    —             —      64     MHz
OS6         TECH_DC       Clock Duty Cycle                   40            —       60     %
LP Oscillator
OS7         FLP           Clock Frequency                    —             —      100    kHz     Note 4
XT Oscillator
OS8         FXT           Clock Frequency                    —             —       4     MHz     Note 4
HS Oscillator
OS9         FHS           Clock Frequency                    —             —      20     MHz     Note 4
Secondary Oscillator
OS10        FSEC          Clock Frequency                    32.4        32.768   33.1   kHz
System Oscillator
OS20        FOSC          System Clock Frequency             —             —       64    MHz     (Note 2, Note 3)
       *These parameters are characterized but not tested.
       †
       Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are
       not tested.
Note 1: Instruction cycle period (TCY) equals four times the input oscillator time base period. All specified values are based on
         characterization data for that particular oscillator type under standard operating conditions with the device executing
         code. Exceeding these specified limits may result in an unstable oscillator operation and/or higher than expected
         current consumption. All devices are tested to operate at “min” values with an external clock applied to OSC1 pin.
         When an external clock input is used, the “max” cycle time limit is “DC” (no clock) for all devices.
     2: The system clock frequency (FOSC) is selected by the “main clock switch controls” as described in Section 10.0
         “Power-Saving Operation Modes”.
     3: The system clock frequency (FOSC) must meet the voltage requirements defined in the Section 44.2 “Standard
         Operating Conditions”.
       4:    LP, XT and HS oscillator modes require an appropriate crystal or resonator to be connected to the device. For clocking
             the device with the external square wave, one of the EC mode selections must be used.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 750
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-8:          EXTERNAL CLOCK/OSCILLATOR TIMING REQUIREMENTS (CONTINUED)
Standard Operating Conditions (unless otherwise stated)

 Param
              Sym.              Characteristic             Min.      Typ†      Max.      Units              Conditions
  No.
OS21        FCY        Instruction Frequency                —       FOSC/4      —        MHz
OS22        TCY        Instruction Period                  62.5     1/FCY       —         ns
       *These parameters are characterized but not tested.
       †
       Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are
       not tested.
Note 1: Instruction cycle period (TCY) equals four times the input oscillator time base period. All specified values are based on
         characterization data for that particular oscillator type under standard operating conditions with the device executing
         code. Exceeding these specified limits may result in an unstable oscillator operation and/or higher than expected
         current consumption. All devices are tested to operate at “min” values with an external clock applied to OSC1 pin.
         When an external clock input is used, the “max” cycle time limit is “DC” (no clock) for all devices.
     2: The system clock frequency (FOSC) is selected by the “main clock switch controls” as described in Section 10.0
         “Power-Saving Operation Modes”.
     3: The system clock frequency (FOSC) must meet the voltage requirements defined in the Section 44.2 “Standard
         Operating Conditions”.
       4:    LP, XT and HS oscillator modes require an appropriate crystal or resonator to be connected to the device. For clocking
             the device with the external square wave, one of the EC mode selections must be used.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 751
                                       PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-9:                         INTERNAL OSCILLATOR PARAMETERS(1)
Standard Operating Conditions (unless otherwise stated)

 Param
                             Sym.               Characteristic            Min.     Typ†     Max. Units             Conditions
  No.
OS50                  FHFOSC           Precision Calibrated HFINTOSC       —         4       —     MHz (Note 2)
                                       Frequency                                     8
                                                                                    12
                                                                                    16
                                                                                    48
                                                                                    64
OS51                  FHFOSCLP Low-Power Optimized HFINTOSC               0.92        1     1.08   MHz     -40°C to 85°C
                               Frequency                                  1.84        2     2.16   MHz     -40°C to 85°C
                                                                          0.88        1     1.12   MHz     -40°C to 125°C
                                                                          1.76        2     2.24   MHz     -40°C to 125°C
OS53*                 FLFOSC           Internal LFINTOSC Frequency        24.80     31      37.2   kHz
OS54*                 THFOSCST HFINTOSC                                    —        11      20     s      VREGPM = 0
                               Wake-up from Sleep Start-up                 —        50      —      s      VREGPM = 1
                               Time
OS56                  TLFOSCST         LFINTOSC                            —       0.2       —     ms
                                       Wake-up from Sleep Start-up Time
      *These parameters are characterized but not tested.
      †Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance
       only and are not tested.
Note 1: To ensure these oscillator frequency tolerances, VDD and VSS must be capacitively decoupled as close to
        the device as possible. 0.1 F and 0.01 F values in parallel are recommended.
     2: See Figure 44-6: Precision Calibrated HFINTOSC and MFINTOSC Frequency Accuracy Over Device VDD
        and Temperature.

FIGURE 44-6:                           PRECISION CALIBRATED HFINTOSC AND MFINTOSC FREQUENCY
                                       ACCURACY OVER DEVICE VDD AND TEMPERATURE


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
                                 1.8     2.0        2.3          3.0       3.5            4.0        4.5         5.0        5.5

                                                                                  VDD (V)


 2017-2021 Microchip Technology Inc.                                                                             DS40001919G-page 752
                      PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-10: PLL SPECIFICATIONS
Standard Operating Conditions (unless otherwise stated) VDD 2.5V
 Param
            Sym.                    Characteristic              Min.      Typ†       Max.     Units Conditions
  No.
PLL01     FPLLIN     PLL Input Frequency Range                    4         —         16       MHz
PLL02     FPLLOUT PLL Output Frequency Range                     16         —         64       MHz Note 1
PLL03     TPLLST     PLL Lock Time from Start-up                 —         200        —         s
PLL04     FPLLJIT    PLL Output Frequency Stability (Jitter)    -0.25       —        0.25       %
      * These parameters are characterized but not tested.
      † Data in “Typ” column is at 5V, 25C unless otherwise stated. These parameters are for design guidance
        only and are not tested.
Note 1: The output frequency of the PLL must meet the FOSC requirements listed in Parameter D002.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 753
                          PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-7:               CLKOUT AND I/O TIMING

       Cycle                 Write                       Fetch                       Read                    Execute
                              Q4                          Q1                          Q2                       Q3
        FOSC
                                                      IO1                                                IO2
                                                                                     IO10
  CLKOUT
                                                         IO8                         IO4                      IO7
                                                                             IO5
       I/O pin
       (Input)
                                                   IO3
    I/O pin              Old Value                                                                           New Value
    (Output)
                                                                  IO7, IO8


TABLE 44-11:            I/O AND CLKOUT TIMING SPECIFICATIONS
Standard Operating Conditions (unless otherwise stated)
Param
                 Sym.                  Characteristic                         Min.          Typ† Max. Units         Conditions
 No.
IO1*       TCLKOUTH       CLKOUT rising edge delay (rising edge                —             —    70    ns
                          Fosc (Q1 cycle) to falling edge CLKOUT
IO2*       TCLKOUTL       CLKOUT falling edge delay (rising edge               —             —    72    ns
                          Fosc (Q3 cycle) to rising edge CLKOUT
IO3*       TIO_VALID      Port output valid time (rising edge Fosc             —             50   70    ns
                          (Q1 cycle) to port valid)
IO4*       TIO_SETUP      Port input setup time (Setup time before             20            —    —     ns
                          rising edge Fosc – Q2 cycle)
IO5*       TIO_HOLD       Port input hold time (Hold time after rising         50            —    —     ns
                          edge Fosc – Q2 cycle)
IO6*       TIOR_SLREN Port I/O rise time, slew rate enabled                    —             25   —     ns     VDD = 3.0V
IO7*       TIOR_SLRDIS Port I/O rise time, slew rate disabled                  —             5    —     ns     VDD = 3.0V
IO8*       TIOF_SLREN     Port I/O fall time, slew rate enabled                —             25   —     ns     VDD = 3.0V
IO9*       TIOF_SLRDIS Port I/O fall time, slew rate disabled                  —             5    —     ns     VDD = 3.0V
IO10*      TINT           INT pin high or low time to trigger an               25            —    —     ns
                          interrupt

IO11*      TIOC           Interrupt-on-Change minimum high or low              25            —    —     ns
                          time to trigger interrupt
*These parameters are characterized but not tested.


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 754
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-8:           RESET, WATCHDOG TIMER, OSCILLATOR START-UP TIMER AND POWER-UP
                       TIMER TIMING


             VDD

          MCLR

                                                                        RST01
         Internal
            POR

                                RST04
          PWRT
        Time-out                            RST05
            OSC
   Start-up Time


 Internal Reset(1)

 Watchdog Timer
       Reset(1)
                                                                                         RST03
                                                                      RST02
                                                                                                      RST02
         I/O pins


        Note 1: Asserted low.


FIGURE 44-9:           BROWN-OUT RESET TIMING AND CHARACTERISTICS

            VDD
                                                                        VBOR and VHYST
                       VBOR


                                        (Device in Brown-out Reset)                  (Device not in Brown-out Reset)


                     RST08


         Reset
                                                                         RST04(1)
 (due to BOR)


        Note 1: Delay depends on PWRTS[1:0] Configuration bits.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 755
                          PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-12: RESET, WDT, OSCILLATOR START-UP TIMER, POWER-UP TIMER, BROWN-OUT
             RESET AND LOW-POWER BROWN-OUT RESET SPECIFICATIONS
Standard Operating Conditions (unless otherwise stated)

 Param
             Sym.                  Characteristic                 Min.     Typ†   Max.    Units             Conditions
  No.

RST01*    TMCLR      MCLR Pulse Width Low to ensure Reset             2     —      —       s
RST02*    TIOZ       I/O high-impedance from Reset detection          —     —      2       s
RST03     TWDT       Watchdog Timer Time-out Period                   —     16     —       ms     1:512 Prescaler
RST04*    TPWRT      Power-up Timer Period                            —     1      —       ms     PWRTS = 00
                                                                            16             ms     PWRTS = 01
                                                                            64             ms     PWRTS = 10
RST05     TOST       Oscillator Start-up Timer Period(1,2)            —    1024    —      TOSC
RST06     VBOR       Brown-out Reset Voltage(4)                   2.7      2.85    3.0     V      BORV = 00
                                                                  2.55      2.7   2.85     V      BORV = 01
                                                                  2.3      2.45    2.6     V      BORV = 10
                                                                  2.3      2.45    2.6     V      BORV = 11 (PIC18Fxxx)
                                                                  1.8       1.9    2.1     V      BORV = 11 (PIC18LFxxx)
RST07     VBORHYS Brown-out Reset Hysteresis                          —     40     —      mV
RST08     TBORDC     Brown-out Reset Response Time                    —     3      —       s
RST09     VLPBOR     Low-Power Brown-out Reset Voltage            1.8       2     2.5      V      PIC18LFXXX only
      *These parameters are characterized but not tested.
      †Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
       tested.
Note 1: By design, the Oscillator Start-up Timer (OST) counts the first 1024 cycles, independent of frequency.
     2: To ensure these voltage tolerances, VDD and VSS must be capacitively decoupled as close to the device as possible.
         0.1 F and 0.01 F values in parallel are recommended.


TABLE 44-13: HIGH/LOW-VOLTAGE DETECT CHARACTERISTICS
Standard Operating Conditions (unless otherwise stated)
Param. No.       Symbol       Characteristic         Min.     Typ†        Max.    Units                 Conditions
HLVD01            VDET       Voltage Detection      1.73(1)    1.90       2.07     V      HLVDSEL[3:0]=0000
                                                     1.91      2.10       2.29     V      HLVDSEL[3:0]=0001
                                                     2.05      2.25       2.45     V      HLVDSEL[3:0]=0010
                                                     2.28      2.50       2.73     V      HLVDSEL[3:0]=0011
                                                     2.37      2.60       2.83     V      HLVDSEL[3:0]=0100
                                                     2.50      2.75       3.00     V      HLVDSEL[3:0]=0101
                                                     2.64      2.90       3.16     V      HLVDSEL[3:0]=0110
                                                     2.87      3.15       3.43     V      HLVDSEL[3:0]=0111
                                                     3.05      3.35       3.65     V      HLVDSEL[3:0]=1000
                                                     3.28      3.60       3.92     V      HLVDSEL[3:0]=1001
                                                     3.41      3.75       4.09     V      HLVDSEL[3:0]=1010
                                                     3.64      4.00       4.36     V      HLVDSEL[3:0]=1011
                                                     3.82      4.20       4.58     V      HLVDSEL[3:0]=1100
                                                     3.96      4.35       4.74     V      HLVDSEL[3:0]=1101
                                                     4.23      4.65       5.07     V      HLVDSEL[3:0]=1110
      * These parameters are characterized but not tested.
      † Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are
        not tested.
Note 1: Device operation below VDD = 1.8 V is not recommended.


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 756
                          PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-14:         ANALOG-TO-DIGITAL CONVERTER (ADC) ACCURACY SPECIFICATIONS(1,2):
Operating Conditions (unless otherwise stated)
VDD = 3.0V, TA = 25°C, TAD = 1s
Param
            Sym.                Characteristic         Min.    Typ†     Max.    Units                 Conditions
 No.
AD01       NR      Resolution                           —        —        12     bit
AD02       EIL     Integral Error                       —       ±0.1     ±2.0    LSb ADCREF+ = 3.0V, ADCREF-= 0V
AD03       EDL     Differential Error                   —       ±0.1     ±1.0    LSb ADCREF+ = 3.0V, ADCREF-= 0V
AD04       EOFF    Offset Error                         —       0.5      6.0     LSb ADCREF+ = 3.0V, ADCREF-= 0V
AD05       EGN     Gain Error                           —       ±0.2     ±6.0    LSb ADCREF+ = 3.0V, ADCREF-= 0V
AD06       VADREF ADC Reference Voltage                1.8       —       VDD      V
                  (ADREF+ - ADREF-)
AD07       VAIN    Full-Scale Range                  ADREF-      —     ADREF+     V
AD08       ZAIN    Recommended Impedance of             —        1        —      k
                   Analog Voltage Source
AD09       RVREF   ADC Voltage Reference Ladder         —        50       —      k     Note 3
                   Impedance
       *These parameters are characterized but not tested.
       †Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
        tested.
Note 1: Total Absolute Error is the sum of the offset, gain and integral nonlinearity (INL) errors.
     2: The ADC conversion result never decreases with an increase in the input and has no missing codes.
     3: This is the impedance seen by the VREF pads when the external reference pads are selected.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 757
                              PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-15: ANALOG-TO-DIGITAL CONVERTER (ADC) CONVERSION TIMING SPECIFICATIONS
Standard Operating Conditions (unless otherwise stated)

Param
      Sym.                     Characteristic             Min.           Typ†         Max.   Units                Conditions
 No.
                                                                                                     Using FOSC as the ADC clock
AD20                                                       0.5            —            9      s
                                                                                                     source ADCS = 1
           TAD     ADC Clock Period
                                                                                                     Using ADCRC as the ADC clock
AD21                                                        —             2            —      s
                                                                                                     source ADCS = 0
                                                                                                     Using FOSC as the ADC clock
                                                            —     14 TAD + 2 TCY       —      —
                                                                                                     source ADCS = 1
AD22       TCNV Conversion Time
                                                                                                     Using ADCRC as the ADC clock
                                                            —     16 TAD + 2 TCY       —      —
                                                                                                     source ADCS = 0
                                                                                                     Using FOSC as the ADC clock
                                                            —        2 TAD + 1 TCY     —      —
                                                                                                     source ADCS = 1
                   Sample and Hold Capacitor
AD24       THCD                                                                                      Using ADCRC as the ADC clock
                   Disconnect Time
                                                            —        3 TAD + 2 TCY     —      —      source ADCS = 0

       *      These parameters are characterized but not tested.
       †      Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
              tested.


FIGURE 44-10:                 ADC CONVERSION TIMING (ADC CLOCK FOSC-BASED)
                                                                                                                               Rev. 10-000321B
                                                                                                                                       6/1/2017


  BSF ADCON0, GO
                                                                                                         1 TCY
                                                           AD22
                              AD24                                                                                1 TCY
                      1 TCY                                                          AD20

  ADC_clk


   ADRES                                                    OLD DATA                                                  NEW DATA


       ADIF


        GO                                                                                                         DONE


   Sample                                         Sampling Stopped


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 758
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-11:                  ADC CONVERSION TIMING (ADC CLOCK FROM ADCRC)
                                                                                                       Rev. 10-000328B
                                                                                                               6/1/2017


   BSF ADCON0, GO
                                                                                           1 TCY
                                                     AD22
                                 AD24
                    2 TCY(1)                                             AD21

   ADC_clk


    ADRES                                             OLD DATA                                 NEW DATA


      ADIF


       GO                                                                                   DONE


    Sample                                      Sampling Stopped


  Note 1: If the ADC clock source is selected as ADCRC, a time of TCY is added before the ADC clock starts. This
          allows the SLEEP instruction to be executed.


 2017-2021 Microchip Technology Inc.                                                     DS40001919G-page 759
                           PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-16:            COMPARATOR SPECIFICATIONS
Operating Conditions (unless otherwise stated)
VDD = 3.0V, TA = 25°C

  Param
                 Sym.                   Characteristics                 Min.         Typ.         Max.            Units               Comments
   No.
CM01         VIOFF          Input Offset Voltage                         —            —           ±60              mV      VICM = VDD/2
CM02         VICM           Input Common Mode Range                     GND           —           VDD              V
CM03         CMRR           Common Mode Input Rejection Ratio            —            50             —             dB
CM04         VHYST          Comparator Hysteresis                        10           25             40            mV
CM05         TRESP(1)       Response Time, Rising Edge                   —           300          900              ns
                            Response Time, Falling Edge                  —           220          500              ns
         *   These parameters are characterized but not tested.
Note    1:   Response time measured with one comparator input at VDD/2, while the other input transitions from VSS to VDD.
        2:   A mode change includes changing any of the control register values, including module enable.


TABLE 44-17: 5-BIT DAC SPECIFICATIONS
Standard Operating Conditions (unless otherwise stated)
VDD = 3.0V, TA = 25°C

  Param
                 Sym.          Characteristics            Min.                Typ.                        Max.          Units            Comments
   No.

DSB01         VLSB         Step Size                       —      (VDACREF+ -VDACREF-) /                   —              V
                                                                           32
DSB01         VACC         Absolute Accuracy               —                   —                           0.5           LSb
DSB03*        RUNIT        Unit Resistor Value             —                  5000                         —              
DSB04*        TST          Settling Time(1)                —                   —                           10             s
         *   These parameters are characterized but not tested.
         †   Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not tested.
Note    1:   Settling time measured while DACR[4:0] transitions from ‘00000’ to ‘01111’.


TABLE 44-18: FIXED VOLTAGE REFERENCE (FVR) SPECIFICATIONS
Standard Operating Conditions (unless otherwise stated)

 Param.
              Symbol               Characteristic                Min.          Typ.          Max.          Units                     Conditions
  No.
FVR01        VFVR1         1x Gain (1.024V)                       -4            —               +4           %          VDD  2.5V, -40°C to 85°C
FVR02        VFVR2         2x Gain (2.048V)                       -4            —               +4           %          VDD  2.5V, -40°C to 85°C
FVR03        VFVR4         4x Gain (4.096V)                       -5            —               +5           %          VDD  4.75V, -40°C to 85°C
FVR04        TFVRST        FVR Start-up Time                     —              25              —            us

TABLE 44-19: ZERO-CROSS DETECT (ZCD) SPECIFICATIONS
Standard Operating Conditions (unless otherwise stated)
VDD = 3.0V, TA = 25°C

   Param.
                    Sym.                Characteristics                  Min           Typ†                 Max            Units         Comments
    No.
ZC01           VPINZC       Voltage on Zero Cross Pin                     —                0.75              —                 V
ZC02           IZCD_MAX     Maximum source or sink current                —                 —               600               A
ZC03           TRESPH       Response Time, Rising Edge                    —                 1                —                s
               TRESPL       Response Time, Falling Edge                   —                 1                —                s
         †   Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not tested.


 2017-2021 Microchip Technology Inc.                                                                                              DS40001919G-page 760
                        PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-12:            TIMER0 AND TIMER1 EXTERNAL CLOCK TIMINGS


           T0CKI

                                                  40                         41


                                                                42


           T1CKI

                                                   45                        46


                                                                 47                               49


           TMR0 or
           TMR1


TABLE 44-20: TIMER0 AND TIMER1 EXTERNAL CLOCK REQUIREMENTS
Standard Operating Conditions (unless otherwise stated)
Operating Temperature -40°C TA +125°C
Param
             Sym.                      Characteristic                        Min.         Typ†   Max.     Units       Conditions
 No.
40*       TT0H         T0CKI High Pulse Width           No Prescaler     0.5 TCY + 20      —       —       ns
                                                        With Prescaler        10           —       —       ns
41*       TT0L         T0CKI Low Pulse Width            No Prescaler     0.5 TCY + 20      —       —       ns
                                                        With Prescaler        10           —       —       ns
42*       TT0P         T0CKI Period                                        Greater of:     —       —       ns     N = prescale value
                                                                         20 or TCY + 40
                                                                                  N
45*       TT1H         T1CKI High Synchronous, No Prescaler              0.5 TCY + 20      —       —       ns
                       Time       Synchronous, with Prescaler                 15           —       —       ns
                                      Asynchronous                            30           —       —       ns
46*       TT1L         T1CKI Low      Synchronous, No Prescaler          0.5 TCY + 20      —       —       ns
                       Time           Synchronous, with Prescaler             15           —       —       ns
                                      Asynchronous                            30           —       —       ns
47*       TT1P         T1CKI Input Synchronous                             Greater of:     —       —       ns     N = prescale value
                       Period                                            30 or TCY + 40
                                                                                  N
                                      Asynchronous                            60           —       —       ns
49*       TCKEZTMR1 Delay from External Clock Edge to Timer                 2 TOSC         —     7 TOSC    —      Timers in Sync
                    Increment                                                                                     mode
      *    These parameters are characterized but not tested.
      †    Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
           tested.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 761
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-13:           CAPTURE/COMPARE/PWM TIMINGS (CCP)
                         CCPx
                (Capture mode)


                                                               CC01               CC02

                                                                          CC03

      Note:   Refer to Figure 44-4 for load conditions.


TABLE 44-21: CAPTURE/COMPARE/PWM REQUIREMENTS (CCP)
Standard Operating Conditions (unless otherwise stated)
Operating Temperature -40°C  TA  +125°C
Param
      Sym.                    Characteristic                    Min.       Typ†    Max.   Units             Conditions
 No.
CC01* TccL      CCPx Input Low Time       No Prescaler      0.5TCY + 20     —       —       ns
                                          With Prescaler         20         —       —       ns
CC02* TccH      CCPx Input High Time      No Prescaler      0.5TCY + 20     —       —       ns
                                          With Prescaler         20         —       —       ns
CC03* TccP      CCPx Input Period                            3TCY + 40      —       —       ns    N = prescale value
                                                                N
      *   These parameters are characterized but not tested.
      †   Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance only and are not
          tested.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 762
                        PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-14:           SPI HOST MODE TIMING (CKE = 0, SMP = 0)


    SS

                         SP81
    SCK
    (CKP = 0)
                                  SP71       SP72
                                                                                      SP78          SP79

    SCK
    (CKP = 1)


                                                                                          SP79      SP78
                         SP80

    SDO                                     MSb                      bit 6 - - - - - -1              LSb


                                                       SP75, SP76

    SDI                                   MSb In                         bit 6 - - - -1               LSb In

                                                        SP74
                                SP73

    Note: Refer to Figure 44-4 for load conditions.


FIGURE 44-15:           SPI HOST MODE TIMING (CKE = 1, SMP = 1)


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


     SDO                        MSb                    bit 6 - - - - - -1                   LSb


                                          SP75, SP76

     SDI                       MSb In                   bit 6 - - - -1                     LSb In

                                  SP74

     Note: Refer to Figure 44-4 for load conditions.


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 763
                        PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-16:            SPI CLIENT MODE TIMING (CKE = 0)


    SS

                        SP70

    SCK                                                                                                    SP83
    (CKP = 0)
                                  SP71        SP72
                                                                                       SP78         SP79

    SCK
    (CKP = 1)


                                                                                       SP79         SP78
                         SP80

    SDO                                     MSb                       bit 6 - - - - - -1            LSb


                                                       SP75, SP76                                                 SP77

    SDI                                   MSb In                      bit 6 - - - -1                  LSb In

                                             SP74

                                            SP73

    Note: Refer to Figure 44-4 for load conditions.


FIGURE 44-17:            SPI CLIENT MODE TIMING (CKE = 1)

                            SP82
     SS

                         SP70
     SCK                                                                                                   SP83
     (CKP = 0)


                                   SP71       SP72


     SCK
     (CKP = 1)

                                                                                SP80


     SDO                           MSb                 bit 6 - - - - - -1                  LSb

                                                                                                                         SP77
                                          SP75, SP76

     SDI
                                 MSb In                bit 6 - - - -1                      LSb In

                                   SP74

     Note: Refer to Figure 44-4 for load conditions.


 2017-2021 Microchip Technology Inc.                                                                                    DS40001919G-page 764
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-22: SPI MODE REQUIREMENTS (HOST MODE)
Standard Operating Conditions (unless otherwise stated)

 Param
               Symbol                 Characteristic                    Min.        Typ†           Max.        Units       Conditions
  No.

                                                                         61          —              —           ns     Transmit-Only mode
                                                                                         (1)
                                                                         —          16              —          MHz
             TSCK        SCK Cycle Time (2x Prescaled)
                                                                         95          —              —           ns      Full Duplex mode
                                                                                         (1)
                                                                         —          10              —          MHz
SP70*        TSSL2SCH,   SDO to SCK or SCK input                      TSCK         —              —           ns          FST = 0
             TSSL2SCL
                                                                         0           —              —           ns          FST = 1
SP71*        TSCH        SCK output high time                       0.5 TSCK - 12    —         0.5 TSCK + 12    ns
SP72*        TSCL        SCK output low time                        0.5 TSCK - 12    —         0.5 TSCK + 12    ns
SP73*        TDIV2SCH,   Setup time of SDI data input to SCK             85          —              —           ns
             TDIV2SCL    edge
SP74*        TSCH2DIL,   Hold time of SDI data input to SCK edge         0           —              —           ns
             TSCL2DIL    Hold time of SDI data input to final SCK     0.5 TSCK       —              —           ns     CKE = 0, SMP = 1
SP75*        TDOR        SDO data output rise time                       —           10             25          ns         CL = 50 pF
SP76*        TDOF        SDO data output fall time                       —           10             25          ns         CL = 50 pF
SP78*        TSCR        SCK output rise time                            —           10             25          ns         CL = 50 pF
SP79*        TSCF        SCK output fall time                            —           10             25          ns         CL = 50 pF
SP80*        TSCH2DOV,   SDO data output valid after SCK edge           - 15         —              15          ns         CL = 20 pF
             TSCL2DOV
SP81*        TDOV2SCH,   SDO data output valid to first SCK edge     TSCK - 10       —              —           ns     CL = 20 pF
             TDOV2SCL                                                                                                  CKE = 1
SP82*        TSSL2DOV    SDO data output valid after SS edge            —           —              50          ns     CL = 20 pF
SP83*        TSCH2SSH,   SS after last SCK edge                   0.5 TSCK - 10    —              —           ns
             TSCL2SSH
SP84*        TSSH2SSL    SStoSSedge                            0.5 TSCK - 10    —              —           ns

         *    These parameters are characterized but not tested.
         †    Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance
              only and are not tested.
  Note 1: SPIxCON1.SMP bit must be set and the slew rate control must be disabled on the clock and data pins
          (clear the corresponding bits in SLRCONx register) for SPI to operate over 4 MHz.


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 765
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-23: SPI MODE REQUIREMENTS (CLIENT MODE)
Standard Operating Conditions (unless otherwise stated)

 Param
               Symbol                  Characteristic                    Min.        Typ†       Max.   Units        Conditions
  No.

                                                                          47          —          —      ns      Receive-only mode
                                                                                          (1)
                                                                          —          20          —     MHz
             TSCK         SCK Total Cycle Time
                                                                          95          —          —      ns       Full duplex mode
                                                                                          (1)
                                                                          —          10          —     MHz
SP70*        TSSL2SCH,    SS to SCK or SCK input                        0          —          —      ns           CKE = 0
             TSSL2SCL
                                                                          25          —          —      ns           CKE = 1
SP71*        TSCH         SCK input high time                             20          —          —      ns
SP72*        TSCL         SCK input low time                              20          —          —      ns
SP73*        TDIV2SCH,    Setup time of SDI data input to SCK             10          —          —      ns
             TDIV2SCL     edge
SP74*        TSCH2DIL,    Hold time of SDI data input to SCK edge          0          —          —      ns
             TSCL2DIL
SP75*        TDOR         SDO data output rise time                       —           10        25      ns     CL = 50 pF
SP76*        TDOF         SDO data output fall time                       —           10        25      ns     CL = 50 pF
SP77*        TSSH2DOZ     SS to SDO output high-impedance                —           —          85     ns
SP80*        TSCH2DOV,    SDO data output valid after SCK edge            —           —         85      ns
             TSCL2DOV
SP82*        TSSL2DOV     SDO data output valid after SS edge            —           —         85      ns
SP83*        TSCH2SSH,    SS after SCK edge                             20          —          —      ns
             TSCL2SSH
SP84*        TSSH2SSL     SStoSSedge                                 47          —          —      ns
         *    These parameters are characterized but not tested.
         †    Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance
              only and are not tested.
  Note 1: SPIxCON1.SMP bit must be set and the slew rate control must be disabled on the clock and data pins
          (clear the corresponding bits in SLRCONx register) for SPI to operate over 4 MHz.


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 766
                            PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 44-18:                I2C BUS START/STOP BITS TIMING


    SCL
                                              SP91                                                                     SP93
                     SP90                                                                   SP92

    SDA


                                Start                                                                   Stop
                              Condition                                                               Condition

    Note: Refer to Figure 44-4 for load conditions.


TABLE 44-24: I2C BUS START/STOP BITS REQUIREMENTS
Standard Operating Conditions (unless otherwise stated)

  Param
                 Symbol                   Characteristic              Min.   Typ     Max.   Units               Conditions
   No.

SP90*           TSU:STA     Start condition       100 kHz mode        4700   —        —      ns     Only relevant for Repeated Start
                            Setup time            400 kHz mode         600   —        —             condition

                                                  1 MHz mode           260   —        —
SP91*           THD:STA     Start condition       100 kHz mode        4000   —        —      ns     After this period, the first clock
                            Hold time             400 kHz mode         600   —        —             pulse is generated

                                                  1 MHz mode           260   —        —
SP92*           TSU:STO     Stop condition        100 kHz mode        4000   —        —      ns
                            Setup time            400 kHz mode         600   —        —
                                                  1 MHz mode           260   —        —
SP93            THD:STO     Stop condition        100 kHz mode        4700   —        —      ns
                            Hold time             400 kHz mode        1300   —        —
                                                  1 MHz mode           500   —        —
          *     These parameters are characterized but not tested.


FIGURE 44-19:                I2C BUS DATA TIMING

                                              SP103        SP100                                          SP102
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


              Note: Refer to Figure 44-4 for load conditions.


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 767
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-25: I2C BUS DATA REQUIREMENTS
Standard Operating Conditions (unless otherwise stated)

  Param.
              Symbol                     Characteristic                     Min.       Max.     Units             Conditions
   No.

SP100*       THIGH       Clock high time          100 kHz mode             4000         —         ns     Device must operate at a
                                                                                                         minimum of 1.5 MHz
                                                  400 kHz mode              600         —         ns     Device must operate at a
                                                                                                         minimum of 10 MHz
                                                  1 MHz mode                260         —         ns     Device must operate at a
                                                                                                         minimum of 10 MHz
SP101*       TLOW        Clock low time           100 kHz mode             4700         —         ns     Device must operate at a
                                                                                                         minimum of 1.5 MHz
                                                  400 kHz mode             1300         —         ns     Device must operate at a
                                                                                                         minimum of 10 MHz
                                                  1 MHz mode                500         —         —      Device must operate at a
                                                                                                         minimum of 10 MHz
SP102*       TR          SDA and SCL rise         100 kHz mode               —         1000       ns
                         time                     400 kHz mode               20         300       ns     CB is specified to be from
                                                                                                         10-400 pF
                                                  1 MHz mode                 —          120       ns
SP103*       TF          SDA and SCL fall time 100 kHz mode                  —          250       ns
                                                  400 kHz mode          20 X (VDD/      250       ns     CB is specified to be from
                                                                          5.5V)                          10-400 pF
                                                  1 MHz mode            20 X (VDD/      120       ns
                                                                          5.5V)
SP106*       THD:DAT     Data input hold time     100 kHz mode               0          —         ns
                                                  400 kHz mode               0           —        ns
                                                  1 MHz mode                 0           —        ns
                                                                                                         (2)
SP107*       TSU:DAT     Data input setup time    100 kHz mode              250         —         ns
                                                  400 kHz mode              100          —        ns
                                                  1 MHz mode                 50          —        ns
                                                                                                         (1)
SP109*       TAA         Output valid from        100 kHz mode               —         3450       ns
                         clock                    400 kHz mode               —          900       ns
                                                  1 MHz mode                 —          450       ns
SP110*       TBUF        Bus free time            100 kHz mode             4700         —         ns     Time the bus must be free
                                                  400 kHz mode             1300          —        ns     before a new transmission
                                                                                                         can start
                                                  1 MHz mode                500          —        ns
SP111        CB          Bus capacitive loading                              —          400       pF
      *      These parameters are characterized but not tested.
Note 1:      As a transmitter, the device must provide this internal minimum delay time to bridge the undefined region (min. 300 ns)
             of the falling edge of SCL to avoid unintended generation of Start or Stop conditions.
        2:   A Fast mode (400 kHz) I2C bus device can be used in a Standard mode (100 kHz) I2C bus system, but the requirement
             TSU:DAT 250 ns must then be met. This will automatically be the case if the device does not stretch the low period of
             the SCL signal. If such a device does stretch the low period of the SCL signal, it must output the next data bit to the SDA
             line TR max. + TSU:DAT = 1000 + 250 = 1250 ns (according to the Standard mode I2C bus specification), before the SCL
             line is released.


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 768
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 44-26: TEMPERATURE INDICATOR REQUIREMENTS
Standard Operating Conditions (unless otherwise stated)

 Param
               Symbol                    Characteristic                   Min.      Typ†    Max.   Units        Conditions
  No.
 TS01*       TACQMIN      Minimum ADC Acquisition Time Delay               —         25      —       µs
 TS02*       MV           Voltage Sensitivity          High Range          —       -3.684    —     mV/°C        TSRNG = 1
                                                       Low Range           —       -2.456    —     mV/°C        TSRNG = 0
         *    These parameters are characterized but not tested.
         †    Data in “Typ” column is at 3.0V, 25°C unless otherwise stated. These parameters are for design guidance
              only and are not tested.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 769
