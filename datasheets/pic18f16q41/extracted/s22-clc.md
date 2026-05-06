22.   CLC - Configurable Logic Cell
      The Configurable Logic Cell (CLC) module provides programmable logic that operates outside the
      speed limitations of software execution. The logic cell takes up to 256 input signals and, through the
      use of configurable gates, reduces those inputs to four logic lines that drive one of eight selectable
      single-output logic functions.
      Input sources are a combination of the following:
      • I/O pins
      •   Internal clocks
      •   Peripherals
      •   Register bits
      The output can be directed internally to peripherals and to an output pin.
      The following figure is a simplified diagram showing signal flow through the CLC. Possible
      configurations include:
      • Combinatorial Logic
          – AND
           – NAND
           – AND-OR
           – AND-OR-INVERT
           – OR-XOR
           – OR-XNOR
      •   Latches
           – SR
           – Clocked D with Set and Reset
           – Transparent D with Set and Reset


--- p332 ---
       Figure 22-1. CLC Simplified Block Diagram


                                                                                                                                                 OUT
                                                                                                                                   D   Q
                                                                                                                                                 CLCxOUT

                                                                                                                            Q1
              LCx_in[0]
              LCx_in[1]                                                                                                           CLCx_out
                                                                                                                                               to Peripherals
              LCx_in[2]   Input Data Selection Gates(1)

                 .                                        lcx g1
                                                                                 EN
                                                                                                                             RxyPPS


                 .                                        lcx g2

                                                          lcx g3
                                                                    Logic
                                                                   Function
                                                                      (2)
                                                                            lcxq
                                                                                                                                 PPS                  CLCx


                 .                                        lcx g4
                                                                                              POL                                       TRIS

                                                                   MODE                                     Interrupt
            LCx_in[n-2]
            LCx_in[n-1]                                                                                           det
             LCx_in[n]
                                                                                                               INTP
                                                                                                                                                       set bit
                                                                                                               INTN                                    CLCxIF
                                                                                                            Interrupt
                                                                                                                  det


       Notes:
       1. See Figure 22-2 for input data selection and gating.
       2. See Figure 22-3 for programmable logic functions.

22.1   CLC Setup
       Programming the CLC module is performed by configuring the four stages in the logic signal flow.
       The four stages are:
       • Data selection
       •   Data gating
       •   Logic function selection
       •   Output polarity
       Each stage is set up at run time by writing to the corresponding CLC Special Function Registers. This
       has the added advantage of permitting logic reconfiguration on-the-fly during program execution.

22.1.1 Data Selection
       Data inputs are selected with CLCnSEL0 through CLCnSEL3 registers.


                     Important: Data selections are undefined at power-up.


       Depending on the number of bits implemented in the CLCnSELy registers, there can be as
       many as 256 sources available as inputs to the configurable logic. Four multiplexers are used to


--- p333 ---
       independently select these inputs to pass on to the next stage as indicated on the left side of the
       following diagram.
       Data inputs in the figure are identified by a generic numbered input name.

       Figure 22-2. Input Data Selection and Gating

                                          Data Selection

                   LCx_in[0]                                                                    Data GATE 1
                                                                   G1D1T


                                                     d1T           G1D1N


                                                     d1N           G1D2T

                   LCx_in[n]
                                    D1S                            G1D2N                                              lcxg1


                   LCx_in[0]                                       G1D3T                     G1POL


                                                                   G1D3N
                                                      d2T

                                                      d2N          G1D4T


                   LCx_in[n]
                                                                   G1D4N
                                    D2S


                   LCx_in[0]

                                                                                                    Data GATE 2

                                                      d3T                                                             lcxg2

                                                      d3N                   (Same as Data GATE 1)

                   LCx_in[n]
                                    D3S
                                                                                                    Data GATE 3

                   LCx_in[0]
                                                                                                                      lcxg3

                                                                            (Same as Data GATE 1)
                                                      d4T

                                                      d4N
                                                                                                    Data GATE 4
                   LCx_in[n]
                                                                                                                      lcxg4
                                    D4S
                                                                            (Same as Data GATE 1)


                  Note: Allare
       Note: All controls   controls are undefined
                               undefined           at power up
                                          at power-up.

       The CLC Input Selection table correlates the generic input name to the actual signal for each CLC
       module. The table column labeled ‘DyS Value’ indicates the MUX selection code for the selected data
       input. DyS is an abbreviation for the MUX select input codes, D1S through D4S, where ‘y’ is the gate
       number.

22.1.2 Data Gating
       Outputs from the input multiplexers are directed to the desired logic function input through the
       data gating stage. Each data gate can direct any combination of the four selected inputs.
       The gate stage is more than just signal direction. The gate can be configured to direct each input
       signal as inverted or noninverted data. Directed signals are ANDed together in each gate. The output
       of each gate can be inverted before going on to the logic function stage.


--- p334 ---
       The gating is in essence a 1-to-4 input AND/NAND/OR/NOR gate. When every input is inverted and
       the output is inverted, the gate is an AND of all enabled data inputs. When the inputs and output are
       not inverted, the gate is an OR or all enabled inputs.
       Table 22-1 summarizes the basic logic that can be obtained in gate 1 by using the gate logic select
       bits. The table shows the logic of four input variables, but each gate can be configured to use less
       than four. If no inputs are selected, the output will be ‘0’ or ‘1’, depending on the gate output polarity
       bit.

       Table 22-1. Data Gating Logic
                      CLCnGLSy                           GyPOL                         Gate Logic
                        0x55                               1                             AND
                        0x55                               0                             NAND
                        0xAA                               1                             NOR
                        0xAA                               0                              OR
                         0x00                               0                           Logic ‘0’
                         0x00                               1                            Logic ‘1’

       It is possible (but not recommended) to select both the true and negated values of an input. When
       this is done, the gate output is ‘0’, regardless of the other inputs, but may emit logic glitches
       (transient-induced pulses). If the output of the channel must be ‘0’ or ‘1’, the recommended method
       is to set all gate bits to ‘0’ and use the gate polarity bit to set the desired level.
       Data gating is configured with the logic gate select registers as follows:
       • Gate 1: CLCnGLS0
       •   Gate 2: CLCnGLS1
       •   Gate 3: CLCnGLS2
       •   Gate 4: CLCnGLS3
       Note: Register number suffixes are different than the gate numbers because other variations of this
       module have multiple gate selections in the same register.
       Data gating is indicated in the right side of Figure 22-2. Only one gate is shown in detail. The
       remaining three gates are configured identically, except when the data enables correspond to the
       enables for that gate.

22.1.3 Logic Function
       There are eight available logic functions including:
       •   AND-OR
       •   OR-XOR
       •   AND
       •   SR Latch
       •   D Flip-Flop with Set and Reset
       •   D Flip-Flop with Reset
       •   J-K Flip-Flop with Reset
       •   Transparent Latch with Set and Reset
       Logic functions are shown in the following diagram. Each logic function has four inputs and one
       output. The four inputs are the four data gate outputs of the previous stage. The output is fed to the
       inversion stage and from there to other peripherals, an output pin, and back to the CLC itself.


--- p335 ---
       Figure 22-3. Programmable Logic Functions
                                                                                                                                                   Rev. 10-000122B
                                                                                                                                                          9/13/2016


                                         AND-OR                                                                OR-XOR


                   lcxg1                                                                   lcxg1

                   lcxg2                                                                   lcxg2
                                                                    lcxq                                                                 lcxq
                   lcxg3                                                                   lcxg3

                   lcxg4                                                                   lcxg4


                                    MODE<2:0> = 000                                                         MODE<2:0> = 001
                                       4-input AND                                                             S-R Latch


                           lcxg1                                                        lcxg1
                                                                                                                            S        Q      lcxq
                                                                                        lcxg2
                           lcxg2
                                                             lcxq
                           lcxg3
                                                                                        lcxg3
                                                                                                                            R
                           lcxg4                                                        lcxg4


                                    MODE<2:0> = 010                                                         MODE<2:0> = 011
                            1-Input D Flip-Flop with S and R                                          2-Input D Flip-Flop with R
                            lcxg4
                                             S
                                                                                      lcxg4
                            lcxg2        D       Q         lcxq                                                             D        Q      lcxq
                                                                                      lcxg2


                            lcxg1            R
                                                                                                               lcxg1             R
                            lcxg3                                                                              lcxg3

                                    MODE<2:0> = 100                                                         MODE<2:0> = 101
                                    J-K Flip-Flop with R                                        1-Input Transparent Latch with S and R
                                                                                                    lcxg4
                            lcxg2        J       Q         lcxq                                                     S
                                                                                                    lcxg2      D        Q         lcxq
                            lcxg1
                            lcxg4        K
                                             R
                                                                                                    lcxg3      LE
                                                                                                                    R
                            lcxg3
                                                                                                    lcxg1

                                    MODE<2:0> = 110                                                         MODE<2:0> = 111


22.1.4 Output Polarity
       The last stage in the Configurable Logic Cell is the output polarity. Setting the POL bit inverts the
       output signal from the logic stage. Changing the polarity while the interrupts are enabled will cause
       an interrupt for the resulting output transition.

22.2   CLC Interrupts
       An interrupt will be generated upon a change in the output value of the CLCx when the appropriate
       interrupt enables are set. A rising edge detector and a falling edge detector are present in each CLC
       for this purpose.
       The CLCxIF bit of the associated PIR register will be set when either edge detector is triggered and
       its associated enable bit is set. The INTP bit enables rising edge interrupts and the INTN bit enables
       falling edge interrupts.


--- p336 ---
       To fully enable the interrupt, set the following bits:
       • The CLCxIE bit of the respective PIE register
       •   The INTP bit (for a rising edge detection)
       •   The INTN bit (for a falling edge detection)
       If priority interrupts are not used:
       1. Clear the IPEN bit of the INTCON register.
       2. Set the GIE bit of the INTCON register.
       3. Set the GIEL bit of the INTCON register.
       If the CLC is a high-priority interrupt:
       1. Set the IPEN bit of the INTCON register.
       2. Set the CLCxIP bit of the respective IPR register.
       3. Set the GIEH bit of the INTCON register.
       If the CLC is a low-priority interrupt:
       1. Set the IPEN bit of the INTCON register.
       2. Clear the CLCxIP bit of the respective IPR register.
       3. Set the GIEL bit of the INTCON register.
       The CLCxIF bit of the respective PIR register must be cleared in software as part of the interrupt
       service. If another edge is detected while this flag is being cleared, the flag will still be set at the end
       of the sequence.

22.3   Effects of a Reset
       The CLCnCON register is cleared to ‘0’ as the result of a Reset. All other selection and gating values
       remain unchanged.

22.4   Output Mirror Copies
       Mirror copies of all CLCxOUT bits are contained in the CLCDATA register. Reading this register reads
       the outputs of all CLCs simultaneously. This prevents any reading skew introduced by testing or
       reading the OUT bits in the individual CLCnCON registers.

22.5   Operation During Sleep
       The CLC module operates independently from the system clock and will continue to run during
       Sleep, provided that the input sources selected remain Active.
       The HFINTOSC remains Active during Sleep when the CLC module is enabled and the HFINTOSC is
       selected as an input source, regardless of the system clock source selected.
       In other words, if the HFINTOSC is simultaneously selected as both the system clock and as a CLC
       input source then, when the CLC is enabled, the CPU will go Idle during Sleep, but the CLC will
       continue to operate and the HFINTOSC will remain Active. This will have a direct effect on the Sleep
       mode current.

22.6   CLC Setup Steps
       These steps need to be followed when setting up the CLC:
       1. Disable the CLC by clearing the EN bit.
       2. Select the desired inputs using the CLCnSEL0 through CLCnSEL3 registers.
       3. Clear any ANSEL bits associated with CLC input pins.
       4. Set all TRIS bits associated with inputs. However, a CLC input will also operate if the pin is
          configured as an output, in which case the TRIS bits must be cleared.


--- p337 ---
       5. Enable the chosen inputs through the four gates using the CLCnGLS0 through CLCnGLS3
          registers.
       6. Select the gate output polarities with the GyPOL bits.
       7. Select the desired logic function with the MODE bits.
       8. Select the desired polarity of the logic output with the POL bit (this step may be combined with
          the previous gate output polarity step).
       9. If driving a device pin, configure the associated pin PPS control register and also clear the TRIS bit
          corresponding to that output.
       10. Configure the interrupts (optional). See the CLC Interrupts section.
       11. Enable the CLC by setting the EN bit.

22.7   Register Overlay
       All CLCs in this device share the same set of registers. Only one CLC instance is accessible at a
       time. The value in the CLCSELECT register is one less than the selected CLC instance. For example, a
       CLCSELECT value of ‘0’ selects CLC1.

22.8   Register Definitions: Configurable Logic Cell


--- p338 ---
22.8.1 CLCSELECT

            Name:        CLCSELECT
            Address:     0x0D5
            CLC Instance Selection Register
            Selects which CLC instance is accessed by the CLC registers

      Bit           7            6              5               4                  3            2            1                0
                                                                                                                 SLCT[1:0]
  Access                                                                                                   R/W               R/W
   Reset                                                                                                    0                 0

Bits 1:0 – SLCT[1:0] CLC instance selection
            Value       Description
            n           Shared CLC registers of instance n+1 are selected for read and write operations


--- p339 ---
22.8.2 CLCnCON

            Name:       CLCnCON
            Address:    0x0D6

            Configurable Logic Cell Control Register

      Bit        7              6              5                4                  3            2      1                0
                EN                            OUT             INTP               INTN               MODE[2:0]
  Access        R/W                            R              R/W                 R/W      R/W        R/W             R/W
   Reset         0                             0                0                  0        0          0               0

Bit 7 – EN CLC Enable
            Value      Description
            1          Configurable logic cell is enabled and mixing signals
            0          Configurable logic cell is disabled and has logic zero output

Bit 5 – OUT Logic cell output data, after LCPOL. Sampled from CLCxOUT.

Bit 4 – INTP Configurable Logic Cell Positive Edge Going Interrupt Enable
            Value      Description
            1          CLCxIF will be set when a rising edge occurs on CLCxOUT
            0          Rising edges on CLCxOUT have no effect on CLCxIF

Bit 3 – INTN Configurable Logic Cell Negative Edge Going Interrupt Enable
            Value      Description
            1          CLCxIF will be set when a falling edge occurs on CLCxOUT
            0          Falling edges on CLCxOUT have no effect on CLCxIF

Bits 2:0 – MODE[2:0] Configurable Logic Cell Functional Mode Selection
            Value      Description
            111        Cell is 1-input transparent latch with Set and Reset
            110        Cell is J-K flip-flop with Reset
            101        Cell is 2-input D flip-flop with Reset
            100        Cell is 1-input D flip-flop with Set and Reset
            011        Cell is SR latch
            010        Cell is 4-input AND
            001        Cell is OR-XOR
            000        Cell is AND-OR


--- p340 ---
22.8.3 CLCnPOL

            Name:       CLCnPOL
            Address:    0x0D7

            Signal Polarity Control Register

      Bit        7              6                5               4                3         2       1              0
                POL                                                             G4POL     G3POL   G2POL          G1POL
  Access        R/W                                                              R/W       R/W     R/W            R/W
   Reset         0                                                                x         x       x              x

Bit 7 – POL CLCxOUT Output Polarity Control
            Value      Description
            1          The output of the logic cell is inverted
            0          The output of the logic cell is not inverted

Bits 0, 1, 2, 3 – GyPOL Gate Output Polarity Control
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          The gate output is inverted when applied to the logic cell
            0          The output of the gate is not inverted


--- p341 ---
22.8.4 CLCnSEL0

              Name:           CLCnSEL0
              Address:        0x0D8

              Generic CLCn Data 1 Select Register

        Bit         7              6           5                 4                3                  2      1                 0
                                                                               D1S[6:0]
  Access                          R/W         R/W               R/W             R/W              R/W      R/W               R/W
   Reset                           x           x                 x                x               x        x                 x

Bits 6:0 – D1S[6:0] CLCn Data1 Input Selection

   Table 22-2. CLC Input Selection
                    DyS                     Input Source                              DyS (cont.)         Input Source (cont.)
              [0] 0000 0000                  CLCIN0PPS                              [26] 0001 1010          PWM3S1P2_OUT
              [1] 0000 0001                  CLCIN1PPS                              [27] 0001 1011                NCO1
              [2] 0000 0010                  CLCIN2PPS                              [28] 0001 1100              CMP1_OUT
              [3] 0000 0011                  CLCIN3PPS                              [29] 0001 1101              CMP2_OUT
              [4] 0000 0100                        FOSC                             [30] 0001 1110                 ZCD
              [5] 0000 0101                  HFINTOSC(1)                            [31] 0001 1111                 IOC
              [6] 0000 0110                  LFINTOSC     (1)
                                                                                    [32] 0010 0000                DSM1
              [7] 0000 0111                  MFINTOSC(1)                            [33] 0010 0001              HLVD_OUT
              [8] 0000 1000              MFINTOSC (32 kHz)(1)                       [34] 0010 0010                CLC1
              [9] 0000 1001              SFINTOSC (1 MHz)(1)                        [35] 0010 0011                CLC2
              [10] 0000 1010                   SOSC(1)                              [36] 0010 0100                CLC3
              [11] 0000 1011                  EXTOSC(1)                             [37] 0010 0101                CLC4
              [12] 0000 1100                  ADCRC(1)                              [38] 0010 0110                U1TX
              [13] 0000 1101                    CLKR                                [39] 0010 0111                U2TX
              [14] 0000 1110                    TMR0                                [40] 0010 1000                U3TX
              [15] 0000 1111                    TMR1                                [41] 0010 1001              SPI1_SDO
              [16] 0001 0000                    TMR2                                [42] 0010 1010              SPI1_SCK
              [17] 0001 0001                    TMR3                                [43] 0010 1011               SPI1_SS
              [18] 0001 0010                    TMR4                                [44] 0010 1100              SPI2_SDO
              [19] 0001 0011                    SMT1                                [45] 0010 1101              SPI2_SCK
              [20] 0001 0100                    CCP1                                [46] 0010 1110               SPI2_SS
              [21] 0001 0101              PWM1S1P1_OUT                              [47] 0010 1111               I2C_SCL
              [22] 0001 0110              PWM1S1P2_OUT                              [48] 0011 0000               I2C_SDA
              [23] 0001 0111              PWM2S1P1_OUT                              [49] 0011 0001               CWG1A
              [24] 0001 1000              PWM2S1P2_OUT                              [50] 0011 0010               CWG1B
              [25] 0001 1001              PWM3S1P1_OUT                              [51] 0011 0011                   -
   Note:
   1.   Requests clock.


              Reset States: POR/BOR = xxxxxxx
                            All Other Resets = uuuuuuu


--- p342 ---
22.8.5 CLCnSEL1

            Name:        CLCnSEL1
            Address:     0x0D9

            Generic CLCn Data 1 Select Register

      Bit           7            6               5               4                3              2      1               0
                                                                               D2S[6:0]
  Access                       R/W             R/W             R/W              R/W         R/W       R/W             R/W
   Reset                        x               x               x                 x          x         x               x

Bits 6:0 – D2S[6:0] CLCn Data2 Input Selection
          Reset States: POR/BOR = xxxxxxx
                        All Other Resets = uuuuuuu
            Value       Description
            n           Refer to the CLC Input Selection table for input selections


--- p343 ---
22.8.6 CLCnSEL2

            Name:        CLCnSEL2
            Address:     0x0DA

            Generic CLCn Data 1 Select Register

      Bit           7            6               5               4                3              2      1               0
                                                                               D3S[6:0]
  Access                       R/W             R/W             R/W              R/W         R/W       R/W             R/W
   Reset                        x               x               x                 x          x         x               x

Bits 6:0 – D3S[6:0] CLCn Data3 Input Selection
          Reset States: POR/BOR = xxxxxxx
                        All Other Resets = uuuuuuu
            Value       Description
            n           Refer to the CLC Input Selection table for input selections


--- p344 ---
22.8.7 CLCnSEL3

            Name:        CLCnSEL3
            Address:     0x0DB

            Generic CLCn Data 4 Select Register

      Bit           7            6               5               4                3              2      1               0
                                                                               D4S[6:0]
  Access                       R/W             R/W             R/W              R/W         R/W       R/W             R/W
   Reset                        x               x               x                 x          x         x               x

Bits 6:0 – D4S[6:0] CLCn Data4 Input Selection
          Reset States: POR/BOR = xxxxxxx
                        All Other Resets = uuuuuuu
            Value       Description
            n           Refer to the CLC Input Selection table for input selections


--- p345 ---
22.8.8 CLCnGLS0

            Name:       CLCnGLS0
            Address:    0x0DC

            CLCn Gate1 Logic Select Register

      Bit        7            6               5                 4              3              2       1              0
               G1D4T        G1D4N           G1D3T             G1D3N          G1D2T          G1D2N   G1D1T          G1D1N
  Access        R/W          R/W             R/W               R/W            R/W            R/W     R/W            R/W
   Reset         x            x               x                 x              x              x       x              x

Bits 1, 3, 5, 7 – G1DyT dyT: Gate1 Data ‘y’ True (noninverted)
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          dyT is gated into g1
            0          dyT is not gated into g1

Bits 0, 2, 4, 6 – G1DyN dyN: Gate1 Data ‘y’ Negated (inverted)
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          dyN is gated into g1
            0          dyN is not gated into g1


--- p346 ---
22.8.9 CLCnGLS1

            Name:       CLCnGLS1
            Address:    0x0DD

            CLCn Gate2 Logic Select Register

      Bit        7            6               5                 4              3              2       1              0
               G2D4T        G2D4N           G2D3T             G2D3N          G2D2T          G2D2N   G2D1T          G2D1N
  Access        R/W          R/W             R/W               R/W            R/W            R/W     R/W            R/W
   Reset         x            x               x                 x              x              x       x              x

Bits 1, 3, 5, 7 – G2DyT dyT: Gate2 Data ‘y’ True (noninverted)
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          dyT is gated into g2
            0          dyT is not gated into g2

Bits 0, 2, 4, 6 – G2DyN dyN: Gate2 Data ‘y’ Negated (inverted)
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          dyN is gated into g2
            0          dyN is not gated into g2


--- p347 ---
22.8.10 CLCnGLS2

            Name:       CLCnGLS2
            Address:    0x0DE

            CLCn Gate3 Logic Select Register

      Bit        7            6               5                 4              3              2       1              0
               G3D4T        G3D4N           G3D3T             G3D3N          G3D2T          G3D2N   G3D1T          G3D1N
  Access        R/W          R/W             R/W               R/W            R/W            R/W     R/W            R/W
   Reset         x            x               x                 x              x              x       x              x

Bits 1, 3, 5, 7 – G3DyT dyT: Gate3 Data ‘y’ True (noninverted)
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          dyT is gated into g3
            0          dyT is not gated into g3

Bits 0, 2, 4, 6 – G3DyN dyN: Gate3 Data ‘y’ Negated (inverted)
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          dyN is gated into g3
            0          dyN is not gated into g3


--- p348 ---
22.8.11 CLCnGLS3

            Name:       CLCnGLS3
            Address:    0x0DF

            CLCn Gate4 Logic Select Register

      Bit        7            6               5                 4              3              2       1              0
               G4D4T        G4D4N           G4D3T             G4D3N          G4D2T          G4D2N   G4D1T          G4D1N
  Access        R/W          R/W             R/W               R/W            R/W            R/W     R/W            R/W
   Reset         x            x               x                 x              x              x       x              x

Bits 1, 3, 5, 7 – G4DyT dyT: Gate4 Data ‘y’ True (noninverted)
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          dyT is gated into g4
            0          dyT is not gated into g4

Bits 0, 2, 4, 6 – G4DyN dyN: Gate4 Data ‘y’ Negated (inverted)
          Reset States: POR/BOR = xxxx
                        All Other Resets = uuuu
            Value      Description
            1          dyN is gated into g4
            0          dyN is not gated into g4


--- p349 ---
22.8.12 CLCDATA

            Name:        CLCDATA
            Address:     0x0D4
            CLC Data Output Register
            Mirror copy of CLC outputs

      Bit           7           6        5              4               3            2         1              0
                                                                     CLC4OUT      CLC3OUT   CLC2OUT        CLC1OUT
  Access                                                               R/W          R/W       R/W            R/W
   Reset                                                                0            0         0              0

Bits 0, 1, 2, 3 – CLCxOUT Mirror copy of CLCx_out
            Value       Description
            1           CLCx_out is 1
            0           CLCx_out is 0


--- p350 ---
22.9      Register Summary - CLC Control
Address     Name       Bit Pos.     7          6           5             4         3          2            1            0
 0x00
  ...      Reserved
 0xD3
 0xD4       CLCDATA      7:0                                                    CLC4OUT    CLC3OUT    CLC2OUT     CLC1OUT
 0xD5      CLCSELECT     7:0                                                                                SLCT[1:0]
 0xD6      CLCnCON       7:0      EN                      OUT           INTP      INTN                MODE[2:0]
 0xD7       CLCnPOL      7:0      POL                                           G4POL      G3POL       G2POL        G1POL
 0xD8      CLCnSEL0      7:0                                                    D1S[6:0]
 0xD9      CLCnSEL1      7:0                                                    D2S[6:0]
 0xDA      CLCnSEL2      7:0                                                    D3S[6:0]
 0xDB      CLCnSEL3      7:0                                                    D4S[6:0]
 0xDC      CLCnGLS0      7:0      G1D4T      G1D4N       G1D3T       G1D3N       G1D2T     G1D2N        G1D1T        G1D1N
 0xDD      CLCnGLS1      7:0      G2D4T      G2D4N       G2D3T       G2D3N       G2D2T     G2D2N        G2D1T        G2D1N
 0xDE      CLCnGLS2      7:0      G3D4T      G3D4N       G3D3T       G3D3N       G3D2T     G3D2N        G3D1T        G3D1N
 0xDF      CLCnGLS3      7:0      G4D4T      G4D4N       G4D3T       G4D3N       G4D2T     G4D2N        G4D1T        G4D1N


--- p351 ---
