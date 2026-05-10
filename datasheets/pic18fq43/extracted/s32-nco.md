                                                                                                                            PIC18F27/47/57Q43
                                                                                                          NCO - Numerically Controlled Oscillator
                                                                                                                                        Module

32.   NCO - Numerically Controlled Oscillator Module
      The Numerically Controlled Oscillator (NCO) module is a timer that uses overflow from the addition
      of an increment value to divide the input frequency. The advantage of the addition method over a
      simple counter driven timer is that the output frequency resolution does not vary with the divider
      value. The NCO is most useful for applications that require frequency accuracy and fine resolution at
      a fixed duty cycle.
      Features of the NCO include:
      • 20-Bit Increment Function
      •     Fixed Duty Cycle (FDC) mode
      •     Pulse Frequency (PF) mode
      •     Output Pulse-Width Control
      •     Multiple Clock Input Sources
      •     Output Polarity Control
      •     Interrupt Capability
      The following figure is a simplified block diagram of the NCO module.

      Figure 32-1. Numerically Controlled Oscillator Module Simplified Block Diagram

                                                           NCOxINC
                                                                   20
                                          (1)
                                                           INCxBUF
                                                                   20             20


                                                NCO_overflow            Adder
          NCOx Cloc k                                                      20
           Sources
                               NCOx_clk
                                                                   NCOxACC
             See
          NCOxCLK                                                          20
           Register
                                                                                  NCO_interrupt                                          Set NCOxIF

                                                      Fixed Duty
                                                      Cycle Mode
                                                       Circuitry
                                                                                                                                     TRIS control
                      CKS                              D       Q                       D     Q      0
                                                                                                                   NCOx_out
                                                                                                                               PPS
                                                                                             _      1
                                                                                             Q                                                  NCOxOUT
                                                                                                                              RxyPPS
                                                                                                    PFM   POL


                                                                                                                                             To Peripherals

                                                     EN                                S     Q
                                                                                                                                                OUT bit in
                                                                                             _                                Synchronizer      NCOxCO N
                                                    Ripple                                                                                      Register
                                                                                       R     Q
                                                   Counter

                                                                                      Pulse
                                                      R                             Frequency
                                                                                   Mode Circuitry
                                                                   PWS


              Note 1: The increment registers are double-buffered to allow for value changes to be made without first disabling
              the NCO module. The full increment value is loaded into the buffer registers on the second rising edge of the
              NCOx_clk signal that occurs immediately after a write to the NCOxINCL register. The buffers are not user-
              accessible and are shown here for reference.


--- p520 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                      NCO - Numerically Controlled Oscillator
                                                                                                                    Module
32.1   NCO Operation
       The NCO operates by repeatedly adding a fixed value to an accumulator. Additions occur at the
       input clock rate. The accumulator will overflow with a carry periodically, which is the raw NCO output
       (NCO_overflow). This effectively reduces the input clock by the ratio of the addition value to the
       maximum accumulator value. See the following equation.

       Equation 32-1. NCO Overflow Frequency
                      NCO Clock Frequency × Increment Value
       FOVERFLOW =
                                         220

       It is apparent from the equation that there is a linear relationship between the increment value and
       the overflow frequency. This linear advantage over divide-by-n timers comes at the cost of output
       jitter. However, the jitter is always plus or minus one NCO clock period that occurs periodically,
       depending on the division remainder. For example, there is no jitter when there is no division
       remainder, whereas a division remainder of 0.5 will result in a jitter frequency one half of the
       overflow frequency.

32.1.1 NCO Clock Sources
       The NCO can be clocked from a variety of sources including the system clock, internal timers, and
       other peripherals. The NCO clock source is selected by configuring the CKS bits.

32.1.2 Accumulator
       The accumulator is a 20-bit register. Read and write access to the accumulator is available through
       three registers:
       • NCOxACCL
       •   NCOxACCH
       •   NCOxACCU

32.1.3 Adder
       The NCO adder is a full adder, which operates synchronously from the source clock. The addition
       of the previous result and the increment value replaces the accumulator value on the rising edge of
       each input clock.

32.1.4 Increment Registers
       The increment value is stored in three registers making up a 20-bit word. In order of LSB to MSB,
       they are:
       • NCOxINCL
       •   NCOxINCH
       •   NCOxINCU
       The increment registers are readable and writable and are double-buffered to allow value changes
       to be made without first disabling the NCO module.
       When the NCO module is enabled, the NCOxINCU and NCOxINCH registers will be written first,
       followed by the NCOxINCL register. Writing to the NCOxINCL register initiates the increment buffer
       registers to be loaded simultaneously on the second rising edge of the NCO_clk signal.
       When the NCO module is disabled, the increment buffers are loaded immediately after a write to the
       increment registers.


--- p521 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                               NCO - Numerically Controlled Oscillator
                                                                                                                             Module
                        Important: The increment buffer registers are not user-accessible.


32.2   Fixed Duty Cycle Mode
       In Fixed Duty Cycle (FDC) mode, every time the accumulator overflows, the output is toggled.
       This provides a 50% duty cycle at half the FOVERFLOW frequency, provided that the increment value
       remains constant. For more information, see the figure below.
       The FDC mode is selected by clearing the PFM bit.

       Figure 32-2. FDC Output Mode Timing Diagram
                                                                                                                               Rev. 10-000029A
                                                                                                                                     11/12/2018


          NCOx
          Clock
          Source


           NCOx
         Increment               4000h                               4000h                                   4000h
           Value


           NCOx
        Accumulator     00000h 04000h 08000h           FC000h 00000h 04000h 08000h               FC000h 00000h 04000h 08000h
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


32.3   Pulse Frequency Mode
       In Pulse Frequency (PF) mode, the output becomes active on the rising clock edge immediately
       following the overflow event and goes inactive 1 to 128 clock periods later, determined by the PWS
       bits. This provides a pulsed output at the FOVERFLOW frequency. For more information, refer to the
       figure above.


                        Important: When the selected pulse width is greater than the accumulator
                        overflow time frame, then the NCO output does not toggle.


       The level of the Active and Inactive states is determined by the POL bit.
       PF mode is selected by setting the PFM bit.


--- p522 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                        NCO - Numerically Controlled Oscillator
                                                                                                                      Module
32.4   Output Polarity Control
       The last stage in the NCO module is the output polarity. The POL bit selects the output polarity. The
       active level of the Pulse Frequency mode is high true when the POL bit is cleared.
       Changing the polarity while the interrupts are enabled will cause an interrupt for the resulting
       output transition.
       The NCO output signal (NCOx_out) is available by internal routing to several other peripherals.

32.5   Interrupts
       When the accumulator overflows, the NCO Interrupt Flag bit, NCOxIF, in the associated PIR register is
       set. To enable interrupt service on this event, the following bits must be set:
       • EN bit
       •   NCOxIE bit in the associated PIE register
       •   Peripheral and Global Interrupt Enable bits
       The interrupt must be cleared by software by clearing the NCOxIF bit in the Interrupt Service
       Routine.

32.6   Effects of a Reset
       All of the NCO registers are cleared to zero as the result of any Reset.

32.7   Operation in Sleep
       The NCO module operates independently from the system clock and will continue to run during
       Sleep, provided that the clock source selected remains active.
       The HFINTOSC remains active during Sleep when the NCO module is enabled and the HFINTOSC is
       selected as the clock source, regardless of the system clock source selected.
       In other words, if the HFINTOSC is simultaneously selected as the system clock and the NCO clock
       source, when the NCO is enabled, the CPU will go Idle during Sleep, but the NCO will continue to
       operate and the HFINTOSC will remain active.
       With a clock running, it will have a direct effect on the Sleep mode current.

32.8   Register Definitions: NCO
       Long bit name prefixes for the NCO peripherals are shown in the table below. Refer to the “Long Bit
       Names” section in the “Register and Bit Naming Conventions” chapter for more information.

       Table 32-1. NCO Long Bit Name Prefixes
                        Peripheral                                              Bit Name Prefix
                           NCO1                                                         NCO1
                           NCO2                                                         NCO2
                           NCO3                                                         NCO3


--- p523 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                NCO - Numerically Controlled Oscillator
                                                                                                                              Module
32.8.1 NCOxCON

            Name:       NCOxCON
            Address:    0x446,0x44E,0x456
            NCO Control Register

      Bit        7             6              5               4                3                2             1              0
                EN                           OUT             POL                                                            PFM
  Access        R/W                           R              R/W                                                            R/W
   Reset         0                            0               0                                                              0

Bit 7 – EN NCO Enable
            Value      Description
            1          NCO module is enabled
            0          NCO module is disabled

Bit 5 – OUT NCO Output
         Displays the current logic level of the NCO module output.

Bit 4 – POL NCO Polarity
            Value      Description
            1          NCO output signal is inverted
            0          NCO output signal is not inverted

Bit 0 – PFM NCO Pulse Frequency Mode
            Value      Description
            1          NCO operates in Pulse Frequency mode. Output frequency is FOVERFLOW.
            0          NCO operates in Fixed Duty Cycle mode. Output frequency is FOVERFLOW divided by 2.


--- p524 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                 NCO - Numerically Controlled Oscillator
                                                                                                                               Module
32.8.2 NCOxCLK

            Name:         NCOxCLK
            Address:      0x447,0x44F,0x457
            NCO Input Clock Control Register

      Bit           7           6                5               4                   3         2               1              0
                             PWS[2:0]                                                       CKS[4:0]
  Access        R/W            R/W              R/W            R/W                  R/W       R/W            R/W             R/W
   Reset         0              0                0              0                    0         0              0               0

Bits 7:5 – PWS[2:0] NCO Output Pulse-Width Select(1)
            Value        Description
            111          NCO output is active for 128 input clock periods
            110          NCO output is active for 64 input clock periods
            101          NCO output is active for 32 input clock periods
            100          NCO output is active for 16 input clock periods
            011          NCO output is active for 8 input clock periods
            010          NCO output is active for 4 input clock periods
            001          NCO output is active for 2 input clock periods
            000          NCO output is active for 1 input clock periods

Bits 4:0 – CKS[4:0] NCO Clock Source Select
                        CKS                                      Clock Source
                                                                                                                Active in Sleep
                       Value                   NCO1                 NCO2                    NC03
                    11111-11011                                    Reserved                                            -
                       11010                                      CLC8_OUT                                            No
                       11001                                       CLC7_out                                           No
                       11000                                       CLC6_out                                           No
                       10111                                      CLC5_OUT                                            No
                       10110                                      CLC4_OUT                                            No
                       10101                                       CLC3_out                                           No
                       10100                                      CLC2_OUT                                            No
                       10011                                      CLC1_OUT                                            No
                       10010                NCO3_OUT              NCO3_OUT                Reserved                    No
                       10001                NCO2_OUT             Reserved                 NCO2_OUT                    No
                       10000                 Reserved           NCO1_OUT                  NCO1_OUT                    No
                    01111-01011                                  Reserved                                              -
                       01010                                    TMR6_OUT                                              No
                       01001                                    TMR4_OUT                                              No
                       01000                                    TMR2_OUT                                              No
                       00111                                      CLKREF                                              No
                       00110                                      EXTOSC                                              Yes
                       00101                                       SOSC                                               Yes
                       00100                                MFINTOSC (31.25 kHz)                                      Yes
                       00011                                MFINTOSC (500 kHz)                                        Yes
                       00010                                     LFINTOSC                                             Yes
                       00001                                     HFINTOSC                                             Yes
                       00000                                        FOSC                                              No


--- p525 ---
                                                                                              PIC18F27/47/57Q43
                                                                            NCO - Numerically Controlled Oscillator
                                                                                                          Module
Note:
1. PWS applies only when operating in Pulse Frequency mode.


--- p526 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                          NCO - Numerically Controlled Oscillator
                                                                                                                        Module
32.8.3 NCOxACC

           Name:       NCOxACC
           Address:    0x440,0x448,0x450

           NCO Accumulator Register

     Bit        23           22           21            20                  19        18           17                  16
                                                                                        ACC[19:16]
  Access                                                                    R/W      R/W         R/W                  R/W
   Reset                                                                     0        0            0                   0

     Bit        15           14           13            12                  11        10                9              8
                                                              ACC[15:8]
  Access       R/W          R/W          R/W           R/W                  R/W      R/W              R/W             R/W
   Reset        0            0            0             0                    0        0                0               0

     Bit        7            6            5              4                   3            2             1              0
                                                               ACC[7:0]
  Access       R/W          R/W          R/W           R/W                  R/W      R/W              R/W             R/W
   Reset        0            0            0             0                    0        0                0               0

Bits 19:0 – ACC[19:0] Accumulated sum of NCO additions

           Notes:
           1. The individual bytes in this multibyte register can be accessed with the following register names:
               – NCOxACCU: Accesses the upper byte ACC[23:16]
                – NCOxACCH: Accesses the high byte ACC[15:8]
                – NCOxACCL: Accesses the low byte ACC[7:0].
           2. The accumulator spans registers NCOxACCU:NCOxACCH:NCOxACCL. The 24 bits are reserved,
              but not all are used. This register updates in real-time, asynchronously to the CPU; there is no
              provision to ensure atomic access to this 24-bit space using an 8-bit bus. Writing to this register
              while the module is operating will produce undefined results.


--- p527 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                          NCO - Numerically Controlled Oscillator
                                                                                                                        Module
32.8.4 NCOxINC

           Name:       NCOxINC
           Address:    0x443,0x44B,0x453

           NCO Increment Register

     Bit        23          22           21             20                  19        18           17                  16
                                                                                        INC[19:16]
  Access                                                                    R/W      R/W          R/W                 R/W
   Reset                                                                     0        0             0                  0

     Bit        15          14           13             12                  11        10                9              8
                                                              INC[15:8]
  Access       R/W          R/W         R/W            R/W                  R/W      R/W              R/W             R/W
   Reset        0            0           0              0                    0        0                0               0

     Bit        7            6            5              4                   3            2             1              0
                                                               INC[7:0]
  Access       R/W          R/W         R/W            R/W                  R/W      R/W              R/W             R/W
   Reset        0            0           0              0                    0        0                0               1

Bits 19:0 – INC[19:0] Value by which the NCOxACC is increased by each NCO clock

           Notes:
           1. The individual bytes in this multibyte register can be accessed with the following register names:
               – NCOxINCU: Accesses the upper byte INC[19:16]
                – NCOxINCH: Accesses the high byte INC[15:8]
                – NCOxINCL: Accesses the low byte INC[7:0].
           2. The logical increment spans NCOxINCU:NCOxINCH:NCOxINCL.
           3. NCOxINC is double-buffered as INCBUF:
               – INCBUF is updated on the next falling edge of NCOxCLK after writing to NCOxINCL
                – NCOxINCU and NCOxINCH will be written prior to writing NCOxINCL.


--- p528 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                          NCO - Numerically Controlled Oscillator
                                                                                                                        Module
32.9      Register Summary - NCO
Address     Name     Bit Pos.   7         6           5              4                3          2                1          0
                       7:0                                                ACC[7:0]
 0x0440    NCO1ACC    15:8                                                ACC[15:8]
                      23:16                                                                          ACC[19:16]
                       7:0                                                 INC[7:0]
 0x0443    NCO1INC    15:8                                                INC[15:8]
                      23:16                                                                          INC[19:16]
 0x0446    NCO1CON     7:0      EN                   OUT            POL                                                    PFM
 0x0447    NCO1CLK     7:0             PWS[2:0]                                              CKS[4:0]
                       7:0                                                ACC[7:0]
 0x0448    NCO2ACC    15:8                                                ACC[15:8]
                      23:16                                                                          ACC[19:16]
                       7:0                                                 INC[7:0]
 0x044B    NCO2INC    15:8                                                INC[15:8]
                      23:16                                                                          INC[19:16]
 0x044E    NCO2CON     7:0      EN                   OUT            POL                                                    PFM
 0x044F    NCO2CLK     7:0             PWS[2:0]                                              CKS[4:0]
                       7:0                                                ACC[7:0]
 0x0450    NCO3ACC    15:8                                                ACC[15:8]
                      23:16                                                                          ACC[19:16]
                       7:0                                                 INC[7:0]
 0x0453    NCO3INC    15:8                                                INC[15:8]
                      23:16                                                                          INC[19:16]
 0x0456    NCO3CON     7:0      EN                   OUT            POL                                                    PFM
 0x0457    NCO3CLK     7:0             PWS[2:0]                                              CKS[4:0]


--- p529 ---
