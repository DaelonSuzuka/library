                         PIC18(L)F26/27/45/46/47/55/56/57K42
22.0     TIMER2/4/6 MODULE                                                  • Three modes of operation:
                                                                              - Free Running Period
The Timer2/4/6 modules are 8-bit timers that can
                                                                              - One-Shot
operate as free-running period counters or in
conjunction with external signals that control start, run,                    - Monostable
freeze, and reset operation in One-Shot and                                 See Figure 22-1 for a block diagram of Timer2. See
Monostable modes of operation. Sophisticated                                Figure 22-2 for the clock source block diagram.
waveform control such as pulse density modulation are
possible by combining the operation of these timers                            Note:     Three identical Timer2 modules are
with other internal peripherals such as the comparators                                  implemented on this device. The timers are
and CCP modules. Features of the timer include:                                          named Timer2, Timer4, and Timer6. All
                                                                                         references to Timer2 apply as well to
• 8-bit timer register                                                                   Timer4 and Timer6. All references to T2PR
• 8-bit period register                                                                  apply as well to T4PR and T6PR.
• Selectable external hardware timer resets
• Programmable prescaler (1:1 to 1:128)
• Programmable postscaler (1:1 to 1:16)
• Selectable synchronous/asynchronous operation
• Alternate clock sources
• Interrupt on period

FIGURE 22-1:                 TIMER2 BLOCK DIAGRAM
           RSEL <4:0>                                                                                                        Rev. 10-000168D
                                                                                                                                    9/12/2016


         TxINPPS
         TxIN    PPS                        MODE<4:0>                                                 MODE<3>


                                            Edge Detector    reset
                External
                                 TMRx_ers   Level Detector                                                                 CCP_pset(1)
                 Reset
                       (2)                  Mode Control
                Sources                     (2 clock Sync)


                                            enable                     MODE<4:3>=01
                                                                                                                              Clear ON
                                                                     MODE<4:1>=1011                                D     Q


            CKPOL
          TMRx_clk                             Prescaler                   0
                                                                                                R
                                                                                        TxTMR
                                                                                                                       Set flag bit
                                                     3          Sync       1                                            TMRxIF

                                             CKPS<2:0>        Fosc/4     PSYNC                                     TMRx_postscaled
                                                                                       Comparator    Postscaler

                                                                                                        4
           ON         Sync
                                  1
                   (2 Clocks)                                                            TxPR       OUTPS<3:0>
                                  0


                                CKSYNC


 2017-2021 Microchip Technology Inc.                                                                             DS40001919G-page 320
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 22-2:           TIMER2 CLOCK SOURCE                  output postscaler counter. When the postscaler count
                       BLOCK DIAGRAM                        equals the value in the OUTPS bits of the TxCON
                                         Rev. 10-000169E
                                                            register, then a one clock period wide pulse occurs on
                                                9/12/2016
                                                            the T2TMR_postscaled output, and the postscaler count
                                                            is cleared.
             CS<3:0>
          TXINPPS                                           22.1.2      ONE SHOT MODE
          TXIN       PPS       0000                         The One Shot mode is identical to the Free Running
                                                            Period mode except that the ON bit is cleared and the
                                                            timer is stopped when T2TMR matches T2PR and will
                                                            not restart until the T2ON bit is cycled off and on.
                                                            Postscaler OUTPS values other than 0 are
                  See                    TMRx_clk
                 TxCLK
                                                            meaningless in this mode because the timer is stopped
                 Register                                   at the first period event and the postscaler is reset
                                                            when the timer is restarted.

                               1111
                                                            22.1.3      MONOSTABLE MODE
                                                            Monostable modes are similar to One Shot modes
                                                            except that the ON bit is not cleared and the timer can
                                                            be restarted by an external Reset event.
22.1      Timer2 Operation
                                                            22.2     Timer2 Output
Timer2 operates in three major modes:
                                                            The     Timer2     module’s     primary     output     is
• Free Running Period
                                                            T2TMR_postscaled, which pulses for a single
• One-Shot                                                  T2TMR_clk period when the postscaler counter
• Monostable                                                matches the value in the OUTPS bits of the TxCON
Within each mode there are several options for starting,    register. The T2PR postscaler is incremented each
stopping, and reset. Table 22-1 lists the options.          time the T2TMR value matches the T2PR value. This
                                                            signal can be selected as an input to several other input
In all modes the T2TMR count register is incremented
                                                            modules.
on the rising edge of the clock signal from the
programmable prescaler. When T2TMR equals T2PR              Timer2 is also used by the CCP module for pulse
then a high level is output to the postscaler counter.      generation in PWM mode. Both the actual T2TMR
T2TMR is cleared on the next clock input.                   value as well as other internal signals are sent to the
                                                            CCP module to properly clock both the period and
An external signal from hardware can also be
                                                            pulse width of the PWM signal. See Section
configured to gate the timer operation or force a
                                                            23.0 “Capture/Compare/PWM Module” for more
T2TMR count Reset. In gate modes, the counter stops
                                                            details on setting up Timer2 for use with the CCP, as
when the gate is disabled and resumes when the gate
                                                            well as the timing diagrams in Section
is enabled. In Reset modes the T2TMR count is reset
                                                            22.5 “Operation Examples” for examples of how the
on either the level or edge from the external source.
                                                            varying Timer2 modes affect CCP PWM output.
The T2TMR and T2PR registers are both directly
readable and writable. The T2TMR register is cleared        22.3     External Reset Sources
and the T2PR register initializes to FFh on any device
Reset. Both the prescaler and postscaler counters are       In addition to the clock source, the Timer2 also takes in
cleared on the following events:                            an external Reset source. This external Reset source
                                                            is selected for Timer2, Timer4, and Timer6 with the
• a write to the T2TMR register
                                                            T2RST, T4RST, and T6RST registers, respectively.
• a write to the TxCON register                             This source can control starting and stopping of the
• any device Reset                                          timer, as well as resetting the timer, depending on
• External Reset Source event that resets the timer.        which mode the timer is in. The mode of the timer is
  Note:     T2TMR is not cleared when TxCON is              controlled by the MODE bits of the T2HLT register.
            written.                                        Edge Triggered modes require six Timer clock periods
                                                            between external triggers. Level Triggered modes
                                                            require the triggering level to be at least three Timer
22.1.1      FREE RUNNING PERIOD MODE
                                                            clock periods long. External triggers are ignored while
The value of T2TMR is compared to that of the Period        in Debug Freeze mode.
register, T2PR, on each clock cycle. When the two
values match, the comparator resets the value of
T2TMR to 00h on the next cycle and increments the


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 321
                       PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 22-1:          TIMER2 OPERATING MODES
                MODE[4:0]        Output                                                            Timer Control
   Mode                                                  Operation
               [4:3]    [2:0]   Operation                                                 Start       Reset             Stop
                        000                     Software gate (Figure 22-4)               ON = 1        —              ON = 0
                                                 Hardware gate, active-high           ON = 1 &          —           ON = 0 or
                        001       Period
                                                      (Figure 22-5)                 TMRx_ers = 1                   TMRx_ers = 0
                                  Pulse
                                                                                      ON = 1 &          —           ON = 0 or
                        010                      Hardware gate, active-low
                                                                                    TMRx_ers = 0                   TMRx_ers = 1
    Free                011                     Rising or Falling Edge Reset                        TMRx_ers ↕
  Running       00
   Period               100      Period       Rising Edge Reset (Figure 22-6)                       TMRx_ers ↑         ON = 0
                        101      Pulse               Falling Edge Reset                             TMRx_ers ↓
                                  with                                                    ON = 1                    ON = 0 or
                        110     Hardware              Low Level Reset                              TMRx_ers = 0
                                                                                                                   TMRx_ers = 0
                                 Reset
                                               High Level Reset (Figure 22-7)                                       ON = 0 or
                        111                                                                        TMRx_ers = 1
                                                                                                                   TMRx_ers = 1
                        000     One-Shot        Software Start (Figure 22-8)              ON = 1        —
                                                                                      ON = 1 &
                        001                    Rising Edge Start (Figure 22-9)                          —
                                  Edge                                               TMRx_ers ↑
                                Triggered                                             ON = 1 &
                        010                          Falling Edge Start                                 —
                                   Start                                             TMRx_ers ↓
                                 (Note 1)                                             ON = 1 &
                        011                           Any Edge Start                                    —              ON =0
                                                                                     TMRx_ers ↕                           or
  One-shot      01                                   Rising Edge Start &              ON = 1 &                     Next clock after
                        100                                                                         TMRx_ers ↑      TMRx = PRx
                                  Edge        Rising Edge Reset (Figure 22-10)       TMRx_ers ↑
                                Triggered                                                                             (Note 2)
                                                    Falling Edge Start &              ON = 1 &
                        101        Start                                                            TMRx_ers ↓
                                                    Falling Edge Reset               TMRx_ers ↓
                                   and
                                Hardware            Rising Edge Start &               ON = 1 &
                        110                                                                        TMRx_ers = 0
                                  Reset        Low Level Reset (Figure 22-11)        TMRx_ers ↑
                                 (Note 1)           Falling Edge Start &              ON = 1 &
                        111                                                                        TMRx_ers = 1
                                                     High Level Reset                TMRx_ers ↓
                        000                                                    Reserved
                                                     Rising Edge Start                ON = 1 &
                        001                                                                             —              ON=0
                                  Edge                (Figure 22-12)                 TMRx_ers ↑
Monostable                                                                                                                or
                                Triggered                                             ON = 1 &
                        010                          Falling Edge Start                                 —          Next clock after
                                   Start                                             TMRx_ers ↓
                                                                                                                   TxTMR = TxPR
                                 (Note 1)                                             ON = 1 &
                        011                           Any Edge Start                                    —             (Note 3)
                                                                                     TMRx_ers ↕
 Reserved       10      100                                                    Reserved
 Reserved               101                                                    Reserved
                                  Level             High Level Start &                ON = 1 &
                        110                                                                        TMRx_ers = 0
                                Triggered     Low Level Reset (Figure 22-13)        TMRx_ers = 1
                                                                                                                     ON = 0 or
                                   Start
  One-shot                                                                                                          Held in Reset
                                   and               Low Level Start &                ON = 1 &
                        111                                                                        TMRx_ers = 1       (Note 2)
                                Hardware             High Level Reset               TMRx_ers = 0
                                  Reset
 Reserved       11      xxx                                                    Reserved
Note 1:      If ON = 0 then an edge is required to restart the timer after ON = 1.
     2:      When TxTMR = TxPR then the next clock clears ON and stops TxTMR at 00h.
     3:      When TxTMR = TxPR then the next clock stops TxTMR at 00h but does not clear ON.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 322
                        PIC18(L)F26/27/45/46/47/55/56/57K42
22.4     Timer2 Interrupt
Timer2 can also generate a device interrupt. The
interrupt is generated when the postscaler counter
matches one of 16 postscale options (from 1:1 through
1:16), which is selected with the postscaler control bits,
OUTPS of the T2CON register. The interrupt is enabled
by setting the T2TMR Interrupt Enable bit, TMR2IE, of
the respective PIE register. The interrupt timing is
illustrated in Figure 22-3.

FIGURE 22-3:             TIMER2 PRESCALER, POSTSCALER, AND INTERRUPT TIMING DIAGRAM

                                                                                                                         Rev. 10-000205B
                                                                                                                                9/12/2016


              CKPS                                                           0b010

              TxPR                                                              1

            OUTPS                                                            0b0001

          TMRx_clk

             TxTMR          0                1                 0                1               0   1                0

     TMRx_postscaled

                                                       (1)                          (2)                        (1)
            TMRxIF


             Note 1:   Setting the interrupt flag is synchronized with the instruction clock.
                       Synchronization may take as many as 2 instruction cycles
                  2:   Cleared by software.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 323
                      PIC18(L)F26/27/45/46/47/55/56/57K42
22.5     Operation Examples
Unless otherwise specified, the following notes apply to
the following timing diagrams:
  - Both the prescaler and postscaler are set to
    1:1 (both the CKPS and OUTPS bits in the
    T2CON register are cleared).
  - The diagrams illustrate any clock except
    FOSC/4 and show clock-sync delays of at
    least two full cycles for both ON and
    T2TMR_ers. When using FOSC/4, the clock-
    sync delay is at least one instruction period
    for T2TMR_ers; ON applies in the next
    instruction period.
  - ON and T2TMR_ers are somewhat
    generalized, and clock-sync delays may
    produce results that are slightly different than
    illustrated.
  - The PWM Duty Cycle and PWM output are
    illustrated assuming that the timer is used for
    the PWM function of the CCP module as
    described in Section 23.0 “Capture/
    Compare/PWM Module” and Section
    24.0 “Pulse-Width Modulation (PWM)”.
    The signals are not a part of the T2TMR
    module.


 2017-2021 Microchip Technology Inc.                      DS40001919G-page 324
                             PIC18(L)F26/27/45/46/47/55/56/57K42
22.5.1       SOFTWARE GATE MODE
The timer increments with each clock input when ON = 1
and does not increment when ON = 0. When the
T2TMR count equals the T2PR period count the timer
resets on the next clock and continues counting from 0.
Operation with the ON bit software controlled is
illustrated in Figure 22-4. With T2PR = 5, the counter
advances until T2TMR = 5, and goes to zero with the
next clock.

FIGURE 22-4:                 SOFTWARE GATE MODE TIMING DIAGRAM
                                                                                                                         Rev. 10-000195C
                                                                                                                                9/12/2016


                 MODE                                                   0b00000

             TMRx_clk

           Instruction (1)    BSF                                                            BCF       BSF


                     ON

                  TxPR                                                       5

                 TxTMR        0     1   2   3   4   5   0   1   2   3    4       5   0   1         2         3   4   5        0         1

    TMRx_postscaled


           PWM Duty
                                                                             3
             Cycle

         PWM Output

              Note     1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                       set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input .


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 325
                      PIC18(L)F26/27/45/46/47/55/56/57K42
22.5.2      HARDWARE GATE MODE
The Hardware Gate modes operate the same as the
Software Gate mode except the T2TMR_ers external
signal can also gate the timer. When used with the CCP
the gating extends the PWM period. If the timer is
stopped when the PWM output is high, then the duty
cycle is also extended.
When MODE[4:0] = 00001, then the timer is stopped
when the external signal is high. When MODE[4:0] =
00010, then the timer is stopped when the external
signal is low.
Figure 22-5 illustrates the Hardware Gating mode for
MODE[4:0] = 00001 in which a high input level starts
the counter.

FIGURE 22-5:           HARDWARE GATE MODE TIMING DIAGRAM (MODE = 00001)

                                                                                           Rev. 10-000196C
                                                                                                  9/12/2016


                     MODE                                 0b00001

                  TMRx_clk

                 TMRx_ers

                      TxPR                                         5

                    TxTMR         0       1   2   3   4    5   0       1   2   3   4   5     0         1

          TMRx_postscaled


                PWM Duty
                                                                   3
                  Cycle

             PWM Output


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 326
                        PIC18(L)F26/27/45/46/47/55/56/57K42
22.5.3      EDGE-TRIGGERED HARDWARE
            LIMIT MODE
In Hardware Limit mode the timer can be reset by the
TMRx_ers external signal before the timer reaches the
period count. Three types of Resets are possible:
• Reset on rising or falling edge
  (MODE[4:0] = 00011)
• Reset on rising edge (MODE[4:0] = 0010)
• Reset on falling edge (MODE[4:0] = 00101)
When the timer is used in conjunction with the CCP in
PWM mode then an early Reset shortens the period
and restarts the PWM pulse after a two clock delay.
Refer to Figure 22-6.

FIGURE 22-6:             EDGE TRIGGERED HARDWARE LIMIT MODE TIMING DIAGRAM (MODE=00100)

                                                                                                                     Rev. 10-000197C
                                                                                                                            9/12/2016


                     MODE                                         0b00100

                 TMRx_clk

                      TxPR                                             5

               Instruction (1)          BSF                                             BCF   BSF


                         ON

                TMRx_ers

                   TxTMR            0         1   2    0      1    2   3    4   5   0     1         2   3   4   5    0         1

          TMRx_postscaled


               PWM Duty
                                                                            3
                 Cycle

             PWM Output


                    Note         1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                 set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input .


 2017-2021 Microchip Technology Inc.                                                                               DS40001919G-page 327
                            PIC18(L)F26/27/45/46/47/55/56/57K42
22.5.4      LEVEL-TRIGGERED HARDWARE                                      When the CCP uses the timer as the PWM time base
            LIMIT MODE                                                    then the PWM output will be set high when the timer
                                                                          starts counting and then set low only when the timer
In the level triggered Hardware Limit Timer modes the
                                                                          count matches the CCPRx value. The timer is reset
counter is reset by high or low levels of the external
                                                                          when either the timer count matches the T2PR value or
signal TMR2_ers, as shown in Figure 22-7. Selecting
                                                                          two clock periods after the external Reset signal goes
MODE[4:0] = 00110 will cause the timer to reset on a
                                                                          true and stays true.
low level external signal. Selecting MODE[4:0] =
00111 will cause the timer to reset on a high level                       The timer starts counting, and the PWM output is set
external signal. In the example, the counter is reset                     high, on either the clock following the T2PR match or
while TMR2_ers = 1. ON is controlled by BSF and BCF                       two clocks after the external Reset signal relinquishes
instructions. When ON=0 the external signal is ignored.                   the Reset. The PWM output will remain high until the
                                                                          timer counts up to match the CCPRx pulse width value.
                                                                          If the external Reset signal goes true while the PWM
                                                                          output is high then the PWM output will remain high
                                                                          until the Reset signal is released allowing the timer to
                                                                          count up to match the CCPRx value.


FIGURE 22-7:                 LEVEL TRIGGERED HARDWARE LIMIT MODE TIMING DIAGRAM
                             (MODE = 00111)

                                                                                                                    Rev. 10-000198C
                                                                                                                           9/12/2016


               MODE                                                      0b00111

           TMRx_clk

                TxPR                                                              5

         Instruction (1)          BSF                                   BCF           BSF


                   ON

           TMRx_ers

              TxTMR           0         1   2      0        1   2   3             4         5   0   0   1   2   3   4         5        0

    TMRx_postscaled


          PWM Duty
                                                                              3
            Cycle

      PWM Output

              Note         1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                           set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input .


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 328
                             PIC18(L)F26/27/45/46/47/55/56/57K42
22.5.5       SOFTWARE START ONE SHOT                                  When One Shot mode is used in conjunction with the
             MODE                                                     CCP PWM operation, the PWM pulse drive starts
                                                                      concurrent with setting the ON bit. Clearing the ON bit
In One Shot mode, the timer resets and the ON bit is
                                                                      while the PWM drive is active will extend the PWM
cleared when the timer value matches the T2PR period
                                                                      drive. The PWM drive will terminate when the timer
value. The ON bit must be set by software to start
                                                                      value matches the CCPRx pulse width value. The
another timer cycle. Setting MODE[4:0] = 01000
                                                                      PWM drive will remain off until software sets the ON bit
selects One Shot mode which is illustrated in
                                                                      to start another cycle. If software clears the ON bit after
Figure 22-8. In the example, ON is controlled by BSF
                                                                      the CCPRx match but before the T2PR match then the
and BCF instructions. In the first case, a BSF
                                                                      PWM drive will be extended by the length of time the
instruction sets ON and the counter runs to completion
                                                                      ON bit remains cleared. Another timing cycle can only
and clears ON. In the second case, a BSF instruction
                                                                      be initiated by setting the ON bit after it has been
starts the cycle, BCF/BSF instructions turn the counter
                                                                      cleared by a T2PR period count match.
off and on during the cycle, and then it runs to
completion.

FIGURE 22-8:                 SOFTWARE START ONE SHOT MODE TIMING DIAGRAM (MODE = 01000)

                                                                                                                Rev. 10-000199C
                                                                                                                       9/12/2016


                 MODE                                            0b01000

             TMRx_clk

                  TxPR                                                5

           Instruction (1)      BSF                             BSF          BCF       BSF


                     ON

                TxTMR           0       1   2   3   4   5         0          1     2     3      4   5       0

     TMRx_postscaled


           PWM Duty
                                                                      3
             Cycle

         PWM Output

                Note 1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions
                        executed by the CPU to set or clear the ON bit of TxCON. CPU
                        execution is asynchronous to the timer clock input.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 329
                                        22.5.6     EDGE-TRIGGERED ONE SHOT MODE                                                       If the timer is halted by clearing the ON bit then another TMRx_ers edge is
 2017-2021 Microchip Technology Inc.


                                                                                                                                      required after the ON bit is set to resume counting. Figure 22-9 illustrates oper-
                                        The Edge-Triggered One Shot modes start the timer on an edge from the                         ation in the rising edge One Shot mode.
                                        external signal input, after the ON bit is set, and clear the ON bit when the
                                                                                                                                      When Edge-Triggered One Shot mode is used in conjunction with the CCP then
                                        timer matches the T2PR period value. The following edges will start the timer:
                                                                                                                                      the edge-trigger will activate the PWM drive and the PWM drive will deactivate
                                        • Rising edge (MODE[4:0] = 01001)
                                                                                                                                      when the timer matches the CCPRx pulse width value and stay deactivated
                                        • Falling edge (MODE[4:0] = 01010)                                                            when the timer halts at the T2PR period count match.
                                        • Rising or Falling edge (MODE[4:0] = 01011)


                                                                                                                                                                                                                           PIC18(L)F26/27/45/46/47/55/56/57K42
                                        FIGURE 22-9:          EDGE TRIGGERED ONE SHOT MODE TIMING DIAGRAM (MODE = 01001)
                                                                                                                                                                                   Rev. 10-000200C
                                                                                                                                                                                          9/12/2016


                                                                               MODE                                                  0b01001

                                                                           TMRx_clk

                                                                                TxPR                                                     5

                                                                         Instruction (1)    BSF                                                BSF               BCF


                                                                                   ON

                                                                           TMRx_ers

                                                                              TxTMR            0         1   2   3   4   5                   0                   1             2

                                                                           CCP_pset

                                                                    TMRx_postscaled
DS40001919G-page 330


                                                                          PWM Duty
                                                                                                                                         3
                                                                            Cycle

                                                                       PWM Output

                                                                             Note      1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                                                                       set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input .
                                        22.5.7      EDGE-TRIGGERED HARDWARE LIMIT ONE SHOT                                                The timer resets and clears the ON bit when the timer value matches the T2PR
 2017-2021 Microchip Technology Inc.


                                                    MODE                                                                                  period value. External signal edges will have no effect until after software sets
                                                                                                                                          the ON bit. Figure 22-10 illustrates the rising edge hardware limit one-shot
                                        In Edge-Triggered Hardware Limit One Shot modes, the timer starts on the                          operation.
                                        first external signal edge after the ON bit is set and resets on all subsequent
                                                                                                                                          When this mode is used in conjunction with the CCP then the first starting edge
                                        edges. Only the first edge after the ON bit is set is needed to start the timer.
                                                                                                                                          trigger, and all subsequent Reset edges, will activate the PWM drive. The PWM
                                        The counter will resume counting automatically two clocks after all subsequent                    drive will deactivate when the timer matches the CCPRx pulse width value and
                                        external Reset edges. Edge triggers are as follows:                                               stay deactivated until the timer halts at the T2PR period match unless an


                                                                                                                                                                                                                              PIC18(L)F26/27/45/46/47/55/56/57K42
                                        • Rising edge Start and Reset                (MODE[4:0] = 01100)                                  external signal edge resets the timer before the match occurs.
                                        • Falling edge Start and Reset                (MODE[4:0] = 01101)


                                        FIGURE 22-10:          EDGE TRIGGERED HARDWARE LIMIT ONE SHOT MODE TIMING DIAGRAM (MODE = 01100))
                                                                                                                                                                                       Rev. 10-000201C
                                                                                                                                                                                              9/12/2016


                                                                  MODE                                                   0b01100

                                                              TMRx_clk

                                                                   TxPR                                                               5

                                                            Instruction(1)      BSF                                             BSF


                                                                     ON

                                                              TMRx_ers

                                                                 TxTMR                0          1   2   3   4   5               0               1    2    0     1   2   3   4     5   0

                                                       TMRx_postscaled


                                                            PWM Duty
                                                                                                                                      3
                                                              Cycle
DS40001919G-page 331


                                                         PWM Output


                                                                             Note   1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                                                                    set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.
                                        22.5.8      LEVEL RESET, EDGE-TRIGGERED HARDWARE LIMIT                                              When the timer count matches the T2PR period count, the timer is reset and
 2017-2021 Microchip Technology Inc.


                                                    ONE SHOT MODES                                                                          the ON bit is cleared. When the ON bit is cleared by either a T2PR match or by
                                                                                                                                            software control a new external signal edge is required after the ON bit is set to
                                        In Level Triggered One Shot mode, the timer count is reset on the external                          start the counter.
                                        signal level and starts counting on the rising/falling edge of the transition from
                                                                                                                                            When Level Triggered Reset One Shot mode is used in conjunction with the
                                        reset level to the active level while the ON bit is set. Reset levels are selected
                                                                                                                                            CCP PWM operation, the PWM drive goes active with the external signal edge
                                        as follows:                                                                                         that starts the timer. The PWM drive goes inactive when the timer count equals
                                        • Low reset level (MODE[4:0] = 01110)                                                               the CCPRx pulse-width count. The PWM drive does not go active when the


                                                                                                                                                                                                                                 PIC18(L)F26/27/45/46/47/55/56/57K42
                                        • High reset level (MODE[4:0] = 01111)                                                              timer count clears at the T2PR period count match.


                                        FIGURE 22-11:          LOW LEVEL RESET, EDGE-TRIGGERED HARDWARE LIMIT ONE SHOT MODE TIMING DIAGRAM (MODE = 01110)


                                                                                                                                                                                              Rev. 10-000202C
                                                                                                                                                                                                     9/12/2016


                                                                    MODE                                                   0b01110

                                                                TMRx_clk

                                                                     TxPR                                                                   5

                                                              Instruction(1)      BSF                                         BSF


                                                                       ON

                                                                TMRx_ers

                                                                   TxTMR                0          1   2   3   4   5                0                1         0        1   2   3    4   5    0

                                                         TMRx_postscaled


                                                               PWM Duty
                                                                                                                                        3
                                                                 Cycle
DS40001919G-page 332


                                                           PWM Output


                                                                               Note   1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                                                                      set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.
                                        22.5.9      EDGE-TRIGGERED MONOSTABLE MODES                                                        When an Edge-Triggered Monostable mode is used in conjunction with the
 2017-2021 Microchip Technology Inc.


                                                                                                                                           CCP PWM operation the PWM drive goes active with the external Reset signal
                                        The Edge-Triggered Monostable modes start the timer on an edge from the
                                                                                                                                           edge that starts the timer, but will not go active when the timer matches the
                                        external Reset signal input, after the ON bit is set, and stop incrementing the
                                                                                                                                           T2PR value. While the timer is incrementing, additional edges on the external
                                        timer when the timer matches the T2PR period value. The following edges will
                                                                                                                                           Reset signal will not affect the CCP PWM.
                                        start the timer:
                                        • Rising edge (MODE[4:0] = 10001)
                                        • Falling edge (MODE[4:0] = 10010)


                                                                                                                                                                                                                                PIC18(L)F26/27/45/46/47/55/56/57K42
                                        • Rising or Falling edge (MODE[4:0] = 10011)

                                        FIGURE 22-12:            RISING EDGE-TRIGGERED MONOSTABLE MODE TIMING DIAGRAM (MODE = 10001)
                                                                                                                                                                                                             Rev. 10-000203B
                                                                                                                                                                                                                   12/13/2016


                                                           MODE                                                                            0b10001

                                                       TMRx_clk

                                                            TxPR                                                                               5

                                                     Instruction(1)       BSF                                                                          BCF      BSF                      BCF       BSF


                                                              ON

                                                       TMRx_ers

                                                          TxTMR                 0          1   2   3   4   5             0         1   2   3   4   5                  0              1   2     3     4   5             0

                                                 TMRx_postscaled


                                                      PWM Duty
                                                                                                                     3
                                                        Cycle

                                                   PWM Output
DS40001919G-page 333


                                                          Note        1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                                                      set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.
                                        22.5.10     LEVEL-TRIGGERED HARDWARE LIMIT ONE SHOT                                               When the timer count matches the T2PR period count, the timer is reset and
 2017-2021 Microchip Technology Inc.


                                                    MODES                                                                                 the ON bit is cleared. When the ON bit is cleared by either a T2PR match or by
                                                                                                                                          software control, the timer will stay in Reset until both the ON bit is set and the
                                        The Level Triggered Hardware Limit One Shot modes hold the timer in Reset
                                                                                                                                          external signal is not at the Reset level.
                                        on an external Reset level and start counting when both the ON bit is set and
                                        the external signal is not at the Reset level. If one of either the external signal               When Level Triggered Hardware Limit One Shot modes are used in conjunction
                                        is not in reset or the ON bit is set then the other signal being set/made active                  with the CCP PWM operation, the PWM drive goes active with either the
                                        will start the timer. Reset levels are selected as follows:                                       external signal edge or the setting of the ON bit, whichever of the two starts the
                                                                                                                                          timer.
                                        • Low reset level (MODE[4:0] = 10110)


                                                                                                                                                                                                                                PIC18(L)F26/27/45/46/47/55/56/57K42
                                        • High reset level (MODE[4:0] = 10111)

                                        FIGURE 22-13:                LEVEL-TRIGGERED HARDWARE LIMIT ONE SHOT MODE TIMING DIAGRAM (MODE = 10110)

                                                                                                                                                                                                             Rev. 10-000204B
                                                                                                                                                                                                                   12/13/2016


                                                          MODE                                                                           0b10110

                                                      TMRx_clk

                                                           TxPR                                                                              5

                                                    Instruction(1)           BSF                                                BSF                                                       BCF   BSF


                                                             ON

                                                      TMRx_ers

                                                         TxTMR               0           1   2   3   4   5                       0                       1   2   3         0      1   2          3       4        5         0

                                              TMRx_postscaled


                                                    PWM Duty
                                                                                                                                            ‘D3
                                                      Cycle
DS40001919G-page 334


                                                  PWM Output

                                                                     Note   1: BSF and BCF represent Bit-Set File and Bit-Clear File instructions executed by the CPU to
                                                                            set or clear the ON bit of TxCON. CPU execution is asynchronous to the timer clock input.
                      PIC18(L)F26/27/45/46/47/55/56/57K42
22.6     Timer2 Operation During Sleep
When PSYNC = 1, Timer2 cannot be operated while
the processor is in Sleep mode. The contents of the
T2TMR and T2PR registers will remain unchanged
while processor is in Sleep mode.
When PSYNC = 0, Timer2 will operate in Sleep as long
as the clock source selected is also still running.
Selecting the LFINTOSC, MFINTOSC, or HFINTOSC
oscillator as the timer clock source will keep the
selected oscillator running during Sleep.


 2017-2021 Microchip Technology Inc.                  DS40001919G-page 335
                        PIC18(L)F26/27/45/46/47/55/56/57K42
22.7        Register Definitions: Timer2/4/6
            Control                                               TABLE 22-2:           OPERATING MODES
Long bit name prefixes for the Timer2/4/6 peripherals                       Peripheral                 Bit Name Prefix
are shown in Table 22-2. Refer to Section                                     Timer2                         T2
1.3.2.2 “Long Bit Names” for more information.
                                                                              Timer4                         T4
                                                                              Timer6                         T6

REGISTER 22-1:           TxCLK: TIMERx CLOCK SELECTION REGISTER
        U-0            U-0             U-0               U-0     R/W-0/0        R/W-0/0         R/W-0/0           R/W-0/0
        —               —               —                —                                CS[3:0]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-4            Unimplemented: Read as ‘0’
bit 3-0            CS[3:0]: Timerx Clock Selection bits

                                                T2TMR                       TMR4                          TMR6
                        CS[3:0]
                                              Clock Source               Clock Source                  Clock Source
                         1111        Reserved                   Reserved                      Reserved
                         1110        CLC4_out                   CLC4_out                      CLC4_out
                         1101        CLC3_out                   CLC3_out                      CLC3_out
                         1100        CLC2_out                   CLC2_out                      CLC2_out
                         1011        CLC1_out                   CLC1_out                      CLC1_out
                         1010        ZCD_OUT                    ZCD_OUT                       ZCD_OUT
                         1001        NCO1OUT                    NCO1OUT                       NCO1OUT
                         1000        CLKREF_OUT                 CLKREF_OUT                    CLKREF_OUT
                         0111        SOSC                       SOSC                          SOSC
                         0110        MFINTOSC (32 kHz)          MFINTOSC (32 kHz)             MFINTOSC (32 kHz)
                         0101        MFINTOSC (500 kHz)         MFINTOSC (500 kHz)            MFINTOSC (500 kHz)
                         0100        LFINTOSC                   LFINTOSC                      LFINTOSC
                         0011        HFINTOSC                   HFINTOSC                      HFINTOSC
                         0010        FOSC                       FOSC                          FOSC
                         0001        FOSC/4                     FOSC/4                        FOSC/4
                         0000        Pin selected by T2INPPS    Pin selected by T4INPPS       Pin selected by T6INPPS


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 336
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 22-2:           TxRST: TIMER2 EXTERNAL RESET SIGNAL SELECTION REGISTER
        U-0            U-0              U-0           R/W-0/0       R/W-0/0       R/W-0/0       R/W-0/0           R/W-0/0
        —               —                —                                       RSEL[4:0]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                   W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            RSEL[4:0]: Timer2 External Reset Signal Source Selection bits

                                                   T2TMR                       TMR4                        TMR6
                       RSEL[4:0]
                                               Reset Source               Reset Source                  Reset Source
                     11111-11001        Reserved                    Reserved                   Reserved
                        11000           UART2_tx_edge               UART2_tx_edge              UART2_tx_edge
                        10111           UART2_rx_edge               UART2_rx_edge              UART2_rx_edge
                        10110           UART1_tx_edge               UART1_tx_edge              UART1_tx_edge
                        10101           UART1_rx_edge               UART1_rx_edge              UART1_rx_edge
                        10100           CLC4_out                    CLC4_out                   CLC4_out
                        10011           CLC3_out                    CLC3_out                   CLC3_out
                        10010           CLC2_out                    CLC2_out                   CLC2_out
                        10001           CLC1_out                    CLC1_out                   CLC1_out
                        10000           ZCD_OUT                     ZCD_OUT                    ZCD_OUT
                        01111           CMP2OUT                     CMP2OUT                    CMP2OUT
                        01110           CMP1OUT                     CMP1OUT                    CMP1OUT
                     01101-01100        Reserved                    Reserved                   Reserved
                        01011           PWM8OUT                     PWM8OUT                    PWM8OUT
                        01010           PWM7OUT                     PWM7OUT                    PWM7OUT
                        01001           PWM6OUT                     PWM6OUT                    PWM6OUT
                        01000           PWM5OUT                     PWM5OUT                    PWM5OUT
                        00111           CCP4OUT                     CCP4OUT                    CCP4OUT
                        00110           CCP3OUT                     CCP3OUT                    CCP3OUT
                        00101           CCP2OUT                     CCP2OUT                    CCP2OUT
                        00100           CCP1OUT                     CCP1OUT                    CCP1OUT
                        00011           TMR6 postscaled             TMR6 postscaled            Reserved
                        00010           TMR4 postscaled             Reserved                   TMR4 postscaled
                        00001           Reserved                    T2TMR postscaled           T2TMR postscaled
                        00000           Pin selected by T2INPPS     Pin selected by T4INPPS    Pin selected by T6INPPS


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 337
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 22-3:           TxTMR: TIMERx COUNTER REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0          R/W-0/0       R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                        TMRx[7:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            TMRx[7:0]: Timerx Counter bits


REGISTER 22-4:           TxPR: TIMERx PERIOD REGISTER
   R/W-1/1           R/W-1/1       R/W-1/1          R/W-1/1       R/W-1/1       R/W-1/1       R/W-1/1         R/W-1/1
                                                           PRx[7:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            PRx[7:0]: Timerx Period Register bits


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 338
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 22-5:           TxCON: TIMERx CONTROL REGISTER
 R/W/HC-0/0          R/W-0/0       R/W-0/0          R/W-0/0      R/W-0/0          R/W-0/0    R/W-0/0        R/W-0/0
        ON                        CKPS[2:0]                                           OUTPS[3:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         HC = Bit is cleared by hardware


bit 7              ON: Timerx On bit(1)
                   1 = Timerx is On
                   0 = Timerx is Off: all counters and state machines are reset
bit 6-4            CKPS[2:0]: Timerx-type Clock Prescale Select bits
                   111 = 1:128 Prescaler
                   110 = 1:64 Prescaler
                   101 = 1:32 Prescaler
                   100 = 1:16 Prescaler
                   011 = 1:8 Prescaler
                   010 = 1:4 Prescaler
                   001 = 1:2 Prescaler
                   000 = 1:1 Prescaler
bit 3-0            OUTPS[3:0]: Timerx Output Postscaler Select bits
                   1111 = 1:16 Postscaler
                   1110 = 1:15 Postscaler
                   1101 = 1:14 Postscaler
                   1100 = 1:13 Postscaler
                   1011 = 1:12 Postscaler
                   1010 = 1:11 Postscaler
                   1001 = 1:10 Postscaler
                   1000 = 1:9 Postscaler
                   0111 = 1:8 Postscaler
                   0110 = 1:7 Postscaler
                   0101 = 1:6 Postscaler
                   0100 = 1:5 Postscaler
                   0011 = 1:4 Postscaler
                   0010 = 1:3 Postscaler
                   0001 = 1:2 Postscaler
                   0000 = 1:1 Postscaler

Note 1:      In certain modes, the ON bit will be auto-cleared by hardware. See Section 22.1.2 “One Shot Mode”.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 339
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 22-6:           TxHLT: TIMERx HARDWARE LIMIT CONTROL REGISTER
   R/W-0/0           R/W-0/0        R/W-0/0         R/W-0/0      R/W-0/0        R/W-0/0       R/W-0/0        R/W-0/0
    PSYNC            CKPOL         CKSYNC                                     MODE[4:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              PSYNC: Timerx Prescaler Synchronization Enable bit(1, 2)
                   1 = TxTMR Prescaler Output is synchronized to Fosc/4
                   0 = TxTMR Prescaler Output is not synchronized to Fosc/4
bit 6              CKPOL: Timerx Clock Polarity Selection bit(3)
                   1 = Falling edge of input clock clocks timer/prescaler
                   0 = Rising edge of input clock clocks timer/prescaler
bit 5              CKSYNC: Timerx Clock Synchronization Enable bit(4, 5)
                   1 = ON register bit is synchronized to T2TMR_clk input
                   0 = ON register bit is not synchronized to T2TMR_clk input
bit 4-0            MODE[4:0]: Timerx Control Mode Selection bits(6, 7)
                   See Table 22-1 for all operating modes.

   Note 1:    Setting this bit ensures that reading TxTMR will return a valid data value.
        2:    When this bit is ‘1’, Timer2 cannot operate in Sleep mode.
        3:    CKPOL may not be changed while ON = 1.
        4:    Setting this bit ensures glitch-free operation when the ON is enabled or disabled.
          5: When this bit is set then the timer operation will be delayed by two TxTMR input clocks after the ON bit is
             set.
          6: Unless otherwise indicated, all modes start upon ON = 1 and stop upon ON = 0 (stops occur without
             affecting the value of TxTMR).
          7: When TxTMR = TxPR, the next clock clears TxTMR, regardless of the operating mode.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 340
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 22-3:       SUMMARY OF REGISTERS ASSOCIATED WITH TIMER2
                                                                                                             Register
   Name         Bit 7        Bit 6        Bit 5        Bit 4      Bit 3      Bit 2       Bit 1       Bit 0
                                                                                                             on Page

TxPR                                            Timer2 Module Period Register                                  322*
TxTMR                                   Holding Register for the 8-bit T2TMR Register                          322*
TxCON            ON                     CKPS[2:0]                               OUTPS[3:0]                     340
TxCLK             —           —             —           —          —                    CS[2:0]                337
TxRST             —           —             —           —                       RSEL[3:0]                      338
TxHLT          PSYNC        CPOL         CSYNC                            MODE[4:0]                            341
Legend: — = unimplemented location, read as ‘0’. Shaded cells are not used for Timer2 module.
      * Page provides register information.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 341
