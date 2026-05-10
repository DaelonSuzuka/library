                                                                                                                              PIC18F27/47/57Q43
                                                                                                                            TMR2 - Timer2 Module


26.   TMR2 - Timer2 Module
      The Timer2 module is an 8-bit timer that incorporates the following features:
      •    8-bit timer and period registers
      •    Readable and writable
      •    Software programmable prescaler (1:1 to 1:128)
      •    Software programmable postscaler (1:1 to 1:16)
      •    Interrupt on T2TMR match with T2PR
      •    One-shot operation
      •    Full asynchronous operation
      •    Includes Hardware Limit Timer (HLT)
      •    Alternate clock sources
      •    External timer Reset signal sources
      •    Configurable timer Reset operation
      See the figure below for a block diagram of Timer2.


                        Important: References to module Timer2 apply to all the even numbered timers
                        on this device (Timer2, Timer4, etc.).


      Figure 26-1. Timer2 with Hardware Limit Timer (HLT) Block Diagram


                         RSEL
                  TxINPPS                                                                                                                     Rev. 10-000168D
                                                                                                                                                     4/29/2019


                  TxIN    PPS
                                                                MODE                                                    MODE[3]

                         External
                                           TMRx_ers          Edge Detector    reset
                          Reset
                        Sources(2)                           Level Detector                                                                 CCP_pset(1)
                                                             Mode Control
                                                             (2 clock Sync)


                                                            enable                    MODE[4:3] = 'b01
                CKPOL                                                                                                                          Clear ON
                   CS                                                            MODE[4:1] = 'b1011                                D      Q
                                      TMRx_clk
          TxINPPS
          TxIN    PPS
                                                                Prescaler                    0
                                                                                                                  R
                                                                                                          TxTMR
                                                                                                                                        Set flag bit
                 See                                                             Sync        1                                           TMRxIF
             TxCLKCON
              register(3)                                        CKPS          Fosc/4      PSYNC                                   TMRx_postscaled
                                                                                                         Comparator   Postscaler


                                        Sync
                                     (2 Clocks)
                                                    1
                                                                                                           TxPR       OUTPS
                            ON                      0


                                                  CSYNC


--- p402 ---
                                                                                           PIC18F27/47/57Q43
                                                                                         TMR2 - Timer2 Module

       Notes:
       1. Signal to the CCP peripheral for PWM pulse trigger in PWM mode.
       2. See RSEL for external Reset sources.
       3. See CS for clock source selections.

26.1   Timer2 Operation
       Timer2 operates in three major modes:
       •   Free-Running Period
       •   One Shot
       •   Monostable
       Within each operating mode, there are several options for starting, stopping and Reset. Table 26-1
       lists the options.
       In all modes, the T2TMR count register increments on the rising edge of the clock signal from the
       programmable prescaler. When T2TMR equals T2PR, a high-level output to the postscaler counter is
       generated. T2TMR is cleared on the next clock input.
       An external signal from hardware can also be configured to gate the timer operation or force a
       T2TMR count Reset. In Gate modes, the counter stops when the gate is disabled and resumes when
       the gate is enabled. In Reset modes, the T2TMR count is reset on either the level or edge from the
       external source.
       The T2TMR and T2PR registers are both directly readable and writable. The T2TMR register is cleared
       and the T2PR register initializes to 0xFF on any device Reset. Both the prescaler and postscaler
       counters are cleared on the following events:
       •   A write to the T2TMR register
       •   A write to the T2CON register
       •   Any device Reset
       •   External Reset source event that resets the timer


                        Important: T2TMR is not cleared when T2CON is written.


26.1.1 Free-Running Period Mode
       The value of T2TMR is compared to that of the period register, T2PR, on each clock cycle. When
       the two values match, the comparator resets the value of T2TMR to 0x00 on the next cycle and
       increments the output postscaler counter. When the postscaler count equals the value in the OUTPS
       bits of the T2CON register, a one clock period wide pulse occurs on the TMR2_postscaled output,
       and the postscaler count is cleared.

26.1.2 One Shot Mode
       The One Shot mode is identical to the Free-Running Period mode except that the ON bit is cleared
       and the timer is stopped when T2TMR matches T2PR and will not restart until the ON bit is cycled
       off and on. Postscaler (OUTPS) values other than zero are ignored in this mode because the timer is
       stopped at the first period event and the postscaler is reset when the timer is restarted.

26.1.3 Monostable Mode
       Monostable modes are similar to One Shot modes except that the ON bit is not cleared and the
       timer can be restarted by an external Reset event.


--- p403 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                            TMR2 - Timer2 Module

26.2   Timer2 Output
       The Timer2 module’s primary output is TMR2_postscaled, which pulses for a single TMR2_clk
       period upon each match of the postscaler counter and the OUTPS bits of the T2CON register. The
       postscaler is incremented each time the T2TMR value matches the T2PR value. This signal can also
       be selected as an input to other Core Independent Peripherals.
       In addition, the Timer2 is also used by the CCP module for pulse generation in PWM mode. See
       the “PWM Overview” and “PWM Period” sections in the “CCP - Capture/Compare/PWM Module”
       chapter for more details on setting up Timer2 for use with the CCP and PWM modules.

26.3   External Reset Sources
       In addition to the clock source, the Timer2 can also be driven by an external Reset source input. This
       external Reset input is selected for each timer with the corresponding TxRST register. The external
       Reset input can control starting and stopping of the timer, as well as resetting the timer, depending
       on the mode used.

26.4   Timer2 Interrupt
       Timer2 can also generate a device interrupt. The interrupt is generated when the postscaler counter
       matches the selected postscaler value (OUTPS bits of T2CON register). The interrupt is enabled by
       setting the TMR2IE interrupt enable bit. Interrupt timing is illustrated in the figure below.

       Figure 26-2. Timer2 Prescaler, Postscaler, and Interrupt Timing Diagram

                                                                                                                              Rev. 10-000 205B
                                                                                                                                      3/6/201 9


                  CKPS                                                          ‘b010

                  TxPR                                                            1

                OUTPS                                                         ‘b0001

              TMRx_clk

                TxTMR           0                1               0                1                 0   1                 0

         TMRx_postscaled

                                                          (1)                      (2)                              (1)
                TMRxIF


                 Notes: 1. Setting the interrupt flag is synchronized with the instruction clock.
                           Synchronization may take as many as two instruction cycles.
                        2. Cleared by software.


26.5   PSYNC Bit
       Setting the PSYNC bit synchronizes the prescaler output to FOSC/4. Setting this bit is required for
       reading the Timer2 counter register while the selected Timer clock is asynchronous to FOSC/4.
       Note: Setting PSYNC requires that the output of the prescaler is slower than FOSC/4. Setting PSYNC
       when the output of the prescaler is greater than or equal to FOSC/4 may cause unexpected results.

26.6   CSYNC Bit
       All bits in the Timer2 SFRs are synchronized to FOSC/4 by default, not the Timer2 input clock. As such,
       if the Timer2 input clock is not synchronized to FOSC/4, it is possible for the Timer2 input clock to
       transition at the same time as the ON bit is set in software, which may cause undesirable behavior
       and glitches in the counter. Setting the CSYNC bit remedies this problem by synchronizing the ON
       bit to the Timer2 input clock instead of FOSC/4. However, as this synchronization uses an edge of the
       TMR2 input clock, up to one input clock cycle will be consumed and not counted by the Timer2 when


--- p404 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                                           TMR2 - Timer2 Module

          CSYNC is set. Conversely, clearing the CSYNC bit synchronizes the ON bit to FOSC/4, which does not
          consume any clock edges but has the previously stated risk of glitches.

26.7      Operating Modes
          The mode of the timer is controlled by the MODE bits. Edge Triggered modes require six Timer clock
          periods between external triggers. Level Triggered modes require the triggering level to be at least
          three Timer clock periods long. External triggers are ignored while in Debug mode.

  Table 26-1. Operating Modes Table
                       MODE              Output                                                       Timer Control
          Mode                          Operation                 Operation
                      [4:3] [2:0]                                                         Start          Reset           Stop
                                                            Software gate (Figure        ON = 1            —            ON = 0
                            000
                                                                    26-3)
                                                            Hardware gate, active-      ON = 1 and         —           ON = 0 or
                            001        Period Pulse                 high               TMRx_ers = 1                   TMRx_ers = 0
                                                                (Figure 26-4)
                                                                                        ON = 1 and         —           ON = 0 or
                            010                            Hardware gate, active-low
                                                                                       TMRx_ers = 0                   TMRx_ers = 1
       Free-Running                                          Rising or falling edge                   TMRx_ers ↕
                       00 011
          Period                                                      Reset
                                                           Rising edge Reset (Figure                  TMRx_ers ↑        ON = 0
                            100
                                       Period Pulse                   26-5)
                            101            with                Falling edge Reset        ON = 1       TMRx_ers ↓
                                      Hardware Reset                                                                   ON = 0 or
                            110                                 Low-level Reset                       TMRx_ers = 0
                                                                                                                      TMRx_ers = 0
                                                            High-level Reset (Figure                                   ON = 0 or
                            111                                                                       TMRx_ers = 1
                                                                     26-6)                                            TMRx_ers = 1
                                         One-shot            Software start (Figure      ON = 1            —
                            000
                                                                    26-7)
                                                           Rising edge start (Figure   ON = 1 and
                            001                                                                            —
                                                                    26-8)              TMRx_ers ↑
                                    Edge-Triggered Start                               ON = 1 and
                            010                                Falling edge start                          —
                                          (Note 1)                                     TMRx_ers ↓
                                                                                       ON = 1 and
                            011                                 Any edge start                             —            ON = 0
                                                                                       TMRx_ers ↕
                                                                                                                         or
                                                             Rising edge start and                           Next clock after
        One Shot       01                                                              ON = 1 and
                            100                            Rising edge Reset (Figure              TMRx_ers ↑
                                                                                       TMRx_ers ↑            TxTMR = TxPR
                                                                     26-9)
                                    Edge-Triggered Start                                                                (Note 2)
                                                             Falling edge start and    ON = 1 and
                            101                                                                   TMRx_ers ↓
                                            and                Falling edge Reset      TMRx_ers ↓
                                      Hardware Reset         Rising edge start and
                                                                                       ON = 1 and
                            110           (Note 1)          Low-level Reset (Figure               TMRx_ers = 0
                                                                                       TMRx_ers ↑
                                                                     26-10)
                                                             Falling edge start and    ON = 1 and
                            111                                                                   TMRx_ers = 1
                                                                High-level Reset       TMRx_ers ↓


--- p405 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                        TMR2 - Timer2 Module

  ...........continued
                         MODE            Output                                                    Timer Control
         Mode                           Operation                Operation
                     [4:3] [2:0]                                                          Start       Reset           Stop
                              000                                             Reserved
                                                             Rising edge start       ON = 1 and
                              001                                                                      —              ON = 0
                                                              (Figure 26-11)         TMRx_ers ↑
                                                                                                                       or
       Monostable                   Edge-Triggered Start                              ON = 1 and
                              010                            Falling edge start                        —         Next clock after
                                          (Note 1)                                    TMRx_ers ↓
                                                                                                                   TxTMR = TxPR
                                                                                      ON = 1 and
                              011                              Any edge start                          —             (Note 3)
                                                                                      TMRx_ers ↕
                         10
        Reserved              100                                             Reserved
        Reserved              101                                             Reserved
                                                            High-level start and
                                      Level-Triggered                                ON = 1 and
                              110                          Low-level Reset (Figure               TMRx_ers = 0  ON = 0 or
                                           Start                                    TMRx_ers = 1
        One Shot                                                   26-12)                                     Held in Reset
                                            and
                                                            Low-level start and       ON = 1 and                     (Note 2)
                              111     Hardware Reset                                              TMRx_ers = 1
                                                             High-level Reset        TMRx_ers = 0
        Reserved         11 xxx                                               Reserved

         Notes:
         1. If ON = 0, then an edge is required to restart the timer after ON = 1.
         2. When T2TMR = T2PR, the next clock clears ON and stops T2TMR at 00h.
         3. When T2TMR = T2PR, the next clock stops T2TMR at 00h but does not clear ON.

26.8     Operation Examples
         Unless otherwise specified, the following notes apply to the following timing diagrams:
         •   Both the prescaler and postscaler are set to 1:1 (both the CKPS and OUTPS bits).
         •   The diagrams illustrate any clock except FOSC/4 and show clock-sync delays of at least two
             full cycles for both ON and TMRx_ers. When using FOSC/4, the clock-sync delay is at least one
             instruction period for TMRx_ers; ON applies in the next instruction period.
         •   ON and TMRx_ers are somewhat generalized, and clock-sync delays may produce results that are
             slightly different than illustrated.
         •   The PWM Duty Cycle and PWM output are illustrated assuming that the timer is used for the
             PWM function of the CCP module as described in the “PWM Overview” section in the “CCP -
             Capture/Compare/PWM Module” chapter. The signals are not a part of the Timer2 module.

26.8.1 Software Gate Mode
         This mode corresponds to legacy Timer2 operation. The timer increments with each clock input
         when ON = 1 and does not increment when ON = 0. When the TxTMR count equals the TxPR period
         count, the timer resets on the next clock and continues counting from zero. Operation with the ON
         bit software controlled is illustrated in Figure 26-3. With TxPR = 5, the counter advances until TxTMR
         = 5 and goes to zero with the next clock.


--- p406 ---
                                                                                                                                       PIC18F27/47/57Q43
                                                                                                                                     TMR2 - Timer2 Module

       Figure 26-3. Software Gate Mode Timing Diagram (MODE = ‘b00000)

                                                                                                                                                          Rev. 10-000 195C
                                                                                                                                                                  3/6/201 9


                   TMRx_clk

                 Instruction(1)     BSF                                                                      BCF           BSF


                          ON

                        TxPR                                                             5

                      TxTMR        0      1   2       3   4   5   0    1   2   3     4       5   0   1             2             3    4         5         0        1

             TMRx_postscaled


                 PWM Duty
                                                                                         3
                   Cycle

               PWM Output

                    Note: 1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                          set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.


26.8.2 Hardware Gate Mode
       The Hardware Gate modes operate the same as the Software Gate mode, except the TMRx_ers
       external signal can also gate the timer. When used with the CCP, the gating extends the PWM period.
       If the timer is stopped when the PWM output is high, then the duty cycle is also extended.
       When MODE = ‘b00001, then the timer is stopped when the external signal is high. When MODE =
       ‘b00010, then the timer is stopped when the external signal is low.
       Figure 26-4 illustrates the Hardware Gating mode for MODE = ‘b00001 in which a high input level
       starts the counter.

       Figure 26-4. Hardware Gate Mode Timing Diagram (MODE = ‘b00001)

                                                                                                                                     Rev. 10-000 196C
                                                                                                                                             3/6/201 9


                            TMRx_clk

                            TMRx_ers

                                  TxPR                                                   5

                                  TxTMR           0           1   2    3   4   5     0       1           2             3    4    5     0         1

                   TMRx_postscaled


                          PWM Duty
                                                                                         3
                            Cycle

                      PWM Output


--- p407 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                                    TMR2 - Timer2 Module

26.8.3 Edge Triggered Hardware Limit Mode
       In Hardware Limit mode, the timer can be reset by the TMRx_ers external signal before the timer
       reaches the period count. Three types of Resets are possible:
       •   Reset on rising or falling edge (MODE = ‘b00011)
       •   Reset on rising edge (MODE = ‘b00100)
       •   Reset on falling edge (MODE = ‘b00101)
       When the timer is used in conjunction with the CCP in PWM mode then an early Reset shortens the
       period and restarts the PWM pulse after a two clock delay. Refer to Figure 26-5.

       Figure 26-5. Edge Triggered Hardware Limit Mode Timing Diagram (MODE = ‘b00100)

                                                                                                                        Rev. 10-000197C
                                                                                                                                3/6/2019


                        TMRx_clk

                             TxPR                                           5

                      Instruction(1)         BSF                                            BCF   BSF


                               ON

                        TMRx_ers

                          TxTMR          0         1   2    0      1   2    3   4   5   0     1         2   3   4   5   0         1

                  TMRx_postscaled


                       PWM Duty
                                                                                3
                        Cycle

                     PWM Output


                            Note:      1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by
                                          the CPU to set or clear the ON bit of TxCON. CPU execution is asynchronous
                                          to the timer clock input.


--- p408 ---
                                                                                                                        PIC18F27/47/57Q43
                                                                                                                      TMR2 - Timer2 Module

26.8.4 Level Triggered Hardware Limit Mode
       In the Level Triggered Hardware Limit Timer modes the counter is reset by high or low levels of the
       external signal TMRx_ers, as shown in Figure 26-6. Selecting MODE = ‘b00110 will cause the timer
       to reset on a low-level external signal. Selecting MODE = ‘b00111 will cause the timer to reset on a
       high-level external signal. In the example, the counter is reset while TMRx_ers = 1. ON is controlled
       by BSF and BCF instructions. When ON = 0, the external signal is ignored.
       When the CCP uses the timer as the PWM time base, then the PWM output will be set high when
       the timer starts counting and then set low only when the timer count matches the CCPRx value. The
       timer is reset when either the timer count matches the TxPR value or two clock periods after the
       external Reset signal goes true and stays true.
       The timer starts counting, and the PWM output is set high on either the clock following the TxPR
       match or two clocks after the external Reset signal relinquishes the Reset. The PWM output will
       remain high until the timer counts up to match the CCPRx pulse-width value. If the external Reset
       signal goes true while the PWM output is high, then the PWM output will remain high until the Reset
       signal is released allowing the timer to count up to match the CCPRx value.

       Figure 26-6. Level Triggered Hardware Limit Mode Timing Diagram (MODE = ‘b00111)

                                                                                                                                  Rev. 10-000 198C
                                                                                                                                          3/5/201 9


                  TMRx_clk

                       TxPR                                                                 5

                Instruction(1)         BSF                                        BCF           BSF


                         ON

                  TMRx_ers

                     TxTMR         0         1   2           0        1   2   3             4         5   0   0   1   2   3   4   5         0

           TMRx_postscaled


                PWM Duty
                                                                                        3
                  Cycle

              PWM Output

                     Note:       1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                    set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.


--- p409 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                               TMR2 - Timer2 Module

26.8.5 Software Start One Shot Mode
       In One Shot mode, the timer resets and the ON bit is cleared when the timer value matches the
       TxPR period value. The ON bit must be set by software to start another timer cycle. Setting MODE =
       ‘b01000 selects One Shot mode which is illustrated in Figure 26-7. In the example, ON is controlled
       by BSF and BCF instructions. In the first case, a BSF instruction sets ON and the counter runs
       to completion and clears ON. In the second case, a BSF instruction starts the cycle, the BCF/BSF
       instructions turn the counter off and on during the cycle, and then it runs to completion.
       When One Shot mode is used in conjunction with the CCP PWM operation, the PWM pulse drive
       starts concurrent with setting the ON bit. Clearing the ON bit while the PWM drive is active will
       extend the PWM drive. The PWM drive will terminate when the timer value matches the CCPRx
       pulse-width value. The PWM drive will remain off until the software sets the ON bit to start another
       cycle. If the software clears the ON bit after the CCPRx match but before the TxPR match, then the
       PWM drive will be extended by the length of time the ON bit remains cleared. Another timing cycle
       can only be initiated by setting the ON bit after it has been cleared by a TxPR period count match.

       Figure 26-7. Software Start One Shot Mode Timing Diagram (MODE = ‘b01000)

                                                                                                                    Rev. 10-000 199C
                                                                                                                            3/6/201 9


                     TMRx_clk

                           TxPR                                                  5

                   Instruction(1)      BSF                                 BSF        BCF       BSF


                            ON

                          TxTMR         0         1   2   3   4   5          0        1     2     3       4   5          0

               TMRx_postscaled


                    PWM Duty
                                                                                 3
                      Cycle

                 PWM Output

                  Note:    1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU
                              to set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.


--- p410 ---
                                                                                                                     PIC18F27/47/57Q43
                                                                                                                   TMR2 - Timer2 Module

26.8.6 Edge Triggered One Shot Mode
       The Edge Triggered One Shot modes start the timer on an edge from the external signal input after
       the ON bit is set and clear the ON bit when the timer matches the TxPR period value. The following
       edges will start the timer:
       •   Rising edge (MODE = ‘b01001)
       •   Falling edge (MODE = ‘b01010)
       •   Rising or Falling edge (MODE = ‘b01011)
       If the timer is halted by clearing the ON bit, then another TMRx_ers edge is required after the ON bit
       is set to resume counting. Figure 26-8 illustrates operation in the rising edge One Shot mode.
       When Edge Triggered One Shot mode is used in conjunction with the CCP, then the edge-trigger
       will activate the PWM drive and the PWM drive will deactivate when the timer matches the CCPRx
       pulse-width value and stay deactivated when the timer halts at the TxPR period count match.

       Figure 26-8. Edge Triggered One Shot Mode Timing Diagram (MODE = ‘b01001)

                                                                                                                             Rev. 10-000 200C
                                                                                                                                     3/6/201 9


                  TMRx_clk

                       TxPR                                                       5

                Instruction(1)       BSF                                               BSF                BCF


                         ON

                  TMRx_ers

                     TxTMR              0         1   2   3   4   5                   0                   1             2

                  CCP_pset

            TMRx_postscaled

                 PWM Duty
                                                                                  3
                   Cycle

              PWM Output

                    Note:        1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                    set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.


--- p411 ---
                                                                                                                             PIC18F27/47/57Q43
                                                                                                                           TMR2 - Timer2 Module

26.8.7 Edge Triggered Hardware Limit One Shot Mode
       In Edge Triggered Hardware Limit One Shot modes, the timer starts on the first external signal edge
       after the ON bit is set and resets on all subsequent edges. Only the first edge after the ON bit is
       set is needed to start the timer. The counter will resume counting automatically two clocks after all
       subsequent external Reset edges. Edge triggers are as follows:
       •    Rising edge start and Reset (MODE = ‘b01100)
       •    Falling edge start and Reset (MODE = ‘b01101)
       The timer resets and clears the ON bit when the timer value matches the TxPR period value. External
       signal edges will have no effect until after software sets the ON bit. Figure 26-9 illustrates the rising
       edge hardware limit one-shot operation.
       When this mode is used in conjunction with the CCP, the first starting edge trigger and all
       subsequent Reset edges will activate the PWM drive. The PWM drive will deactivate when the timer
       matches the CCPRx pulse-width value and stay deactivated until the timer halts at the TxPR period
       match unless an external signal edge resets the timer before the match occurs.

       Figure 26-9. Edge Triggered Hardware Limit One Shot Mode Timing Diagram (MODE = ‘b01100)

                                                                                                                                           Rev. 10-000 201C
                                                                                                                                                   3/6/201 9


                 TMRx_clk

                      TxPR                                                               5

               Instruction(1)       BSF                                            BSF


                        ON

                 TMRx_ers

                    TxTMR                 0         1   2   3   4   5               0               1   2     0    1   2   3   4     5     0

           TMRx_postscaled


                PWM Duty
                                                                                         3
                  Cycle

             PWM Output


                                Note: 1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                      set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.


--- p412 ---
                                                                                                                                 PIC18F27/47/57Q43
                                                                                                                               TMR2 - Timer2 Module

26.8.8 Level Reset, Edge Triggered Hardware Limit One Shot Modes
       In Level Triggered One Shot mode, the timer count is reset on the external signal level and starts
       counting on the rising/falling edge of the transition from Reset level to the active level while the ON
       bit is set. Reset levels are selected as follows:
       •    Low Reset level (MODE = ‘b01110)
       •    High Reset level (MODE = ‘b01111)
       When the timer count matches the TxPR period count, the timer is reset and the ON bit is cleared.
       When the ON bit is cleared by either a TxPR match or by software control, a new external signal edge
       is required after the ON bit is set to start the counter.
       When Level-Triggered Reset One Shot mode is used in conjunction with the CCP PWM operation,
       the PWM drive goes active with the external signal edge that starts the timer. The PWM drive goes
       inactive when the timer count equals the CCPRx pulse-width count. The PWM drive does not go
       active when the timer count clears at the TxPR period count match.

       Figure 26-10. Low Level Reset, Edge Triggered Hardware Limit One Shot Mode Timing Diagram (MODE =
       ‘b01110)

                                                                                                                                               Rev. 10-000 202C
                                                                                                                                                       3/6/201 9


                 TMRx_clk

                      TxPR                                                                   5

               Instruction(1)       BSF                                        BSF


                        ON

                 TMRx_ers

                    TxTMR                 0         1   2   3   4   5                0              1          0       1   2   3     4   5     0

           TMRx_postscaled


                PWM Duty
                                                                                         3
                  Cycle

             PWM Output


                                Note: 1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                      set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.


26.8.9 Edge Triggered Monostable Modes
       The Edge Triggered Monostable modes start the timer on an edge from the external Reset signal
       input after the ON bit is set and stop incrementing the timer when the timer matches the TxPR
       period value. The following edges will start the timer:
       •    Rising edge (MODE = ‘b10001)
       •    Falling edge (MODE = ‘b10010)
       •    Rising or Falling edge (MODE = ‘b10011)
       When an Edge Triggered Monostable mode is used in conjunction with the CCP PWM operation, the
       PWM drive goes active with the external Reset signal edge that starts the timer but will not go active
       when the timer matches the TxPR value. While the timer is incrementing, additional edges on the
       external Reset signal will not affect the CCP PWM.


--- p413 ---
                                                                                                                                                           PIC18F27/47/57Q43
                                                                                                                                                         TMR2 - Timer2 Module

       Figure 26-11. Rising Edge Triggered Monostable Mode Timing Diagram (MODE = ‘b10001)
                                                                                                                                                                                     Rev. 10-000203B
                                                                                                                                                                                             3/6/2019


                 TMRx_clk

                      TxPR                                                                                  5

               Instruction(1)          BSF                                                                           BCF       BSF                       BCF        BSF


                        ON

                 TMRx_ers

                    TxTMR                    0         1    2   3    4   5           0         1    2   3   4    5                       0           1    2    3         4   5            0

           TMRx_postscaled


                PWM Duty
                                                                                 3
                  Cycle

             PWM Output


                    Note: 1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                          set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.


26.8.10 Level Triggered Hardware Limit One Shot Modes
       The Level Triggered Hardware Limit One Shot modes hold the timer in Reset on an external Reset
       level and start counting when both the ON bit is set and the external signal is not at the Reset level.
       If one of either the external signal is not in Reset or the ON bit is set, then the other signal being
       set/made active will start the timer. Reset levels are selected as follows:
       •     Low Reset level (MODE = ‘b10110)
       •     High Reset level (MODE = ‘b10111)
       When the timer count matches the TxPR period count, the timer is reset and the ON bit is cleared.
       When the ON bit is cleared by either a TxPR match or by software control, the timer will stay in Reset
       until both the ON bit is set and the external signal is not at the Reset level.
       When Level Triggered Hardware Limit One Shot modes are used in conjunction with the CCP PWM
       operation, the PWM drive goes active with either the external signal edge or the setting of the ON
       bit, whichever of the two starts the timer.

       Figure 26-12. Level Triggered Hardware Limit One Shot Mode Timing Diagram (MODE = ‘b10110)
                                                                                                                                                                                 Rev. 10-000 204B
                                                                                                                                                                                         3/6/201 9


                 TMRx_clk

                      TxPR                                                                                  5

                             (1)
               Instruction                   BSF                                              BSF                                                        BCF       BSF


                        ON

                 TMRx_ers

                    TxTMR                    0          1   2   3    4   5                     0                           1   2     3       0   1   2              3        4        5         0

           TMRx_postscaled


                PWM Duty
                                                                                                            D3
                  Cycle

             PWM Output

                                   Note: 1. BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                          set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.


--- p414 ---
                                                                                                     PIC18F27/47/57Q43
                                                                                                   TMR2 - Timer2 Module

26.9   Timer2 Operation During Sleep
       When PSYNC = 1, Timer2 cannot be operated while the processor is in Sleep mode. The contents of
       the T2TMR and T2PR registers will remain unchanged while the processor is in Sleep mode.
       When PSYNC = 0, Timer2 will operate in Sleep as long as the clock source selected is also still
       running. If any internal oscillator is selected as the clock source, it will stay active during Sleep mode.

26.10 Register Definitions: Timer2 Control
       Long bit name prefixes for the Timer2 peripherals are shown in the table below. Refer to the “Long
       Bit Names” section of the “Register and Bit Naming Conventions” chapter for more information.

       Table 26-2. Timer2 Long Bit Name Prefixes
                         Peripheral                                              Bit Name Prefix
                          Timer2                                                         T2
                          Timer4                                                         T4
                          Timer6                                                         T6


                    Important: References to module Timer2 apply to all the even numbered timers
                    on this device (Timer2, Timer4, etc.).


--- p415 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                                TMR2 - Timer2 Module

26.10.1 TxTMR

           Name:      TxTMR
           Address:   0x322,0x32E,0x33A
           Timer Counter Register

     Bit        7           6           5             4           3                    2    1              0
                                                       TxTMR[7:0]
  Access       R/W         R/W         R/W          R/W         R/W               R/W      R/W            R/W
   Reset        0           0           0            0            0                0        0              0

Bits 7:0 – TxTMR[7:0] Timerx Counter


--- p416 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                                       TMR2 - Timer2 Module

26.10.2 TxPR

            Name:       TxPR
            Address:    0x323,0x32F,0x33B
            Timer Period Register

      Bit        7             6               5              4                   3           2    1              0
                                                                   TxPR[7:0]
  Access        R/W           R/W            R/W            R/W                  R/W     R/W      R/W            R/W
   Reset         1             1              1              1                    1       1        1              1

Bits 7:0 – TxPR[7:0] Timer Period Register
            Value      Description
            0 to 255   The timer restarts at ‘0’ when TxTMR reaches the TxPR value


--- p417 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                        TMR2 - Timer2 Module

26.10.3 TxCON

            Name:       TxCON
            Address:    0x324,0x330,0x33C
            Timerx Control Register

      Bit        7              6             5                 4                   3          2        1          0
                ON                         CKPS[2:0]                                         OUTPS[3:0]
  Access      R/W/HC          R/W            R/W              R/W                  R/W    R/W         R/W         R/W
   Reset         0             0              0                0                    0      0            0          0

Bit 7 – ON Timer On(1)
            Value      Description
            1          Timer is on
            0          Timer is off: All counters and state machines are reset

Bits 6:4 – CKPS[2:0] Timer Clock Prescale Select
            Value      Description
            111        1:128 Prescaler
            110        1:64 Prescaler
            101        1:32 Prescaler
            100        1:16 Prescaler
            011        1:8 Prescaler
            010        1:4 Prescaler
            001        1:2 Prescaler
            000        1:1 Prescaler

Bits 3:0 – OUTPS[3:0] Timer Output Postscaler Select
            Value      Description
            1111       1:16 Postscaler
            1110       1:15 Postscaler
            1101       1:14 Postscaler
            1100       1:13 Postscaler
            1011       1:12 Postscaler
            1010       1:11 Postscaler
            1001       1:10 Postscaler
            1000       1:9 Postscaler
            0111       1:8 Postscaler
            0110       1:7 Postscaler
            0101       1:6 Postscaler
            0100       1:5 Postscaler
            0011       1:4 Postscaler
            0010       1:3 Postscaler
            0001       1:2 Postscaler
            0000       1:1 Postscaler

            Note:
            1. In certain modes, the ON bit will be auto-cleared by hardware. See Table 26-1.


--- p418 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                                          TMR2 - Timer2 Module

26.10.4 TxHLT

            Name:       TxHLT
            Address:    0x325,0x331,0x33D

            Timer Hardware Limit Control Register

      Bit        7             6               5                4                   3       2         1              0
               PSYNC         CPOL            CSYNC                                       MODE[4:0]
  Access        R/W          R/W              R/W             R/W                  R/W     R/W       R/W            R/W
   Reset         0             0               0               0                    0       0         0              0

Bit 7 – PSYNC Timer Prescaler Synchronization Enable(1, 2)
            Value      Description
            1          Timer Prescaler Output is synchronized to FOSC/4
            0          Timer Prescaler Output is not synchronized to FOSC/4

Bit 6 – CPOL Timer Clock Polarity Selection(3)
            Value      Description
            1          Falling edge of input clock clocks timer/prescaler
            0          Rising edge of input clock clocks timer/prescaler

Bit 5 – CSYNC Timer Clock Synchronization Enable(4, 5)
            Value      Description
            1          ON bit is synchronized to timer clock input
            0          ON bit is not synchronized to timer clock input

Bits 4:0 – MODE[4:0] Timer Control Mode Selection(6, 7)
            Value      Description
            00000 to   See Table 26-1
            11111


            Notes:
            1. Setting this bit ensures that reading TxTMR will return a valid data value.
            2. When this bit is ‘1’, the Timer cannot operate in Sleep mode.
            3. CKPOL must not be changed while ON = 1.
            4. Setting this bit ensures glitch-free operation when the ON is enabled or disabled.
            5. When this bit is set, then the timer operation will be delayed by two input clocks after the ON bit
               is set.
            6. Unless otherwise indicated, all modes start upon ON = 1 and stop upon ON = 0 (stops occur
               without affecting the value of TxTMR).
            7. When TxTMR = TxPR, the next clock clears TxTMR, regardless of the operating mode.


--- p419 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                        TMR2 - Timer2 Module

26.10.5 TxCLKCON

            Name:      TxCLKCON
            Address:   0x326,0x332,0x33E

            Timer Clock Source Selection Register

      Bit         7           6                  5          4                   3        2          1               0
                                                                                       CS[4:0]
  Access                                                  R/W                  R/W      R/W        R/W             R/W
   Reset                                                   0                    0        0          0               0

Bits 4:0 – CS[4:0] Timer Clock Source Selection

   Table 26-3. Clock Source Selection
                                                                         Clock Source
             CS
                                        Timer2                              Timer4                        Timer6
      11111-10110                                                          Reserved
         10101                                                            CLC8_OUT
         10100                                                            CLC7_OUT
         10011                                                            CLC6_OUT
         10010                                                            CLC5_OUT
         10001                                                            CLC4_OUT
         10000                                                            CLC3_OUT
         01111                                                            CLC2_OUT
         01110                                                            CLC1_OUT
         01101                                                             ZCD_OUT
         01100                                                            NCO3_OUT
         01011                                                            NCO2_OUT
         01010                                                            NCO1_OUT
         01001                                                           CLKREF_OUT
         01000                                                              EXTOSC
         00111                                                               SOSC
         00110                                                      MFINTOSC (31.25 kHz)
         00101                                                       MFINTOSC (500 kHz)
         00100                                                             LFINTOSC
         00011                                                            HFINTOSC
         00010                                                                FOSC
         00001                                                               FOSC/4
         00000               Pin selected by T2INPPS               Pin selected by T4INPPS       Pin selected by T6INPPS


--- p420 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                                         TMR2 - Timer2 Module

26.10.6 TxRST

            Name:       TxRST
            Address:    0x327,0x333,0x33F
            Timer External Reset Signal Selection Register

      Bit        7            6            5             4                   3                 2     1              0
                                                                                  RSEL[5:0]
  Access                                 R/W           R/W                  R/W               R/W   R/W            R/W
   Reset                                  0             0                    0                 0     0              0

Bits 5:0 – RSEL[5:0] External Reset Source Selection

   Table 26-4. External Reset Sources
                                                                     Reset Source
              RSEL
                                        TMR2                             TMR4                               TMR6
      111111-100100                                                    Reserved
          100011                                              U5TX_Edge (Positive/Negative)
          100010                                              U5RX_Edge (Positive/Negative)
          100001                                              U4TX_Edge (Positive/Negative)
          100000                                              U4RX_Edge (Positive/Negative)
          011111                                              U3TX_Edge (Positive/Negative)
          011110                                              U3RX_Edge (Positive/Negative)
          011101                                              U2TX_Edge (Positive/Negative)
          011100                                              U2RX_Edge (Positive/Negative)
          011011                                              U1TX_Edge (Positive/Negative)
          011010                                              U1RX_Edge (Positive/Negative)
          011001                                                      CLC8_OUT
          011000                                                      CLC7_OUT
          010111                                                      CLC6_OUT
          010110                                                      CLC5_OUT
          010101                                                      CLC4_OUT
          010100                                                      CLC3_OUT
          010011                                                      CLC2_OUT
          010010                                                      CLC1_OUT
          010001                                                       ZCD_OUT
          010000                                                      CMP2_OUT
          001111                                                      CMP1_OUT
          001110                                                       Reserved
          001101                                                       Reserved
          001100                                                   PWM3S1P2_OUT
          001011                                                   PWM3S1P1_OUT
          001010                                                   PWM2S1P2_OUT
          001001                                                   PWM2S1P1_OUT
          001000                                                   PWM1S1P2_OUT
          000111                                                   PWM1S1P1_OUT
          000110                                                      CCP3_OUT
          000101                                                      CCP2_OUT
          000100                                                      CCP1_OUT


--- p421 ---
                                                                                         PIC18F27/47/57Q43
                                                                                       TMR2 - Timer2 Module

...........continued
                                                            Reset Source
         RSEL
                             TMR2                              TMR4                      TMR6
       000011          TMR6_Postscaler_OUT               TMR6_Postscaler_OUT            Reserved
       000010          TMR4_Postscaler_OUT                    Reserved             TMR4_Postscaler_OUT
       000001                  Reserved                  TMR2_Postscaler_OUT        TMR2_Postscaler_OUT
       000000          Pin selected by T2INPPS          Pin selected by T4INPPS    Pin selected by T6INPPS


--- p422 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                                  TMR2 - Timer2 Module

26.11 Register Summary - Timer2
Address    Name      Bit Pos.     7          6            5             4                3             2                1          0
 0x0322    T2TMR       7:0                                                  T2TMR[7:0]
 0x0323     T2PR       7:0                                                   T2PR[7:0]
 0x0324    T2CON       7:0       ON                   CKPS[2:0]                                            OUTPS[3:0]
0x0325      T2HLT      7:0      PSYNC      CPOL        CSYNC                                       MODE[4:0]
0x0326    T2CLKCON     7:0                                                                           CS[4:0]
0x0327      T2RST      7:0                                                                   RSEL[5:0]
0x0328
  ...     Reserved
0x032D
0x032E      T4TMR      7:0                                                  T4TMR[7:0]
0x032F       T4PR      7:0                                                   T4PR[7:0]
0x0330      T4CON      7:0       ON                   CKPS[2:0]                                           OUTPS[3:0]
0x0331      T4HLT      7:0      PSYNC      CPOL        CSYNC                                       MODE[4:0]
0x0332    T4CLKCON     7:0                                                                           CS[4:0]
0x0333      T4RST      7:0                                                                   RSEL[5:0]
0x0334
  ...     Reserved
0x0339
0x033A      T6TMR      7:0                                                  T6TMR[7:0]
0x033B       T6PR      7:0                                                   T6PR[7:0]
0x033C      T6CON      7:0       ON                   CKPS[2:0]                                           OUTPS[3:0]
0x033D      T6HLT      7:0      PSYNC      CPOL        CSYNC                                       MODE[4:0]
0x033E    T6CLKCON     7:0                                                                           CS[4:0]
0x033F      T6RST      7:0                                                                   RSEL[5:0]


--- p423 ---
