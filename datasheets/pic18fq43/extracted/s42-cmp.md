                                                                                                                PIC18F27/47/57Q43
                                                                                                          CMP - Comparator Module


42.    CMP - Comparator Module
       Comparators are used to interface analog circuits to a digital circuit by comparing two analog
       voltages and providing a digital indication of their relative magnitudes. Comparators are very useful
       mixed signal building blocks because they provide analog functionality independent of program
       execution.
       The analog comparator module includes the following features:
       •   Programmable input selection
       •   Programmable output polarity
       •   Rising/falling output edge interrupts
       •   Wake-up from Sleep
       •   Selectable voltage reference
       •   ADC auto-trigger
       •   Inter-connections with other available modules (e.g., timer clocks)

42.1   Comparator Overview
       A single comparator is shown in Figure 42-1 along with the relationship between the analog input
       levels and the digital output. When the analog voltage at VIN+ is less than the analog voltage at VIN-,
       the output of the comparator is a digital low level. When the analog voltage at VIN+ is greater than
       the analog voltage at VIN-, the output of the comparator is a digital high level.

       Figure 42-1. Single Comparator
                                                                                       Rev. 30-000125A
                                                                                              5/17/2017


                                            VIN+           +
                                                                              Output
                                            VIN-           –


                                             VIN-
                                             VIN+


                                        Output

       Note:
       1. The black areas of the output of the comparator represent the uncertainty due to input offsets
          and response time.


--- p779 ---
                                                                                                                                   PIC18F27/47/57Q43
                                                                                                                             CMP - Comparator Module

       Figure 42-2. Comparator Module Simplified Block Diagram

                                                                                                                                          Re v. 10 -00 00 27 R
                                                                                                                                                   2/11 /20 19


                                                                                         Interrupt           INTP
                                                                                               Rising
                                                                                               Edge                                                    set bit
                    NCH                 EN(1)
                                                                                                                                                        CxIF
                                                                                         Interrupt           INTN
                                                                                               Falling
                                                                EN(1)                           Edge

           See CMxNCH                              CxVN
             Register
                                                           -                                                                      Comparator Output
                                                               Cx

                                                   CxVP    +

                                                                HYS     POL


                                                                                                                      CxOUT_sync         To Other
            See CMxPCH                                                                                                                   Peripherals
              Register                                                                       SYNC
                                                                                                                                      TRIS bit
                                                                                                         0
                                                                                                                     PPS                             CxOUT
                                             (1)
                                                                                         D    Q          1
                  PCH                   EN


                                                          (From Timer1 Module) T1CLK
                                                                                                                    RxyPPS


               Note 1:    When EN = 0, all multiplexer inputs are disconnected and the Comparator will produce a ‘0’ at the output.


42.2   Comparator Control
       Each comparator has two control registers: CMxCON0 and CMxCON1.
       The CMxCON0 register contains Control and Status bits for the following:
       •   Enable
       •   Output
       •   Output Polarity
       •   Hysteresis Enable
       •   Timer1 Output Synchronization
       The CMxCON1 register contains Control bits for the following:
       •   Interrupt on Positive/Negative Edge Enables
       The CMxPCH and CMxNCH registers are used to select the positive and negative input channels,
       respectively.

42.2.1 Comparator Enable
       Setting the EN bit enables the comparator for operation. Clearing the EN bit disables the
       comparator, resulting in minimum current consumption.

42.2.2 Comparator Output
       The output of the comparator can be monitored in two different registers. Each output can be read
       individually by reading the OUT bit. Outputs of all the comparators can be collectively accessed by
       reading the CMOUT register.


--- p780 ---
                                                                                                     PIC18F27/47/57Q43
                                                                                               CMP - Comparator Module

       The comparator output can also be routed to an external pin through the RxyPPS register. Refer
       to the “PPS - Peripheral Pin Select Module” chapter for more details. The corresponding TRIS bit
       must be clear to enable the pin as an output.


                    Important: The internal output of the comparator is latched with each
                    instruction cycle. Unless otherwise specified, external outputs are not latched.


42.2.3 Comparator Output Polarity
       Inverting the output of the comparator is functionally equivalent to swapping the comparator
       inputs. The polarity of the comparator output can be inverted by setting the POL bit. Clearing the
       POL bit results in a noninverted output. Table 42-1 shows the Output state versus Input conditions,
       including polarity control.

       Table 42-1. Comparator Output State vs. Input Conditions
                                  Input Condition                                        POL            OUT
                                   CxVn > CxVp                                            0               0
                                   CxVn < CxVp                                            0               1
                                   CxVn > CxVp                                            1               1
                                   CxVn < CxVp                                            1               0


42.3   Comparator Output Synchronization
       The output from a comparator can be synchronized with Timer1 by setting the SYNC bit.
       Once enabled, the comparator output is latched on the falling edge of the Timer1 source clock. If
       a prescaler is used with Timer1, the comparator output is latched after the prescaling function. To
       prevent a Race condition, the comparator output is latched on the falling edge of the Timer1 clock
       source and Timer1 increments on the rising edge of its clock source. A simplified block diagram of
       the comparator module is shown in Figure 42-2. Refer to the “TMR1 - Timer1 Module with Gate
       Control” chapter for more details.

42.4   Comparator Hysteresis
       A selectable amount of separation voltage can be added to the input pins of each comparator to
       provide a hysteresis function to the overall operation. Hysteresis is enabled by setting the HYS bit.
       See the “Comparator Specifications” section for more information.

42.5   Comparator Interrupt
       An interrupt can be generated for every rising or falling edge of the comparator output.
       When either edge detector is triggered and its associated enable bit is set (INTP and/or INTN bits),
       the Corresponding Interrupt Flag bit (CxIF bit of the respective PIR register) will be set.
       To enable the interrupt, the following bits must be set:
       •   EN bit
       •   INTP bit (for a rising edge detection)
       •   INTN bit (for a falling edge detection)
       •   CxIE bit of the respective PIE register
       •   GIE bit of the INTCON0 register
       The associated interrupt flag bit, CxIF bit of the respective PIR register, must be cleared in software
       to successfully detect another edge.


--- p781 ---
                                                                                               PIC18F27/47/57Q43
                                                                                         CMP - Comparator Module

                   Important: Although a comparator is disabled, an interrupt will be generated by
                   changing the output polarity with the POL bit.


42.6   Comparator Positive Input Selection
       Configuring the PCH bits direct an internal voltage reference or an analog pin to the noninverting
       input of the comparator.
       Any time the comparator is disabled (EN = 0), all comparator inputs are disabled.

42.7   Comparator Negative Input Selection
       The NCH bits direct an analog input pin, internal reference voltage or analog ground to the inverting
       input of the comparator.


                   Important: To use CxINy+ and CxINy- pins as analog input, the appropriate bits
                   must be set in the ANSEL register and the corresponding TRIS bits must also be
                   set to disable the output drivers.


42.8   Comparator Response Time
       The comparator output is indeterminate for a period of time after the change of an input source
       or the selection of a new reference voltage. This period is referred to as the response time. The
       response time of the comparator differs from the settling time of the voltage reference. Therefore,
       both of these times must be considered when determining the total response time to a comparator
       input change. See the Comparator and Voltage Reference Specifications in the “Comparator
       Specifications” and “Fixed Voltage Reference (FVR) Specifications” sections for more details.

42.9   Analog Input Connection Considerations
       A simplified circuit for an analog input is shown in Figure 42-3. Since the analog input pins share
       their connection with a digital input, they have reverse biased ESD protection diodes to VDD and
       VSS. The analog input, therefore, must be between VSS and VDD. If the input voltage deviates from
       this range by more than 0.6V in either direction, one of the diodes is forward biased and abnormal
       behavior may occur.
       A maximum source impedance of 10 kΩ is recommended for the analog sources. Also, any external
       component connected to an analog input pin, such as a capacitor or a Zener diode, will have very
       little leakage current to minimize corrupting the result.
       Notes:
       1. When reading a PORT register, all pins configured as analog inputs will read as a ‘0’. Pins
          configured as digital inputs will convert as an analog input, according to the input specification.
       2. Analog levels on any pin defined as a digital input may cause the input buffer to consume more
          current than specified.


--- p782 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                         CMP - Comparator Module

       Figure 42-3. Analog Input Model

                                                                                                           Re v. 10 -00 00 71D
                                                       VDD                                                          2/11 /20 19


                                          Analog
                                                             VT   0.6V
                               RS        Input pin                                   RIC
                                                                                                       To Comparator


                        VA                  CPIN             VT   0.6V        ILEAKAGE(1)
                                            5 pF


                                                                              VSS


                      Legend: CPIN       = Input Capacitance
                              ILE AKAG E = Leakage Current at the pin due to various junctions
                              RIC        = Interconnect Resistance
                              RS         = Source Impedance
                              VA         = Analog Voltage
                              VT         = Diode Forward Voltage

                      Note:
                       1. See the "Electrical Specifications" chapter.


42.10 Operation in Sleep Mode
       The comparator module can operate during Sleep. A comparator interrupt will wake the device from
       Sleep. The CxIE bits of the respective PIE register must be set to enable comparator interrupts.
       The comparator clock source is based on the Timer1 clock source. If the Timer1 clock source is either
       the system clock (FOSC) or the instruction clock (FOSC/4), Timer1 will not operate during Sleep, and
       synchronized comparator outputs will not operate.

42.11 ADC Auto-Trigger Source
       The output of the comparator module can be used to trigger an ADC conversion. When the
       ADACT register is set to trigger on a comparator output, an ADC conversion will trigger when the
       comparator output goes high.

42.12 Register Definitions: Comparator Control
       Long bit name prefixes for the Comparator peripherals are shown in the table below. Refer to
       the “Long Bit Names” section in the “Register and Bit Naming Conventions” chapter for more
       information.

       Table 42-2. Comparator Long Bit Name Prefixes
                              Peripheral                                                    Bit Name Prefix
                                    C1                                                            C1
                                    C2                                                            C2


--- p783 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                         CMP - Comparator Module

42.12.1 CMxCON0

           Name:       CMxCON0
           Address:    0x070,0x074

           Comparator Control Register 0

     Bit        7             6                 5             4                3                2         1            0
               EN            OUT                             POL                                         HYS         SYNC
  Access       R/W            R                              R/W                                         R/W          R/W
   Reset        0             0                               0                                           0            0

Bit 7 – EN Comparator Enable
           Value      Description
           1          Comparator is enabled
           0          Comparator is disabled and consumes no active power

Bit 6 – OUT Comparator Output
           Value      Condition                                                                     Description
           1          If POL = 0 (noninverted polarity):                                            CxVP > CxVN
           0          If POL = 0 (noninverted polarity):                                            CxVP < CxVN
           1          If POL = 1 (inverted polarity):                                               CxVP < CxVN
           0          If POL = 1 (inverted polarity):                                               CxVP > CxVN


Bit 4 – POL Comparator Output Polarity Select
           Value      Description
           1          Comparator output is inverted
           0          Comparator output is not inverted

Bit 1 – HYS Comparator Hysteresis Enable
           Value      Description
           1          Comparator hysteresis enabled
           0          Comparator hysteresis disabled

Bit 0 – SYNC Comparator Output Synchronous Mode
           Value      Description
           1          Comparator output to Timer1 and I/O pin is synchronous to changes on Timer1 clock source. Output updated
                      on the falling edge of Timer1 clock source.
           0          Comparator output to Timer1 and I/O pin is asynchronous


--- p784 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                         CMP - Comparator Module

42.12.2 CMxCON1

           Name:        CMxCON1
           Address:     0x071,0x075

           Comparator Control Register 1

     Bit           7            6               5               4                  3           2           1            0
                                                                                                         INTP         INTN
  Access                                                                                                 R/W           R/W
   Reset                                                                                                   0            0

Bit 1 – INTP Comparator Interrupt on Positive-Going Edge Enable
           Value       Description
           1           The CxIF interrupt flag will be set upon a positive-going edge of the CxOUT bit
           0           No interrupt flag will be set on a positive-going edge of the CxOUT bit

Bit 0 – INTN Comparator Interrupt on Negative-Going Edge Enable
           Value       Description
           1           The CxIF interrupt flag will be set upon a negative-going edge of the CxOUT bit
           0           No interrupt flag will be set on a negative-going edge of the CxOUT bit


--- p785 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                                CMP - Comparator Module

42.12.3 CMxNCH

            Name:      CMxNCH
            Address:   0x072,0x076

            Comparator Inverting Channel Select Register

      Bit        7           6           5              4                  3             2       1             0
                                                                                              NCH[2:0]
  Access                                                                            R/W         R/W           R/W
   Reset                                                                             0           0             0

Bits 2:0 – NCH[2:0] Comparator Inverting Input Channel Select
                                  NCH                                            Negative Input Sources
                                  111                                                      VSS
                                  110                                                 FVR_Buffer2
                                  101                                             NCH not connected
                                  100                                             NCH not connected
                                  011                                                    CxIN3-
                                  010                                                    CxIN2-
                                  001                                                    CxIN1-
                                  000                                                    CxIN0-


--- p786 ---
                                                                                                     PIC18F27/47/57Q43
                                                                                               CMP - Comparator Module

42.12.4 CMxPCH

           Name:      CMxPCH
           Address:   0x073,0x077

           Comparator Noninverting Channel Select Register

     Bit        7           6           5             4                  3             2        1             0
                                                                                             PCH[2:0]
  Access                                                                          R/W          R/W           R/W
   Reset                                                                           0            0             0

Bits 2:0 – PCH[2:0] Comparator Noninverting Input Channel Select
                                PCH                                             Positive Input Sources
                                111                                                       VSS
                                110                                                  FVR_Buffer2
                                101                                                  DAC_Output
                                100                                              PCH not connected
                                011                                              PCH not connected
                                010                                              PCH not connected
                                001                                                     CxIN1+
                                000                                                     CxIN0+


--- p787 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                            CMP - Comparator Module

42.12.5 CMOUT

           Name:      CMOUT
           Address:   0x06F

           Comparator Output Register

     Bit        7          6            5              4                  3             2     1           0
                                                                                            C2OUT       C1OUT
  Access                                                                                      R           R
   Reset                                                                                      0           0

Bits 0, 1 – CxOUT Mirror copy of the CMxCON0.OUT


--- p788 ---
                                                                                              PIC18F27/47/57Q43
                                                                                        CMP - Comparator Module

42.13 Register Summary - Comparator
Address    Name     Bit Pos.   7         6           5              4        3      2        1            0
 0x6F      CMOUT      7:0                                                                  C2OUT       C1OUT
 0x70     CM1CON0     7:0      EN       OUT                        POL                       HYS        SYNC
 0x71     CM1CON1     7:0                                                                   INTP        INTN
 0x72     CM1NCH      7:0                                                                 NCH[2:0]
 0x73      CM1PCH     7:0                                                                 PCH[2:0]
 0x74     CM2CON0     7:0      EN       OUT                        POL                       HYS        SYNC
 0x75     CM2CON1     7:0                                                                   INTP        INTN
 0x76     CM2NCH      7:0                                                                 NCH[2:0]
 0x77      CM2PCH     7:0                                                                 PCH[2:0]


--- p789 ---
