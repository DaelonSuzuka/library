                        PIC18(L)F26/27/45/46/47/55/56/57K42
38.0      COMPARATOR MODULE                                    38.1      Comparator Overview
  Note:     The       PIC18(L)F26/27/45/46/47/55/56/           A single comparator is shown in Figure 38-1 along with
            57K42 devices have two comparators.                the relationship between the analog input levels and
            Therefore, all information in this section         the digital output. When the analog voltage at VIN+ is
            refers to both C1 and C2.                          less than the analog voltage at VIN-, the output of the
                                                               comparator is a digital low level. When the analog
Comparators are used to interface analog circuits to a         voltage at VIN+ is greater than the analog voltage at
digital circuit by comparing two analog voltages and           VIN-, the output of the comparator is a digital high level.
providing a digital indication of their relative magnitudes.
Comparators are very useful mixed signal building              FIGURE 38-1:             SINGLE COMPARATOR
blocks because they provide analog functionality
independent of program execution.
                                                                      VIN+             +
The analog comparator module includes the following
                                                                                                           Output
features:                                                              VIN-             –
• Programmable input selection
• Programmable output polarity
• Rising/falling output edge interrupts
                                                                       VIN-
                                                                       VIN+


                                                                 Output


                                                                 Note:        The black areas of the output of the
                                                                              comparator represents the uncertainty
                                                                              due to input offsets and response time.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 644
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 38-2:                COMPARATOR MODULE SIMPLIFIED BLOCK DIAGRAM


                                                                                                                                 Rev. 10-000027N
                                                                                                                                       10/12/2016

                     3                (1)
       NCH<2:0>                    EN
                                                                                  Interrupt            INTP
                                                                                        Rising
                                                                                         Edge                                              set bit
          CxIN0-         000                                                                                                                CxIF
                                                                                  Interrupt            INTN
          CxIN1-         001
                                                                                        Falling
         CxIN2-          010                     EN(1)                                   Edge

         CxIN3-          011       CxVP
                                            -                                                              D    Q                   CxOUT
        Reserved         100
                                                 Cx
        Reserved         101       CxVN
      FVR_buffer2        110
                                            +                                                         Q1

                         111
                                                SP    HYS    POL


                                                                                                                CxOUT_sync      To Other
                                                                                                                                Peripherals
                                                                                       SYNC
        CxIN0+           000
                                                                                                                             TRIS bit
        CxIN1+           001                                                                      0

        Reserved         010                                                                                   PPS                       CxOUT
                                                                                 D     Q          1
        Reserved         011
        Reserved         100                                                                                  RxyPPS
                                                (From Timer1 Module) T1CLK
      DAC_output         101
      FVR_buffer2        110
                         111


       PCH<2:0>                    EN(1)
                     3


           Note 1:       When CxON = 0, all multiplexer inputs are disconnected and the Comparator will produce a ‘0’ at the output.


 2017-2021 Microchip Technology Inc.                                                                                   DS40001919G-page 645
                      PIC18(L)F26/27/45/46/47/55/56/57K42
38.2     Comparator Control                                 38.2.3     COMPARATOR OUTPUT POLARITY
Each comparator has two control registers: CMxCON0          Inverting the output of the comparator is functionally
and CMxCON1.                                                equivalent to swapping the comparator inputs. The
                                                            polarity of the comparator output can be inverted by
The CMxCON0 register (see Register 38-1) contains           setting the POL bit of the CMxCON0 register. Clearing
Control and Status bits for the following:                  the POL bit results in a noninverted output.
• Enable                                                    Table 38-1 shows the output state versus input
• Output                                                    conditions, including polarity control.
• Output polarity
• Hysteresis enable
                                                            TABLE 38-1:       COMPARATOR OUTPUT
• Timer1 output synchronization                                               STATE VS. INPUT
The CMxCON1 register (see Register 38-2) contains                             CONDITIONS
Control bits for the following:
                                                              Input Condition        POL           CxOUT
• Interrupt on positive/negative edge enables
                                                               CxVN > CxVP            0               0
The CMxPCH and CMxNCH registers are used to
                                                               CxVN < CxVP            0               1
select the positive and negative input channels,
respectively.                                                  CxVN > CxVP            1               1
                                                               CxVN < CxVP            1               0
38.2.1      COMPARATOR ENABLE
Setting the EN bit of the CMxCON0 register enables
the comparator for operation. Clearing the EN bit
disables the comparator resulting in minimum current
consumption.

38.2.2      COMPARATOR OUTPUT
The output of the comparator can be monitored by
reading either the CxOUT bit of the CMxCON0 register
or the CxOUT bit of the CMOUT register.
The comparator output can also be routed to an
external pin through the RxyPPS register (Register 17-2).
The corresponding TRIS bit must be clear to enable the
pin as an output.
   Note 1: The internal output of the comparator is
           latched with each instruction cycle.
           Unless otherwise specified, external
           outputs are not latched.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 646
                       PIC18(L)F26/27/45/46/47/55/56/57K42
38.3      Comparator Hysteresis                              38.5      Comparator Positive Input
A selectable amount of separation voltage can be
                                                                       Selection
added to the input pins of each comparator to provide a      Configuring the PCH[2:0] bits of the CMxPCH register
hysteresis function to the overall operation. Hysteresis     directs an internal voltage reference or an analog pin to
is enabled by setting the HYS bit of the CMxCON0             the noninverting input of the comparator:
register.
                                                             • CxIN0+, CxIN1+ analog pin
See Comparator Specifications in Table 44-16 for more        • DAC output
information.
                                                             • FVR (Fixed Voltage Reference)
38.3.1      COMPARATOR OUTPUT                                • VSS (Ground)
            SYNCHRONIZATION                                  See Section 34.0 “Fixed Voltage Reference (FVR)”
The output from a comparator can be synchronized             for more information on the Fixed Voltage Reference
with Timer1 by setting the SYNC bit of the CMxCON0           module.
register.                                                    See Section 37.0 “5-Bit Digital-to-Analog Converter
Once enabled, the comparator output is latched on the        (DAC) Module” for more information on the DAC input
falling edge of the Timer1 source clock. If a prescaler is   signal.
used, the CxOUT bit is synchronized with the timer, so       Any time the comparator is disabled (EN = 0), all
that the software sees no ambiguity due to timing. See       comparator inputs are disabled.
the Comparator Block Diagram (Figure 38-2) and the
Timer1 Block Diagram (Figure 21-1) for more                  38.6      Comparator Negative Input
information.
                                                                       Selection
38.4      Comparator Interrupt                               The NCH[2:0] bits of the CMxNCH register direct an
                                                             analog input pin and internal reference voltage or
An interrupt can be generated for every rising or falling    analog ground to the inverting input of the comparator:
edge of the comparator output.
                                                             • CxIN0-, CxIN1-, CxIN2-, CxIN3- analog pin
When either edge detector is triggered and its
                                                             • FVR (Fixed Voltage Reference)
associated enable bit is set (INTP and/or INTN bits of
the CMxCON1 register), the Corresponding Interrupt           • Analog Ground
Flag bit (CxIF bit of the respective PIR register) will be
set.
                                                               Note:     To use CxINy+ and CxINy- pins as analog
To enable the interrupt, you must set the following bits:                input, the appropriate bits must be set in
• EN bit of the CMxCON0 register                                         the    ANSEL       register    and    the
                                                                         corresponding TRIS bits must also be set
• CxIE bit of the respective PIE register
                                                                         to disable the output drivers.
• INTP bit of the CMxCON1 register (for a rising
  edge detection)
• INTN bit of the CMxCON1 register (for a falling
  edge detection)
• GIE bit of the INTCON0 register
The associated interrupt flag bit, CxIF bit of the
respective PIR register, must be cleared in software. If
another edge is detected while this flag is being
cleared, the flag will still be set at the end of the
sequence.
  Note:     Although a comparator is disabled, an
            interrupt can be generated by changing
            the output polarity with the POL bit of the
            CMxCON0 register, or by switching the
            comparator on or off with the EN bit of the
            CMxCON0 register.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 647
                      PIC18(L)F26/27/45/46/47/55/56/57K42
38.7     Comparator Response Time                               38.8     Analog Input Connection
The comparator output is indeterminate for a period of
                                                                         Considerations
time after the change of an input source or the selection       A simplified circuit for an analog input is shown in
of a new reference voltage. This period is referred to as       Figure 38-3. Since the analog input pins share their
the response time. The response time of the comparator          connection with a digital input, they have reverse
differs from the settling time of the voltage reference.        biased ESD protection diodes to VDD and VSS. The
Therefore, both of these times must be considered when          analog input, therefore, must be between VSS and VDD.
determining the total response time to a comparator             If the input voltage deviates from this range by more
input change. See the Comparator and Voltage                    than 0.6V in either direction, one of the diodes is
Reference Specifications in Table 44-16 and Table 44-           forward biased and a latch-up may occur.
18 for more details.
                                                                The maximum source impedance for analog sources is
                                                                mentioned in Parameter AD08 in Table 44-14. Also, any
                                                                external component connected to an analog input pin,
                                                                such as a capacitor or a Zener diode, may have very little
                                                                leakage current to minimize inaccuracies introduced.
                                                                   Note 1: When reading a PORT register, all pins
                                                                           configured as analog inputs will read as a
                                                                           ‘0’. Pins configured as digital inputs will
                                                                           convert as an analog input, according to
                                                                           the input specification.
                                                                         2: Analog levels on any pin defined as a
                                                                            digital input, may cause the input buffer to
                                                                            consume more current than is specified.

FIGURE 38-3:           ANALOG INPUT MODEL
                                                                                                           Rev. 10-000071C
                                                                                                                  9/27/2017

                                              VDD
                                Analog
                                                    VT ≈ 0.6V
                     RS        Input pin                                  RIC
                                                                                              To Comparator
                                                                                (1)
                                                                    ILEA KAGE
               VA                 CPIN              VT ≈ 0.6V
                                  5pF

                                                                   VSS


            Legend: CPIN     = Input Capacitance
                    ILEAKAGE = Leakage Current at the pin due to various junctions
                    RIC      = Interconnect Resistance
                    RS       = Source Impedance
                    VA       = Analog Voltage
                    VT       = Threshold Voltage


           Note 1: See Section 44.0 “Electrical Specifications”.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 648
                      PIC18(L)F26/27/45/46/47/55/56/57K42
38.9     CWG1 Auto-Shutdown Source
The output of the comparator module can be used as
an auto-shutdown source for the CWG1 module. When
the output of the comparator is active and the
corresponding WGASxE is enabled, the CWG
operation will be suspended immediately (see Section
26.10.1.2 “External Input Source”).

38.10 ADC Auto-Trigger Source
The output of the comparator module can be used to
trigger an ADC conversion. When the ADACT register
is set to trigger on a comparator output, an ADC
conversion will trigger when the Comparator output
goes high.

38.11 TMR2/4/6 Reset
The output of the comparator module can be used to
reset Timer2. When the TxRST register is appropriately
set, the timer will reset when the Comparator output
goes high.

38.12 Operation in Sleep Mode
The comparator module can operate during Sleep. The
comparator clock source is based on the Timer1 clock
source. If the Timer1 clock source is either the system
clock (FOSC) or the instruction clock (FOSC/4), Timer1
will not operate during Sleep, and synchronized
comparator outputs will not operate.
A comparator interrupt will wake the device from
Sleep. The CxIE bits of the respective PIE register
must be set to enable comparator interrupts.


 2017-2021 Microchip Technology Inc.                     DS40001919G-page 649
                       PIC18(L)F26/27/45/46/47/55/56/57K42
38.13 Register Definitions: Comparator Control
Long bit name prefixes for the Comparators are shown
in Table 38-2. Refer to Section 1.3.2.2 “Long Bit
Names” for more information.
TABLE 38-2:
         Peripheral               Bit Name Prefix
             C1                               C1
             C2                               C2

REGISTER 38-1:          CMxCON0: COMPARATOR x CONTROL REGISTER 0
   R/W-0/0            R-0/0             U-0         R/W-0/0       U-0                U-1     R/W-0/0        R/W-0/0
        EN            OUT               —              POL         —                 —         HYS           SYNC
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
-n = Value at POR                ‘1’ = Bit is set             ‘0’ = Bit is cleared         x = Bit is unknown


bit 7             EN: Comparator Enable bit
                  1 = Comparator is enabled
                  0 = Comparator is disabled and consumes no active power
bit 6             OUT: Comparator Output bit
                  If POL = 0 (noninverted polarity):
                  1 = CxVP > CxVN
                  0 = CxVP < CxVN
                  If POL = 1 (inverted polarity):
                  1 = CxVP < CxVN
                  0 = CxVP > CxVN
bit 5             Unimplemented: Read as ‘0’
bit 4             POL: Comparator Output Polarity Select bit
                  1 = Comparator output is inverted
                  0 = Comparator output is not inverted
bit 3             Unimplemented: Read as ‘0’
bit 2             Unimplemented: Read as ‘1’
bit 1             HYS: Comparator Hysteresis Enable bit
                  1 = Comparator hysteresis enabled
                  0 = Comparator hysteresis disabled
bit 0             SYNC: Comparator Output Synchronous Mode bit
                  1 = Comparator output to Timer1 and I/O pin is synchronous to changes on Timer1 clock source.
                      Output updated on the falling edge of Timer1 clock source.
                  0 = Comparator output to Timer1 and I/O pin is asynchronous


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 650
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 38-2:         CMxCON1: COMPARATOR x CONTROL REGISTER 1
        U-0           U-0               U-0        U-0          U-0               U-0      R/W-0/0       R/W-0/0
        —             —                 —          —            —                 —          INTP             INTN
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit           U = Unimplemented bit, read as ‘0’
-n = Value at POR               ‘1’ = Bit is set           ‘0’ = Bit is cleared          x = Bit is unknown


bit 7-2          Unimplemented: Read as ‘0’
bit 1            INTP: Comparator Interrupt on Positive-Going Edge Enable bit
                 1 = The CxIF interrupt flag will be set upon a positive-going edge of the CxOUT bit
                 0 = No interrupt flag will be set on a positive-going edge of the CxOUT bit
bit 0            INTN: Comparator Interrupt on Negative-Going Edge Enable bit
                 1 = The CxIF interrupt flag will be set upon a negative-going edge of the CxOUT bit
                 0 = No interrupt flag will be set on a negative-going edge of the CxOUT bit

REGISTER 38-3:         CMxNCH: COMPARATOR x INVERTING CHANNEL SELECT REGISTER
        U-0           U-0               U-0        U-0          U-0           R/W-0/0      R/W-0/0       R/W-0/0
        —             —                 —          —            —                         NCH[2:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit           U = Unimplemented bit, read as ‘0’
-n = Value at POR               ‘1’ = Bit is set           ‘0’ = Bit is cleared          x = Bit is unknown


bit 7-3          Unimplemented: Read as ‘0’
bit 2-0          NCH[2:0]: Comparator Inverting Input Channel Select bits
                 111 = VSS
                 110 = FVR_Buffer2
                 101 = NCH not connected
                 100 = NCH not connected
                 011 = CxIN3-
                 010 = CxIN2-
                 001 = CxIN1-
                 000 = CxIN0-


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 651
                           PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 38-4:              CMxPCH: COMPARATOR x NONINVERTING CHANNEL SELECT REGISTER
        U-0                U-0                U-0              U-0             U-0              R/W-0/0            R/W-0/0          R/W-0/0
        —                  —                   —                 —             —                                  PCH[2:0]
bit 7                                                                                                                                    bit 0


Legend:
R = Readable bit                         W = Writable bit               U = Unimplemented bit, read as ‘0’
-n = Value at POR                        ‘1’ = Bit is set               ‘0’ = Bit is cleared                  x = Bit is unknown


bit 7-3             Unimplemented: Read as ‘0’
bit 2-0             PCH[2:0]: Comparator Noninverting Input Channel Select bits
                    111 = VSS
                    110 = FVR_Buffer2
                    101 = DAC_Output
                    100 = PCH not connected
                    011 = PCH not connected
                    010 = PCH not connected
                    001 = CxIN1+
                    000 = CxIN0+

REGISTER 38-5:              CMOUT: COMPARATOR OUTPUT REGISTER
        U-0                U-0                U-0              U-0             U-0                U-0               R-0/0            R-0/0
        —                  —                   —                 —             —                  —                C2OUT            C1OUT
bit 7                                                                                                                                    bit 0


Legend:
R = Readable bit                         W = Writable bit               U = Unimplemented bit, read as ‘0’
-n = Value at POR                        ‘1’ = Bit is set               ‘0’ = Bit is cleared                  x = Bit is unknown


bit 7-2             Unimplemented: Read as ‘0’
bit 1               C2OUT: Mirror copy of C2OUT bit
bit 0               C1OUT: Mirror copy of C1OUT bit


TABLE 38-3:          SUMMARY OF REGISTERS ASSOCIATED WITH COMPARATOR MODULE
                                                                                                                                       Reset
    Name           Bit 7         Bit 6          Bit 5       Bit 4      Bit 3            Bit 2             Bit 1             Bit 0      Values
                                                                                                                                      on page

CMxCON0             EN           OUT             —          POL          —               —                HYS               SYNC        651
CMxCON1             —             —              —           —           —               —                INTP              INTN        652
CMxNCH              —             —              —           —           —                              NCH[2:0]                        652
CMxPCH              —             —              —           —           —                              PCH[2:0]                        653
CMOUT               —             —              —           —           —               —                C2OUT         C1OUT           653
Legend:       — = unimplemented, read as ‘0’. Shaded cells are unused by the comparator module.


 2017-2021 Microchip Technology Inc.                                                                                DS40001919G-page 652
