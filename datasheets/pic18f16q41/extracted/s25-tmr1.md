25.   TMR1 - Timer1 Module with Gate Control
      The Timer1 module is a 16-bit timer/counter with the following features:
      •   16-bit timer/counter register pair (TMRxH:TMRxL)
      •   Programmable internal or external clock source
      •   2-bit prescaler
      •   Clock source for optional comparator synchronization
      •   Multiple Timer1 gate (count enable) sources
      •   Interrupt-on-overflow
      •   Wake-up on overflow (external clock, Asynchronous mode only)
      •   16-bit read/write operation
      •   Time base for the capture/compare function with the CCP modules
      •   Special event trigger (with CCP)
      •   Selectable gate source polarity
      •   Gate Toggle mode
      •   Gate Single Pulse mode
      •   Gate value status
      •   Gate event interrupt


                   Important: References to the module Timer1 apply to all the odd numbered timers on
                   this device.


--- p365 ---
       Figure 25-1. Timer1 Block Diagram

                  TxGATE
                                          4
              TxGPPS
                                                                                                             GSPM
                PPS               00 00


                                                                                                                             1
                                                                                            0     Single Pulse                               D      Q     GVAL
                  NOTE (5)                                                                                                   0
                                  11 11
                                                                                            1     Acq. Control
                                                                                                                                       Q1
                                                                 D         Q

                       GPOL                                                                       GGO/DONE
                                                                 CK        Q
                          ON                                                                                                                Interrupt
                                                                                                                                                            set bit
                                                                 R
                       GTM                                                                                                                       det       TMRxGIF


                                                                                                                                 GE
                   set flag bit
                    TMRxIF
                                                                                                            ON
                                                                      EN
                                                 (2)                                                                                         To Comparators (6)
                                              TMRx
            Tx_overflow                                                                                                   Synchronized Clock Input
                               TMRxH             TMRxL           Q     D                                0
                                                                                                        1
               TxCLK
                                                                                        SYNC

                                                                                      TxCLK
                                                                                                    4
                                                                  TxCKIPPS
                                                                                       (1)
                                                                      PPS                       0000

                                                                                                                 Prescaler
                                                                                                                                                 Synchronize(3)
                                                                                                                  1,2,4,8
                                                                                      (4)
                                                                               Note                                                                       det
                                                                                                111 1
                                                                                                                      2
                                                                                                                                       Fosc/2
                                                                                                                  CKPS                Internal           Sleep
                                                                                                                                       Clock             Input


       Notes:
       1. This signal comes from the pin selected by Timer1 PPS register.
       2. TMRx register increments on rising edge.
       3. Synchronize does not operate while in Sleep.
       4. See TxCLK for clock source selections.
       5. See TxGATE for gate source selections.
       6. Synchronized comparator output must not be used in conjunction with synchronized input clock.

25.1   Timer1 Operation
       The Timer1 module is a 16-bit incrementing counter accessed through the TMRx register. Writes to
       TMRx directly update the counter. When used with an internal clock source, the module is a timer
       that increments on every instruction cycle. When used with an external clock source, the module can
       be used as either a timer or counter and increments on every selected edge of the external source.
       Timer1 is enabled by configuring the ON and GE bits. Table 25-1 shows the possible Timer1 enable
       selections.


--- p366 ---
        Table 25-1. Timer1 Enable Selections
               ON                GE                                        Timer1 Operation
                1                 1                                          Count enabled
                1                 0                                            Always on
                0                 1                                               Off
                0                 0                                               Off


25.2    Clock Source Selection
        The CS bits select the clock source for Timer1. These bits allow the selection of several possible
        synchronous and asynchronous clock sources.

25.2.1 Internal Clock Source
        When the internal clock source is selected, the TMRx register will increment on multiples of FOSC as
        determined by the Timer1 prescaler.
        When the FOSC internal clock source is selected, the TMRx register value will increment by four
        counts every instruction clock cycle. Due to this condition, a two LSB error in resolution will occur
        when reading the TMRx value. To utilize the full resolution of Timer1, an asynchronous input signal
        must be used to gate the Timer1 clock input.


                     Important: In Counter mode, a falling edge must be registered by the counter prior to the
                     first incrementing rising edge after any one or more of the following conditions:
                     • Timer1 enabled after POR
                     •   Write to TMRxH or TMRxL
                     •   Timer1 is disabled
                     •   Timer1 is disabled (ON = 0) when TxCKI is high, then Timer1 is enabled (ON = 1) when
                         TxCKI is low. Refer to the figure below.


        Figure 25-2. Timer1 Incrementing Edge

              TxCKI = 1
              When TMRx
              Enabled


              TxCKI = 0
              When TMRx
              Enabled


        Notes:
        1. Arrows indicate counter increments.
        2. In Counter mode, a falling edge must be registered by the counter prior to the first incrementing
           rising edge of the clock.

25.2.2 External Clock Source
        When the external clock source is selected, the TMRx module may work as a timer or a counter.
        When enabled to count, Timer1 is incremented on the rising edge of the external clock input of
        the TxCKIPPS pin. This external clock source can be synchronized to the system clock or it can run
        asynchronously.


--- p367 ---
25.3   Timer1 Prescaler
       Timer1 has four prescaler options allowing 1, 2, 4 or 8 divisions of the clock input. The CKPS bits
       control the prescale counter. The prescale counter is not directly readable or writable; however, the
       prescaler counter is cleared upon a write to TMRx.

25.4   Secondary Oscillator
       A secondary low-power 32.768 kHz oscillator circuit is built-in between pins SOSCI (input) and SOSCO
       (amplifier output). This internal circuit is to be used in conjunction with an external 32.768 kHz
       crystal. The secondary oscillator is not dedicated only to Timer1; it can also be used by other
       modules.
       The oscillator circuit is enabled by setting the SOSCEN bit of the OSCEN register. This can be used as
       one of the Timer1 clock sources selected with the CS bits. The oscillator will continue to run during
       Sleep.


                   Important: The oscillator requires a start-up and stabilization time before use. Thus, the
                   SOSCEN bit of the OSCEN register must be set and a suitable delay observed prior to
                   enabling Timer1. A software check can be performed to confirm if the secondary oscillator
                   is enabled and ready to use. This is done by polling the secondary oscillator ready Status
                   bit. Refer to the “OSC - Oscillator Module (with Fail-Safe Clock Monitor)” chapter for
                   more details.


25.5   Timer1 Operation in Asynchronous Counter Mode
       When the SYNC Control bit is set, the external clock input is not synchronized. The timer increments
       asynchronously to the internal phase clocks. If the external clock source is selected, then the timer
       will continue to run during Sleep and can generate an interrupt on overflow, which will wake up the
       processor. However, special precautions in software are needed to read/write the timer.


                   Important: When switching from synchronous to asynchronous operation, it is possible
                   to skip an increment. When switching from asynchronous to synchronous operation, it is
                   possible to produce an additional increment.


25.5.1 Reading and Writing TMRx in Asynchronous Counter Mode
       Reading TMRxH or TMRxL while the timer is running from an external asynchronous clock will
       ensure a valid read (taken care of in hardware). However, the user must keep in mind that reading
       the 16-bit timer in two 8-bit values itself poses certain problems, since there may be a carry-out of
       TMRxL to TMRxH between the reads.
       For writes, it is recommended that the user simply stop the timer and write the desired values. A
       write contention may occur by writing to the timer registers, while the register is incrementing. This
       may produce an unpredictable value in the TMRxH:TMRxL register pair.

25.6   Timer1 16-Bit Read/Write Mode
       Timer1 can be configured to read and write all 16 bits of data to and from the 8-bit TMRxL and
       TMRxH registers, simultaneously. The 16-bit read and write operations are enabled by setting the
       RD16 bit. To accomplish this function, the TMRxH register value is mapped to a buffer register called
       the TMRxH buffer register. While in 16-bit mode, the TMRxH register is not directly readable or
       writable and all read and write operations take place through the use of this TMRxH buffer register.
       When a read from the TMRxL register is requested, the value of the TMRxH register is
       simultaneously loaded into the TMRxH buffer register. When a read from the TMRxH register is
       requested, the value is provided from the TMRxH buffer register instead. This provides the user with


--- p368 ---
       the ability to accurately read all 16 bits of the Timer1 value from a single instance in time (refer
       to Figure 25-3 for more details). In contrast, when not in 16-bit mode, the user must read each
       register separately and determine if the values have become invalid due to a rollover that may have
       occurred between the read operations.
       When a write request of the TMRxL register is requested, the TMRxH buffer register is
       simultaneously updated with the contents of the TMRxH register. The value of TMRxH must be
       preloaded into the TMRxH buffer register prior to the write request for the TMRxL register. This
       provides the user with the ability to write all 16 bits to the TMRx register at the same time. Any
       requests to write to TMRxH directly does not clear the Timer1 prescaler value. The prescaler value is
       only cleared through write requests to the TMRxL register.

       Figure 25-3. Timer1 16-Bit Read/Write Mode Block Diagram

                                                                               From
                                                                               TMRx
                                                                               Circuitr y

                                                              TMRx                 Set TMRxIF
                                                TMRxL
                                                             High Byte             on Overflow
                                                                        8

                                                                              Read TMRxL
                                                                              Write TMRxL
                                                               8
                                                   8
                                                              TMRxH


                                                                    8
                                                        8
                                                                            Inte rnal Da ta Bus


25.7   Timer1 Gate
       Timer1 can be configured to count freely or the count can be enabled and disabled using Timer1
       gate circuitry. This is also referred to as Timer1 gate enable. Timer1 gate can also be driven by
       multiple selectable sources.

25.7.1 Timer1 Gate Enable
       The Timer1 Gate Enable mode is enabled by setting the GE bit. The polarity of the Timer1 Gate
       Enable mode is configured using the GPOL bit.
       When Timer1 Gate Enable mode is enabled, Timer1 will increment on the rising edge of the Timer1
       clock source. When Timer1 Gate signal is inactive, the timer will not increment and hold the current
       count. Enable mode is disabled, no incrementing will occur and Timer1 will hold the current count.
       See Figure 25-4 for timing details.

       Table 25-2. Timer1 Gate Enable Selections
                 TMRxCLK                  GPOL                TxG                                   Timer1 Operation
                    ↑                       1                   1                                        Counts
                    ↑                       1                   0                                      Holds Count
                    ↑                       0                   1                                      Holds Count
                    ↑                       0                   0                                        Counts


--- p369 ---
       Figure 25-4. Timer1 Gate Enable Mode

                TMRxGE


                TxGPOL


                 TxG_IN


                 TxCKI


                 TxGVAL


                 Timer1


25.7.2 Timer1 Gate Source Selection
       The gate source for Timer1 is selected using the GSS bits. The polarity selection for the gate source is
       controlled by the GPOL bit.
       Any of the above mentioned signals can be used to trigger the gate. The output of the CMPx
       can be synchronized to the Timer1 clock or left asynchronous. For more information refer to the
       “Comparator Output Synchronization” section.

25.7.3 Timer1 Gate Toggle Mode
       When Timer1 Gate Toggle mode is enabled, it is possible to measure the full-cycle length of a Timer1
       Gate signal, as opposed to the duration of a single-level pulse. The Timer1 gate source is routed
       through a flip-flop that changes state on every incrementing edge of the signal. See the figure below
       for timing details.
       Timer1 Gate Toggle mode is enabled by setting the GTM bit. When the GTM bit is cleared, the
       flip-flop is cleared and held clear. This is necessary to control which edge is measured.


                   Important: Enabling Toggle mode at the same time as changing the gate polarity may
                   result in indeterminate operation.


--- p370 ---
       Figure 25-5. Timer1 Gate Toggle Mode

           TMRxGE

           TxGPOL


            TxGTM


          TxTxG_IN


             TxCKI


            TxGVAL


            Timer1


25.7.4 Timer1 Gate Single Pulse Mode
       When Timer1 Gate Single Pulse mode is enabled, it is possible to capture a single pulse gate event.
       Timer1 Gate Single Pulse mode is first enabled by setting the GSPM bit. Next, the GGO/DONE must
       be set. The Timer1 will be fully enabled on the next incrementing edge. On the next trailing edge of
       the pulse, the GGO/DONE bit will automatically be cleared. No other gate events will be allowed to
       increment Timer1 until the GGO/DONE bit is once again set in software.

       Figure 25-6. Timer1 Gate Single Pulse Mode

            TMRxGE

             TxGPOL


             TxGSPM
                                                                             Cleared by hardware on
            TxGGO/                    Set by software                        falling edge of TxGVAL
             DONE
                                    Counting enabled on
                                     rising edge of TxG
               TxG_IN


               TxCKI


              TxGVAL


              TIMER1

                                                                                                         Cleared by
             TMRxGIF          Cleared by software                             Set by hardware on          software
                                                                            falling edge of TxGVAL


--- p371 ---
       Clearing the GSPM bit will also clear the GGO/DONE bit. See the figure below for timing details.
       Enabling the Toggle mode and the Single Pulse mode simultaneously will permit both sections to
       work together. This allows the cycle times on the Timer1 gate source to be measured. See the figure
       below for timing details.

       Figure 25-7. Timer1 Gate Single Pulse and Toggle Combined Mode

             TMRxGE

             TxGPOL


             TxGSPM

               TxGTM
                                                                                              Cleared by hardware on
             TxGGO/                  Set by software                                          falling edge of TxGVAL
              DONE
                                   Counting enabled on
                                    rising edge of TxG
               TxG_IN


                TxCKI


             TxGVAL


             TIMER1

                                                                  Set by hardware on                    Cleared by
             TMRxGIF         Cleared by software                falling edge of TxGVAL                   software


25.7.5 Timer1 Gate Value Status
       When Timer1 gate value status is utilized, it is possible to read the most current level of the gate
       control value. The value is stored in the GVAL bit in the TxGCON register. The GVAL bit is valid even
       when the Timer1 gate is not enabled (GE bit is cleared).

25.7.6 Timer1 Gate Event Interrupt
       When Timer1 gate event interrupt is enabled, it is possible to generate an interrupt upon the
       completion of a gate event. When the falling edge of GVAL occurs, the TMRxGIF flag bit in one of the
       PIR registers will be set. If the TMRxGIE bit in the corresponding PIE register is set, then an interrupt
       will be recognized.
       The TMRxGIF flag bit operates even when the Timer1 gate is not enabled (the GE bit is cleared). For
       more information on selecting high- or low-priority status for the Timer1 gate event interrupt, see
       the “VIC - Vectored Interrupt Controller Module” chapter.

25.8   Timer1 Interrupt
       The TMRx register increments to FFFFh and rolls over to 0000h. When TMRx rolls over, the Timer1
       interrupt flag bit of the PIRx register is set. To enable the interrupt-on-rollover, the following bits
       must be set:
       •   The ON bit of the TxCON register


--- p372 ---
       •   The TMRxIE bits of the PIEx register
       •   Global interrupts must be enabled
       The interrupt is cleared by clearing the TMRxIF bit as a task in the Interrupt Service Routine. For
       more information on selecting high- or low-priority status for the Timer1 overflow interrupt, see the
       “VIC - Vectored Interrupt Controller Module” chapter.


                    Important: The TMRx register and the TMRxIF bit must be cleared before enabling
                    interrupts.


25.9   Timer1 Operation During Sleep
       Timer1 can only operate during Sleep when configured as an asynchronous counter. In this mode,
       many clock sources can be used to increment the counter. To set up the timer to wake the device:
       •   The ON bit must be set
       •   The TMRxIE bit of the PIEx register must be set
       •   Global interrupts must be enabled
       •   The SYNC bit must be set
       •   Configure the TxCLK register for using any clock source other than FOSC and FOSC/4
       The device will wake up on an overflow and execute the next instruction. If global interrupts are
       enabled, the device will call the IRS. The secondary oscillator will continue to operate in Sleep
       regardless of the SYNC bit setting.

25.10 CCP Capture/Compare Time Base
       The CCP modules use TMRx as the time base when operating in Capture or Compare mode. In
       Capture mode, the value in TMRx is copied into the CCPRx register on a capture event. In Compare
       mode, an event is triggered when the value in the CCPRx register matches the value in TMRx. This
       event can be a Special Event Trigger.

25.11 CCP Special Event Trigger
       When any of the CCPs are configured to trigger a special event, the trigger will clear the TMRx
       register. This special event does not cause a Timer1 interrupt. The CCP module may still be
       configured to generate a CCP interrupt. In this mode of operation, the CCPRx register becomes the
       period register for Timer1. Timer1 must be synchronized and FOSC/4 must be selected as the clock
       source to utilize the Special Event Trigger. Asynchronous operation of Timer1 can cause a Special
       Event Trigger to be missed. In the event that a write to TMRxH or TMRxL coincides with a Special
       Event Trigger from the CCP, the write will take precedence.

25.12 Peripheral Module Disable
       When a peripheral is not used or inactive, the module can be disabled by setting the Module Disable
       bit in the PMD registers. This will reduce power consumption to an absolute minimum. Setting the
       PMD bits holds the module in Reset and disconnects the module’s clock source. The Module Disable
       bits for Timer1 (TMR1MD) are in the PMDx register. See the “PMD - Peripheral Module Disable”
       chapter for more information.

25.13 Register Definitions: Timer1 Control
       Long bit name prefixes for the Timer registers are shown in the table below, where ‘x’ refers to the
       Timer instance number. Refer to the “Long Bit Names” section in the “Register and Bit Naming
       Conventions” chapter for more information.


--- p373 ---
Table 25-3. Timer1 Register Long Bit Name Prefixes
                  Peripheral                                              Bit Name Prefix
                    Timer1                                                        T1
                    Timer3                                                        T3


--- p374 ---
25.13.1 TxCON

            Name:        TxCON
            Address:     0x314,0x325

            Timer Control Register

      Bit           7            6                 5                 4                  3          2              1            0
                                                        CKPS[1:0]                                SYNC            RD16         ON
  Access                                          R/W               R/W                           R/W            R/W          R/W
   Reset                                           0                 0                             0              0            0

Bits 5:4 – CKPS[1:0] Timer Input Clock Prescaler Select
          Reset States: POR/BOR = 00
                        All Other Resets = uu
            Value       Description
            11          1:8 Prescaler value
            10          1:4 Prescaler value
            01          1:2 Prescaler value
            00          1:1 Prescaler value

Bit 2 – SYNC Timer External Clock Input Synchronization Control
          Reset States: POR/BOR = 0
                        All Other Resets = u
            Value       Condition                           Description
            x           CS = FOSC/4 or FOSC                 This bit is ignored. Timer uses the incoming clock as is.
            1           All other clock sources             Do not synchronize external clock input
            0           All other clock sources             Synchronize external clock input with system clock

Bit 1 – RD16 16-Bit Read/Write Mode Enable
         Reset States: POR/BOR = 0
                       All Other Resets = u
            Value       Description
            1           Enables register read/write of Timer in one 16-bit operation
            0           Enables register read/write of Timer in two 8-bit operations

Bit 0 – ON Timer On
         Reset States: POR/BOR = 0
                       All Other Resets = u
            Value       Description
            1           Enables Timer
            0           Disables Timer


--- p375 ---
25.13.2 TxGCON

            Name:       TxGCON
            Address:    0x315,0x326

            Timer Gate Control Register

      Bit        7            6               5                  4           3               2                1             0
                 GE          GPOL            GTM               GSPM      GGO/DONE           GVAL
  Access        R/W          R/W             R/W                R/W        R/W               R
   Reset         0            0               0                  0           0               x

Bit 7 – GE Timer Gate Enable
         Reset States: POR/BOR = 0
                       All Other Resets = u
            Value      Condition        Description
            1          ON = 1           Timer counting is controlled by the Timer gate function
            0          ON = 1            Timer is always counting
            X          ON = 0            This bit is ignored


Bit 6 – GPOL Timer Gate Polarity
         Reset States: POR/BOR = 0
                       All Other Resets = u
            Value      Description
            1          Timer gate is active-high (Timer counts when gate is high)
            0          Timer gate is active-low (Timer counts when gate is low)

Bit 5 – GTM Timer Gate Toggle Mode
         Timer Gate flip-flop toggles on every rising edge when Toggle mode is enabled.
         Reset States: POR/BOR = 0
                       All Other Resets = u
            Value      Description
            1          Timer Gate Toggle mode is enabled
            0          Timer Gate Toggle mode is disabled and Toggle flip-flop is cleared

Bit 4 – GSPM Timer Gate Single Pulse Mode
         Reset States: POR/BOR = 0
                       All Other Resets = u
            Value      Description
            1          Timer Gate Single Pulse mode is enabled and is controlling Timer gate
            0          Timer Gate Single Pulse mode is disabled

Bit 3 – GGO/DONE Timer Gate Single Pulse Acquisition Status
         This bit is automatically cleared when TxGSPM is cleared.
         Reset States: POR/BOR = 0
                        All Other Resets = u
            Value      Description
            1          Timer Gate Single Pulse Acquisition is ready, waiting for an edge
            0          Timer Gate Single Pulse Acquisition has completed or has not been started

Bit 2 – GVAL Timer Gate Current State
         Indicates the current state of the timer gate that can be provided to TMRxH:TMRxL
         Unaffected by the Timer Gate Enable (GE) bit


--- p376 ---
25.13.3 TxCLK

            Name:      TxCLK
            Address:   0x317,0x328

            Timer Clock Source Selection Register

      Bit        7            6           5              4                   3           2                 1             0
                                                                                       CS[4:0]
  Access                                               R/W                  R/W         R/W              R/W           R/W
   Reset                                                0                    0           0                0             0

Bits 4:0 – CS[4:0] Timer Clock Source Selection

   Table 25-4. Timer Clock Sources
                  CS                                                         Clock Source
                                                     Timer1                                              Timer3
            11111 - 10001                                                        Reserved
                10000                                                            CLC4_OUT
                01111                                                            CLC3_OUT
                01110                                                            CLC2_OUT
                01101                                                            CLC1_OUT
                01100                            TMR3_OUT                                               Reserved
                01011                             Reserved                                             TMR1_OUT
                01010                                                       TMR0_OUT
                01001                                                      CLKREF_OUT
                01000                                                         EXTOSC
                00111                                                          SOSC
                00110                                                   MFINTOSC (32 kHz)
                00101                                                   MFINTOSC (500 kHz)
                00100                                                        LFINTOSC
                00011                                                       HFINTOSC
                00010                                                           FOSC
                00001                                                          FOSC/4
                00000                     Pin selected by T1CKIPPS                              Pin selected by T3CKIPPS

            Reset States: POR/BOR = 00000
                          All Other Resets = uuuuu


--- p377 ---
25.13.4 TxGATE

            Name:       TxGATE
            Address:    0x316,0x327

            Timer Gate Source Selection Register

      Bit        7           6            5              4                   3             2               1             0
                                                                                        GSS[4:0]
  Access                                               R/W                  R/W          R/W              R/W          R/W
   Reset                                                0                    0             0               0            0

Bits 4:0 – GSS[4:0] Timer Gate Source Selection

   Table 25-5. Timer Gate Sources
                  GSS                                                            Gate Source
                                                     Timer1                                               Timer3
            11111 - 10110                                                   Reserved
                10101                                                      CLC4_OUT
                10100                                                      CLC3_OUT
                10011                                                      CLC2_OUT
                10010                                                      CLC1_OUT
                10001                                                       ZCD_OUT
                10000                                                      CMP2_OUT
                01111                                                      CMP1_OUT
                01110                                                      NCO1_OUT
                01101                                                    PWM3S1P2_OUT
                01100                                                    PWM3S1P1_OUT
                01011                                                    PWM2S1P2_OUT
                01010                                                    PWM2S1P1_OUT
                01001                                                    PWM1S1P2_OUT
                01000                                                    PWM1S1P1_OUT
                00111                                                      CCP1_OUT
                00110                                                      SMT1_OUT
                00101                                                  TMR4_Postscaler_OUT
                00100                              TMR3_OUT                                              Reserved
                00011                                                  TMR2_Postscaler_OUT
                00010                               Reserved                                            TMR1_OUT
                00001                                                             TMR0_OUT
                00000                         Pin selected by T1GPPS                               Pin selected by T3GPPS


--- p378 ---
25.13.5 TMRx

           Name:       TMRx
           Address:    0x312,0x323

           Timer Register

     Bit         15          14          13             12           11               10             9             8
                                                          TMRx[15:8]
  Access        R/W         R/W          R/W           R/W         R/W               R/W           R/W           R/W
   Reset         0           0            0             0             0               0             0             0

     Bit         7           6            5              4          3                     2          1             0
                                                          TMRx[7:0]
  Access        R/W         R/W          R/W           R/W         R/W               R/W           R/W           R/W
   Reset         0           0            0             0           0                 0             0             0

Bits 15:0 – TMRx[15:0] Timer Register Value
         Reset States: POR/BOR = 0000000000000000
                       All Other Resets = uuuuuuuuuuuuuuuu

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names:
           • TMRxH: Accesses the high byte TMRx[15:8]
           •   TMRxL: Accesses the low byte TMRx[7:0]


--- p379 ---
25.14 Register Summary - Timer1
Address    Name      Bit Pos.   7         6           5             4                3           2          1           0
  0x00
   ...    Reserved
 0x0311
                      7:0                                                TMR1[7:0]
 0x0312    TMR1
                      15:8                                              TMR1[15:8]
 0x0314    T1CON      7:0                               CKPS[1:0]                              SYNC       RD16         ON
 0x0315   T1GCON      7:0       GE      GPOL         GTM        GSPM          GGO/DONE         GVAL
 0x0316   T1GATE      7:0                                                                     GSS[4:0]
 0x0317    T1CLK      7:0                                                                     CS[4:0]
 0x0318
   ...    Reserved
 0x0322
                      7:0                                                TMR3[7:0]
 0x0323    TMR3
                      15:8                                              TMR3[15:8]
 0x0325    T3CON      7:0                               CKPS[1:0]                              SYNC       RD16         ON
 0x0326   T3GCON      7:0       GE      GPOL         GTM        GSPM          GGO/DONE         GVAL
 0x0327   T3GATE      7:0                                                                     GSS[4:0]
 0x0328    T3CLK      7:0                                                                     CS[4:0]


--- p380 ---
