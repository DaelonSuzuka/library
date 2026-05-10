                      PIC18(L)F26/27/45/46/47/55/56/57K42
8.0      REFERENCE CLOCK OUTPUT
         MODULE
The reference clock output module provides the ability
to send a clock signal to the clock reference output pin
(CLKR). The reference clock output can also be used
as a signal for other peripherals, such as the Data
Signal Modulator (DSM), Memory Scanner and Timer
module.
The reference clock output module has the following
features:
• Selectable clock source using the CLKRCLK
  register
• Programmable clock divider
• Selectable duty cycle

FIGURE 8-1:             CLOCK REFERENCE BLOCK DIAGRAM
                                                                                                                              Rev. 10-000261B
                                                                                                                                     5/11/2016


                                                                    CLKRDIV<2:0>
                                                 CLKREN    Counter Reset
                                                                                                  128
                                                                                                        111

                                                                        Reference Clock Divider
                       See                                                                        64          CLKRDC<1:0>
                                                                                                        110
                     CLKRCLK                                                                      32
                      Register                                                                          101
                                                                                                  16                                     CLKR
                                                                                                        100
                                                                                                  8            Duty Cycle     PPS
                                                                                                        011
                                                                                                  4
                                                                                                        010
                                                                                                  2
                                                                                                        001             To Peripherals

                                     CLKREN                                                             000
                    CLKRCLK<3:0>


FIGURE 8-2:             CLOCK REFERENCE TIMING

                                                                                                                                                      Rev. 10-000264B
                                                                                                                                                             5/25/2016

                                        P1       P2

                  CLKRCLK


                   CLKREN

            CLKR Output
            CLKRDIV<2:0> = 001
            CLKRDC<1:0> = 10
                                    Duty Cycle
                                      (50%)

            CLKR Output                 CLKRCLK/2
            CLKRDIV<2:0> = 001
            CLKRDC<1:0> = 01
                                   Duty Cycle
                                     (25%)


 2017-2021 Microchip Technology Inc.                                                                                                            DS40001919G-page 111
                      PIC18(L)F26/27/45/46/47/55/56/57K42
8.1      Clock Source                                     8.3       Selectable Duty Cycle
The input to the reference clock output can be selected   The DC[1:0] bits of the CLKRCON register can be used
using the CLKRCLK register.                               to modify the duty cycle of the output clock. A duty cycle
                                                          of 25%, 50%, or 75% can be selected for all clock rates,
8.1.1       CLOCK SYNCHRONIZATION                         with the exception of the undivided base FOSC value.
Once the reference clock enable (EN) is set, the          The duty cycle can be changed while the module is
module is ensured to be glitch-free at start-up.          enabled; however, in order to prevent glitches on the
When the reference clock output is disabled, the output   output, the DC[1:0] bits may only be changed when the
signal will be disabled immediately.                      module is disabled (EN = 0).

Clock dividers and clock duty cycles can be changed
while the module is enabled, but glitches may occur on      Note:     The DC1 bit is reset to ‘1’. This makes the
the output. To avoid possible glitches, clock dividers                default duty cycle 50% and not 0%.
and clock duty cycles may be changed only when the
CLKREN is clear.
                                                          8.4       Operation in Sleep Mode
8.2      Programmable Clock Divider                       The reference clock output module clock is based on
                                                          the system clock. When the device goes to Sleep, the
The module takes the clock input and divides it based     module outputs will remain in their current state. This
on the value of the DIV[2:0] bits of the CLKRCON          will have a direct effect on peripherals using the
register (Register 8-1).                                  reference clock output as an input signal. No change
The following configurations can be made based on the     may occur in the module from entering or exiting from
DIV[2:0] bits:                                            Sleep.
• Base FOSC value
• FOSC divided by 2
• FOSC divided by 4
• FOSC divided by 8
• FOSC divided by 16
• FOSC divided by 32
• FOSC divided by 64
• FOSC divided by 128
The clock divider values can be changed while the
module is enabled; however, in order to prevent
glitches on the output, the DIV[2:0] bits may only be
changed when the module is disabled (EN = 0).


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 112
                        PIC18(L)F26/27/45/46/47/55/56/57K42
8.5       Register Definitions: Reference Clock
Long bit name prefixes for the Reference Clock
peripherals are shown below. Refer to Section
1.3.2.2 “Long Bit Names” for more information.


          Peripheral               Bit Name Prefix
             CLKR                        CLKR


REGISTER 8-1:            CLKRCON: REFERENCE CLOCK CONTROL REGISTER
   R/W-0/0             U-0              U-0         R/W-1/1       R/W-0/0        R/W-0/0         R/W-0/0        R/W-0/0
        EN              —               —                   DC[1:0]                             DIV[2:0]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              EN: Reference Clock Module Enable bit
                   1 = Reference clock module enabled
                   0 = Reference clock module is disabled
bit 6-5            Unimplemented: Read as ‘0’
bit 4-3            DC[1:0]: Reference Clock Duty Cycle bits(1)
                   11 = Clock outputs duty cycle of 75%
                   10 = Clock outputs duty cycle of 50%
                   01 = Clock outputs duty cycle of 25%
                   00 = Clock outputs duty cycle of 0%
bit 2-0            DIV[2:0]: Reference Clock Divider bits
                   111 = Base clock value divided by 128
                   110 = Base clock value divided by 64
                   101 = Base clock value divided by 32
                   100 = Base clock value divided by 16
                   011 = Base clock value divided by 8
                   010 = Base clock value divided by 4
                   001 = Base clock value divided by 2
                   000 = Base clock value

Note 1:      Bits are valid for reference clock divider values of two or larger, the base clock cannot be further divided.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 113
                           PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 8-2:               CLKRCLK: CLOCK REFERENCE CLOCK SELECTION MUX
        U-0                U-0                U-0                U-0           R/W-0/0       R/W-0/0        R/W-0/0       R/W-0/0
        —                  —                   —                 —                                 CLK[3:0]
bit 7                                                                                                                          bit 0


Legend:
R = Readable bit                         W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                     x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                         ‘0’ = Bit is cleared


bit 7-4             Unimplemented: Read as ‘0’
bit 3-0             CLK[3:0]: CLKR Clock Selection bits
                    1111 = Reserved
                    
                    
                    
                    1011 = Reserved
                    1010 = CLC4 Output
                    1001 = CLC3 Output
                    1000 = CLC2 Output
                    0111 = CLC1 Output
                    0110 = NCO1 Output
                    0101 = SOSC
                    0100 = MFINTOSC (31.25 kHz)
                    0011 = MFINTOSC (500 kHz)
                    0010 = LFINTOSC (31 kHz)
                    0001 = HFINTOSC
                    0000 = FOSC

TABLE 8-1:            SUMMARY OF REGISTERS ASSOCIATED WITH CLOCK REFERENCE OUTPUT
                                                                                                                           Register
   Name            Bit 7         Bit 6         Bit 5        Bit 4      Bit 3         Bit 2        Bit 1           Bit 0
                                                                                                                           on Page
CLKRCON            EN             —             —                DC[1:0]                         DIV[2:0]                    113
CLKRCLK             —             —             —            —             —                     CLK[2:0]                    114
Legend:       — = unimplemented, read as ‘0’. Shaded cells are not used by the CLKR module.


 2017-2021 Microchip Technology Inc.                                                                           DS40001919G-page 114
