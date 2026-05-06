40.   ADCC - Analog-to-Digital Converter with Computation Module
      The Analog-to-Digital Converter with Computation (ADCC) allows conversion of an analog input
      signal to a 12-bit binary representation of that signal. This device uses analog inputs that are
      multiplexed into a single Sample-and-Hold circuit. The output of the Sample-and-Hold is connected
      to the input of the converter. The converter generates a 12-bit binary result via successive
      approximation and stores the conversion result into the ADC result registers.
      Additionally, the following features are provided within the ADC module:
      •   Acquisition Timer
      •   Hardware Capacitive Voltage Divider (CVD) support:
           – Precharge timer
           – Adjustable Sample-and-Hold capacitor array
           – Guard ring digital output drive
      •   Automatic Repeat and Sequencing:
           – Automated double sample conversion for CVD
           – Two sets of Result registers (Current Result and Previous Result)
           – Auto-conversion trigger
           – Internal re-trigger
      •   Computation Features:
           – Averaging and low-pass filter functions
           – Reference comparison
           – 2-level threshold comparison
           – Selectable interrupts
      Figure 40-1 shows the block diagram of the ADC.
      The ADC voltage reference is software selectable to be either internally generated or externally
      supplied.
      The ADC can generate an interrupt upon completion of a conversion and upon threshold
      comparison. These interrupts can be used to wake up the device from Sleep.


--- p711 ---
       Figure 40-1. ADCC Block Diagram

                                                                           PREF

                                          FVR_buffer1           11           Positive
                                                                            Reference
                                                                10            Select
                                           VREF+ pin
                                           Reserved             01

                                                                00
                                                    VDD
                                                                           NREF
                                                     VREF - pin
                                                                     1         Negative
                                                                               Reference
                                                                     0          Select
                                                          VSS                                               CS
                          AN0
                          ANa                                             VREF-         VREF+
            External
                                                                                                                    FOSC/n Fosc
                                 .


            Channel                                                                                                                  FOS C
                          ANz                                                                              ADC            Divider
              Inputs                                                                            ADC_clk
                                                                sampled                                    Clock
                                    VSS                           input                                    Select
                                                                                                                                     ADCRC
                         Temp Indicator
             Internal     DAC1_output
            Channel                                                                                       ADC CLOCK SOURCE
                          FVR_buffer1
               Inputs
                          FVR_buffer2                                   ADC
                                                                     Sample Circuit
                                  PCH
                                  set bit ADIF

                                                             complete                                               ADC Result
                Write to bit
                                     GO/DONE
                GO/DONE
                                                                  start
                                                                                                                0 = Left Justify
                                                                                                      FM
                                                                                                                1 = Right Justify
                                                                                  Enable
                                                                                                                          16

                                                                                                             ADRESH        ADRESL
                                   Trigger Select
                        ACT
                                                                          ON
                                      . . .
                                                                                       VSS
                                  Trigger Sources


                                AUTO-CONVERSION
                                    TRIGGER


40.1   ADC Configuration
       When configuring the ADC the following functions must be considered:
       •   Port Configuration
       •   Channel Selection
       •   ADC Voltage Reference Selection
       •   ADC Conversion Clock Source
       •   Interrupt Control
       •   Result Formatting
       •   Conversion Trigger Selection


--- p712 ---
       •   ADC Acquisition Time
       •   ADC Precharge Time
       •   Additional Sample-and-Hold Capacitor
       •   Single/Double Sample Conversion
       •   Guard Ring Outputs

40.1.1 Port Configuration
       The ADC will convert the voltage level on a pin whether or not the ANSEL bit is set. When converting
       analog signals, the I/O pin will be configured for analog by setting the associated TRIS and ANSEL
       bits. Refer to the “I/O Ports” chapter for more information.


                   Important: Analog voltages on any pin that is defined as a digital input may cause the
                   input buffer to conduct excess current.


40.1.2 Channel Selection
       The ADPCH register determines which channel is connected to the Sample-and-Hold circuit for
       conversion. When switching channels, it is recommended to have some acquisition time (ADACQ
       register) before starting the next conversion. Refer to the ADC Operation section for more
       information.


                   Important: To reduce the chance of measurement error, it is recommended to discharge
                   the Sample-and-Hold capacitor when switching between ADC channels by starting a
                   conversion on a channel connected to VSS and terminating the conversion after the
                   acquisition time has elapsed. If the ADC does not have a dedicated VSS input channel,
                   the VSS selection through the DAC output channel can be used. If the DAC is in use, a free
                   input channel can be connected to VSS, and can be used in place of the DAC.


40.1.3 ADC Voltage Reference
       The PREF bits provide control of the positive voltage reference. The NREF bit provides control of the
       negative voltage reference. Refer to the ADREF register for the list of available positive and negative
       sources.

40.1.4 Conversion Clock
       The conversion clock source is selected with the CS bit. When CS = 1 the ADC clock source is an
       internal fixed-frequency clock referred to as ADCRC. When CS = 0 the ADC clock source is derived
       from FOSC.


                   Important: When CS = 0, the clock can be divided using the ADCLK register to meet the
                   ADC clock period requirements.


       The time to complete one bit conversion is defined as the TAD. Refer to Figure 40-2 for the complete
       timing details of the ADC conversion.
       For correct conversion, the appropriate TAD specification must be met. Refer to the ADC Timing
       Specifications table in the “Electrical Specifications” chapter for more details. The table below
       gives examples of appropriate ADC clock selections.


--- p713 ---
Table 40-1. ADC Clock Period (TAD) Vs. Device Operating Frequencies(1,3)
 ADC Clock                                                        ADC Clock Period (TAD) for Different Device Frequency (FOSC)
                       ADCLK
  Source                                    64 MHz             32 MHz          20 MHz           16 MHz           8 MHz             4 MHz                1 MHz
      FOSC/2         ‘b000000              31.25 ns(2)       62.5 ns(2)       100 ns(2)        125 ns(2)        250 ns(2)          500 ns               2.0 μs
      FOSC/4         ‘b000001              62.5 ns(2)        125 ns(2)        200 ns(2)        250 ns(2)         500 ns            1.0 μs               4.0 μs
      FOSC/6         ‘b000010              93.75 ns(2)       187.5 ns(2)      300 ns(2)        375 ns(2)         750 ns            1.5 μs               6.0 μs
      FOSC/8         ‘b000011               125 ns(2)        250 ns(2)        400 ns(2)         500 ns           1.0 μs            2.0 μs               8.0 μs
        ...              ...                   ...               ...              ...              ...              ...               ...                 ...
     FOSC/16         ‘b000111               250 ns(2)          500 ns           800 ns           1.0 μs          2.0 μs            4.0 μs           16.0 μs(2)
        ...              ...                   ...               ...              ...              ...              ...               ...                 ...
     FOSC/32         ‘b001111                500 ns            1.0 μs           1.6 μs           2.0 μs          4.0 μs            8.0 μs           32.0 μs(2)
        ...              ...                   ...               ...              ...              ...              ...               ...                 ...
     FOSC/64        ‘b0111111                1.0 μs            2.0 μs           3.2 μs           4.0 μs          8.0 μs           16.0 μs(3)        64.0 μs(2)
        ...              ...                   ...               ...              ...              ...              ...               ...                 ...
     FOSC/128        ‘b111111                2.0 μs            4.0 μs           6.4 μs           8.0 μs         16.0 μs(2)        32.0 μs(2)       128.0 μs(2)
     ADCRC             CS = 1              1.0-6.0 μs        1.0-6.0 μs       1.0-6.0 μs       1.0-6.0 μs       1.0-6.0 μs       1.0-6.0 μs        1.0-6.0 μs
Notes:
1.     Refer to the “Electrical Specifications” chapter to see the TAD parameter for the ADCRC source typical TAD value.
2.     These values violate the required TAD time.
3.     The ADC clock period (TAD) and total ADC conversion time can be minimized when the ADC clock is derived from the system clock
       FOSC. However, the ADCRC oscillator source must be used when conversions are to be performed with the device in Sleep mode.


                               Important:
                               • Except for the ADCRC clock source, any changes in the system clock frequency will
                                 change the ADC clock frequency, which may adversely affect the ADC result.
                               •       The internal control logic of the ADC runs off of the clock selected by the CS bit.
                                       When the CS bit is set to ‘1’ (ADC runs on ADCRC), there may be unexpected delays
                                       in operation when setting the ADC control bits.


          Figure 40-2. Analog-to-Digital Conversion Cycles

                     Precharge                  Acquisition/                                  ADC Conversion Time
                       Time                    Sharing Time
                     (TPRE) (2)                  (TACQ ) (3)


                External and Internal External and Internal
                                                                           Holding capacitor CHOLD is
                Channels are          Channels share
                                                                           disconnected from analog input (1)
                charged/discharged charge
                                                                                                                          On the following cycle: (1)
                                                                  If ADPRE = 0                                            ADRES is loaded
                If ADPRE           0        If ADACQ     0        If ADACQ = 0                                            The GO bit is cleared
                                                                                                                          The ADIF bit is set


               Set the GO bit
                 Note:
                  1. Refer to the ADC Conversion Timing Specifications table in the Electrical Specifications chapter.
                  2. Refer to the ADPRE register for more details.
                  3. Refer to the ADACQ register for more details.


--- p714 ---
40.1.5 Interrupts
        The ADC module allows for the ability to generate an interrupt upon completion of an Analog-to-
        Digital Conversion. The ADC Interrupt Flag is the ADIF bit in the PIRx register. The ADC Interrupt
        Enable is the ADIE bit in the PIEx register. The ADIF bit must be cleared by software.


                     Important:
                     1. The ADIF bit is set at the completion of every conversion, regardless of whether or not
                        the ADC interrupt is enabled.
                     2. The ADC operates during Sleep only when the ADCRC oscillator is selected.


        While the device is operating in Sleep:
        • If ADIE = 1 and GIE = 0 : An interrupt will wake up the device from Sleep. Upon waking from
          Sleep, the instructions following the SLEEP instruction is executed. Interrupt Service Routine is
          not executed.
        •   If ADIE = 1 and GIE = 1 : An interrupt will wake up the device from Sleep. Upon waking from Sleep,
            the instruction following the SLEEP instruction is always executed. Then the execution will switch
            to the Interrupt Service Routine.

40.1.6 Result Formatting
        The ADC conversion result can be supplied in two formats, left justified or right justified. The FM bit
        controls the output format as shown in Figure 40-3.

        Figure 40-3. 12-Bit ADC Conversion Result Format

                                          ADRESH                                                 ADRESL

               (FM = 0)    MSB                                                                   LSB
                           bit 7                                   bit 0      bit 7                                 bit 0


                                                       12-bit ADC Result                               Unimplemented:
                                                                                                         Read as 0


               (FM = 1)                          MSB                                                                LSB
                           bit 7                                   bit 0      bit 7                                 bit 0


                              Unimplemented:                                 12-bit ADC Result
                                Read as 0


                     Important: Writes to the ADRES register pair are always right justified regardless of the
                     selected format mode. Therefore, a data read after writing to ADRES when FM = 0 will be
                     shifted left four places.


40.2    ADC Operation
40.2.1 Starting a Conversion
        To enable the ADC module, the ON bit must be set to ‘1’. A conversion may be started by any of the
        following:
        •   Software setting the GO bit to ‘1’


--- p715 ---
        •   An external trigger (source selected by ADACT)
        •   A Continuous-mode retrigger (see the Continuous Sampling Mode section for more details)


                     Important: The GO bit will not be set in the same instruction that turns on the ADC. Refer
                     to the ADC Conversion Procedure (Basic Mode) section for more details.


40.2.2 Completion of a Conversion
        When any individual conversion is complete, the existing value in ADRES is written into ADPREV (if
        PSIS = 0) and the new conversion results appear in ADRES. When the conversion completes, the ADC
        module will:
        •   Clear the GO bit (unless the CONT bit is set)
        •   Set the ADIF Interrupt Flag bit
        •   Set the MATH bit
        •   Update ADACC
        After every conversion when DSEN = 0, or after every other conversion when DSEN = 1, the following
        events occur:
        •   ADERR is calculated
        •   ADTIF interrupt is set if ADERR calculation meets threshold comparison

40.2.3 ADC Operation During Sleep
        The ADC module can operate during Sleep. This requires the ADC clock source to be set to
        the ADCRC option. When the ADCRC oscillator source is selected, the ADC waits one additional
        instruction before starting the conversion. This allows the SLEEP instruction to be executed, which
        can reduce system noise during the conversion. If the ADC interrupt is enabled, the device will wake
        up from Sleep when the conversion completes. If the ADC interrupt is disabled, the device remains
        in Sleep and the ADC module is turned off after the conversion completes, although the ON bit
        remains set.

40.2.4 External Trigger During Sleep
        If the external trigger is received during Sleep while the ADC clock source is set to the ADCRC, the
        ADC module will perform the conversion and set the ADIF bit upon completion.
        If an external trigger is received when the ADC clock source is something other than ADCRC, the
        trigger will be recorded, but the conversion will not begin until the device exits Sleep.

40.2.5 Auto-Conversion Trigger
        The auto-conversion trigger allows periodic ADC measurements without software intervention.
        When a rising edge of the selected source occurs, the GO bit is set by hardware.
        The auto-conversion trigger source is selected with the ACT bits.
        Using the auto-conversion trigger does not ensure proper ADC timing. It is the user’s responsibility
        to ensure that the ADC timing requirements are met.

40.2.6 ADC Conversion Procedure (Basic Mode)
        This is an example procedure for using the ADC to perform an Analog-to-Digital Conversion:
        1. Configure Port:
            – Disable pin output driver (refer to the TRISx register)


--- p716 ---
     – Configure pin as analog (refer to the ANSELx register)
2. Configure the ADC module:
    – Select ADC conversion clock
     – Configure voltage reference
     – Select ADC input channel
     – Configure precharge (ADPRE) and acquisition (ADACQ) time period
     – Turn on ADC module
3. Configure ADC interrupt (optional):
    – Clear ADC interrupt flag
     – Enable ADC interrupt
     – Enable global interrupt (GIE bit)(1)
4. If ADACQ = 0, software must wait the required acquisition time(2).
5. Start conversion by setting the GO bit.
6. Wait for ADC conversion to complete by one of the following:
    – Polling the GO bit
     – Waiting for the ADC interrupt (if interrupt is enabled)
7. Read ADC Result.
8. Clear the ADC interrupt flag (if interrupt is enabled).
Notes:
1. With global interrupts disabled (GIE = 0), the device will wake from Sleep but will not enter an
   Interrupt Service Routine.
2. Refer to the ADC Acquisition Requirements section for more details.

        Example 40-1. ADC Conversion (assembly)

         ; This code block configures the ADC for polling, Vdd and Vss references,
         ; ADCRC oscillator, and AN0 input.
         ; Conversion start & polling for completion are included.

             BANKSEL ADCON1      ;
             clrf    ADCON1      ;
             clrf    ADCON2      ; Legacy mode, no filtering, ADRES->ADPREV
             clrf    ADCON3      ; no math functions
             clrf    ADREF       ; Vref = Vdd & Vss
             clrf    ADPCH       ; select RA0/AN0
             clrf    ADACQ       ; software controlled acquisition time
             clrf    ADCAP       ; default S&H capacitance
             clrf    ADRPT       ; no repeat measurements
             clrf    ADACT       ; auto-conversion disabled
             movlw   B'10010100' ; ADC On, right-justified, ADCRC clock
             movwf   ADCON0
             BANKSEL TRISA       ;
             bsf     TRISA,0     ; Set RA0 to input
             BANKSEL ANSEL       ;
             bsf     ANSEL,0     ; Set RA0 to analog
             call    SampleTime ; Acquisiton delay
             BANKSEL ADCON0
             bsf     ADCON0,GO   ; Start conversion
             btfsc   ADCON0,GO   ; Is conversion done?
             goto    $-2         ; No, test again
             BANKSEL ADRESH      ;
             movf    ADRESH,W    ; Read upper byte
             movwf   RESULTHI    ; store in GPR space
             movf    ADRESL,W    ; Read lower byte
             movwf   RESULTLO    ; Store in GPR space


--- p717 ---
               Example 40-2. ADC Conversion (C)

                /*This code block configures the ADC
                for polling, VDD and VSS references,
                ADCRC oscillator and AN0 input.
                Conversion start & polling for completion
                are included.
                  */
                     void main() {
                         //System Initialize
                         initializeSystem();

                           //Setup ADC
                           ADCON0bits.FM = 1;      //right justify
                           ADCON0bits.CS = 1;      //ADCRC Clock
                           ADPCH = 0x00;           //RA0 is Analog channel
                           TRISAbits.TRISA0 = 1;   //Set RA0 to input
                           ANSELAbits.ANSELA0 = 1; //Set RA0 to analog
                           ADACQ = 32;             //Set acquisition time
                           ADCON0bits.ON = 1;      //Turn ADC On

                      while (1) {
                          ADCON0bits.GO = 1;     //Start conversion
                          while (ADCON0bits.GO); //Wait for conversion done
                          resultHigh = ADRESH;   //Read result
                          resultLow = ADRESL;    //Read result
                      }
                 }


40.3   ADC Acquisition Requirements
       For the ADC to meet its specified accuracy, the charge holding capacitor (CHOLD) must be allowed
       to fully charge to the input channel voltage level. The analog input model is shown in Figure 40-4.
       The source impedance (RS) and the internal sampling switch (RSS) impedance directly affect the time
       required to charge the capacitor CHOLD. The sampling switch (RSS) impedance varies over the device
       voltage (VDD). The maximum recommended impedance for analog sources is 10 kΩ. As the source
       impedance is decreased, the acquisition time may be decreased. After the analog input channel
       is selected (or changed), an ADC acquisition time must be completed before the conversion can
       be started. To calculate the minimum acquisition time, Equation 40-1 may be used. This equation
       assumes an error of 1/2 LSb. The 1/2 LSb error is the maximum error allowed for the ADC to meet
       its specified resolution.

       Equation 40-1. Acquisition Time Example
       Assumptions: Temperature = 50°C; External impedance = 10 kΩ; VDD = 5.0V
       TACQ = Amplifier Settling Time + Hold Capacitor Charging Time + Temperature Coefficient
       TACQ = TAMP + TC + TCOFF

       TACQ = 2 μs + TC + Temperature − 25°C 0.05 μs/°C
       The value for TC can be approximated with the following equations:

                            1
       VAPPLIED 1 −                   = VCHOLD ; [1] VCHOLD charged to within ½ LSb
                       2n + 1 − 1
                       −TC
       VAPPLIED 1 − e RC      = VCHOLD ; [2] VCHOLD charge response to VAPPLIED

                       −TC
                                                      1
       VAPPLIED 1 − e RC      = VAPPLIED 1 −      n+1
                                                                  ; Combining [1] and [2]
                                                  2        − 1

       Note: Where n = ADC resolution in bits


--- p718 ---
Solving for TC:
TC = − CHOLD RIC + RSS + RS ln 1/8191
TC = − 28 pF 1 kΩ + 7 kΩ + 10 kΩ ln 0.0001221
TC = 4.54 μs
Therefore:
TACQ = 2 μs + 4.54 μs +      50°C − 25°C           0.05 μs/°C
TACQ = 7.79 μs


               Important:
               • The reference voltage (VREF) has no effect on the equation, since it cancels itself out.
               •   The charge holding capacitor (CHOLD) is not discharged after each conversion.
               •   The maximum recommended impedance for analog sources is 10 kΩ. This is required to
                   meet the pin leakage specification.


Figure 40-4. Analog Input Model

                                                                                         Sampling
                                        VDD
                                                                                          Switch
                          Analog
                                              VT   0.6V                             SS
                   RS    Input pin                                       RIC   1K              RSS


          VA                CPIN              VT   0.6V           ILEAKAGE(1)                             CHOLD = 28 PF
                            5 pF


                                                                  VSS                                     Ref-


       Legend: CPIN       = Input Capacitance
               ILE AKAG E = Leakage Current at the pin due to various junctions                      11
               RIC        = Interconnect Resistance                                       Sampling 109
               RS         = Source Impedance                                               Switch    8      RSS
               VA         = Analog Voltage                                                 (K )      7
               VT         = Diode Forward Voltage                                                     6
                                                                                                      5
               SS         = Sampling Switch
               RSS        = Resistance of the Sampling Switch
               CHOLD      = Sample/Hold Capacitance                                                       2 3 4 5 6
                                                                                                             VDD
       Note:                                                                                                 (V)
        1. Refer to the Electrical Specifications chapter.


--- p719 ---
       Figure 40-5. ADC Transfer Function

                                                                                                                  Rev. 30-000115B
                                                                                                                         6/27/2017


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
                                                            0.5 LSB                                 1.5 LSB

                                           REF-              Zero-Scale
                                                             Transition         Full-Scale
                                                                                Transition        REF+


40.4   ADC Charge Pump
       The ADC module has a dedicated charge pump which can be controlled through the ADCP
       register. The primary purpose of the charge pump is to supply a constant voltage to the gates
       of transistor devices in the Analog-to-Digital Converter, signal and reference input pass-gates, to
       prevent degradation of transistor performance at low operating voltage.
       The charge pump can be enabled by setting the CPON bit. Once enabled, the pump will undergo a
       start-up time to stabilize the charge pump output. Once the output stabilizes and is ready for use,
       the CPRDY bit will be set.

40.5   Computation Operation
       The ADC module hardware is equipped with post-conversion computation features. These features
       provide post-processing functions such as digital filtering/averaging and threshold comparison.
       Based on computation results, the module can be configured to take additional samples or stop
       conversions, and an interrupt may be asserted.


--- p720 ---
Figure 40-6. Computational Features Simplified Block Diagram

                                                           CALC

                                                                                          TMD
       ADRES

                      CRS
                                          ADFLTR
                                                                                                             Set
                                                          Error                       Threshold
                                                                         ADERR                            Interrupt
                    Average/                            Calculation                     Logic
                                    1                                                                       Flag
                     Filter               ADPREV
                                    0
                                          ADSTPT
                                                                                  ADUTH         ADLTH
                       PSIS


The operation of the ADC computational features is controlled by the MD bits.
The module can be operated in one of five modes:
•   Basic: This is a Legacy mode. In this mode, ADC conversion occurs on single (DSEN = 0) or double
    (DSEN = 1) samples. ADIF is set after each conversion is complete. ADTIF is set according to the
    Calculation mode.
•   Accumulate: With each trigger, the ADC conversion result is added to the accumulator and CNT
    increments. ADIF is set after each conversion. ADTIF is set according to the Calculation mode.
•   Average: With each trigger, the ADC conversion result is added to the accumulator. When the RPT
    number of samples have been accumulated, a threshold test is performed. Upon the next trigger,
    the accumulator is cleared. For the subsequent tests, additional ADRPT samples are required to
    be accumulated.
•   Burst Average: At the trigger, the accumulator is cleared. The ADC conversion results are then
    collected repetitively until ADRPT samples are accumulated and finally the threshold is tested.
•   Low-Pass Filter (LPF): With each trigger, the ADC conversion result is sent through a filter. When
    ADRPT samples have occurred, a threshold test is performed. Every trigger after that the ADC
    conversion result is sent through the filter and another threshold test is performed.
The five modes are summarized in the following table.


--- p721 ---
                                                                              Table 40-2. Computation Modes
                                                                                                                                   Register Clear
                                                                                                                                                         Value after Cycle(1) Completion                  Threshold Operations                    Value at ADTIF Interrupt
                                                                                   Mode                    rotatethispage90


                                                                                                                              MD       Event
                                                                                                                                   ADACC and CNT          ADACC                 ADCNT        Retrigger      Threshold Test       Interrupt      AOV           ADFLTR         ADCNT
                                                                                                                                                                                                                             If threshold =
                                                                              Basic                                           0      ACLR = 1           Unchanged            Unchanged         No           Every Sample                        N/A            N/A           count
                                                                                                                                                                                                                                   true
                                                                                                                                                                        If (ADCNT = 0xFF):
                                                                                                                                                    S1 + ADACC or (S2 -                                                      If threshold =    ADACC
                                                                              Accumulate                                      1      ACLR = 1                           ADCNT, otherwise:      No           Every Sample                                   ADACC/2CRS        count
                                                                                                                                                       S1) + ADACC                                                                 true       Overflow
                                                                                                                                                                             ADCNT+1
                                                                                                                                  ACLR = 1 or
                                                                                                                                                                If (ADCNT = 0xFF):
                                                                                                                                ADCNT ≥ ADRPT S1 + ADACC or (S2                                              If ADCNT ≥      If threshold =    ADACC
                                                                              Average                                         2                                 ADCNT, otherwise:              No                                                          ADACC/2CRS        count
                                                                                                                                 at GO set or   -S1) + ADACC                                                    ADRPT              true       Overflow
                                                                                                                                                                     ADCNT + 1
                                                                                                                                   retrigger
                                                                                                                                                      Each repetition:    Each repetition:
                                                                                                                                   ACLR = 1 or at                                          Repeat while
                                                                                                                                                     same as Average     same as Average                     If ADCNT ≥      If threshold =    ADACC
                                                                              Burst Average                                   3      GO set or                                               ADCNT <                                                       ADACC/2CRS ADRPT
                                                                                                                                                    End with sum of all End with ADCNT =                        ADRPT              true       Overflow
                                                                                                                                     retrigger                                                ADRPT
                                                                                                                                                         samples              ADRPT


                                                                                                                                                    S1 + ADACC-ADACC/ If (ADCNT = 0xFF):                                                                   ADACC/2CRS
                                                                                                                                                                                                             If ADCNT ≥      If threshold =    ADACC
                                                                              Low-pass Filter 4                                      ACLR = 1        2CRS or (S2 - S1) + ADCNT, otherwise:     No                                                           (Filtered        count
                                                                                                                                                                                                                ADRPT              true       Overflow
                                                                                                                                                    ADACC-ADACC/2CRS        ADCNT + 1                                                                        Value)
                                                                              Notes:    rotatethispage90
subsidiaries


                                                                              1.   When DSEN = 0, Cycle means one conversion. When DSEN = 1, Cycle means two conversions.
                                                          Data Sheet


                                                                              2.   S1 and S2 are abbreviations for Sample 1 and Sample 2, respectively. When DSEN = 0, S1 = ADRES; When DSEN = 1, S1 = ADPREV and S2 = ADRES.


                                                                                                                                                                                                                                                                                     ADCC - Analog-to-Digital Converter with Computation Module

40.5.1 Digital Filter/Average
        The digital filter/average module consists of an accumulator with data feedback options, and control
        logic to determine when threshold tests need to be applied. The accumulator can be accessed
        through the ADACC register.
        Upon each trigger event (the GO bit set or external event trigger), the ADC conversion result is added
        to or subtracted from the accumulator. If the accumulated value exceeds 2(accumulator_width)-1 = 218-1
        = 262143, the AOV overflow bit is set.
        The number of samples to be accumulated is determined by the ADRPT (ADC Repeat Setting)
        register. Each time a sample is added to the accumulator, the ADCNT register is incremented. Once
        ADRPT samples are accumulated (ADCNT = ADRPT), the accumulator may be cleared automatically
        depending on ADC Operation mode. An accumulator clear command can be issued in software by
        setting the ACLR bit. Setting the ACLR bit will also clear the AOV (Accumulator Overflow) bit, as well
        as the ADCNT register. The ACLR bit is cleared by the hardware when accumulator clearing action is
        complete.


                     Important: When ADC is operating from ADCRC, up to five ADCRC clock cycles are
                     required to execute the ADACC clearing operation.


        The CRS bits control the data shift on the accumulator result, which effectively divides the value in
        the accumulator registers. For the Accumulate mode of the digital filter, the shift provides a simple
        scaling operation. For the Average/Burst Average mode, the calculated average is only accurate
        when the number of samples agrees with the number of bits shifted. For the Low-Pass Filter mode,
        the shift is an integral part of the filter, and determines the cutoff frequency of the filter. Table 40-3
        shows the -3 dB cutoff frequency in ωT (radians) and the highest signal attenuation obtained by this
        filter at Nyquist frequency (ωT = π).

        Table 40-3. Low-Pass Filter -3 dB Cutoff Frequency
           CRS                     ωT (radians) @ -3 dB Frequency                               dB @ FNyquist=1/(2T)
            1                                   0.72                                                    -9.5
            2                                  0.284                                                   -16.9
            3                                  0.134                                                   -23.5
            4                                  0.065                                                   -29.8
            5                                  0.032                                                   -36.0
            6                                  0.016                                                   -42.0


40.5.2 Basic Mode
        Basic mode (MD = ‘b000) disables all additional computation features. In this mode, no
        accumulation occurs but threshold error comparison is performed. Double sampling, Continuous
        mode, and all CVD features are still available, but no digital filter/average calculations are
        performed.

40.5.3 Accumulate Mode
        In Accumulate mode (MD = ‘b001), after every conversion, the ADC result is added to the ADACC
        register. The ADACC register is right-shifted by the value of the CRS bits. This right-shifted value
        is copied into the ADFLTR register. The Formatting mode does not affect the right-justification of
        the ADACC or ADFLTR values. Upon each sample, ADCNT is incremented, counting the number
        of samples accumulated. After each sample and accumulation, the ADFLTR value has a threshold
        comparison performed on it (see the Threshold Comparison section) and the ADTIF interrupt may
        trigger.


--- p723 ---
40.5.4 Average Mode
       In Average mode (MD = ‘b010), the ADACC registers accumulate with each ADC sample, much as
       in Accumulate mode, and the ADCNT register increments with each sample. The ADFLTR register is
       also updated with the right-shifted value of the ADACC register. The value of the CRS bits governs
       the number of right shifts. However, in Average mode, the threshold comparison is performed upon
       ADCNT being greater than or equal to a user-defined ADRPT value. In this mode, when ADRPT
       = 2^CRS, the final accumulated value will be divided by the number of samples, allowing for a
       threshold comparison operation on the average of all gathered samples.

40.5.5 Burst Average Mode
       The Burst Average mode (MD = ‘b011) acts the same as the Average mode in most respects. The
       one way it differs is that it continuously retriggers ADC sampling until the CNT value is equal to
       ADRPT, even if Continuous Sampling mode (see the Continuous Sampling Mode section) is not
       enabled. This provides a threshold comparison on the average of a short burst of ADC samples.

40.5.6 Low-Pass Filter Mode
       The Low-Pass Filter mode (MD = ‘b100) acts similarly to the Average mode in how it handles
       samples (accumulates samples until the ADCNT value is greater than or equal to RPT, then triggers a
       threshold comparison), but instead of a simple average, it performs a low-pass filter operation on all
       of the samples, reducing the effect of high-frequency noise on the total, then performs a threshold
       comparison on the results. In this mode, the CRS bits determine the cutoff frequency of the low-pass
       filter (as demonstrated by Digital Filter/Average). Refer to the Computation Operation section for a
       more detailed description of the mathematical operation.
       For more information about Low-Pass Filter mode, refer to the following Microchip application note,
       available in the corporate website (www.microchip.com):
       • AN2749, “PIC18 12-bit ADCC in Low-Pass Filter Mode”

40.5.7 Threshold Comparison
       At the end of each computation:
       •   The conversion results are captured at the end-of-conversion.
       •   The error (ADERR) is calculated based on a difference calculation which is selected by the CALC
           bits. The value can be one of the following calculations:
            – The first derivative of single measurements
            – The CVD result when double sampling is enabled
            – The current result vs. setpoint value in the ADSTPT register
            – The current result vs. the filtered/average result
            – The first derivative of the filtered/average value
            – Filtered/average value vs. setpoint value in the ADSTPT register
       •   The result of the calculation (ADERR) is compared to the upper and lower thresholds, ADUTH and
           ADLTH registers, to set the UTHR and LTHR flag bits. The threshold logic is selected by the TMD
           bits. The threshold trigger option can be one of the following:
            – Never interrupt
            – Error is less than lower threshold
            – Error is greater than or equal to lower threshold
            – Error is between thresholds (inclusive)
            – Error is outside of thresholds
            – Error is less than or equal to upper threshold


--- p724 ---
           – Error is greater than upper threshold
           – Always interrupt regardless of threshold test results
           – If the Threshold condition is met, the threshold interrupt flag ADTIF is set.


                   Important:
                   • The threshold tests are signed operations.
                   •   If the AOV bit is set, a threshold interrupt is signaled. It is good practice for threshold
                       interrupt handlers to verify the validity of the threshold by checking AOV bit.


40.5.8 Repetition and Sampling Options
40.5.8.1 Continuous Sampling Mode
       Setting the CONT bit automatically retriggers a new conversion cycle after updating the ADACC
       register. That means the GO bit remains set to generate automatic retriggering. If SOI = 1, a
       Threshold Interrupt condition will clear GO bit and the conversion will stop.
40.5.8.2 Double Sample Conversion
       Double sampling is enabled by setting the DSEN bit. When this bit is set, two conversions are
       required before the module calculates the threshold error. Each conversion must be triggered
       separately when CONT = 0 but will repeat automatically form a single trigger when CONT = 1. The
       first conversion will set the MATH bit and update ADACC, but will not calculate ADERR or trigger
       ADTIF. When the second conversion completes, the first value is transferred to ADPREV (depending
       on the setting of PSIS) and the value of the second conversion is placed into ADRES. Only upon the
       completion of the second conversion is ADERR calculated and ADTIF triggered (depending on the
       value of CALC).

40.6   Capacitive Voltage Divider (CVD) Features
       The ADC module contains several features that allow the user to perform a relative capacitance
       measurement on any ADC channel using the internal ADC Sample-and-Hold capacitance as a
       reference. This relative capacitance measurement can be used to implement capacitive touch or
       proximity sensing applications. The following figure shows the basic block diagram of the CVD
       portion of the ADC module.


--- p725 ---
Figure 40-7. Hardware Capacitive Voltage Divider Block Diagram


                                          VDD                                             VDD


                                                PPOL & Precharge                                PPOL & Precharge
                                                                    Precharge
                           ANx
                                                                                                               ADC

    Capacitive                                  PPOL & Precharge                                PPOL & Precharge
   Sensor Node
                                                         ANx
                                                      Multiplexer


                                                                                                          ADCAP

                                 Additional
                                  Sample
                                 Capacitors


This is an example on how to configure ADC for CVD operation:
1. Configure Port:
    a. Disable pin output driver (refer to the TRISx register)
    b. Configure pin as analog (refer to the ANSELx register)
2. Configure the ADC module:
   a. Select ADC conversion clock
    b. Configure voltage reference
    c. Select ADC input channel
    d. Configure precharge (ADPRE) and acquisition (ADACQ) time period
    e. Select precharge polarity (PPOL)
    f.   Enable Double Sampling (DSEN)
    g. Turn on ADC module
3. Configure ADC interrupt (optional):
   a. Clear ADC interrupt flag
    b. Enable ADC interrupt
    c. Enable global interrupt (GIE bit)(1)
4. Start double sample conversion by setting the GO bit.
5. Wait for ADC conversion to complete by one of the following:
   a. Polling the GO bit
    b. Waiting for the ADC interrupt (if interrupt is enabled)
6. Second ADC conversion depends on the state of CONT:
   a. If CONT = 1, both conversion will repeat automatically from a single trigger
    b. If CONT = 0, each conversion must be triggered separately
7. The ADERR register contains the CVD result.


--- p726 ---
       8. Clear the ADC interrupt flag (if interrupt is enabled).
       Note:
       1. With global interrupts disabled (GIE = 0), the device will wake from Sleep but will not enter an
          Interrupt Service Routine.

40.6.1 CVD Operation
       A CVD operation begins with the ADC’s internal Sample-and-Hold capacitor (CHOLD) being
       disconnected from the path which connects it to the external capacitive sensor node. While
       disconnected, CHOLD is precharged to VDD or discharged to VSS. The sensor node is either discharged
       or charged to VSS or VDD, respectively to the opposite level of CHOLD. When the precharge phase
       is complete, the VDD/VSS bias paths for the two nodes are disconnected and the paths between
       CHOLD and the external sensor node is reconnected, at which time the acquisition phase of the CVD
       operation begins. During acquisition, a capacitive voltage divider is formed between the precharged
       CHOLD and sensor nodes, which results in a final voltage level setting on CHOLD which is determined
       by the capacitances and precharge levels of the two nodes. After acquisition, the ADC converts the
       voltage level on CHOLD. This process is then repeated with the selected precharge levels inverted for
       both the CHOLD and the sensor nodes. The waveform for two CVD measurements, which is known as
       differential CVD measurement, is shown in the following figure.

       Figure 40-8. Differential CVD Measurement Waveform

                                                               Precharge Acquire                                  Convert          Precharge Acquire      Convert

                VDD


                                                                                                                  Note 1                                   Note 1
                   Voltage


                               ADC Sample and Hold Capacitor


                                                                    External Capacitive Sensor


                VSS


                                                                                                   First Sample                                Second Sample
                                                                                                                             Time

                Note 1:      External Capacitive Sensor voltage during the conversion phase m ay vary as per the configuration of the
                             corresponding pin.


40.6.2 Precharge Control
       The Precharge stage is the period of time that brings the external channel and internal Sample-and-
       Hold capacitor to known voltage levels. Precharge is enabled by writing a nonzero value to the
       ADPRE register. This stage is initiated when an ADC conversion begins, either from setting the GO


--- p727 ---
        bit, a Special Event Trigger, or a conversion restart from the computation functionality. If the ADPRE
        register is cleared when an ADC conversion begins, this stage is skipped.
        During the precharge time, CHOLD is disconnected from the outer portion of the sample path that
        leads to the external capacitive sensor and is connected to either VDD or VSS, depending on the value
        of the PPOL bit. At the same time, the PORT pin logic of the selected analog channel is overridden
        to drive a digital high or low out, to precharge the outer portion of the ADC’s sample path, which
        includes the external sensor. The output polarity of this override is determined by the PPOL bit such
        that the external sensor cap is charged opposite of the internal CHOLD cap. The amount of time for
        precharge is controlled by the ADPRE register.


                    Important: The external charging overrides the TRIS/LAT/Guard outputs setting of the
                    respective I/O pin. If there is a device attached to this pin, precharge will not be used.


40.6.3 Acquisition Control for CVD (ADPRE > 0)
        The Acquisition stage allows time for the voltage on the internal Sample-and-Hold capacitor to
        charge or discharge from the selected analog channel. This acquisition time is controlled by the
        ADACQ register. The acquisition stage begins when precharge stage ends.
        At the start of the acquisition stage, the PORT pin logic of the selected analog channel is overridden
        to turn off the digital high/low output drivers so they do not affect the final result of the charge
        averaging. Also, the selected ADC channel is connected to CHOLD. This allows charge averaging to
        proceed between the precharged channel and the CHOLD capacitor.


                    Important: When ADPRE > 0 setting ADACQ to ‘0’ will set a maximum acquisition time.
                    When precharge is disabled, setting ADACQ to ‘0’ will disable hardware acquisition time
                    control.


40.6.4 Guard Ring Outputs
        Figure 40-9 shows a typical guard ring circuit. CGUARD represents the capacitance of the guard ring
        trace placed on the PCB. The user selects values for RA and RB that will create a voltage profile on
        CGUARD, which will match the selected acquisition channel.
        The purpose of the guard ring is to generate a signal in phase with the CVD sensing signal
        to minimize the effects of the parasitic capacitance on sensing electrodes. It also can be used
        as a mutual drive for mutual capacitive sensing. For more information about active guard and
        mutual drive, refer to the following Microchip application note, available on the corporate website
        (www.microchip.com):
        • AN1478, “mTouchTM Sensing Solution Acquisition Methods Capacitive Voltage Divider”
        The ADC has two guard ring drive outputs, ADGRDA and ADGRDB. These outputs are routed through
        PPS controls to I/O pins. Refer to the “PPS - Peripheral Pin Select Module” chapter for more
        details. The polarity of these outputs is controlled by the GPOL and IPEN bits.
        At the start of the first precharge stage, both outputs are set to match the GPOL bit. Once the
        acquisition stage begins, ADGRDA changes polarity, while ADGRDB remains unchanged. When
        performing a double sample conversion, setting the IPEN bit causes both guard ring outputs to
        transition to the opposite polarity of GPOL at the start of the second precharge stage, and ADGRDA
        toggles again for the second acquisition. For more information on the timing of the guard ring
        output, refer to Figure 40-10.


--- p728 ---
Figure 40-9. Guard Ring Circuit
                                                                                                                                 Rev. 30-000120A
                                                                                                                                        5/16/2017


                                                                                   ADGRDA
                                                                                                                RA


                                                                                                                 RB        CGUARD

                                                                                   ADGRDB


Figure 40-10. Differential CVD with Guard Ring Output Waveform

                            Precharge Acquire                                                     Convert       Precharge Acquire                   Convert
          VDD


                                                                                                  Note 1                                            Note 1
                Voltage


                                                      External Capacitive Sensor
                             Guard Ring Capacitance


          VSS


                                                                                   First Sample                             Second Sample
                                                                                                            Time


         ADGRDA


          ADGRDB


          Note 1:         External Capacitive Sensor voltage during the conversion phase m ay vary as per the configuration of the
                          corresponding pin.


--- p729 ---
40.6.5 Additional Sample-and-Hold Capacitance
       Additional capacitance can be added in parallel with the internal Sample-and-Hold capacitor (CHOLD)
       by using the ADCAP register. This register selects a digitally programmable capacitance that is added
       to the ADC conversion bus, increasing the effective internal capacitance of the Sample-and-Hold
       capacitor in the ADC module. This is used to improve the match between internal and external
       capacitance for a better sensing performance. The additional capacitance does not affect analog
       performance of the ADC because it is not connected during conversion.

40.7   Register Definitions: ADC Control
       Long bit name prefixes for the ADC peripherals are shown in the following table. Refer to the “Long
       Bit Names” section of the “Register and Bit Naming Conventions” chapter for more information.

       Table 40-4. ADC Long Bit Name Prefixes
                         Peripheral                                             Bit Name Prefix
                            ADC                                                         AD


--- p730 ---
40.7.1 ADCON0

            Name:       ADCON0
            Address:    0x3F3

            ADC Control Register 0

      Bit        7             6                5               4                3               2                1             0
                ON           CONT                               CS                              FM                             GO
  Access        R/W           R/W                              R/W                              R/W                         R/W/HC/HS
   Reset         0             0                                0                                0                              0

Bit 7 – ON ADC Enable
            Value      Description
            1          ADC is enabled
            0          ADC is disabled

Bit 6 – CONT ADC Continuous Operation Enable
            Value      Description
            1          GO is retriggered upon completion of each conversion trigger until ADTIF is set (if SOI is set) or until GO is
                       cleared (regardless of the value of SOI)
            0          ADC is cleared upon completion of each conversion trigger

Bit 4 – CS ADC Clock Selection
            Value      Description
            1          Clock supplied from ADCRC dedicated oscillator
            0          Clock supplied by FOSC, divided according to ADCLK register

Bit 2 – FM ADC Results Format/Alignment Selection
            Value      Description
            1          ADRES and ADPREV data are right justified
            0          ADRES and ADPREV data are left justified, zero-filled

Bit 0 – GO ADC Conversion Status(1,2)
            Value      Description
            1          ADC conversion cycle in progress. Setting this bit starts an ADC conversion cycle. The bit is cleared by hardware
                       as determined by the CONT bit
            0          ADC conversion completed/not in progress

            Notes:
            1. This bit requires ON bit to be set.
            2. If cleared by software while a conversion is in progress, the results of the conversion up to this
               point will be transferred to ADRES and the state machine will be reset, but the ADIF Interrupt
               Flag bit will not be set; filter and threshold operations will not be performed.


--- p731 ---
40.7.2 ADCON1

            Name:       ADCON1
            Address:    0x3F4

            ADC Control Register 1

      Bit         7             6             5                4                  3            2             1               0
                PPOL          IPEN           GPOL                                                                          DSEN
  Access        R/W           R/W            R/W                                                                           R/W
   Reset          0             0             0                                                                              0

Bit 7 – PPOL Precharge Polarity
          Action During 1st Precharge Stage
            Value      Condition        Description
            x          ADPRE = 0        Bit has no effect
            1          ADPRE > 0         External analog I/O pin is connected to VDD.
                                         Internal AD sampling capacitor (CHOLD) is connected to VSS.
            0          ADPRE > 0         External analog I/O pin is connected to VSS.
                                         Internal AD sampling capacitor (CHOLD) is connected to VDD.

Bit 6 – IPEN A/D Inverted Precharge Enable
            Value      Condition Description
            x          DSEN = 0 Bit has no effect
            1          DSEN = 1 The precharge and guard signals in the second conversion cycle are the opposite polarity of the first
                                cycle
            0          DSEN = 1 Both conversion cycles use the precharge and guards specified by PPOL and GPOL


Bit 5 – GPOL Guard Ring Polarity Selection
            Value      Description
            1          ADC guard Ring outputs start as digital high during Precharge stage
            0          ADC guard Ring outputs start as digital low during Precharge stage

Bit 0 – DSEN Double-Sample Enable
            Value      Description
            1          Two conversions are processed as a pair. The selected computation is performed after every second
                       conversion.
            0          Selected computation is performed after every conversion


--- p732 ---
40.7.3 ADCON2

            Name:       ADCON2
            Address:    0x3F5

            ADC Control Register 2

      Bit        7             6              5                4                3                 2                1            0
                PSIS                       CRS[2:0]                           ACLR                               MD[2:0]
  Access        R/W           R/W            R/W             R/W             R/W/HC             R/W               R/W         R/W
   Reset         0             0              0               0                 0                0                 0           0

Bit 7 – PSIS ADC Previous Sample Input Select
            Value      Description
            1          ADFLTR is transferred to ADPREV at start-of-conversion
            0          ADRES is transferred to ADPREV at start-of-conversion

Bits 6:4 – CRS[2:0] ADC Accumulated Calculation Right Shift Select
            Value      Condition                  Description
            1 to 6     MD =‘b100                  Low-pass filter time constant is 2CRS, filter gain is 1:1(2)
            1 to 6     MD =‘b011 to ‘b001          The accumulated value is right-shifted by CRS (divided by 2CRS)(1,2)
            x          MD =‘b000                   These bits are ignored


Bit 3 – ACLR A/D Accumulator Clear Command(3)
            Value      Description
            1          The ADACC and ADCNT registers and the AOV bit are cleared
            0          Clearing action is complete (or not started)

Bits 2:0 – MD[2:0] ADC Operating Mode Selection(4)
            Value      Description
            111-101    Reserved
            100        Low-Pass Filter mode
            011        Burst Average mode
            010        Average mode
            001        Accumulate mode
            000        Basic (Legacy) mode

            Notes:
            1. To correctly calculate an average, the number of samples (set in ADRPT) must be 2CRS.
            2. CRS = ‘b111 and ‘b000 are reserved.
            3. This bit is cleared by hardware when the accumulator operation is complete; depending on
               oscillator selections, the delay may be many instructions.
            4. See the Computation Operation section for full mode descriptions.


--- p733 ---
40.7.4 ADCON3

            Name:          ADCON3
            Address:       0x3F6

            ADC Control Register 3

      Bit           7              6            5                4                3               2           1               0
                                             CALC[2:0]                           SOI                       TMD[2:0]
  Access                         R/W           R/W              R/W            R/W/HC          R/W           R/W            R/W
   Reset                          0             0                0                0             0             0              0

Bits 6:4 – CALC[2:0] ADC Error Calculation Mode Select
                                                  ADERR
            CALC        DSEN = 0 Single-Sample       DSEN = 1 CVD Double-Sample                          Application
                                Mode                            Mode(1)
            111               Reserved                         Reserved                                    Reserved
            110               Reserved                         Reserved                                    Reserved
            101            ADFLTR-ADSTPT                   ADFLTR-ADSTPT                     Average/filtered value vs. setpoint
                                                                                              First derivative of filtered value(3)
            100            ADPREV-ADFLTR                     ADPREV-ADFLTR
                                                                                                           (negative)
            011               Reserved                           Reserved                                  Reserved
            010             ADRES-ADFLTR                  (ADRES-ADPREV)-ADFLTR            Actual result vs. averaged/filtered value
            001             ADRES-ADSTPT                  (ADRES-ADPREV)-ADSTPT                    Actual result vs. setpoint
                                                                                          First derivative of single measurement(2)
            000             ADRES-ADPREV                      ADRES-ADPREV
                                                                                                      Actual CVD result(2)
            Notes:
            1.   When DSEN = 1 and PSIS = 0, ADERR is computed only after every second sample.
            2.   When PSIS = 0.
            3.   When PSIS = 1.


Bit 3 – SOI ADC Stop-on-Interrupt
            Value         Condition Description
            x             CONT = 0 This bit is not used
            1              CONT = 1 GO is cleared when the threshold conditions are met, otherwise the conversion is retriggered
            0              CONT = 1 GO is not cleared by hardware, must be cleared by software to stop retriggers


Bits 2:0 – TMD[2:0] Threshold Interrupt Mode Select
            Value         Description
            111           Interrupt regardless of threshold test results
            110           Interrupt if ADERR > ADUTH
            101           Interrupt if ADERR ≤ ADUTH
            100           Interrupt if ADERR < ADLTH or ADERR > ADUTH
            011           Interrupt if ADERR > ADLTH and ADERR < ADUTH
            010           Interrupt if ADERR ≥ ADLTH
            001           Interrupt if ADERR < ADLTH
            000           Never interrupt


--- p734 ---
40.7.5 ADSTAT

            Name:        ADSTAT
            Address:     0x3F7

            ADC Status Register

      Bit        7             6              5              4               3                2         1               0
                AOV          UTHR           LTHR          MATH                                       STAT[2:0]
  Access     R/C/HS/HC         R              R           R/C/HS                              R         R               R
   Reset         0             0              0              0                                0         0               0

Bit 7 – AOV ADC Accumulator Overflow
            Value      Description
            1          The ADACC or ADFLTR or ADERR registers have overflowed
            0          The ADACC, ADFLTR and ADERR registers have not overflowed

Bit 6 – UTHR ADC Module Greater-than Upper Threshold Flag
            Value      Description
            1          ADERR > ADUTH
            0          ADERR ≤ ADUTH

Bit 5 – LTHR ADC Module Less-than Lower Threshold Flag
            Value      Description
            1          ADERR < ADLTH
            0          ADERR ≥ ADLTH

Bit 4 – MATH ADC Module Computation Status
         ADC Module Computation Status(1)
            Value      Description
            1          The ADACC, ADFLTR, ADUTH and ADLTH registers and the AOV bit are updating or have already updated
            0          Associated registers/bits have not changed since this bit was last cleared

Bits 2:0 – STAT[2:0] ADC Module Cycle Multi-Stage Status
            Value      Description
            111        ADC module is in 2nd conversion stage
            110        ADC module is in 2nd acquisition stage
            101        ADC module is in 2nd precharge stage
            100        ADC computation is suspended between 1st and 2nd sample; the computation results are incomplete and
                       awaiting data from the 2nd sample(2,3)
            011        ADC module is in 1st conversion stage
            010        ADC module is in 1st acquisition stage
            001        ADC module is in 1st precharge stage
            000        ADC module is not converting

            Notes:
            1. MATH bit cannot be cleared by software while STAT = ‘b100.
            2. If ADC clock source is ADCRC, and FOSC < ADCRC, the indicated status may not be valid.
            3. STAT = ‘b100 appears between the two triggers when DSEN = 1 and CONT = 0.


--- p735 ---
40.7.6 ADCLK

            Name:        ADCLK
            Address:     0x3FA

            ADC Clock divider Register

      Bit           7           6              5                4                   3               2         1              0
                                                                                         CS[5:0]
  Access                                      R/W              R/W                 R/W             R/W       R/W           R/W
   Reset                                       0                0                   0               0         0             0

Bits 5:0 – CS[5:0] ADC Clock divider Select
            Value       Description
            n           ADC Clock frequency = FOSC/(2*(n+1))

            Note: ADC Clock divider is only available if FOSC is selected as the ADC clock source (CS = 0).


--- p736 ---
40.7.7 ADREF

            Name:        ADREF
            Address:     0x3F8

            ADC Reference Selection Register

      Bit           7            6               5              4               3                2          1                 0
                                                               NREF                                              PREF[1:0]
  Access                                                       R/W                                         R/W               R/W
   Reset                                                        0                                           0                 0

Bit 4 – NREF ADC Negative Voltage Reference Selection
            Value       Description
            1           VREF- is connected to external VREF-
            0           VREF- is connected to AVSS

Bits 1:0 – PREF[1:0] ADC Positive Voltage Reference Selection
            Value       Description
            11          VREF+ is connected to internal Fixed Voltage Reference (FVR) module
            10          VREF+ is connected to external VREF+
            01          Reserved
            00          VREF+ is connected to VDD


--- p737 ---
40.7.8 ADPCH

            Name:       ADPCH
            Address:    0x3EC

            ADC Positive Channel Selection Register

      Bit        7           6            5              4                   3            2            1              0
                                                               PCH[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset         0           0            0             0                    0          0              0             0

Bits 7:0 – PCH[7:0] ADC Positive Input Channel Selection
                               PCH                                            ADC Positive Channel Input
                       11111111 - 10010100                                 Reserved. No channel connected.
                             10010011                                               RC3 (OPA1IN1+)(6)
                       10010010 - 10010001                                 Reserved. No channel connected.
                             10010000                                              RC0 (OPA1IN0+)(5,6)
                       10001111 - 10001110                                 Reserved. No channel connected.
                             10001101                                              RB5 (OPA1IN0+)(4,6)
                       10001100 - 10000011                                 Reserved. No channel connected.
                             10000010                                               RA2 (OPA1IN2+)(6)
                             10000001                                      Reserved. No channel connected.
                             10000000                                               RA0 (OPA1IN3+)(6)
                       01111111 - 01000000                                 Reserved. No channel connected.
                             00111111                                   Fixed Voltage Reference (FVR) Buffer 2(1)
                             00111110                                   Fixed Voltage Reference (FVR) Buffer 1(1)
                             00111101                                                DAC1 output(2)
                             00111100                                           Temperature Indicator(3)
                             00111011                                             VSS (Analog Ground)
                             00111010                                                DAC2 output(2)
                             00111001                                          OPA positive input source
                       00111000 - 00011000                                 Reserved. No channel connected.
                             00010111                                                 RC7/ANC7(4)
                             00010110                                                  RC6/ANC6(4)
                             00010101                                                   RC5/ANC5
                             00010100                                                   RC4/ANC4
                             00010011                                                   RC3/ANC3
                             00010010                                                   RC2/ANC2
                             00010001                                                   RC1/ANC1
                             00010000                                                   RC0/ANC0
                             00001111                                                  RB7/ANB7(4)
                             00001110                                                  RB6/ANB6(4)
                             00001101                                                  RB5/ANB5(4)
                             00001100                                                  RB4/ANB4(4)
                       00001011 - 00000110                                   Reserved. No channel connected.
                             00000101                                                   RA5/ANA5
                             00000100                                                   RA4/ANA4
                             00000011                                                   RA3/ANA3
                             00000010                                                   RA2/ANA2


--- p738 ---
...........continued
                     PCH                                           ADC Positive Channel Input
                   00000001                                                RA1/ANA1
                   00000000                                                RA0/ANA0
Notes:
1.   Refer to the “Fixed Voltage Reference Module” chapter for more details.
2.   Refer to the “Digital-to-Analog Converter Module” chapter for more details.
3.   Refer to the “Temperature Indicator Module” chapter for more details.
4.   20-pin devices only.
5.   14-pin devices only.
6.   This configuration routes the specified analog channel to the noninverting input of the OPA module
     (OPAxIN+), and connects the output of the OPA (OPAxOUT) to the input of the ADC for conversion. The OPA
     module must be configured accordingly to use this mode of operation. Refer to the "OPA - Analog Signal
     Conditioning" chapter for more details.


--- p739 ---
40.7.9 ADPRE

            Name:        ADPRE
            Address:     0x3F1

            ADC Precharge Time Control Register

      Bit        15           14          13             12                  11           10            9              8
                                                                                       PRE[12:8]
  Access                                                R/W                  R/W         R/W           R/W           R/W
   Reset                                                 0                    0            0            0             0

      Bit        7             6           5              4                   3            2            1              0
                                                                PRE[7:0]
  Access        R/W           R/W         R/W           R/W                  R/W          R/W          R/W           R/W
   Reset         0             0           0             0                    0            0            0             0

Bits 12:0 – PRE[12:0] Precharge Time Select
                                                                                   Precharge Time
                            PRE
                                                                CS = 0                                 CS = 1
                      1 1111 1111 1111                 8191 clocks of FOSC                 8191 clocks of ADCRC
                      1 1111 1111 1110                 8190 clocks of FOSC                 8190 clocks of ADCRC
                      1 1111 1111 1101                 8189 clocks of FOSC                 8189 clocks of ADCRC
                             ...                                ...                                   ...
                      0 0000 0000 0010                  2 clocks of FOSC                     2 clocks of ADCRC
                      0 0000 0000 0001                   1 clocks of FOSC                    1 clocks of ADCRC
                      0 0000 0000 0000                          Not included in the data conversion cycle

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names:
            1. ADPREH: Accesses the high byte ADPRE[12:8].
            2. ADPREL: Accesses the low byte ADPRE[7:0].


--- p740 ---
40.7.10 ADACQ

            Name:           ADACQ
            Address:        0x3EE

            ADC Acquisition Time Control Register

      Bit         15             14           13            12                  11            10           9              8
                                                                                           ACQ[12:8]
  Access                                                   R/W                  R/W          R/W          R/W           R/W
   Reset                                                    0                    0             0           0             0

      Bit           7            6             5             4                   3             2           1              0
                                                                   ACQ[7:0]
  Access          R/W           R/W          R/W           R/W                  R/W           R/W         R/W           R/W
   Reset           0             0            0             0                    0             0           0             0

Bits 12:0 – ACQ[12:0] Acquisition (charge share time) Select
                                                                                      Acquisition Time
                              ACQ
                                                                   CS = 0                                 CS = 1
                        1 1111 1111 1111                  8191 clocks of FOSC                8191 clocks of ADCRC
                        1 1111 1111 1110                  8190 clocks of FOSC                8190 clocks of ADCRC
                        1 1111 1111 1101                  8189 clocks of FOSC                8189 clocks of ADCRC
                               ...                                ...                                   ...
                        0 0000 0000 0010                   2 clocks of FOSC                    2 clocks of ADCRC
                        0 0000 0000 0001                   1 clocks of FOSC                    1 clocks of ADCRC
                        0 0000 0000 0000                         Not included in the data conversion cycle(1)
            Note:
            1.   If ADPRE is not equal to ‘0’, then ACQ = 0 means Acquisition Time is 8192 clocks of FOSC or ADCRC.


            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names:
            • ADACQH: Accesses the high byte ADACQ[12:8]
            •    ADACQL: Accesses the low byte ADACQ[7:0]


--- p741 ---
40.7.11 ADCAP

            Name:       ADCAP
            Address:    0x3F0

            ADC Additional Sample Capacitor Selection Register

      Bit        7             6              5              4                   3          2              1              0
                                                                                         CAP[4:0]
  Access                                                    R/W                 R/W        R/W            R/W           R/W
   Reset                                                     0                   0          0              0             0

Bits 4:0 – CAP[4:0] ADC Additional Sample Capacitor Selection
            Value      Description
            1 to 31    Number of pF in the additional capacitance
            0          No additional capacitance


--- p742 ---
40.7.12 ADRPT

            Name:      ADRPT
            Address:   0x3E7

            ADC Repeat Setting Register

      Bit        7           6             5             4                   3            2            1              0
                                                               RPT[7:0]
  Access        R/W         R/W           R/W          R/W                  R/W        R/W            R/W           R/W
   Reset         0           0             0            0                    0          0              0             0

Bits 7:0 – RPT[7:0] ADC Repeat Threshold
          Determines the number of times the ADC is triggered for a threshold check. When CNT reaches this
          value, the error threshold is checked. Used when the computation mode is Low-Pass Filter, Burst
          Average, or Average. See the Computation Operation section for more details.


--- p743 ---
40.7.13 ADCNT

            Name:      ADCNT
            Address:   0x3E6

            ADC Repeat Counter Register

      Bit        7          6              5             4                   3            2            1              0
                                                               CNT[7:0]
  Access        R/W        R/W            R/W          R/W                  R/W        R/W            R/W           R/W
   Reset         0          0              0            0                    0          0              0             0

Bits 7:0 – CNT[7:0] ADC Repeat Count
          Counts the number of times the ADC is triggered before the threshold is checked. When this value
          reaches RPT, the threshold is checked. Used when the computation mode is Low-Pass Filter, Burst
          Average, or Average. See the Computation Operation section for more details.


--- p744 ---
40.7.14 ADFLTR

            Name:       ADFLTR
            Address:    0x3E1

            ADC Filter Register

      Bit         15          14          13             12                  11          10             9              8
                                                               FLTR[15:8]
  Access          R           R            R              R                  R             R            R              R
   Reset          x           x            x              x                  x             x            x              x

      Bit         7           6            5              4                  3             2            1              0
                                                               FLTR[7:0]
  Access          R           R            R              R                  R             R            R              R
   Reset          x           x            x              x                  x             x            x              x

Bits 15:0 – FLTR[15:0] ADC Filter Output - Signed Two’s Complement
         In Accumulate, Average and Burst Average modes, this is equal to ACC right shifted by the CRS bits.
         In LPF mode, this is the output of the Low-Pass Filter.

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names:
            • ADFLTRH: Accesses the high byte ADFLTR[15:8]
            •   ADFLTRL: Accesses the low byte ADFLTR[7:0]


--- p745 ---
40.7.15 ADRES

           Name:       ADRES
           Address:    0x3EA

           ADC Result Register

     Bit         15          14          13             12                  11          10             9              8
                                                              RES[15:8]
  Access        R/W         R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset         0           0            0             0                    0          0              0             0

     Bit         7           6            5              4                   3            2            1              0
                                                               RES[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset         0           0            0             0                    0          0              0             0

Bits 15:0 – RES[15:0] ADC Sample Result

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • ADRESH: Accesses the high byte ADRES[15:18]
           •   ADRESL: Accesses the low byte ADRES[7:0]


--- p746 ---
40.7.16 ADPREV

            Name:         ADPREV
            Address:      0x3E8

            ADC Previous Result Register

      Bit           15          14            13             12                  11           10            9              8
                                                                   PREV[15:8]
  Access            R               R         R               R                  R            R             R              R
   Reset            0               0         0               0                  0            0             0              0

      Bit           7               6          5              4                  3            2             1              0
                                                                   PREV[7:0]
  Access            R               R         R               R                  R            R             R              R
   Reset            0               0         0               0                  0            0             0              0

Bits 15:0 – PREV[15:0] Previous ADC Result
            Value        Condition      Description
            n            PSIS = 1       n = ADFLTR value at the start of current ADC conversion
            n            PSIS = 0       n = ADRES at the start of current ADC conversion(1)


            Notes:
            1. If PSIS = 0, ADPREV is formatted the same way as ADRES is, depending on the FM bit.
            2. The individual bytes in this multibyte register can be accessed with the following register names:
                – ADPREVH: Accesses ADPREV[15:8]
                    – ADPREVL: Accesses ADPREV[7:0]


--- p747 ---
40.7.17 ADACC

           Name:       ADACC
           Address:    0x3E3

           ADC Accumulator Register(1)
           See the Computation Operation section for more details.


                       Important: This register contains signed two’s complement accumulator value and the
                       upper unused bits contain copies of the sign bit.


     Bit        23          22           21             20                  19          18            17            16
                                                                                                         ACC[17:16]
  Access                                                                                              R/W         R/W
   Reset                                                                                               x             x

     Bit        15          14           13             12                  11          10             9              8
                                                              ACC[15:8]
  Access       R/W          R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset        x            x            x             x                    x          x              x             x

     Bit        7            6            5              4                   3            2            1              0
                                                               ACC[7:0]
  Access       R/W          R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset        x            x            x             x                    x          x              x             x

Bits 17:0 – ACC[17:0] ADC Accumulator - Signed Two’s Complement

           Notes:
           1. This register can only be written when GO = 0.
           2. The individual bytes in this multibyte register can be accessed with the following register names:
               – ADACCU: Accesses the upper byte ADACC[17:16]
                – ADACCH: Accesses the high byte ADACC[15:8]
                – ADACCL: Accesses the low byte ADACC[7:0]


--- p748 ---
40.7.18 ADSTPT

           Name:       ADSTPT
           Address:    0x3DF

           ADC Threshold Setpoint Register
           Depending on CALC, may be used to determine ADERR.

     Bit        15           14          13             12           11                 10             9              8
                                                          STPT[15:8]
  Access        R/W         R/W          R/W           R/W          R/W                R/W            R/W           R/W
   Reset         0           0            0             0             0                 0              0             0

     Bit         7           6            5              4                   3            2            1              0
                                                              STPT[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset         0           0            0             0                    0          0              0             0

Bits 15:0 – STPT[15:0] ADC Threshold Setpoint - Signed Two’s Complement

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • ADSTPTH: Accesses the high byte ADSTPT[15:8]
           •   ADSTPTH: Accesses the low byte ADSTPT[7:0]


--- p749 ---
40.7.19 ADERR

           Name:       ADERR
           Address:    0x3DD

           ADC Setpoint Error Register
           ADC Setpoint Error calculation is determined by the CALC bits.

     Bit         15          14          13             12                  11          10             9              8
                                                              ERR[15:8]
  Access         R           R            R              R                  R             R            R              R
   Reset         x           x            x              x                  x             x            x              x

     Bit         7           6            5              4                  3             2            1              0
                                                               ERR[7:0]
  Access         R           R            R              R                  R             R            R              R
   Reset         x           x            x              x                  x             x            x              x

Bits 15:0 – ERR[15:0] ADC Setpoint Error - Signed Two’s Complement

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • ADERRH: Accesses the high byte ADERR[15:8]
           •   ADERRL: Accesses the low byte ADERR[7:0]


--- p750 ---
40.7.20 ADLTH

           Name:       ADLTH
           Address:    0x3D9

           ADC Lower Threshold Register
           ADLTH and ADUTH are compared with ADERR to set the UTHR and LTHR bits. Depending on the
           setting of TMD, an interrupt may be triggered by the results of this comparison.

     Bit         15          14          13             12                  11          10             9              8
                                                              LTH[15:8]
  Access        R/W         R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset         0           0            0             0                    0          0              0             0

     Bit         7           6            5              4                   3            2            1              0
                                                               LTH[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset         0           0            0             0                    0          0              0             0

Bits 15:0 – LTH[15:0] ADC Lower Threshold - Signed Two’s Complement

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • ADLTHH: Accesses the high byte ADLTH[15:8]
           •   ADLTHL: Accesses the low byte ADLTH[7:0]


--- p751 ---
40.7.21 ADUTH

           Name:       ADUTH
           Address:    0x3DB

           ADC Upper Threshold Register
           ADLTH and ADUTH are compared with ADERR to set the UTHR and LTHR bits. Depending on the
           setting of TMD, an interrupt may be triggered by the results of this comparison.

     Bit        15           14          13             12          11                  10             9              8
                                                          UTH[15:8]
  Access        R/W         R/W          R/W           R/W         R/W                 R/W            R/W           R/W
   Reset         0           0            0             0           0                   0              0             0

     Bit         7           6            5              4                   3            2            1              0
                                                               UTH[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W        R/W            R/W           R/W
   Reset         0           0            0             0                    0          0              0             0

Bits 15:0 – UTH[15:0] ADC Upper Threshold - Signed Two’s Complement

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • ADUTHH: Accesses the high byte ADUTH[15:8]
           •   ADUTHL: Accesses the low byte ADUTH[7:0]


--- p752 ---
40.7.22 ADACT

            Name:      ADACT
            Address:   0x3F9

            ADC Auto Conversion Trigger Source Selection Register

      Bit        7           6           5              4                   3           2               1            0
                                                                                     ACT[4:0]
  Access                                              R/W                  R/W         R/W             R/W         R/W
   Reset                                               0                    0           0               0           0

Bits 4:0 – ACT[4:0] Auto-Conversion Trigger Select
                          ACT                                        Auto-Conversion Trigger Source
                     11111 - 11010                                               Reserved
                         11001                                           Software write to ADPCH
                         11000                                           Software read of ADRESH
                         10111                                           Software read of ADERRH
                         10110                                                  CLC4_OUT
                         10101                                                  CLC3_OUT
                         10100                                                  CLC2_OUT
                         10011                                                  CLC1_OUT
                         10010                                      Interrupt-on-change Interrupt Flag
                         10001                                                  CMP2_OUT
                         10000                                                  CMP1_OUT
                         01111                                                  NCO1_OUT
                         01110                                               PWM3S1P2_OUT
                         01101                                               PWM3S1P1_OUT
                         01100                                               PWM2S1P2_OUT
                         01011                                               PWM2S1P1_OUT
                         01010                                               PWM1S1P2_OUT
                         01001                                               PWM1S1P1_OUT
                         01000                                                 CCP1_trigger
                         00111                                                SMT1_overflow
                         00110                                                  TMR4_postscaled
                         00101                                                   TMR3_overflow
                         00100                                                  TMR2_postscaled
                         00011                                                   TMR1_overflow
                         00010                                                   TMR0_overflow
                         00001                                             Pin selected by ADACTPPS
                         00000                                             External Trigger Disabled


--- p753 ---
40.7.23 ADCP

           Name:       ADCP
           Address:    0x3D8

           ADC Charge Pump Control Register

     Bit        7             6               5              4                  3            2             1             0
              CPON                                                                                                     CPRDY
  Access       R/W                                                                                                       R
   Reset        0                                                                                                        0

Bit 7 – CPON Charge Pump On Control
           Value      Description
           1          Charge Pump On when requested by the ADC
           0          Charge Pump Off

Bit 0 – CPRDY Charge Pump Ready Status
           Value      Description
           1          Charge Pump is ready
           0          Charge Pump is not ready (or never started)


--- p754 ---
40.8      Register Summary - ADC
Address     Name      Bit Pos.    7          6            5             4                 3              2           1                0
 0x00
  ...      Reserved
0x03D7
0x03D8      ADCP        7:0      CPON                                                                                            CPRDY
                        7:0                                                   LTH[7:0]
0x03D9      ADLTH
                        15:8                                                 LTH[15:8]
                        7:0                                                   UTH[7:0]
0x03DB      ADUTH
                        15:8                                                 UTH[15:8]
                        7:0                                                   ERR[7:0]
0x03DD      ADERR
                        15:8                                                 ERR[15:8]
                        7:0                                                   STPT[7:0]
 0x03DF     ADSTPT
                        15:8                                                 STPT[15:8]
                        7:0                                                   FLTR[7:0]
 0x03E1     ADFLTR
                        15:8                                                 FLTR[15:8]
                        7:0                                                   ACC[7:0]
 0x03E3     ADACC       15:8                                                 ACC[15:8]
                       23:16                                                                                             ACC[17:16]
 0x03E6     ADCNT       7:0                                                   CNT[7:0]
 0x03E7     ADRPT       7:0                                                   RPT[7:0]
                        7:0                                                  PREV[7:0]
 0x03E8     ADPREV
                        15:8                                                 PREV[15:8]
                        7:0                                                   RES[7:0]
 0x03EA     ADRES
                        15:8                                                  RES[15:8]
0x03EC      ADPCH       7:0                                                   PCH[7:0]
0x03ED     Reserved
                       7:0                                                   ACQ[7:0]
 0x03EE     ADACQ
                       15:8                                                                          ACQ[12:8]
 0x03F0     ADCAP      7:0                                                                            CAP[4:0]
                       7:0                                                    PRE[7:0]
 0x03F1     ADPRE
                       15:8                                                                          PRE[12:8]
 0x03F3    ADCON0      7:0        ON       CONT                         CS                              FM                        GO
 0x03F4    ADCON1      7:0       PPOL      IPEN        GPOL                                                                      DSEN
 0x03F5    ADCON2      7:0       PSIS                 CRS[2:0]                           ACLR                     MD[2:0]
 0x03F6    ADCON3      7:0                            CALC[2:0]                           SOI                    TMD[2:0]
 0x03F7    ADSTAT      7:0       AOV       UTHR         LTHR        MATH                                         STAT[2:0]
 0x03F8     ADREF      7:0                                          NREF                                                PREF[1:0]
 0x03F9     ADACT      7:0                                                                            ACT[4:0]
 0x03FA     ADCLK      7:0                                                                      CS[5:0]


--- p755 ---
