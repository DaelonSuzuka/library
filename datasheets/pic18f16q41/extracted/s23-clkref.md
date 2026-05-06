23.    CLKREF - Reference Clock Output Module
       The reference clock output module provides the ability to send a clock signal to the clock reference
       output pin (CLKR). The reference clock output can be routed internally as an input signal for other
       peripherals, such as the timers and CLCs.
       The reference clock output module has the following features:
       •   Selectable clock source using the CLKRCLK register
       •   Programmable clock divider
       •   Selectable duty cycle
       The figure below shows the simplified block diagram of the clock reference module.

       Figure 23-1. Clock Reference Block Diagram

                                                                                                                                      Rev. 10-000261B
                                                                                                                                             1/23/2019


                                                                                                        DIV
                                                  EN         Counter Reset
                                                                                                       128
                                                                                                              111


                                                                             Reference Clock Divider
                  See                                                                                  64                  DC       RxyPPS
                CLKRCLK                                                                                       110
                 Register                                                                              32
                                                                                                              101
                                                                                                       16                                         CLKR
                                                                                                              100
                                                                                                        8              Duty Cycle     PPS
                                                                                                              011
                                                                                                        4
                                                                                                              010
                                                                                                        2
                                                                                                              001               To Peripherals

                                    EN                                                                        000
                     CLK


       Figure 23-2. Clock Reference Timing

                                                                                                                                      Rev. 10-000264B
                                                                                                                                             1/23/2019

                                       P1          P2

                         CLKRCLK


                            EN

                   CLKR Output
                      DIV = 001
                      DC = 10
                                     Duty Cycle
                                       (50%)

                   CLKR Output         CLKRCLK/2
                      DIV = 001
                      DC = 01
                                    Duty Cycle
                                      (25%)


23.1   Clock Source
       The clock source of the reference clock peripheral is selected with the CLK bits.


--- p352 ---
23.1.1 Clock Synchronization
       The CLKR output signal is ensured to be glitch-free when the EN bit is set to start the module and
       enable the CLKR output. When the reference clock output is disabled, the output signal will be
       disabled immediately.

23.2   Programmable Clock Divider
       The module takes the clock input and divides it based on the value of the DIV bits.
       The following configurations are available:
       •   Base clock frequency value
       •   Base clock frequency divided by 2
       •   Base clock frequency divided by 4
       •   Base clock frequency divided by 8
       •   Base clock frequency divided by 16
       •   Base clock frequency divided by 32
       •   Base clock frequency divided by 64
       •   Base clock frequency divided by 128

23.3   Selectable Duty Cycle
       The DC bits are used to modify the duty cycle of the output clock. A duty cycle of 0%, 25%, 50%, or
       75% can be selected for all clock rates when the DIV value is not 0b000. When DIV = 0b000, the duty
       cycle defaults to 50% for all values of DC except 0b00, in which case the duty cycle is 0% (constant
       low output).


                    Important: The DC value at Reset is 10. This makes the default duty cycle 50% and not 0%.


                    Important: Clock dividers and clock duty cycles can be changed while the module is
                    enabled but doing so may cause glitches to occur on the output. To avoid possible glitches,
                    clock dividers and clock duty cycles will be changed only when the EN bit is clear.


23.4   Operation in Sleep Mode
       The reference clock module continues to operate and provide a signal output in Sleep for all clock
       source selections except FOSC (CLK = 0).

23.5   Register Definitions: Reference Clock
       Long bit name prefixes for the Reference Clock peripherals are shown in the following table. Refer
       to the “Long Bit Names” section in the “Register and Bit Naming Conventions” chapter for more
       information.

       Table 23-1. CLKREF Long Bit Name Prefixes
                         Peripheral                                             Bit Name Prefix
                           CLKR                                                         CLKR


--- p353 ---
23.5.1 CLKRCON

            Name:       CLKRCON
            Address:    0x039

            Reference Clock Control Register

      Bit        7             6               5             4                   3            2             1              0
                EN                                                 DC[1:0]                               DIV[2:0]
  Access        R/W                                         R/W                 R/W      R/W               R/W           R/W
   Reset         0                                           1                   0        0                 0             0

Bit 7 – EN Reference Clock Module Enable
            Value      Description
            1          Reference clock module enabled
            0          Reference clock module is disabled

Bits 4:3 – DC[1:0] Reference Clock Duty Cycle(1)
            Value      Description
            11         Clock outputs duty cycle of 75%
            10         Clock outputs duty cycle of 50%
            01         Clock outputs duty cycle of 25%
            00         Clock outputs duty cycle of 0%

Bits 2:0 – DIV[2:0] Reference Clock Divider
            Value      Description
            111        Base clock value divided by 128
            110        Base clock value divided by 64
            101        Base clock value divided by 32
            100        Base clock value divided by 16
            011        Base clock value divided by 8
            010        Base clock value divided by 4
            001        Base clock value divided by 2
            000        Base clock value

            Note:
            1. Bits are valid for DIV ≥ 001. For DIV = 000, duty cycle is fixed at 50%.


--- p354 ---
23.5.2 CLKRCLK

            Name:        CLKRCLK
            Address:     0x03A

            Clock Reference Clock Selection Register

      Bit         7             6            5              4                   3            2               1            0
                                                                                                 CLK[3:0]
  Access                                                                       R/W       R/W                R/W         R/W
   Reset                                                                        0         0                  0           0

Bits 3:0 – CLK[3:0] CLKR Clock Selection

            Table 23-2. Clock Reference Module Clock Sources
                                    CLK                                                 Clock Source
                            1111 - 1100                                                   Reserved
                               1011                                                      CLC4_OUT
                               1010                                                      CLC3_OUT
                               1001                                                      CLC2_OUT
                               1000                                                      CLC1_OUT
                               0111                                                      NCO1_OUT
                               0110                                                        EXTOSC
                               0101                                                         SOSC
                               0100                                                  MFINTOSC (32 kHz)
                               0011                                                  MFINTOSC (500 kHz)
                                0010                                                     LFINTOSC
                                0001                                                     HFINTOSC
                                0000                                                        FOSC


--- p355 ---
23.6      Register Summary - Reference CLK
Address     Name      Bit Pos.   7         6           5             4             3           2             1              0
 0x00
  ...      Reserved
 0x38
 0x39      CLKRCON      7:0      EN                                      DC[1:0]                          DIV[2:0]
 0x3A      CLKRCLK      7:0                                                                        CLK[3:0]


--- p356 ---
