                                                                                                         PIC18F27/47/57Q43
                                                                                        CCP - Capture/Compare/PWM Module


28.    CCP - Capture/Compare/PWM Module
       The Capture/Compare/PWM module is a peripheral that allows the user to time and control different
       events and to generate Pulse-Width Modulation (PWM) signals. In Capture mode, the peripheral
       allows the timing of the duration of an event. The Compare mode allows the user to trigger an
       external event when a predetermined amount of time has expired. The PWM mode can generate
       Pulse-Width Modulated signals of varying frequency and duty cycle.
       Each individual CCP module can select the timer source that controls the module. The default timer
       selection is Timer1 when using Capture/Compare mode and Timer2 when using PWM mode in the
       CCPx module.
       Note that the Capture/Compare mode operation is described with respect to Timer1 and the PWM
       mode operation is described with respect to Timer2 in the following sections.
       The Capture and Compare functions are identical for all CCP modules.


                    Important: In devices with more than one CCP module, it is very important to
                    pay close attention to the register names used. Throughout this section, the prefix
                    “CCPx” is used as a generic replacement for specific numbering. A number placed
                    where the “x” is in the prefix is used to distinguish between separate modules. For
                    example, CCP1CON and CCP2CON control the same operational aspects of two
                    completely different CCP modules.


28.1   CCP Module Configuration
       Each Capture/Compare/PWM module is associated with a control register (CCPxCON), a capture
       input selection register (CCPxCAP) and a data register (CCPRx). The data register, in turn, is
       comprised of two 8-bit registers: CCPRxL (low byte) and CCPRxH (high byte).

28.1.1 CCP Modules and Timer Resources
       The CCP modules utilize Timers 1 through 6 that vary with the selected mode. Various timers are
       available to the CCP modules in Capture, Compare or PWM modes, as shown in the table below.

       Table 28-1. CCP Mode - Timer Resources
                   CCP Mode                                                Timer Resource
                    Capture
                                                                       Timer1, Timer3 or Timer5
                   Compare
                     PWM                                               Timer2, Timer4 or Timer6

       The assignment of a particular timer to a module is selected as shown in the “Capture, Compare,
       and PWM Timers Selection” chapter. All of the modules may be active at once and may share the
       same timer resource if they are configured to operate in the same mode (Capture/Compare or PWM)
       at the same time.

28.1.2 Open-Drain Output Option
       When operating in Output mode (the Compare or PWM modes), the drivers for the CCPx pins can
       be optionally configured as open-drain outputs. This feature allows the voltage level on the pin to be
       pulled to a higher level through an external pull-up resistor and allows the output to communicate
       with external circuits without the need for additional level shifters.


--- p449 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                CCP - Capture/Compare/PWM Module

28.2   Capture Mode
       Capture mode makes use of the 16-bit odd numbered timer resources (Timer1, Timer3, etc.). When
       an event occurs on the capture source, the 16-bit CCPRx register captures and stores the 16-bit value
       of the TMRx register. An event is defined as one of the following and is configured by the MODE bits:
       •    Every falling edge of CCPx input
       •    Every rising edge of CCPx input
       •    Every 4th rising edge of CCPx input
       •    Every 16th rising edge of CCPx input
       •    Every edge of CCPx input (rising or falling)
       When a capture is made, the Interrupt Request Flag bit CCPxIF of the PIRx register is set. The
       interrupt flag must be cleared in software. If another capture occurs before the value in the CCPRx
       register is read, the old captured value is overwritten by the new captured value. The following figure
       shows a simplified diagram of the capture operation.


                       Important: If an event occurs during a 2-byte read, the high and low-byte data
                       will be from different events. It is recommended while reading the CCPRx register
                       pair to either disable the module or read the register pair twice for data integrity.


       Figure 28-1. Capture Mode Operation Block Diagram

                                                                                                                           Rev. 10-000158E
                                                                                                                                  3/11/2019
                                                                                                         RxyPPS
                                                                                                                           CCPx
                                                                                                          PPS
                                      CTS
                                                                                                                    TRIS


                                                                                                                  CCPRx

                                                                                                                     16
           Capture Trigger Sources                                                 set CCPxIF
           See CCPxCAP register                    Prescaler            and
                                                    1,4,16           Edge Detect
                                                                                                                     16
               CCPx            PPS
                                                            MODE                                                  TMR1

                            CCPxPPS


28.2.1 Capture Sources
       The capture source is selected with the CTS bits.
       In Capture mode, the CCPx pin must be configured as an input by setting the associated TRIS control
       bit.


                       Important: If the CCPx pin is configured as an output, a write to the port can
                       cause a capture event.


28.2.2 Timer1 Mode for Capture
       Timer1 must be running in Timer mode or Synchronized Counter mode for the CCP module to use
       the capture feature. In Asynchronous Counter mode, the capture operation may not work.


--- p450 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                       CCP - Capture/Compare/PWM Module

       See the “TMR1 - Timer1 Module with Gate Control” chapter for more information on configuring
       Timer1.

28.2.3 Software Interrupt Mode
       When the Capture mode is changed, a false capture interrupt may be generated. The user will keep
       the CCPxIE Interrupt Enable bit of the PIEx register clear to avoid false interrupts. Additionally, the
       user will clear the CCPxIF Interrupt Flag bit of the PIRx register following any change in Operating
       mode.


                   Important: Clocking Timer1 from the system clock (FOSC) must not be used in
                   Capture mode. For Capture mode to recognize the trigger event on the CCPx pin,
                   Timer1 must be clocked from the instruction clock (FOSC/4) or from an external
                   clock source.


28.2.4 CCP Prescaler
       There are four prescaler settings specified by the MODE bits. Whenever the CCP module is turned
       off or when the CCP module is not in Capture mode, the prescaler counter is cleared. Any Reset will
       clear the prescaler counter.
       Switching from one capture prescaler to another does not clear the prescaler and may generate a
       false interrupt. To avoid this unexpected operation, turn the module off by clearing the CCPxCON
       register before changing the prescaler. The example below demonstrates the code to perform this
       function.

               Example 28-1. Changing between Capture Prescalers

                BANKSEL CCP1CON          ;only needed when CCP1CON is not in ACCESS space
                CLRF    CCP1CON          ;Turn CCP module off
                MOVLW   NEW_CAPT_PS      ;CCP ON and Prescaler select → W
                MOVWF   CCP1CON          ;Load CCP1CON with this value


28.2.5 Capture During Sleep
       Capture mode depends upon the Timer1 module for proper operation. There are two options for
       driving the Timer1 module in Capture mode. It can be driven by the instruction clock (FOSC/4) or by
       an external clock source.
       When Timer1 is clocked by FOSC/4, Timer1 will not increment during Sleep. When the device wakes
       from Sleep, Timer1 will continue from its previous state.
       Capture mode will operate during Sleep when Timer1 is clocked by an external clock source.

28.3   Compare Mode
       The Compare mode function described in this section is available and identical for all CCP modules.
       Compare mode makes use of the 16-bit odd numbered Timer resources (Timer1, Timer3, etc.). The
       16-bit value of the CCPRx register is constantly compared against the 16-bit value of the TMRx
       register. When a match occurs, one of the following events can occur:
       •   Toggle the CCPx output and clear TMRx
       •   Toggle the CCPx output without clearing TMRx
       •   Set the CCPx output
       •   Clear the CCPx output
       •   Generate a Pulse output


--- p451 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                            CCP - Capture/Compare/PWM Module

       •   Generate a Pulse output and clear TMRx
       The action on the pin is based on the value of the MODE control bits.
       All Compare modes can generate an interrupt. When MODE = ‘b0001 or ‘b1011, the CCP resets the
       TMRx register.
       The following figure shows a simplified diagram of the compare operation.

       Figure 28-2. Compare Mode Operation Block Diagram

                                                                      MODE


                                                                               Auto-conversion Trigger


                                                                                                  CCPRx

                    CCPx         PPS                  Q    S          Output
                                                                                                Comparator
                                                                      Logic
                                                           R

                                RxyPPS
                                                                                                  TMR1
                                           TRIS


                                                               Set CCPxIF Interrupt Flag


28.3.1 CCPx Pin Configuration
       The CCPx pin must be configured as an output in software by clearing the associated TRIS bit and
       defining the appropriate output pin through the RxyPPS registers. See the “PPS - Peripheral Pin
       Select Module” chapter for more details.
       The CCP output can also be used as an input for other peripherals.


                   Important: Clearing the CCPxCON register will force the CCPx compare output
                   latch to the default low level. This is not the PORT I/O data latch.


28.3.2 Timer1 Mode for Compare
       In Compare mode, Timer1 must be running in either Timer mode or Synchronized Counter mode.
       The compare operation may not work in Asynchronous Counter mode.
       See the “TMR1 - Timer1 Module with Gate Control” chapter for more information on configuring
       Timer1.


                   Important: Clocking Timer1 from the system clock (FOSC) must not be used
                   in Compare mode. For Compare mode to recognize the trigger event on the
                   CCPx pin, Timer1 must be clocked from the instruction clock (FOSC/4) or from an
                   external clock source.


28.3.3 Compare During Sleep
       Since FOSC is shut down during Sleep mode, the Compare mode will not function properly during
       Sleep, unless the timer is running. The device will wake on interrupt (if enabled).


--- p452 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                         CCP - Capture/Compare/PWM Module

28.4   PWM Overview
       Pulse-Width Modulation (PWM) is a scheme that controls power to a load by switching quickly
       between fully ON and fully OFF states. The PWM signal resembles a square wave where the high
       portion of the signal is considered the ON state and the low portion of the signal is considered the
       OFF state. The high portion, also known as the pulse width, can vary in time and is defined in steps.
       A larger number of steps applied, which lengthens the pulse width, also supplies more power to the
       load. Lowering the number of steps applied, which shortens the pulse width, supplies less power.
       The PWM period is defined as the duration of one complete cycle or the total amount of ON and OFF
       time combined.
       PWM resolution defines the maximum number of steps that can be present in a single PWM period.
       A higher resolution allows for more precise control of the power applied to the load.
       The term duty cycle describes the proportion of the ON time to the OFF time and is expressed in
       percentages, where 0% is fully OFF and 100% is fully ON. A lower duty cycle corresponds to less
       power applied and a higher duty cycle corresponds to more power applied. The figure below shows
       a typical waveform of the PWM signal.

       Figure 28-3. CCP PWM Output Signal

                                            Period


                                    Pulse Width
                                                                        TMR2 = PR2

                                                           TMR2 = CCPRx

                                        TMR2 = 0


28.4.1 Standard PWM Operation
       The standard PWM function described in this section is available and identical for all CCP modules. It
       generates a Pulse-Width Modulation (PWM) signal on the CCPx pin with up to ten bits of resolution.
       The period, duty cycle and resolution are controlled by the following registers:
       •   Even numbered TxPR registers (T2PR, T4PR, etc.)
       •   Even numbered TxCON registers (T2CON, T4CON, etc.)
       •   16-bit CCPRx registers
       •   CCPxCON registers
       It is required to have FOSC/4 as the clock input to TxTMR for correct PWM operation. The following
       figure shows a simplified block diagram of the PWM operation.


--- p453 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                     CCP - Capture/Compare/PWM Module

       Figure 28-4. Simplified PWM Block Diagram

                                                                                                                           Rev. 10-000 157C

                       Duty cycle registers                                                                                       2/20/201 9


                   CCPRxH          CCPRxL
                                                                                        CCPx_out
                                                                                                          to peripherals
                                                                                                    set CCPIF
                        10-bit Latch(2)
                   (Not accessible by user)


                          Comparator                              R       Q             PPS                         CCPx


                                                                  S                   RxyPPS
              TMR2 Module                                                                                  TRIS Control

                                      R
                          TMR2                (1)


                                    ERS logic
                        Comparator                            CCPx_pset


                            PR2


              Notes:    1. An 8-bit timer is concatenated with two bits generated by Fosc or two bits of the internal prescaler
                           to create 10-bit time base.
                        2. The alignment of the 10 bits from the CCPR register is determined by the CCPxFMT bit.


                    Important: The corresponding TRIS bit must be cleared to enable the PWM
                    output on the CCPx pin.


28.4.2 Setup for PWM Operation
       The following steps illustrate how to configure the CCP module for standard PWM operation:
       1. Select the desired output pin with the RxyPPS control to select CCPx as the source. Disable the
          selected pin output driver by setting the associated TRIS bit. The output will be enabled later at
          the end of the PWM setup.
       2. Load the selected timer TxPR period register with the PWM period value.
       3. Configure the CCP module for the PWM mode by loading the CCPxCON register with the
          appropriate values.
       4. Load the CCPRx register with the PWM duty cycle value and configure the FMT bit to set the
          proper register alignment.
       5. Configure and start the selected timer:
           – Clear the TMRxIF Interrupt Flag bit of the PIRx register. See the Important Note below.
            – Select the timer clock source to be as FOSC/4. This is required for correct operation of the
              PWM module.
            – Configure the TxCKPS bits of the TxCON register with the desired timer prescale value.
            – Enable the timer by setting the TxON bit.
       6. Enable the PWM output:


--- p454 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                        CCP - Capture/Compare/PWM Module

             – Wait until the timer overflows and the TMRxIF bit of the PIRx register is set. See the
               Important Note below.
             – Enable the CCPx pin output driver by clearing the associated TRIS bit.


                              Important: To send a complete duty cycle and period on the first PWM
                              output, the above steps must be included in the setup sequence. If it is not
                              critical to start with a complete PWM signal on the first output, then step 6
                              may be ignored.


28.4.3 Timer2 Timer Resource
       The PWM Standard mode makes use of the 8-bit Timer2 timer resources to specify the PWM period.

28.4.4 PWM Period
       The PWM period is specified by the T2PR register of Timer2. The PWM period can be calculated
       using the formula in the equation below.

       Equation 28-1. PWM Period
       PWM Period =      T2PR + 1 • 4 • TOSC • TMR2 Prescale Value

       where TOSC = 1/FOSC
       When T2TMR is equal to T2PR, the following three events occur on the next increment event:
       •   T2TMR is cleared
       •   The CCPx pin is set (Exception: If the PWM duty cycle = 0%, the pin will not be set)
       •   The PWM duty cycle is transferred from the CCPRx register into a 10-bit buffer


                    Important: The Timer postscaler (see the “Timer2 Interrupt” section in the
                    “TMR2 - Timer2 Module” chapter) is not used in the determination of the PWM
                    frequency.


28.4.5 PWM Duty Cycle
       The PWM duty cycle is specified by writing a 10-bit value to the CCPRx register. The alignment of
       the 10-bit value is determined by the FMT bit (see Figure 28-5). The CCPRx register can be written to
       at any time. However, the duty cycle value is not latched onto the 10-bit buffer until after a match
       between T2PR and T2TMR.
       The equations below are used to calculate the PWM pulse width and the PWM duty cycle ratio.


--- p455 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                     CCP - Capture/Compare/PWM Module

       Figure 28-5. PWM 10-Bit Alignment


                                              CCP RxH                  CCP RxL
                                           7 6 5 4 3 2 1 0       7 6 5 4 3 2 1 0
                                                                                           FMT = 0


                                                             CCP RxH                   CCP RxL
                                        FMT = 1         7 6 5 4 3 2 1 0          7 6 5 4 3 2 1 0


                                                             10-bit Duty Cycle
                                                          9 8 7 6 5 4 3 2 1 0


       Equation 28-2. Pulse Width
       Pulse Widtℎ = CCPRxH: CCPRxL register value • TOSC • TMR2 Prescale Value

       Equation 28-3. Duty Cycle
                             CCPRxH: CCPRxL register value
       DutyCycleRatio =
                                     4 T2PR + 1

       The CCPRx register is used to double buffer the PWM duty cycle. This double buffering is essential
       for glitchless PWM operation.
       The 8-bit timer T2TMR register is concatenated with either the 2-bit internal system clock (FOSC),
       or two bits of the prescaler, to create the 10-bit time base. The system clock is used if the Timer2
       prescaler is set to 1:1.
       When the 10-bit time base matches the CCPRx register, then the CCPx pin is cleared (see Figure
       28-4).

28.4.6 PWM Resolution
       The resolution determines the number of available duty cycles for a given period. For example, a
       10-bit resolution will result in 1024 discrete duty cycles, whereas an 8-bit resolution will result in 256
       discrete duty cycles.
       The maximum PWM resolution is 10 bits when T2PR is 0xFF. The resolution is a function of the T2PR
       register value, as shown below.

       Equation 28-4. PWM Resolution
                        log 4 T2PR + 1
       Resolution =                    bits
                              log 2


                    Important: If the pulse-width value is greater than the period, the assigned PWM
                    pin(s) will remain unchanged.


       Table 28-2. Example PWM Frequencies and Resolutions (FOSC = 20 MHz)
                PWM Frequency               1.22 kHz         4.88 kHz        19.53 kHz           78.12 kHz    156.3 kHz     208.3 kHz
       Timer Prescale                          16               4                 1                 1             1             1
       T2PR Value                             0xFF            0xFF               0xFF              0x3F         0x1F          0x17
       Maximum Resolution (bits)               10              10                 10                8             7            6.6


--- p456 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                              CCP - Capture/Compare/PWM Module

        Table 28-3. Example PWM Frequencies and Resolutions (FOSC = 8 MHz)
                 PWM Frequency             1.22 kHz     4.90 kHz     19.61 kHz     76.92 kHz          153.85 kHz     200.0 kHz
        Timer Prescale                           16         4             1               1               1              1
        T2PR Value                           0x65         0x65           0x65         0x19              0x0C           0x09
        Maximum Resolution (bits)                8          8             8               6               5              5


28.4.7 Operation in Sleep Mode
        In Sleep mode, the T2TMR register will not increment and the state of the module will not change. If
        the CCPx pin is driving a value, it will continue to drive that value. When the device wakes up, T2TMR
        will continue from the previous state.

28.4.8 Changes in System Clock Frequency
        The PWM frequency is derived from the system clock frequency. Any changes in the system clock
        frequency will result in changes to the PWM frequency. See the “OSC - Oscillator Module (With
        Fail-Safe Clock Monitor)” chapter for additional details.

28.4.9 Effects of Reset
        Any Reset will force all ports to Input mode and the CCP registers to their Reset states.

28.5    Register Definitions: CCP Control
        Long bit name prefixes for the CCP peripherals are shown in the following table. Refer to the “Long
        Bit Names” section in the “Register and Bit Naming Conventions” chapter for more information.

        Table 28-4. CCP Long Bit Name Prefixes
                          Peripheral                                              Bit Name Prefix
                            CCP1                                                          CCP1
                            CCP2                                                          CCP2
                            CCP3                                                          CCP3


--- p457 ---
                                                                                                                       PIC18F27/47/57Q43
                                                                                                      CCP - Capture/Compare/PWM Module

28.5.1 CCPxCON

           Name:           CCPxCON
           Address:        0x342,0x346,0x34A

           CCP Control Register

     Bit        7                 6              5              4                 3               2          1                 0
               EN                               OUT            FMT                                 MODE[3:0]
  Access       R/W                               R             R/W               R/W            R/W        R/W                R/W
   Reset        0                                x              0                 0              0           0                 0

Bit 7 – EN CCP Module Enable
           Value          Description
           1              CCP is enabled
           0              CCP is disabled

Bit 5 – OUT CCP Output Data (read-only)

Bit 4 – FMT CCPxRH:L Value Alignment (PWM mode)
           Value          Condition                                      Description
           x              Capture mode                                   Not used
           x              Compare mode                                   Not used
           1              PWM mode                                       Left aligned format
           0              PWM mode                                       Right aligned format

Bits 3:0 – MODE[3:0] CCP Mode Select

           Table 28-5. CCPx Mode Select
               MODE Value              Operating Mode        Operation                                                    Set CCPxIF
                   11xx                      PWM             PWM operation                                                   Yes
                   1011                                      Pulse output; clear TMR1(2)                                     Yes
                   1010                                      Pulse output                                                    Yes
                                            Compare
                   1001                                      Clear output(1)                                                 Yes
                   1000                                      Set output(1)                                                   Yes
                   0111                                      Every 16th rising edge of CCPx input                            Yes
                   0110                                      Every 4th rising edge of CCPx input                             Yes
                   0101                     Capture          Every rising edge of CCPx input                                 Yes
                   0100                                      Every falling edge of CCPx input                                Yes
                   0011                                      Every edge of CCPx input                                        Yes
                   0010                                      Toggle output                                                   Yes
                                            Compare
                   0001                                      Toggle output; clear TMR1(2)                                    Yes
                   0000                     Disabled                                                                          —

           Notes:
           1. The set and clear operations of the Compare mode are reset by setting MODE = ‘b0000 or EN =
              0.
           2. When MODE = ‘b0001 or ‘b1011, then the timer associated with the CCP module is cleared.
              TMR1 is the default selection for the CCP module, so it is used for indication purposes only.


--- p458 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                  CCP - Capture/Compare/PWM Module

28.5.2 CCPxCAP

            Name:        CCPxCAP
            Address:     0x343,0x347,0x34B
            Capture Trigger Input Selection Register

      Bit         7             6             5              4                   3            2                1           0
                                                                                                   CTS[3:0]
  Access                                                                        R/W        R/W                R/W         R/W
   Reset                                                                         0          0                  0           0

Bits 3:0 – CTS[3:0] Capture Trigger Input Selection

            Table 28-6. Capture Trigger Sources
                         CTS Value                                                       Source
                        1111-1100                                                       Reserved
                           1011                                                        CLC8_OUT
                           1010                                                        CLC7_OUT
                           1001                                                        CLC6_OUT
                           1000                                                        CLC5_OUT
                           0111                                                        CLC4_OUT
                           0110                                                        CLC3_OUT
                           0101                                                        CLC2_OUT
                           0100                                                        CLC1_OUT
                           0011                                                       IOC Interrupt
                           0010                                                        CMP2_OUT
                           0001                                                        CMP1_OUT
                           0000                                                 Pin selected by CCPxPPS


--- p459 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                              CCP - Capture/Compare/PWM Module

28.5.3 CCPRx

           Name:       CCPRx
           Address:    0x340,0x344,0x348

           Capture/Compare/Pulse-Width Register

     Bit        15           14          13             12           11               10                 9             8
                                                          CCPR[15:8]
  Access        R/W         R/W          R/W           R/W         R/W               R/W                R/W           R/W
   Reset         x           x            x             x             x               x                  x             x

     Bit         7           6            5              4                   3            2              1             0
                                                              CCPR[7:0]
  Access        R/W         R/W          R/W           R/W                  R/W      R/W                R/W           R/W
   Reset         x           x            x             x                    x        x                  x             x

Bits 15:0 – CCPR[15:0] Capture/Compare/Pulse-Width
         Reset States: POR/BOR = xxxxxxxxxxxxxxxx
                       All other Resets = uuuuuuuuuuuuuuuu

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • When MODE = Capture or Compare
              – CCPRxH: Accesses the high byte CCPR[15:8]
                – CCPRxL: Accesses the low byte CCPR[7:0]
           •   When MODE = PWM and FMT = 0
                – CCPRx[15:10]: Not used
                – CCPRxH[1:0]: Accesses the two Most Significant bits CCPR[9:8]
                – CCPRxL: Accesses the eight Least Significant bits CCPR[7:0]
           •   When MODE = PWM and FMT = 1
                – CCPRxH: Accesses the eight Most Significant bits CCPR[9:2]
                – CCPRxL[7:6]: Accesses the two Least Significant bits CCPR[1:0]
                – CCPRx[5:0]: Not used


--- p460 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                        CCP - Capture/Compare/PWM Module

28.6      Register Summary - CCP Control
Address     Name     Bit Pos.   7         6           5              4              3        2               1          0
                      7:0                                               CCPR[7:0]
 0x0340     CCPR1
                      15:8                                             CCPR[15:8]
 0x0342    CCP1CON    7:0       EN                   OUT            FMT                          MODE[3:0]
 0x0343    CCP1CAP    7:0                                                                         CTS[3:0]
                      7:0                                               CCPR[7:0]
 0x0344     CCPR2
                      15:8                                             CCPR[15:8]
 0x0346    CCP2CON    7:0       EN                   OUT            FMT                          MODE[3:0]
 0x0347    CCP2CAP    7:0                                                                         CTS[3:0]
                      7:0                                               CCPR[7:0]
 0x0348     CCPR3
                      15:8                                             CCPR[15:8]
 0x034A    CCP3CON    7:0       EN                   OUT            FMT                          MODE[3:0]
 0x034B    CCP3CAP    7:0                                                                         CTS[3:0]


--- p461 ---
