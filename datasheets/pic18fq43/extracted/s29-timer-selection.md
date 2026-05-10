                                                                                                   PIC18F27/47/57Q43
                                                                                     Capture, Compare, and PWM Timers
                                                                                                             Selection

29.    Capture, Compare, and PWM Timers Selection
       Each of these modules has an independent timer selection which can be accessed using the timer
       selection register. The default timer selection is Timer1 for capture or compare functions and Timer2
       for PWM functions.

29.1   Register Definitions: Capture, Compare, and PWM Timers Selection


--- p462 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                               Capture, Compare, and PWM Timers
                                                                                                                       Selection
29.1.1 CCPTMRS0

            Name:      CCPTMRS0
            Address:   0x34C

            CCP Timers Selection Register

      Bit        7           6              5          4                    3             2              1            0
                                           C3TSEL[1:0]                        C2TSEL[1:0]                 C1TSEL[1:0]
  Access                                R/W          R/W                   R/W          R/W            R/W          R/W
   Reset                                 0             1                    0             1             0             1

Bits 0:1, 2:3, 4:5 – CnTSEL CCPn Timer Selection
                       CnTSEL Value                                 Capture/Compare                               PWM
                            11                                             Timer5                                Timer6
                            10                                             Timer3                                Timer4
                            01                                             Timer1                                Timer2
                            00                                                      Reserved


--- p463 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                         Capture, Compare, and PWM Timers
                                                                                                                 Selection
29.2      Register Summary - Capture, Compare, and PWM Timers Selection
Address     Name      Bit Pos.   7        6           5                 4     3                 2       1                 0
 0x034C    CCPTMRS0     7:0                               C3TSEL[1:0]             C2TSEL[1:0]               C1TSEL[1:0]


--- p464 ---
