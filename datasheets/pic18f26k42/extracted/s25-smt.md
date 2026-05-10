                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.0     SIGNAL MEASUREMENT TIMER
         (SMT)
The SMT is a 24-bit counter with advanced clock and
gating logic, which can be configured for measuring a
variety of digital signal parameters such as pulse width,
frequency and duty cycle, and the time difference
between edges on two signals. The device has only
one SMT module implemented.
Features of the SMT include:
• 24-bit timer/counter
  - Three 8-bit registers (SMT1L/H/U)
  - Readable and writable
  - Optional 16-bit operating mode
• Two 24-bit measurement capture registers
• One 24-bit period match register
• Multi-mode operation, including relative timing
  measurement
• Interrupt on period match
• Multiple clock, gate and signal sources
• Interrupt on acquisition complete
• Ability to read current input values


 2017-2021 Microchip Technology Inc.                       DS40001919G-page 362
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 25-1:            SMT BLOCK DIAGRAM


                                                                                                                 Rev. 10-000161E
                                                                                                                       10/12/2016


                                                                             Period Latch
                                                                                                 Set SMTxPRAIF
              SMT_window         SMT
                                Clock                                          SMTxPR
                                Sync
                                Circuit
                                                 Control       Set SMTxIF
                                                  Logic                       Comparator
               SMT_signal        SMT
                                Clock
                                Sync
                                Circuit

                                                                                            24-bit
                                                                    Reset                                SMTxCPR
                                                                                            Buffer

                                                                   Enable     SMTxTMR       24-bit
                                                                                                         SMTxCPW
                       CLKR     111                                                         Buffer

                       SOSC     110                          Window Latch
                                                                                                 Set SMTxPWAIF
               MFINTOSC/16      101
                 MFINTOSC       100
                                          Prescaler
                  LFINTOSC      011
                 HFINTOSC       010
                       FOSC     001
                     FOSC/4     000


                    CSEL<2:0>


FIGURE 25-2:            SMT SIGNAL AND WINDOW BLOCK DIAGRAM
                                                                                                                          Rev. 10-000173D
                                                                                                                                10/12/2016


              See                                                             See
            SMTxSIG                                   SMT_signal            SMTxWIN                    SMT_window
            Register                                                         Register


              SSEL<4:0>                                                     WSEL<4:0>


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 363
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.1     SMT Operation                                      25.2.3      PERIOD LATCH REGISTERS
The core of the module is the 24-bit counter,               The SMT1CPR registers are the 24-bit SMT period
SMT1TMR combined with a complex data acquisition            latch. They are used to latch in other values of the
front-end. Depending on the mode of operation               SMT1TMR when triggered by various other signals,
selected, the SMT can perform a variety of                  which are determined by the mode the SMT is currently
measurements summarized in Table 25-1.                      in.
                                                            The SMT1CPR registers can also be updated with the
25.1.1      CLOCK SOURCES                                   current value of the SMT1TMR value by setting the
Clock sources available to the SMT include:                 CPRUP bit in the SMT1STAT register.
• FOSC
                                                            25.3     Halt Operation
• FOSC/4
• HFINTOSC 16 MHz                                           The counter can be prevented from rolling-over using
• LFINTOSC                                                  the STP bit in the SMT1CON0 register. When halting is
                                                            enabled, the period match interrupt persists until the
• MFINTOSC 31.25 kHz
                                                            SMT1TMR is reset (either by a manual Reset, Section
The SMT clock source is selected by configuring the         25.2.1 “Time Base”) or by clearing the GO bit of the
CSEL[2:0] bits in the SMT1CLK register. The clock           SMT1CON1 register and writing the SMT1TMR values
source can also be prescaled using the PS[1:0] bits of      in software.
the SMT1CON0 register. The prescaled clock source is
used to clock both the counter and any synchronization      25.4     Polarity Control
logic used by the module.
                                                            The three input signals for the SMT have polarity
25.1.2      PERIOD MATCH INTERRUPT                          control to determine whether or not they are active-
Similar to other timers, the SMT triggers an interrupt      high/positive edge or active-low/negative edge signals.
when SMT1TMR rolls over to ‘0’. This happens when           The following bits apply to Polarity Control:
SMT1TMR = SMT1PR, regardless of mode. Hence, in
                                                            • WSEL bit (Window Polarity)
any mode that relies on an external signal or a window
to reset the timer, proper operation requires that          • SSEL bit (Signal Polarity)
SMT1PR be set to a period larger than that of the           • CSEL bit (Clock Polarity)
expected signal or window.                                  These bits are located in the SMT1CON0 register.

25.2     Basic Timer Function Registers                     25.5     Status Information
The SMT1TMR time base and the SMT1CPW/                      The SMT provides input status information for the user
SMT1PR/SMT1CPR buffer registers serve several               without requiring the need to deal with the polarity of
functions and can be manually updated using software.       the incoming signals.

25.2.1      TIME BASE                                       25.5.1      WINDOW STATUS
The SMT1TMR is the 24-bit counter that is the center of     Window status is determined by the WS bit of the
the SMT. It is used as the basic counter/timer for          SMT1STAT register. This bit is only used in Windowed
measurement in each of the modes of the SMT. It can be      Measure, Gated Counter and Gated Window Measure
reset to a value of 24’h00_0000 by setting the RST bit of   modes, and is only valid when TS = 1, and will be
the SMT1STAT register. It can be written to and read        delayed in time by synchronizer delays in non-Counter
from software, but it is not guarded for atomic access,     modes.
therefore reads and writes to the SMT1TMR may only
be made when the GO = 0, or the software may have           25.5.2      SIGNAL STATUS
other measures to ensure integrity of SMT1TMR reads/
                                                            Signal status is determined by the AS bit of the
writes.
                                                            SMT1STAT register. This bit is used in all modes
                                                            except Window Measure, Time of Flight and Capture
25.2.2      PULSE-WIDTH LATCH REGISTERS
                                                            modes, and is only valid when TS = 1, and will be
The SMT1CPW registers are the 24-bit SMT pulse-             delayed in time by synchronizer delays in non-Counter
width latch. They are used to latch in the value of the     modes.
SMT1TMR when triggered by various signals, which
are determined by the mode the SMT is currently in.         25.5.3      GO STATUS
The SMT1CPW registers can also be updated with the
                                                            Timer run status is determined by the TS bit of the
current value of the SMT1TMR value by setting the
                                                            SMT1STAT register, and will be delayed in time by
CPWUP bit of the SMT1STAT register.
                                                            synchronizer delays in non-Counter modes.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 364
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6     Modes of Operation                                       25.6.1     TIMER MODE
The modes of operation are summarized in Table 25-1.              Timer mode is the simplest mode of operation where
The following sections provide detailed descriptions,             the SMT1TMR is used as a 16/24-bit timer. No data
examples of how the modes can be used. Note that all              acquisition takes place in this mode. The timer
waveforms assume WPOL/SPOL/CPOL = 0. When                         increments as long as the GO bit has been set by
WPOL/SPOL/CPOL = 1, all SMTSIGx, SMTWINx and                      software. No SMT window or SMT signal events affect
SMT clock signals will have a polarity opposite to that           the GO bit. Everything is synchronized to the SMT
indicated. For all modes, the REPEAT bit controls                 clock source. When the timer experiences a period
whether the acquisition is repeated or single. When               match (SMT1TMR = SMT1PR), SMT1TMR is reset
REPEAT = 0 (Single Acquisition mode), the timer will              and the period match interrupt trips. See Figure 25-3.
stop incrementing and the GO bit will be reset upon the
completion of an acquisition. Otherwise, the timer will
continue and allow for continued acquisitions to
overwrite the previous ones until the timer is stopped in
software.


TABLE 25-1:        MODES OF OPERATION
                                                        Synchronous
     MODE                  Mode of Operation                                              Reference
                                                         Operation
       0000      Timer                                      Yes        Section 25.6.1 “Timer Mode”
       0001      Gated Timer                                Yes        Section 25.6.2 “Gated Timer Mode”
       0010      Period and Duty Cycle Acquisition          Yes        Section 25.6.3 “Period and Duty Cycle Mode”
       0011      High and Low Time Measurement              Yes        Section 25.6.4 “High and Low Measure Mode”
       0100      Windowed Measurement                       Yes        Section 25.6.5 “Windowed Measure Mode”
       0101      Gated Windowed Measurement                 Yes        Section 25.6.6 “Gated Windowed Measure Mode”
       0110      Time of Flight                             Yes        Section 25.6.7 “Time of Flight Measure Mode”
       0111      Capture                                    Yes        Section 25.6.8 “Capture Mode”
       1000      Counter                                    No         Section 25.6.9 “Counter Mode”
       1001      Gated Counter                              No         Section 25.6.10 “Gated Counter Mode”
       1010      Windowed Counter                           No         Section 25.6.11 “Windowed Counter Mode”
  1011-1111      Reserved                                   —          —


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 365
                                        FIGURE 25-3:         TIMER MODE TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                              Rev. 10-000 174A
                                                                                                                                                                                    12/19/201 3


                                                SMTx Clock


                                                                                                                                                                                                  PIC18(L)F26/27/45/46/47/55/56/57K42
                                                  SMTxEN

                                                 SMTxGO

                                               SMTxGO_sync

                                                  SMTxPR                                                                 11

                                                 SMTxTMR                   0             1   2   3   4   5   6   7   8        9 10 11 0   1   2   3   4   5   6   7   8   9

                                                  SMTxIF
DS40001919G-page 366
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.2      GATED TIMER MODE
Gated Timer mode uses the SMTSIGx input to control
whether or not the SMT1TMR will increment. Upon a
falling edge of the external signal, the SMT1CPW
register will update to the current value of the
SMT1TMR. Example waveforms for both repeated and
single acquisitions are provided in Figure 25-4 and
Figure 25-5.


 2017-2021 Microchip Technology Inc.                 DS40001919G-page 367
                                        FIGURE 25-4:       GATED TIMER MODE REPEAT ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                   Rev. 10-000 176A
                                                                                                                                         12/19/201 3


                                                SMTx_signal

                                             SMTx_signalsync


                                                                                                                                                       PIC18(L)F26/27/45/46/47/55/56/57K42
                                                 SMTx Clock

                                                    SMTxEN

                                                    SMTxGO

                                               SMTxGO_sync

                                                    SMTxPR                                              0xFFFFFF

                                                  SMTxTMR                    0                  1   2    3   4     5       6   7

                                                  SMTxCPW                                                              5       7

                                                SMTxPWAIF
DS40001919G-page 368
                                        FIGURE 25-5:       GATED TIMER MODE SINGLE ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                            Rev. 10-000 175A
                                                                                                                                  12/19/201 3


                                                SMTx_signal


                                                                                                                                                PIC18(L)F26/27/45/46/47/55/56/57K42
                                             SMTx_signalsync

                                                 SMTx Clock

                                                    SMTxEN

                                                    SMTxGO

                                               SMTxGO_sync

                                                    SMTxPR                                               0xFFFFFF

                                                  SMTxTMR                   0                    1   2    3   4     5

                                                  SMTxCPW                                                               5

                                                SMTxPWAIF
DS40001919G-page 369
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.3      PERIOD AND DUTY CYCLE MODE
In Duty Cycle mode, either the duty cycle or period
(depending on polarity) of the SMT1_signal can be
acquired relative to the SMT clock. The CPW register is
updated on a falling edge of the signal, and the CPR
register is updated on a rising edge of the signal, along
with the SMT1TMR resetting to 0x0001. In addition, the
GO bit is reset on a rising edge when the SMT is in
Single Acquisition mode. See Figure 25-6 and
Figure 25-7.


 2017-2021 Microchip Technology Inc.                       DS40001919G-page 370
                                        FIGURE 25-6:       PERIOD AND DUTY-CYCLE REPEAT ACQUISITION MODE TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                       Rev. 10-000 177A
                                                                                                                                                                             12/19/201 3


                                                  SMTx_signal


                                                                                                                                                                                           PIC18(L)F26/27/45/46/47/55/56/57K42
                                               SMTx_signalsync

                                                   SMTx Clock

                                                        SMTxEN

                                                       SMTxGO

                                                 SMTxGO_sync

                                                       SMTxTMR                 0                  1   2   3   4   5   6   7   8   9 10 11 1   2   3   4            5

                                                    SMTxCPW                                                                       5                            2

                                                       SMTxCPR                                                                                            11

                                                  SMTxPWAIF

                                                   SMTxPRAIF
DS40001919G-page 371
                                        FIGURE 25-7:       PERIOD AND DUTY-CYCLE SINGLE ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                     Rev. 10-000 178A
                                                                                                                                                           12/19/201 3


                                                  SMTx_signal


                                                                                                                                                                         PIC18(L)F26/27/45/46/47/55/56/57K42
                                               SMTx_signalsync

                                                   SMTx Clock

                                                       SMTxEN

                                                       SMTxGO

                                                 SMTxGO_sync

                                                    SMTxTMR                    0                  1   2   3   4   5   6   7   8   9 10 11

                                                    SMTxCPW                                                                                 5

                                                    SMTxCPR                                                                                     11

                                                  SMTxPWAIF

                                                   SMTxPRAIF
DS40001919G-page 372
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.4      HIGH AND LOW MEASURE MODE
This mode measures the high and low pulse time of the
SMTSIGx relative to the SMT clock. It begins
incrementing the SMT1TMR on a rising edge on the
SMTSIGx input, then updates the SMT1CPW register
with the value and resets the SMT1TMR on a falling
edge, starting to increment again. Upon observing
another rising edge, it updates the SMT1CPR register
with its current value and once again resets the
SMT1TMR value and begins incrementing again. See
Figure 25-8 and Figure 25-9.


 2017-2021 Microchip Technology Inc.                   DS40001919G-page 373
                                        FIGURE 25-8:        HIGH AND LOW MEASURE MODE REPEAT ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                           Rev. 10-000 180A
                                                                                                                                                                                 12/19/201 3


                                                   SMTx_signal


                                                                                                                                                                                               PIC18(L)F26/27/45/46/47/55/56/57K42
                                                SMTx_signalsync

                                                       SMTx Clock

                                                         SMTxEN

                                                         SMTxGO

                                                  SMTxGO_sync

                                                        SMTxTMR                 0                  1   2   3   4   5   1   2   3   4   5   6   1   2   1   2           3

                                                       SMTxCPW                                                                     5                               2

                                                        SMTxCPR                                                                                                6

                                                   SMTxPWAIF

                                                       SMTxPRAIF
DS40001919G-page 374
                                        FIGURE 25-9:        HIGH AND LOW MEASURE MODE SINGLE ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                  Rev. 10-000 179A
                                                                                                                                                        12/19/201 3


                                             SMTx_signal


                                                                                                                                                                      PIC18(L)F26/27/45/46/47/55/56/57K42
                                          SMTx_signalsync

                                              SMTx Clock

                                                 SMTxEN

                                                 SMTxGO

                                            SMTxGO_sync

                                               SMTxTMR                     0                  1   2   3   4   5   1   2   3   4   5   6

                                               SMTxCPW                                                                                    5

                                               SMTxCPR                                                                                        6

                                             SMTxPWAIF

                                              SMTxPRAIF
DS40001919G-page 375
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.5      WINDOWED MEASURE MODE
This mode measures the window duration of the
SMTWINx input of the SMT. It begins incrementing the
timer on a rising edge of the SMTWINx input and
updates the SMT1CPR register with the value of the
timer and resets the timer on a second rising edge. See
Figure 25-10 and Figure 25-11.


 2017-2021 Microchip Technology Inc.                     DS40001919G-page 376
                                        FIGURE 25-10:    WINDOWED MEASURE MODE REPEAT ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                                Rev. 10-000 182A
                                                                                                                                                                                      12/19/201 3


                                                    SMTxWIN


                                                                                                                                                                                                    PIC18(L)F26/27/45/46/47/55/56/57K42
                                                SMTxWIN_sync

                                                  SMTx Clock

                                                     SMTxEN

                                                    SMTxGO

                                                SMTxGO_sync

                                                   SMTxTMR           0          1   2   3   4   5   6   7   8   9 10 11 12 1   2   3   4    5   6   7   8   1   2   3       4

                                                    SMTxCPR                                                                            12                               8

                                                  SMTxPRAIF
DS40001919G-page 377
                                        FIGURE 25-11:    WINDOWED MEASURE MODE SINGLE ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                  Rev. 10-000 181A
                                                                                                                                        12/19/201 3


                                                   SMTxWIN


                                                                                                                                                      PIC18(L)F26/27/45/46/47/55/56/57K42
                                               SMTxWIN_sync

                                                 SMTx Clock

                                                    SMTxEN

                                                   SMTxGO

                                               SMTxGO_sync

                                                  SMTxTMR           0           1   2   3   4   5   6   7   8   9 10 11 12

                                                   SMTxCPR                                                                   12

                                                 SMTxPRAIF
DS40001919G-page 378
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.6      GATED WINDOWED MEASURE
            MODE
This mode measures the duty cycle of the SMT1_signal
input over a known input window. It does so by
incrementing the timer on each pulse of the clock signal
while the SMT1_signal input is high, updating the
SMT1CPR register and resetting the timer on every
rising edge of the SMTWINx input after the first. See
Figure 25-12 and Figure 25-13.


 2017-2021 Microchip Technology Inc.                      DS40001919G-page 379
                                        FIGURE 25-12:      GATED WINDOWED MEASURE MODE REPEAT ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                     Rev. 10-000 184A
                                                                                                                                           12/19/201 3


                                                   SMTxWIN


                                                                                                                                                         PIC18(L)F26/27/45/46/47/55/56/57K42
                                              SMTxWIN_sync

                                                SMTx_signal

                                             SMTx_signalsync

                                                 SMTx Clock

                                                    SMTxEN

                                                    SMTxGO

                                               SMTxGO_sync

                                                  SMTxTMR           0          1    2       3    4   5   6       0       1   2   3        0

                                                  SMTxCPR                                                            6                 3

                                                 SMTxPRAIF
DS40001919G-page 380
                                        FIGURE 25-13:      GATED WINDOWED MEASURE MODE SINGLE ACQUISITION TIMING DIAGRAMS
DS40001919G-page 381


                                                                                                                                                        PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                                                                    Rev. 10-000 183A
                                                                                                                                          12/19/201 3


                                                     SMTxWIN

                                                SMTxWIN_sync

                                                  SMTx_signal

                                               SMTx_signalsync

                                                   SMTx Clock

                                                      SMTxEN

                                                      SMTxGO

                                                 SMTxGO_sync

                                                    SMTxTMR           0         1    2       3     4   5                    6

                                                    SMTxCPR                                                                     6

                                                   SMTxPRAIF
 2017-2021 Microchip Technology Inc.
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.7      TIME OF FLIGHT MEASURE MODE
This mode measures the time interval between a rising
edge on the SMTWINx input and a rising edge on the
SMT1_signal input, beginning to increment the timer
upon observing a rising edge on the SMTWINx input,
while updating the SMT1CPR register and resetting the
timer upon observing a rising edge on the SMT1_signal
input. In the event of two SMTWINx rising edges
without an SMT1_signal rising edge, it will update the
SMT1CPW register with the current value of the timer
and reset the timer value. See Figure 25-14 and
Figure 25-15.


 2017-2021 Microchip Technology Inc.                    DS40001919G-page 382
                                        FIGURE 25-14:     TIME OF FLIGHT MODE REPEAT ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                    Rev. 10-000186A
                                                                                                                                                                           4/22/2016


                                              SMTxWIN


                                                                                                                                                                                       PIC18(L)F26/27/45/46/47/55/56/57K42
                                         SMTxWIN_sync

                                            SMTx_signal

                                        SMTx_signalsync

                                            SMTx Clock

                                               SMTxEN

                                               SMTxGO

                                          SMTxGO_sync

                                             SMTxTMR        0      1   2   3   4        5                     1       2   3   4   5   6   7   8   9 10 11 12 13 1        2

                                             SMTxCPW                                                                                                                13

                                              SMTxCPR                                                             4

                                            SMTxPWAIF

                                            SMTxPRAIF
DS40001919G-page 383
                                        FIGURE 25-15:     TIME OF FLIGHT MODE SINGLE ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                      Rev. 10-000185A
                                                                                                                             4/26/2016


                                                   SMTxWIN

                                              SMTxWIN_sync


                                                                                                                                         PIC18(L)F26/27/45/46/47/55/56/57K42
                                                SMTx_signal

                                             SMTx_signalsync

                                                 SMTx Clock

                                                    SMTxEN

                                                    SMTxGO

                                               SMTxGO_sync

                                                  SMTxTMR       0     1   2   3   4                               5

                                                  SMTxCPW

                                                  SMTxCPR                                                         4

                                                SMTxPWAIF

                                                 SMTxPRAIF
DS40001919G-page 384
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.8      CAPTURE MODE
This mode captures the Timer value based on a rising
or falling edge on the SMTWINx input and triggers an
interrupt. This mimics the capture feature of a CCP
module. The timer begins incrementing upon the GO
bit being set, and updates the value of the SMT1CPR
register on each rising edge of SMTWINx, and updates
the value of the CPW register on each falling edge of
the SMTWINx. See Figure 25-16 and Figure 25-17.


 2017-2021 Microchip Technology Inc.                   DS40001919G-page 385
                                        FIGURE 25-16:      CAPTURE MODE REPEAT ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                         Rev. 10-000 188A
                                                                                                                                                                               12/19/201 3


                                                    SMTxWIN


                                                                                                                                                                                             PIC18(L)F26/27/45/46/47/55/56/57K42
                                                SMTxWIN_sync

                                                  SMTx Clock

                                                        SMTxEN

                                                    SMTxGO

                                                SMTxGO_sync

                                                   SMTxTMR       0   1   2   3   4   5   6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32

                                                   SMTxCPW                                                 3                                           19                      32

                                                    SMTxCPR                                            2                                          18                      31

                                                  SMTxPWAIF

                                                  SMTxPRAIF
DS40001919G-page 386
                                        FIGURE 25-17:    CAPTURE MODE SINGLE ACQUISITION TIMING DIAGRAM
DS40001919G-page 387


                                                                                                                                      PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                                                  Rev. 10-000 187A
                                                                                                                        12/19/201 3


                                                    SMTxWIN

                                                SMTxWIN_sync

                                                  SMTx Clock

                                                     SMTxEN

                                                    SMTxGO

                                                SMTxGO_sync

                                                   SMTxTMR     0   1   2                                  3

                                                   SMTxCPW                                                    3

                                                    SMTxCPR                                               2

                                                  SMTxPWAIF

                                                  SMTxPRAIF
 2017-2021 Microchip Technology Inc.
                                        25.6.9     COUNTER MODE
 2017-2021 Microchip Technology Inc.


                                        This mode increments the timer on each pulse of the SMT1_signal input. This
                                        mode is asynchronous to the SMT clock and uses the SMT1_signal as a time
                                        source. The SMT1CPW register will be updated with the current SMT1TMR
                                        value on the rising edge of the SMT1WIN input. See Figure 25-18.

                                        FIGURE 25-18:        COUNTER MODE TIMING DIAGRAM


                                                                                                                                                                                                           PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                                                                                                                        Rev. 10-000189A
                                                                                                                                                                                               4/12/2016


                                                         SMTxWIN

                                                       SMTx_signal

                                                          SMTxEN

                                                          SMTxGO

                                                         SMTxTMR              0             1   2   3   4   5   6   7   8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26        27

                                                        SMTxCPW                                                                                        12                          25
DS40001919G-page 388
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.10     GATED COUNTER MODE
This mode counts pulses on the SMT1_signal input,
gated by the SMT1WIN input. It begins incrementing
the timer upon seeing a rising edge of the SMT1WIN
input and updates the SMT1CPW register upon a
falling edge on the SMT1WIN input. See Figure 25-
19 and Figure 25-20.


 2017-2021 Microchip Technology Inc.                DS40001919G-page 389
                                        FIGURE 25-19:     GATED COUNTER MODE REPEAT ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                           Rev. 10-000190A
                                                                                                                                                 12/18/2013


                                                   SMTxWIN

                                                 SMTx_signal


                                                                                                                                                                  PIC18(L)F26/27/45/46/47/55/56/57K42
                                                     SMTxEN

                                                    SMTxGO

                                                   SMTxTMR         0                     1   2   3   4   5   6   7   8       9 10 11 12   13

                                                   SMTxCPW                                                               8                13

                                                 SMTxPWAIF


                                        FIGURE 25-20:     GATED COUNTER MODE SINGLE ACQUISITION TIMING DIAGRAM
                                                                                                                                               Rev. 10-000191A
                                                                                                                                                     12/18/2013


                                                    SMTxWIN

                                                  SMTx_signal

                                                     SMTxEN

                                                     SMTxGO
DS40001919G-page 390


                                                   SMTxTMR         0                     1   2   3   4   5   6   7   8

                                                   SMTxCPW                                                               8

                                                  SMTxPWAIF
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.6.11     WINDOWED COUNTER MODE
This mode counts pulses on the SMT1_signal input,
within a window dictated by the SMT1WIN input. It
begins counting upon seeing a rising edge of the
SMT1WIN input, updates the SMT1CPW register on a
falling edge of the SMT1WIN input, and updates the
SMT1CPR register on each rising edge of the
SMT1WIN input beyond the first. See Figure 25-21 and
Figure 25-22.


 2017-2021 Microchip Technology Inc.                  DS40001919G-page 391
                                        FIGURE 25-21:        WINDOWED COUNTER MODE REPEAT ACQUISITION TIMING DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                     Rev. 10-000192A
                                                                                                                                                                           12/18/2013


                                                 SMTxWIN

                                               SMTx_signal


                                                                                                                                                                                        PIC18(L)F26/27/45/46/47/55/56/57K42
                                                  SMTxEN

                                                  SMTxGO

                                                 SMTxTMR            0                    1   2   3   4   5   6   7   8   9 10 11 12 13 14 15 16 1   2   3   4    5

                                                 SMTxCPW                                                                                  9                      5

                                                 SMTxCPR                                                                                                    16

                                               SMTxPWAIF

                                                SMTxPRAIF
DS40001919G-page 392
                                        FIGURE 25-22:      WINDOWED COUNTER MODE SINGLE ACQUISITION TIMING DIAGRAM
DS40001919G-page 393


                                                                                                                                                                                  PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                                                                                               Rev. 10-000193A
                                                                                                                                                                     12/18/2013


                                                          SMTxWIN

                                                        SMTx_signal

                                                           SMTxEN

                                                           SMTxGO

                                                         SMTxTMR        0                    1   2   3   4   5   6   7   8   9 10 11 12 13 14 15 16

                                                         SMTxCPW                                                                                      9

                                                          SMTxCPR                                                                                         16

                                                        SMTxPWAIF

                                                        SMTxPRAIF
 2017-2021 Microchip Technology Inc.
                      PIC18(L)F26/27/45/46/47/55/56/57K42
25.7     Interrupts
The SMT can trigger an interrupt under three different
conditions:
• PW Acquisition Complete
• PR Acquisition Complete
• Counter Period Match
The interrupts are controlled by the PIR and PIE
registers of the device.

25.7.1      PW AND PR ACQUISITION
            INTERRUPTS
The SMT can trigger interrupts whenever it updates the
SMT1CPW         and     SMT1CPR       registers,    the
circumstances for which are dependent on the SMT
mode, and are discussed in each mode’s specific
section. The SMT1CPW interrupt is controlled by
SMT1PWAIF and SMT1PWAIE bits in the respective
PIR and PIE registers. The SMT1CPR interrupt is
controlled by the SMT1PRAIF and SMT1PRAIE bits,
also located in the respective PIR and PIE registers.
In synchronous SMT modes, the interrupt trigger is
synchronized to the SMT1CLK. In Asynchronous
modes, the interrupt trigger is asynchronous. In either
mode, once triggered, the interrupt will be
synchronized to the CPU clock.

25.7.2      COUNTER PERIOD MATCH
            INTERRUPT
As described in Section 25.1.2 “Period Match
interrupt”, the SMT will also interrupt upon SMT1TMR,
matching SMT1PR with its period match limit functionality
described in Section 25.3 “Halt Operation”. The period
match interrupt is controlled by SMT1IF and SMT1IE,
located in the respective PIR and PIE registers.


 2017-2021 Microchip Technology Inc.                       DS40001919G-page 394
                        PIC18(L)F26/27/45/46/47/55/56/57K42
25.8      Register Definitions: SMT Control
Long bit name prefixes for the Signal Measurement
Timer peripherals are shown in Section 1.3 “Register
and Bit naming conventions”.
TABLE 25-2:         LONG BIT NAMES PREFIXES
                    FOR SMT PERIPHERALS
          Peripheral               Bit Name Prefix
            SMT1                         SMT1


REGISTER 25-1:           SMT1CON0: SMT CONTROL REGISTER 0
   R/W-0/0             U-0          R/W-0/0         R/W-0/0       R/W-0/0       R/W-0/0          R/W-0/0     R/W-0/0
    EN(1)               —            STP            WPOL          SPOL           CPOL                  PS[1:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              EN: SMT Enable bit(1)
                   1 = SMT is enabled
                   0 = SMT is disabled; internal states are reset, clock requests are disabled
bit 6              Unimplemented: Read as ‘0’
bit 5              STP: SMT Counter Halt Enable bit
                   When SMT1TMR = SMT1PR:
                   1 = Counter remains SMT1PR; period match interrupt occurs when clocked
                   0 = Counter resets to 24’h000000; period match interrupt occurs when clocked
bit 4              WPOL: SMT1WIN Input Polarity Control bit
                   1 = SMT1WIN signal is active-low/falling edge enabled
                   0 = SMT1WIN signal is active-high/rising edge enabled
bit 3              SPOL: SMT1SIG Input Polarity Control bit
                   1 = SMT1_signal is active-low/falling edge enabled
                   0 = SMT1_signal is active-high/rising edge enabled
bit 2              CPOL: SMT Clock Input Polarity Control bit
                   1 = SMT1TMR increments on the falling edge of the selected clock signal
                   0 = SMT1TMR increments on the rising edge of the selected clock signal
bit 1-0            PS[1:0]: SMT Prescale Select bits
                   11 = Prescaler = 1:8
                   10 = Prescaler = 1:4
                   01 = Prescaler = 1:2
                   00 = Prescaler = 1:1

Note 1:      Setting EN to ‘0’ does not affect the register contents.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 395
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-2:           SMT1CON1: SMT CONTROL REGISTER 1
 R/W/HC-0/0          R/W-0/0          U-0               U-0       R/W-0/0     R/W-0/0          R/W-0/0      R/W-0/0
        GO          REPEAT              —               —                           MODE[3:0]
bit 7                                                                                                             bit 0


Legend:
HC = Bit is cleared by hardware                               HS = Bit is set by hardware
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         q = Value depends on condition


bit 7              GO: GO Data Acquisition bit
                   1 = Incrementing, acquiring data is enabled
                   0 = Incrementing, acquiring data is disabled
bit 6              REPEAT: SMT Repeat Acquisition Enable bit
                   1 = Repeat Data Acquisition mode is enabled
                   0 = Single Acquisition mode is enabled
bit 5-4            Unimplemented: Read as ‘0’
bit 3-0            MODE[3:0] SMT Operation Mode Select bits
                   1111 = Reserved
                   •
                   •
                   •
                   1011 = Reserved
                   1010 = Windowed counter
                   1001 = Gated counter
                   1000 = Counter
                   0111 = Capture
                   0110 = Time of flight
                   0101 = Gated windowed measure
                   0100 = Windowed measure
                   0011 = High and low time measurement
                   0010 = Period and Duty-Cycle Acquisition
                   0001 = Gated Timer
                   0000 = Timer


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 396
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-3:           SMT1STAT: SMT STATUS REGISTER
 R/W/HC-0/0        R/W/HC-0/0     R/W/HC-0/0            U-0       U-0          R-0/0           R-0/0         R-0/0
   CPRUP             CPWUP           RST                —          —             TS            WS             AS
bit 7                                                                                                              bit 0


Legend:
HC = Bit is cleared by hardware                               HS = Bit is set by hardware
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         q = Value depends on condition


bit 7              CPRUP: SMT Manual Period Buffer Update bit
                   1 = Request update to SMT1CPRx registers
                   0 = SMT1CPRx registers update is complete
bit 6              CPWUP: SMT Manual Pulse Width Buffer Update bit
                   1 = Request update to SMT1CPW registers
                   0 = SMT1CPW registers update is complete
bit 5              RST: SMT Manual Timer Reset bit
                   1 = Request Reset to SMT1TMR registers
                   0 = SMT1TMR registers update is complete
bit 4-3            Unimplemented: Read as ‘0’
bit 2              TS: GO Value Status bit
                   1 = SMT timer is incrementing
                   0 = SMT timer is not incrementing
bit 1              WS: SMT1WIN Value Status bit
                   1 = SMT window is open
                   0 = SMT window is closed
bit 0              AS: SMT_signal Value Status bit
                   1 = SMT acquisition is in progress
                   0 = SMT acquisition is not in progress


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 397
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-4:          SMT1CLK: SMT CLOCK SELECTION REGISTER
        U-0            U-0           U-0               U-0       U-0         R/W-0/0       R/W-0/0         R/W-0/0
        —               —               —              —          —                       CSEL[2:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared         q = Value depends on condition


bit 7-3            Unimplemented: Read as ‘0’
bit 2-0            CSEL[2:0]: SMT Clock Selection bits
                   111 = Reference Clock Output
                   110 = SOSC
                   101 = MFINTOSC/16 (32 kHz)
                   100 = MFINTOSC (500 kHz)
                   011 = LFINTOSC
                   010 = HFINTOSC 16 MHz
                   001 = FOSC
                   000 = FOSC/4


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 398
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-5:           SMT1WIN: SMT1 WINDOW INPUT SELECT REGISTER
        U-0            U-0            U-0           R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
          —             —               —                                    WSEL[4:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         q = Value depends on condition


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            WSEL[4:0]: SMT1 Window Selection bits
                   11111 = Reserved
                   •
                   •
                   •
                   11011 = Reserved
                   11010 = CLC4_out
                   11001 = CLC3_out
                   11000 = CLC2_out
                   10111 = CLC1_out
                   10110 = ZCD1_out
                   10101 = CMP2_out
                   10100 = CMP1_out
                   10011 = NCO1_out
                   10010 = Reserved
                   10001 = Reserved
                   10000 = PWM8_out
                   01111 = PWM7_out
                   01110 = PWM6_out
                   01101 = PWM5_out
                   01100 = CCP4_out
                   01011 = CCP3_out
                   01010 = CCP2_out
                   01001 = CCP1_out
                   01000 = TMR6_postscaled
                   00111 = TMR4_postscaled
                   00110 = TMR2_postscaled
                   00100 = CLKREF
                   00011 = SOSC
                   00010 = MFINTOSC/16 (32 kHz)
                   00001 = LFINTOSC
                   00000 = SMTxWINPPS


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 399
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-6:          SMT1SIG: SMT1 SIGNAL INPUT SELECT REGISTER
        U-0            U-0           U-0           R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
        —               —               —                                   SSEL[4:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared         q = Value depends on condition


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            SSEL[4:0]: SMT1 Signal Selection bits
                   11111 = Reserved
                   •
                   •
                   •
                   11010 = Reserved
                   11001 = CLC4_out
                   11000 = CLC3_out
                   10111 = CLC2_out
                   10110 = CLC1_out
                   10101 = ZCD1_out
                   10100 = CMP2_out
                   10011 = CMP1_out
                   10010 = NCO1_out
                   10001 = Reserved
                   10000 = Reserved
                   01111 = PWM8_out
                   01110 = PWM7_out
                   01101 = PWM6_out
                   01100 = PWM5_out
                   01011 = CCP4_out
                   01010 = CCP3_out
                   01001 = CCP2_out
                   01000 = CCP1_out
                   00111 = TMR6_postscaled
                   00110 = TMR5_postscaled
                   00101 = TMR4_postscaled
                   00100 = TMR3_postscaled
                   00011 = TMR2_postscaled
                   00010 = TMR1_postscaled
                   00001 = TMR0_overflow
                   00000 = SMTxSIGPPS


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 400
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-7:          SMT1TMRL: SMT TIMER REGISTER – LOW BYTE
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0       R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                       SMT1TMR[7:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1TMR[7:0]: Significant bits of the SMT Counter – Low Byte


REGISTER 25-8:          SMT1TMRH: SMT TIMER REGISTER – HIGH BYTE
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0       R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                       SMT1TMR[15:8]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1TMR[15:8]: Significant bits of the SMT Counter – High Byte


REGISTER 25-9:          SMT1TMRU: SMT TIMER REGISTER – UPPER BYTE
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0       R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                       SMT1TMR[23:16]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1TMR[23:16]: Significant bits of the SMT Counter – Upper Byte


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 401
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-10: SMT1CPRL: SMT CAPTURED PERIOD REGISTER – LOW BYTE
        R-x/x         R-x/x         R-x/x              R-x/x      R-x/x         R-x/x          R-x/x          R-x/x
                                                        SMT1CPR[7:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1CPR[7:0]: Significant bits of the SMT Period Latch – Low Byte


REGISTER 25-11: SMT1CPRH: SMT CAPTURED PERIOD REGISTER – HIGH BYTE
        R-x/x         R-x/x         R-x/x              R-x/x      R-x/x         R-x/x          R-x/x          R-x/x
                                                        SMT1CPR[15:8]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1CPR[15:8]: Significant bits of the SMT Period Latch – High Byte


REGISTER 25-12: SMT1CPRU: SMT CAPTURED PERIOD REGISTER – UPPER BYTE
        R-x/x         R-x/x         R-x/x              R-x/x      R-x/x         R-x/x          R-x/x          R-x/x
                                                       SMT1CPR[23:16]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1CPR[23:16]: Significant bits of the SMT Period Latch – Upper Byte


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 402
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-13: SMT1CPWL: SMT CAPTURED PULSE WIDTH REGISTER – LOW BYTE
        R-x/x         R-x/x         R-x/x              R-x/x      R-x/x         R-x/x          R-x/x          R-x/x
                                                        SMT1CPW[7:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1CPW[7:0]: Significant bits of the SMT PW Latch – Low Byte


REGISTER 25-14: SMT1CPWH: SMT CAPTURED PULSE WIDTH REGISTER – HIGH BYTE
        R-x/x         R-x/x         R-x/x              R-x/x      R-x/x         R-x/x          R-x/x          R-x/x
                                                       SMT1CPW[15:8]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1CPW[15:8]: Significant bits of the SMT PW Latch – High Byte


REGISTER 25-15: SMT1CPWU: SMT CAPTURED PULSE WIDTH REGISTER – UPPER BYTE
        R-x/x         R-x/x         R-x/x              R-x/x      R-x/x         R-x/x          R-x/x          R-x/x
                                                       SMT1CPW[23:16]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            SMT1CPW[23:16]: Significant bits of the SMT PW Latch – Upper Byte


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 403
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 25-16: SMT1PRL: SMT PERIOD REGISTER – LOW BYTE
   R/W-x/1           R/W-x/1       R/W-x/1          R/W-x/1      R/W-x/1       R/W-x/1       R/W-x/1         R/W-x/1
                                                         SMT1PR[7:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            SMT1PR[7:0]: Significant bits of the SMT Timer Value for Period Match – Low Byte


REGISTER 25-17: SMT1PRH: SMT PERIOD REGISTER – HIGH BYTE
   R/W-x/1           R/W-x/1       R/W-x/1          R/W-x/1      R/W-x/1       R/W-x/1       R/W-x/1         R/W-x/1
                                                        SMT1PR[15:8]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            SMT1PR[15:8]: Significant bits of the SMT Timer Value for Period Match – High Byte


REGISTER 25-18: SMT1PRU: SMT PERIOD REGISTER – UPPER BYTE
   R/W-x/1           R/W-x/1       R/W-x/1          R/W-x/1      R/W-x/1       R/W-x/1       R/W-x/1         R/W-x/1
                                                        SMT1PR[23:16]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            SMT1PR[23:16]: Significant bits of the SMT Timer Value for Period Match – Upper Byte


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 404
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 25-3:       SUMMARY OF REGISTERS ASSOCIATED WITH SMT1
                                                                                                               Register
    Name          Bit 7       Bit 6      Bit 5       Bit 4          Bit 3      Bit 2       Bit 1       Bit 0
                                                                                                               on Page
SMT1CON0           EN          —         STP        WPOL        SPOL          CPOL         SMT1PS[1:0]           396
SMT1CON1           GO       REPEAT        —           —                          MODE[3:0]                       397
SMT1STAT        CPRUP       CPWUP        RST          —              —         TS          WS           AS       398
SMT1CLK            —           —          —           —              —                  CSEL[2:0]                399
SMT1SIG            —           —          —                                 SSEL[4:0]                            401
SMT1WIN            —           —          —                                 WSEL[4:0]                            400
SMT1TMRL                                                TMR[7:0]                                                 402
SMT1TMRH                                               TMR[15:8]                                                 402
SMT1TMRU                                               TMR[23:16]                                                402
SMT1CPRL                                                CPR[7:0]                                                 403
SMT1CPRH                                               CPR[15:8]                                                 403
SMT1CPRU                                               CPR[23:16]                                                403
SMT1CPWL                                                CPW[7:0]                                                 404
SMT1CPWH                                               CPW[15:8]                                                 404
SMT1CPWU                                               CPW[23:16]                                                404
SMT1PRL                                                   PR[7:0]                                                405
SMT1PRH                                                 PR[15:8]                                                 405
SMT1PRU                                                 PR[23:16]                                                405
Legend:     — = unimplemented read as ‘0’. Shaded cells are not used for SMT1 module.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 405
