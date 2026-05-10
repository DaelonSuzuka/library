                                                                                                    PIC18F27/47/57Q43
                                                                                CWG - Complementary Waveform Generator
                                                                                                               Module

31.    CWG - Complementary Waveform Generator Module
       The Complementary Waveform Generator (CWG) produces half-bridge, full-bridge, and steering of
       PWM waveforms. It is backward compatible with previous CCP functions.
       The CWG has the following features:
       •   Six Operating modes:
             – Synchronous Steering mode
            – Asynchronous Steering mode
            – Full Bridge mode, Forward
            – Full Bridge mode, Reverse
            – Half Bridge mode
            – Push-Pull mode
       •   Output Polarity Control
       •   Output Steering
       •   Independent 6-bit Rising and Falling Event Dead-Band Timers:
             – Clocked dead band
            – Independent rising and falling dead-band enables
       •   Auto-Shutdown Control with:
            – Selectable shutdown sources
            – Auto-restart option
            – Auto-shutdown pin override control

31.1   Fundamental Operation
       The CWG generates two output waveforms from the selected input source.
       The off-to-on transition of each output can be delayed from the on-to-off transition of the other
       output, thereby creating a time delay immediately where neither output is driven. This is referred to
       as dead time and is covered in the Dead-Band Control section.
       It may be necessary to guard against the possibility of circuit faults or a feedback event arriving too
       late or not at all. In this case, the active drive must be terminated before the Fault condition causes
       damage. This is referred to as auto-shutdown and is covered in the Auto-Shutdown section.

31.2   Operating Modes
       The CWG module can operate in six different modes, as specified by the MODE bits:
       •   Half Bridge mode
       •   Push-Pull mode
       •   Asynchronous Steering mode
       •   Synchronous Steering mode
       •   Full Bridge mode, Forward
       •   Full Bridge mode, Reverse
       All modes accept a single pulse input and provide up to four outputs as described in the following
       sections.
       All modes include auto-shutdown control as described in the Auto-Shutdown section.


--- p492 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                              CWG - Complementary Waveform Generator
                                                                                                                             Module
                    Important: Except as noted for Full Bridge mode, mode changes must only be
                    performed while EN = 0.


31.2.1 Half Bridge Mode
       In Half Bridge mode, two output signals are generated as true and inverted versions of the input
       as illustrated in Figure 31-1. A nonoverlap (dead band) time is inserted between the two outputs to
       prevent shoot-through current in various power supply applications. Dead-band control is described
       in the Dead-Band Control section. The output steering feature cannot be used in this mode. A basic
       block diagram of this mode is shown in Figure 31-2.
       The unused outputs CWGxC and CWGxD drive similar signals as CWGxA and CWGxB, with polarity
       independently controlled by the POLC and POLD bits, respectively.

       Figure 31-1. CWG Half Bridge Mode Operation
                                                                                                                                         Rev. 30-000097A
                                                                                                                                                4/14/2017


       CWGx_clock


          CWGxA
          CWGxC
                                                                     Rising event dead band                                Rising event dead band
                                         Falling event dead band                                 Falling event dead band

          CWGxB
          CWGxD


        CWGx_data


--- p493 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                         CWG - Complementary Waveform Generator
                                                                                                                        Module
Figure 31-2. Simplified CWG Block Diagram (Half Bridge Mode, MODE = ‘b100)

                                                                                               LSAC                Re v. 10 -00 02 09 D
                                                                                                                            1/29 /20 19


                                                                                                 1
                                                                                                       11
                                                                                                 0
                                                                                                       10
                                                                                          High-Z
                                                                                                       01

                     Rising Dead-Band Block                                                            00
     CWG Clock             clock                                                                               1
                                                      CWG Data A
                                        data out
     CWG Data             data in                                                                              0          CWGxA
                                                                              POLA


                                                                                                LSBD


                     Falling Dead-Band Block                                                     1     11
                          clock                       CWG Data B                                 0     10
                                        data out
                          data in                                                         High-Z       01
                                                                                                       00

      CWG Data Input                                      CWG                                                  1
                                                          Data
                                                                                                               0        CWGxB
                                                                              POLB
                                    D    Q

                                    E                                                           LSAC


          EN                                                                                     1     11
                                                                                                 0     10
                                                                                             High-Z    01
                                                                                                       00

                                                                                                               1
                                                                                                               0 CWGxC
                                                                              POLC

        Auto-shutdown source                          S   Q
         (CWGxAS1 register)                                                                     LSBD
                                                      R


                    REN                                                                          1     11
           SHUTDO WN = 0                                                                         0     10
                                                                                             High-Z    01
                                                                                                       00

                                                                                                               1
                                                                                                               0 CWG1D
                                                                              POLD

                                                   SHUTDO WN

                                                       FREEZE
                                                                                     D   Q

                                                                     CWG Data


--- p494 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                CWG - Complementary Waveform Generator
                                                                                                               Module
31.2.2 Push-Pull Mode
       In Push-Pull mode, two output signals are generated, alternating copies of the input as illustrated
       in Figure 31-3. This alternation creates the Push-Pull effect required for driving some transformer-
       based power supply designs. Steering modes are not used in Push-Pull mode. A basic block diagram
       for the Push-Pull mode is shown in Figure 31-4.
       The Push-Pull sequencer is reset whenever EN = 0 or if an auto-shutdown event occurs. The
       sequencer is clocked by the first input pulse, and the first output appears on CWGxA.
       The unused outputs CWGxC and CWGxD drive copies of CWGxA and CWGxB, respectively, but with
       polarity controlled by the POLC and POLD bits.

       Figure 31-3. CWG Push-Pull Mode Operation
                                                                                                            Rev. 30-000098A
                                                                                                                   4/14/2017


              CWGx clock


           CWG Data Input


                 CWGxA


                 CWGxB


--- p495 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                     CWG - Complementary Waveform Generator
                                                                                                                    Module
Figure 31-4. Simplified CWG Block Diagram (Push-Pull Mode, MODE = ‘b101)

                                                                                         LSAC                  Re v. 10 -00 02 10 D
                                                                                                                        1/29 /20 19


                                                                                          1     11
                                                                                          0     10
                                                                                      High-Z    01
                                                                                                00

                                                                                                           1
       CWG Data                                      CWG Data A
                                                                                                           0 CWGxA
                                                                          POLA


                                                                                         LSBD
                                 D   Q

                                     Q
                                                                                          1     11
                                                                                          0     10
                                                                                      High-Z    01

                                                    CWG Data B                                  00

                                                                                                           1
     CWG Data Input                                  CWG                                                   0 CWGxB
                                                                          POLB
                                                     Data
                                 D   Q
                                                                                         LSAC
                                 E

                                                                                          1     11
          EN                                                                              0     10
                                                                                      High-Z    01
                                                                                                00

                                                                                                           1
                                                                                                           0 CWGxC
                                                                          POLC
          Auto-shutdown source                       S   Q
           (CWGxAS1 register)
                                                     R                                   LSBD


                      REN
                                                                                          1     11
               SHUTDO WN = 0
                                                                                          0     10
                                                                                      High-Z    01
                                                                                                00

                                                                                                           1
                                                                                                           0 CWGxD
                                                                          POLD


                                                 SHUTDO WN
                                                    FREEZE
                                                                                 D   Q

                                                                  CWG Data


--- p496 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                    CWG - Complementary Waveform Generator
                                                                                                                   Module
31.2.3 Full Bridge Mode
       In Forward and Reverse Full Bridge modes, three outputs drive static values while the fourth is
       modulated by the input data signal. The mode selection may be toggled between forward and
       reverse by toggling the MODE[0] bit of the CWGxCON0 register while keeping the MODE[2:1] bits
       static, without disabling the CWG module. When connected, as shown in Figure 31-5, the outputs are
       appropriate for a full-bridge motor driver. Each CWG output signal has independent polarity control,
       so the circuit can be adapted to high-active and low-active drivers. A simplified block diagram for the
       Full Bridge modes is shown in Figure 31-6.

       Figure 31-5. Example of Full-Bridge Application

                                                                                                         Re v. 10 -00 02 63 A
                                                                                                                   2/8/20 19
                                                                              VDD


                                        FET              QA                               QC
                                                                                                     FET
                                       Driver                                                       Driver
                  CWG1A


                  CWG1B                                                      LOAD


                  CWG1C                 FET                                                          FET
                                       Driver                                                       Driver

                  CWG1D                                  QB                               QD


--- p497 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                           CWG - Complementary Waveform Generator
                                                                                                                          Module
Figure 31-6. Simplified CWG Block Diagram (Forward and Reverse Full Bridge Modes)

           MODE = ‘b010: Forward
                                                                                                                  Re v. 10 -00 02 12 D
                                                                                                                            2/7/20 19


                                                                                                  LSAC
           MODE = ‘b011: Reverse

                                                                                                   1     11
                             Rising Dead-Band Block                                                0     10
                CWG Clock         clock
                                         signal out                                            High-Z    01
                                 signal in                                                               00

                                             CWG                                                                  1
                                                                          CWG Data A
                                             Data
                                                                                                                  0          CWGA
                                                                               POLA
      MODE[0]     D   Q

        CWG           Q                                                                           LSBD
        Data

                                          cwg data                                                 1     11
                                 signal in                                                         0     10
                                          signal out
                CWG Clock         clock                                                        High-Z    01
                             Falling Dead-Band Block                                                     00

                                                                                                                  1
      CWG Data Input                                                      CWG Data B
                                                           CWG Data
                                                                                                                  0 CWGxB
                                                                               POLB
                                 D   Q

                                 E                                                                LSAC


                                                                                                   1     11
          EN
                                                                                                   0     10
                                                                                               High-Z    01
                                                                                                         00


                                                                         CWG Data C
                                                                                                                  1
                                                                                                                  0 CWGxC
                                                                               POLC
          Auto-shutdown source                         S    Q
           (CWGxAS1 register)
                                                       R                                          LSBD


                      REN
                                                                                                   1     11
             SHUTDO WN = 0
                                                                                                   0     10
                                                                                               High-Z    01
                                                                                                         00


                                                                         CWG Data D
                                                                                                                  1
                                                                                                                  0 CWGxD
                                                                               POLD

                                                 SHUTDO WN

                                                       FREEZE
                                                                                       D   Q

                                                                       CWG Data


--- p498 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                      CWG - Complementary Waveform Generator
                                                                                                                     Module
        In Forward Full Bridge mode (MODE = ‘b010), CWGxA is driven to its Active state, CWGxB and
        CWGxC are driven to their Inactive state, and CWGxD is modulated by the input signal, as shown in
        Figure 31-7.
        In Reverse Full Bridge mode (MODE = ‘b011), CWGxC is driven to its Active state, CWGxA and
        CWGxD are driven to their Inactive states, and CWGxB is modulated by the input signal, as shown in
        Figure 31-7.
        In Full Bridge mode, the dead-band period is used when there is a switch from forward to reverse
        or vice versa. This dead-band control is described in the Dead-Band Control section, with additional
        details in the Rising Edge and Reverse Dead Band and Falling Edge and Forward Dead Band sections.
        Steering modes are not used with either of the Full Bridge modes.

        Figure 31-7. Example of Full-Bridge Output
                                                                                                              Rev. 30-000099A


                  Forward
                                                                                                                     4/14/2017


                   Mode
                                           Period


                 CWGxA (2)


                 CWGxB (2)


                 CWGxC (2)
                             Pulse Width


                 CWGxD (2)

                             (1)                                (1)


                  Reverse
                   Mode
                                            Period


                CWGxA (2)
                             Pulse Width


                CWGxB (2)


                CWGxC (2)


                CWGxD (2)

                             (1)                                (1)


        Notes:
        1. A rising CWG data input creates a rising event on the modulated output.
        2. Output signals shown as active-high; all POLy bits are clear.

31.2.3.1 Direction Change in Full Bridge Mode
        In Full Bridge mode, changing the MODE[0] bit controls the forward/reverse direction. Direction
        changes occur on the next rising edge of the modulated input. The sequence, described as follows,
        is illustrated in Figure 31-8.


--- p499 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                        CWG - Complementary Waveform Generator
                                                                                                                       Module
        1. The associated active output CWGxA and the inactive output CWGxC are switched to drive in the
           opposite direction.
        2. The previously modulated output CWGxD is switched to the Inactive state, and the previously
           inactive output CWGxB begins to modulate.
        3. CWG modulation resumes after the direction-switch dead band has elapsed.

        Figure 31-8. Example of PWM Direction Change at Near 100% Duty Cycle

                                                                                                Rev. 30-000100A
                                                                                                       4/14/2017


                                                          t1
                                   Forward Period                         Reverse Period


                 CWGxA


                CWGxB                                                     Pulse Width


                CWGxC

                CWGxD

                                    Pulse Width
                                                               TON


        External Switch C
                                                                   TOFF

        External Switch D


         Potential Shoot-                                                  T = TOFF - TON
         Through Current


31.2.3.2 Dead-Band Delay in Full Bridge Mode
        Dead-band delay is important when either of the following conditions is true:
        •   The direction of the CWG output changes when the duty cycle of the data input is at or near 100%
        •   The turn-off time of the power switch, including the power device and driver circuit, is greater
            than the turn-on time
        The dead-band delay is inserted only when changing directions and only the modulated output is
        affected. The statically-configured outputs (CWGxA and CWGxC) are not afforded dead band and
        switch essentially simultaneously.
        Figure 31-8 shows an example of the CWG outputs changing directions from forward to reverse,
        at near 100% duty cycle. In this example, at time t1, the output of CWGxA and CWGxD becomes
        inactive, while the output of CWGxC becomes active. Since the turn-off time of the power devices is
        longer than the turn-on time, a shoot-through current will flow through the power devices QC and
        QD for the duration of ‘T’. The same phenomenon will occur to power devices QA and QB for the
        CWG direction change from reverse to forward.
        When changing the CWG direction at high duty cycle is required for an application, two possible
        solutions for eliminating the shoot-through current are:
        1. Reduce the CWG duty cycle for one period before changing directions.


--- p500 ---
                                                                                                  PIC18F27/47/57Q43
                                                                              CWG - Complementary Waveform Generator
                                                                                                             Module
       2. Use switch drivers that can drive the switches off faster than they can drive them on.

31.2.4 Steering Modes
       In both Synchronous and Asynchronous Steering modes, the CWG Data can be steered to any
       combination of four CWG outputs. A fixed value will be presented on all the outputs not used for
       the PWM output. Each output has independent polarity, steering, and shutdown options. Dead-band
       control is not used in either Steering mode.
       For example, when STRA = 0, the corresponding pin is held at the level defined by OVRA. When STRA
       = 1, the pin is driven by the CWG Data signal. The POLy bits control the signal polarity only when
       STRy = 1.
       The CWG auto-shutdown operation also applies in Steering modes as described in the Auto-
       Shutdown section. An auto-shutdown event will only affect pins that have STRy = 1.


--- p501 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                CWG - Complementary Waveform Generator
                                                                                                               Module
Figure 31-9. Simplified CWG Block Diagram (Output Steering Modes)

             MODE = ‘b000: Asynchronous                                                      LSAC          Re v. 10 -00 02 11 D
                                                                                                                     2/7/20 19


             MODE = ‘b001: Synchronous
                                                                                         1    11
                                                                                         0    10
                                                                                 High-Z       01
                                                                                              00

                                                     CWG Data A                                        1
                                                                                     1
                                                            POLA                                       0 CWGxA
                                                                                     0
                                                                      OVRA

                                                                         STRA                LSBD


                                                                                         1    11
                                                                                         0    10
                                              CWG
            CWG Data                          Data                               High-Z       01
              Input
                                                                                              00

                             D   Q                    CWG Data B
                                                                                                       1
                             E                                                       1
                                                            POLB                                       0 CWGxB
                                                                                     0
                                                                         OVRB
             EN                                                           STRB               LSAC


                                                                                         1    11
                                                                                         0    10
                                                                                 High-Z       01
                                                                                              00

                                                      CWG Data C                                       1
      Auto-shutdown source
                                          S   Q                                      1
       (CWGxAS1 register)                                   POLC                                       0 CWGxC
                                          R                                          0
                                                                         OVRC

                    REN                                                   STRC               LSBD
         SHUTDO WN = 0

                                                                                         1    11
                                                                                         0    10
                                                                                 High-Z       01
                                                                                              00

                                                      CWG Data D                                       1
                                                                                     1
                                                            POLD                                       0 CWGxD
                                                                                     0
                                                                         OVRD
                                     SHUTDO WN
                                                                                 STRD
                                          FREEZE
                                                                     D    Q

                                                      CWG Data


--- p502 ---
                                                                                                                        PIC18F27/47/57Q43
                                                                                                    CWG - Complementary Waveform Generator
                                                                                                                                   Module
31.2.4.1 Synchronous Steering Mode
        In Synchronous Steering mode (MODE = ‘b001), the changes to steering selection registers take
        effect on the next rising edge of CWG Data (see the figure below). In Synchronous Steering mode,
        the output will always produce a complete waveform.


                     Important: Only the STRx bits are synchronized; the OVRx bits are not
                     synchronized.


        Figure 31-10. Example of Synchronous Steering (MODE = ‘b001)
                                                                                                                                                  Rev. 30-000101A
                                                                                                                                                         4/14/2017


                 CWGx clock


                  CWG Data


                    CWGxA


                    CWGxB


31.2.4.2 Asynchronous Steering Mode
        In Asynchronous mode (MODE = ‘b000), steering takes effect at the end of the instruction cycle that
        writes to STRx. In Asynchronous Steering mode, the output signal may be an incomplete waveform
        (see the figure below). This operation may be useful when the user firmware needs to immediately
        remove a signal from the output pin.

        Figure 31-11. Example of Asynchronous Steering (MODE = ‘b000)
                                                                                                                               Rev. 30-000102A
                                                                                                                                      4/14/2017


                              CWG Data

                                         End of Instruction Cycle                                   End of Instruction Cycle

                                 STRA


                               CWGxA


                                                                    CWG1A Follows CWG1 data input


31.2.4.3 Start-Up Considerations
        The application hardware must use the proper external pull-up and/or pull-down resistors on the
        CWG output pins. This is required because all I/O pins are forced to high-impedance at Reset.
        The Polarity Control (POLy) bits allow the user to choose whether the output signals are active-high
        or active-low.

31.3    Clock Source
        The clock source is used to drive the dead-band timing circuits. The CWG module allows the
        following clock sources to be selected:
        •   FOSC (system clock)
        •   HFINTOSC
        When the HFINTOSC is selected, the HFINTOSC will be kept running during Sleep. Therefore, the
        CWG modes requiring dead band can operate in Sleep, provided that the CWG data input is also
        active during Sleep. The clock sources are selected using the CS bit. The system clock FOSC is disabled
        in Sleep and thus dead-band control cannot be used.


--- p503 ---
                                                                                                   PIC18F27/47/57Q43
                                                                               CWG - Complementary Waveform Generator
                                                                                                              Module
31.4    Selectable Input Sources
        The CWG generates the output waveforms from the input sources which are selected with the ISM
        bits. Refer to the CWGxISM register for more details.

31.5    Output Control
31.5.1 CWG Output
        Each CWG output can be routed to a Peripheral Pin Select (PPS) output via the RxyPPS register. Refer
        to the “PPS - Peripheral Pin Select Module” chapter for more details.

31.5.2 Polarity Control
        The polarity of each CWG output can be selected independently. When the output polarity bit
        is set, the corresponding output is active-high. Clearing the output polarity bit configures the
        corresponding output as active-low. However, polarity does not affect the override levels. Output
        polarity is selected with the POLy bits. Auto-shutdown and steering options are unaffected by
        polarity.

31.6    Dead-Band Control
        The dead-band control provides nonoverlapping complementary outputs to prevent shoot-through
        current when the outputs switch. Dead-band operation is employed for Half Bridge and Full Bridge
        modes. The CWG contains two 6-bit dead-band counters. One is used for the rising edge of the input
        source control in Half Bridge mode or for reverse direction change dead band in Full Bridge mode.
        The other is used for the falling edge of the input source control in Half Bridge mode or for forward
        direction change dead band in Full Bridge mode.
        Dead band is timed by counting CWG clock periods from zero up to the value in the rising or falling
        dead-band counter registers.

31.6.1 Dead-Band Functionality in Half Bridge Mode
        In Half Bridge mode, the dead-band counters dictate the delay between the falling edge of the
        normal output and the rising edge of the inverted output. This can be seen in Figure 31-1.

31.6.2 Dead-Band Functionality in Full Bridge Mode
        In Full Bridge mode, the dead-band counters are used when undergoing a direction change. The
        MODE[0] bit can be set or cleared while the CWG is running, allowing for changes from Forward to
        Reverse mode. The CWGxA and CWGxC signals will change immediately upon the first rising input
        edge following a direction change, but the modulated signals (CWGxB or CWGxD, depending on the
        direction of the change) will experience a delay dictated by the dead-band counters.

31.7    Rising Edge and Reverse Dead Band
        In Half Bridge mode, the rising edge dead band delays the turn-on of the CWGxA output after the
        rising edge of the CWG data input. In Full Bridge mode, the reverse dead-band delay is only inserted
        when changing directions from Forward mode to Reverse mode, and only the modulated output,
        CWGxB, is affected.
        The CWGxDBR register determines the duration of the dead-band interval on the rising edge of the
        input source signal. This duration is from 0 to 64 periods of the CWG clock. The following figure
        illustrates different dead-band delays for rising and falling CWG Data events.


--- p504 ---
                                                                                                     PIC18F27/47/57Q43
                                                                                 CWG - Complementary Waveform Generator
                                                                                                                Module
       Figure 31-12. Dead-Band Operation, CWGxDBR = 0x01, CWGxDBF = 0x02
                                                                                                                  Rev. 30-000103A
                                                                                                                         4/14/2017


       cwg_clock


       CWG Data


        CWGxA


        CWGxB


       Dead band is always initiated on the edge of the input source signal. A count of zero indicates that
       no dead band is present.
       If the input source signal reverses polarity before the dead-band count is completed, then no signal
       will be seen on the respective output.
       The CWGxDBR register value is double-buffered. When EN = 0, the buffer is loaded when CWGxDBR
       is written. When EN = 1, the buffer will be loaded at the rising edge following the first falling edge of
       the CWG Data, after the LD bit is set.

31.8   Falling Edge and Forward Dead Band
       In Half Bridge mode, the falling edge dead band delays the turn-on of the CWGxB output at the
       falling edge of the CWG data input. In Full Bridge mode, the forward dead-band delay is only
       inserted when changing directions from Reverse mode to Forward mode, and only the modulated
       output, CWGxD, is affected.
       The CWGxDBF register determines the duration of the dead-band interval on the falling edge of the
       input source signal. This duration is from 0 to 64 periods of the CWG clock.
       Dead-band delay is always initiated on the edge of the input source signal. A count of zero indicates
       that no dead band is present.
       If the input source signal reverses polarity before the dead-band count is completed, then no signal
       will be seen on the respective output.

       Figure 31-13. Dead-Band Operation, CWGxDBR = 0x03, CWGxDBF = 0x06, Source Shorter Than Dead Band
                                                                                                                  Rev. 30-000104A
                                                                                                                         4/14/2017


       cwg_clock


       CWG Data

         CWGxA


         CWGxB

                                                             source shorter than dead band


       The CWGxDBF register value is double-buffered. When EN = 0, the buffer is loaded when CWGxDBF
       is written. When EN = 1, the buffer will be loaded at the rising edge following the first falling edge of
       the data input after the LD bit is set.


--- p505 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                             CWG - Complementary Waveform Generator
                                                                                                                            Module
31.9   Dead-Band Jitter
       When the rising and falling edges of the input source are asynchronous to the CWG clock, it creates
       jitter in the dead-band time delay. The maximum jitter is equal to one CWG clock period. Refer to the
       equations below for more details.

       Equation 31-1. Dead-Band Delay Time Calculation
                                       1
       TDEAD − BAND_MIN =                     • DBx
                                   FCWG_CLOCK
                                       1
       TDEAD − BAND_MAX =                     • DBx + 1
                                   FCWG_CLOCK
       T JITTER = TDEAD − BAND_MAX − TDEAD − BAND_MIN
                         1
       T JITTER =
                     FCWG_CLOCK
       TDEAD − BAND_MAX = TDEAD − BAND_MIN + T JITTER
       Dead-Band Delay Example Calculation
       DBx = 0x0A = 10
       FCWG_CLOCK = 8 MHz
       T JITTER =   1   = 125 ns
                  8 MHz
       TDEAD − BAND_MIN = 125 ns • 10 = 1.25 μs
       TDEAD − BAND_MAX = 1.25 μs + 0.125 μs = 1.37 μs

31.10 Auto-Shutdown
       Auto-shutdown is a method to immediately override the CWG output levels with specific overrides
       that allow for safe shutdown of the circuit. The Shutdown state can be either cleared automatically
       or held until cleared by software. The auto-shutdown circuit is illustrated in the following figure.

       Figure 31-14. CWG Shutdown Block Diagram

                      Write 1 to                                                                                         Re v. 10 -00 01 72 F
                                                                                                                                   2/8/20 19
                  SHUTDOWN bit


           Auto-shutdown source
            (CWGxAS1 register)
                                                                            SHUTDOWN                      S
                                                                  S     Q
                                                                                                     D        Q    CWG_shutdown
                                            REN                                FREEZE
                                                                  R
                                       Write 0 to
                                   SHUTDOWN bit
                                                                                          CWG_data   CK


31.10.1 Shutdown
       The Shutdown state can be entered by either of the following two methods:
       •   Software Generated
       •   External Input

31.10.2 Software Generated Shutdown
       Setting the SHUTDOWN bit will force the CWG into the Shutdown state.
       When the auto-restart is disabled, the Shutdown state will persist as long as the SHUTDOWN bit is
       set.


--- p506 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                CWG - Complementary Waveform Generator
                                                                                                               Module
        When auto-restart is enabled, the SHUTDOWN bit will clear automatically and resume operation on
        the next rising edge event. The SHUTDOWN bit indicates when a Shutdown condition exists. The bit
        may be set or cleared in software or by hardware.

31.10.3 External Input Source
        External shutdown inputs provide the fastest way to safely suspend CWG operation in the event
        of a Fault condition. When any of the selected shutdown inputs goes active, the CWG outputs
        will immediately go to the selected override levels without software delay. The override levels are
        selected by the LSBD and LSAC bits. Several input sources can be selected to cause a Shutdown
        condition. All input sources are active-low. The shutdown input sources are individually enabled by
        the ASyE bits.


                     Important: Shutdown inputs are level sensitive, not edge sensitive. The
                     Shutdown state cannot be cleared, except by disabling auto-shutdown, as long
                     as the shutdown input level persists.


31.10.4 Pin Override Levels
        The levels driven to the CWG outputs during an auto-shutdown event are controlled by the LSBD
        and LSAC bits. The LSBD bits control CWGxB/D output levels, while the LSAC bits control the
        CWGxA/C output levels.

31.10.5 Auto-Shutdown Interrupts
        When an auto-shutdown event occurs, either by software or hardware setting SHUTDOWN, the
        CWGxIF flag bit of the PIRx register is set.

31.11 Auto-Shutdown Restart
        After an auto-shutdown event has occurred, there are two ways to resume operation:
        •   Software controlled
        •   Auto-restart
        In either case, the shutdown source must be cleared before the restart can take place. That is, either
        the Shutdown condition must be removed, or the corresponding ASyE bit must be cleared.

31.11.1 Software-Controlled Restart
        When the REN bit is clear (REN = 0), the CWG module must be restarted after an auto-shutdown
        event through software.
        Once all auto-shutdown sources are removed, the software must clear the SHUTDOWN bit. Once
        SHUTDOWN is cleared, the CWG module will resume operation upon the first rising edge of the CWG
        data input.


                     Important: The SHUTDOWN bit cannot be cleared in software if the Auto-
                     Shutdown condition is still present.


--- p507 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                              CWG - Complementary Waveform Generator
                                                                                                                             Module
        Figure 31-15. Shutdown Functionality, Auto-Restart Disabled (REN = 0, LSAC = ‘b01, LSBD = ‘b01)
                                                                                                                                    Rev. 30-000105A
                                                                                                                                           4/14/2017


                                                            Shutdown Event Ceases     REN Cleared by Software


             CWG Input


       Shutdown Source


            SHUTDOWN

               CWGxA
               CWGxC                                        Tri-State (No Pulse)


               CWGxB                                        Tri-State (No Pulse)
               CWGxD
                               No Shutdown
                                                     Shutdown                                                      Output Resumes


31.11.2 Auto-Restart
        When the REN bit is set (REN = 1), the CWG module will restart from the Shutdown state
        automatically.
        Once all Auto-Shutdown conditions are removed, the hardware will automatically clear the
        SHUTDOWN bit. Once SHUTDOWN is cleared, the CWG module will resume operation upon the
        first rising edge of the CWG data input.


                         Important: The SHUTDOWN bit cannot be cleared in software if the Auto-
                         Shutdown condition is still present.


        Figure 31-16. Shutdown Functionality, Auto-Restart Enabled (REN = 1, LSAC = ‘b01, LSBD = ‘b01)
                                                                                                                                     Rev. 30-000106A
                                                                                                                                            4/14/2017


                                                          Shutdown Event Ceases     REN auto-cleared by hardware


             CWG Input

       Shutdown Source


            SHUTDOWN

               CWGxA                                      Tri-State (No Pulse)
               CWGxC

               CWGxB                                      Tri-State (No Pulse)
               CWGxD
                              No Shutdown
                                                      Shutdown                           Output Resumes


31.12 Operation During Sleep
        The CWG module operates independently from the system clock and will continue to run during
        Sleep, provided that the clock and input sources selected remain active.
        The HFINTOSC remains active during Sleep when all the following conditions are met:
        •   CWG module is enabled
        •   Input source is active
        •   HFINTOSC is selected as the clock source, regardless of the system clock source selected.


--- p508 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                CWG - Complementary Waveform Generator
                                                                                                               Module
      In other words, if the HFINTOSC is simultaneously selected as the system clock and the CWG clock
      source when the CWG is enabled and the input source is active, then the CPU will go Idle during
      Sleep, but the HFINTOSC will remain active, and the CWG will continue to operate. This will have a
      direct effect on the Sleep mode current.

31.13 Configuring the CWG
      1. Ensure that the TRIS control bits corresponding to CWG outputs are set so that all are configured
         as inputs, ensuring that the outputs are inactive during setup. External hardware must ensure
         that pin levels are held to safe levels.
      2. Clear the EN bit, if not already cleared.
      3. Configure the MODE bits to set the output operating mode.
      4. Configure the POLy bits to set the output polarities.
      5. Configure the ISM bits to select the data input source.
      6. If a Steering mode is selected, configure the STRy bits to select the desired output on the CWG
         outputs.
      7. Configure the LSBD and LSAC bits to select the Auto-Shutdown Output Override states (this is
         necessary even if not using auto-shutdown, because start-up will be from a Shutdown state).
      8. If auto-restart is desired, set the REN bit.
      9. If auto-shutdown is desired, configure the ASyE bits to select the shutdown source.
      10. Set the desired rising and falling dead-band times with the CWGxDBR and CWGxDBF registers.
      11. Select the clock source with the CS bit.
      12. Set the EN bit to enable the module.
      13. Clear the TRIS bits that correspond to the CWG outputs to set them as outputs.
      If auto-restart is to be used, set the REN bit and the SHUTDOWN bit will be cleared automatically.
      Otherwise, clear the SHUTDOWN bit in software to start the CWG.

31.14 Register Definitions: CWG Control
      Long bit name prefixes for the CWG peripherals are shown in the table below. Refer to the “Long Bit
      Names” section in the “Register and Bit Naming Conventions” chapter for more information.

      Table 31-1. CWG Long Bit Name Prefixes
                       Peripheral                                              Bit Name Prefix
                         CWG1                                                          CWG1
                         CWG2                                                          CWG2
                         CWG3                                                          CWG3


--- p509 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                           CWG - Complementary Waveform Generator
                                                                                                                          Module
31.14.1 CWGxCON0

           Name:       CWGxCON0
           Address:    0x3C0,0x3C9,0x3D2

           CWG Control Register 0

     Bit        7             6                5               4                  3            2             1                  0
               EN            LD                                                                           MODE[2:0]
  Access       R/W         R/W/HC                                                             R/W           R/W               R/W
   Reset        0             0                                                                0             0                 0

Bit 7 – EN CWG Enable
           Value      Description
           1          Module is enabled
           0          Module is disabled

Bit 6 – LD CWG1 Load Buffers(1)
           Value      Description
           1          Dead-band count buffers to be loaded on CWG data rising edge, following first falling edge after this bit is set
           0          Buffers remain unchanged

Bits 2:0 – MODE[2:0] CWG Mode
           Value      Description
           111        Reserved
           110        Reserved
           101        CWG outputs operate in Push-Pull mode
           100        CWG outputs operate in Half Bridge mode
           011        CWG outputs operate in Reverse Full Bridge mode
           010        CWG outputs operate in Forward Full Bridge mode
           001        CWG outputs operate in Synchronous Steering mode
           000        CWG outputs operate in Asynchronous Steering mode

           Note:
           1. This bit can only be set after EN = 1; it cannot be set in the same cycle when EN is set.


--- p510 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                          CWG - Complementary Waveform Generator
                                                                                                                         Module
31.14.2 CWGxCON1

            Name:        CWGxCON1
            Address:     0x3C1,0x3CA,0x3D3

            CWG Control Register 1

      Bit           7            6                5             4                  3         2            1             0
                                                 IN                              POLD       POLC        POLB          POLA
  Access                                          R                               R/W       R/W          R/W           R/W
   Reset                                          x                                0         0            0             0

Bit 5 – IN CWG Input Value (read-only)
            Value       Description
            1           CWG data input is a logic ‘1’
            0           CWG data input is a logic ‘0’


Bits 0, 1, 2, 3 – POLy CWG Output ‘y’ Polarity
            Value       Description
            1           Signal output is inverted polarity
            0           Signal output is normal polarity


--- p511 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                       CWG - Complementary Waveform Generator
                                                                                                                      Module
31.14.3 CWGxCLK

            Name:        CWGxCLK
            Address:     0x3BC,0x3C5,0x3CE

            CWG Clock Input Selection Register

      Bit           7           6              5             4                  3             2        1            0
                                                                                                                    CS
  Access                                                                                                           R/W
   Reset                                                                                                            0

Bit 0 – CS CWG Clock Source Selection Select
            Value       Description
            1           HFINTOSC (remains operating during Sleep)
            0           FOSC


--- p512 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                     CWG - Complementary Waveform Generator
                                                                                                                    Module
31.14.4 CWGxISM

            Name:       CWGxISM
            Address:    0x3BD,0x3C6,0x3CF

            CWGx Input Selection Register

      Bit        7           6              5              4                   3        2             1            0
                                                                                     ISM[4:0]
  Access                                                 R/W                  R/W      R/W          R/W          R/W
   Reset                                                  0                    0        0            0            0

Bits 4:0 – ISM[4:0] CWG Data Input Source Select
                                                                      Input Selection
                  ISM
                                      CWG1                                CWG2                            CWG3
             11111-11010                                                 Reserved
                11001                                                   CLC8_OUT
                11000                                                   CLC7_OUT
                10111                                                   CLC6_OUT
                10110                                                   CLC5_OUT
                10101                                                   CLC4_OUT
                10100                                                   CLC3_OUT
                10011                                                   CLC2_OUT
                10010                                                   CLC1_OUT
                10001                                                   DSM1_OUT
                10000                                                   CMP2_OUT
                01111                                                   CMP1_OUT
                01110                                                   NCO3_OUT
                01101                                                   NCO2_OUT
                01100                                                   NCO1_OUT
             01011-01010                                                 Reserved
                01001                                                 PWM3S1P1_OUT
                01000                                                 PWM3S1P2_OUT
                00111                                                 PWM2S1P1_OUT
                00110                                                 PWM2S1P2_OUT
                00101                                                 PWM1S1P1_OUT
                00100                                                 PWM1S1P2_OUT
                00011                                                    CCP3_OUT
                00010                                                    CCP2_OUT
                00001                                                    CCP1_OUT
                00000        Pin selected by CWG1PPS             Pin selected by CWG2PPS        Pin selected by CWG3PPS


--- p513 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                        CWG - Complementary Waveform Generator
                                                                                                                       Module
31.14.5 CWGxSTR

            Name:       CWGxSTR
            Address:    0x3C4,0x3CD,0x3D6

            CWG Steering Control Register(1)

      Bit         7           6              5              4                   3          2              1             0
                OVRD         OVRC           OVRB           OVRA               STRD       STRC           STRB          STRA
  Access         R/W         R/W            R/W            R/W                R/W        R/W            R/W           R/W
   Reset          0           0              0              0                   0          0              0             0

Bits 4, 5, 6, 7 – OVRy Steering Data OVR'y'
            Value      Condition             Description
            x          STRy = 1              CWGx'y' output has the CWG data input waveform with polarity control from POLy bit
            1          STRy = 0 and POLy = x CWGx'y' output is high
            0          STRy = 0 and POLy = x CWGx'y' output is low


Bits 0, 1, 2, 3 – STRy STR'y' Steering Enable(2)
            Value      Description
            1          CWGx'y' output has the CWG data input waveform with polarity control from the POLy bit
            0          CWGx'y' output is assigned to value of the OVRy bit

            Notes:
            1. The bits in this register apply only when MODE = ‘b00x (CWGxCON0, Steering modes).
            2. This bit is double-buffered when MODE = ‘b001.


--- p514 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                  CWG - Complementary Waveform Generator
                                                                                                                                 Module
31.14.6 CWGxAS0

           Name:       CWGxAS0
           Address:    0x3C2,0x3CB,0x3D4

           CWG Auto-Shutdown Control Register 0

     Bit     7                6                  5                4                   3                 2         1             0
         SHUTDOWN            REN                     LSBD[1:0]                             LSAC[1:0]
  Access R/W/HS/HC           R/W             R/W                 R/W                 R/W               R/W
   Reset     0                0               0                   1                   0                 1

Bit 7 – SHUTDOWN Auto-Shutdown Event Status(1,2)
           Value      Description
           1          An Auto-Shutdown state is in effect
           0          No auto-shutdown event has occurred

Bit 6 – REN Auto-Restart Enable
           Value      Description
           1          Auto-restart is enabled
           0          Auto-restart is disabled

Bits 5:4 – LSBD[1:0] CWGxB and CWGxD Auto-Shutdown State Control
           Value      Description
           11         A logic ‘1’ is placed on CWGxB/D when an auto-shutdown event occurs
           10         A logic ‘0’ is placed on CWGxB/D when an auto-shutdown event occurs
           01         Pin is tri-stated on CWGxB/D when an auto-shutdown event occurs
           00         The Inactive state of the pin, including polarity, is placed on CWGxB/D after the required dead-band interval
                      when an auto-shutdown event occurs

Bits 3:2 – LSAC[1:0] CWGxA and CWGxC Auto-Shutdown State Control
           Value      Description
           11         A logic ‘1’ is placed on CWGxA/C when an auto-shutdown event occurs
           10         A logic ‘0’ is placed on CWGxA/C when an auto-shutdown event occurs
           01         Pin is tri-stated on CWGxA/C when an auto-shutdown event occurs
           00         The Inactive state of the pin, including polarity, is placed on CWGxA/C after the required dead-band interval
                      when an auto-shutdown event occurs

           Notes:
           1. This bit may be written while EN = 0, to place the outputs into the shutdown configuration.
           2. The outputs will remain in Auto-Shutdown state until the next rising edge of the CWG data input
              after this bit is cleared.


--- p515 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                   CWG - Complementary Waveform Generator
                                                                                                                  Module
31.14.7 CWGxAS1

            Name:       CWGxAS1
            Address:    0x3C3,0x3CC,0x3D5

            CWG Auto-Shutdown Control Register 1

      Bit        7           6            5             4                 3           2            1            0
                AS7E        AS6E         AS5E          AS4E              AS3E        AS2E         AS1E         AS0E
  Access        R/W         R/W          R/W           R/W               R/W         R/W          R/W          R/W
   Reset         0           0            0             0                 0           0            0            0

Bits 0, 1, 2, 3, 4, 5, 6, 7 – ASyE CWG Auto-Shutdown Source Enable(1,2)
                                                       Auto-Shutdown Source
             ASyE
                               CWG1                             CWG2                                CWG3
             AS7E                                             CLC6_OUT
             AS6E            CLC2_OUT                         CLC3_OUT                            CLC4_OUT
             AS5E                                            CMP2_OUT
             AS4E                                            CMP1_OUT
             AS3E                                   TMR6_Postscaler_OUT (Inverted)
             AS2E                                   TMR4_Postscaler_OUT (Inverted)
             AS1E                                   TMR2_Postscaler_OUT (Inverted)
             AS0E      Pin selected by CWG1PPS        Pin selected by CWG2PPS               Pin selected by CWG3PPS

            Notes:
            1. This bit may be written while EN = 0, to place the outputs into the shutdown configuration.
            2. The outputs will remain in Auto-Shutdown state until the next rising edge of the CWG data input
               after this bit is cleared.


--- p516 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                             CWG - Complementary Waveform Generator
                                                                                                                            Module
31.14.8 CWGxDBR

           Name:        CWGxDBR
           Address:     0x3BE,0x3C7,0x3D0

           CWG Rising Dead-Band Count Register

     Bit           7           6               5              4                   3                2         1             0
                                                                                       DBR[5:0]
  Access                                     R/W            R/W                  R/W              R/W       R/W          R/W
   Reset                                      x              x                    x                x         x            x

Bits 5:0 – DBR[5:0] CWG Rising Edge-Triggered Dead-Band Count
          Reset States: POR/BOR = xxxxxx
                        All Other Resets = uuuuuu
           Value       Description
           n           Dead band is active no less than n and no more than n+1 CWG clock periods after the rising edge
           0           0 CWG clock periods. Dead-band generation is bypassed.


--- p517 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                             CWG - Complementary Waveform Generator
                                                                                                                            Module
31.14.9 CWGxDBF

           Name:        CWGxDBF
           Address:     0x3BF,0x3C8,0x3D1

           CWG Falling Dead-Band Count Register

     Bit           7           6               5              4                   3                2         1             0
                                                                                       DBF[5:0]
  Access                                     R/W             R/W                 R/W              R/W       R/W           R/W
   Reset                                      x               x                   x                x         x             x

Bits 5:0 – DBF[5:0] CWG Falling Edge-Triggered Dead-Band Count
          Reset States: POR/BOR = xxxxxx
                        All Other Resets = uuuuuu
           Value       Description
           n           Dead band is active no less than n and no more than n+1 CWG clock periods after the falling edge
           0           0 CWG clock periods. Dead-band generation is bypassed.


--- p518 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                    CWG - Complementary Waveform Generator
                                                                                                                   Module
31.15 Register Summary - CWG
Address    Name      Bit Pos.      7            6           5             4         3              2          1           0
0x03BC    CWG1CLK      7:0                                                                                               CS
0x03BD    CWG1ISM      7:0                                                                    ISM[4:0]
0x03BE    CWG1DBR      7:0                                                              DBR[5:0]
0x03BF     CWG1DBF     7:0                                                              DBF[5:0]
0x03C0    CWG1CON0     7:0         EN          LD                                                         MODE[2:0]
0x03C1    CWG1CON1     7:0                                  IN                    POLD         POLC        POLB         POLA
0x03C2     CWG1AS0     7:0      SHUTDOWN      REN             LSBD[1:0]               LSAC[1:0]
0x03C3     CWG1AS1     7:0         AS7E       AS6E        AS5E         AS4E       AS3E         AS2E         AS1E        AS0E
0x03C4     CWG1STR     7:0        OVRD        OVRC        OVRB        OVRA        STRD         STRC         STRB        STRA
0x03C5     CWG2CLK     7:0                                                                                               CS
0x03C6     CWG2ISM     7:0                                                                     ISM[4:0]
0x03C7     CWG2DBR     7:0                                                              DBR[5:0]
0x03C8     CWG2DBF     7:0                                                              DBF[5:0]
0x03C9    CWG2CON0     7:0         EN          LD                                                         MODE[2:0]
0x03CA    CWG2CON1     7:0                                  IN                    POLD         POLC        POLB         POLA
0x03CB     CWG2AS0     7:0      SHUTDOWN      REN             LSBD[1:0]               LSAC[1:0]
0x03CC     CWG2AS1     7:0         AS7E       AS6E        AS5E         AS4E       AS3E         AS2E         AS1E        AS0E
0x03CD     CWG2STR     7:0        OVRD        OVRC        OVRB        OVRA        STRD         STRC         STRB        STRA
0x03CE     CWG3CLK     7:0                                                                                               CS
0x03CF     CWG3ISM     7:0                                                                     ISM[4:0]
0x03D0     CWG3DBR     7:0                                                              DBR[5:0]
0x03D1     CWG3DBF     7:0                                                              DBF[5:0]
0x03D2    CWG3CON0     7:0         EN          LD                                                         MODE[2:0]
0x03D3    CWG3CON1     7:0                                  IN                    POLD         POLC        POLB         POLA
0x03D4     CWG3AS0     7:0      SHUTDOWN      REN             LSBD[1:0]               LSAC[1:0]
0x03D5     CWG3AS1     7:0         AS7E       AS6E        AS5E         AS4E       AS3E         AS2E         AS1E        AS0E
0x03D6     CWG3STR     7:0        OVRD        OVRC        OVRB        OVRA        STRD         STRC         STRB        STRA


--- p519 ---
