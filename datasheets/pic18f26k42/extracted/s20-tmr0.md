                          PIC18(L)F26/27/45/46/47/55/56/57K42
20.0     TIMER0 MODULE
Timer0 module is an 8/16-bit timer/counter with the
following features:
• 16-bit timer/counter
• 8-bit timer/counter with programmable period
• Synchronous or asynchronous operation
• Selectable clock sources
• Programmable prescaler
• Programmable postscaler
• Operation during Sleep mode
• Interrupt on match or overflow
• Output on I/O pin (via PPS) or to other peripherals

FIGURE 20-1:              BLOCK DIAGRAM OF TIMER0
                                                                                                                                  Rev. 10-000017F
                                                                                                                                        11/11/2016


               CLC1           111
           SOSC               110                                                        T0_match
                                                                                                        Peripherals
       MFINTOSC               101       CKPS<3:0>
       LFINTOSC               100                                               TMR0     OUTPS<3:0>                              T0IF
                                        Prescaler                    1
       HFINTOSC               011                                          IN      OUT    Postscaler                             T0_out
                                                          SYNC       0
           FOSC/4             010
               PPS            001                         FOSC/4                MD16                                                            TMR0
                                                                   ASYNC                                   D        Q           PPS
                              000
         T0CKIPPS                                                                                              CK Q         RxyPPS

                                   3

                            CS<2:0>


                      8-bit TMR0 (MD16 = 0)                                                   16-bit TMR0 (MD16 = 1)


                                        Clear                                      IN                      TMR0 High              OUT
          IN             TMR0L      R                                                      TMR0L
                                                                                                             Byte

                                                                                                                            8
                                                                                                                                 Read TMR0L
                      COMPARATOR                    OUT
                                                                                                                                 Write TMR0L
                                           T0_match                                                             8
                                                                                                    8          TMR0H
                       TMR0 High
                         Byte
                                          Latch                                                                         8
                                          Enable
                         TMR0H
                                                                                                                8
                                                                                            Internal Data Bus


 2017-2021 Microchip Technology Inc.                                                                                   DS40001919G-page 299
                       PIC18(L)F26/27/45/46/47/55/56/57K42
20.1       Timer0 Operation                                  Both the prescaler and postscaler counters are cleared
                                                             on the following events:
Timer0 can operate as either an 8-bit timer/counter or
                                                             • A write to the TMR0L register
a 16-bit timer/counter. The mode is selected with the
                                                             • A write to either the T0CON0 or T0CON1
MD16 bit of the T0CON register.
                                                               registers
20.1.1      16-BIT MODE                                      • Any device Reset – Power-on Reset (POR),
                                                               MCLR Reset, Watchdog Timer Reset (WDTR) or
The register pair TMR0H:TMR0L increments on the              • Brown-out Reset (BOR)
rising edge of the clock source. A 15-bit prescaler on
the clock input gives several prescale options (see          20.1.3      COUNTER MODE
prescaler control bits, CKPS[3:0] in the T0CON1
                                                             In Counter mode, the prescaler is normally disabled by
register).
                                                             setting the CKPS bits of the T0CON1 register to ‘0000’.
20.1.1.1      Timer0 Reads and Writes in 16-Bit              Each rising edge of the clock input (or the output of the
                                                             prescaler if the prescaler is used) increments the
              Mode
                                                             counter by ‘1’.
In 16-bit mode, in order to avoid rollover between
reading high and low registers, the TMR0H register is        20.1.4      TIMER MODE
a buffered copy of the actual high byte of Timer0, which
                                                             In Timer mode, the Timer0 module will increment every
is neither directly readable, nor writable (see Figure 20-
                                                             instruction cycle as long as there is a valid clock signal
1). TMR0H is updated with the contents of the high byte
                                                             and the CKPS bits of the T0CON1 register
of Timer0 during a read of TMR0L. This provides the
                                                             (Register 20-2) are set to ‘0000’. When a prescaler is
ability to read all 16 bits of Timer0 without having to
                                                             added, the timer will increment at the rate based on the
verify that the read of the high and low byte was valid,
                                                             prescaler value.
due to a rollover between successive reads of the high
and low byte.                                                20.1.5      ASYNCHRONOUS MODE
Similarly, a write to the high byte of Timer0 must also      When the ASYNC bit of the T0CON1 register is set
take place through the TMR0H Buffer register. The high       (ASYNC = ‘1’), the counter increments with each rising
byte is updated with the contents of TMR0H when a            edge of the input source (or output of the prescaler, if
write occurs to TMR0L. This allows all 16 bits of Timer0     used). Asynchronous mode allows the counter to
to be updated at once.                                       continue operation during Sleep mode provided that
                                                             the clock also continues to operate during Sleep.
20.1.2      8-BIT MODE
In 8-bit mode, the value of TMR0L is compared to that        20.1.6      SYNCHRONOUS MODE
of the Period buffer, a copy of TMR0H, on each clock         When the ASYNC bit of the T0CON1 register is clear
cycle. When the two values match, the following events       (ASYNC = ‘0’), the counter clock is synchronized to the
happen:                                                      system clock (FOSC/4). When operating in
• TMR0_out goes high for one prescaled clock                 Synchronous mode, the counter clock frequency
  period                                                     cannot exceed FOSC/4.
• TMR0L is reset
• The contents of TMR0H are copied to the period             20.2     Clock Source Selection
  buffer
                                                             The CS[2:0] bits of the T0CON1 register are used to
In 8-bit mode, the TMR0L and TMR0H registers are
                                                             select the clock source for Timer0. Register 20-2
both directly readable and writable. The TMR0L
                                                             displays the clock source selections.
register is cleared on any device Reset, while the
TMR0H register initializes at FFh.
                                                             20.2.1      INTERNAL CLOCK SOURCE
                                                             When the internal clock source is selected, Timer0
                                                             operates as a timer and will increment on multiples of
                                                             the clock source, as determined by the Timer0
                                                             prescaler.

                                                             20.2.2      EXTERNAL CLOCK SOURCE
                                                             When an external clock source is selected, Timer0 can
                                                             operate as either a timer or a counter. Timer0 will
                                                             increment on multiples of the rising edge of the external
                                                             clock source, as determined by the Timer0 prescaler.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 300
                       PIC18(L)F26/27/45/46/47/55/56/57K42
20.3     Programmable Prescaler                               20.7     Timer0 Output
A software programmable prescaler is available for            The Timer0 output can be routed to any I/O pin via the
exclusive use with Timer0. There are 16 prescaler             RxyPPS output selection register (see Section
options for Timer0 ranging in powers of two from 1:1 to       17.0 “Peripheral Pin Select (PPS) Module” for
1:32768. The prescaler values are selected using the          additional information). The Timer0 output can also be
CKPS[3:0] bits of the T0CON1 register.                        used by other peripherals, such as the auto-conversion
The prescaler is not directly readable or writable.           trigger of the Analog-to-Digital Converter. Finally, the
Clearing the prescaler register can be done by writing        Timer0 output can be monitored through software via
to the TMR0L register or to the T0CON0/T0CON1                 the Timer0 output bit (OUT) of the T0CON0 register
register or by any Reset.                                     (Register 20-1).
                                                              TMR0_out will be a pulse of one postscaled clock
20.4     Programmable Postscaler                              period when a match occurs between TMR0L and PR0
                                                              (Period register for TMR0) in 8-bit mode, or when
A software programmable postscaler (output divider) is        TMR0 rolls over in 16-bit mode. The Timer0 output is a
available for exclusive use with Timer0. There are 16         50% duty cycle that toggles on each TMR0_out rising
postscaler options for Timer0 ranging from 1:1 to 1:16.       clock edge.
The postscaler values are selected using the OUTPS
bits of the T0CON0 register.
The postscaler is not directly readable or writable.
Clearing the postscaler register can be done by writing
to the TMR0L register or to the T0CON0/T0CON1
register or by any Reset.

20.5     Operation During Sleep
When operating synchronously, Timer0 will halt. When
operating asynchronously, Timer0 will continue to
increment and wake the device from Sleep (if Timer0
interrupts are enabled) provided that the input clock
source is active.

20.6     Timer0 Interrupts
The Timer0 interrupt flag bit (TMR0IF) is set when
either of the following conditions occur:
• 8-bit TMR0L matches the TMR0H value
• 16-bit TMR0 rolls over from ‘FFFFh’
When the postscaler bits (OUTPS) are set to 1:1
operation (no division), the T0IF flag bit will be set with
every TMR0 match or rollover. In general, the TMR0IF
flag bit will be set every OUTPS +1 matches or
rollovers.
If Timer0 interrupts are enabled (TMR0IE bit of the
PIE3 register = ‘1’), the CPU will be interrupted and the
device may wake from Sleep (see Section
20.2 “Clock Source Selection” for more details).


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 301
                       PIC18(L)F26/27/45/46/47/55/56/57K42
20.8      Register Definitions: Timer0 Control

REGISTER 20-1:          T0CON0: TIMER0 CONTROL REGISTER 0
   R/W-0/0             U-0              R-0        R/W-0/0      R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
        EN              —           OUT                MD16                         OUTPS[3:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7              EN: TMR0 Enable bit
                   1 = The module is enabled and operating
                   0 = The module is disabled and in the lowest power mode
bit 6              Unimplemented: Read as ‘0’
bit 5              OUT: TMR0 Output bit (read-only)
                   TMR0 output bit
bit 4              MD16: TMR0 Operating as 16-Bit Timer Select bit
                   1 = TMR0 is a 16-bit timer
                   0 = TMR0 is an 8-bit timer
bit 3-0            OUTPS[3:0]: TMR0 Output Postscaler (Divider) Select bits
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


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 302
                        PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 20-2:          T0CON1: TIMER0 CONTROL REGISTER 1
   R/W-0/0           R/W-0/0       R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                     CS[2:0]                        ASYNC                           CKPS[3:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-5            CS[2:0]:Timer0 Clock Source Select bits
                   111 = CLC1
                   110 = SOSC
                   101 = MFINTOSC (500 kHz)
                   100 = LFINTOSC
                   011 = HFINTOSC
                   010 = FOSC/4
                   001 = Pin selected by T0CKIPPS (Inverted)
                   000 = Pin selected by T0CKIPPS (Noninverted)
bit 4              ASYNC: TMR0 Input Asynchronization Enable bit
                   1 = The input to the TMR0 counter is not synchronized to system clocks
                   0 = The input to the TMR0 counter is synchronized to FOSC/4
bit 3-0            CKPS[3:0]: Prescaler Rate Select bit
                   1111 = 1:32768
                   1110 = 1:16384
                   1101 = 1:8192
                   1100 = 1:4096
                   1011 = 1:2048
                   1010 = 1:1024
                   1001 = 1:512
                   1000 = 1:256
                   0111 = 1:128
                   0110 = 1:64
                   0101 = 1:32
                   0100 = 1:16
                   0011 = 1:8
                   0010 = 1:4
                   0001 = 1:2
                   0000 = 1:1


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 303
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 20-3:            TMR0L: TIMER0 COUNT REGISTER
   R/W-0/0           R/W-0/0          R/W-0/0        R/W-0/0        R/W-0/0         R/W-0/0           R/W-0/0      R/W-0/0
                                                          TMR0L[7:0]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            TMR0L[7:0]: TMR0 Counter bits [7:0]

REGISTER 20-4:            TMR0H: TIMER0 PERIOD REGISTER
   R/W-1/1           R/W-1/1          R/W-1/1        R/W-1/1        R/W-1/1         R/W-1/1           R/W-1/1      R/W-1/1
                                                         TMR0H[15:8]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            When MD16 = 0
                   PR0[7:0]:TMR0 Period Register Bits [7:0]
                   When MD16 = 1
                   TMR0H[15:8]: TMR0 Counter bits [15:8]


TABLE 20-1:         SUMMARY OF REGISTERS ASSOCIATED WITH TIMER0
                                                                                                                    Register
     Name            Bit 7       Bit 6       Bit 5        Bit 4       Bit 3       Bit 2       Bit 1        Bit 0
                                                                                                                    on Page
T0CON0               EN           —          OUT         MD16                        OUTPS[3:0]                       303
T0CON1                          CS[2:0]                  ASYNC                        CKPS[3:0]                       304
TMR0L                                                        TMR0L[7:0]                                               305
TMR0H                                                       TMR0H[15:8]                                               305
Legend:      — = unimplemented location, read as ‘0’. Shaded cells are not used by Timer0.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 304
