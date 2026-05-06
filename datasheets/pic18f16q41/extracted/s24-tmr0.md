24.   TMR0 - Timer0 Module
      The Timer0 module has the following features:
      •   8-bit timer with programmable period
      •   16-bit timer
      •   Selectable clock sources
      •   Synchronous and asynchronous operation
      •   Programmable prescaler (Independent of Watchdog Timer)
      •   Programmable postscaler
      •   Interrupt on match or overflow
      •   Output on I/O pin (via PPS) or to other peripherals
      •   Operation during Sleep

      Figure 24-1. Timer0 Block Diagram

                                                                                                                                         Rev. Tim er0 Blo
                                                                                                                                               2/12/201 9


               See T0CON1                    T0CKPS                               TMR0                                                  Peripherals
                   Register                                                        bod y         T0OUTPS                                T0IF
                                            Prescaler                   1
                                                                             IN       OUT       Postscaler                              T0_out
                                                              SYNC      0

                   PPS                                        FOSC/4       T016BIT                                                                          TMR0
                                                                    T0ASYNC                                    D          Q            PPS

              T0CKIPPS                                                                                             CK Q            RxyPPS


                                T0CS


              8-bit TMR0 Body Diagram (T016BIT = 0)                                         16-bit TMR0 Body Diagram (T016BIT = 1)


                                            Clear                                      IN                     Timer 0 High                OUT
              IN           TMR0L        R                                                        TMR0L           Byte

                                                                                                                                   8

                                                                                                                                        Read TMR0L
                         COMPARATOR                     OUT
                                                                                                                                        Write TMR0L
                                               T0_match                                                               8
                                                                                                        8
                                                                                                                   TMR0H
                         Timer 0 High
                            Byte
                                               Latch                                                                          8
                                              Enable
                           TMR0H
                                                                                                                      8
                                                                                                  Internal Data Bus


--- p357 ---
24.1   Timer0 Operation
       Timer0 can operate as either an 8-bit or 16-bit timer. The mode is selected with the MD16 bit.

24.1.1 8-Bit Mode
       In this mode, Timer0 increments on the rising edge of the selected clock source. A prescaler on the
       clock input gives several prescale options (see the prescaler control bits, CKPS). In this mode, as
       shown in Figure 24-1, a buffered version of TMR0H is maintained.
       This is compared with the value of TMR0L on each cycle of the selected clock source. When the two
       values match, the following events occur:
       • TMR0L is reset
       •   The contents of TMR0H are copied to the TMR0H buffer for next comparison

24.1.2 16-Bit Mode
       In this mode, Timer0 increments on the rising edge of the selected clock source. A prescaler on
       the clock input gives several prescale options (see the prescaler control bits, CKPS). In this mode,
       TMR0H:TMR0L form the 16-bit timer value. As shown in Figure 24-1, reads and writes of the TMR0H
       register are buffered. The TMR0H register is updated with the contents of the high byte of Timer0
       when the TMR0L register is read. Similarly, writing the TMR0L register causes a transfer of the
       TMR0H register value to the Timer0 high byte.
       This buffering allows all 16 bits of Timer0 to be read and written at the same time. Timer0 rolls
       over to 0x0000 on incrementing past 0xFFFF. This makes the timer free-running. While actively
       operating in 16-bit mode, the Timer0 value can be read but not written.

24.2   Clock Selection
       Timer0 has several options for clock source selections, the option to operate synchronously/
       asynchronously and an available programmable prescaler. The CS bits are used to select the clock
       source for Timer0.

24.2.1 Synchronous Mode
       When the ASYNC bit is clear, Timer0 clock is synchronized to the system clock (FOSC/4). When
       operating in Synchronous mode, Timer0 clock frequency cannot exceed FOSC/4. During Sleep mode,
       the system clock is not available and Timer0 cannot operate.

24.2.2 Asynchronous Mode
       When the ASYNC bit is set, Timer0 increments with each rising edge of the input source (or output of
       the prescaler, if used). Asynchronous mode allows Timer0 to continue operation during Sleep mode
       provided the selected clock source operates during Sleep.

24.2.3 Programmable Prescaler
       Timer0 has 16 programmable input prescaler options ranging from 1:1 to 1:32768. The prescaler
       values are selected using the CKPS bits. The prescaler counter is not directly readable or writable.
       The prescaler counter is cleared on the following events:
       •   A write to the TMR0L register
       •   A write to either the T0CON0 or T0CON1 registers
       •   Any device Reset

24.2.4 Programmable Postscaler
       Timer0 has 16 programmable output postscaler options ranging from 1:1 to 1:16. The postscaler
       values are selected using the OUTPS bits. The postscaler divides the output of Timer0 by the
       selected ratio. The postscaler counter is not directly readable or writable. The postscaler counter
       is cleared on the following events:


--- p358 ---
       •   A write to the TMR0L register
       •   A write to either the T0CON0 or T0CON1 registers
       •   Any device Reset

24.3   Timer0 Output and Interrupt
24.3.1 Timer0 Output
       TMR0_out toggles on every match between TMR0L and TMR0H in 8-bit mode or when
       TMR0H:TMR0L rolls over in 16-bit mode. If the output postscaler is used, the output is scaled by
       the ratio selected. The Timer0 output can be routed to an I/O pin via the RxyPPS output selection
       register or internally to a number of Core Independent Peripherals. The Timer0 output can be
       monitored through software via the OUT output bit.

24.3.2 Timer0 Interrupt
       The Timer0 Interrupt Flag (TMR0IF) bit is set when the TMR0_out toggles. If the Timer0 interrupt is
       enabled (TMR0IE), the CPU will be interrupted when the TMR0IF bit is set. When the postscaler bits
       (T0OUTPS) are set to 1:1 operation (no division), the T0IF flag bit will be set with every TMR0 match
       or rollover. In general, the TMR0IF flag bit will be set every T0OUTPS +1 matches or rollovers.

24.3.3 Timer0 Example

               Timer0 Configuration:
               • Timer0 mode = 16-bit
               •   Clock Source = FOSC/4 (250 kHz)
               •   Synchronous operation
               •   Prescaler = 1:1
               •   Postscaler = 1:2 (T0OUTPS = 1)
               In this case, the TMR0_out toggles every two rollovers of TMR0H:TMR0L.
               i.e., (0xFFFF)*2*(1/250 kHz) = 524.28 ms


24.4   Operation During Sleep
       When operating synchronously, Timer0 will halt when the device enters Sleep mode. When
       operating asynchronously and the selected clock source is active, Timer0 will continue to increment
       and wake the device from Sleep mode if the Timer0 interrupt is enabled.

24.5   Register Definitions: Timer0 Control


--- p359 ---
24.5.1 T0CON0

            Name:       T0CON0
            Address:    0x31A

            Timer0 Control Register 0

      Bit        7             6                 5           4                  3               2        1          0
                EN                              OUT         MD16                              OUTPS[3:0]
  Access        R/W                              R          R/W                R/W         R/W         R/W         R/W
   Reset         0                               0           0                  0           0            0          0

Bit 7 – EN TMR0 Enable
            Value      Description
            1          The module is enabled and operating
            0          The module is disabled

Bit 5 – OUT TMR0 Output

Bit 4 – MD16 16-Bit Timer Operation Select
            Value      Description
            1          TMR0 is a 16-bit timer
            0          TMR0 is an 8-bit timer

Bits 3:0 – OUTPS[3:0] TMR0 Output Postscaler (Divider) Select
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


--- p360 ---
24.5.2 T0CON1

            Name:        T0CON1
            Address:     0x31B

            Timer0 Control Register 1

      Bit           7          6                5             4                 3              2                 1              0
                             CS[2:0]                        ASYNC                                  CKPS[3:0]
  Access        R/W           R/W              R/W           R/W               R/W           R/W               R/W             R/W
   Reset         0             0                0             0                 0             0                 0               0

Bits 7:5 – CS[2:0] Timer0 Clock Source Select
                                       Value                                                       Description
                                       111                                                          CLC1_OUT
                                       110                                                            SOSC
                                       101                                                     MFINTOSC (500 kHz)
                                       100                                                          LFINTOSC
                                       011                                                          HFINTOSC
                                       010                                                            FOSC/4
                                       001                                             Pin selected by T0CKIPPS (Inverted)
                                       000                                           Pin selected by T0CKIPPS (Noninverted)

Bit 4 – ASYNC TMR0 Input Asynchronization Enable
            Value       Description
            1           The input to the TMR0 counter is not synchronized to system clocks
            0           The input to the TMR0 counter is synchronized to Fosc/4

Bits 3:0 – CKPS[3:0] Prescaler Rate Select
            Value       Description
            1111        1:32768
            1110        1:16384
            1101        1:8192
            1100        1:4096
            1011        1:2048
            1010        1:1024
            1001        1:512
            1000        1:256
            0111        1:128
            0110        1:64
            0101        1:32
            0100        1:16
            0011        1:8
            0010        1:4
            0001        1:2
            0000        1:1


--- p361 ---
24.5.3 TMR0H

           Name:       TMR0H
           Address:    0x319

           Timer0 Period/Count High Register

     Bit        7             6                5              4            3                  2         1                0
                                                                TMR0H[7:0]
  Access       R/W           R/W             R/W             R/W         R/W             R/W           R/W              R/W
   Reset        1             1               1               1            1              1             1                1

Bits 7:0 – TMR0H[7:0] TMR0 Most Significant Counter
           Value      Condition Description
           0 to 255   MD16 = 0 8-bit Timer0 Period Value. TMR0L continues counting from 0 when this value is reached.
           0 to 255   MD16 = 1     16-bit Timer0 Most Significant Byte


--- p362 ---
24.5.4 TMR0L

            Name:       TMR0L
            Address:    0x318

            Timer0 Period/Count Low Register

      Bit        7             6        5                 4           3                 2    1              0
                                                           TMR0L[7:0]
  Access        R/W          R/W       R/W              R/W         R/W            R/W      R/W            R/W
   Reset         0            0         0                0            0             0        0              0

Bits 7:0 – TMR0L[7:0] TMR0 Least Significant Counter
            Value      Condition         Description
            0 to 255   MD16 = 0          8-bit Timer0 Counter bits
            0 to 255   MD16 = 1             16-bit Timer0 Least Significant Byte


--- p363 ---
24.6      Register Summary - Timer0
Address     Name      Bit Pos.   7          6          5             4            3   2                1          0
  0x00
   ...     Reserved
 0x0317
 0x0318      TMR0L      7:0                                          TMR0L[7:0]
 0x0319     TMR0H       7:0                                          TMR0H[7:0]
 0x031A     T0CON0      7:0      EN                   OUT        MD16                     OUTPS[3:0]
 0x031B     T0CON1      7:0              CS[2:0]                 ASYNC                     CKPS[3:0]


--- p364 ---
