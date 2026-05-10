                                                                                                          PIC18F27/47/57Q43
                                                                                            ZCD - Zero-Cross Detection Module


43.   ZCD - Zero-Cross Detection Module
      The ZCD module detects when an A/C signal crosses through the ground potential. The actual
      zero-crossing threshold is the zero-crossing reference voltage, ZCPINV, which is typically 0.75V above
      ground.
      The connection to the signal to be detected is through a series current-limiting resistor. The module
      applies a current source or sink to the ZCD pin to maintain a constant voltage on the pin, thereby
      preventing the pin voltage from forward biasing the ESD protection diodes. When the applied
      voltage is greater than the reference voltage, the module sinks current. When the applied voltage
      is less than the reference voltage, the module sources current. The current source and sink action
      keeps the pin voltage constant over the full range of the applied voltage. The ZCD module is shown
      in the following simplified block diagram.

      Figure 43-1. Simplified ZCD Block Diagram

                                                                                                                         Rev. 10-000194E
                                                                                                                                 3/4/2019


                                                                                                 VPULLUP

                                                                                     RPULLUP
                                                                                    (optional)
                                                         VDD


                      -                                              ZCDxIN                                RSERIES


                                                                                                              External
          Zcpinv      +                                                                                       voltage
                                                                                                               source


                                                                                    RPULLDOWN
                                                                                     (optional)


                                                                           ZCD Output for other modules


                      POL

                                                                                OUT pin


                                                               Interrupt
                                                                     det
                                                                    INTP                                     Set
                                                                                                           ZCDxIF
                                                                   INTN                                     flag
                                                               Interrupt
                                                                     det


--- p790 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                   ZCD - Zero-Cross Detection Module

       The ZCD module is useful when monitoring an A/C waveform for, but not limited to, the following
       purposes:
       •   A/C period measurement
       •   Accurate long term time measurement
       •   Dimmer phase delayed drive
       •   Low EMI cycle switching

43.1   External Resistor Selection
       The ZCD module requires a current-limiting resistor in series with the external voltage source. The
       impedance and rating of this resistor depends on the external source peak voltage. Select a resistor
       value that will drop all of the peak voltage when the current through the resistor is less than the
       maximum input current (ZC02). Refer to the “Electrical Specifications” chapter for more details.
       Make sure that the ZCD I/O pin internal weak pull-up is disabled so it does not interfere with the
       current source and sink.

       Equation 43-1. External Resistor
                   VPEAK
       RSERIES =
                    IZCD

       Figure 43-2. External Voltage Source
                                                                                 Rev. 30-000001A
                                                                                       7/18/2017


                                                                     VMAXPEAK
                                          VPEAK                      VMINPEAK


                                                                                    Z CPINV


43.2   ZCD Logic Output
       The ZCD module includes a Status bit, which can be read to determine whether the current source
       or sink is active. The OUT bit is set when the current sink is active and is cleared when the current
       source is active. The OUT bit is affected by the polarity bit.
       The OUT signal can also be used as input to other modules. This is controlled by the registers of the
       corresponding module.

43.3   ZCD Logic Polarity
       The POL bit inverts the OUT bit relative to the current source and sink output. When the POL bit
       is set, an OUT high indicates that the current source is active and a low output indicates that the
       current sink is active. The POL bit affects the ZCD interrupts.

43.4   ZCD Interrupts
       An interrupt will be generated upon a change in the ZCD logic output when the appropriate
       interrupt enables are set. The ZCD module has a rising edge detector and a falling edge detector.
       The ZCDIF bit of the PIRx register will be set when either edge detector is triggered and its
       associated enable bit is set. The INTP enables rising edge interrupts and the INTN bit enables falling
       edge interrupts.
       To fully enable the interrupt, the following bits must be set:
       •   ZCDIE bit of the PIEx register
       •   INTP bit for rising edge detection


--- p791 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                        ZCD - Zero-Cross Detection Module

       •   INTN bit for falling edge detection
       •   GIEL and GIE bits of the INTCON0 register
       Changing the POL bit will cause an interrupt, regardless of the level of the SEN bit.
       The ZCDIF bit of the PIRx register must be cleared in software as part of the interrupt service. If
       another edge is detected while this flag is being cleared, the flag will still be set at the end of the
       sequence.

43.5   Correction for ZCPINV Offset
       The actual voltage at which the ZCD switches is the reference voltage at the noninverting input of
       the ZCD op amp. For external voltage source waveforms other than square waves, this voltage offset
       from zero causes the zero-cross event to occur either too early or too late.

43.5.1 Correction by AC Coupling
       When the external voltage source is sinusoidal, the effects of the ZCPINV offset can be eliminated by
       isolating the external voltage source from the ZCD pin with a capacitor, in addition to the voltage
       reducing resistor. The capacitor will cause a phase shift resulting in the ZCD output switch in
       advance of the actual zero-crossing event. The phase shift will be the same for both rising and
       falling zero-crossings, which can be compensated for by either delaying the CPU response to the
       ZCD switch by a timer or other means or selecting a capacitor value large enough that the phase
       shift is negligible.
       To determine the series resistor and capacitor values for this configuration, start by computing the
       impedance, Z, to obtain a peak current less than the maximum input current (ZC02). Refer to the
       "Electrical Specifications" chapter for more details. Next, arbitrarily select a suitably large nonpolar
       capacitor and compute its reactance, Xc, at the external voltage source frequency. Finally, compute
       the series resistor, capacitor peak voltage, and phase shift using the formulas shown below.
       When this technique is used and the input signal is not present, the ZCD will tend to oscillate. To
       avoid this oscillation, connect the ZCD pin to VDD or GND with a high-impedance resistor.

               Note: In this example, the impedance value is calculated for a peak current of 300
               μA.

               Equation 43-2. R-C Equations
               VPEAK = external voltage source peak voltage
               f = external voltage source frequency
               C = series capacitor
               R = series resistor
               VC = peak capacitor voltage
               Φ = capacitor induced zero-crossing phase advance in radians
               TΦ = time ZC event occurs before actual zero-crossing
                      VPEAK
               Z=
                    3 × 10−4
                        1
               XC =
                      2πfC

               R=     Z2 − XC2

               VC = XC 3 × 10−4


--- p792 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             ZCD - Zero-Cross Detection Module

                            XC
               Φ = tan −1
                            R

               TΦ = Φ
                   2πf


               Equation 43-3. R-C Calculation Example
               Vrms = 120

               VPEAK = Vrms × 2 = 169.7
               f = 60 Hz
               C = 0.1 μF
                      VPEAK           169.7
               Z=              =             = 565.7 kΩ
                    3 × 10−4        3 × 10−4
                        1 =       1
               XC =                        = 26.53 kΩ
                      2πfC  2π × 60 × 10−7

               R=     Z2 − XC2 = 565.1 kΩ computed
               Ra = 560 kΩ used

               ZR =    Ra2 + XC2 = 560.6 kΩ
                         VPEAK
               IPEAK =         = 302.7 × 10−6A
                          ZR
               VC = XC × IPEAK = 8.0 V
                            XC
               Φ = tan −1      = 0.047 radians
                            R

               TΦ = Φ = 125.6 μs
                   2πf


43.5.2 Correction by Offset Current
        When the waveform is varying relative to VSS, the zero-cross is detected too early as the waveform
        falls and too late as the waveform rises. When the waveform is varying relative to VDD, the zero-cross
        is detected too late as the waveform rises and too early as the waveform falls. The actual offset time
        can be determined for sinusoidal waveforms with the corresponding equations shown below.


               Equation 43-4. ZCD Event Offset
               When External Voltage source is relative to VSS:
                                    ZCPINV
                           sin−1    VPEAK
               Toffset =
                                   2πf
               When External Voltage source is relative to VDD:


--- p793 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                          ZCD - Zero-Cross Detection Module
                                   VDD − ZCPINV
                           sin−1      VPEAK
               Toffset =
                                    2πf


       This offset time can be compensated for by adding a pull-up or pull-down biasing resistor to the ZCD
       pin. A pull-up resistor is used when the external voltage source is varying relative to VSS. A pull-down
       resistor is used when the voltage is varying relative to VDD. The resistor adds a bias to the ZCD pin so
       that the target external voltage source must go to zero to pull the pin voltage to the ZCPINV switching
       voltage. The pull-up or pull-down value can be determined with the equations shown below.


               Equation 43-5. ZCD Pull-up/Pull-down Resistor
               When External Voltage source is relative to VSS:
                           RSERIES Vpullup − ZCPINV
               Rpullup =
                                    ZCPINV
               When External Voltage source is relative to VDD:
                             RSERIES ZCPINV
               Rpulldown =
                              VDD − ZCPINV


43.6   Handling VPEAK Variations
       If the peak amplitude of the external voltage is expected to vary, the series resistor must be selected
       to keep the ZCD current source and to sink below the design maximum range specified by ZC02 and
       above a reasonable minimum range, depending on the application. The compensating pull-up for
       this series resistance can be determined with the equations shown in Equation 43-5 because the
       pull-up value is independent from the peak voltage.


                   Tip: It is recommended that the maximum peak voltage be no more than six
                   times the minimum peak voltage.


43.7   Operation During Sleep
       The ZCD current sources and interrupts are unaffected by Sleep.

43.8   Effects of a Reset
       The ZCD circuit can be configured to default to the Active or Inactive state on Power-on Reset (POR).
       When the ZCD Configuration bit is cleared, the ZCD circuit will be active at POR. When the ZCD
       Configuration bit is set, the SEN bit must be set to enable the ZCD module.

43.9   Disabling the ZCD Module
       The ZCD module can be disabled in two ways:
       1. The ZCD Configuration bit disables the ZCD module when set. When this is the case, then the
          ZCD module will be enabled by setting the SEN bit. When the ZCD bit is clear, the ZCD is always
          enabled and the SEN bit has no effect.
       2. The ZCD can also be disabled using the ZCDMD bit of the PMDx register. This is subject to the
          status of the ZCD bit.

43.10 Register Definitions: ZCD Control
       Long bit name prefixes for the ZCD peripherals are shown in the table below. Refer to the “Long Bit
       Names” section of the “Register and Bit Naming Conventions” chapter for more information.


--- p794 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                        ZCD - Zero-Cross Detection Module

Table 43-1. ZCD Long Bit Name Prefixes
                  Peripheral                                              Bit Name Prefix
                     ZCD                                                          ZCD


--- p795 ---
                                                                                                                     PIC18F27/47/57Q43
                                                                                                       ZCD - Zero-Cross Detection Module

43.10.1 ZCDCON

            Name:       ZCDCON
            Address:    0x04C

            Zero-Cross Detect Control Register

      Bit        7               6            5               4                3               2                1              0
                SEN                          OUT             POL                                              INTP           INTN
  Access        R/W                           R              R/W                                              R/W             R/W
   Reset         0                            x               0                                                 0              0

Bit 7 – SEN Zero-Cross Detect Software Enable
          This bit is ignored when the ZCD fuse is cleared.
            Value      Condition           Description
            X          ZCD Config fuse = 0 Zero-cross detect is always enabled. This bit is ignored.
            1          ZCD Config fuse = 1   Zero-cross detect is enabled. ZCD pin is forced to output to source and sink current.
            0          ZCD Config fuse = 1   Zero-cross detect is disabled. ZCD pin operates according to PPS and TRIS controls.


Bit 5 – OUT Zero-Cross Detect Data Output
            Value      Condition                     Description
            1          POL = 0                       ZCD pin is sinking current
            0          POL = 0                        ZCD pin is sourcing current
            1          POL = 1                        ZCD pin is sourcing current
            0          POL = 1                        ZCD pin is sinking current


Bit 4 – POL Zero-Cross Detect Polarity
            Value      Description
            1          ZCD logic output is inverted
            0          ZCD logic output is not inverted

Bit 1 – INTP Zero-Cross Detect Positive-Going Edge Interrupt Enable
            Value      Description
            1          The ZCDIF bit is set on low-to-high ZCD_output transition
            0          The ZCDIF bit is unaffected by low-to-high ZCD_output transition

Bit 0 – INTN Zero-Cross Detect Negative-Going Edge Interrupt Enable
            Value      Description
            1          The ZCDIF bit is set on high-to-low ZCD_output transition
            0          The ZCDIF bit is unaffected by high-to-low ZCD_output transition


--- p796 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                    ZCD - Zero-Cross Detection Module

43.11 Register Summary - ZCD
Address   Name     Bit Pos.    7         6           5              4        3        2           1           0
 0x4C     ZCDCON     7:0      SEN                   OUT            POL                          INTP        INTN


--- p797 ---
