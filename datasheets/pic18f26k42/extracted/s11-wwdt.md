                      PIC18(L)F26/27/45/46/47/55/56/57K42
11.0     WINDOWED WATCHDOG
         TIMER (WWDT)
The Watchdog Timer (WDT) is a system timer that
generates a Reset if the firmware does not issue a
CLRWDT instruction within the time-out period. The
Watchdog Timer is typically used to recover the system
from unexpected events. The Windowed Watchdog
Timer (WWDT) differs in that CLRWDT instructions are
only accepted when they are performed within a
specific window during the time-out period.
The WWDT has the following features:
• Selectable clock source
• Multiple operating modes
  - WWDT is always On
  - WWDT is off when in Sleep
  - WWDT is controlled by software
  - WWDT is always Off
• Configurable time-out period is from 1 ms to 256s
  (nominal)
• Configurable window size from 12.5% to 100% of
  the time-out period
• Multiple Reset conditions


 2017-2021 Microchip Technology Inc.                    DS40001919G-page 178
                        PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 11-1:             WINDOWED WATCHDOG TIMER BLOCK DIAGRAM

                                                                                                                Rev. 10-000162D
                                                                                                                       1/27/2017


                                                                            WWDT
                                                                            Armed
                                                                                                               WDT
                                                                                                              Window
                                                                                                              Violation
                                                                               Window Closed
                                        Window
                                                                               Comparator
                    CLRWDT               Sizes


                                                  WINDOW

                    RESET


              Reserved         111
              Reserved         110
              Reserved         101
                                                            R
              Reserved         100                    18-bit Prescale
              Reserved         011                       Counter
                                                      E
                 SOSC          010
  MFINTOSC 31.25 kHz           001
             LFINTOSC          000


                   CS


                                                 PS

                                                                        R
                                                                           5-bit            Overflow
                                                                                                           WDT Time-out
                                                                        WDT Counter          Latch


        WDTE<1:0> = 01
                    SEN

        WDTE<1:0> = 11

        WDTE<1:0> = 10
                   Sleep


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 179
                      PIC18(L)F26/27/45/46/47/55/56/57K42
11.1     Independent Clock Source                        11.3     Time-out Period
The WWDT can derive its time base from either the        If the WDTCPS[4:0] Configuration bits default to
31 kHz LFINTOSC or 31.25 kHz MFINTOSC internal           0b11111, then the PS bits of the WDTCON0 register
oscillators, depending on the value of WDTE[1:0]         set the time-out period from 1 ms to 256 seconds
Configuration bits.                                      (nominal). If any value other than the default value is
If WDTE = 0b1x, then the clock source will be enabled    assigned to WDTCPS[4:0] Configuration bits, then the
depending on the WDTCCS[2:0] Configuration bits.         timer period will be based on the WDTCPS[4:0] bits in
                                                         the CONFIG3L register. After a Reset, the default time-
If WDTE = 0b01, the SEN bit may be set by software       out period is 2s.
to enable WWDT, and the clock source is enabled by
the CS bits in the WDTCON1 register.
                                                         11.4     Watchdog Window
Time intervals in this chapter are based on a minimum
nominal interval of 1 ms. See Section 44.0 “Electrical   The Windowed Watchdog Timer has an optional
Specifications” for LFINTOSC and MFINTOSC                Windowed mode that is controlled by the WDTCWS[2:0]
tolerances.                                              Configuration bits and WINDOW[2:0] bits of the
                                                         WDTCON1 register. In the Windowed mode, the
                                                         CLRWDT instruction must occur within the allowed
11.2     WWDT Operating Modes
                                                         window of the WDT period. Any CLRWDT instruction that
The Windowed Watchdog Timer module has four              occurs outside of this window will trigger a window
operating modes controlled by the WDTE[1:0] bits in      violation and will cause a WWDT Reset, similar to a
Configuration Words. See Table 11-1.                     WWDT time out. See Figure 11-2 for an example.
                                                         The window size is controlled by the WINDOW[2:0]
11.2.1        WWDT IS ALWAYS ON                          Configuration bits, or the WINDOW[2:0] bits of
When the WDTE bits of Configuration Words are set to     WDTCON1, if WDTCWS[2:0] = 111.
‘11’, the WWDT is always on.                             The five Most Significant bits of the WDTTMR register
WWDT protection is active during Sleep.                  are used to determine whether the window is open, as
                                                         defined by the WINDOW[2:0] bits of the WDTCON1
11.2.2        WWDT IS OFF IN SLEEP                       register.
When the WDTE bits of Configuration Words are set to     In the event of a window violation, a Reset will be
‘10’, the WWDT is on, except in Sleep.                   generated and the WDTWV bit of the PCON0 register
WWDT protection is not active during Sleep.              will be cleared. This bit is set by a POR or can be set in
                                                         firmware.
11.2.3        WWDT CONTROLLED BY
              SOFTWARE                                   11.5     Clearing the WWDT
When the WDTE bits of Configuration Words are set to     The WWDT is cleared when any of the following
‘01’, the WWDT is controlled by the SEN bit of the       conditions occur:
WDTCON0 register.
                                                         • Any Reset
WWDT protection is unchanged by Sleep. See               • Valid CLRWDT instruction is executed
Table 11-1 for more details.
                                                         • Device enters Sleep
                                                         • Exit Sleep by Interrupt
TABLE 11-1:       WWDT OPERATING MODES                   • WWDT is disabled
                                 Device       WWDT       • Oscillator Start-up Timer (OST) is running
   WDTE[1:0]          SEN
                                 Mode         Mode       • Any write to the WDTCON0 or WDTCON1
         11             X           X     Active           registers
                                 Awake    Active         11.5.1      CLRWDT CONSIDERATIONS
         10             X
                                  Sleep   Disabled                   (WINDOWED MODE)
                        1           X     Active         When in Windowed mode, the WWDT must be armed
         01
                        0           X     Disabled       before a CLRWDT instruction will clear the timer. This is
         00             X           X     Disabled       performed by reading the WDTCON0 register.
                                                         Executing a CLRWDT instruction without performing
                                                         such an arming action will trigger a window violation
                                                         regardless of whether the window is open or not.
                                                         See Table 11-2 for more information.


 2017-2021 Microchip Technology Inc.                                                     DS40001919G-page 180
                      PIC18(L)F26/27/45/46/47/55/56/57K42
11.6     Operation During Sleep
When the device enters Sleep, the WWDT is cleared.
If the WWDT is enabled during Sleep, the WWDT
resumes counting. When the device exits Sleep, the
WWDT is cleared again.
The WWDT remains clear until the Oscillator Start-up
Timer (OST) completes, if enabled. See Section
7.2.1.3 “Oscillator Start-up Timer (OST)” for more
information on the OST.
When a WWDT time-out occurs while the device is in
Sleep, no Reset is generated. Instead, the device
wakes up and resumes operation. The TO and PD bits
in the STATUS register are changed to indicate the
event. The RWDT bit in the PCON0 register can also be
used. See Section 4.0 “Memory Organization” for
more information.


TABLE 11-2:       WWDT CLEARING CONDITIONS
                                      Conditions                                                WWDT
WDTE[1:0] = 00
WDTE[1:0] = 01 and SEN = 0
WDTE[1:0] = 10 and enter Sleep
                                                                                                Cleared
CLRWDT Command
Oscillator Fail Detected
Exit Sleep + System Clock = SOSC, EXTRC, INTOSC, EXTCLK
Exit Sleep + System Clock = XT, HS, LP                                                Cleared until the end of OST
Change INTOSC divider (IRCF bits)                                                             Unaffected

FIGURE 11-2:           WINDOW PERIOD AND DELAY

                                                                                                      Rev. 10-000 163A
                                                                                                             11/8/201 3


                   CLRWDT Instruction
                   (or other WDT reset)
                                                   Window Period


                                 Window Closed                Window Open


                                 Window Delay                               Time-out Event
                           (window violation can occur)


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 181
                           PIC18(L)F26/27/45/46/47/55/56/57K42
11.7           Register Definitions: Windowed Watchdog Timer Control

REGISTER 11-1:                WDTCON0: WATCHDOG TIMER CONTROL REGISTER 0
        U-0              U-0         R/W(3)-q/q(2)         R/W(3)-q/q(2)    R/W(3)-q/q(2)   R/W(3)-q/q(2)       R/W(3)-q/q(2)   R/W-0/0
          —               —
                                                                              PS[4:0]                                              SEN
bit 7                                                                                                                                    bit 0


Legend:
R = Readable bit                    W = Writable bit                       U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                x = Bit is unknown                     -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                    ‘0’ = Bit is cleared                   q = Value depends on condition


bit 7-6             Unimplemented: Read as ‘0’
bit 5-1             PS[4:0]: Watchdog Timer Prescale Select bits(1)
                    Bit Value = Prescale Rate
                    11111 = Reserved. Results in minimum interval (1:32)
                          •
                          •
                          •
                    10011 = Reserved. Results in minimum interval (1:32)

                    10010 =    1:8388608 (223) (Interval 256s nominal)
                    10001 =    1:4194304 (222) (Interval 128s nominal)
                    10000 =    1:2097152 (221) (Interval 64s nominal)
                    01111 =    1:1048576 (220) (Interval 32s nominal)
                    01110 =    1:524288 (219) (Interval 16s nominal)
                    01101 =    1:262144 (218) (Interval 8s nominal)
                    01100 =    1:131072 (217) (Interval 4s nominal)
                    01011 =    1:65536 (Interval 2s nominal) (Reset value)
                    01010 =    1:32768 (Interval 1s nominal)
                    01001 =    1:16384 (Interval 512 ms nominal)
                    01000 =    1:8192 (Interval 256 ms nominal)
                    00111 =    1:4096 (Interval 128 ms nominal)
                    00110 =    1:2048 (Interval 64 ms nominal)
                    00101 =    1:1024 (Interval 32 ms nominal)
                    00100 =    1:512 (Interval 16 ms nominal)
                    00011 =    1:256 (Interval 8 ms nominal)
                    00010 =    1:128 (Interval 4 ms nominal)
                    00001 =    1:64 (Interval 2 ms nominal)
                    00000 =    1:32 (Interval 1 ms nominal)
bit 0               SEN: Software Enable/Disable for Watchdog Timer bit
                    If WDTE[1:0] = 1x:
                    This bit is ignored.
                    If WDTE[1:0] = 01:
                    1 = WDT is turned on
                    0 = WDT is turned off
                    If WDTE[1:0] = 00:
                    This bit is ignored.

Note 1:         Times are approximate. WDT time is based on 31 kHz LFINTOSC.
     2:         When WDTCPS [4:0] in CONFIG3L = 11111, the Reset value of PS[4:0] is 01011. Otherwise, the Reset value of
                PS[4:0] is equal to WDTCPS[4:0] in CONFIG3L.
          3:    When WDTCPS [4:0] in CONFIG3L ≠ 11111, these bits are read-only.
          4:    When the WWDT is configured to run using the SOSC as a clock source and the device is allowed to undergo a Reset,
                as triggered by a WDT time-out, the SOSC would also undergo a Reset. That means the SOSC will execute its start-up
                sequence which requires 1024 SOSC clock counts before it is made available for peripherals to use. So for example, if
                the WDT is set for a 1 ms time-out and the device is allowed to undergo a WDT Reset, then the actual WDT Reset
                period will be: WDT_PERIOD = (1/(SOSC_FREQUENCY) * 1024) + 1 ms.


 2017-2021 Microchip Technology Inc.                                                                                DS40001919G-page 182
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 11-2:             WDTCON1: WATCHDOG TIMER CONTROL REGISTER 1
    U-0        R/W -q/q(1) R/W(3)-q/q(1) R/W(3)-q/q(1)
                    (3)
                                                             U-0          R/W(4)-q/q(2)   R/W(4)-q/q(2)   R/W(4)-q/q(2)
        —                                                     —
                                   CS[2:0]                                                WINDOW[2:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                W = Writable bit          U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown        -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared      q = Value depends on condition


bit 7          Unimplemented: Read as ‘0’
bit 6-4        CS[2:0]: Watchdog Timer Clock Select bits
               111 = Reserved
                   •
                   •
                   •
               011 = Reserved
               010 = SOSC
               001 = MFINTOSC 31.25 kHz
               000 = LFINTOSC 31 kHz
bit 3          Unimplemented: Read as ‘0’
bit 2-0        WINDOW[2:0]: Watchdog Timer Window Select bits

                                        Window delay       Window opening
                   WINDOW[2:0]
                                        Percent of time    Percent of time
                          111                  N/A                 100
                          110                 12.5                 87.5
                          101                  25                  75
                          100                 37.5                 62.5
                          011                  50                  50
                          010                 62.5                 37.5
                          001                  75                  25
                          000                 87.5                 12.5

Note 1:       If WDTCCS [2:0] in CONFIG3H = 111, the Reset value of CS[2:0] is 000.
     2:      The Reset value of WINDOW[2:0] is determined by the value of WDTCWS[2:0] in the CONFIG3H register.
     3:      If WDTCCS[2:0] in CONFIG3H ≠ 111, these bits are read-only.
     4:      If WDTCWS[2:0] in CONFIG3H ≠ 111, these bits are read-only.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 183
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 11-3:           WDTPSL: WWDT PRESCALE SELECT LOW BYTE REGISTER (READ-ONLY)
     R-0/0            R-0/0          R-0/0              R-0/0       R-0/0         R-0/0          R-0/0          R-0/0
                                                           PSCNT[7:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                 W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            PSCNT[7:0]: Prescale Select Low Byte bits(1)

Note 1:      The 18-bit WDT prescale value, PSCNT[17:0] includes the WDTPSL, WDTPSH and the lower bits of the
             WDTTMR registers. PSCNT[17:0] is intended for debug operations and may not be read during normal
             operation.

REGISTER 11-4:           WDTPSH: WWDT PRESCALE SELECT HIGH BYTE REGISTER (READ-ONLY)
     R-0/0            R-0/0          R-0/0              R-0/0       R-0/0         R-0/0          R-0/0          R-0/0
                                                          PSCNT[15:8]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                 W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            PSCNT[15:8]: Prescale Select High Byte bits(1)

Note 1:      The 18-bit WDT prescale value, PSCNT[17:0] includes the WDTPSL, WDTPSH and the lower bits of the
             WDTTMR registers. PSCNT[17:0] is intended for debug operations and may not be read during normal
             operation.


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 184
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 11-5:           WDTTMR: WDT TIMER REGISTER (READ-ONLY)
     R-0/0            R-0/0         R-0/0              R-0/0      R-0/0           R-0/0        R-0/0          R-0/0
                               WDTTMR[4:0]                                        STATE             PSCNT[17:16]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-3            WDTTMR[4:0]: Watchdog Window Value bits


                                          WDT Window State
                     WINDOW                                           Open Percent
                                        Closed             Open
                       111               N/A           00000-11111         100
                       110       00000-00011           00100-11111         87.5
                       101       00000-00111           01000-11111          75
                       100       00000-01011           01100-11111         62.5
                       011       00000-01111           10000-11111          50
                       010       00000-10011           10100-11111         37.5
                       001       00000-10111           11000-11111          25
                       000       00000-11011           11100-11111         12.5

bit 2              STATE: WDT Armed Status bit
                   1 = WDT is armed
                   0 = WDT is not armed
bit 1-0            PSCNT[17:16]: Prescale Select Upper Byte bits(1)

Note 1:      The 18-bit WDT prescale value, PSCNT[17:0] includes the WDTPSL, WDTPSH and the lower bits of the
             WDTTMR registers. PSCNT[17:0] is intended for debug operations and may not be read during normal
             operation.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 185
                      PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 11-3:       SUMMARY OF REGISTERS ASSOCIATED WITH WINDOWED WATCHDOG TIMER
                                                                                                        Register
    Name           Bit 7      Bit 6        Bit 5      Bit 4    Bit 3     Bit 2       Bit 1      Bit 0
                                                                                                        on Page

WDTCON0             —           —                              PS[4:0]                          SEN       182
WDTCON1             —                     CS[2:0]               —                WINDOW[2:0]              183
WDTPSL                                                   PSCNT[7:0]                                       184
WDTPSH                                                  PSCNT[15:8]                                       184
WDTTMR                                  WDTTMR[4:0]                      STATE        PSCNT[17:16]        185
Legend: x = unknown, u = unchanged, – = unimplemented locations read as ‘0’. Shaded cells are not used by
        Windowed Watchdog Timer.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 186
