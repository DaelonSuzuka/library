                          PIC18(L)F26/27/45/46/47/55/56/57K42
21.0     TIMER1/3/5 MODULE WITH                                                                   Asynchronous mode only)
         GATE CONTROL                                                                           • 16-Bit Read/Write Operation
                                                                                                • Time base for the Capture/Compare function with
Timer1/3/5 module is a 16-bit timer/counter with the                                              the CCP modules
following features:
                                                                                                • Special Event Trigger (with CCP)
• 16-bit timer/counter register pair (TMRxH:TMRxL)                                              • Selectable Gate Source Polarity
• Programmable internal or external clock source                                                • Gate Toggle mode
• 2-bit prescaler                                                                               • Gate Single Pulse mode
• Dedicated Secondary 32 kHz oscillator circuit                                                 • Gate Value Status
• Optionally synchronized comparator out                                                        • Gate Event Interrupt
• Multiple Timer1/3/5 gate (count enable) sources
                                                                                                Figure 21-1 is a block diagram of the Timer1/3/5
• Interrupt on overflow                                                                         module.
• Wake-up on overflow (external clock,

FIGURE 21-1:              TIMER1/3/5 BLOCK DIAGRAM
                                                                                                                                                                Rev. 10-000018L
          GSS<4:0>                                                                                                                                                     9/12/2016

                                     5
         TxGPPS
                                                                                                                 GSPM
          PPS                00000


                                                                                                                             1
                                                                                            0        Single Pulse                            D      Q     GVAL
             NOTE (5)                                                                                                        0
                             11111
                                                                                            1        Acq. Control
                                                                                                                                       Q1
                                                                  D          Q

                  GPOL                                                                               GGO/DONE
                                                                  CK         Q
                     ON                                                                                                                     Interrupt
                                                                                                                                                            set bit
                                                                  R
                  GTM                                                                                                                            det       TMRxGIF


                                                                                                                                 GE
              set flag bit
               TMRxIF
                                                                                                            ON
                                                                        EN
                                                (2)                                                                                          To Comparators (6)
                                         TMRx
       Tx_overflow                                                                                                          Synchronized Clock Input
                          TMRxH                 TMRxL             Q      D                              0
                                                                                                        1
          TxCLK
                                                                                           SYNC

                                                                                     CS<4:0>
                                                                                                       5
                                                                      TxCKIPPS
                                                                                          (1)
                                                                        PPS                        00000

                                                                                                                 Prescaler
                                                                                                                                                 Synchronize(3)
                                                                                                                  1,2,4,8
                                                                                 Note (4)                                                                 det
                                                                                                   11111
                                                                                                                        2
                                                                                                                                       Fosc/2
                                                                                                             CKPS<1:0>                Internal           Sleep
                                                                                                                                       Clock             Input


             Note 1:      ST Buffer is high speed type when using TxCKIPPS.
                     2:   TMRx register increments on rising edge.
                     3:   Synchronize does not operate while in Sleep.
                     4    S      R        i t    21 3 f   l   k                  l   ti


 2017-2021 Microchip Technology Inc.                                                                                                       DS40001919G-page 305
                       PIC18(L)F26/27/45/46/47/55/56/57K42
21.1     Timer1/3/5 Operation                                 The following asynchronous sources may be used at
                                                              the Timer1/3/5 gate:
The Timer1/3/5 module is a 16-bit incrementing
counter which is accessed through the TMRxH:TMRxL             • Asynchronous event on the TxGPPS pin
register pair. Writes to TMRxH or TMRxL directly              • TMR0OUT
update the counter.                                           • TMR1/3/5OUT (excluding the TMR for which it is
When used with an internal clock source, the module is          being used)
a timer and increments on every instruction cycle.            • TMR 2/4/6OUT (postscaled)
When used with an external clock source, the module           • CMP1/2OUT
can be used as either a timer or counter and                  • SMT1_match
increments on every selected edge of the external             • NCO1OUT
source.                                                       • PWM3/4 OUT
Timer1/3/5 is enabled by configuring the ON and GE            • CCP1/2/3/4 OUT
bits in the TxCON and TxGCON registers, respectively.         • CLC1/2/3/4 OUT
Table 21-1 displays the Timer1/3/5 enable selections.
                                                              • ZCDOUT

TABLE 21-1:        TIMER1/3/5 ENABLE                            Note:     In Counter mode, a falling edge must be
                   SELECTIONS                                             registered by the counter prior to the first
                                           Timer1/3/5                     incrementing rising edge after any one or
         ON                GE                                             more of the following conditions:
                                           Operation
         1                  1           Count Enabled                    • Timer1/3/5 enabled after POR
                                                                         • Write to TMRxH or TMRxL
         1                  0           Always On
                                                                         • Timer1/3/5 is disabled
         0                  1           Off
                                                                         • Timer1/3/5 is disabled (TMRxON = 0)
         0                  0           Off                                when TxCKI is high then Timer1/3/5
                                                                           is enabled (TMRxON = 1) when
21.2     Clock Source Selection                                            TxCKI is low.
The CS[4:0] bits of the TMRxCLK register (Register 21-
                                                              21.2.2      EXTERNAL CLOCK SOURCE
3) are used to select the clock source for Timer1/3/5.
The TxCLK register allows the selection of several            When the external clock source is selected, the Timer1/
possible synchronous and asynchronous clock                   3/5 module may work as a timer or a counter.
sources. Register 21-3 displays the clock source              When enabled to count, Timer1/3/5 is incremented on
selections.                                                   the rising edge of the external clock input of the
                                                              TxCKIPPS pin. This external clock source can be
21.2.1        INTERNAL CLOCK SOURCE                           synchronized to the microcontroller system clock or it
When the internal clock source is selected the                can run asynchronously.
TMRxH:TMRxL register pair will increment on multiples         When used as a timer with a clock oscillator, an
of FOSC as determined by the Timer1/3/5 prescaler.            external 32.768 kHz crystal can be used in conjunction
When the FOSC internal clock source is selected, the          with the dedicated secondary internal oscillator circuit.
Timer1/3/5 register value will increment by four counts
every instruction clock cycle. Due to this condition, a
2 LSB error in resolution will occur when reading the
Timer1/3/5 value. To utilize the full resolution of Timer1/
3/5, an asynchronous input signal must be used to gate
the Timer1/3/5 clock input.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 306
                      PIC18(L)F26/27/45/46/47/55/56/57K42
21.3      Timer1/3/5 Prescaler                              21.4.1      READING AND WRITING TIMER1/3/
                                                                        5 IN ASYNCHRONOUS COUNTER
Timer1/3/5 has four prescaler options allowing 1, 2, 4 or
                                                                        MODE
8 divisions of the clock input. The CKPS bits of the
TxCON register control the prescale counter. The            Reading TMRxH or TMRxL while the timer is running
prescale counter is not directly readable or writable;      from an external asynchronous clock will ensure a valid
however, the prescaler counter is cleared upon a write to   read (taken care of in hardware). However, the user
TMRxH or TMRxL.                                             may keep in mind that reading the 16-bit timer in two 8-
                                                            bit values itself, poses certain problems, since the timer
21.4      Timer1/3/5 Operation in                           may overflow between the reads. For writes, it is rec-
                                                            ommended that the user simply stop the timer and write
          Asynchronous Counter Mode
                                                            the desired values. A write contention may occur by
If control bit SYNC of the TxCON register is set, the       writing to the timer registers, while the register is incre-
external clock input is not synchronized. The timer         menting. This may produce an unpredictable value in
increments asynchronously to the internal phase             the TMRxH:TMRxL register pair.
clocks. If external clock source is selected then the
timer will continue to run during Sleep and can             21.5     Timer1/3/5 16-Bit Read/Write Mode
generate an interrupt on overflow, which will wake up
the processor. However, special precautions in              Timer1/3/5 can be configured to read and write all 16
software are needed to read/write the timer (see            bits of data, to and from, the 8-bit TMRxL and TMRxH
Section 21.4.1 “Reading and Writing Timer1/3/5 in           registers, simultaneously. The 16-bit read and write
Asynchronous Counter Mode”).                                operations are enabled by setting the RD16 bit of the
                                                            TxCON register.
  Note:     When switching from synchronous to
                                                            To accomplish this function, the TMRxH register value
            asynchronous operation, it is possible to
                                                            is mapped to a buffer register called the TMRxH buffer
            skip an increment. When switching from
                                                            register. While in 16-Bit mode, the TMRxH register is
            asynchronous to synchronous operation,
                                                            not directly readable or writable and all read and write
            it is possible to produce an additional
                                                            operations take place through the use of this TMRxH
            increment.
                                                            buffer register.
                                                            When a read from the TMRxL register is requested, the
                                                            value of the TMRxH register is simultaneously loaded
                                                            into the TMRxH buffer register. When a read from the
                                                            TMRxH register is requested, the value is provided
                                                            from the TMRxH buffer register instead. This provides
                                                            the user with the ability to accurately read all 16 bits of
                                                            the Timer1/3/5 value from a single instance in time.
                                                            Reference the block diagram in Figure 21-2 for more
                                                            details.
                                                            In contrast, when not in 16-Bit mode, the user must
                                                            read each register separately and determine if the
                                                            values have become invalid due to a rollover that may
                                                            have occurred between the read operations.
                                                            When a write request of the TMRxL register is
                                                            requested, the TMRxH buffer register is simultaneously
                                                            updated with the contents of the TMRxH register. The
                                                            value of TMRxH must be preloaded into the TMRxH
                                                            buffer register prior to the write request for the TMRxL
                                                            register. This provides the user with the ability to write
                                                            all 16 bits to the TMRxL:TMRxH register pair at the
                                                            same time.
                                                            Any requests to write to the TMRxH directly does not
                                                            clear the Timer1/3/5 prescaler value. The prescaler
                                                            value is only cleared through write requests to the
                                                            TMRxL register.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 307
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 21-2:               TIMER1/3/5 16-BIT READ/
                           WRITE MODE BLOCK
                           DIAGRAM
                                                  From
                                                 Timer1
                                                 Circuitry
                            TMR1                   Set
              TMR1L        High Byte             TMR1IF
                                               on Overflow
                                       8


                                            Read TMR1L
                                            Write TMR1L
                             8
                   8
                            TMR1H


                                 8
                       8
                                           Internal Data Bus

       Block Diagram of Timer1 Example of TIMER1/3/5


21.6       Timer1/3/5 Gate
Timer1/3/5 can be configured to count freely or the
count can be enabled and disabled using Timer1/3/5
gate circuitry. This is also referred to as Timer1/3/5 gate
enable.
Timer1/3/5 gate can also be driven by multiple
selectable sources.

21.6.1        TIMER1/3/5 GATE ENABLE
The Timer1/3/5 Gate Enable mode is enabled by
setting the TMRxGE bit of the TxGCON register. The
polarity of the Timer1/3/5 Gate Enable mode is
configured using the TxGPOL bit of the TxGCON
register.
When Timer1/3/5 Gate Enable mode is enabled,
Timer1/3/5 will increment on the rising edge of the
Timer1/3/5 clock source. When Timer1/3/5 Gate signal
is inactive, the timer will not increment and hold the
current count. See Figure 21-4 for timing details.


TABLE 21-2:            TIMER1/3/5 GATE ENABLE
                       SELECTIONS
                                                Timer1/3/5
 TMRxCLK         TxGPOL          TxG
                                                Operation
                      1          1         Counts
                      1          0         Holds Count
                      0          1         Holds Count
                      0          0         Counts


 2017-2021 Microchip Technology Inc.                          DS40001919G-page 308
                      PIC18(L)F26/27/45/46/47/55/56/57K42
21.6.2      TIMER1/3/5 GATE SOURCE                          21.6.4      TIMER1/3/5 GATE SINGLE PULSE
            SELECTION                                                   MODE
The gate source for Timer1/3/5 can be selected using        When Timer1/3/5 Gate Single Pulse mode is enabled,
the GSS[4:0] bits of the TMRxGATE register                  it is possible to capture a single-pulse gate event.
(Register 21-4). The polarity selection for the gate        Timer1/3/5 Gate Single Pulse mode is first enabled by
source is controlled by the TxGPOL bit of the TxGCON        setting the GSPM bit in the TxGCON register. Next, the
register (Register 21-2).                                   GGO/DONE bit in the TxGCON register must be set.
Any of the above mentioned signals can be used to           The Timer1/3/5 will be fully enabled on the next
trigger the gate. The output of the CMPx can be             incrementing edge of the gate signal. On the next
synchronized to the Timer1/3/5 clock or left                trailing edge of the pulse, the GGO/DONE bit will
asynchronous. For more information see Section              automatically be cleared. No other gate events will be
38.3.1 “Comparator Output Synchronization”.                 allowed to increment Timer1/3/5 until the GGO/DONE
                                                            bit is once again set in software.
21.6.3      TIMER1/3/5 GATE TOGGLE MODE                     Clearing the TxGSPM bit of the TxGCON register will
When Timer1/3/5 Gate Toggle mode is enabled, it is          also clear the GGO/DONE bit. See Figure 21-6 for
possible to measure the duration between every rising       timing details.
and falling edge of the gate signal.                        Enabling the Toggle mode and the Single Pulse mode
The Timer1/3/5 gate source is routed through a flip-flop    simultaneously will permit both sections to work
that changes state on every incrementing edge of the        together. This allows the period on the Timer1/3/5 gate
signal. See Figure 21-5 for timing details.                 source to be measured. See Figure 21-7 for timing
                                                            details.
Timer1/3/5 Gate Toggle mode is enabled by setting the
GTM bit of the TxGCON register. When the GTM bit is         21.6.5      TIMER1/3/5 GATE VALUE STATUS
cleared, the flip-flop is cleared and held clear. This is
necessary in order to control which edge is measured.       When Timer1/3/5 Gate Value Status is utilized, it is
                                                            possible to read the most current level of the gate
  Note:     Enabling Toggle mode at the same time           signal. The value is stored in the GVAL bit in the
            as changing the gate polarity may result in     TxGCON register. The GVAL bit is valid even when the
            indeterminate operation.                        Timer1/3/5 gate is not enabled (GE bit is cleared).

                                                            21.6.6      TIMER1/3/5 GATE EVENT
                                                                        INTERRUPT
                                                            When Timer1/3/5 Gate Event Interrupt is enabled, it is
                                                            possible to generate an interrupt upon the completion
                                                            of a gate event. When the falling edge of GVAL occurs,
                                                            the TMRxGIF flag bit in the respective PIR register will
                                                            be set. If the TMRxGIE bit in the respective PIE register
                                                            is set, then an interrupt will be recognized.
                                                            The TMRxGIF flag bit operates even when the Timer1/
                                                            3/5 gate is not enabled (GE bit is cleared).
                                                            For more information on selecting high or low priority
                                                            status for the Timer1/3/5 Gate Event Interrupt see
                                                            Section 9.0 “Interrupt Controller”.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 309
                       PIC18(L)F26/27/45/46/47/55/56/57K42
21.7      Timer1/3/5 Interrupt                                21.9     CCP Capture/Compare Time Base
The Timer1/3/5 register pair (TMRxH:TMRxL)                    The CCP modules use the TMRxH:TMRxL register pair
increments to FFFFh and rolls over to 0000h. When             as the time base when operating in Capture or
Timer1/3/5 rolls over, the Timer1/3/5 interrupt flag bit of   Compare mode.
the respective PIR register is set. To enable the             In Capture mode, the value in the TMRxH:TMRxL
interrupt-on-rollover, you must set these bits:               register pair is copied into the CCPRxH:CCPRxL
• ON bit of the TxCON register                                register pair on a configured event.
• TMRxIE bits of the respective PIE register                  In Compare mode, an event is triggered when the value
• GIE/GIEH bit of the INTCON0 register                        in the CCPRxH:CCPRxL register pair matches the
The interrupt is cleared by clearing the TMRxIF bit in        value in the TMRxH:TMRxL register pair. This event
the Interrupt Service Routine.                                can be a Special Event Trigger.

For more information on selecting high or low priority        For more information, see Section 23.0 “Capture/
status for the Timer1/3/5 Overflow Interrupt, see             Compare/PWM Module”.
Section 9.0 “Interrupt Controller”.
                                                              21.10 CCP Special Event Trigger
  Note:     The TMRxH:TMRxL register pair and the
            TMRxIF bit may be cleared before                  When any of the CCP’s are configured to trigger a
            enabling interrupts.                              special event, the trigger will clear the TMRxH:TMRxL
                                                              register pair. This special event does not cause a
                                                              Timer1/3/5 interrupt. The CCP module may still be
21.8      Timer1/3/5 Operation During Sleep
                                                              configured to generate a CCP interrupt.
Timer1/3/5 can only operate during Sleep when set up          In this mode of operation, the CCPRxH:CCPRxL
in Asynchronous Counter mode. In this mode, an                register pair becomes the period register for Timer1/3/
external crystal or clock source can be used to               5.
increment the counter. To set up the timer to wake the
device:                                                       Timer1/3/5 may be synchronized and FOSC/4 may be
                                                              selected as the clock source in order to utilize the Spe-
• ON bit of the TxCON register must be set                    cial Event Trigger. Asynchronous operation of Timer1/
• TMRxIE bit of the respective PIE register must be           3/5 can cause a Special Event Trigger to be missed.
  set
                                                              In the event that a write to TMRxH or TMRxL coincides
• SYNC bit of the TxCON register must be set                  with a Special Event Trigger from the CCP, the write will
• Configure the TMRxCLK register for using                    take precedence.
  secondary oscillator as the clock source
• Enable the SOSCEN bit of the OSCEN register
  (Register 7-7)
The device will wake up on an overflow and execute
the next instruction. If the GIE/GIEH bit of the
INTCON0 register is set, the device will call the
Interrupt Service Routine.
The secondary oscillator will continue to operate in
Sleep regardless of the SYNC bit setting.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 310
                        PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 21-3:             TIMER1/3/5 INCREMENTING EDGE

    TxCKI = 1
    when TxTMR
    Enabled


    TxCKI = 0
    when TxTMR
    Enabled

  Note 1:    Arrows indicate counter increments.
        2:   In Counter mode, a falling edge must be registered by the counter prior to the first incrementing rising edge of the clock.


FIGURE 21-4:             TIMER1/3/5 GATE ENABLE MODE


        TMRxGE


        TxGPOL


         TxG_IN


             TxCKI


         TxGVAL


    Timer1/3/5                    N                              N+1                N+2                   N+3         N+4


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 311
                         PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 21-5:             TIMER1/3/5 GATE TOGGLE MODE


     TMRxGE


     TxGPOL


      TxGTM


    TxTxG_IN


       TxCKI


     TxGVAL


   TIMER1/3/5        N                  N+1 N+2 N+3    N+4             N+5 N+6 N+7     N+8


FIGURE 21-6:             TIMER1/3/5 GATE SINGLE PULSE MODE


      TMRxGE

      TxGPOL


      TxGSPM
                                                             Cleared by hardware on
       TxGGO/                     Set by software            falling edge of TxGVAL
         DONE
                                 Counting enabled on
                                  rising edge of TxG
       TxG_IN


         TxCKI


       TxGVAL


 TIMER1/3/5                  N                         N+1   N+2

                                                                                         Cleared by
     TMRxGIF              Cleared by software                Set by hardware on           software
                                                             falling edge of TxGVAL


 2017-2021 Microchip Technology Inc.                                             DS40001919G-page 312
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 21-7:           TIMER1/3/5 GATE SINGLE-PULSE AND TOGGLE COMBINED MODE

    TMRxGE

     TxGPOL


     TxGSPM


      TxGTM

                                                                                        Cleared by hardware on
     TxGGO/                      Set by software                                        falling edge of TxGVAL
       DONE                    Counting enabled on
                                rising edge of TxG
      TxG_IN


        TxCKI


     TxGVAL


    TIMER1/3/5             N                         N+1     N+2      N+3         N+4

                                                             Set by hardware on                   Cleared by
    TMRxGIF             Cleared by software             falling edge of TxGVAL                     software


21.11 Peripheral Module Disable
When a peripheral module is not used or inactive, the
module can be disabled by setting the Module Disable
bit in the PMD registers. This will reduce power
consumption to an absolute minimum. Setting the PMD
bits holds the module in Reset and disconnects the
module’s clock source. The Module Disable bits for
Timer1 (TMR1MD), Timer3 (TMR3MD) and Timer5
(TMR5MD) are in the respective PMD registers. See
Section 19.0 “Peripheral Module Disable (PMD)” for
more information.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 313
                        PIC18(L)F26/27/45/46/47/55/56/57K42
21.12 Register Definitions: Timer1/3/5
Long bit name prefixes for the Timer1/3/5 are shown
below. Refer to Section 1.3.2.2 “Long Bit Names” for
more information.


          Peripheral               Bit Name Prefix
              Timer1                       T1
              Timer3                       T3
              Timer5                       T5


REGISTER 21-1:           TXCON: TIMERx CONTROL REGISTER
        U-0            U-0          R/W-0/u         R/W-0/u        U-0           R/W-0/u      R/W-0/0       R/W-0/u
        —               —                 CKPS[1:0]                 —                SYNC      RD16            ON
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
-n = Value at POR                ‘1’ = Bit is set             ‘0’ = Bit is cleared          u = unchanged


bit 7-6            Unimplemented: Read as ‘0’
bit 5-4            CKPS[1:0]: Timerx Input Clock Prescale Select bits
                   11 = 1:8 Prescale value
                   10 = 1:4 Prescale value
                   01 = 1:2 Prescale value
                   00 = 1:1 Prescale value
bit 3              Unimplemented: Read as ‘0’
bit 2              SYNC: Timerx External Clock Input Synchronization Control bit
                   TMRxCLK = FOSC/4 or FOSC:
                         This bit is ignored. Timer1 uses the incoming clock as is.
                   Else:
                         1 = Do not synchronize external clock input
                         0 = Synchronize external clock input with system clock
bit 1              RD16: 16-Bit Read/Write Mode Enable bit
                   1 = Enables register read/write of Timerx in one 16-bit operation
                   0 = Enables register read/write of Timerx in two 8-bit operation
bit 0              ON: Timerx On bit
                   1 = Enables Timerx
                   0 = Disables Timerx


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 314
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 21-2:         TxGCON: TIMERx GATE CONTROL REGISTER
   R/W-0/u         R/W-0/u       R/W-0/u          R/W-0/u      R/W-0/u             R-x           U-0            U-0
        GE         GPOL            GTM            GSPM       GGO/DONE              GVAL          —              —
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit               W = Writable bit             U = Unimplemented bit, read as ‘0’
-n = Value at POR              ‘1’ = Bit is set             ‘0’ = Bit is cleared           x = Bit is unknown


bit 7           GE: Timerx Gate Enable bit
                If TMRxON = 1:
                1 = Timerx counting is controlled by the Timerx gate function
                0 = Timerx is always counting
                If TMRxON = 0:
                      This bit is ignored
bit 6           GPOL: Timerx Gate Polarity bit
                1 = Timerx gate is active-high (Timerx counts when gate is high)
                0 = Timerx gate is active-low (Timerx counts when gate is low)
bit 5           GTM: Timerx Gate Toggle Mode bit
                1 = Timerx Gate Toggle mode is enabled
                0 = Timerx Gate Toggle mode is disabled and Toggle flip-flop is cleared
                Timerx Gate Flip Flop Toggles on every rising edge
bit 4           GSPM: Timerx Gate Single Pulse Mode bit
                1 = Timerx Gate Single Pulse mode is enabled and is controlling Timerx gate)
                0 = Timerx Gate Single Pulse mode is disabled
bit 3           GGO/DONE: Timerx Gate Single Pulse Acquisition Status bit
                1 = Timerx Gate Single Pulse Acquisition is ready, waiting for an edge
                0 = Timerx Gate Single Pulse Acquisition has completed or has not been started.
                This bit is automatically cleared when TxGSPM is cleared.
bit 2           GVAL: Timerx Gate Current State bit
                Indicates the current state of the Timerx gate that could be provided to TMRxH:TMRxL
                Unaffected by Timerx Gate Enable (TMRxGE)
bit 1-0         Unimplemented: Read as ‘0’


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 315
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 21-3:         TxCLK: TIMERx CLOCK REGISTER
        U-0           U-0               U-0             R/W-0/u     R/W-0/u          R/W-0/u          R/W-0/u            R/W-0/u
        —             —                 —                                                CS[4:0]
bit 7                                                                                                                         bit 0


Legend:
R = Readable bit                  W = Writable bit                U = Unimplemented bit, read as ‘0’
-n = Value at POR                 ‘1’ = Bit is set                ‘0’ = Bit is cleared             u = unchanged


bit 7-5          Unimplemented: Read as ‘0’
bit 4-0          CS[4:0]: Timerx Clock Source Selection bits

                                                     Timer1                    Timer3                           Timer5
                        CS
                                              Clock Source                   Clock Source                     Clock Source

                    11111-10001      Reserved                       Reserved                       Reserved
                       10000         CLC4                           CLC4                           CLC4
                       01111         CLC3                           CLC3                           CLC3
                       01110         CLC2                           CLC2                           CLC2
                       01101         CLC1                           CLC1                           CLC1
                       01100         TMR5 overflow                  TMR5 overflow                  Reserved
                       01011         TMR3 overflow                  Reserved                       TMR3 overflow
                       01010         Reserved                       TMR1 overflow                  TMR1 overflow
                       01001         TMR0 overflow                  TMR0 overflow                  TMR0 overflow
                       01000         CLKREF                         CLKREF                         CLKREF
                       00111         SOSC                           SOSC                           SOSC
                       00110         MFINTOSC (32 kHz)              MFINTOSC (32 kHz)              MFINTOSC (32 kHz)
                       00101         MFINTOSC (500 kHz)             MFINTOSC (500 kHz)             MFINTOSC (500 kHz)
                       00100         LFINTOSC                       LFINTOSC                       LFINTOSC
                       00011         HFINTOSC                       HFINTOSC                       HFINTOSC
                       00010         Fosc                           Fosc                           Fosc
                       00001         Fosc/4                         Fosc/4                         Fosc/4
                       00000         T1CKIPPS                       T3CKIPPS                       T5CKIPPS


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 316
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 21-4:           TxGATE: TIMERx GATE ISM REGISTER
     U-0           U-0           U-0            R/W-0/u      R/W-0/u             R/W-0/u        R/W-0/u              R/W-0/u
        —           —             —                                              GSS[4:0]
bit 7                                                                                                                     bit 0


Legend:
R = Readable bit            W = Writable bit              U = Unimplemented bit, read as ‘0’
-n = Value at POR           ‘1’ = Bit is set              ‘0’ = Bit is cleared               u = unchanged


bit 7-5       Unimplemented: Read as ‘0’
bit 4-0       GSS[4:0]: Timerx Gate Source Selection bits

                                             Timer1                     Timer3                           Timer5
                     GSS
                                           Gate Source                Gate Source                      Gate Source
                 11111-11011    Reserved                   Reserved                         Reserved
                    11010       CLC4_out                   CLC4_out                         CLC4_out
                    11001       CLC3_out                   CLC3_out                         CLC3_out
                    11000       CLC2_out                   CLC2_out                         CLC2_out
                    10111       CLC1_out                   CLC1_out                         CLC1_out
                    10110       ZCDOUT                     ZCDOUT                           ZCDOUT
                    10101       CMP2OUT                    CMP2OUT                          CMP2OUT
                    10100       CMP1OUT                    CMP1OUT                          CMP1OUT
                    10011       NCO1OUT                    NCO1OUT                          NCO1OUT
                 10010-10001    Reserved                   Reserved                         Reserved
                    10000       PWM8OUT                    PWM8OUT                          PWM8OUT
                    01111       PWM7OUT                    PWM7OUT                          PWM7OUT
                    01110       PWM6OUT                    PWM6OUT                          PWM6OUT
                    01101       PWM5OUT                    PWM5OUT                          PWM5OUT
                    01100       CCP4OUT                    CCP4OUT                          CCP4OUT
                    01011       CCP3OUT                    CCP3OUT                          CCP3OUT
                    01010       CCP2OUT                    CCP2OUT                          CCP2OUT
                    01001       CCP1OUT                    CCP1OUT                          CCP1OUT
                    01000       SMT1_match                 SMT1_match                       SMT1_match
                    00111       TMR6OUT (postscaled)       TMR6OUT (postscaled)             TMR6OUT (postscaled)
                    00110       TMR5 overflow              TMR5 overflow                    Reserved
                    00101       TMR4OUT (postscaled)       TMR4OUT (postscaled)             TMR4OUT (postscaled)
                    00100       TMR3 overflow              Reserved                         TMR3 overflow
                    00011       TMR2OUT (postscaled)       TMR2OUT (postscaled)             TMR2OUT (postscaled)
                    00010       Reserved                   TMR1 overflow                    TMR1 overflow
                    00001       TMR0 overflow              TMR0 overflow                    TMR0 overflow
                    00000       Pin selected by T1GPPS     Pin selected by T3GPPS           Pin selected by T5GPPS


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 317
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 21-5:          TMRxL: TIMERx LOW BYTE REGISTER
    R/W-x/x          R/W-x/x       R/W-x/x         R/W-x/x     R/W-x/x       R/W-x/x        R/W-x/x         R/W-x/x
                                                       TMRxL[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            TMRxL[7:0]:Timerx Low Byte bits

REGISTER 21-6:          TMRxH: TIMERx HIGH BYTE REGISTER
    R/W-x/x          R/W-x/x       R/W-x/x         R/W-x/x     R/W-x/x       R/W-x/x        R/W-x/x         R/W-x/x
                                                       TMRxH[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            TMRxH[7:0]:Timerx High Byte bits


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 318
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 21-3:       SUMMARY OF REGISTERS ASSOCIATED WITH TIMER1/3/5 AS A TIMER/COUNTER
                                                                                                                Reset
                                                                                                                Values
   Name          Bit 7         Bit 6        Bit 5      Bit 4        Bit 3        Bit 2      Bit 1       Bit 0
                                                                                                                  on
                                                                                                                 Page

TxCON             —              —            CKPS[1:0]              —          SYNC       RD16          ON       315
TxGCON            GE           GPOL         GTM       GSPM       GO/DONE        GVAL         —            —       316
TxCLK             —              —           —                                CS[4:0]                             317

TxGATE            —              —           —                               GSS[4:0]                             318
TMRxL                                Least Significant Byte of the 16-bit TMR3 Register                           319
TMRxH                    Holding Register for the Most Significant Byte of the 16-bit TMR3 Register               319
Legend: — = Unimplemented location, read as ‘0’. Shaded cells are not used by TIMER1/3/5.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 319
