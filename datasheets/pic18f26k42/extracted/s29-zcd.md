                      PIC18(L)F26/27/45/46/47/55/56/57K42
29.0     ZERO-CROSS DETECTION                               29.1       External Resistor Selection
         (ZCD) MODULE                                       The ZCD module requires a current-limiting resistor in
The ZCD module detects when an A/C signal crosses           series with the external voltage source. The impedance
through the ground potential. The actual zero-crossing      and rating of this resistor depends on the external
threshold is the zero-crossing reference voltage,           source peak voltage. Select a resistor value that will
VCPINV, which is typically 0.75V above ground.              drop all of the peak voltage when the current through
                                                            the resistor is nominally 300 A. Refer to Equation 29-
The connection to the signal to be detected is through      1 and Figure 29-1. Make sure that the ZCD I/O pin
a series current-limiting resistor. The module applies a    internal weak pull-up is disabled so it does not interfere
current source or sink to the ZCD pin to maintain a         with the current source and sink.
constant voltage on the pin, thereby preventing the pin
voltage from forward biasing the ESD protection
                                                            EQUATION 29-1:          EXTERNAL RESISTOR
diodes. When the applied voltage is greater than the
reference voltage, the module sinks current. When the
applied voltage is less than the reference voltage, the                                  V PEAK
module sources current. The current source and sink                          R SERIES = -------------–---
                                                                                                        4
action keeps the pin voltage constant over the full                                     310
range of the applied voltage. The ZCD module is
shown in the simplified block diagram Figure 29-2.
The ZCD module is useful when monitoring an A/C
waveform for, but not limited to, the following purposes:   FIGURE 29-1:            EXTERNAL VOLTAGE
• A/C period measurement                                                                     VMAXPEAK
• Accurate long term time measurement                          VPEAK                         VMINPEAK
• Dimmer phase delayed drive
• Low EMI cycle switching

                                                                                                            VCPINV


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 459
                         PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 29-2:             SIMPLIFIED ZCD BLOCK DIAGRAM


                                                                                           VPULLUP              Rev. 10-000194E
                                                                                                                       9/13/2016


                                                                                optional


                                                           VDD                RPULLUP


                     -                                                 ZCDxIN                        RSERIES


                                                                                                        External
        Zcpinv       +                                                       RPULLDOWN                  voltage
                                                                                                        source

                                                                                optional


                                                                             ZCD Output for other modules


                     POL

                                                                                     OUT pin


                                                                 Interrupt
                                                                       det
                                                                      INTP                                      Set
                                                                                                               ZCDxIF
                                                                     INTN                                       flag
                                                                 Interrupt
                                                                       det


29.2     ZCD Logic Output                                          29.3      ZCD Logic Polarity
The ZCD module includes a Status bit, which can be                 The POL bit of the ZCDCON register inverts the OUT
read to determine whether the current source or sink is            bit relative to the current source and sink output. When
active. The OUT bit of the ZCDCON register is set                  the POL bit is set, a OUT high indicates that the current
when the current sink is active, and cleared when the              source is active, and a low output indicates that the
current source is active. The OUT bit is affected by the           current sink is active.
polarity bit, even if the module is disabled.                      The POL bit affects the ZCD interrupts.
The OUT signal can also be used as input to other
modules. This is controlled by the registers of the
corresponding module. OUT can be used as follows:
• Gate source for TMR1/3/5
• Clock source for TMR2/4/6
• Reset source for TMR2/4/6


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 460
                        PIC18(L)F26/27/45/46/47/55/56/57K42
29.4      ZCD Interrupts                                         29.5        Correcting for VCPINV offset
An interrupt will be generated upon a change in the              The actual voltage at which the ZCD switches is the
ZCD logic output when the appropriate interrupt                  reference voltage at the noninverting input of the ZCD
enables are set. A rising edge detector and a falling            op amp. For external voltage source waveforms other
edge detector are present in the ZCD for this purpose.           than square waves, this voltage offset from zero
The ZCDIF bit of the respective PIR register will be set         causes the zero-cross event to occur either too early or
when either edge detector is triggered and its                   too late. When the waveform is varying relative to VSS,
associated enable bit is set. The INTP enables rising            then the zero cross is detected too early as the
edge interrupts and the INTN bit enables falling edge            waveform falls and too late as the waveform rises.
interrupts. Both are located in the ZCDCON register.             When the waveform is varying relative to VDD, then the
Priority of the interrupt can be changed if the IPEN bit         zero cross is detected too late as the waveform rises
of the INTCON register is set. The ZCD interrupt can be          and too early as the waveform falls. The actual offset
made high or low priority by setting or clearing the             time can be determined for sinusoidal waveforms with
ZCDIP bit of the respective IPR register.                        the corresponding equations shown in Equation 29-2.

To fully enable the interrupt, the following bits must be set:
                                                                 EQUATION 29-2:                      ZCD EVENT OFFSET
• ZCDIE bit of the respective PIE register
• INTP bit of the ZCDCON register                                When External Voltage Source is relative to VSS:
  (for a rising edge detection)
                                                                                            asin ------------------
• INTN bit of the ZCDCON register
                                                                                                         V C PIN V
  (for a falling edge detection)                                                                           V PEAK
                                                                                 TO FFSET = -----------------------------------
• GIE bits of the INTCON0 register                                                               2  Freq
Changing the POL bit can cause an interrupt,
regardless of the level of the SEN bit.                          When External Voltage Source is relative to VDD:
The ZCDIF bit of the respective PIR register must be
cleared in software as part of the interrupt service. If
                                                                                            asin ---------------------------------
                                                                                                         V D D –V C PIN V
another edge is detected while this flag is being
cleared, the flag will still be set at the end of the                                                             V PEAK
                                                                                 TO FFSET = -------------------------------------------------
sequence.                                                                                               2  Freq

                                                                 This offset time can be compensated for by adding a
                                                                 pull-up or pull-down biasing resistor to the ZCD pin. A
                                                                 pull-up resistor is used when the external voltage
                                                                 source is varying relative to VSS. A pull-down resistor is
                                                                 used when the voltage is varying relative to VDD. The
                                                                 resistor adds a bias to the ZCD pin so that the target
                                                                 external voltage source must go to zero to pull the pin
                                                                 voltage to the VCPINV switching voltage. The pull-up or
                                                                 pull-down value can be determined with the equations
                                                                 shown in Equation 29-3 or Equation 29-4.

                                                                 EQUATION 29-3:                      ZCD PULL-UP/DOWN
                                                                  When External Signal is relative to Vss:

                                                                                     R SERIE S V PU LLU P – V C PIN V 
                                                                        R PU LLU P = -------------------------------------------------------------------------
                                                                                                                      V C PIN V
                                                                  When External Signal is relative to VDD:

                                                                                         R SERIES V C PIN V 
                                                                        R PU LLD O W N = ---------------------------------------------
                                                                                            V D D – V C PIN V 


 2017-2021 Microchip Technology Inc.                                                                                DS40001919G-page 461
                                   PIC18(L)F26/27/45/46/47/55/56/57K42
Measuring VCPINV can be difficult, especially when the                                   29.8     Effects of a Reset
waveform is relative to VDD. However, by combining
Equations 29-2 and 29-3, the resistor value can be                                       The ZCD circuit can be configured to default to the active
determined from the time difference between the                                          or inactive state on Power-on-Reset (POR). When the
ZCD_output high and low intervals. Note that the time                                    ZCD Configuration bit is cleared, the ZCD circuit will be
difference, ΔT, is 4*TOFFSET. The equation for                                           active at POR. When the ZCD Configuration bit is set,
determining the pull-up and pull-down resistor values                                    the SEN bit of the ZCDCON register must be set to
from the high and low ZCD_output periods is shown in                                     enable the ZCD module.
Equation 29-4.
                                                                                         29.9     Disabling the ZCD Module
EQUATION 29-4:                      PULL-UP/DOWN                                         The ZCD module can be disabled in two ways:
                                    RESISTOR VALUES
                                                                                         1.   Configuration Word 2H has the ZCD bit which
                                                                                              disables the ZCD module when set, but it can be
                                                                                            enabled using the SEN bit of the ZCDCON
                                          V BIA S                                           register (Register 29-1). If the ZCD bit is clear,
    R = R SERIES --------------------------------------------------------------- – 1
                 V PE AK  sin Freq---                         T 
                                                                    --------                 the ZCD is always enabled.
                                                                   2               2.   The ZCD can also be disabled using the
                                                                                              ZCDMD bit of the respective PMD2 register
                                                                                              (Register 19-3). This is subject to the status of
  R is pull-up or pull-down resistor.                                                         the ZCD bit.
  VBIAS is VPULLUP when R is pull-up or VDD when R
  is pull-down.
  ΔT is the ZCDOUT high and low period difference.


29.6         Handling VPEAK Variations
If the peak amplitude of the external voltage is
expected to vary, the series resistor must be selected
to keep the ZCD current source and sink below the
design maximum range of ± 600 A and above a
reasonable minimum range. A general rule of thumb is
that the maximum peak voltage can be no more than
six times the minimum peak voltage. To ensure that the
maximum current does not exceed ± 600 A and the
minimum is at least ± 100 A, compute the series
resistance as shown in Equation 29-5. The
compensating pull-up for this series resistance can be
determined with Equation 29-3 because the pull-up
value is not dependent to the peak voltage.

EQUATION 29-5:                      SERIES R FOR V RANGE

                  V M AXPEAK + V M IN PEAK
       R SERIES = ---------------------------------–---
                                                      ---------------------
                                                      4
                                      710


29.7         Operation During Sleep
The ZCD current sources and interrupts are unaffected
by Sleep.


 2017-2021 Microchip Technology Inc.                                                                                     DS40001919G-page 462
                         PIC18(L)F26/27/45/46/47/55/56/57K42
29.10 Register Definitions: ZCD Control

REGISTER 29-1:            ZCDCON: ZERO-CROSS DETECT CONTROL REGISTER
   R/W-0/0               U-0                R-x           R/W-0/0       U-0                U-0           R/W-0/0      R/W-0/0
        SEN              —                 OUT             POL           —                 —              INTP            INTN
bit 7                                                                                                                         bit 0


Legend:
R = Readable bit                       W = Writable bit             U = Unimplemented bit, read as ‘0’
-n = Value at POR                      ‘1’ = Bit is set             ‘0’ = Bit is cleared             x = Bit is unknown


bit 7              SEN: Zero-Cross Detect Software Enable bit
                   This bit is ignored when ZCDSEN configuration bit is set.
                   1= Zero-cross detect is enabled.
                   0= Zero-cross detect is disabled. ZCD pin operates according to PPS and TRIS controls.
bit 6              Unimplemented: Read as ‘0’
bit 5              OUT: Zero-Cross Detect Data Output bit
                   ZCDPOL bit = 0:
                   1 = ZCD pin is sinking current
                   0 = ZCD pin is sourcing current
                   ZCDPOL bit = 1:
                   1 = ZCD pin is sourcing current
                   0 = ZCD pin is sinking current
bit 4              POL: Zero-Cross Detect Polarity bit
                   1 = ZCD logic output is inverted
                   0 = ZCD logic output is not inverted
bit 3-2            Unimplemented: Read as ‘0’
bit 1              INTP: Zero-Cross Detect Positive-Going Edge Interrupt Enable bit
                   1 = ZCDIF bit is set on low-to-high ZCD_output transition
                   0 = ZCDIF bit is unaffected by low-to-high ZCD_output transition
bit 0              INTN: Zero-Cross Detect Negative-Going Edge Interrupt Enable bit
                   1 = ZCDIF bit is set on high-to-low ZCD_output transition
                   0 = ZCDIF bit is unaffected by high-to-low ZCD_output transition


TABLE 29-1:         SUMMARY OF REGISTERS ASSOCIATED WITH THE ZCD MODULE
                                                                                                                          Register
  Name           Bit 7         Bit 6           Bit 5        Bit 4     Bit 3        Bit 2         Bit 1        Bit 0
                                                                                                                          on page
ZCDCON           SEN            —              OUT          POL        —            —            INTP         INTN          464
Legend:       — = unimplemented, read as ‘0’. Shaded cells are unused by the ZCD module.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 463
