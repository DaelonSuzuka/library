30.    PWM - Pulse-Width Modulator with Compare
       This module is a 16-bit Pulse-Width Modulator (PWM) with a compare feature and multiple outputs.
       The outputs are grouped in slices where each slice has two outputs. There can be up to four slices in
       each PWM module. The EN bit enables the PWM operation for all slices simultaneously. The prescale
       counter, postscale counter, and all internal logic is held in Reset while the EN bit is low.
       Features of this module include the following:
       • Five main operating modes:
           – Left Aligned
            – Right Aligned
            – Center-Aligned
            – Variable Aligned
            – Compare
               • Pulsed
                • Toggled
       •   Push-pull operation (available in Left and Right Aligned modes only)
       •   Independent 16-bit period timer
       •   Programmable clock sources
       •   Programmable trigger sources for synchronous duty cycle and period changes
       •   Programmable synchronous/asynchronous Reset sources
       •   Programmable Reset source polarity control
       •   Programmable PWM output polarity control
       •   Up to four two-output slices per module
       Block diagrams of each PWM mode are shown in their respective sections.

30.1   Output Slices
       A PWM module can have up to four output slices. An output slice consists of two PWM outputs,
       PWMx_SaP1_out and PWMx_SaP2_out. Both share the same operating mode. However, other slices
       may operate in a different mode. PWMx_SaP1_out and PWMx_SaP2_out have independent duty
       cycles which are set with the respective P1 and P2 parameter registers.

30.1.1 Output Polarity
       The polarity for the PWMx_SaP1_out and PWMx_SaP2_out is controlled with the respective POL1 and
       POL2 bits. Setting the polarity bit inverts the output Active state to Low True. Toggling the polarity bit
       toggles the output whether or not the PWM module is enabled.

30.1.2 Operating Modes
       Each output slice can operate in one of six modes selected with the MODE bits. The Left and Right
       Aligned modes can also be operated in Push-Pull mode by setting the PPEN bit. The following
       sections provide more details on each mode, including block diagrams.


--- p442 ---
30.1.2.1 Left Aligned Mode
        In Left Aligned mode, the active part of the duty cycle is at the beginning of the period. The outputs
        start active and stay active for the number of prescaled PWM clock periods specified by the P1 and
        P2 parameter registers, then go inactive for the remainder of the period. Block and timing diagrams
        follow.

        Figure 30-1. Left-Aligned Block Diagram


                                                        P1 Buffer
                                                                                 Duty Cycle


                                                                                               Reset
                                                        PR Buffer
                                                                                                           PWMx_SaP1_out
                                                                                                       Q


                                                                                                Set

             Clock                       PWMx_clk                   Period
                              Prescale                   Timer      Event
           Sources

                                                                                                Set

                PWMxCLK                                                                                    PWMx_SaP2_out
                                                                                                       Q


                                                                                               Reset


                                                                                 Duty Cycle
                                                        P2 Buffer


--- p443 ---
Figure 30-2. Left-Aligned Timing Diagram

    PWMx_clk


  PWMx_timer         0      1       2      3        4       5      0         1         2     3      4     5      0     1


     SaP1_out


     SaP2_out


      SaP1IF


      SaP2IF                                                      Reset by software


    PWMxPIF


      PWMxIF


      Note: MODE = ‘b000, PR = 5, P1 = 4, P2 = 2.


--- p444 ---
30.1.2.2 Right Aligned Mode
        In Right Aligned mode, the active part of the duty cycle is at the end of the period. The outputs start
        in the Inactive state and then go Active the number of prescaled PWM clock periods specified by the
        P1 and P2 parameter registers before the end of the period. Block and timing diagrams follow.

        Figure 30-3. Right-Aligned Block Diagram


                                                            P1 Buffer
                                                                                          Duty Cycle


                                                                                                                  Set
                                                            PR Buffer
                                                                                                                                 PWMx_SaP1_out
                                                                                                                         Q


                                                                                                                 Reset
                                             PWMx_clk
             Clock                Prescale                      Timer
                                                                        Period
                                                                        Event
           Sources

                                                                                                                 Reset

                PWMxCLK                                                                                                          PWMx_SaP2_out
                                                                                                                         Q


                                                                                                                  Set


                                                                                          Duty Cycle
                                                            P2 Buffer


        Figure 30-4. Right-Aligned Timing Diagram

           PWMx_clk


          PWMx_timer          0        1      2     3       4           5        0   1          2            3     4         5       0      1


            SaP1_out


            SaP2_out


              SaP2IF


              SaP1IF                                                                     Reset by software


              Note: MODE = ‘b001, PR = 5, P1 = 4, P2 = 2.


--- p445 ---
30.1.2.3 Center-Aligned Mode
       In Center-Aligned mode, the active duty cycle is centered in the period. The period for this mode is
       twice that of other modes, as shown in the following equation.

       Equation 30-1. Center-Aligned Period
                    PR + 1 × 2
       Period =
                    FPWMx_clk

       The parameter register specifies the number of PWM clock periods that the output goes Active
       before the period center. The output goes inactive the same number of prescaled PWM clock
       periods after the period center. Block and timing diagrams follow.

       Figure 30-5. Center-Aligned Block Diagram


                                                          P1 Buffer
                                                                                       Duty Cycle


                                                                                                             Reset
                                                          PR Buffer                                                          PWMx_SaP1_out
                                                                                                                     Q


                                                                                                              Set
                                           PWMx_clk
            Clock               Prescale                      Timer
                                                                      Period
                                                                      Event
          Sources


                                                                                                              Set
               PWMxCLK
                                                                                                                             PWMx_SaP2_out
                                                                                                                     Q


                                                                                                             Reset

                                                                                       Duty Cycle
                                                          P2 Buffer


       Figure 30-6. Center-Aligned Timing Diagram

           PWMx_clk


          PWMx_timer        0         1     2      3      4           5        0   1        2         3         4        5       0      1


            SaP1_out


            SaP2_out


              SaP1IF                                                                            Reset by software


              SaP2IF

            Note: MODE = ‘b010, PR = 5, P1 = 4, P2 = 2.


--- p446 ---
30.1.2.4 Variable Alignment Mode
       In Variable Alignment mode, the active part of the duty cycle starts when the parameter 1 value
       (P1) matches the timer and ends when the parameter 2 value (P2) matches the timer. Both outputs
       are identical because both parameter values are used for the same duty cycle. Block and timing
       diagrams follow.

       Figure 30-7. Variable Alignment Block Diagram


                                                          P1 Buffer
                                                                                   =


                                                          PR Buffer
                                                                                                   Set

                                                                                                                       PWMx_SaP1_out
                                                                                                           Q


                                           PWMx_clk                                               Reset                PWMx_SaP2_out
            Clock               Prescale                      Timer
                                                                      Period
                                                                      Event
          Sources


               PWMxCLK
                                                                                   =
                                                          P2 Buffer


       Figure 30-8. Variable Alignment Timing Diagram

           PWMx_clk


          PWMx_timer        0         1     2      3      4           5        0   1     2         3           4   5       0      1


            SaP1_out


            SaP2_out


              SaP1IF                                                                   Reset by software


              SaP1IF


            PWMxPIF


            Note: MODE = ‘b011, PR = 5, P1 = 4, P2 = 2.


--- p447 ---
30.1.2.5 Compare Modes
       In the Compare modes, the PWM timer is compared to the P1 and P2 parameter values. When a
       match occurs, the output is either pulsed or toggled. In Pulsed Compare mode, the duty cycle is
       always one prescaled PWM clock period. In Toggle Compare mode, the duty cycle is always one full
       PWM period. Refer to the following sections for more details.
30.1.2.5.1 Pulsed Compare Mode
       In Pulsed Compare mode, the duty cycle is one prescaled PWM clock period that starts when the
       timer matches the parameter value and ends one prescaled PWM clock period later. The outputs
       start in the Inactive state and then go Active during the duty cycle. Block and timing diagrams follow.

       Figure 30-9. Pulsed Compare Block Diagram


                                                          P1 Buffer
                                                                                   =

                                                                                                  Pulse

                                                                                                                       PWMx_SaP1_out
                                                                                                           Q
                                                          PR Buffer


                                           PWMx_clk
            Clock               Prescale                      Timer
                                                                      Period                                           PWMx_SaP2_out
          Sources
                                                                      Event                                Q


                                                                                                  Pulse

               PWMxCLK
                                                                                   =
                                                          P2 Buffer


       Figure 30-10. Pulsed Compare Timing Diagram

           PWMx_clk


         PWMx_timer         0         1     2     3       4           5        0   1     2         3           4   5       0      1


           SaP1_out


           SaP2_out


             SaP1IF                                                                    Reset by software


             SaP1IF


           PWMxPIF


            Note: MODE = ‘b100, PR = 5, P1 = 4, P2 = 2.


--- p448 ---
30.1.2.5.2 Toggled Compare
        In Toggled Compare mode, the duty cycle is alternating full PWM periods. The output goes Active
        when the PWM timer matches the P1 or P2 parameter value and goes Inactive in the next period at
        the same match point. Block and timing diagrams follow.

        Figure 30-11. Toggled Compare Block Diagram


                                                           P1 Buffer
                                                                                    =

                                                                                                  Toggle

                                                                                                                        PWMx_SaP1_out
                                                                                                            Q
                                                           PR Buffer


                                            PWMx_clk
             Clock               Prescale                      Timer
                                                                       Period                                           PWMx_SaP2_out
           Sources
                                                                       Event                                Q


                                                                                                  Toggle

                PWMxCLK
                                                                                    =
                                                           P2 Buffer


        Figure 30-12. Toggled Compare Timing Diagram

            PWMx_clk


          PWMx_timer         0         1     2      3      4           5        0   1     2         3           4   5       0      1


            SaP1_out


            SaP2_out


              SaP1IF                                                                    Reset by software


              SaP1IF


            PWMxPIF


             Note: MODE = ‘b101, PR = 5, P1 = 4, P2 = 2.


--- p449 ---
30.1.3 Push-Pull Mode
       The Push-Pull mode is enabled by setting the PPEN bit. Push-Pull operates only in the Left Aligned
       and Right Aligned modes. In the Push-Pull mode, the outputs are Active every other PWM period.
       PWMx_SaP1_out is Active when the PWMx_SaP2_out is not and the PWMx_SaP2_out is Active when
       the PWMx_SaP1_out is not. When the parameter value (P1 or P2) is greater than the period value
       (PR), then the corresponding output is Active for one full PWM period. The following figures illustrate
       timing examples of Left and Right Aligned Push-Pull modes.

       Figure 30-13. Left Aligned Push-Pull Mode Timing Diagram

          PWMx_clk


         PWMx_timer         0      1       2        3       4      5       0         1           2         3    4   5     0      1


           SaP1_out


           SaP2_out


             SaP1IF


             SaP2IF

                                                                                            Reset by software
             Note: MODE = ‘b000, PR = 5, P1 = 4, P2 = 2, PPEN = 1.


       Figure 30-14. Right Aligned Push-Pull Mode Timing Diagram

          PWMx_clk


        PWMx_timer          0       1      2         3      4       5       0         1           2        3    4   5      0     1


           SaP1_out


           SaP2_out


             SaP1IF                                                     Reset by software


             SaP2IF


             Note: MODE = ‘b001, PR = 5, P1 = 6, P2 = 2, PPEN = 1.


30.2   Period Timer
       All slices in a PWM instance operate with the same period. The value written to the PWMxPR register
       is one less than the number of prescaled PWM clock periods (PWM_clk) in the PWM period.
       The PWMxPR register is double-buffered. When the PWM is operating, writes to the PWMxPR
       register are transferred to the period buffer only after the LD bit is set or an external load event
       occurs. The transfer occurs at the next period Reset event. If the LD bit is set less than three PWM
       clock periods before the end of the period, then the transfer may be one full period later.


--- p450 ---
       Loading the buffers of multiple PWM instances can be coordinated using the PWMLOAD register.
       See the Buffered Period and Parameter Registers section for more details.

30.3   Clock Sources
       The time base for the PWM period prescaler is selected with the CLK bits. Changes take effect
       immediately when written. Clearing the EN bit before making clock source changes is recommended
       to avoid unexpected behavior.

30.3.1 Clock Prescaler
       The PWM clock frequency can be reduced with the clock prescaler. There are 256 prescale selections
       from 1:1 to 1:256.
       The CPRE bits select the prescale value. Changes to the prescale value take effect immediately.
       Clearing the EN bit before making prescaler changes is recommended to avoid unexpected
       behavior. The prescale counter is reset when the EN bit is cleared.

30.4   External Period Resets
       The period timer can be reset and held at zero by a logic level from one of various sources. The
       Reset event also resets the postscaler counter. The resetting source is selected with the ERS bits.
       The Reset can be configured with the ERSNOW bit to occur on either the next PWM clock or the
       next PWM period Reset event. When the ERSNOW bit is set, then the Reset will occur on the next
       PWM clock. When the ERSNOW bit is cleared, then the Reset will be held off until the timer resets at
       the end of the period. The difference between a normal period Reset and an ERS Reset is that once
       the timer is reset, it is held at zero until the ERS signal goes false. The following timing diagrams
       illustrate the two types of external Reset.

       Figure 30-15. Right Aligned Mode with ERSNOW = 1

           PWMx_clk


         PWMx_timer         0       1      2     3      4      5       0     1       2     3     0     0      0     1


          PWMx_ers


           SaP1_out


           SaP2_out


           Note: PR = 5, P1 = 4, P2 = 2.


--- p451 ---
       Figure 30-16. Left Aligned Mode with ERSNOW = 0

           PWMx_clk


         PWMx_timer         0       1      2     3      4      5       0     0       0     1     2     3      4     5


          PWMx_ers


           SaP1_out


           SaP2_out


           Note: PR = 5, P1 = 4, P2 = 2.


30.5   Buffered Period and Parameter Registers
       The PWMxPR, PWMxSaP1 and PWMxSaP2 registers are double-buffered. The PWM module operates
       on the buffered copies. The values in all these registers are copied to the buffer registers when the
       PWM module is enabled.
       Changes to the PWMxPR, PWMxSaP1 and PWMxSaP2 registers do not affect the buffer registers
       while the PWM is operating until either software sets the LD bit or an external load event occurs.
       For all operating modes except Center-Aligned, the values are copied to the buffer registers when
       the PWM timer is reloaded at the end of the period in which the load request occurred. In the
       Center-Aligned mode, the buffer update occurs on every other period Reset event because one full
       center-aligned period uses two period cycles. Load requests occurring three or less clocks before the
       end of the period may not be serviced until the following period.
       A list of external load trigger sources is shown in the PWMxLDS register. Software can set the LD bits
       of multiple PWM instances simultaneously with the PWMLOAD register.


                      Important: No changes are allowed after the LD bit is set until after the LD bit is cleared
                      by hardware. Unexpected behavior may result if the LD bit is cleared by software.


30.6   Synchronizing Multiple PWMs
       To synchronize multiple PWMs, the PWMEN register is used to enable selected PWMs
       simultaneously. The bits in the PWMEN register are mirror copies of the EN bit of every PWM
       in the device. Setting or clearing the EN bits in the PWMEN register enables or disables all the
       corresponding PWMs simultaneously.

30.7   Interrupts
       Each PWM instance has a period interrupt and interrupts associated with the mode and parameter
       settings.

30.7.1 Period Interrupt
       The period interrupt occurs when the PWMx timer value matches the PR value, thereby also
       resetting the PWMx timer. Refer to Figure 30-2 for a timing example. The period interrupt is
       indicated with the PWMxPIF flag bit in one of the PIR registers and is set whether or not the interrupt
       is enabled. This flag must be reset by software. The PWMxPIF interrupt is enabled with the PWMxPIE
       bit in the corresponding PIE register.


--- p452 ---
30.7.1.1 Period Interrupt Postscaler
        The frequency of the period interrupt events can be reduced with the period interrupt postscaler. A
        postscaler counter suppresses period interrupts until the postscale count is reached. Only one PWM
        period interrupt is generated for every postscale counts. There are 256 postscale selections from 1:1
        to 1:256.
        The PIPOS bits select the postscale value. Changes to the postscale value take effect immediately.
        Clearing the EN bit before making postscaler changes is recommended to avoid unexpected
        behavior. The postscale counter is reset when the EN bit is cleared.

30.7.2 Parameter Interrupts
        The P1 and P2 parameters in each slice have interrupts that occur depending on the selected mode.
        The individual parameter interrupts are indicated in the PWMxGIR register and enabled by the
        corresponding bits in the PWMxGIE register.
        A timing example is shown in Figure 30-2. Refer to the timing diagrams of each of the other modes
        for more details.
        All the enabled PWMxGIR interrupts of one PMW instance are OR’d together into the PWMxIF bit in
        one of the PIR registers. The PWMxIF bit is read-only. When any of the PWMxGIR bits are set then the
        PWMxIF bit is true. All PWMxGIF flags must be reset to clear the PWMxIF bit. The PWMxIF interrupt is
        enabled with the PWMxIE bit in the corresponding PIE register.

30.8    Operation During Sleep
        The PWM module operates in Sleep only if the PWM clock is Active. Some internal clock sources
        are automatically enabled to operate in Sleep when a peripheral using them is enabled. Those
        clock sources are identified in the clock source table shown in the PWMxCLK clock source selection
        register.

30.9    Register Definitions: PWM Control
        Long bit name prefixes for the PWM peripherals are shown in the table below. Refer to the “Long Bit
        Names” section in the “Register and Bit Naming Conventions” chapter for more information.

        Table 30-1. PWM Long Bit Name Prefixes
                         Peripheral                                             Bit Name Prefix
                           PWM1                                                         PWM1
                           PWM2                                                         PWM2
                           PWM3                                                         PWM3


--- p453 ---
30.9.1 PWMxERS

            Name:        PWMxERS
            Address:     0x460,0x46F,0x47E
            PWMx External Reset Source

      Bit        7            6          5              4                   3            2               1            0
                                                                                             ERS[3:0]
  Access                                                                   R/W      R/W                 R/W          R/W
   Reset                                                                    0        0                   0            0

Bits 3:0 – ERS[3:0] External Reset Source Select
                                                                        Reset Source
                       ERS
                                             PWM1                          PWM2                               PWM3
                1111 - 1100                                        Reserved (ERS Disabled)
                    1011                                                 CLC4_OUT
                    1010                                                 CLC3_OUT
                    1001                                                 CLC2_OUT
                    1000                                                 CLC1_OUT
                    0111               PWM3S1P2_OUT                   PWM3S1P2_OUT                         Reserved
                    0110               PWM3S1P1_OUT                   PWM3S1P1_OUT                         Reserved
                    0101               PWM2S1P2_OUT                       Reserved                      PWM2S1P2_OUT
                    0100               PWM2S1P1_OUT                       Reserved                      PWM2S1P1_OUT
                    0011                  Reserved                    PWM1S1P2_OUT                      PWM1S1P2_OUT
                    0010                  Reserved                    PWM1S1P1_OUT                      PWM1S1P1_OUT
                    0001                PWM1ERSPPS                     PWM2ERSPPS                        PWM3ERSPPS
                    0000                                                ERS Disabled


--- p454 ---
30.9.2 PWMxCLK

           Name:        PWMxCLK
           Address:     0x461,0x470,0x47F
           PWMx Clock Source

     Bit         7             6             5             4                   3            2               1         0
                                                                                                CLK[3:0]
  Access                                                                      R/W      R/W                 R/W      R/W
   Reset                                                                       0        0                   0        0

Bits 3:0 – CLK[3:0] PWM Clock Source Select
                      CLK                               Source                              Operates in Sleep
                      1111                             Reserved                                     N/A
                      1110                            CLC4_OUT                                     Yes(1)
                      1101                            CLC3_OUT                                     Yes(1)
                      1100                            CLC2_OUT                                     Yes(1)
                      1011                            CLC1_OUT                                     Yes(1)
                      1010                           NCO1_OUT                                      Yes(1)
                      1001                              CLKREF                                     Yes(1)
                      1000                              EXTOSC                                      Yes
                      0111                               SOSC                                       Yes
                      0110                      MFINTOSC (32 kHz)                                   Yes
                      0101                     MFINTOSC (500 kHz)                                   Yes
                      0100                            LFINTOSC                                      Yes
                      0011                            HFINTOSC                                      Yes
                      0010                               FOSC                                       No
                      0001                          PWMIN1PPS                                      Yes(1)
                      0000                          PWMIN0PPS                                      Yes(1)
           Note: Operation during Sleep is possible if the clock supplying the source peripheral operates in Sleep.


--- p455 ---
30.9.3 PWMxLDS

            Name:        PWMxLDS
            Address:     0x462,0x471,0x480
            PWMx Auto-load Trigger Source Select Register

      Bit        7            6          5              4                   3            2               1         0
                                                                                             LDS[3:0]
  Access                                                                   R/W      R/W                 R/W      R/W
   Reset                                                                    0        0                   0        0

Bits 3:0 – LDS[3:0] Auto-load Trigger Source Select
                           LDS                                                Source
                       1111 - 1011                                      Auto-load Disabled
                           1010                                     DMA4_Destination_Count_Done
                           1001                                     DMA3_Destination_Count_Done
                           1000                                     DMA2_Destination_Count_Done
                           0111                                     DMA1_Destination_Count_Done
                           0110                                             CLC4_OUT
                           0101                                             CLC3_OUT
                           0100                                             CLC2_OUT
                           0011                                             CLC1_OUT
                           0010                                            PWMIN1PPS
                           0001                                            PWMIN0PPS
                           0000                                         Auto-load Disabled


--- p456 ---
30.9.4 PWMxPR

           Name:       PWMxPR
           Address:    0x463,0x472,0x481
           PWMx Period Register
           Determines the PWMx period

     Bit        15           14          13             12                  11        10            9            8
                                                               PR[15:8]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W          R/W           R/W
   Reset         0           0            0             0                    0        0            0             0

     Bit         7           6            5              4                   3            2         1            0
                                                                PR[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W          R/W           R/W
   Reset         0           0            0             0                    0        0            0             0

Bits 15:0 – PR[15:0] PWM Period
         Number of PWM clocks periods in the PWM period

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • PWMxPRH: Accesses the high byte PR[15:8]
           •   PWMxPRL: Accesses the low byte PR[7:0]


--- p457 ---
30.9.5 PWMxCPRE

           Name:        PWMxCPRE
           Address:     0x465,0x474,0x483
           PWMx Clock Prescaler Register

     Bit           7           6              5              4                   3            2         1            0
                                                                  CPRE[7:0]
  Access       R/W            R/W           R/W            R/W                  R/W      R/W          R/W           R/W
   Reset        0              0             0              0                    0        0            0             0

Bits 7:0 – CPRE[7:0] PWM Clock Prescale Value
           Value       Description
           n           PWM clock is prescaled by n+1


--- p458 ---
30.9.6 PWMxPIPOS

            Name:        PWMxPIPOS
            Address:     0x466,0x475,0x484
            PWMx Period Interrupt Postscaler Register

      Bit           7            6              5              4            3                   2         1            0
                                                                 PIPOS[7:0]
  Access        R/W            R/W            R/W             R/W          R/W             R/W          R/W           R/W
   Reset         0              0              0               0            0               0            0             0

Bits 7:0 – PIPOS[7:0] Period Interrupt Postscale Value
            Value       Description
            n           Period interrupt occurs after n+1 period events


--- p459 ---
30.9.7 PWMxGIR

            Name:        PWMxGIR
            Address:     0x467,0x476,0x485
            PWMx Interrupt Register

      Bit           7           6             5              4                  3             2        1             0
                                                                                                     S1P2          S1P1
  Access                                                                                            R/W/HS        R/W/HS
   Reset                                                                                               0             0

Bit 1 – SaP2 Slice “a” Parameter 2 Interrupt Flag
            Value       Mode                             Description
            1           Variable Aligned or Compare      Compare match between P2 and PWM counter has occurred
            1           Center-Aligned                   PWMx_SaP2_out has changed
            1           Right Aligned                    Left edge of PWMx_SaP2_out pulse has occurred
            1           Left Aligned                     Right edge of PWMx_SaP2_out pulse has occurred
            0           All                              Interrupt event has not occurred

Bit 0 – SaP1 Slice “a” Parameter 1 Interrupt Flag
            Value       Mode                             Description
            1           Variable Aligned or Compare      Compare match between P1 and PWM counter has occurred
            1           Center-Aligned                   PWMx_SaP1_out has changed
            1           Right Aligned                    Left edge of PWMx_SaP1_out pulse has occurred
            1           Left Aligned                     Right edge of PWMx_SaP1_out pulse has occurred
            0           All                              Interrupt event has not occurred


--- p460 ---
30.9.8 PWMxGIE

            Name:        PWMxGIE
            Address:     0x468,0x477,0x486
            PWMx Interrupt Enable Register

      Bit           7            6              5               4                  3            2         1            0
                                                                                                        S1P2         S1P1
  Access                                                                                                R/W          R/W
   Reset                                                                                                  0            0

Bit 1 – SaP2 Slice “a” Parameter 2 Interrupt Enable
            Value       Description
            1           Slice “a” Parameter 2 match interrupt is enabled
            0           Slice “a” Parameter 2 match interrupt is not enabled

Bit 0 – SaP1 Slice “a” Parameter 1 Interrupt Enable
            Value       Description
            1           Slice “a” Parameter 1 match interrupt is enabled
            0           Slice “a” Parameter 1 match interrupt is not enabled


--- p461 ---
30.9.9 PWMxCON

            Name:       PWMxCON
            Address:    0x469,0x478,0x487
            PWM Control Register

      Bit        7              6               5               4                  3            2               1              0
                EN                                                                             LD            ERSPOL         ERSNOW
  Access        R/W                                                                          R/W/HC           R/W             R/W
   Reset         0                                                                              0               0              0

Bit 7 – EN PWM Module Enable
            Value      Description
            1          PWM module is enabled
            0          PWM module is disabled. The prescaler, postscaler, and all internal logic is reset. Outputs go to their default
                       states. Register values remain unchanged.

Bit 2 – LD Reload Registers
          Reload the period and duty cycle registers on the next period event
            Value      Description
            1          Reload PR/P1/P2 registers
            0          Reload not enabled or reload complete

Bit 1 – ERSPOL External Reset Polarity Select
            Value      Description
            1          External Reset input is active-low
            0          External Reset input is active-high

Bit 0 – ERSNOW External Reset Mode Select
          Determines when an external Reset event takes effect.
            Value      Description
            1          Stop counter on the next PWM clock. Output goes to the Inactive state.
            0          Stop counter at the end of the period. Output goes to the Inactive state.


--- p462 ---
30.9.10 PWMxSaCFG

            Name:         PWMxSaCFG
            PWM Slice “a” Configuration Register(1)

      Bit          7            6               5              4                  3             2       1              0
                  POL2         POL1                                             PPEN                 MODE[2:0]
  Access          R/W          R/W                                               R/W       R/W         R/W            R/W
   Reset           0            0                                                 0         0           0              0

Bit 7 – POL2 PWM Slice “a” Parameter 2 Output Polarity
            Value        Description
            1            PWMx_SaP2_out is low true
            0            PWMx_SaP2_out is high true

Bit 6 – POL1 PWM Slice “a” Parameter 1 Output Polarity
            Value        Description
            1            PWMx_SaP1_out is low true
            0            PWMx_SaP1_out is high true

Bit 3 – PPEN Push-Pull Mode Enable
          Each period the output alternates between PWMx_SaP1_out and PWMx_SaP2_out. Only Left and
          Right Aligned modes are supported. Other modes may exhibit unexpected results.
            Value        Description
            1            PWMx Slice “a” Push-Pull mode is enabled
            0            PWMx Slice “a” Push-Pull mode is not enabled

Bits 2:0 – MODE[2:0] PWM Module Slice “a” Operating Mode Select
          Selects operating mode for both PWMx_SaP1_out and PWMx_SaP2_out
            Value        Description
            11x          Reserved. Outputs go to Reset state.
            101          Compare mode: Toggle PWMx_SaP1_out and PWMx_SaP2_out on PWM timer match with corresponding
                         parameter register
            100          Compare mode: Set PWMx_SaP1_out and PWMx_SaP2_out high on PWM timer match with corresponding
                         parameter register
            011          Variable Aligned mode
            010          Center-Aligned mode
            001          Right Aligned mode
            000          Left Aligned mode

            Note:
            1. Changes to this register must be done only when the EN bit is cleared.


--- p463 ---
30.9.11 PWMxSaP1

            Name:         PWMxSaP1
            PWM Slice “a” Parameter 1 Register
            Determines the active period of slice “a”, parameter 1 output

      Bit           15          14            13             12                  11        10            9            8
                                                                    P1[15:8]
  Access         R/W           R/W           R/W            R/W                  R/W      R/W          R/W           R/W
   Reset          0             0             0              0                    0        0            0             0

      Bit           7            6             5              4                   3            2         1            0
                                                                     P1[7:0]
  Access         R/W           R/W           R/W            R/W                  R/W      R/W          R/W           R/W
   Reset          0             0             0              0                    0        0            0             0

Bits 15:0 – P1[15:0] Parameter 1 Value
            Value        Mode             Description
            n            Compare          Compare match event occurs when PWMx timer = n (refer to MODE selections)
            n            Variable Aligned PWMx_SaP1_out and PWMx_SaP2 both go high when PWMx timer = n
            n            Center-Aligned   PWMx_SaP1_out is high 2*n PWMx clock periods centered around PWMx period event
            n            Right Aligned    PWMx_SaP1_out is high n PWMx clock periods at end of PWMx period
            n            Left Aligned     PWMx_SaP1_out is high n PWMx clock periods at beginning of PWMx period

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names:
            • PWMxSaP1H: Accesses the high byte P1[15:8]
            •   PWMxSaP1L: Accesses the low byte P1[7:0]


--- p464 ---
30.9.12 PWMxSaP2

            Name:         PWMxSaP2
            PWM Slice “a” Parameter 2 Register
            Determines the active period of slice “a”, parameter 2 output

      Bit           15          14            13             12                  11        10            9            8
                                                                    P2[15:8]
  Access         R/W           R/W           R/W            R/W                  R/W      R/W          R/W           R/W
   Reset          0             0             0              0                    0        0            0             0

      Bit           7            6             5              4                   3            2         1            0
                                                                     P2[7:0]
  Access         R/W           R/W           R/W            R/W                  R/W      R/W          R/W           R/W
   Reset          0             0             0              0                    0        0            0             0

Bits 15:0 – P2[15:0] Parameter 2 Value
            Value        Mode             Description
            n            Compare          Compare match event occurs when PWMx timer = n (refer to MODE selections)
            n            Variable Aligned PWMx_SaP1_out and PWMx_SaP2 both go low when PWMx timer = n
            n            Center-Aligned   PWMx_SaP2_out is high 2*n PWMx clock periods centered around PWMx period event
            n            Right Aligned    PWMx_SaP2_out is high n PWMx clock periods at end of PWMx period
            n            Left Aligned     PWMx_SaP2_out is high n PWMx clock periods at beginning of PWMx period

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names:
            • PWMxSaP2H: Accesses the high byte P2[15:8]
            •   PWMxSaP2L: Accesses the low byte P2[7:0]


--- p465 ---
30.9.13 PWMLOAD

            Name:        PWMLOAD
            Address:     0x49C
            Mirror copies of all PWMxLD bits

      Bit           7            6              5               4                  3        2               1               0
                                                                                         MPWM3LD         MPWM2LD         MPWM1LD
  Access                                                                                   R/W             R/W             R/W
   Reset                                                                                    0               0               0

Bits 0, 1, 2 – MPWMxLD Mirror copy of PWMxLD bit
          Mirror copies of all PWMxLD bits can be set simultaneously to synchronize the load event across all
          PWMs
            Value       Description
            1           PWMx parameter and period values will be transferred to their buffer registers at the next period Reset event
            0           There are no PWMx period and parameter value transfers pending


--- p466 ---
30.9.14 PWMEN

            Name:        PWMEN
            Address:     0x49D
            Mirror copies of all PWMxEN bits

      Bit           7           6             5              4                  3        2            1            0
                                                                                      MPWM3EN      MPWM2EN      MPWM1EN
  Access                                                                                R/W          R/W          R/W
   Reset                                                                                 0            0            0

Bits 0, 1, 2 – MPWMxEN Mirror copy of PWMxEN bit
          Mirror copies of all PWMxEN bits can be set simultaneously to synchronize the enable event across
          all PWMs
            Value       Description
            1           PWMx is enabled
            0           PWMx is not enabled


--- p467 ---
30.10 Register Summary - PWM
Address     Name      Bit Pos.    7          6           5             4                3          2               1          0
  0x00
   ...     Reserved
 0x045F
0x0460    PWM1ERS      7:0                                                                              ERS[3:0]
0x0461    PWM1CLK      7:0                                                                              CLK[3:0]
0x0462    PWM1LDS      7:0                                                                              LDS[3:0]
                       7:0                                                   PR[7:0]
0x0463     PWM1PR
                       15:8                                                 PR[15:8]
0x0465    PWM1CPRE     7:0                                                 CPRE[7:0]
0x0466    PWM1PIPOS    7:0                                                 PIPOS[7:0]
0x0467     PWM1GIR     7:0                                                                                     S1P2         S1P1
0x0468     PWM1GIE     7:0                                                                                     S1P2         S1P1
0x0469     PWM1CON     7:0        EN                                                               LD         ERSPOL      ERSNOW
0x046A    PWM1S1CFG    7:0       POL2      POL1                                        PPEN                  MODE[2:0]
                       7:0                                                  P1[7:0]
0x046B    PWM1S1P1
                       15:8                                                 P1[15:8]
                       7:0                                                  P2[7:0]
0x046D    PWM1S1P2
                       15:8                                                 P2[15:8]
0x046F    PWM2ERS      7:0                                                                              ERS[3:0]
0x0470    PWM2CLK      7:0                                                                              CLK[3:0]
0x0471    PWM2LDS      7:0                                                                              LDS[3:0]
                       7:0                                                   PR[7:0]
0x0472     PWM2PR
                       15:8                                                 PR[15:8]
0x0474    PWM2CPRE     7:0                                                 CPRE[7:0]
0x0475    PWM2PIPOS    7:0                                                 PIPOS[7:0]
0x0476     PWM2GIR     7:0                                                                                     S1P2         S1P1
0x0477     PWM2GIE     7:0                                                                                     S1P2         S1P1
0x0478     PWM2CON     7:0        EN                                                               LD         ERSPOL      ERSNOW
0x0479    PWM2S1CFG    7:0       POL2      POL1                                        PPEN                  MODE[2:0]
                       7:0                                                  P1[7:0]
0x047A    PWM2S1P1
                       15:8                                                 P1[15:8]
                       7:0                                                  P2[7:0]
0x047C    PWM2S1P2
                       15:8                                                 P2[15:8]
0x047E    PWM3ERS      7:0                                                                              ERS[3:0]
0x047F    PWM3CLK      7:0                                                                              CLK[3:0]
0x0480    PWM3LDS      7:0                                                                              LDS[3:0]
                       7:0                                                   PR[7:0]
0x0481     PWM3PR
                       15:8                                                 PR[15:8]
0x0483    PWM3CPRE     7:0                                                 CPRE[7:0]
0x0484    PWM3PIPOS    7:0                                                 PIPOS[7:0]
0x0485     PWM3GIR     7:0                                                                                     S1P2         S1P1
0x0486     PWM3GIE     7:0                                                                                     S1P2         S1P1
0x0487     PWM3CON     7:0        EN                                                               LD         ERSPOL      ERSNOW
0x0488    PWM3S1CFG    7:0       POL2      POL1                                        PPEN                  MODE[2:0]
                       7:0                                                  P1[7:0]
0x0489    PWM3S1P1
                       15:8                                                 P1[15:8]
                       7:0                                                  P2[7:0]
0x048B    PWM3S1P2
                       15:8                                                 P2[15:8]
0x048D
  ...      Reserved
0x049B
0x049C    PWMLOAD       7:0                                                                    MPWM3LD       MPWM2LD      MPWM1LD
0x049D     PWMEN        7:0                                                                    MPWM3EN       MPWM2EN      MPWM1EN


--- p468 ---
