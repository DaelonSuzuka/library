                      PIC18(L)F26/27/45/46/47/55/56/57K42
28.0     NUMERICALLY CONTROLLED
         OSCILLATOR (NCO) MODULE
The Numerically Controlled Oscillator (NCO) module is
a timer that uses overflow from the addition of an
increment value to divide the input frequency. The
advantage of the addition method over simple counter
driven timer is that the output frequency resolution
does not vary with the divider value. The NCO is most
useful for applications that require frequency accuracy
and fine resolution at a fixed duty cycle.
Features of the NCO include:
• 20-bit Increment Function
• Fixed Duty Cycle mode (FDC) mode
• Pulse Frequency (PF) mode
• Output Pulse-Width Control
• Multiple Clock Input Sources
• Output Polarity Control
• Interrupt Capability
Figure 28-1 is a simplified block diagram of the NCO
module.


 2017-2021 Microchip Technology Inc.                     DS40001919G-page 449
                                        FIGURE 28-1:              DIRECT DIGITAL SYNTHESIS MODULE SIMPLIFIED BLOCK DIAGRAM
DS40001919G-page 450


                                                                                                                                                                                                                                                             PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                       NCOxINCU NCOxINCH NCOxINCL                                                                                                                         Rev. 10-000028E
                                                                                                                                                                                                                                                10/12/2016
                                                                                                     20
                                                                                 (1)
                                                                                        INCBUFU     INCBUFH     INCBUFL
                                                                                                        20
                                                                                                                       20
                                                         1111

                                                                                        NCO_overflow        Adder
                                         NCOx Clock                                                             20
                                          Sources
                                                                     NCOx_clk
                                                                                           NCOxACCU NCOxACCH NCOxACCL
                                           See                                                          20
                                         NCOxCLK
                                          Register
                                                                                                                      NCO_interrupt                                                                                                set bit
                                                                                                                                                                                                                                  NCOxIF
                                                         0000                                  Fixed Duty
                                                                                               Cycle Mode
                                                                                                Circuitry
                                             CKS<3:0>                                           D      Q                    D      Q                      0                                                         TRIS bit
                                                          4

                                                                                                                                   _                                                                                              NCOxOUT
                                                                                                                                                          1
                                                                                                                                   Q

                                                                                                                                                         PFM         POL

                                                                                                                                                                                                                 NCOx_out
                                                                                                                                                                                                                                  To Peripherals

                                                                                                                             S     Q
 2017-2021 Microchip Technology Inc.


                                                                                              EN

                                                                                                                                   _                                                                  D      Q                   OUT
                                                                                             Ripple
                                                                                                                            R      Q
                                                                                            Counter

                                                                                                                           Pulse                                                               Q1
                                                                                               R                         Frequency
                                                                                                          3             Mode Circuitry
                                                                                                       PWS<2:0>


                                            Note 1:     The increment registers are double-buffered to allow for value changes to be made without first disabling the NCO module. The full increment value is loaded into the buffer registers on the
                                                        second rising edge of the NCOx_clk signal that occurs immediately after a write to NCOxINCL register. The buffers are not user-accessible and are shown here for reference.
                       PIC18(L)F26/27/45/46/47/55/56/57K42
28.1     NCO Operation
The NCO operates by repeatedly adding a fixed value to
an accumulator. Additions occur at the input clock rate.
The accumulator will overflow with a carry periodically,
which is the raw NCO output (NCO_overflow). This
effectively reduces the input clock by the ratio of the
addition value to the maximum accumulator value. See
Equation 28-1.
The NCO output can be further modified by stretching
the pulse or toggling a flip-flop. The modified NCO
output is then distributed internally to other peripherals
and can be optionally output to a pin. The accumulator
overflow also generates an interrupt (NCO_overflow).
The NCO period changes in discrete steps to create an
average frequency. This output depends on the ability
of the receiving circuit (i.e., CWG or external resonant
converter circuitry) to average the NCO output to
reduce uncertainty.

EQUATION 28-1:          NCO OVERFLOW FREQUENCY

                                    N C O C lock Frequency  Increm ent Value
                     F O VERFLO W = --------------------------------------------------------20
                                                                                            -------------------------------------------------------
                                                                                        2

28.1.1      NCO CLOCK SOURCES                                                              28.1.4             INCREMENT REGISTERS
Clock sources available to the NCO include:                                                The increment value is stored in three registers making
• FOSC                                                                                     up a 20-bit incrementer. In order of LSB to MSB they
• HFINTOSC                                                                                 are:
• LFINTOSC                                                                                 • NCO1INCL
• MFINTOSC/4 (32 kHz)                                                                      • NCO1INCH
• MFINTOSC (500 kHz)                                                                       • NCO1INCU
• CLC1/2/3/4_out
• CLKREF                                                                                   When the NCO module is enabled, the NCO1INCU and
• SOSC                                                                                     NCO1INCH registers may be written first, then the
                                                                                           NCO1INCL register. Writing to the NCO1INCL register
The NCO clock source is selected by configuring the                                        initiates the increment buffer registers to be loaded
N1CKS[2:0] bits in the NCO1CLK register.                                                   simultaneously on the second rising edge of the
                                                                                           NCO_clk signal.
28.1.2      ACCUMULATOR
                                                                                           The registers are readable and writable. The increment
The accumulator is a 20-bit register. Read and write
                                                                                           registers are double-buffered to allow value changes to
access to the accumulator is available through three
                                                                                           be made without first disabling the NCO module.
registers:
                                                                                           When the NCO module is disabled, the increment
• NCO1ACCL
                                                                                           buffers are loaded immediately after a write to the
• NCO1ACCH                                                                                 increment registers.
• NCO1ACCU

28.1.3       ADDER                                                                             Note: The increment buffer registers are not user-
The NCO Adder is a full adder, which operates                                                        accessible.
independently from the source clock. The addition of
the previous result and the increment value replaces
the accumulator value on the rising edge of each input
clock.


 2017-2021 Microchip Technology Inc.                                                                                                          DS40001919G-page 451
                      PIC18(L)F26/27/45/46/47/55/56/57K42
28.2     FIXED DUTY CYCLE MODE                             28.5     Interrupts
In Fixed Duty Cycle (FDC) mode, every time the             When the accumulator overflows (NCO_overflow), the
accumulator overflows (NCO_overflow), the output is        NCO Interrupt Flag bit, NCO1IF, of the PIR4 register is
toggled. This provides a 50% duty cycle, provided that     set. To enable the interrupt event (NCO_interrupt), the
the increment value remains constant. For more             following bits must be set:
information, see Figure 28-2.                              • EN bit of the NCO1CON register
                                                           • NCO1IE bit of the PIE4 register
28.3     PULSE FREQUENCY MODE                              • GIE/GIEH bit of the INTCON0 register
In Pulse Frequency (PF) mode, every time the               The interrupt must be cleared by software by clearing
Accumulator overflows, the output becomes active for       the NCO1IF bit in the Interrupt Service Routine.
one or more clock periods. Once the clock period
expires, the output returns to an inactive state. This     28.6     Effects of a Reset
provides a pulsed output. The output becomes active
on the rising clock edge immediately following the         All of the NCO registers are cleared to zero as the
overflow event. For more information, see Figure 28-2.     result of a Reset.

The value of the active and inactive states depends on
the polarity bit, POL in the NCO1CON register.
                                                           28.7     Operation in Sleep
The PF mode is selected by setting the PFM bit in the      The NCO module operates independently from the
NCO1CON register.                                          system clock and will continue to run during Sleep,
                                                           provided that the clock source selected remains active.
28.3.1      OUTPUT PULSE-WIDTH CONTROL                     The HFINTOSC remains active during Sleep when the
When operating in PF mode, the active state of the         NCO module is enabled and the HFINTOSC is
output can vary in width by multiple clock periods.        selected as the clock source, regardless of the system
Various pulse widths are selected with the PWS[2:0]        clock source selected.
bits in the NCO1CLK register.                              In other words, if the HFINTOSC is simultaneously
When the selected pulse width is greater than the          selected as the system clock and the NCO clock
Accumulator overflow time frame, then DDS operation        source, when the NCO is enabled, the CPU will go Idle
is undefined.                                              during Sleep, but the NCO will continue to operate and
                                                           the HFINTOSC will remain active.
28.4     OUTPUT POLARITY CONTROL                           This will have a direct effect on the Sleep mode current.
The last stage in the NCO module is the output polarity.
The POL bit in the NCO1CON register selects the
output polarity. Changing the polarity while the
interrupts are enabled will cause an interrupt for the
resulting output transition. The NCO output signal is
available to most of the other peripherals available on
the device.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 452
                          PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 28-2:               FDC OUTPUT MODE OPERATION DIAGRAM
                                                                                                  Rev. 10-000029A
                                                                                                         11/7/2013


      NCOx
      Clock
      Source


       NCOx
     Increment               4000h                    4000h                        4000h
       Value


       NCOx
    Accumulator     00000h 04000h 08000h   FC000h 00000h 04000h 08000h   FC000h 00000h 04000h 08000h
       Value


    NCO_overflow


    NCO_interrupt


    NCOx Output
     FDC Mode


    NCOx Output
     PF Mode
    NCOxPWS =
      000

    NCOx Output
     PF Mode
    NCOxPWS =
      001


 2017-2021 Microchip Technology Inc.                                                DS40001919G-page 453
                        PIC18(L)F26/27/45/46/47/55/56/57K42
28.8      NCO Control Registers

REGISTER 28-1:           NCO1CON: NCO CONTROL REGISTER
   R/W-0/0             U-0           R-0/0          R/W-0/0       U-0           U-0            U-0          R/W-0/0
        EN              —            OUT                POL        —             —             —              PFM
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              EN: NCO1 Enable bit
                   1 = NCO1 module is enabled
                   0 = NCO1 module is disabled
bit 6              Unimplemented: Read as ‘0’
bit 5              OUT: NCO1 Output bit
                   Displays the current output value of the NCO1 module.
bit 4              POL: NCO1 Polarity
                   1 = NCO1 output signal is inverted
                   0 = NCO1 output signal is not inverted
bit 3-1            Unimplemented: Read as ‘0’
bit 0              PFM: NCO1 Pulse Frequency Mode bit
                   1 = NCO1 operates in Pulse Frequency mode
                   0 = NCO1 operates in Fixed Duty Cycle mode, divide by 2


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 454
                         PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 28-2:            NCO1CLK: NCO1 INPUT CLOCK CONTROL REGISTER
   R/W-0/0           R/W-0/0         R/W-0/0              U-0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                   PWS[2:0](1,2)                          —                            CKS[3:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                   W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared


bit 7-5            PWS[2:0]: NCO1 Output Pulse Width Select bits(1,2)
                   111 = NCO1 output is active for 128 input clock periods
                   110 = NCO1 output is active for 64 input clock periods
                   101 = NCO1 output is active for 32 input clock periods
                   100 = NCO1 output is active for 16 input clock periods
                   011 = NCO1 output is active for 8 input clock periods
                   010 = NCO1 output is active for 4 input clock periods
                   001 = NCO1 output is active for 2 input clock periods
                   000 = NCO1 output is active for 1 input clock period
bit 4              Unimplemented: Read as ‘0’
bit 3-0            CKS[3:0]: NCO1 Clock Source Select bits
                   1111 = Reserved
                       •
                       •
                       •
                   1011 = Reserved
                   1010 = CLC4_out
                   1001 = CLC3_out
                   1000 = CLC2_out
                   0111 = CLC1_out
                   0110 = CLKREF_out
                   0101 = SOSC
                   0100 = MFINTOSC/4 (32 kHz)
                   0011 = MFINTOSC (500 kHz)
                   0010 = LFINTOSC
                   0001 = HFINTOSC
                   0000 = FOSC

Note 1: N1PWS applies only when operating in Pulse Frequency mode.
     2: If NCO1 pulse width is greater than NCO1 overflow period, operation is undefined.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 455
                        PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 28-3:           NCO1ACCL: NCO1 ACCUMULATOR REGISTER – LOW BYTE
   R/W-0/0           R/W-0/0      R/W-0/0          R/W-0/0         R/W-0/0       R/W-0/0        R/W-0/0         R/W-0/0
                                                           ACC[7:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit               W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged           x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set               ‘0’ = Bit is cleared


bit 7-0            ACC[7:0]: NCO1 Accumulator, Low Byte

REGISTER 28-4:           NCO1ACCH: NCO1 ACCUMULATOR REGISTER – HIGH BYTE
   R/W-0/0           R/W-0/0       R/W-0/0             R/W-0/0        R/W-0/0       R/W-0/0           R/W-0/0    R/W-0/0
                                                          ACC[15:8]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit                W = Writable bit                   U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown                 -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            ACC[15:8]: NCO1 Accumulator, High Byte


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 456
                         PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 28-5:              NCO1ACCU: NCO1 ACCUMULATOR REGISTER – UPPER BYTE(1)
        U-0           U-0          U-0                U-0         R/W-0/0         R/W-0/0        R/W-0/0         R/W-0/0
        —              —            —                 —                                 ACC[19:16]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit               W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged           x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set               ‘0’ = Bit is cleared


bit 7-4            Unimplemented: Read as ‘0’
bit 3-0            ACC[19:16]: NCO1 Accumulator, Upper Byte

Note 1:       The accumulator spans registers NCO1ACCU:NCO1ACCH: NCO1ACCL. The 24 bits are reserved but
              not all are used.This register updates in real time, asynchronously to the CPU; there is no provision to
              ensure atomic access to this 24-bit space using an 8-bit bus. Writing to this register while the module is
              operating will produce undefined results.

REGISTER 28-6:              NCO1INCL: NCO1 INCREMENT REGISTER – LOW BYTE(1,2)
   R/W-0/0           R/W-0/0       R/W-0/0            R/W-0/0        R/W-0/0        R/W-0/0          R/W-0/0     R/W-1/1
                                                            INC[7:0]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            INC[7:0]: NCO1 Increment, Low Byte

Note 1:       The logical increment spans NCO1INCU:NCO1INCH:NCO1INCL.
     2:       NCO1INC is double-buffered as INCBUF; INCBUF is updated on the next falling edge of NCOCLK after
              writing to NCO1INCL; NCO1INCU and NCO1INCH may be written prior to writing NCO1INCL.

REGISTER 28-7:              NCO1INCH: NCO1 INCREMENT REGISTER – HIGH BYTE(1)
   R/W-0/0           R/W-0/0       R/W-0/0            R/W-0/0        R/W-0/0        R/W-0/0          R/W-0/0     R/W-0/0
                                                            INC[15:8]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            INC[15:8]: NCO1 Increment, High Byte

Note 1:       The logical increment spans NCO1INCU:NCO1INCH:NCO1INCL.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 457
                         PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 28-8:              NCO1INCU: NCO1 INCREMENT REGISTER – UPPER BYTE(1)
        U-0            U-0              U-0             U-0             R/W-0/0      R/W-0/0         R/W-0/0           R/W-0/0
        ―                ―              ―               ―                                    INC[19:16]
bit 7                                                                                                                       bit 0


Legend:
R = Readable bit                 W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-4            Unimplemented: Read as ‘0’
bit 3-0            INC[19:16]: NCO1 Increment, Upper Byte

Note 1:       The logical increment spans NCO1INCU:NCO1INCH:NCO1INCL.


TABLE 28-1:          SUMMARY OF REGISTERS ASSOCIATED WITH NCO

                                                                                                                         Register
    Name            Bit 7       Bit 6           Bit 5           Bit 4        Bit 3    Bit 2        Bit 1       Bit 0
                                                                                                                         on Page


NCO1CON             N1EN         ―            N1OUT            N1POL          ―          ―          ―         N1PFM        455
NCO1CLK                        N1PWS[2:0]                        ―            ―                 N1CKS[2:0]                 456
NCO1ACCL                                                      NCO1ACC[7:0]                                                 457
NCO1ACCH                                                      NCO1ACC[15:8]                                                457
NCO1ACCU             ―           ―               ―               ―                   NCO1ACC[19:16]                        458
NCO1INCL                                                      NCO1INC[7:0]                                                 458
NCO1INCH                                                      NCO1INC[15:8]                                                458
NCO1INCU             ―           ―               ―               ―                    NCO1INC[19:16]                       459
Legend:       — = unimplemented read as ‘0’. Shaded cells are not used for NCO module.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 458
