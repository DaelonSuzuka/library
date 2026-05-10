                                                                                                           PIC18F27/47/57Q43
                                                                                              SMT - Signal Measurement Timer


27.     SMT - Signal Measurement Timer
        The Signal Measurement Timer (SMT) is a 24-bit counter with advanced clock and gating logic,
        which can be configured for measuring a variety of digital signal parameters such as pulse width,
        frequency and duty cycle, and the time difference between edges on two signals.
        Features of the SMT include:
        • 24-Bit Timer/Counter
        •   Two 24-Bit Measurement Capture Registers
        •   One 24-Bit Period Match Register
        •   Multi-Mode Operation, Including Relative Timing Measurement
        •   Interrupt-on-Period Match and Acquisition Complete
        •   Multiple Clock, Signal and Window Sources
        Below is the block diagram for the SMT module.

        Figure 27-1. Signal Measurement Timer Block Diagram

                                                                                                         Rev. 10-000161E
                                                                                                               11/13/2018


                                                                              Period Latch
                                                                                                  Set SMTxPRAIF
               SMT_window           SMT
                                   Clock                                        SMTxPR
                                   Sync
                                   Circuit
                                                     Control      Set SMTxIF
                                                      Logic                    Comparator
                SMT_signal          SMT
                                   Clock
                                   Sync
                                   Circuit

                                                                                             24-bit
                                                                     Reset                                SMTxCPR
                                                                                             Buffer

                                                                    Enable     SMTxTMR       24-bit
                                                                                                          SMTxCPW
                                                                                             Buffer

                   SMT                                         Window Latch
                                         Prescaler                                                Set SMTxPWAIF
                   Clock
                  Sources


                            CSEL


27.1    SMT Operation
27.1.1 Clock Source Selection
        The SMT clock source is selected by configuring the CSEL bits. The clock source is prescaled by using
        the PS bits. The prescaled clock source is used to clock both the counter and any synchronization
        logic used by the module.
        The polarity of the clock source is selected by using the CPOL bit.

27.1.2 Signal and Window Source Selection
        The SMT signal and window sources are selected by configuring the SSEL bits and the WSEL bits
        (refer to the figure below).


--- p424 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                       SMT - Signal Measurement Timer

       The polarity of the signal and window sources is selected by using the SPOL and WPOL bits,
       respectively.

       Figure 27-2. SMT Signal and SMT Window Source Selections

                                                                                           Rev. 10-000173D
                                                                                                 11/13/2018


                          See                                       See
                        SMTxSIG                SMT_signal         SMTxWIN              SMT_window
                        Register                                   Register


                               SSEL                                     WSEL


27.1.3 Time Base
       The SMTxTMR register is the 24-bit counter/timer used for measurement in each of the modes of
       the SMT. Setting the RST bit clears the SMTxTMR register to 0x000000. It can be written to and read
       by software. It is not guarded for atomic access, therefore reads and writes to the SMTxTMR register
       must be made only when GO = 0.
       The counter can be prevented from resetting at the end of the timer period by using the STP bit.
       When STP = 1, the SMTxTMR will stop and remain equal to the SMTxPR register. When STP = 0, the
       SMTxTMR register resets to 0x000000 at the end of the period.

27.1.4 Pulse-Width and Period Captures
       The SMTxCPW and SMTxCPR registers are used to latch in the value of the SMTxTMR register, based
       on the SMT mode of operation. These registers can also be updated with the current value of the
       SMTxTMR value by setting the CPWUP and CPRUP bits, respectively.

27.1.5 Status Information
       The SMT provides input status information for the user without requiring the need to monitor the
       raw incoming signals.
       Go Status: Timer run status is indicated by the TS bit. The TS bit is delayed in time by synchronizer
       delays in non-counter modes.
       Signal Status: Signal status is indicated by the AS bit. This bit is used in all modes, except Window
       Measure, Time-of-Flight, and Capture modes, and is only valid when TS = 1. The signal status is
       delayed in time by synchronizer delays in non-counter modes.
       Window Status: Window status is indicated by the WS bit. This bit is only used in Windowed
       Measure, Gated Counter, and Gated Window Measure modes, and is only valid when TS = 1. Window
       status is delayed in time by synchronizer delays in non-counter modes.

27.1.6 Modes of Operation
       The modes of operation are summarized in the table below. The sections following the table provide
       descriptions and examples of how each mode can be used. Note that all waveforms assume WPOL/
       SPOL/CPOL = 0.
       For all modes, the REPEAT bit controls whether the acquisition happens only once or is repeated.
       When REPEAT = 0 (Single Acquisition mode), the timer will stop incrementing and the GO bit will


--- p425 ---
                                                                                                                                PIC18F27/47/57Q43
                                                                                                                   SMT - Signal Measurement Timer

       be cleared upon the completion of an acquisition. Otherwise, the timer will continue and allow for
       continued acquisitions to overwrite the previous ones, until the timer is stopped by software.

       Table 27-1. Modes of Operation
              MODE                            Mode of Operation                                                Synchronous Operation
           1111-1011                                 Reserved                                                                    -
               1010                           Windowed Counter                                                                  No
               1001                             Gated Counter                                                                   No
               1000                                  Counter                                                                    No
               0111                                  Capture                                                                    Yes
               0110                       Time of Flight Measurement                                                            Yes
               0101                     Gated Windowed Measurement                                                              Yes
               0100                        Windowed Measurement                                                                 Yes
               0011                     High and Low Time Measurement                                                           Yes
               0010                 Period and Duty Cycle Measurement                                                           Yes
               0001                              Gated Timer                                                                    Yes
               0000                                   Timer                                                                     Yes

27.1.6.1 Timer Mode
       Timer mode is the basic mode of operation where the SMTxTMR register is used as a 24-bit timer.
       No data acquisition takes place in this mode. The timer increments as long as the GO bit has been
       set by software. No SMT window or SMT signal events affect the GO bit. Everything is synchronized
       to the SMT clock source. When the timer experiences a period match (SMTxTMR = SMTxPR), the
       SMTxTMR register is reset and the period match interrupt is set. Refer to the figure below.

       Figure 27-3. Timer Mode Timing Diagram
                                                                                                                                             Rev. 10-000174A
                                                                                                                                                   11/13/2018


           SMTx Clock

             SMTxEN

             SMTxGO

         SMTxGO_sync

             SMTxPR                                                               11

            SMTxTMR             0                1    2   3   4   5   6   7   8        9 10 11 0   1   2   3   4    5   6   7   8        9

              SMTxIF


27.1.6.2 Gated Timer Mode
       Gated Timer mode uses the SMT_signal input, selected with the SSEL bits, to control whether or not
       the SMTxTMR register will increment. Upon a falling edge of the signal, the SMTxCPW register will
       update to the current value of the SMTxTMR register. Example waveforms for both repeated and
       single acquisitions are provided in the figures below.


--- p426 ---
                                                                                                     PIC18F27/47/57Q43
                                                                                        SMT - Signal Measurement Timer

Figure 27-4. Gated Timer Mode, Repeat Acquisition Timing Diagram
                                                                                                              Rev. 10-000176A
                                                                                                                    11/15/2018


     SMTx_signal

  SMTx_signalsync

      SMTx Clock

         SMTxEN

         SMTxGO

    SMTxGO_sync

         SMTxPR                                                  0xFFFFFF

       SMTxTMR                     0                     1   2     3   4        5        6             7

       SMTxCPW                                                                      5                  7

     SMTxPWAIF


Figure 27-5. Gated Timer Mode, Single Acquisition Timing Diagram
                                                                                                                Rev. 10-000175A
                                                                                                                      11/15/2018


     SMTx_signal

 SMTx_signalsync

      SMTx Clock

        SMTxEN

        SMTxGO

   SMTxGO_sync

        SMTxPR                                                   0xFFFFFF

       SMTxTMR                 0                         1   2     3   4    5

       SMTxCPW                                                                               5

     SMTxPWAIF


--- p427 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                      SMT - Signal Measurement Timer

27.1.6.3 Period and Duty Cycle Measurement Mode
       In this mode, either the duty cycle or period of the input signal can be acquired relative to the SMT
       clock. The SMTxCPW register is updated on a falling edge of the signal, and the SMTxCPR register
       is updated on a rising edge of the signal. The rising edge also resets the SMTxTMR register to
       0x000001. The GO bit is reset on a rising edge when the SMT is in Single Acquisition mode. Refer to
       the figures below.

       Figure 27-6. Period and Duty Cycle, Repeat Acquisition Mode Timing Diagram
                                                                                                                                     Rev. 10-000177A
                                                                                                                                           11/15/2018


             SMTx_signal

         SMTx_signalsync

             SMTx Clock

                SMTxEN

                SMTxGO

           SMTxGO_sync

               SMTxTMR                  0                      1   2    3   4   5   6   7   8   9 10 11 1   2   3   4            5

              SMTxCPW                                                                           5                            2

               SMTxCPR                                                                                                  11

             SMTxPWAIF

             SMTxPRAIF


       Figure 27-7. Period and Duty Cycle, Single Acquisition Mode Timing Diagram
                                                                                                                                       Rev. 10-000178A
                                                                                                                                             11/15/2018


            SMTx_signal

         SMTx_signalsync

             SMTx Clock

                SMTxEN

                SMTxGO

           SMTxGO_sync

              SMTxTMR                   0                      1   2    3   4   5   6   7   8   9 10 11                  1

              SMTxCPW                                                                                       5

              SMTxCPR                                                                                                   11

            SMTxPWAIF

             SMTxPRAIF


--- p428 ---
                                                                                                                       PIC18F27/47/57Q43
                                                                                                          SMT - Signal Measurement Timer

27.1.6.4 High and Low Measurement Mode
       This mode measures the high and low pulse time of the SMT_signal, relative to the SMT clock. The
       SMTxTMR register starts incrementing on a rising edge of the input signal. On the falling edge, the
       SMTxTMR register value is written to the SMTxCPW register. The SMTxTMR register is then reset
       and continues to increment. On the next rising edge, the SMTxTMR register value is written to the
       SMTxCPR register. The SMTxTMR register is then reset and continues to increment. Refer to the
       figures below.

       Figure 27-8. High and Low Measurement Mode, Repeat Acquisition Timing Diagram
                                                                                                                                       Rev. 10-000180A
                                                                                                                                             11/15/2018


           SMTx_signal

        SMTx_signalsync

            SMTx Clock

               SMTxEN

               SMTxGO

          SMTxGO_sync

             SMTxTMR                   0                     1   2    3   4   5   1   2   3   4   5   6    1   2   1   2           3

             SMTxCPW                                                                          5                                2

             SMTxCPR                                                                                                       6

           SMTxPWAIF

            SMTxPRAIF


       Figure 27-9. High and Low Measurement Mode, Single Acquisition Timing Diagram
                                                                                                                                       Rev. 10-000179A
                                                                                                                                             11/15/2018


           SMTx_signal

        SMTx_signalsync

            SMTx Clock

               SMTxEN

               SMTxGO

          SMTxGO_sync

             SMTxTMR                   0                     1   2    3   4   5   1   2   3   4   5   6

             SMTxCPW                                                                                           5

             SMTxCPR                                                                                                       6

           SMTxPWAIF

            SMTxPRAIF


--- p429 ---
                                                                                                                         PIC18F27/47/57Q43
                                                                                                            SMT - Signal Measurement Timer

27.1.6.5 Windowed Measurement Mode
       This mode measures the period of the SMT_window input, selected with the WSEL bits, relative to
       the SMT clock. On the rising edge of the window input, the SMTxTMR register value is written to the
       SMTxCPR register. In Repeat mode, the SMTxTMR register is reset and continues to increment. The
       capture and Reset process repeats on the next rising edge. Refer to the figures below.

       Figure 27-10. Windowed Measurement Mode, Repeat Acquisition Timing Diagram
                                                                                                                                              Rev. 10-000182A
                                                                                                                                                    11/15/2018


            SMTxWIN

        SMTxWIN_sync

           SMTx Clock

             SMTxEN

             SMTxGO

         SMTxGO_sync

            SMTxTMR           0            1   2   3   4   5    6   7   8   9 10 11 12 1   2   3   4    5    6   7    8   1   2   3       4

            SMTxCPR                                                                                12                                 8

          SMTxPRAIF


       Figure 27-11. Windowed Measurement Mode, Single Acquisition Timing Diagram
                                                                                                                                              Rev. 10-000181A
                                                                                                                                                    11/15/2018


            SMTxWIN

        SMTxWIN_sync

           SMTx Clock

             SMTxEN

             SMTxGO

         SMTxGO_sync

            SMTxTMR           0            1   2   3   4   5    6   7   8   9 10 11 12

            SMTxCPR                                                                                                  12

           SMTxPRAIF


--- p430 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                               SMT - Signal Measurement Timer

27.1.6.6 Gated Window Measurement Mode
       This mode measures the duty cycle of the SMT_signal input over a known input window. It does
       so by incrementing the SMTxTMR register on each rising edge of the SMTx clock signal when the
       SMT_signal input is high. The accumulated SMTxTMR register value is written to the SMTxCPR
       register, and the SMTxTMR register is reset on every rising edge of the window input after the
       first. Refer to the figures below.

       Figure 27-12. Gated Windowed Measurement Mode, Repeat Acquisition Timing Diagram
                                                                                                                       Rev. 10-000184A
                                                                                                                             11/15/2018


              SMTxWIN

         SMTxWIN_sync

           SMTx_signal

        SMTx_signalsync

            SMTx Clock

               SMTxEN

               SMTxGO

          SMTxGO_sync

             SMTxTMR         0           1     2         3      4     5   6        0       1    2           3               0

             SMTxCPR                                                                   6                                 3

            SMTxPRAIF


       Figure 27-13. Gated Windowed Measurement Mode, Single Acquisition Timing Diagram
                                                                                                                       Rev. 10-000183A
                                                                                                                             11/15/2018


              SMTxWIN

         SMTxWIN_sync

            SMTx_signal

        SMTx_signalsync

            SMTx Clock

               SMTxEN

               SMTxGO

          SMTxGO_sync

              SMTxTMR        0           1     2         3      4     5                             6

              SMTxCPR                                                                                   6

            SMTxPRAIF


--- p431 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                         SMT - Signal Measurement Timer

27.1.6.7 Time-of-Flight Measurement Mode
       This mode measures the time interval between a rising edge on the SMT_window input and a rising
       edge on the SMT_signal input. The SMTxTMR register starts incrementing on the rising edge of the
       window input. The SMTxTMR register value is written to the SMTxCPR register and the SMTxTMR
       register is reset on a rising edge of the signal input. In the event of two rising edges of the window
       signal without a signal rising edge, the SMTxCPW register will be written with the current value of the
       SMTxTMR register, which will then be reset. Refer to the figures below.

       Figure 27-14. Time-of-Flight Mode, Repeat Acquisition Timing Diagram
                                                                                                                                    Rev. 10-000186A
                                                                                                                                          11/15/2018


               SMTxWIN

          SMTxWIN_sync

            SMTx_signal

         SMTx_signalsync

             SMTx Clock

                SMTxEN

                SMTxGO

           SMTxGO_sync

              SMTxTMR      0    1   2   3   4            5                       1   2   3   4   5   6    7   8   9 10 11 12 13 1        2

              SMTxCPW                                                                                                               13

              SMTxCPR                                                            4

            SMTxPWAIF

             SMTxPRAIF


       Figure 27-15. Time-of-Flight Mode, Single Acquisition Timing Diagram
                                                                                                                                    Rev. 10-000185A
                                                                                                                                          11/15/2018


               SMTxWIN

          SMTxWIN_sync

            SMTx_signal

         SMTx_signalsync

             SMTx Clock

                SMTxEN

                SMTxGO

           SMTxGO_sync

              SMTxTMR      0    1   2   3   4                                    5

              SMTxCPW

              SMTxCPR                                                            4

            SMTxPWAIF

             SMTxPRAIF


--- p432 ---
                                                                                                                     PIC18F27/47/57Q43
                                                                                                        SMT - Signal Measurement Timer

27.1.6.8 Capture Mode
       This mode captures the SMTxTMR register value based on a rising or falling edge of the SMT_window
       input and triggers an interrupt. This mimics the capture feature of a CCP module. The timer begins
       incrementing upon the GO bit being set. The SMTxTMR register value is written to the SMTxCPR
       register on each rising edge of the SMT_window input. The SMTxTMR register value is written to
       the SMTxCPW register on each falling edge of the SMT_window input. The timer is not reset by any
       hardware conditions in this mode and must be reset by software, if desired. Refer to the figures
       below.

       Figure 27-16. Capture Mode, Repeat Acquisition Timing Diagram
                                                                                                                                 Rev. 10-000188A
                                                                                                                                       11/15/2018


             SMTxWIN

         SMTxWIN_sync

           SMTx Clock

              SMTxEN

              SMTxGO

         SMTxGO_sync

            SMTxTMR     0   1   2   3   4   5    6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32

            SMTxCPW                                                3                                           19                      32

             SMTxCPR                                           2                                          18                      31

           SMTxPWAIF

           SMTxPRAIF


       Figure 27-17. Capture Mode, Single Acquisition Timing Diagram
                                                                                                                                 Rev. 10-000187A
                                                                                                                                       11/15/2018


             SMTxWIN

         SMTxWIN_sync

           SMTx Clock

              SMTxEN

              SMTxGO

         SMTxGO_sync

             SMTxTMR    0   1   2                                                      3

            SMTxCPW                                                                        3

             SMTxCPR                                                                   2

           SMTxPWAIF

           SMTxPRAIF


--- p433 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                      SMT - Signal Measurement Timer

27.1.6.9 Counter Mode
       This mode increments the SMTxTMR register on each rising edge of the SMT_signal input. This
       mode is asynchronous to the SMT clock and uses the SMT_signal input as a time source. The
       SMTxCPW register will be updated with the current SMTxTMR register value on the falling edge of
       the SMT_window input. Refer to the figure below.

       Figure 27-18. Counter Mode Timing Diagram
                                                                                                                                  Rev. 10-000189A
                                                                                                                                        11/15/2018


           SMTxWIN

         SMTx_signal

            SMTxEN

            SMTxGO

          SMTxTMR          0         1   2   3   4   5   6   7    8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26        27

          SMTxCPW                                                                                12                          25


27.1.6.10 Gated Counter Mode
       This mode counts rising edges on the SMT_signal input, gated by the SMT_window input.
       It increments the SMTxTMR register for each rising edge of the SMT_signal input while the
       SMT_window input is high. The SMTxTMR register value is written to the SMTxCPW register upon
       a falling edge of the SMT_window input. Refer to the figures below.

       Figure 27-19. Gated Counter Mode, Repeat Acquisition Timing Diagram
                                                                                                                                  Rev. 10-000190A
                                                                                                                                        11/15/2018


           SMTxWIN

         SMTx_signal

            SMTxEN

            SMTxGO

          SMTxTMR          0                             1   2    3   4   5   6   7          8              9 10 11 12       13

          SMTxCPW                                                                                     8                       13

         SMTxPWAIF


       Figure 27-20. Gated Counter Mode, Single Acquisition Timing Diagram
                                                                                                                                  Rev. 10-000191A
                                                                                                                                        11/15/2018


           SMTxWIN

         SMTx_signal

            SMTxEN

            SMTxGO

          SMTxTMR          0                             1   2    3   4   5   6   7          8

          SMTxCPW                                                                                     8

         SMTxPWAIF


--- p434 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                   SMT - Signal Measurement Timer

27.1.6.11 Windowed Counter Mode
       This mode counts rising edges of the SMT_signal between rising edges of the SMT_window input.
       Beginning with the rising edge of the SMT_window input, the SMTxTMR register is incremented for
       every rising edge of the SMT_signal input. The SMTxTMR register value is written to the SMTxCPW
       register on the falling edge of the SMT_window input and the SMTxTMR register continues to
       increment. The SMTxTMR register value is written to the SMTxCPR register, then reset on each rising
       edge of the SMT_window input after the first. Refer to the figures below.

       Figure 27-21. Windowed Counter Mode, Repeat Acquisition Timing Diagram
                                                                                                                                     Rev. 10-000192A
                                                                                                                                           11/15/2018


             SMTxWIN

           SMTx_signal

              SMTxEN

              SMTxGO

            SMTxTMR       0                       1   2    3   4   5   6   7   8   9 10 11 12 13 14 15 16 1     2   3   4        5

            SMTxCPW                                                                                 9                             5

             SMTxCPR                                                                                                    16

           SMTxPWAIF

           SMTxPRAIF


       Figure 27-22. Windowed Counter Mode, Single Acquisition Timing Diagram
                                                                                                                                     Rev. 10-000193A
                                                                                                                                           11/15/2018


             SMTxWIN

           SMTx_signal

              SMTxEN

              SMTxGO

            SMTxTMR       0                       1   2    3   4   5   6   7   8   9 10 11 12 13 14 15 16

            SMTxCPW                                                                                         9

             SMTxCPR                                                                                                    16

           SMTxPWAIF

           SMTxPRAIF


27.1.7 Interrupts
       The SMT has three interrupts located in one of the PIR registers:
       • Pulse-Width Acquisition Interrupt (SMTxPWAIF): Interrupt triggers when the SMTxCPW
         register is updated with the SMTxTMR register value.
       •    Period Acquisition Interrupt (SMTxPRAIF): Interrupt triggers when the SMTxCPR register is
            updated with the SMTxTMR register value.
       •    Counter Period Match Interrupt (SMTxIF): Interrupt triggers when the SMTxTMR register
            equals the SMTxPR register.
       Each of the above interrupts can be enabled/disabled using the corresponding bits in the PIE
       register.


--- p435 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                               SMT - Signal Measurement Timer

27.1.8 Operation During Sleep
       The SMT can operate during Sleep mode, provided that the clock and signal sources continue to
       function. In general, internal clock sources, such as HFINTOSC, continue to operate in Sleep mode
       when selected as the clock source, whereas external oscillators, such as FOSC and FOSC/4 cease to
       operate in Sleep.

27.2   Register Definitions: SMT Control
       Long bit name prefixes for the SMT peripherals are shown in the table below. Replace the x in SMTx
       with the SMT peripheral instance number. Refer to the “Long Bit Names” section in the “Register
       and Nit Naming Conventions” chapter for more information.

       Table 27-2. SMT Long Bit Name Prefixes
                        Peripheral                                              Bit Name Prefix
                           SMT1                                                         SMT1


--- p436 ---
                                                                                                                     PIC18F27/47/57Q43
                                                                                                        SMT - Signal Measurement Timer

27.2.1 SMTxCON0

            Name:       SMTxCON0
            Address:    0x030C

            SMT Control Register 0

      Bit        7              6              5              4                    3               2           1              0
                EN                            STP            WPOL                SPOL            CPOL              PS[1:0]
  Access        R/W                           R/W            R/W                 R/W             R/W         R/W             R/W
   Reset         0                             0              0                    0               0          0               0

Bit 7 – EN SMT Enable
            Value      Description
            1          SMT is enabled
            0          SMT is disabled; internal states are reset, clock requests are disabled

Bit 5 – STP SMT Counter Halt Enable
            Value      Condition                      Description
            1          When SMTxTMR = SMTxPR          Counter remains at SMTxPR; period match interrupt occurs when clocked
            0          When SMTxTMR = SMTxPR          Counter resets to 0x000000; period match interrupt occurs when clocked

Bit 4 – WPOL SMT_window Input Polarity Control
            Value      Description
            1          SMT_window input is active-low/falling edge enabled
            0          SMT_window input is active-high/rising edge enabled

Bit 3 – SPOL SMT_signal Input Polarity Control
            Value      Description
            1          SMT_signal input is active-low/falling edge enabled
            0          SMT_signal input is active-high/rising edge enabled

Bit 2 – CPOL SMT Clock Input Polarity Control
            Value      Description
            1          SMTxTMR increments on the falling edge of the selected clock signal
            0          SMTxTMR increments on the rising edge of the selected clock signal

Bits 1:0 – PS[1:0] SMT Prescale Select
            Value      Description
            11         Prescaler = 1:8
            10         Prescaler = 1:4
            01         Prescaler = 1:2
            00         Prescaler = 1:1


--- p437 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                 SMT - Signal Measurement Timer

27.2.2 SMTxCON1

           Name:       SMTxCON1
           Address:    0x030D

           SMT Control Register 1

     Bit        7            6                5              4                   3           2       1                0
               GO          REPEAT                                                          MODE[3:0]
  Access       R/W          R/W                                                 R/W     R/W        R/W               R/W
   Reset        0            0                                                   0       0           0                0

Bit 7 – GO SMT GO Data Acquisition
           Value      Description
           1          Incrementing, acquiring data are enabled
           0          Incrementing, acquiring data are disabled

Bit 6 – REPEAT SMT Repeat Acquisition Enable
           Value      Description
           1          Repeat Data Acquisition mode is enabled
           0          Single Acquisition mode is enabled

Bits 3:0 – MODE[3:0] SMT Operation Mode Select
           Value      Description
           1111       Reserved
           1110       Reserved
           1101       Reserved
           1100       Reserved
           1011       Reserved
           1010       Windowed Counter
           1001       Gated Counter
           1000       Counter
           0111       Capture
           0110       Time-of-Flight
           0101       Gated Windowed Measurement
           0100       Windowed Measurement
           0011       High and Low Time Measurement
           0010       Period and Duty Cycle Acquisition
           0001       Gated Timer
           0000       Timer


--- p438 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                                SMT - Signal Measurement Timer

27.2.3 SMTxSTAT

            Name:       SMTxSTAT
            Address:    0x030E

            SMT Status Register

      Bit        7             6               5              4                  3         2          1             0
              CPRUP         CPWUP             RST                                          TS         WS            AS
  Access      R/W/HC        R/W/HC            R/W                                          R          R             R
   Reset         0             0               0                                           0          0             0

Bit 7 – CPRUP SMT Manual Period Buffer Update
            Value      Description
            1          Request write of SMTxTMR value to SMTxCPR registers
            0          SMTxCPR registers update is complete

Bit 6 – CPWUP SMT Manual Pulse-Width Buffer Update
            Value      Description
            1          Request write of SMTxTMR value to SMTxCPW registers
            0          SMTxCPW registers update is complete

Bit 5 – RST SMT Manual Timer Reset
            Value      Description
            1          Request Reset to SMTxTMR registers
            0          SMTxTMR registers update is complete

Bit 2 – TS SMT GO Value Status
            Value      Description
            1          SMTxTMR is incrementing
            0          SMTxTMR is not incrementing

Bit 1 – WS SMT Window Status
            Value      Description
            1          SMT window is open
            0          SMT window is closed

Bit 0 – AS SMT Signal Value Status
            Value      Description
            1          SMT acquisition is in progress
            0          SMT acquisition is not in progress


--- p439 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                  SMT - Signal Measurement Timer

27.2.4 SMTxCLK

            Name:        SMTxCLK
            Address:     0x030F

            SMT Clock Selection Register

      Bit        7                6        5              4                   3            2                1            0
                                                                                               CSEL[3:0]
  Access                                                                     R/W      R/W                  R/W          R/W
   Reset                                                                      0        0                    0            0

Bits 3:0 – CSEL[3:0] SMT Clock Selection
                     CSEL Value                         SOURCE                                        Active in Sleep
                     1111-1001                         Reserved                                             No
                        1000                             CLKR                                               No
                        0111                            EXTOSC                                              Yes
                        0110                             SOSC                                               Yes
                        0101                      MFINTOSC (31.25 kHz)                                      Yes
                        0100                      MFINTOSC (500 kHz)                                        Yes
                        0011                           LFINTOSC                                             Yes
                        0010                           HFINTOSC                                             Yes
                        0001                             FOSC                                               No
                        0000                            FOSC/4                                              No


--- p440 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                           SMT - Signal Measurement Timer

27.2.5 SMTxWIN

           Name:       SMTxWIN
           Address:    0x0311

           SMT Window Input Select Register

     Bit        7           6           5             4                   3           2           1               0
                                                                            WSEL[5:0]
  Access                              R/W           R/W                  R/W         R/W        R/W             R/W
   Reset                               0             0                    0           0          0               0

Bits 5:0 – WSEL[5:0] SMT Window Signal Selection
                      WSEL Value                       Window Source                            Active in Sleep
                    111111-101000                         Reserved                                    No
                        100111                           CLC8_OUT                                     No
                        100110                           CLC7_OUT                                     No
                        100101                           CLC6_OUT                                     No
                        100100                           CLC5_OUT                                     No
                        100011                           CLC4_OUT                                     No
                        100010                           CLC3_OUT                                     No
                        100001                           CLC2_OUT                                     No
                        100000                           CLC1_OUT                                     No
                        011111                            ZCD_OUT                                     No
                        011110                           CMP2_OUT                                     No
                        011101                           CMP1_OUT                                     No
                        011100                           NCO3_OUT                                     No
                        011011                           NCO2_OUT                                     No
                        011010                           NCO1_OUT                                     No
                        011001                            Reserved                                    No
                        011000                            Reserved                                    No
                        010111                         PWM3S1P2_OUT                                   No
                        010110                         PWM3S1P1_OUT                                   No
                        010101                         PWM2S1P2_OUT                                   No
                        010100                        PWM2S1P1_OUT                                    No
                        010011                        PWM1S1P2_OUT                                    No
                        010010                        PWM1S1P1_OUT                                    No
                        010001                          CCP3_OUT                                      No
                        010000                          CCP2_OUT                                      No
                        001111                          CCP1_OUT                                      No
                    001110-001010                        Reserved                                     No
                        001001                      TMR6_Postscaler_OUT                               No
                        001000                      TMR4_Postscaler_OUT                               No
                        000111                      TMR2_Postscaler_OUT                               No
                        000110                          TMR0_OUT                                      No
                        000101                            CLKREF                                      No
                        000100                            EXTOSC                                      Yes
                        000011                             SOSC                                       Yes
                        000010                      MFINTOSC (31.25 kHz)                              Yes
                        000001                           LFINTOSC                                     Yes


--- p441 ---
                                                                                     PIC18F27/47/57Q43
                                                                        SMT - Signal Measurement Timer

...........continued
           WSEL Value                   Window Source                        Active in Sleep
            000000                       SMT1WINPPS                                No


--- p442 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                      SMT - Signal Measurement Timer

27.2.6 SMTxSIG

            Name:      SMTxSIG
            Address:   0x0310

            SMT Signal Selection Register

      Bit        7            6              5             4                   3                 2           1             0
                                                                                    SSEL[5:0]
  Access                                    R/W          R/W                  R/W               R/W        R/W            R/W
   Reset                                     0            0                    0                 0          0              0

Bits 5:0 – SSEL[5:0] SMT Signal Selection
                            SSEL Value                                                        Source
                          111111-100110                                                      Reserved
                              100101                                                        CLC8_OUT
                              100100                                                        CLC7_OUT
                              001101                                                        CCP1_OUT
                              001111                                                        CCP3_OUT
                              010000                                                      PWM1S1P1_OUT
                              010010                                                      PWM2S1P1_OUT
                              010011                                                      PWM2S1P2_OUT
                              010100                                                      PWM3S1P1_OUT
                              010101                                                      PWM3S1P2_OUT
                              010110                                                         Reserved
                              010111                                                         Reserved
                              011000                                                        NCO1_OUT
                              011001                                                        NCO2_OUT
                              011010                                                        NCO3_OUT
                              011011                                                        CMP1_OUT
                              011100                                                        CMP2_OUT
                              011101                                                         ZCD_OUT
                              011110                                                        CLC1_OUT
                              011111                                                        CLC2_OUT
                              100000                                                       CLC3_OUT
                              100010                                                       CLC5_OUT
                              100001                                                       CLC4_OUT
                              100011                                                       CLC6_OUT
                              001110                                                       CCP2_OUT
                              010001                                                     PWM1S1P2_OUT
                          001100-001000                                                     Reserved
                              000111                                                   TMR6_Postscaler_OUT
                              000110                                                       TMR5_OUT
                              000101                                                   TMR4_Postscaler_OUT
                              000100                                                       TMR3_OUT
                              000011                                                   TMR2_Postscaler_OUT
                              000010                                                       TMR1_OUT
                              000001                                                       TMR0_OUT
                              000000                                                      SMT1SIGPPS


--- p443 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                              SMT - Signal Measurement Timer

27.2.7 SMTxTMR

           Name:       SMTxTMR
           Address:    0x0300

           SMT Timer Register

     Bit        23           22          21             20           19               18            17            16
                                                          TMR[23:16]
  Access        R/W         R/W          R/W           R/W         R/W               R/W           R/W            R/W
   Reset         0           0            0             0             0               0             0              0

     Bit        15           14          13             12          11                10             9             8
                                                          TMR[15:8]
  Access        R/W         R/W          R/W           R/W         R/W               R/W           R/W            R/W
   Reset         0           0            0             0           0                 0             0              0

     Bit         7           6            5              4                   3            2          1             0
                                                               TMR[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W           R/W            R/W
   Reset         0           0            0             0                    0        0             0              0

Bits 23:0 – TMR[23:0] SMT Timer Value

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • SMTxTMRU: Accesses the upper byte TMR[23:16]
           •   SMTxTMRH: Accesses the high byte TMR[15:8]
           •   SMTxTMRL: Accesses the low byte TMR[7:0]


--- p444 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                              SMT - Signal Measurement Timer

27.2.8 SMTxCPR

           Name:       SMTxCPR
           Address:    0x0303

           SMT Captured Period Register

     Bit         23          22           21            20                  19        18            17            16
                                                             CPR[23:16]
  Access         R           R            R              R                  R             R          R             R
   Reset         x           x            x              x                  x             x          x             x

     Bit         15          14           13            12                  11        10             9             8
                                                              CPR[15:8]
  Access         R           R            R              R                  R             R          R             R
   Reset         x           x            x              x                  x             x          x             x

     Bit         7           6            5              4                  3             2          1             0
                                                               CPR[7:0]
  Access         R           R            R              R                  R             R          R             R
   Reset         x           x            x              x                  x             x          x             x

Bits 23:0 – CPR[23:0] SMTxTMR Value at Time of Period Capture Event
         Reset States: POR/BOR = xxxxxxxxxxxxxxxxxxxxxxxx
                       All Other Resets = uuuuuuuuuuuuuuuuuuuuuuuu

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • SMTxCPRU: Accesses the upper byte CPR[23:16]
           •   SMTxCPRH: Accesses the high byte CPR[15:8]
           •   SMTxCPRL: Accesses the low byte CPR[7:0]


--- p445 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                              SMT - Signal Measurement Timer

27.2.9 SMTxCPW

           Name:       SMTxCPW
           Address:    0x0306

           SMT Captured Pulse-Width Register

     Bit        23           22          21             20           19               18            17            16
                                                           CPW[23:16]
  Access         R           R            R             R             R                   R          R             R
   Reset         x           x            x              x            x                   x          x             x

     Bit        15           14          13             12                  11        10             9             8
                                                              CPW[15:8]
  Access         R           R            R              R                  R             R          R             R
   Reset         x           x            x              x                  x             x          x             x

     Bit         7           6            5              4                  3             2          1             0
                                                              CPW[7:0]
  Access         R           R            R              R                  R             R          R             R
   Reset         x           x            x              x                  x             x          x             x

Bits 23:0 – CPW[23:0] SMTxTMR Value at Time of Capture Event
         Reset States: POR/BOR = xxxxxxxxxxxxxxxxxxxxxxxx
                       All Other Resets = uuuuuuuuuuuuuuuuuuuuuuuu

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • SMTxCPWU: Accesses the upper byte CPW[23:16]
           •   SMTxCPWH: Accesses the high byte CPW[15:8]
           •   SMTxCPWL: Accesses the low byte CPW[7:0]


--- p446 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                              SMT - Signal Measurement Timer

27.2.10 SMTxPR

           Name:       SMTxPR
           Address:    0x0309

           SMT Period Register

     Bit         23          22          21             20                  19        18            17            16
                                                              PR[23:16]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W           R/W            R/W
   Reset         1           1            1             1                    1        1             1              1

     Bit         15          14          13             12                  11        10             9             8
                                                               PR[15:8]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W           R/W            R/W
   Reset         1           1            1             1                    1        1             1              1

     Bit         7           6            5              4                   3            2          1             0
                                                                PR[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W           R/W            R/W
   Reset         1           1            1             1                    1        1             1              1

Bits 23:0 – PR[23:0] The SMTxTMR Value at Which the SMTxTMR Resets to Zero

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • SMTxPRU: Accesses the upper byte PR[23:16]
           •   SMTxPRH: Accesses the high byte PR[15:8]
           •   SMTxPRL: Accesses the low byte PR[7:0]


--- p447 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                       SMT - Signal Measurement Timer

27.3      Register Summary - SMT Control
Address     Name       Bit Pos.     7          6           5             4                3             2            1            0
                         7:0                                                   TMR[7:0]
 0x0300    SMT1TMR       15:8                                                 TMR[15:8]
                        23:16                                                TMR[23:16]
                         7:0                                             CPR[7:0]
 0x0303    SMT1CPR      15:8                                             CPR[15:8]
                        23:16                                           CPR[23:16]
                         7:0                                             CPW[7:0]
 0x0306    SMT1CPW      15:8                                            CPW[15:8]
                        23:16                                           CPW[23:16]
                         7:0                                              PR[7:0]
 0x0309     SMT1PR      15:8                                             PR[15:8]
                        23:16                                            PR[23:16]
0x030C     SMT1CON0      7:0        EN                    STP        WPOL         SPOL                 CPOL             PS[1:0]
0x030D     SMT1CON1      7:0       GO       REPEAT                                                         MODE[3:0]
0x030E      SMT1STAT     7:0      CPRUP     CPWUP         RST                                           TS           WS           AS
0x030F      SMT1CLK      7:0                                                                               CSEL[3:0]
0x0310       SMT1SIG     7:0                                                                  SSEL[5:0]
0x0311      SMT1WIN      7:0                                                                  WSEL[5:0]


--- p448 ---
