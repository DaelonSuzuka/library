                                                                                                   PIC18F27/47/57Q43
                                                                                      WWDT - Windowed Watchdog Timer


15.   WWDT - Windowed Watchdog Timer
      A Watchdog Timer (WDT) is a system timer that generates a Reset if the firmware does not
      issue a CLRWDT instruction within the time-out period. A Watchdog Timer is typically used to
      recover the system from unexpected events. The Windowed Watchdog Timer (WWDT) differs from
      nonwindowed operation in that CLRWDT instructions are only accepted when they are performed
      within a specific window during the time-out period.
      The WWDT has the following features:
      • Selectable clock source
      •   Multiple operating modes
           – WWDT is always on
           – WWDT is off when in Sleep
           – WWDT is controlled by software
           – WWDT is always off
      •   Configurable time-out period from 1 ms to 256s (nominal)
      •   Configurable window size from 12.5% to 100% of the time-out period
      •   Multiple Reset conditions


--- p253 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                          WWDT - Windowed Watchdog Timer

       Figure 15-1. Windowed Watchdog Timer Block Diagram

                                                                       WWDT
                                                                       Armed
                                                                                                        WDT
                                                                                                      Window
                                                                                                      Violation
                                                                          Window Closed
                                    Window
                                                                          Comparator
                     CLRWDT          Sizes


                                              WINDOW

                     RESET


                       ..
                        .                             R
                     See
                                               18-bit Prescale
                   WDTCON1
                                                  Counter
                    Register
                                               E
                       ..
                        .

                     CS


                                             PS

                                                                   R
                                                                      5-bit            Overflow
                                                                                                     WDT Time-out
                                                                   WDT Counter          Latch

             WDTE = b01
                     SEN

             WDTE = b11

             WDTE = b10
                    Sleep


15.1   Independent Clock Source
       The WWDT can derive its time base from either the 31 KHz LFINTOSC or 31.25 kHz MFINTOSC
       internal oscillators, depending on the value of WDT Operating Mode (WDTE) Configuration bits. If
       WDTE = ‘b1x, then the clock source will be enabled depending on the WDTCCS Configuration bits. If
       WDTE = ‘b01, the SEN bit will be set by software to enable WWDT and the clock source is enabled by
       the CS bits. Time intervals in this chapter are based on a minimum nominal interval of 1 ms. See the
       device Electrical Specifications for LFINTOSC and MFINTOSC tolerances.

15.2   WWDT Operating Modes
       The Windowed Watchdog Timer module has four operating modes that are controlled by the WDTE
       Configuration bit. The table below summarizes the different WWDT operating modes.


--- p254 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                             WWDT - Windowed Watchdog Timer

       Table 15-1. WWDT Operating Modes
              WDTE             SEN                        Device Mode                                WWDT Mode
               11               X                               X                                      Active
                                                             Awake                                     Active
               10               X
                                                              Sleep                                   Disabled
                                1                               X                                      Active
               01
                                0                               X                                     Disabled
               00               X                               X                                     Disabled


15.2.1 WWDT Is Always On
       When the WDTE Configuration bits are set to ‘b11, the WWDT is always on. WWDT protection is
       active during Sleep.

15.2.2 WWDT Is Off in Sleep
       When the WDTE Configuration bits are set to ‘b10, the WWDT is on, except in Sleep mode. WWDT
       protection is not active during Sleep.

15.2.3 WWDT Controlled by Software
       When the WDTE Configuration bits are set to ‘b01, the WWDT is controlled by the SEN bit. WWDT
       protection is unchanged by Sleep. See Table 15-1 for more details.

15.3   Time-Out Period
       When the WDTCPS Configuration bits are set to the default value of ‘b11111, the PS bits set the
       time-out period from 1 ms to 256 seconds (nominal). If any value other than the default value is
       assigned to the WDTCPS Configuration bits, then the timer period will be based on the WDTCPS
       Configuration bits. After a Reset, the default time-out period is 2s.

15.4   Watchdog Window
       The Windowed Watchdog Timer has an optional Windowed mode that is controlled by either the
       WDTCWS Configuration bits or the WINDOW bits. In the Windowed mode (WINDOW < ‘b1111),
       the CLRWDT instruction must occur within the allowed window of the WDT period. Any CLRWDT
       instruction that occurs outside of this window will trigger a window violation and will cause a WWDT
       Reset, similar to a WWDT time-out. See Figure 15-2 for an example.
       When the WDTCWS Configuration bits are ‘b111, then the window size is controlled by the WINDOW
       bits, otherwise the window size is controlled by the WDTCWS bits. The five Most Significant bits of
       the WDTTMR register are used to determine whether the window is open, as defined by the window
       size. In the event of a window violation, a Reset will be generated and the WDTWV bit of the PCON0
       register will be cleared. This bit is set by a POR and can be set by software.

       Figure 15-2. Window Period and Delay

                                CLRWDT Instruction
                               (or other WDT Reset)
                                                           Window Period


                                           Window Closed              Window Open

                                                                                    Time-out Event
                                           Window Delay
                                     (window violation can occur)


--- p255 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                  WWDT - Windowed Watchdog Timer

15.5   Clearing the Watchdog Timer
       The Watchdog Timer is cleared when any of the following conditions occur:
       • Any Reset
       •   A valid CLRWDT instruction is executed
       •   The device enters Sleep
       •   The devices exits Sleep by Interrupt
       •   The WWDT is disabled
       •   The Oscillator Start-up Timer (OST) is running
       •   Any write to the WDTCON0 or WDTCON1 registers

15.5.1 CLRWDT Considerations (Windowed Mode)
       When in Windowed mode, the WWDT must be armed before a CLRWDT instruction will clear the
       timer. This is performed by reading the WDTCON0 register. Executing a CLRWDT instruction without
       performing such an arming action will trigger a window violation regardless of whether the window
       is open or not. See Table 15-2 for more information.

15.6   Operation During Sleep
       When the device enters Sleep, the Watchdog Timer is cleared. If the WWDT is enabled during Sleep,
       the Watchdog Timer resumes counting. When the device exits Sleep, the Watchdog Timer is cleared
       again. The Watchdog Timer remains clear until the Oscillator Start-up Timer (OST) completes, if
       enabled. When a WWDT time-out occurs while the device is in Sleep, no Reset is generated. Instead,
       the device wakes up and resumes operation. The TO and PD bits in the STATUS register are changed
       to indicate the event. The RWDT bit in the PCON0 register indicates that a Watchdog Reset has
       occurred.

       Table 15-2. WWDT Clearing Conditions
                                           Conditions                                                        WWDT
       WDTE = ‘b00
       WDTE = ‘b01 and SEN = 0
       WDTE = ‘b10 and enter Sleep
                                                                                                             Cleared
       CLRWDT Command
       Oscillator Fail Detected
       Exit Sleep + System Clock = SOSC, EXTRC, INTOSC, EXTCLK
       Exit Sleep + System Clock = XT, HS, LP                                                      Cleared until the end of OST
       Change INTOSC divider (IRCF bits)                                                                   Unaffected


15.7   Register Definitions: Windowed Watchdog Timer Control
       Long bit name prefixes for the Windowed Watchdog Timer peripherals are shown in the following
       table. Refer to the "Long Bit Names" section in the “Register and Bit Naming Conventions”
       chapter for more information.

       Table 15-3. WDT Long Bit Name Prefixes
                           Peripheral                                                   Bit Name Prefix
                              WDT                                                               WDT


--- p256 ---
                                                                                                                     PIC18F27/47/57Q43
                                                                                                        WWDT - Windowed Watchdog Timer

15.7.1 WDTCON0

            Name:         WDTCON0
            Address:      0x078

            Watchdog Timer Control Register 0

      Bit        7                6               5               4                 3             2                  1           0
                                                                                 PS[4:0]                                        SEN
  Access                                         R/W             R/W              R/W        R/W                   R/W          R/W
   Reset                                          q               q                q          q                     q            0

Bits 5:1 – PS[4:0] Watchdog Timer Prescaler Select(2)
            Value        Description
            11111 to     Reserved. Results in minimum interval (1 ms)
            10011
            10010         1:8388608 (223) (Interval 256s nominal)
            10001         1:4194304 (222) (Interval 128s nominal)
            10000         1:2097152 (221) (Interval 64s nominal)
            01111         1:1048576 (220) (Interval 32s nominal)
            01110         1:524288 (219) (Interval 16s nominal)
            01101         1:262144 (218) (Interval 8s nominal)
            01100         1:131072 (217) (Interval 4s nominal)
            01011         1:65536 (Interval 2s nominal) (Reset value)
            01010         1:32768 (Interval 1s nominal)
            01001         1:16384 (Interval 512 ms nominal)
            01000         1:8192 (Interval 256 ms nominal)
            00111         1:4096 (Interval 128 ms nominal)
            00110         1:2048 (Interval 64 ms nominal)
            00101         1:1024 (Interval 32 ms nominal)
            00100         1:512 (Interval 16 ms nominal)
            00011         1:256 (Interval 8 ms nominal)
            00010         1:128 (Interval 4 ms nominal)
            00001         1:64 (Interval 2 ms nominal)
            00000         1:32 (Interval 1 ms nominal)

Bit 0 – SEN Software Enable/Disable for Watchdog Timer
                  Value                            Condition                                             Description
                     x                            If WDTE = 1x                                        This bit is ignored
                     1                            If WDTE = 01                                        WDT is turned on
                     0                            If WDTE = 01                                        WDT is turned off
                     x                            If WDTE = 00                                        This bit is ignored


            Notes:
            1. When the WDTCPS Configuration bits = ‘b11111, the Reset value (q) of WDTPS is ‘b01011.
               Otherwise, the Reset value of WDTPS is equal to the WDTCPS in Configuration bits.
            2. When the WDTCPS in Configuration bits ≠ ‘b11111, these bits are read-only.


--- p257 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                 WWDT - Windowed Watchdog Timer

15.7.2 WDTCON1

            Name:       WDTCON1
            Address:    0x079

            Watchdog Timer Control Register 1

      Bit        7           6             5               4                  3             2            1              0
                                         CS[2:0]                                                     WINDOW[2:0]
  Access                    R/W           R/W            R/W                           R/W              R/W            R/W
   Reset                     q             q              q                             q                q              q

Bits 6:4 – CS[2:0] Watchdog Timer Clock Select(1,3)
                                    CS                                                          Clock Source
                                  111-100                                                   Reserved
                                    011                                                      EXTOSC
                                    010                                                       SOSC
                                    001                                                MFINTOSC (31.25 kHz)
                                    000                                                 LFINTOSC (31 kHz)

Bits 2:0 – WINDOW[2:0] Watchdog Timer Window Select(2,4)
               WINDOW             Window Delay Percent of Time                      Window Opening Percent of Time
                 111                          N/A                                                     100
                 110                          12.5                                                    87.5
                 101                           25                                                      75
                 100                          37.5                                                    62.5
                 011                           50                                                      50
                 010                          62.5                                                    37.5
                 001                           75                                                      25
                 000                          87.5                                                    12.5

            Notes:
            1. When the WDTCCS in Configuration bits = ‘0b111, the Reset value of WDTCS is ‘b000.
            2. The Reset value (q) of WINDOW is determined by the value of WDTCWS in the Configuration bits.
            3. When the WDTCCS in Configuration bits ≠ ‘b111, these bits are read-only.
            4. When the WDTCWS in Configuration bits ≠ ‘b111, these bits are read-only.


--- p258 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                             WWDT - Windowed Watchdog Timer

15.7.3 WDTPSH

            Name:      WDTPSH
            Address:   0x07B

            WWDT Prescaler Select Register (Read-Only)

      Bit        7           6           5              4             3                  2            1            0
                                                          PSCNTH[7:0]
  Access         R           R           R              R            R                   R            R            R
   Reset         0           0           0              0             0                  0            0            0

Bits 7:0 – PSCNTH[7:0] Prescaler Select High Byte(1)

            Note:
            1. The 18-bit WDT prescaler value, PSCNT[17:0] includes the WDTPSL, WDTPSH and the lower bits
               of the WDTTMR registers. PSCNT[17:0] is intended for debug operations and will be read during
               normal operation.


--- p259 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                             WWDT - Windowed Watchdog Timer

15.7.4 WDTPSL

            Name:      WDTPSL
            Address:   0x07A

            WWDT Prescaler Select Register (Read-Only)

      Bit        7           6           5              4                  3             2            1            0
                                                            PSCNTL[7:0]
  Access         R           R           R              R                  R             R            R            R
   Reset         0           0           0              0                  0             0            0            0

Bits 7:0 – PSCNTL[7:0] Prescaler Select Low Byte(1)

            Note:
            1. The 18-bit WDT prescaler value, PSCNT[17:0] includes the WDTPSL, WDTPSH and the lower bits
               of the WDTTMR registers. PSCNT[17:0] is intended for debug operations and will be read during
               normal operation.


--- p260 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                  WWDT - Windowed Watchdog Timer

15.7.5 WDTTMR

            Name:             WDTTMR
            Address:          0x07C

            WDT Timer Register (Read-Only)

      Bit           7             6             5              4                  3             2          1           0
                                             TMR[4:0]                                         STATE         PSCNT[17:16]
  Access            R             R            R               R                  R             R          R           R
   Reset            0             0             0              0                  0             0          0           0

Bits 7:3 – TMR[4:0] Watchdog Window Value
                    WINDOW                               WDT Window State                                  Open Percent
                                               Closed                                 Open
                        111                      N/A                            00000-11111                    100
                        110                  00000-00011                        00100-11111                    87.5
                        101                  00000-00111                        01000-11111                     75
                        100                  00000-01011                        01100-11111                    62.5
                        011                  00000-01111                        10000-11111                     50
                        010                  00000-10011                        10100-11111                    37.5
                        001                  00000-10111                        11000-11111                     25
                        000                  00000-11011                        11100-11111                    12.5

Bit 2 – STATE WDT Armed Status
            Value         Description
            1             WDT is armed
            0             WDT is not armed

Bits 1:0 – PSCNT[17:16] Prescaler Select Upper Byte(1)

            Note:
            1. The 18-bit WDT prescaler value, PSCNT[17:0] includes the WDTPSL, WDTPSH and the lower bits
               of the WDTTMR registers. PSCNT[17:0] is intended for debug operations and will not be read
               during normal operation.


--- p261 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                         WWDT - Windowed Watchdog Timer

15.8      Register Summary - WDT Control
Address     Name     Bit Pos.   7        6            5            4                 3      2          1          0
 0x78      WDTCON0     7:0                                                     PS[4:0]                           SEN
 0x79      WDTCON1     7:0                         CS[2:0]                                        WINDOW[2:0]
 0x7A       WDTPSL     7:0                                             PSCNTL[7:0]
 0x7B      WDTPSH      7:0                                         PSCNTH[7:0]
 0x7C      WDTTMR      7:0                        TMR[4:0]                                STATE        PSCNT[17:16]


--- p262 ---
