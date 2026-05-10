                       PIC18(L)F26/27/45/46/47/55/56/57K42
36.0     ANALOG-TO-DIGITAL
         CONVERTER WITH
         COMPUTATION (ADC2)
         MODULE
The Analog-to-Digital Converter with Computation
(ADC2) allows conversion of an analog input signal to
a 12-bit binary representation of that signal. This device
uses analog inputs, which are multiplexed into a single
sample and hold circuit. The output of the sample and
hold is connected to the input of the converter. The
converter generates a 12-bit binary result via
successive approximation and stores the conversion
result into the ADC result registers (ADRESH:ADRESL
register pair).
Additionally, the following features are provided within
the ADC module:
• 13-bit Acquisition Timer
• Hardware Capacitive Voltage Divider (CVD)
  support:
  - 13-bit Precharge Timer
  - Adjustable sample and hold capacitor array
  - Guard ring digital output drive
• Automatic repeat and sequencing:
  - Automated double sample conversion for
    CVD
  - Two sets of result registers (Result and
    Previous result)
  - Auto-conversion trigger
  - Internal retrigger
• Computation features:
  - Averaging and Low-Pass Filter functions
  - Reference Comparison
  - 2-level Threshold Comparison
  - Selectable Interrupts
Figure 36-1 shows the block diagram of the ADC.
The ADC voltage reference is software selectable to be
either internally generated or externally supplied.
The ADC can generate an interrupt upon completion of
a conversion and upon threshold comparison. These
interrupts can be used to wake up the device from
Sleep.


 2017-2021 Microchip Technology Inc.                        DS40001919G-page 602
                          PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 36-1:               ADC2 BLOCK DIAGRAM
                                                                            PREF<1:0>                                               Rev. 10-000034D
                                                                                                                                           3/13/2019


                                        FVR_buffer1            11        Positive
                                          VREF+ pin                     Reference
                                                               10         Select
                                           Reserved            01
                                                               00
                                                                            NREF
                                                  VDD
                                                        VREF- pin      1
                                                                       0
                                                         VSS                                             CS
                  AN0
                  ANa                                                        Vref-   Vref+
   External                 .
   Channel                  .                                                                                      FOSC /n Fosc
                            .                                                                                             Divider   FOSC
     Inputs                                                                                  ADC_clk    ADC
                  ANz                                       sampled                                     Clock
                                VSS                           input                                     Select        ADCRC
                                                                                                                                    ADCRC
                 Temp Indicator
    Internal
   Channel         DACx_output                                                                         ADC CLOCK SOURCE
      Inputs
                       FVR_buffer                                   ADC
                                                                 Sample Circuit
                       PCH<5:0>
                                                                                                              FM
                           set bit ADIF

                                                                                               12
                                                            complete                                    12-bit Result
        Write to bit
                                 GO/DONE
        GO/DONE                                                                                                  16
                                                               start
                                                                                                    ADRESH         ADRESL
                                                                             Enable


                                Trigger Select
        ACT<4:0>                                                       ON
                                   . . .                                             VSS
                                Trigger Sources


                          AUTO CONVERSION
                              TRIGGER


 2017-2021 Microchip Technology Inc.                                                                                    DS40001919G-page 603
                      PIC18(L)F26/27/45/46/47/55/56/57K42
36.1      ADC Configuration                               36.1.3       ADC VOLTAGE REFERENCE
When configuring and using the ADC the following          The PREF[1:0] bits of the ADREF register provide
functions must be considered:                             control of the positive voltage reference. The positive
                                                          voltage reference can be:
• Port configuration
                                                          • VREF+ pin
• Channel selection
                                                          • VDD
• ADC voltage reference selection
                                                          • FVR outputs
• ADC conversion clock source
• Interrupt control                                       The NREF bit of the ADREF register provides control of
                                                          the negative voltage reference. The negative voltage
• Result formatting
                                                          reference can be:
• Conversion Trigger Selection
                                                          • VREF- pin
• ADC Acquisition Time
                                                          • VSS
• ADC Precharge Time
                                                          See Section 34.0 “Fixed Voltage Reference (FVR)”
• Additional Sample and Hold Capacitor
                                                          for more details on the Fixed Voltage Reference.
• Single/Double Sample Conversion
• Guard Ring Outputs                                      36.1.4        CONVERSION CLOCK
                                                          The conversion clock source is selected with the CS bit
36.1.1      PORT CONFIGURATION
                                                          in the ADCON0 register. When CS = 1 the ADC clock
The ADC will convert the voltage level on a pin whether   source is an internal fixed-frequency clock referred to
or not the ANSEL bit is set. When converting analog       as ADCRC. When CS = 0 the ADC clock source is
signals, the I/O pin may be configured for analog by      derived from FOSC.
setting the associated TRIS and ANSEL bits. Refer to
Section 16.0 “I/O Ports” for more information.              Note:      When ADCON0.CS = 0, the clock can be
                                                                       divided using the ADCLK register to meet
  Note:     Analog voltages on any pin that is defined                 the ADC clock period requirements.
            as a digital input may cause the input
            buffer to conduct excess current.             The time to complete one bit conversion is defined as
                                                          TAD. Refer Figure 36-2 for the complete timing details
36.1.2      CHANNEL SELECTION                             of the ADC conversion.

There are several channel selections available:           For correct conversion, the appropriate TAD specification
                                                          must be met. Refer to Table 44-15 for more information.
• Eight PORTA pins (RA[7:0])                              Table 36-1 gives examples of appropriate ADC clock
• Eight PORTB pins (RB[7:0])                              selections.
• Eight PORTC pins (RC[7:0])
                                                             Note 1: Unless using the ADCRC, any changes
• Eight PORTD pins (RD[7:0], PIC18(L)F45/46/47/                      in the system clock frequency will change
  55/56/57K42 only)                                                  the ADC clock frequency, which may
• Three PORTE pins (RE[2:0], PIC18(L)F45/46/47/                      adversely affect the ADC result.
  55/56/57K42 only)
                                                                    2: The internal control logic of the ADC runs
• Eight PORTF pins (RD[7:0], PIC18(L)F55/56/                           off of the clock selected by the CS bit of
  57K42 only)                                                          ADCON0. What this can mean is when
• Temperature Indicator                                                the CS bit of ADCON0 is set to ‘1’ (ADC
• DAC output                                                           runs on ADCRC), there may be
• Fixed Voltage Reference (FVR)                                        unexpected delays in operation when
                                                                       setting ADC control bits.
• VSS (ground)
The ADPCH register determines which channel is
connected to the sample and hold circuit.
When changing channels, a delay is required before
starting the next conversion.
Refer to Section 36.2 “ADC Operation” for more
information.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 604
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 36-1:           ADC CLOCK PERIOD (TAD) VS. DEVICE OPERATING FREQUENCIES(1,3)
                                                                               Device Frequency (FOSC)
     ADC
                            CS[5:0]              64 MHz        32 MHz        20 MHz       16 MHz       8 MHz          4 MHz           1 MHz
 Clock Source
                                                   TAD           TAD           TAD          TAD         TAD            TAD             TAD

FOSC/2                      000000              31.25 ns(2)   62.5 ns(2)    100 ns(2)    125 ns(2)    250 ns(2)       500 ns          2.0 s
FOSC/4                      000001              62.5 ns(2)    125 ns(2)     200 ns(2)    250 ns(2)     500 ns         1.0 s          4.0 s
FOSC/6                      000010              93.75 ns(2)   187.5 ns(2)   300 ns(2)    375 ns(2)     750 ns         1.5 s          6.0 s
FOSC/8                      000011              125 ns(2)     250 ns(2)     400 ns(2)     500 ns       1.0 s         2.0 s          8.0 s
...                            ...                  ...           ...           ...          ...          ...            ...               ...
FOSC/16                     000111              250 ns(2)       500 ns       800 ns       1.0 s       2.0 s         4.0 s      16.0 s(2)
...                            ...                  ...           ...           ...          ...          ...            ...               ...
FOSC/128                    111111                2.0 s        4.0 s       6.4 s       8.0 s      16.0 s(2)     32.0 s(2)   128.0 s(2)
ADCRC                   ADCON0.CS = 1           1.0-6.0 s    1.0-6.0 s    1.0-6.0 s   1.0-6.0 s   1.0-6.0 s    1.0-6.0 s    1.0-6.0 s
Legend:       Shaded cells are outside of recommended range.
Note 1:       See TAD parameter for ADCRC source typical TAD value.
      2:      These values violate the required TAD time.
      3:      The ADC clock period (TAD) and total ADC conversion time can be minimized when the ADC clock is derived from the system
              clock FOSC. However, the ADCRC oscillator source must be used when conversions are to be performed with the device in
              Sleep mode.


FIGURE 36-2:              ANALOG-TO-DIGITAL CONVERSION CYCLES
                                                                                                                                  Rev. 10-000035E
                                                                                                                                          6/1/2017
         Precharge            Acquisition/                                   ADC Conversion Time
            Time             Sharing Time
        1-8191 FOSC          1-8191 FOSC
           (TPRE)               (TACQ)


  External and Internal External and Internal
  Channels are          Channels share                        Holding capacitor CHOLD is
  charged/discharged charge                                   disconnected from analog input (1)

                                                                                                         On the following cycle: (1)
                                                If ADPRE = 0                                             ADRES is loaded
      If ADPRE ≠ 0        If ADACQ ≠ 0          If ADACQ = 0                                             GO bit is cleared
                                                                                                         ADIF bit is set


 Set GO bit

      Note 1: Refer to Table 44-15 for ADC Conversion Timing Specifications.


 2017-2021 Microchip Technology Inc.                                                                              DS40001919G-page 605
                       PIC18(L)F26/27/45/46/47/55/56/57K42
36.1.5       INTERRUPTS                                            36.1.6        RESULT FORMATTING
The ADC module allows for the ability to generate an               The 12-bit ADC conversion result can be supplied in
interrupt upon completion of an Analog-to-Digital                  two formats, left justified or right justified. The FM bits
conversion. The ADC Interrupt Flag is the ADIF bit in              of the ADCON0 register controls the output format.
the PIRx register. The ADC Interrupt Enable is the                 Figure 36-3 shows the two output formats.
ADIE bit in the PIEx register. The ADIF bit must be
cleared in software.                                               Writes to the ADRES register pair are always right
                                                                   justified regardless of the selected format mode. There-
   Note 1: The ADIF bit is set at the completion of                fore, data read after writing to ADRES when FM = 0 will
           every conversion, regardless of whether                 be shifted left four places.
           or not the ADC interrupt is enabled.
         2: The ADC operates during Sleep only
            when the ADCRC oscillator is selected.
This interrupt can be generated while the device is
operating or while in Sleep. If the device is in Sleep, the
interrupt will wake up the device. Upon waking from
Sleep, the next instruction following the SLEEP
instruction is always executed. If the user is attempting
to wake up from Sleep and resume in-line code
execution, the ADIE bit of the PIEx register and the GIE
bits of the INTCON0 register must both be set. If all
these bits are set, the execution will switch to the
Interrupt Service Routine.

FIGURE 36-3:            12-BIT ADC CONVERSION RESULT FORMAT


                                           ADRESH                                               ADRESL
         (FM = 0)       MSB
                        bit 7                                      bit 0       bit 7           LSB                    bit 0


                                                       12-bit ADC Result                               Unimplemented:
                                                                                                        Read as ‘0’


         (FM = 1)                               MSB                                                                   LSB
                        bit 7                                      bit 0       bit 7                                  bit 0


                         Unimplemented: Read as ‘0’                        12-bit ADC Result


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 606
                       PIC18(L)F26/27/45/46/47/55/56/57K42
36.2        ADC Operation                                  36.2.4      EXTERNAL TRIGGER DURING
                                                                       SLEEP
36.2.1       STARTING A CONVERSION
                                                           If the external trigger is received during Sleep while
To enable the ADC module, the ON bit of the ADCON0         ADC clock source is set to the ADCRC, ADC module
register must be set to a ‘1’. A conversion may be         will perform the conversion and set the ADIF bit upon
started by any of the following:                           completion.
• Software setting the GO bit of ADCON0 to ‘1’             If an external trigger is received when the ADC clock
• An external trigger (selected by Register 36-3)          source is something other than ADCRC, the trigger will
• A continuous-mode retrigger (see section Sec-            be recorded, but the conversion will not begin until the
  tion 36.5.8 “Continuous Sampling mode”)                  device exits Sleep.
.
                                                           36.2.5      AUTO-CONVERSION TRIGGER
    Note:    The GO bit may not be set in the same
                                                           The auto-conversion trigger allows periodic ADC
             instruction that turns on the ADC. Refer to
                                                           measurements without software intervention. When a
             Section 36.2.6 “ADC Conversion Pro-
                                                           rising edge of the selected source occurs, the GO bit is
             cedure (Basic Mode)”.
                                                           set by hardware.
36.2.2       COMPLETION OF A CONVERSION                    The auto-conversion trigger source is selected by the
                                                           ADACT register.
When any individual conversion is complete, the value
already in ADRES is written into PREV (if PSIS = 1)        Using the auto-conversion trigger does not assure
and the new conversion results appear in ADRES.            proper ADC timing. It is the user’s responsibility to
When the conversion completes, the ADC module will:        ensure that the ADC timing requirements are met. See
                                                           Register 36-33 for auto-conversion sources.
• Clear the GO bit (unless the CONT bit of
  ADCON0 is set)
• Set the ADIF Interrupt Flag bit
• Set the MATH bit
• Update ACC
When DSEN = 0 then after every conversion, or when
DSEN = 1 then after every other conversion, the follow-
ing events occur:
• ERR is calculated
• ADTIF is set if ERR calculation meets threshold
  comparison
Importantly, filter and threshold computations occur
after the conversion itself is complete. As such,
interrupt handlers responding to ADIF may check
ADTIF before reading filter and threshold results.

36.2.3       ADC OPERATION DURING SLEEP
The ADC module can operate during Sleep. This
requires the ADC clock source to be set to the ADCRC
option. When the ADCRC oscillator source is selected,
the ADC waits one additional instruction before starting
the conversion. This allows the SLEEP instruction to be
executed, which can reduce system noise during the
conversion. If the ADC interrupt is enabled, the device
will wake up from Sleep when the conversion
completes. If the ADC interrupt is disabled, the device
remains in Sleep and the ADC module is turned off
after the conversion completes, although the ON bit
remains set.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 607
                          PIC18(L)F26/27/45/46/47/55/56/57K42
36.2.6          ADC CONVERSION PROCEDURE                   7.    Read ADC Result.
                (BASIC MODE)                               8.    Clear the ADC interrupt flag (required if interrupt
This is an example procedure for using the ADC to                is enabled).
perform an analog-to-digital conversion:                        Note 1: The global interrupt can be disabled if the
1.       Configure Port:                                                user is attempting to wake up from Sleep
                                                                        and resume in-line code execution.
         • Disable pin output driver (Refer to the TRISx
            register)                                                2: Refer to Section 36.3 “ADC Acquisi-
         • Configure pin as analog (Refer to the                        tion Requirements”.
            ANSELx register)
2.       Configure the ADC module:
         • Select ADC conversion clock
         • Select voltage reference
         • Select ADC input channel
         • Precharge and acquisition
         • Turn on ADC module
3.       Configure ADC interrupt (optional):
         • Clear ADC interrupt flag
         • Enable ADC interrupt
         • Enable global interrupt(1)
4.       If ADACQ = 0, software must wait the required
         acquisition time(2).
5.       Start conversion by setting the GO bit.
6.       Wait for ADC conversion to complete by one of
         the following:
         • Polling the GO bit
         • Polling the ADIF bit
         • Waiting for the ADC interrupt (interrupts
            enabled)

EXAMPLE 36-1:             ADC CONVERSION
     /*This code block configures the ADC
     for polling, VDD and VSS references, ADCRC
     oscillator and AN0 input.
     Conversion start & polling for completion
     are included.
      */
     void main() {
         //System Initialize
         initializeSystem();

           //Setup ADC
           ADCON0bits.FM = 1; //right justify
           ADCON0bits.CS = 1; //ADCRC Clock
           ADPCH = 0x00; //RA0 is Analog channel
           TRISAbits.TRISA0 = 1; //Set RA0 to input
           ANSELAbits.ANSELA0 = 1; //Set RA0 to analog
           ADCON0bits.ON = 1; //Turn ADC On

           while (1) {
               ADCON0bits.GO = 1; //Start conversion
               while (ADCON0bits.GO); //Wait for conversion done
               resultHigh = ADRESH; //Read result
               resultLow = ADRESL; //Read result
           }
     }


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 608
                         PIC18(L)F26/27/45/46/47/55/56/57K42
36.3     ADC Acquisition Requirements                                  impedance is decreased, the acquisition time may be
                                                                       decreased. After the analog input channel is selected
For the ADC to meet its specified accuracy, the charge                 (or changed), an ADC acquisition must be completed
holding capacitor (CHOLD) must be allowed to fully                     before the conversion can be started. To calculate the
charge to the input channel voltage level. The Analog                  minimum acquisition time, Equation 36-1 may be used.
Input model is shown in Figure 36-4. The source                        This equation assumes that 1/2 LSb error is used
impedance (RS) and the internal sampling switch (RSS)                  (4,096 steps for the ADC). The 1/2 LSb error is the
impedance directly affect the time required to charge                  maximum error allowed for the ADC to meet its
the capacitor CHOLD. The sampling switch (RSS)                         specified resolution.
impedance varies over the device voltage (VDD), refer
to Figure 36-4. Refer to Parameter AD08 mentioned in
Table 44-14 for the maximum recommended
impedance for analog sources. If the source

EQUATION 36-1:             ACQUISITION TIME EXAMPLE

   Assumptions:         Tem perature = 50°C and externalim pedance of1k 5.0V V D D

                TAC Q = Am plifier Settling Tim e + H old Capacitor Charging Tim e + Tem perature Coefficient
                      = TAM P + TC + TC O FF
                      = 2µs + TC +   Tem perature -25°C   0.05µs/°C  

  The value for TC can be approximated with the following equations:


        V AP P LIED  1 – ------n----
                                     ---------------- = V C H O LD
                                       1
                                                                              ;[1] VCHOLD charged to within 1/2 lsb
                                     +1
                           2               –1
                                –TC
                          ---------
                            RC
        V AP P LIED  1 – e  = V C H O LD                                    ;[2] VCHOLD charge response to VAPPLIED
                                   
                                –Tc
                          --------
        V AP P LIED  1 – e  = V A P PLIE D  1 – ------n----
                                                              ---------------- ;combining [1] and [2]
                            RC                                  1
                                                  2
                                                              +1
                                                                     –1

        Note: Where n = number of bits of the ADC.


  Solving for TC:

                 TC = –C H O LD  R IC + R SS + R S ln(1/8191)
                    = –28pF  1k + 7k + 1k  ln(0.0001221)
                       = 2.27µs
   Therefore:
                TAC Q = 2µs + 2.27µs +   50°C-25°C   0.05µs/°C  
                        = 5.52µs


   Note 1: The reference voltage (VREF) has no effect on the equation, since it cancels itself out.
         2: The charge holding capacitor (CHOLD) is not discharged after each conversion.
         3: The maximum recommended impedance for analog sources is mentioned in Parameter AD08 in Table 44-
            14. This is required to meet the pin leakage specification.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 609
                              PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 36-4:                        ANALOG INPUT MODEL

                                                                                                    Sampling
                                                       VDD                                                                      Rev. 10-000070C
                                                                                                                                       4/16/2019
                                                                                                     Switch
                                           Analog
                                                             VT ≈ 0.6V                         SS
                  RS                      Input pin                               RIC ≤ 1KΩ               RSS


           VA                                   CPIN         VT ≈ 0.6V        ILEA KAGE (1)                             CHOLD = 28 PF
                                                5pF


                                                                              VSS                                        Ref-


         Legend: CPIN     = Input Capacitance
                 ILEAKAGE = Leakage Current at the pin due to various junctions                                 11
                 RIC      = Interconnect Resistance                                                  Sampling 109
                 RS       = Source Impedance                                                          Switch    8         RSS
                 VA       = Analog Voltage                                                            (KΩ )     7
                 VT       = Diode Forward Voltage                                                                6
                                                                                                                 5
                 SS       = Sampling Switch
                 RSS      = Resistance of the Sampling Switch
                 CHOLD    = Sample/Hold Capacitance                                                                     2 3 4 5 6
                                                                                                                            VDD
         Note:                                                                                                              (V)
          1. Refer to Table 44-4 (parameter D340 and D341).


FIGURE 36-5:                        ADC TRANSFER FUNCTION


                                                               Full-Scale Range


                                            FFFh
                                           FFEh
                                           FFDh
                                           FFCh
                       ADC Output Code


                                           FFBh


                                                03h
                                                02h
                                                01h
                                                00h
                                                                                               Analog Input Voltage
                                                        0.5 LSB                                1.5 LSB

                                         REF-           Zero-Scale
                                                        Transition           Full-Scale
                                                                             Transition       REF+


 2017-2021 Microchip Technology Inc.                                                                                DS40001919G-page 610
                      PIC18(L)F26/27/45/46/47/55/56/57K42
36.4     ADC Charge Pump                                       36.5      Computation Operation
The ADC module has a dedicated charge pump which               The ADC module hardware is equipped with post
can be controlled through the ADCP register                    conversion computation features. These features
(Register 36-36). The primary purpose of the charge            provide data post-processing functions that can be
pump is to supply a constant voltage to the gates of           operated on the ADC conversion result, including
transistor devices in the A/D converter, signal and            digital filtering/averaging and threshold comparison
reference input pass-gates, to prevent degradation of          functions.
transistor performance at low operating voltage.
The charge pump can be enabled by setting the CPON
bit in the ADCP register. Once enabled, the pump will
undergo a start-up time to stabilize the charge pump
output. Once the output stabilizes and is ready for use,
the CPRDY bit of the ADCP register will be set.

FIGURE 36-6:           COMPUTATIONAL FEATURES SIMPLIFIED BLOCK DIAGRAM

                                                             CALC                                     Rev. 10-000260C
                                                                                                             4/16/2019


                                                                                      TMD
         ADRES
                         CRS
                                            ADFLTR
                                                                                                             Set
                                                             Error       ADERR      Threshold
                                                                                                          Interrupt
                       Average/                            Calculation                Logic
                                        1                                                                   Flag
                        Filter                ADPREV
                                        0
                                              ADSTPT
                                                                                 ADUTH      ADLTH
                          PSIS


The operation of the ADC computational features is             • Low-Pass Filter (LPF): With each trigger, the ADC
controlled by MD[2:0] bits in the ADCON2 register.             conversion result is sent through a filter. When RPT
The module can be operated in one of five modes:               samples have occurred, a threshold test is performed.
                                                               Every trigger after that the ADC conversion result is
• Basic: In this mode, ADC conversion occurs on single         sent through the filter and another threshold test is
(DSEN = 0) or double (DSEN = 1) samples. ADIF is               performed.
set after all the conversion are complete.
                                                               The five modes are summarized in Table 36-2 below.
• Accumulate: With each trigger, the ADC conversion
result is added to accumulator and CNT increments.
ADIF is set after each conversion. ADTIF is set
according to the calculation mode.
• Average: With each trigger, the ADC conversion
result is added to the accumulator. When the RPT
number of samples have been accumulated, a
threshold test is performed. Upon the next trigger, the
accumulator is cleared. For the subsequent tests,
additional RPT samples are required to be
accumulated.
• Burst Average: At the trigger, the accumulator is
cleared. The ADC conversion results are then collected
repetitively until RPT samples are accumulated and
finally the threshold is tested.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 611
 2017-2021 Microchip Technology Inc.


                                        TABLE 36-2:         COMPUTATION MODES
                                                              Bit Clear Conditions              Value after Trigger completion                           Threshold Operations                            Value at ADTIF interrupt

                                        Mode          MD          ACC and CNT                   ACC                        CNT               Retrigger    Threshold Test       Interrupt         ADAOV                 FLTR          CNT

                                        Basic          0            ACLR = 1                 Unchanged                  Unchanged               No        Every Sample     If threshold=true       N/A                  N/A          count

                                        Accumulate     1            ACLR = 1                  S + ACC              If (CNT=0xFF): CNT,          No        Every Sample     If threshold=true   ACC Overflow         ACC/2CRS         count
                                                                                                 or                  otherwise: CNT+1


                                                                                                                                                                                                                                             PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                           (S2-S1) + ACC
                                        Average        2    ACLR = 1 or CNT>=RPT at           S + ACC              If (CNT=0xFF): CNT,          No        If CNT>=RPT      If threshold=true   ACC Overflow         ACC/2CRS         count
                                                                GO or retrigger                  or                  otherwise: CNT+1
                                                                                           (S2-S1) + ACC
                                        Burst          3      ACLR = 1 or GO set or    Each repetition: same as   Each repetition: same as    Repeat      If CNT>=RPT      If threshold=true   ACC Overflow         ACC/2CRS         RPT
                                        Average                     retrigger                 Average                    Average               while
                                                                                         End with sum of all        End with CNT=RPT         CNT<RPT
                                                                                              samples
                                        Low-pass       4            ACLR = 1                S+ACC-ACC/            Count up, stop counting       No        If CNT>=RPT      If threshold=true   ACC Overflow          ACC/2CRS        count
                                        Filter                                                  2CRS                when CNT = 0xFF                                                                               (Filtered Value)
                                                                                                 or
                                                                                       (S2-S1)+ACC-ACC/2CRS
                                         Note:       S1 and S2 are abbreviations for Sample 1 and Sample 2, respectively. When DSEN = 0, S1 = ADRES; When DSEN = 1, S1 = PREV and S2 = ADRES.
DS40001919G-page 612
                       PIC18(L)F26/27/45/46/47/55/56/57K42
36.5.1      DIGITAL FILTER/AVERAGE                               the ADSTAT register, as well as the ADCNT register.
                                                                 The ACLR bit is cleared by the hardware when
The digital filter/average module consists of an
                                                                 accumulator clearing action is complete.
accumulator with data feedback options, and control
logic to determine when threshold tests need to be
applied. The ADACC register is a 24-bit wide register              Note:     When ADC is operating from ADCRC, five
which     can     be     accessed     through     the                        ADCRC clock cycles are required to
ADACCU:ADACCH:ADACCL register pair. It contains                              execute the ACC clearing operation.
18-bit accumulator value ACC [17:0] and one extended             The CRS [2:0] bits in the ADCON2 register control the
sign bit.                                                        data shift on the accumulator result, which effectively
Upon each trigger event (the GO bit set or external              divides        the       value          in      accumulator
event trigger), the ADC conversion result is added to            (ADACCU:ADACCH:ADACCL) register pair. The right-
the accumulator. If the accumulated result exceeds               shifted     value     is    stored       in   the    signed
2(accumulator_width)-1 = 262143, the overflow bit ADAOV          ADFLTRH:ADFLTRL register pair. When the value in
in the ADSTAT register is set.                                   the ADFLTR register overflows, the overflow bit
                                                                 ADAOV in the ADSTAT register is set. For the
The number of samples to be accumulated is
                                                                 Accumulate mode of the digital filter, the shift provides
determined by the RPT (A/D Repeat Setting) register.
                                                                 a simple scaling operation. For the Average/Burst
Each time a sample is added to the accumulator, the
                                                                 Average mode, the shift bits are used to determine the
ADCNT register is incremented. Once RPT samples
                                                                 number of logical right shifts to be performed on the
are accumulated (CNT = RPT), an accumulator clear
                                                                 accumulated result. For the Low-pass Filter mode, the
command can be issued by the software by setting the
                                                                 shift is an integral part of the filter, and determines the
ACLR bit in the ADCON2 register. Setting the ACLR bit
                                                                 cut-off frequency of the filter. Table 36-3 shows the -3
will also clear the ADAOV (Accumulator overflow) bit in
                                                                 dB cut-off frequency in ωT (radians) and the highest
                                                                 signal attenuation obtained by this filter at nyquist
                                                                 frequency (ωT = π).


TABLE 36-3:        LOW-PASS FILTER -3 dB CUT-OFF FREQUENCY
               ADCRS                     ωT (radians) @ -3 dB Frequency                  dB @ Fnyquist=1/(2T)
                  1                                       0.72                                     -9.5
                  2                                      0.284                                    -16.9
                  3                                      0.134                                    -23.5
                  4                                      0.065                                    -29.8
                  5                                      0.032                                    -36.0
                  6                                      0.016                                    -42.0

36.5.2      BASIC MODE                                           comparison performed on it (see Section
                                                                 36.5.7 “Threshold Comparison”) and the ADTIF
Basic mode (MD = 000) disables all additional
                                                                 interrupt may trigger.
computation features. In this mode, no accumulation
occurs but threshold error comparison is performed.
                                                                 36.5.4      AVERAGE MODE
Double sampling, Continuous mode, and all CVD
features are still available, but no features involving the      In Average mode (MD = 010), the ADACC registers
digital filter/average features are used.                        accumulate with each ADC sample, much as in
                                                                 Accumulate mode, and the ADCNT register increments
36.5.3      ACCUMULATE MODE                                      with each sample. The ADFLTR register is also
                                                                 updated with the right-shifted value of the ADACC
In Accumulate mode (MD = 001), after every
                                                                 register. The value of the CRS bits governs the number
conversion, the ADC result is added to the ADACC
                                                                 of right shifts. However, in Average mode, the threshold
register. The ADACC register is right-shifted by the
                                                                 comparison is performed upon CNT being greater than
value of the CRS bits in the ADCON2 register. This
                                                                 or equal to a user-defined RPT value. In this mode
right-shifted value is copied in to the ADFLTR register.
                                                                 when RPT = 2^CNT, then the final accumulated value
The Formatting mode does not affect the right-
                                                                 will be divided by number of samples, allowing for a
justification of the ACC value. Upon each sample, CNT
                                                                 threshold comparison operation on the average of all
is also incremented, incrementing the number of
                                                                 gathered samples.
samples accumulated. After each sample and
accumulation, the ACC value has a threshold


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 613
                       PIC18(L)F26/27/45/46/47/55/56/57K42
36.5.5      BURST AVERAGE MODE                                • The result of the calculation (ERR) is compared to
                                                                the upper and lower thresholds, ADUTH and
The Burst Average mode (MD = 011) acts the same as
                                                                ADLTH registers, to set the UTHR and LTHR flag
the Average mode in most respects. The one way it
                                                                bits. The threshold logic is selected by TMD[2:0]
differs is that it continuously retriggers ADC sampling
                                                                bits in the ADCON3 register. The threshold trigger
until the CNT value is greater than or equal to RPT,
                                                                option can be one of the following:
even if Continuous Sampling mode (see Section
                                                                - Never interrupt
36.5.8 “Continuous Sampling mode”) is not
                                                                - Error is less than lower threshold
enabled. This allows for a threshold comparison on the
                                                                - Error is greater than or equal to lower
average of a short burst of ADC samples.
                                                                   threshold
36.5.6      LOW-PASS FILTER MODE                                - Error is between thresholds (inclusive)
                                                                - Error is outside of thresholds
The Low-pass Filter mode (MD = 100) acts similarly to           - Error is less than or equal to upper threshold
the Average mode in how it handles samples                      - Error is greater than upper threshold
(accumulates samples until CNT value greater than or            - Always interrupt regardless of threshold test
equal to RPT, then triggers threshold comparison), but             results
instead of a simple average, it performs a low-pass             - If the threshold condition is met, the threshold
filter operation on all of the samples, reducing the effect        interrupt flag ADTIF is set.
of high-frequency noise on the average, then performs
a threshold comparison on the results. (see Table 36-2
                                                                 Note 1: The threshold         tests    are   signed
for a more detailed description of the mathematical
                                                                         operations.
operation). In this mode, the CRS bits determine the
cut-off frequency of the low-pass filter (as                           2: If ADAOV is set, a threshold interrupt is
demonstrated by Table 36-3).                                              signaled.

36.5.7      THRESHOLD COMPARISON                              36.5.8      CONTINUOUS SAMPLING MODE
At the end of each computation:                               Setting the CONT bit in the ADCON0 register
• The conversion results are latched and held                 automatically retriggers a new conversion cycle after
  stable at the end-of-conversion.                            updating the ADACC register. The GO bit remains set
• The error is calculated based on a difference               and re-triggering occurs automatically.
  calculation which is selected by the CALC[2:0]              If SOI = 1, a threshold interrupt condition will clear GO
  bits in the ADCON3 register and stored in the               and the conversions will stop.
  signed ADERRH:ADERRL register pair. If the
  value of the ADERR register overflows, the                  36.5.9      DOUBLE SAMPLE CONVERSION
  ADAOV overflow bit is set in the ADSTAT register.           Double sampling is enabled by setting the DSEN bit of
  The value can be one of the following calculations          the ADCON1 register. When this bit is set, two
  (see Register 36-4 for more details):                       conversions are required before the module will
  - The first derivative of single measurements               calculate threshold error (each conversion must still be
  - The CVD result in CVD mode                                triggered separately). The first conversion will set the
  - The current result vs. a setpoint                         MATH bit of the ADSTAT register and update ADACC,
  - The current result vs. the filtered/average               but will not calculate ERR or trigger ADTIF. When the
     result                                                   second conversion completes, the first value is
  - The first derivative of the filtered/average              transferred to PREV (depending on the setting of PSIS)
     value                                                    and the value of the second conversion is placed into
  - Filtered/average value vs. a setpoint                     ADRES. Only upon the completion of the second
                                                              conversion is ERR calculated and ADTIF triggered
                                                              (depending on the value of CALC).


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 614
                      PIC18(L)F26/27/45/46/47/55/56/57K42
36.6      Capacitive Voltage Divider (CVD)
          Features
The ADC module contains several features that allow
the user to perform a relative capacitance
measurement on any ADC channel using the internal
ADC sample and hold capacitance as a reference. This
relative capacitance measurement can be used to
implement capacitive touch or proximity sensing
applications. Figure 36-7 shows the basic block
diagram of the CVD portion of the ADC module.

FIGURE 36-7:           HARDWARE CAPACITIVE VOLTAGE DIVIDER BLOCK DIAGRAM


                                                                                                                  Rev. 10-000322C
                                                                                                                         4/16/2019


                                            VDD                                               VDD


                                                  PPOL & Precharge                                   PPOL & Precharge
                                                                       Precharge
                             ANx
                                                                                                                        ADC


      Capacitive                                  PPOL & Precharge                                   PPOL & Precharge
     Sensor Node
                                                           ANx
                                                        Multiplexer

                                                                                                               ADCAP

                                   Additional
                                    Sample
                                   Capacitors


This is an example to configure ADC for CVD                      4. Start double sample conversion by setting the
operation:                                                          GO bit.
1. Configure Port:                                               5. Wait for ADC conversion to complete by one
   1.1 Disable pin output driver (Refer to the                      of the following:
   TRISx register)                                                  • Polling the GO bit
   1.2 Configure pin as analog (Refer to the                        • Waiting for the ADC interrupt (if interrupt is
   ANSELx register)                                                 enabled)
2. Configure the ADC module:                                     6. Second ADC conversion depends on the
   2.1. Select ADC conversion clock                                 state of CONT:
   2.2. Configure voltage reference                                 6.1. If CONT = 1, both conversion will repeat
   2.3. Select ADC input channel                                    automatically form a single trigger
   2.4. Configure precharge (ADPRE) and                             6.2. If CONT = 0, each conversion must be
   acquisition (ADACQ) time period                                  triggered separately
   2.5. Select precharge polarity (PPOL bit)                     7. ADERR register contains the CVD result
   2.6. Enable Double Sampling (DSEN bit)                        8. Clear the ADC interrupt flag (if interrupt is
   2.7. Turn on ADC module                                          enabled).
3. Configure ADC interrupt (optional):                               Note 1: With global interrupts disabled (GIE = 0),
   3.1. Clear ADC interrupt flag                                             the device will wake from Sleep but will
   3.2. Enable ADC interrupt                                                 not enter an Interrupt Service Routine.
   3.3. Enable global interrupt (GIE bit)(1)


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 615
                          PIC18(L)F26/27/45/46/47/55/56/57K42
36.6.1      CVD OPERATION
A CVD operation begins with the ADC’s internal
Sample-and-Hold        capacitor     (CHOLD)      being
disconnected from the path which connects it to the
external capacitive sensor node. While disconnected,
CHOLD is precharged to VDD or discharged to VSS. The
sensor node is either discharged or charged to VSS or
VDD, respectively to the opposite level of CHOLD. When
the precharge phase is complete, the VDD/VSS bias
paths for the two nodes are disconnected and the paths
between CHOLD and the external sensor node is
reconnected, at which time the acquisition phase of the
CVD operation begins. During acquisition, a capacitive
voltage divider is formed between the precharged
CHOLD and sensor nodes, which results in a final
voltage level setting on CHOLD which is determined by
the capacitances and precharge levels of the two
nodes. After acquisition, the ADC converts the voltage
level on CHOLD. This process is then repeated with the
selected precharge levels inverted for both the CHOLD
and the sensor nodes. Figure 36-8 shows the
waveform for two inverted CVD measurements, which
is known as differential CVD measurement.

FIGURE 36-8:               DIFFERENTIAL CVD MEASUREMENT WAVEFORM
                                                                                                                                                          Rev. 10-000335B
                                                                                                                                                                 4/17/2019
                                                           Precharge Acquire                                Convert     Precharge Acquire       Convert

             VDD


                                                                                                            Note 1                              Note 1
               Voltage


                           ADC Sample and Hold Capacitor


                                                                External Capacitive Sensor


            VSS


                                                                                             First Sample                           Second Sample
                                                                                                                      Time

            Note 1:      External Capacitive Sensor voltage during the conversion phase may vary as per the configuration of the
                         corresponding pin.


 2017-2021 Microchip Technology Inc.                                                                                                               DS40001919G-page 616
                        PIC18(L)F26/27/45/46/47/55/56/57K42
36.6.2       PRECHARGE CONTROL                                 36.6.4      GUARD RING OUTPUTS
The precharge stage is an optional period of time that         Figure 36-9 shows a typical guard ring circuit. CGUARD
brings the external channel and internal sample and            represents the capacitance of the guard ring trace
hold capacitor to known voltage levels. Precharge is           placed on the PCB board. The user selects values for
enabled by writing a non-zero value to the ADPRE               RA and RB that will create a voltage profile on CGUARD,
register. This stage is initiated when an ADC                  which will match the selected acquisition channel.
conversion begins, either from setting the GO bit, a           The purpose of the guard ring is to generate a signal in
special event trigger, or a conversion restart from the        phase with the CVD sensing signal to minimize the
computation functionality. If the ADPRE register is            effects of the parasitic capacitance on sensing
cleared when an ADC conversion begins, this stage is           electrodes. It also can be used as a mutual drive for
skipped.                                                       mutual capacitive sensing. For more information about
During the precharge time, CHOLD is disconnected from          active guard and mutual drive, see Application Note
the outer portion of the sample path that leads to the         AN1478, “mTouchTM Sensing Solution Acquisition
external capacitive sensor and is connected to either          Methods Capacitive Voltage Divider” (DS01478).
VDD or VSS, depending on the value of the PPOL bit of          The ADC has two guard ring drive outputs, ADGRDA
ADCON1. At the same time, the port pin logic of the            and ADGRDB. These outputs can be routed through
selected analog channel is overridden to drive a digital       PPS controls to I/O pins                (see Section
high or low out, in order to precharge the outer portion       17.0 “Peripheral Pin Select (PPS) Module” for
of the ADC’s sample path, which includes the external          details) and the polarity of these outputs are controlled
sensor. The output polarity of this override is also           by the GPOL and IPEN bits of ADCON1.
determined by the PPOL bit of ADCON1. The amount
of time that this charging receives is controlled by the       At the start of the first precharge stage, both outputs
ADPRE register.                                                are set to match the GPOL bit of ADCON1. Once the
                                                               acquisition stage begins, ADGRDA changes polarity,
                                                               while ADGRDB remains unchanged. When performing
   Note 1: The external charging overrides the TRIS            a double sample conversion, setting the IPEN bit of
           setting of the respective I/O pin.                  ADCON1 causes both guard ring outputs to transition
          2: If there is a device attached to this pin,        to the opposite polarity of GPOL at the start of the
             Precharge may not be used.                        second precharge stage, and ADGRDA toggles again
                                                               for the second acquisition. For more information on the
36.6.3       ACQUISITION CONTROL FOR CVD                       timing of the guard ring output, refer to Figure 36-9 and
             (ADPRE > 0)                                       Figure 36-10.

The Acquisition stage allows time for the voltage on the
                                                               FIGURE 36-9:           GUARD RING CIRCUIT
internal Sample-and-Hold capacitor to charge or
discharge from the selected analog channel. This
acquisition time is controlled by the ADACQ register.
                                                                   ADGRDA
The acquisition stage begins when precharge stage
ends.                                                                                          RA

At the start of the acquisition stage, the port pin logic of
the selected analog channel is overridden to turn off the
digital high/low output drivers so they do not affect the
final result of the charge averaging. Also, the selected                                       RB           CGUARD
ADC channel is connected to CHOLD. This allows
charge averaging to proceed between the precharged                 ADGRDB
channel and the CHOLD capacitor.

  Note:      When PRE > 0, acquisition time cannot be
             ‘0’. In this case, setting ADACQ to ‘0’ will
             set a maximum acquisition time (8191
             ADC clock cycles). When precharge is
             disabled, setting ADACQ to ‘0’ will disable
             hardware acquisition time control.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 617
                                          PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 36-10:                                        DIFFERENTIAL CVD WITH GUARD RING OUTPUT WAVEFORM

                                                                                                                                                           Rev. 10-000336B
                           Precharge Acquire                                                      Convert     Precharge Acquire       Convert                     4/17/2019


         VDD


                                                                                                  Note 1                                  Note 1
               Voltage


                                                      External Capacitive Sensor
                            Guard Ring Capacitance


         VSS


                                                                                   First Sample                           Second Sample

                                                                                                            Time


         ADGRDA


         ADGRDB


         Note 1:         External Capacitive Sensor voltage during the conversion phase may vary as per the configuration of the
                         corresponding pin.


36.6.5      ADDITIONAL SAMPLE AND HOLD
            CAPACITANCE
Additional capacitance can be added in parallel with the
internal sample and hold capacitor (CHOLD) by using
the ADCAP register. This register selects a digitally
programmable capacitance which is added to the ADC
conversion bus, increasing the effective internal
capacitance of the sample and hold capacitor in the
ADC module. This is used to improve the match
between internal and external capacitance for a better
sensing performance. The additional capacitance does
not affect analog performance of the ADC because it is
not connected during conversion. See Figure 36-6.


 2017-2021 Microchip Technology Inc.                                                                                                              DS40001919G-page 618
                        PIC18(L)F26/27/45/46/47/55/56/57K42
36.7     Register Definitions: ADC Control
REGISTER 36-1:           ADCON0: ADC CONTROL REGISTER 0
   R/W-0/0           R/W-0/0          U-0           R/W-0/0         U-0          R/W-0/0          U-0          R/W/HS/
                                                                                                               HC-0/0
        ON           CONT                —              CS           —             FM               —            GO
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared          HC = Bit is cleared by hardware
                                                               HS = Bit is set by hardware


bit 7              ON: ADC Enable bit
                   1 = ADC is enabled
                   0 = ADC is disabled
bit 6              CONT: ADC Continuous Operation Enable bit
                   1 = GO is retriggered upon completion of each conversion trigger until ADTIF is set (if SOI is set) or
                          until GO is cleared (regardless of the value of SOI)
                   0 = ADC is cleared upon completion of each conversion trigger
bit 5              Unimplemented: Read as ‘0’
bit 4              CS: ADC Clock Selection bit
                   1 = Clock supplied from ADCRC dedicated oscillator
                   0 = Clock supplied by FOSC, divided according to ADCLK register
bit 3              Unimplemented: Read as ‘0’
bit 2              FM: ADC results Format/alignment Selection
                   1 = ADRES and PREV data are right-justified
                   0 = ADRES and PREV data are left-justified, zero-filled
bit 1              Unimplemented: Read as ‘0’
bit 0              GO: ADC Conversion Status bit(1,2)
                   1 = ADC conversion cycle in progress. Setting this bit starts an ADC conversion cycle. The bit is
                       cleared by hardware as determined by the CONT bit
                   0 = ADC conversion completed/not in progress
Note 1:      This bit requires ON bit to be set.
     2:      If cleared by software while a conversion is in progress, the results of the conversion up to this point will
             be transfered to ADRES and the state machine will be reset, but the ADIF interrupt flag bit will not be set;
             filter and threshold operations will not be performed.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 619
                        PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 36-2:           ADCON1: ADC CONTROL REGISTER 1
   R/W-0/0           R/W-0/0        R/W-0/0              U-0           U-0           U-0            U-0          R/W-0/0
    PPOL               IPEN             GPOL             —              —             —                 —         DSEN
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              PPOL: Precharge Polarity bit
                   If ADPRE != 0x00:

                                                               Action During 1st Precharge Stage
                      PPOL
                                  External (selected analog I/O pin)              Internal (AD sampling capacitor)
                         1                  Connected to VDD                           CHOLD connected to VSS
                         0                  Connected to VSS                          CHOLD connected to VDD

                   Otherwise:
                   The bit is ignored
bit 6              IPEN: A/D Inverted Precharge Enable bit
                   If DSEN = 1
                   1 = The precharge and guard signals in the second conversion cycle are the opposite polarity of the
                        first cycle
                   0 = Both Conversion cycles use the precharge and guards specified by PPOL and GPOL
                   Otherwise:
                   The bit is ignored
bit 5              GPOL: Guard Ring Polarity Selection bit
                   1 = ADC guard Ring outputs start as digital high during Precharge stage
                   0 = ADC guard Ring outputs start as digital low during Precharge stage
bit 4-1            Unimplemented: Read as ‘0’
bit 0              DSEN: Double-sample enable bit
                   1 = Two conversions are performed on each trigger. Data from the first conversion appears in PREV
                   0 = One conversion is performed for each trigger


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 620
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-3:           ADCON2: ADC CONTROL REGISTER 2
   R/W-0/0            R/W-0/0       R/W-0/0          R/W-0/0    R/W/HC-0       R/W-0/0        R/W-0/0        R/W-0/0
     PSIS                          CRS[2:0]                      ACLR                         MD[2:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         HC = Bit is cleared by hardware


bit 7              PSIS: ADC Previous Sample Input Select bits
                   1 = PREV is the FLTR value at start-of-conversion
                   0 = PREV is the RES value at start-of-conversion
bit 6-4            CRS[2:0]: ADC Accumulated Calculation Right Shift Select bits
                   If MD = 100:
                   Low-pass filter time constant is 2CRS, filter gain is 1:1
                   If MD = 001, 010 or 011:
                   The accumulated value is right-shifted by CRS (divided by 2CRS)(1,2)
                   Otherwise:
                   Bits are ignored
bit 3              ACLR: A/D Accumulator Clear Command bit(3)
                   1 = ACC, ADAOV and CNT registers are cleared
                   0 = Clearing action is complete (or not started)
bit 2-0            MD[2:0]: ADC Operating Mode Selection bits(4)
                   111-101 = Reserved
                   100 = Low-pass Filter mode
                   011 = Burst Average mode
                   010 = Average mode
                   001 = Accumulate mode
                   000 = Basic mode
Note 1:        To correctly calculate an average, the number of samples (set in RPT) must be 2CRS.
     2:        CRS = 0b111 is a reserved option.
     3:        This bit is cleared by hardware when the accumulator operation is complete; depending on oscillator
               selections, the delay may be many instructions.
          4:   See Table 36-2 for Full mode descriptions.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 621
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-4:           ADCON3: ADC CONTROL REGISTER 3
        U-0          R/W-0/0        R/W-0/0          R/W-0/0     R/W/HC-0            R/W-0/0      R/W-0/0          R/W-0/0
        —                          CALC[2:0]                        SOI                          TMD[2:0]
bit 7                                                                                                                       bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared          HC = Bit is cleared by hardware


bit 7              Unimplemented: Read as ‘0’
bit 6-4            CALC[2:0]: ADC Error Calculation Mode Select bits

                                       DSEN = 0 Single-        DSEN = 1 CVD Double-
                       CALC                                                                             Application
                                        Sample Mode               Sample Mode(1)
                         111                Reserved                      Reserved             Reserved
                         110                Reserved                      Reserved             Reserved
                         101              FLTR-STPT                   FLTR-STPT                Average/filtered value vs.
                                                                                               setpoint
                         100              PREV-FLTR                   PREV-FLTR                First derivative of filtered
                                                                                               value(3) (negative)
                         011                Reserved                      Reserved             Reserved
                         010               RES-FLTR               (RES-PREV)-FLTR              Actual result vs. averaged/
                                                                                               filtered value
                         001               RES-STPT               (RES-PREV)-STPT              Actual result vs.setpoint
                         000              RES-PREV                    RES-PREV                 First derivative of single
                                                                                               measurement(2)
                                                                                               Actual CVD result in CVD
                                                                                               mode(2)
bit 3              SOI: ADC Stop-on-Interrupt bit
                   If CONT = 1:
                   1 = GO is cleared when the threshold conditions are met, otherwise the conversion is retriggered
                   0 = GO is not cleared by hardware, must be cleared by software to stop retriggers
bit 2-0            TMD[2:0]: Threshold Interrupt Mode Select bits
                   111 = Interrupt regardless of threshold test results
                   110 = Interrupt if ERR>UTH
                   101 = Interrupt if ERRUTH
                   100 = Interrupt if ERRLTH or ERR>UTH
                   011 = Interrupt if ERR>LTH and ERR<UTH
                   010 = Interrupt if ERR≥LTH
                   001 = Interrupt if ERR<LTH
                   000 = Never interrupt

Note 1:       When PSIS = 0, the value of (RES-PREV) is the value of (S2-S1) from Table 36-2.
     2:       When PSIS = 0
     3:       When PSIS = 1.


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 622
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-5:          ADSTAT: ADC STATUS REGISTER
     R-0/0            R-0/0         R-0/0        R/W/HC-0/0       U-0          R-0/0          R-0/0        R-0/0
   ADAOV              UTHR          LTHR               MATH        —                       STAT[2:0]
bit 7                                                                                                           bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared          HS/HC = Bit is set/cleared by hardware


bit 7              ADAOV: ADC Accumulator Overflow bit
                   1 = ADACC or ADFLTR or ADERR registers have overflowed
                   0 = ADACC, ADFLTR and ADERR registers have not overflowed
bit 6              UTHR: ADC Module Greater-than Upper Threshold Flag bit
                   1 = ERR >UTH
                   0 = ERR UTH
bit 5              LTHR: ADC Module Less-than Lower Threshold Flag bit
                   1 = ERR < LTH
                   0 = ERR ≥ LTH
bit 4              MATH: ADC Module Computation Status bit(1)
                   1 = Registers ADACC, ADFLTR, ADUTH, ADLTH and the ADAOV bit are updating or have already
                       updated
                   0 = Associated registers/bits have not changed since this bit was last cleared
bit 3              Unimplemented: Read as ‘0’
bit 2-0            STAT[2:0]: ADC Module Cycle Multistage Status bits
                   111 = ADC module is in 2nd conversion stage
                   110 = ADC module is in 2nd acquisition stage
                   101 = ADC module is in 2nd precharge stage
                   100 = ADC computation is suspended between 1st and 2nd sample; the computation results are
                          incomplete and awaiting data from the 2nd sample(2, 3)
                   011 = ADC module is in 1st conversion stage
                   010 = ADC module is in 1st acquisition stage
                   001 = ADC module is in 1st precharge stage
                   000 = ADC module is not converting

Note 1:      MATH bit cannot be cleared by software while STAT = 0b100.
     2:      If the selected clock is ADCRC and FOSC < ADCRC, this reading may be invalid.
     3:      STAT = 0b100 appears between the two triggers when DSEN = 1 and CONT = 0.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 623
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-6:           ADCLK: ADC CLOCK SELECTION REGISTER
        U-0            U-0         R/W-0/0          R/W-0/0      R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
        —               —                                                CS[5:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            CS[5:0]: ADC Clock Divider Select bits
                   111111 = FOSC/128
                   111110 = FOSC/126
                   111101 = FOSC/124
                   
                   
                   
                   000000 = FOSC/2


  Note:       ADC clock divider is only available if FOSC is selected as the ADC clock source (ADCON0.CS = 0).


REGISTER 36-7:           ADREF: ADC REFERENCE SELECTION REGISTER
        U-0            U-0            U-0           R/W-0/0        U-0             U-0        R/W-0/0        R/W-0/0
        —               —               —               NREF        —              —                  PREF[1:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-5            Unimplemented: Read as ‘0’
bit 4              NREF: ADC Negative Voltage Reference Selection bit
                   1 = VREF- is connected to external VREF-
                   0 = VREF- is connected to VSS
bit 3-2            Unimplemented: Read as ‘0’
bit 1-0            PREF: ADC Positive Voltage Reference Selection bits
                   11 = VREF+ is connected to internal Fixed Voltage Reference (FVR) module
                   10 = VREF+ is connected to external VREF+
                   01 = Reserved
                   00 = VREF+ is connected to VDD


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 624
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-8:            ADPCH: ADC POSITIVE CHANNEL SELECTION REGISTER
        U-0             U-0          R/W-0/0             R/W-0/0     R/W-0/0         R/W-0/0            R/W-0/0      R/W-0/0
          —              —                                                   PCH[5:0]
bit 7                                                                                                                      bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            PCH[5:0]: ADC Positive Input Channel Selection bits

                       111111 = FVR buffer 2(2)                            010111 = ANC7
                       111110 = FVR buffer 1(2)                            010110 = ANC6
                       111101 = DAC1 output(1)                             010101 = ANC5
                       111100 = Temperature indicator(3)                   010100 = ANC4
                       111011 = VSS (Analog Ground)                        010011 = ANC3
                       111010 = Reserved. No channel connected.            010010 = ANC2
                                                                          010001 = ANC1
                                                                          010000 = ANC0
                                                                          001111 = ANB7
                       110000 = Reserved. No channel connected.            001110 = ANB6
                                                                           001101 = ANB5
                       101111 = ANF7(4)                                    001100 = ANB4
                       101110 = ANF6(4)                                    001011 = ANB3
                       101101 = ANF5(4)                                    001010 = ANB2
                                                                           001001 = ANB1
                       101100 = ANF4(4)                                    001000 = ANB0
                       101011 = ANF3(4)                                    000111 = ANA7
                       101010 = ANF2(4)                                    000110 = ANA6
                                                                           000101 = ANA5
                       101001 = ANF1(4)                                    000100 = ANA4
                       101000 = ANF0(4)                                    000011 = ANA3
                       100111 = Reserved. No channel connected.            000010 = ANA2
                       •                                                   000001 = ANA1
                                                                           000000 = ANA0
                       •
                       100011 = Reserved. No channel connected.
                       100010 = ANE2(5)
                       100001 = ANE1(5)
                       100000 = ANE0(5)
                       011111 = AND7(5)
                       011110 = AND6(5)
                       011101 = AND5(5)
                       011100 = AND4(5)
                       011011 = AND3(5)
                       011010 = AND2(5)
                       011001 = AND1(5)
                       011000 = AND0(5)
Note 1:       See Section 37.0 “5-Bit Digital-to-Analog Converter (DAC) Module” for more information.
     2:       See Section 34.0 “Fixed Voltage Reference (FVR)” for more information.
     3:       See Section 35.0 “Temperature Indicator Module” for more information.
     4:       Reserved on PIC18(L)F26/27/45/46/47K42 parts.
     5:       Reserved on PIC18(L)F26K42 parts.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 625
                           PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-9:              ADPREL: ADC PRECHARGE TIME CONTROL REGISTER (LOW BYTE)
   R/W-0/0               R/W-0/0     R/W-0/0          R/W-0/0         R/W-0/0     R/W-0/0        R/W-0/0        R/W-0/0
                                                           PRE[7:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                   W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-0             PRE[7:0]: Precharge Time Select bits
                    See Table 36-4.


REGISTER 36-10: ADPREH: ADC PRECHARGE TIME CONTROL REGISTER (HIGH BYTE)
        U-0               U-0           U-0           R/W-0/0         R/W-0/0     R/W-0/0        R/W-0/0        R/W-0/0
        —                  —             —                                       PRE[12:8]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                   W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-5             Unimplemented: Read as ‘0’
bit 4-0             PRE[12:8]: Precharge Time Select bits
                    See Table 36-4.


TABLE 36-4:              PRECHARGE TIME
                                                                          Precharge time
              ADPRE
                                                      CS! = ADCRC                              CS = ADCRC

        1 1111 1111 1111                          8191 clocks of FOSC                      8191 clocks of ADCRC
        1 1111 1111 1110                          8190 clocks of FOSC                      8190 clocks of ADCRC
        1 1111 1111 1101                          8189 clocks of FOSC                      8189 clocks of ADCRC
                   ...                                    ...                                         ...
        0 0000 0000 0010                            2 clocks of FOSC                         2 clocks of ADCRC
        0 0000 0000 0001                            1 clock of FOSC                          1 clock of ADCRC
        0 0000 0000 0000                                    Not included in the data conversion cycle


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 626
                           PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-11: ADACQL: ADC ACQUISITION TIME CONTROL REGISTER (LOW BYTE)
   R/W-0/0               R/W-0/0     R/W-0/0          R/W-0/0        R/W-0/0       R/W-0/0        R/W-0/0         R/W-0/0
                                                            ACQ[7:0]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                   W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-0            ACQ[7:0]: Acquisition (charge share time) Select bits
                   See Table 36-5.


REGISTER 36-12: ADACQH: ADC ACQUISITION TIME CONTROL REGISTER (HIGH BYTE)
        U-0               U-0           U-0           R/W-0/0        R/W-0/0       R/W-0/0        R/W-0/0         R/W-0/0
        —                  —             —                                        ACQ[12:8]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                   W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            ACQ[12:8]: Acquisition (charge share time) Select bits
                   See Table 36-5.


TABLE 36-5:          ACQUISITION TIME
                                                                          Acquisition time
               ADACQ
                                                      ADCS! = ADCRC                            ADCS = ADCRC

        1 1111 1111 1111                           8191 clocks of FOSC                       8191 clocks of ADCRC
        1 1111 1111 1110                           8190 clocks of FOSC                       8190 clocks of ADCRC
        1 1111 1111 1101                           8189 clocks of FOSC                       8189 clocks of ADCRC
                   ...                                       ...                                        ...
        0 0000 0000 0010                              2 clocks of FOSC                        2 clocks of ADCRC
        0 0000 0000 0001                              1 clock of FOSC                          1 clock of ADCRC
        0 0000 0000 0000                                    Not included in the data conversion cycle(1)
Note 1:       If ADPRE is not equal to ‘0’, then ADACQ = 0 means Acquisition time is 8192 clocks of FOSC or ADCRC.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 627
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-13: ADCAP: ADC ADDITIONAL SAMPLE CAPACITOR SELECTION REGISTER
        U-0            U-0            U-0           R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
        —               —               —                                     CAP[4:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            CAP[4:0]: ADC Additional Sample Capacitor Selection bits
                   11111 = 31 pF
                   11110 = 30 pF
                   11101 = 29 pF
                   
                   
                   
                   00011 = 3 pF
                   00010 = 2 pF
                   00001 = 1 pF
                   00000 = No additional capacitance


REGISTER 36-14: ADRPT: ADC REPEAT SETTING REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                         RPT[7:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            RPT[7:0]: ADC Repeat Threshold bits
                   Determines the number of times that the ADC is triggered before the threshold is checked when the
                   computation is Low-pass Filter, Burst Average, or Average modes. See Table 36-2 for more details.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 628
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-15: ADCNT: ADC REPEAT COUNTER REGISTER
   R/W-x/u           R/W-x/u       R/W-x/u          R/W-x/u          R/W-x/u       R/W-x/u       R/W-x/u         R/W-x/u
                                                              CNT[7:0]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            CNT[7:0]: ADC Repeat Count bits
                   Counts the number of times that the ADC has been triggered and is used along with CNT to determine
                   when the error threshold is checked when the computation is Low-pass Filter, Burst Average, or
                   Average modes. See Table Table 36-2 for more details.


REGISTER 36-16: ADFLTRH: ADC FILTER HIGH BYTE REGISTER
        R-x            R-x            R-x               R-x               R-x        R-x            R-x            R-x
                                                          FLTR[15:8]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            FLTR[15:8]: ADC Filter Output Most Significant bits — Signed 2’s Complement
                   In Accumulate, Average, and Burst Average mode, this is equal to ACC right shifted by the CRS bits
                   of ADCON2. In LPF mode, this is the output of the Low-pass Filter.


REGISTER 36-17: ADFLTRL: ADC FILTER LOW BYTE REGISTER
        R-x            R-x            R-x               R-x               R-x        R-x            R-x            R-x
                                                              FLTR[7:0]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            FLTR[7:0]: ADC Filter Output Least Significant bits — Signed 2’s Complement
                   In Accumulate, Average, and Burst Average mode, this is equal to ACC right shifted by the CRS bits
                   of ADCON2. In LPF mode, this is the output of the Low-pass Filter.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 629
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-18: ADRESH: ADC RESULT REGISTER HIGH, FM = 0
   R/W-x/u           R/W-x/u        R/W-x/u          R/W-x/u         R/W-x/u       R/W-x/u       R/W-x/u         R/W-x/u
                                                          RES[11:4]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            RES[11:4]: ADC Result Register bits
                   Upper eight bits of 12-bit conversion result.


REGISTER 36-19: ADRESL: ADC RESULT REGISTER LOW, FM = 0
   R/W-x/u           R/W-x/u        R/W-x/u          R/W-x/u           U-0           U-0            U-0            U-0
                            RES[3:0]                                    —             —             —               —
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-4            RES[3:0]: ADC Result Register bits. Lower four bits of 12-bit conversion result.
bit 3-0            Reserved


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 630
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-20: ADRESH: ADC RESULT REGISTER HIGH, FM = 1
        U-0            U-0            U-0               U-0          R/W-x/u       R/W-x/u       R/W-x/u         R/W-x/u
        —               —               —               —                                RES[11:8]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-4            Reserved
bit 3-0            RES[11:8]: ADC Sample Result bits. Upper four bits of 12-bit conversion result.

REGISTER 36-21: ADRESL: ADC RESULT REGISTER LOW, FM = 1
   R/W-x/u           R/W-x/u        R/W-x/u         R/W-x/u          R/W-x/u       R/W-x/u       R/W-x/u         R/W-x/u
                                                              RES[7:0]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            RES[7:0]: ADC Result Register bits. Lower eight bits of 12-bit conversion result.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 631
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-22: ADPREVH: ADC PREVIOUS RESULT REGISTER
        R-x            R-x            R-x               R-x           R-x          R-x           R-x            R-x
                                                          PREV[15:8]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            PREV[15:8]: Previous ADC Results bits
                   If PSIS = 1:
                   Upper byte of FLTR at the start of current ADC conversion
                   If PSIS = 0:
                   Upper bits of ADRES at the start of current ADC conversion(1)

Note 1:       If PSIS = 0, ADPREVH and ADPREVL are formatted the same way as ADRES is, depending on the FM
              bit.

REGISTER 36-23: ADPREVL: ADC PREVIOUS RESULT REGISTER
        R-x            R-x            R-x               R-x           R-x          R-x           R-x            R-x
                                                          PREV[7:0]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            PREV[7:0]: Previous ADC Results bits
                   If PSIS = 1:
                   Lower byte of FLTR at the start of current ADC conversion
                   If PSIS = 0:
                   Lower bits of ADRES at the start of current ADC conversion(1)

Note 1:       If PSIS = 0, ADPREVH and ADPREVL are formatted the same way as ADRES is, depending on the FM
              bit.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 632
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-24: ADACCU: ADC ACCUMULATOR REGISTER UPPER
   R/W-x/x           R/W-x/x         R/W-x/x          R/W-x/x        R/W-x/x       R/W-x/x        R/W-x/x         R/W-x/x
     (sign)            (sign)          (sign)             (sign)      (sign)        (sign)                ACC[17:16]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                   W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-2            Six copies of sign bit (1)
bit 1-0            ACC[17:16]: ADC Accumulator MSB — Signed 2’s Complement. Upper two bits of accumulator value.
                   See Table 36-2 for more details.
   Note 1: The ADACC register is a 24-bit wide register which contains the 18-bit accumulator value and six copies
           of the sign bit.
          2: This register can only be written when GO=0.


REGISTER 36-25: ADACCH: ADC ACCUMULATOR REGISTER HIGH
   R/W-x/x           R/W-x/x         R/W-x/x          R/W-x/x        R/W-x/x       R/W-x/x        R/W-x/x         R/W-x/x
                                                              ACC[15:8]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                   W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-0            ACC[15:8]: ADC Accumulator middle bits — Signed 2’s Complement. Middle eight bits of accumulator
                   value. See Table 36-2 for more details.
   Note 1: The ADACC register is a 24-bit wide register which contains the 18-bit accumulator value and six copies
           of the sign bit.
          2: This register can only be written when GO=0.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 633
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-26: ADACCL: ADC ACCUMULATOR REGISTER LOW
   R/W-x/x           R/W-x/x       R/W-x/x         R/W-x/x     R/W-x/x       R/W-x/x        R/W-x/x        R/W-x/x
                                                        ACC[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            ACC[7:0]: ADC Accumulator LSB — Signed 2’s Complement. Lower eight bits of accumulator value.
                   See Table 36-2 for more details.
   Note 1: The ADACC register is a 24-bit wide register which contains the 18-bit accumulator value and six copies
           of the sign bit.
          2: This register can only be written when GO=0.

REGISTER 36-27: ADSTPTH: ADC THRESHOLD SETPOINT REGISTER HIGH
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                       STPT[15:8]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            STPT[15:8]: ADC Threshold Setpoint MSB — Signed 2’s Complement. Upper byte of ADC threshold
                   setpoint, depending on CALC, may be used to determine ERR, see Register 36-29 for more details.


REGISTER 36-28: ADSTPTL: ADC THRESHOLD SETPOINT REGISTER LOW
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                       STPT[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            STPT[7:0]: ADC Threshold Setpoint LSB — Signed 2’s Complement. Lower byte of ADC threshold
                   setpoint, depending on CALC, may be used to determine ERR, see Register 36-30 for more details.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 634
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-29: ADERRH: ADC SETPOINT ERROR REGISTER HIGH
        R-x            R-x            R-x               R-x               R-x        R-x            R-x            R-x
                                                          ERR[15:8]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            ERR[15:8]: ADC Setpoint Error MSB — Signed 2’s Complement. Upper byte of ADC Setpoint Error.
                   Setpoint Error calculation is determined by CALC bits of ADCON3, see Register 36-4 for more details.

REGISTER 36-30: ADERRL: ADC SETPOINT ERROR LOW BYTE REGISTER
        R-x            R-x            R-x               R-x               R-x        R-x            R-x            R-x
                                                              ERR[7:0]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            ERR[7:0]: ADC Setpoint Error LSB — Signed 2’s Complement. Lower byte of ADC Setpoint Error cal-
                   culation is determined by CALC bits of ADCON3, see Register 36-4 for more details.

REGISTER 36-31: ADLTHH: ADC LOWER THRESHOLD HIGH BYTE REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0          R/W-0/0          R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                              LTH[15:8]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            LTH[15:8]: ADC Lower Threshold MSB — Signed 2’s Complement. LTH and UTH are compared with
                   ERR to set the UTHR and LTHR bits of ADSTAT. Depending on the setting of TMD, an interrupt may
                   be triggered by the results of this comparison.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 635
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-32: ADLTHL: ADC LOWER THRESHOLD LOW BYTE REGISTER
   R/W-0/0           R/W-0/0      R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                        LTH[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            LTH[7:0]: ADC Lower Threshold LSB — Signed 2’s Complement. LTH and UTH are compared with
                   ERR to set the UTHR and LTHR bits of ADSTAT. Depending on the setting of TMD, an interrupt may
                   be triggered by the results of this comparison.

REGISTER 36-33: ADUTHH: ADC UPPER THRESHOLD HIGH BYTE REGISTER
   R/W-0/0           R/W-0/0      R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                       UTH[15:8]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            UTH[15:8]: ADC Upper Threshold MSB — Signed 2’s Complement. LTH and UTH are compared with
                   ERR to set the UTHR and LTHR bits of ADSTAT. Depending on the setting of TMD, an interrupt may
                   be triggered by the results of this comparison.

REGISTER 36-34: ADUTHL: ADC UPPER THRESHOLD LOW BYTE REGISTER
   R/W-0/0           R/W-0/0      R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                        UTH[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            UTH[7:0]: ADC Upper Threshold LSB — Signed 2’s Complement. LTH and UTH are compared with
                   ERR to set the UTHR and LTHR bits of ADSTAT. Depending on the setting of TMD, an interrupt may
                   be triggered by the results of this comparison.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 636
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-35: ADACT: ADC AUTO CONVERSION TRIGGER CONTROL REGISTER
        U-0             U-0              U-0              R/W-0/0     R/W-0/0         R/W-0/0            R/W-0/0      R/W-0/0
          —              —                —                                           ACT[4:0]
bit 7                                                                                                                       bit 0


Legend:
R = Readable bit                   W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            ACT[4:0]: Auto-Conversion Trigger Select Bits
                   11111 = Reserved, do not use
                   
                   
                   
                   11110 = Reserved, do not use
                   11101 = Software write to ADPCH
                   11100 = Reserved, do not use
                   11011 = Software read of ADRESH
                   11010 = Software read of ADERRH
                   11001 = CLC4_out
                   11000 = CLC3_out
                   10111 = CLC2_out
                   10110 = CLC1_out
                   10101 = Logical OR of all Interrupt-on-change Interrupt Flags
                   10100 = CMP2_out
                   10011 = CMP1_out
                   10010 = NCO1_out
                   10001 = PWM8_out
                   10000 = PWM7_out
                   01111 = PWM6_out
                   01110 = PWM5_out
                   01101 = CCP4_trigger
                   01100 = CCP3_trigger
                   01011 = CCP2_trigger
                   01010 = CCP1_trigger
                   01001 = SMT1_trigger
                   01000 = TMR6_postscaled
                   00111 = TMR5_overflow
                   00110 = TMR4_postscaled
                   00101 = TMR3_overflow
                   00100 = TMR2_postscaled
                   00011 = TMR1_overflow
                   00010 = TMR0_overflow
                   00001 = Pin selected by ADACTPPS
                   00000 = External Trigger Disabled


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 637
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 36-36: ADCP: ADC CHARGE PUMP CONTROL REGISTER
   R/W-0/0             U-0              U-0             U-0                U-0                  U-0                U-0           R-0/0
    CPON                  —             —               —                   —                      —                —            CPRDY
bit 7                                                                                                                                 bit 0


Legend:
R = Readable bit                 W = Writable bit                   U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                 -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared               HS= Hardware set


bit 7              CPON: Charge Pump On Control bit
                   1 = Charge Pump On when requested by the ADC
                   0 = Charge Pump Off
bit 6-1            Unimplemented: Read as ‘0’
bit 0              CPRDY: Charge Pump Ready Status bit
                   1 = Charge Pump is ready
                   0 = Charge Pump is not ready (or never started)


TABLE 36-6:         SUMMARY OF REGISTERS ASSOCIATED WITH ADC
                                                                                                                                  Register
    Name            Bit 7       Bit 6         Bit 5      Bit 4          Bit 3              Bit 2        Bit 1            Bit 0
                                                                                                                                  on Page

ADCON0               ON       CONT              —         CS                —              FM               —            GO         620
ADCON1              PPOL       IPEN           GPOL          —               —               —               —            DSEN       621
ADCON2              PSIS                    CRS[2:0]                   ACLR                            MD[2:0]                      622
ADCON3                —                   CALC[2:0]                     SOI                            TMD[2:0]                     623
ADSTAT             ADAOV       UTHR           LTHR       MATH                                   STAT[3:0]                           624
ADCLK                —           —                                               CS[5:0]                                            625
ADREF                —           —             —         NREF               —               —                   PREF[1:0]           625
ADPCH                —           —                                              PCH[5:0]                                            626
ADPREL                                                          PRE[7:0]                                                            627
ADPREH               —           —             —                                     PRE[12:8]                                      627
ADACQL                                                          ACQ[7:0]                                                            628
ADACQH               —           —             —                                     ACQ[12:8]                                      624
ADCAP                —           —             —                                      CAP[4:0]                                      629
ADRPT                                                           RPT[7:0]                                                            629
ADCNT                                                           CNT[7:0]                                                            630
ADFLTRL                                                         FLTR[7:0]                                                           630
ADFLTRH                                                       FLTR[15:8]                                                            630
ADRESL                                                          RESL[7:0]                                                         631, 632
ADRESH                                                          RESH[7:0]                                                         631, 632
ADPREVH                                                       PREV[15:8]                                                            633
ADPREVL                                                         PREV[7:0]                                                           633
ADACCH                                                          ACC[15:8]                                                           634
ADACCL                                                          ACC[7:0]                                                            635
ADACCU              (sign)     (sign)         (sign)     (sign)        (sign)          (sign)               ACC[17:16]              634
ADSTPTL                                                         STPT[7:0]                                                           635
ADSTPTH                                                       STPT[15:8]                                                            635


 2017-2021 Microchip Technology Inc.                                                                                DS40001919G-page 638
                       PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 36-6:       SUMMARY OF REGISTERS ASSOCIATED WITH ADC (CONTINUED)
                                                                                                              Register
    Name          Bit 7       Bit 6        Bit 5       Bit 4        Bit 3       Bit 2      Bit 1     Bit 0
                                                                                                              on Page
ADERRL                                                      ERR[7:0]                                            636
ADERRH                                                      ERR[15:8]                                           636
ADLTHH                                                      LTH[15:8]                                           636
ADLTHL                                                      LTH[7:0]                                            637
ADUTHH                                                      UTH[15:8]                                           637
ADUTHL                                                      UTH[7:0]                                            637
ADERRL                                                      ERR[15:8]                                           636
ADACT              —            —           —                                 ACT[5:0]                          638
ADCP             CPON           —           —           —               —        —          —       CPRDY       639
Legend:     — = unimplemented read as ‘0’. Shaded cells are not used for the ADC module.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 639
