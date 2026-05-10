                       PIC18(L)F26/27/45/46/47/55/56/57K42
27.0      CONFIGURABLE LOGIC CELL
          (CLC)
The Configurable Logic Cell (CLCx) module provides
programmable logic that operates outside the speed
limitations of software execution. The logic cell takes up
the input signals and, through the use of configurable
gates, reduces the inputs to four logic lines that drive
one of eight selectable single-output logic functions.
Input sources are a combination of the following:
• I/O pins
• Internal clocks
• Peripherals
• Register bits
The output can be directed internally to peripherals and
to an output pin.
There are four CLC modules available on this device -
CLC1, CLC2, CLC3 and CLC4.
  Note:     The CLC1, CLC2, CLC3 and CLC4 are
            four separate module instances of the
            same CLC module design. Throughout
            this section, the lower case ‘x’ in register
            names is a generic reference to the CLC
            number (which may be substituted with 1,
            2, 3, or 4 during code development). For
            example, the control register is generically
            described in this chapter as CLCxCON,
            but the actual device registers are
            CLC1CON, CLC2CON, CLC3CON and
            CLC4CON.
Refer to Figure 27-1 for a simplified diagram showing
signal flow through the CLCx.
Possible configurations include:
• Combinatorial Logic
  - AND
  - NAND
  - AND-OR
  - AND-OR-INVERT
  - OR-XOR
  - OR-XNOR
• Latches
  - S-R
  - Clocked D with Set and Reset
  - Transparent D with Set and Reset


 2017-2021 Microchip Technology Inc.                        DS40001919G-page 434
                          PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 27-1:              CLCx SIMPLIFIED BLOCK DIAGRAM
                                                                                                                                      Rev. 10-000025H
                                                                                                                                             11/9/2016


                                                                                                                                   OUT
                                                                                                                     D   Q
                                                                                                                                   CLCxOUT

                                                                                                              Q1
                  LCx_in[0]
                  LCx_in[1]                                                                                          CLCx_out
                                                                                                                                 to Peripherals
                  LCx_in[2]


                               Input Data Selection Gates(1)
                      .                                        lcxg1
                                                                                   EN
                                                                                                              CLCxPPS


                      .                                        lcxg2

                                                               lcxg3
                                                                         Logic
                                                                        Function
                                                                           (2)
                                                                                 lcxq
                                                                                                                   PPS                  CLCx


                      .                                        lcxg4
                                                                                        POL                               TRIS

                 LCx_in[n-2]                                           MODE<2:0>                Interrupt
                 LCx_in[n-1]                                                                          det
                  LCx_in[n]
                                                                                                   INTP
                                                                                                                                       set bit
                                                                                                   INTN                                CLCxIF
                                                                                                Interrupt
                                                                                                      det


       Note 1:    See Figure 27-2: Input Data Selection and Gating
            2:    See Figure 27-3: Programmable Logic Functions.


27.1     CLCx Setup                                                                           Data inputs are selected with CLCxSEL0 through
                                                                                              CLCxSEL3        registers (Register 27-3 through
Programming the CLCx module is performed by                                                   Register 27-6).
configuring the four stages in the logic signal flow. The
four stages are:                                                                                Note:       Data selections are undefined at power-up.
• Data selection
• Data gating
• Logic function selection
• Output polarity
Each stage is setup at run time by writing to the
corresponding CLCx Special Function Registers. This
has the added advantage of permitting logic
reconfiguration on-the-fly during program execution.

27.1.1      DATA SELECTION
There are many signals available as inputs to the
configurable logic. Four input multiplexers are used to
select the inputs to pass on to the next stage.
Data selection is through four multiplexers as indicated
on the left side of Figure 27-2. Data inputs in the figure
are identified by a generic numbered input name.
Table 27-1 correlates the generic input name to the
actual signal for each CLC module. The column labeled
‘DyS[5:0] Value’ indicates the MUX selection code for the
selected data input. DyS is an abbreviation for the MUX
select input codes: D1S[5:0] through D4S[5:0].


 2017-2021 Microchip Technology Inc.                                                                                              DS40001919G-page 435
                      PIC18(L)F26/27/45/46/47/55/56/57K42
                                                   TABLE 27-1:      CLCx DATA INPUT SELECTION
TABLE 27-1:       CLCx DATA INPUT                                   (CONTINUED)
                  SELECTION                             DyS[5:0]
                                                                              CLCx Input Source
                                                         Value
       DyS[5:0]
                               CLCx Input Source
        Value                                         001110 [14]      TMR2 _out
    111111 [63]        Reserved                       001101 [13]      TMR1 _overflow
          .                                           001100 [12]      TMR0 _overflow
          .                                           001011 [11]      CLKR _out
          .                                           001010 [10]      ADCRC
    110100 [52]        Reserved                       001001 [9]       SOSC
    110011 [51]        CWG3B_out                      001000 [8]       MFINTOSC (32 kHz)
    110010 [50]        CWG3A_out                      000111 [7]       MFINTOSC (500 kHz)
    110001 [49]        CWG2B_out                      000110 [6]       LFINTOSC
    110000 [48]        CWG2A_out                      000101 [5]       HFINTOSC
    101111 [47]        CWG1B_out                      000100 [4]       FOSC
    101110 [46]        CWG1A_out                      000011 [3]       CLCIN3PPS
    101101 [45]        SS1                            000010 [2]       CLCIN2PPS
    101100 [44]        SCK1                           000001 [1]       CLCIN1PPS
    101011 [43]        SDO1                           000000 [0]       CLCIN0PPS
    101010 [42]        Reserved
    101001 [41]        UART2_tx_out
    101000 [40]        UART1_tx_out
    100111 [39]        CLC4_out
    100110 [38]        CLC3_out
    100101 [37]        CLC2_out
    100100 [36]        CLC1_out
    100011 [35]        DSM1_out
    100010 [34]        IOC_flag
    100001 [33]        ZCD_out
    100000 [32]        CMP2_out
    011111 [31]        CMP1_out
    011110 [30]        NCO1_out
    011101 [29]        Reserved
    011100 [28]        Reserved
    011011 [27]        PWM8_out
    011010 [26]        PWM7_out
    011001 [25]        PWM6_out
    011000 [24]        PWM5_out
    010111 [23]        CCP4_out
    010110 [22]        CCP3_out
    010101 [21]        CCP2_out
    010100 [20]        CCP1 _out
    010011 [19]        SMT1_out
    010010 [18]        TMR6_out
    010001 [17]        TMR5 _overflow
    010000 [16]        TMR4 _out
    001111 [15]        TMR3 _overflow


 2017-2021 Microchip Technology Inc.                                          DS40001919G-page 436
                       PIC18(L)F26/27/45/46/47/55/56/57K42
27.1.2      DATA GATING                                      Data gating is indicated in the right side of Figure 27-2.
                                                             Only one gate is shown in detail. The remaining three
Outputs from the input multiplexers are directed to the
                                                             gates are configured identically with the exception that
desired logic function input through the data gating
                                                             the data enables correspond to the enables for that
stage. Each data gate can direct any combination of the
                                                             gate.
four selected inputs.
  Note:     Data gating is undefined at power-up.            27.1.3      LOGIC FUNCTION
The gate stage is more than just signal direction. The       There are eight available logic functions including:
gate can be configured to direct each input signal as        • AND-OR
inverted or noninverted data. Directed signals are           • OR-XOR
ANDed together in each gate. The output of each gate
                                                             • AND
can be inverted before going on to the logic function
stage.                                                       • S-R Latch
                                                             • D Flip-Flop with Set and Reset
The gating is in essence a 1-to-4 input AND/NAND/OR/
NOR gate. When every input is inverted and the output        • D Flip-Flop with Reset
is inverted, the gate is an OR of all enabled data inputs.   • J-K Flip-Flop with Reset
When the inputs and output are not inverted, the gate        • Transparent Latch with Set and Reset
is an AND or all enabled inputs.                             Logic functions are shown in Figure 27-2. Each logic
Table 27-2 summarizes the basic logic that can be            function has four inputs and one output. The four inputs
obtained in gate 1 by using the gate logic select bits.      are the four data gate outputs of the previous stage.
The table shows the logic of four input variables, but       The output is fed to the inversion stage and from there
                                                             to other peripherals, an output pin, and back to the
each gate can be configured to use less than four. If
                                                             CLCx itself.
no inputs are selected, the output will be zero or one,
depending on the gate output polarity bit.                   27.1.4      OUTPUT POLARITY
TABLE 27-2:        DATA GATING LOGIC                         The last stage in the Configurable Logic Cell is the
                                                             output polarity. Setting the POL bit of the CLCxPOL
   CLCxGLSy            GyPOL            Gate Logic           register inverts the output signal from the logic stage.
0x55               1              AND                        Changing the polarity while the interrupts are enabled
                                                             will cause an interrupt for the resulting output transition.
0x55               0              NAND
0xAA               1              NOR
0xAA               0              OR
0x00               0              Logic 0
0x00               1              Logic 1
It is possible (but not recommended) to select both the
true and negated values of an input. When this is done,
the gate output is zero, regardless of the other inputs,
but may emit logic glitches (transient-induced pulses).
If the output of the channel must be zero or one, the
recommended method is to set all gate bits to zero and
use the gate polarity bit to set the desired level.
Data gating is configured with the logic gate select
registers as follows:
• Gate 1: CLCxGLS0 (Register 27-7)
• Gate 2: CLCxGLS1 (Register 27-8)
• Gate 3: CLCxGLS2 (Register 27-9)
• Gate 4: CLCxGLS3 (Register 27-10)
Register number suffixes are different than the gate
numbers because other variations of this module have
multiple gate selections in the same register.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 437
                       PIC18(L)F26/27/45/46/47/55/56/57K42
27.2     CLCx Interrupts                                    27.6     CLCx Setup Steps
An interrupt will be generated upon a change in the         The following steps may be followed when setting up
output value of the CLCx when the appropriate interrupt     the CLCx:
enables are set. A rising edge detector and a falling       • Disable CLCx by clearing the EN bit.
edge detector are present in each CLC for this purpose.
                                                            • Select desired inputs using CLCxSEL0 through
The CLCxIF bit of the associated PIRx register will be        CLCxSEL3 registers (See Table 27-1).
set when either edge detector is triggered and its          • Clear any associated ANSEL bits.
associated enable bit is set. The INTP enables rising       • Set all TRIS bits associated with inputs.
edge interrupts and the INTN bit enables falling edge
                                                            • Clear all TRIS bits associated with outputs.
interrupts. Both are located in the CLCxCON register.
                                                            • Enable the chosen inputs through the four gates
To fully enable the interrupt, set the following bits:        using CLCxGLS0, CLCxGLS1, CLCxGLS2, and
• CLCxIE bit of the respective PIE register                   CLCxGLS3 registers.
• INTP bit of the CLCxCON register (for a rising            • Select the gate output polarities with the GyPOL
  edge detection)                                             bits of the CLCxPOL register.
• INTN bit of the CLCxCON register (for a falling           • Select the desired logic function with the
  edge detection)                                             MODE[2:0] bits of the CLCxCON register.
• GIE bits of the INTCON0 register                          • Select the desired polarity of the logic output with
The CLCxIF bit of the respective PIR register, must be        the POL bit of the CLCxPOL register. (This step
cleared in software as part of the interrupt service. If      may be combined with the previous gate output
another edge is detected while this flag is being             polarity step).
cleared, the flag will still be set at the end of the       • If driving a device pin, set the desired pin PPS
sequence.                                                     control register and also clear the TRIS bit
                                                              corresponding to that output.
27.3     Output Mirror Copies                               • If interrupts are desired, configure the following
                                                              bits:
Mirror copies of all CON output bits are contained in the     - Set the INTP bit in the CLCxCON register for
CLCxDATA register. Reading this register reads the                rising event.
outputs of all CLCs simultaneously. This prevents any
                                                              - Set the INTN bit in the CLCxCON register for
reading skew introduced by testing or reading the OUT
                                                                  falling event.
bits in the individual CLCxCON registers.
                                                              - Set the CLCxIE bit of the respective PIE
                                                                  register.
27.4     Effects of a Reset
                                                              - Set the GIE bits of the INTCON0 register.
The CLCxCON register is cleared to zero as the result       • Enable the CLCx by setting the EN bit of the
of a Reset. All other selection and gating values remain      CLCxCON register.
unchanged.

27.5     Operation During Sleep
The CLC module operates independently from the
system clock and will continue to run during Sleep,
provided that the input sources selected remain active.
The HFINTOSC remains active during Sleep when the
CLC module is enabled and the HFINTOSC is
selected as an input source, regardless of the system
clock source selected.
In other words, if the HFINTOSC is simultaneously
selected as the system clock and as a CLC input
source, when the CLC is enabled, the CPU will go Idle
during Sleep, but the CLC will continue to operate and
the HFINTOSC will remain active.
This will have a direct effect on the Sleep mode current.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 438
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 27-2:            INPUT DATA SELECTION AND GATING


                                  Data Selection
   LCx_in[0]         000000

                                                                               Data GATE 1

                                           d1T           G1D1T


                                           d1N           G1D1N
   LCx_in[n]         111111
                                                         G1D2T
                              D1S[5:0]

                                                         G1D2N                                    lcxg1
   LCx_in[0]         000000

                                                         G1D3T
                                                                             G1POL
                                           d2T
                                                         G1D3N
                                           d2N
                                                         G1D4T
   LCx_in[n]         111111

                           D2S[5:0]                      G1D4N


   LCx_in[0]         000000
                                                                               Data GATE 2
                                                                                                  lcxg2
                                           d3T
                                                            (Same as Data GATE 1)
                                           d3N
                                                                               Data GATE 3
   LCx_in[n]         111111
                                                                                                 lcxg3
                              D3S[5:0]
                                                            (Same as Data GATE 1)

   LCx_in[0]         000000                                                    Data GATE 4
                                                                                                 lcxg4

                                           d4T              (Same as Data GATE 1)

                                           d4N

   LCx_in[n]         111111

                              D4S[5:0]


   Note:       All controls are undefined at power-up.


 2017-2021 Microchip Technology Inc.                                               DS40001919G-page 439
                         PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 27-3:                 PROGRAMMABLE LOGIC FUNCTIONS
                                                                                                                         Rev. 10-000122B
                                                                                                                                9/13/2016


                                   AND-OR                                                   OR-XOR


             lcxg1                                                      lcxg1

             lcxg2                                                      lcxg2
                                                              lcxq                                                    lcxq
             lcxg3                                                      lcxg3

             lcxg4                                                      lcxg4


                              MODE<2:0> = 000                                            MODE<2:0> = 001
                                 4-input AND                                                S-R Latch


                     lcxg1                                           lcxg1
                                                                                                         S        Q      lcxq
                                                                     lcxg2
                     lcxg2
                                                       lcxq
                     lcxg3
                                                                     lcxg3
                                                                                                         R
                     lcxg4                                           lcxg4


                              MODE<2:0> = 010                                            MODE<2:0> = 011
                      1-Input D Flip-Flop with S and R                             2-Input D Flip-Flop with R
                      lcxg4
                                       S
                                                                     lcxg4
                      lcxg2        D       Q         lcxq                                                D        Q      lcxq
                                                                     lcxg2


                      lcxg1            R
                                                                                            lcxg1            R
                      lcxg3                                                                 lcxg3

                              MODE<2:0> = 100                                            MODE<2:0> = 101
                              J-K Flip-Flop with R                           1-Input Transparent Latch with S and R
                                                                                 lcxg4
                      lcxg2        J       Q         lcxq                                        S
                                                                                 lcxg2      D        Q       lcxq
                      lcxg1
                      lcxg4        K
                                       R
                                                                                 lcxg3      LE
                                                                                                 R
                      lcxg3
                                                                                 lcxg1

                              MODE<2:0> = 110                                            MODE<2:0> = 111


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 440
                        PIC18(L)F26/27/45/46/47/55/56/57K42
27.7      Register Definitions: CLC Control

REGISTER 27-1:           CLCxCON: CONFIGURABLE LOGIC CELL CONTROL REGISTER
   R/W-0/0             U-0           R-0/0          R/W-0/0      R/W-0/0        R/W-0/0       R/W-0/0        R/W-0/0
        EN              —             OUT               INTP      INTN                      MODE[2:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              EN: Configurable Logic Cell Enable bit
                   1 = Configurable logic cell is enabled and mixing input signals
                   0 = Configurable logic cell is disabled and has logic zero output
bit 6              Unimplemented: Read as ‘0’
bit 5              OUT: Configurable Logic Cell Data Output bit
                   Read-only: logic cell output data, after LCPOL; sampled from CLCxOUT
bit 4              INTP: Configurable Logic Cell Positive Edge Going Interrupt Enable bit
                   1 = CLCxIF will be set when a rising edge occurs on CLCxOUT
                   0 = CLCxIF will not be set
bit 3              INTN: Configurable Logic Cell Negative Edge Going Interrupt Enable bit
                   1 = CLCxIF will be set when a falling edge occurs on CLCxOUT
                   0 = CLCxIF will not be set
bit 2-0            MODE[2:0]: Configurable Logic Cell Functional Mode bits
                   111 = Cell is 1-input transparent latch with S and R
                   110 = Cell is J-K flip-flop with R
                   101 = Cell is 2-input D flip-flop with R
                   100 = Cell is 1-input D flip-flop with S and R
                   011 = Cell is S-R latch
                   010 = Cell is 4-input AND
                   001 = Cell is OR-XOR
                   000 = Cell is AND-OR


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 441
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 27-2:           CLCxPOL: SIGNAL POLARITY CONTROL REGISTER
   R/W-0/0             U-0              U-0              U-0      R/W-x/u       R/W-x/u        R/W-x/u         R/W-x/u
        POL             —               —                —        G4POL          G3POL         G2POL           G1POL
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              POL: CLCxOUT Output Polarity Control bit
                   1 = The output of the logic cell is inverted
                   0 = The output of the logic cell is not inverted
bit 6-4            Unimplemented: Read as ‘0’
bit 3              G4POL: Gate 3 Output Polarity Control bit
                   1 = The output of gate 3 is inverted when applied to the logic cell
                   0 = The output of gate 3 is not inverted
bit 2              G3POL: Gate 2 Output Polarity Control bit
                   1 = The output of gate 2 is inverted when applied to the logic cell
                   0 = The output of gate 2 is not inverted
bit 1              G2POL: Gate 1 Output Polarity Control bit
                   1 = The output of gate 1 is inverted when applied to the logic cell
                   0 = The output of gate 1 is not inverted
bit 0              G1POL: Gate 0 Output Polarity Control bit
                   1 = The output of gate 0 is inverted when applied to the logic cell
                   0 = The output of gate 0 is not inverted


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 442
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 27-3:            CLCxSEL0: GENERIC CLCx DATA 0 SELECT REGISTER
          U-0            U-0             R/W-x/u            R/W-x/u      R/W-x/u              R/W-x/u         R/W-x/u         R/W-x/u
          —               —                                                        D1S[5:0]
bit 7                                                                                                                                   bit 0


Legend:
R = Readable bit                     W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                 x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                     ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            D1S[5:0]: CLCx Data1 Input Selection bits
                   See Table 27-1.

REGISTER 27-4:            CLCxSEL1: GENERIC CLCx DATA 1 SELECT REGISTER
          U-0            U-0             R/W-x/u            R/W-x/u      R/W-x/u              R/W-x/u         R/W-x/u         R/W-x/u
          —               —                                                        D2S[5:0]
bit 7                                                                                                                                   bit 0


Legend:
R = Readable bit                     W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                 x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                     ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            D2S[5:0]: CLCx Data 2 Input Selection bits
                   See Table 27-1.

REGISTER 27-5:            CLCxSEL2: GENERIC CLCx DATA 2 SELECT REGISTER
          U-0            U-0             R/W-x/u            R/W-x/u      R/W-x/u              R/W-x/u         R/W-x/u         R/W-x/u
          —               —                                                        D3S[5:0]
bit 7                                                                                                                                   bit 0


Legend:
R = Readable bit                     W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                 x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                     ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            D3S[5:0]: CLCx Data 3 Input Selection bits
                   See Table 27-1.

REGISTER 27-6:            CLCxSEL3: GENERIC CLCx DATA 3 SELECT REGISTER
          U-0            U-0             R/W-x/u            R/W-x/u      R/W-x/u              R/W-x/u         R/W-x/u         R/W-x/u
          —               —                                                        D4S[5:0]
bit 7                                                                                                                                   bit 0


Legend:
R = Readable bit                     W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                 x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                     ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            D4S[5:0]: CLCx Data 4 Input Selection bits
                   See Table 27-1.


 2017-2021 Microchip Technology Inc.                                                                            DS40001919G-page 443
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 27-7:          CLCxGLS0: GATE 0 LOGIC SELECT REGISTER
   R/W-x/u           R/W-x/u       R/W-x/u          R/W-x/u     R/W-x/u       R/W-x/u        R/W-x/u         R/W-x/u
    G1D4T            G1D4N          G1D3T           G1D3N       G1D2T         G1D2N          G1D1T           G1D1N
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              G1D4T: Gate 0 Data 4 True (noninverted) bit
                   1 = CLCIN3 (true) is gated into CLCx Gate 0
                   0 = CLCIN3 (true) is not gated into CLCx Gate 0
bit 6              G1D4N: Gate 0 Data 4 Negated (inverted) bit
                   1 = CLCIN3 (inverted) is gated into CLCx Gate 0
                   0 = CLCIN3 (inverted) is not gated into CLCx Gate 0
bit 5              G1D3T: Gate 0 Data 3 True (noninverted) bit
                   1 = CLCIN2 (true) is gated into CLCx Gate 0
                   0 = CLCIN2 (true) is not gated into CLCx Gate 0
bit 4              G1D3N: Gate 0 Data 3 Negated (inverted) bit
                   1 = CLCIN2 (inverted) is gated into CLCx Gate 0
                   0 = CLCIN2 (inverted) is not gated into CLCx Gate 0
bit 3              G1D2T: Gate 0 Data 2 True (noninverted) bit
                   1 = CLCIN1 (true) is gated into CLCx Gate 0
                   0 = CLCIN1 (true) is not gated into l CLCx Gate 0
bit 2              G1D2N: Gate 0 Data 2 Negated (inverted) bit
                   1 = CLCIN1 (inverted) is gated into CLCx Gate 0
                   0 = CLCIN1 (inverted) is not gated into CLCx Gate 0
bit 1              G1D1T: Gate 0 Data 1 True (noninverted) bit
                   1 = CLCIN0 (true) is gated into CLCx Gate 0
                   0 = CLCIN0 (true) is not gated into CLCx Gate 0
bit 0              G1D1N: Gate 0 Data 1 Negated (inverted) bit
                   1 = CLCIN0 (inverted) is gated into CLCx Gate 0
                   0 = CLCIN0 (inverted) is not gated into CLCx Gate 0


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 444
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 27-8:          CLCxGLS1: GATE 1 LOGIC SELECT REGISTER
   R/W-x/u           R/W-x/u       R/W-x/u          R/W-x/u     R/W-x/u       R/W-x/u        R/W-x/u         R/W-x/u
    G2D4T            G2D4N          G2D3T           G2D3N       G2D2T         G2D2N          G2D1T           G2D1N
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              G2D4T: Gate 1 Data 4 True (noninverted) bit
                   1 = CLCIN3 (true) is gated into CLCx Gate 1
                   0 = CLCIN3 (true) is not gated into CLCx Gate 1
bit 6              G2D4N: Gate 1 Data 4 Negated (inverted) bit
                   1 = CLCIN3 (inverted) is gated into CLCx Gate 1
                   0 = CLCIN3 (inverted) is not gated into CLCx Gate 1
bit 5              G2D3T: Gate 1 Data 3 True (noninverted) bit
                   1 = CLCIN2 (true) is gated into CLCx Gate 1
                   0 = CLCIN2 (true) is not gated into CLCx Gate 1
bit 4              G2D3N: Gate 1 Data 3 Negated (inverted) bit
                   1 = CLCIN2 (inverted) is gated into CLCx Gate 1
                   0 = CLCIN2 (inverted) is not gated into CLCx Gate 1
bit 3              G2D2T: Gate 1 Data 2 True (noninverted) bit
                   1 = CLCIN1 (true) is gated into CLCx Gate 1
                   0 = CLCIN1 (true) is not gated into CLCx Gate 1
bit 2              G2D2N: Gate 1 Data 2 Negated (inverted) bit
                   1 = CLCIN1 (inverted) is gated into CLCx Gate 1
                   0 = CLCIN1 (inverted) is not gated into CLCx Gate 1
bit 1              G2D1T: Gate 1 Data 1 True (noninverted) bit
                   1 = CLCIN0 (true) is gated into CLCx Gate 1
                   0 = CLCIN0 (true) is not gated into CLCx Gate1
bit 0              G2D1N: Gate 1 Data 1 Negated (inverted) bit
                   1 = CLCIN0 (inverted) is gated into CLCx Gate 1
                   0 = CLCIN0 (inverted) is not gated into CLCx Gate 1


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 445
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 27-9:          CLCxGLS2: GATE 2 LOGIC SELECT REGISTER
   R/W-x/u           R/W-x/u       R/W-x/u          R/W-x/u     R/W-x/u       R/W-x/u        R/W-x/u         R/W-x/u
    G3D4T            G3D4N          G3D3T           G3D3N       G3D2T         G3D2N          G3D1T           G3D1N
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              G3D4T: Gate 2 Data 4 True (noninverted) bit
                   1 = CLCIN3 (true) is gated into CLCx Gate 2
                   0 = CLCIN3 (true) is not gated into CLCx Gate 2
bit 6              G3D4N: Gate 2 Data 4 Negated (inverted) bit
                   1 = CLCIN3 (inverted) is gated into CLCx Gate 2
                   0 = CLCIN3 (inverted) is not gated into CLCx Gate 2
bit 5              G3D3T: Gate 2 Data 3 True (noninverted) bit
                   1 = CLCIN2 (true) is gated into CLCx Gate 2
                   0 = CLCIN2 (true) is not gated into CLCx Gate 2
bit 4              G3D3N: Gate 2 Data 3 Negated (inverted) bit
                   1 = CLCIN2 (inverted) is gated into CLCx Gate 2
                   0 = CLCIN2 (inverted) is not gated into CLCx Gate 2
bit 3              G3D2T: Gate 2 Data 2 True (noninverted) bit
                   1 = CLCIN1 (true) is gated into CLCx Gate 2
                   0 = CLCIN1 (true) is not gated into CLCx Gate 2
bit 2              G3D2N: Gate 2 Data 2 Negated (inverted) bit
                   1 = CLCIN1 (inverted) is gated into CLCx Gate 2
                   0 = CLCIN1 (inverted) is not gated into CLCx Gate 2
bit 1              G3D1T: Gate 2 Data 1 True (noninverted) bit
                   1 = CLCIN0 (true) is gated into CLCx Gate 2
                   0 = CLCIN0 (true) is not gated into CLCx Gate 2
bit 0              G3D1N: Gate 2 Data 1 Negated (inverted) bit
                   1 = CLCIN0 (inverted) is gated into CLCx Gate 2
                   0 = CLCIN0 (inverted) is not gated into CLCx Gate 2


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 446
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 27-10: CLCxGLS3: GATE 3 LOGIC SELECT REGISTER
   R/W-x/u           R/W-x/u       R/W-x/u          R/W-x/u     R/W-x/u       R/W-x/u        R/W-x/u         R/W-x/u
    G4D4T            G4D4N          G4D3T           G4D3N       G4D2T         G4D2N          G4D1T           G4D1N
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              G4D4T: Gate 3 Data 4 True (noninverted) bit
                   1 = CLCIN3 (true) is gated into CLCx Gate 3
                   0 = CLCIN3 (true) is not gated into CLCx Gate 3
bit 6              G4D4N: Gate 3 Data 4 Negated (inverted) bit
                   1 = CLCIN3 (inverted) is gated into CLCx Gate 3
                   0 = CLCIN3 (inverted) is not gated into CLCx Gate 3
bit 5              G4D3T: Gate 3 Data 3 True (noninverted) bit
                   1 = CLCIN2 (true) is gated into CLCx Gate 3
                   0 = CLCIN2 (true) is not gated into CLCx Gate 3
bit 4              G4D3N: Gate 3 Data 3 Negated (inverted) bit
                   1 = CLCIN2 (inverted) is gated into CLCx Gate 3
                   0 = CLCIN2 (inverted) is not gated into CLCx Gate 3
bit 3              G4D2T: Gate 3 Data 2 True (noninverted) bit
                   1 = CLCIN1 (true) is gated into CLCx Gate 3
                   0 = CLCIN1 (true) is not gated into CLCx Gate 3
bit 2              G4D2N: Gate 3 Data 2 Negated (inverted) bit
                   1 = CLCIN1 (inverted) is gated into CLCx Gate 3
                   0 = CLCIN1 (inverted) is not gated into CLCx Gate 3
bit 1              G4D1T: Gate 4 Data 1 True (noninverted) bit
                   1 = CLCIN0 (true) is gated into CLCx Gate 3
                   0 = CLCIN0 (true) is not gated into CLCx Gate 3
bit 0              G4D1N: Gate 3 Data 1 Negated (inverted) bit
                   1 = CLCIN0 (inverted) is gated into CLCx Gate 3
                   0 = CLCIN0 (inverted) is not gated into CLCx Gate 3


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 447
                           PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 27-11: CLCDATA: CLC DATA OUTPUT
        U-0                U-0                U-0               U-0          R-0              R-0              R-0             R-0
        —                  —                   —                —        CLC4OUT           CLC3OUT           CLC2OUT         CLC1OUT
bit 7                                                                                                                                bit 0


Legend:
R = Readable bit                         W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                     x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                         ‘0’ = Bit is cleared


bit 7-4             Unimplemented: Read as ‘0’
bit 3               CLC4OUT: Mirror copy of OUT bit of CLC4CON register
bit 2               CLC3OUT: Mirror copy of OUT bit of CLC3CON register
bit 1               CLC2OUT: Mirror copy of OUT bit of CLC2CON register
bit 0               CLC1OUT: Mirror copy of OUT bit of CLC1CON register


TABLE 27-3:           SUMMARY OF REGISTERS ASSOCIATED WITH CLCx

                                                                                                                               Register on
   Name            Bit 7         Bit 6           Bit 5           Bit 4      Bit 3     Bit 2          Bit 1           Bit 0
                                                                                                                                 Page

CLCxCON            EN             ―                OUT           INTP      INTN                     MODE[2:0]                        442
CLCxPOL            POL            ―                 ―             ―       G4POL      G3POL          G2POL            G1POL           443
CLCxSEL0            ―             ―                                             D1S[5:0]                                             444
CLCxSEL1            ―             ―                                             D2S[5:0]                                             444
CLCxSEL2            ―             ―                                             D3S[5:0]                                             444
CLCxSEL3            ―             ―                                             D4S[5:0]                                             444
CLCxGLS0        G1D4T            G1D4N          G1D3T           G1D3N     G1D2T      G1D2N           G1D1T           G1D1N           445
CLCxGLS1        G2D4T            G2D4N          G2D3T           G2D3N     G2D2T      G2D2N           G2D1T           G2D1N           446
CLCxGLS2        G3D4T            G3D4N          G3D3T           G3D3N     G3D2T      G3D2N           G3D1T           G3D1N           447
CLCxGLS3        G4D4T            G4D4N          G4D3T           G4D3N     G4D2T      G4D2N           G4D1T           G4D1N           448
CLCDATA             ―             ―                 ―             ―      CLC4OUT CLC3OUT            CLC2OUT      CLC1OUT             449
Legend:       — = unimplemented, read as ‘0’. Shaded cells are unused by the CLCx modules.


 2017-2021 Microchip Technology Inc.                                                                           DS40001919G-page 448
