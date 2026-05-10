                       PIC18(L)F26/27/45/46/47/55/56/57K42
26.0     COMPLEMENTARY                                        26.2      Operating Modes
         WAVEFORM GENERATOR                                   The CWG module can operate in six different modes,
         (CWG) MODULE                                         as specified by the MODE[2:0] bits of the CWGxCON0
                                                              register:
The Complementary Waveform Generator (CWG)
produces half-bridge, full-bridge, and steering of PWM        • Half Bridge mode
waveforms. It is backwards compatible with previous           • Push Pull mode
CCP functions. There are three instances of the CWG           • Asynchronous Steering mode
module present on the device.                                 • Synchronous Steering mode
                                                              • Full Bridge mode, Forward
Each of the CWG modules has the following features:           • Full Bridge mode, Reverse
• Six operating modes:                                        All modes accept a single pulse data input, and
  - Synchronous Steering mode                                 provide up to four outputs as described in the following
  - Asynchronous Steering mode                                sections.
  - Full Bridge mode, Forward                                 All modes include auto-shutdown control as described
  - Full Bridge mode, Reverse                                 in Section 26.10 “Auto-Shutdown”.
  - Half Bridge mode                                            Note:     Except as noted for Full Bridge mode
  - Push Pull mode                                                        (Section 26.2.3 “Full Bridge Modes”),
• Output polarity control                                                 mode changes may only be performed
• Output steering                                                         while EN = 0 (Register 26-1).
• Independent 6-bit rising and falling event dead-
  band timers                                                 26.2.1      HALF BRIDGE MODE
  - Clocked dead band                                         In Half Bridge mode, two output signals are generated
  - Independent rising and falling dead-band                  as true and inverted versions of the input as illustrated
    enables                                                   in Figure 26-2. A nonoverlap (dead-band) time is
                                                              inserted between the two outputs as described in
• Auto-shutdown control with:
                                                              Section 26.6 “Dead-Band Control”. The output
  - Selectable shutdown sources                               steering feature cannot be used in this mode. A basic
  - Auto-restart option                                       block diagram of this mode is shown in Figure 26-1.
  - Auto-shutdown pin override control                        The unused outputs CWGxC and CWGxD drive similar
                                                              signals as CWGxA and CWGxB, with polarity
26.1     Fundamental Operation                                independently controlled by the POLC and POLD bits
                                                              of the CWGxCON1 register, respectively.
The CWG generates two output waveforms from the
selected input source.
The off-to-on transition of each output can be delayed
from the on-to-off transition of the other output, thereby
creating a time delay immediately where neither output
is driven. This is referred to as dead time and is covered
in Section 26.6 “Dead-Band Control”.
It may be necessary to guard against the possibility of
circuit faults or a feedback event arriving too late or not
at all. In this case, the active drive must be terminated
before the Fault condition causes damage. This is
referred to as auto-shutdown and is covered in Section
26.10 “Auto-Shutdown”.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 406
                       PIC18(L)F26/27/45/46/47/55/56/57K42

FIGURE 26-1:            SIMPLIFIED CWG BLOCK DIAGRAM (HALF BRIDGE MODE, MODE[2:0] = 100)


                                                                                  LSAC<1:0>                  Rev. 10-000209D
                                                                                                                     2/2/2016


                                                                                          ‘1’   00
                                                                                          ‘0’   01
                                                                                     High-Z     10
                                                                                                11
                      Rising Dead-Band Block
     CWG Clock             clock                                                                         1
                                                     CWG Data A
                                        data out
     CWG Data             data in                                                                        0        CWG1A
                                                                       POLA


                                                                                  LSBD<1:0>


                      Falling Dead-Band Block                                             ‘1’   00
                          clock                      CWG Data B                           ‘0’   01
                                        data out
                          data in                                                    High-Z     10
                                                                                                11

      CWG Data Input                                     CWG                                             1
                                                         Data
                                                                                                         0       CWG1B
                                                                       POLB
                                    D    Q

                                    E                                             LSAC<1:0>


          EN                                                                              ‘1’   00
                                                                                          ‘0’   01
                                                                                       High-Z   10
                                                                                                11

                                                                                                         1
                                                                                                         0 CWG1C
                                                                       POLC
         Auto-shutdown source                        S   Q
          (CWGxAS1 register)                                                      LSBD<1:0>
                                                     R


                    REN                                                                   ‘1’   00
            SHUTDOWN = 0                                                                  ‘0’   01
                                                                                       High-Z   10
                                                                                                11

                                                                                                         1
                                                                                                         0 CWG1D
                                                                       POLD

                                                   SHUTDOWN

                                                      FREEZE
                                                                              D    Q

                                                                  CWG Data


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 407
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 26-2:           CWGx HALF BRIDGE MODE OPERATION

CWGx_clock


     CWGxA
     CWGxC
                                                                  Rising Event Dead Band                        Rising Event D
                                        Falling Event Dead Band                         Falling Event Dead Band
     CWGxB
     CWGxD

 CWGx_data
       Note: CWGx_rising_src = CCP1_out, CWGx_falling_src = ~CCP1_out


26.2.2      PUSH PULL MODE
In Push Pull mode, two output signals are generated,
alternating copies of the input as illustrated in
Figure 26-4. This alternation creates the push-pull
effect required for driving some transformer-based
power supply designs. Steering modes are not used in
Push Pull mode. A basic block diagram for the Push
Pull mode is shown in Figure 26-3.
The push-pull sequencer is reset whenever EN = 0 or
if an auto-shutdown event occurs. The sequencer is
clocked by the first input pulse, and the first output
appears on CWGxA.
The unused outputs CWGxC and CWGxD drive copies
of CWGxA and CWGxB, respectively, but with polarity
controlled by the POLC and POLD bits of the
CWGxCON1 register, respectively.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 408
                      PIC18(L)F26/27/45/46/47/55/56/57K42

FIGURE 26-3:           SIMPLIFIED CWG BLOCK DIAGRAM (PUSH PULL MODE, MODE[2:0] = 101)

                                                                   LSAC<1:0>
                                                                                             Rev. 10-000210D
                                                                                                     2/2/2016


                                                                           ‘1’   00
                                                                           ‘0’   01
                                                                       High-Z    10
                                                                                 11

                                                                                         1
      CWG Data                             CWG Data A
                                                                                         0 CWG1A
                                                            POLA


                                                                   LSBD<1:0>
                                 D   Q

                                     Q
                                                                           ‘1’   00
                                                                           ‘0’   01

                                                                       High-Z    10

                                           CWG Data B                            11

                                                                                         1
     CWG Data Input                         CWG                                          0 CWG1B
                                                            POLB
                                            Data
                                 D   Q
                                                                   LSAC<1:0>
                                 E

                                                                           ‘1’   00
          EN                                                               ‘0’   01
                                                                       High-Z    10
                                                                                 11

                                                                                         1
                                                                                         0 CWG1C
                                                            POLC
          Auto-shutdown source             S   Q
           (CWGxAS1 register)
                                           R                       LSBD<1:0>


                      REN                                                        00
                                                                           ‘1’
               SHUTDOWN = 0
                                                                           ‘0’   01
                                                                       High-Z    10
                                                                                 11

                                                                                         1
                                                                                         0 CWG1D
                                                            POLD


                                         SHUTDOWN
                                           FREEZE
                                                                   D   Q

                                                        CWG Data


 2017-2021 Microchip Technology Inc.                                                 DS40001919G-page 409
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 26-4:           CWGx PUSH PULL MODE OPERATION


           CW G 1
            clock

            Input
           source


          C W G 1A


          C W G 1B


26.2.3      FULL BRIDGE MODES
In Forward and Reverse Full Bridge modes, three
outputs drive static values while the fourth is modulated
by the input data signal. The mode selection may be
toggled between forward and reverse by toggling the
MODE[0] bit of the CWGxCON0 while keeping
MODE[2:1] static, without disabling the CWG module.
When connected as shown in Figure 26-5, the outputs
are appropriate for a full-bridge motor driver. Each
CWG output signal has independent polarity control, so
the circuit can be adapted to high-active and low-active
drivers. A simplified block diagram for the Full Bridge
modes is shown in Figure 26-6.

FIGURE 26-5:           EXAMPLE OF FULL-BRIDGE APPLICATION
                                                                                 Rev. 10-000263A
                                                                                        12/8/2015


                                                             VDD


                                    FET             QA             QC
                                                                         FET
                                   Driver                               Driver
            CWG1A


            CWG1B                                           LOAD


            CWG1C                   FET                                  FET
                                   Driver                               Driver

            CWG1D                                   QB             QD


 2017-2021 Microchip Technology Inc.                                   DS40001919G-page 410
                         PIC18(L)F26/27/45/46/47/55/56/57K42

FIGURE 26-6:             SIMPLIFIED CWG BLOCK DIAGRAM (FORWARD AND REVERSE FULL BRIDGE
                         MODES)

         MODE<2:0> = 010: Forward
                                                                                                               Rev. 10-000212D
                                                                                                                       2/2/2016


                                                                                        LSAC<1:0>
         MODE<2:0> = 011: Reverse


                                                                                                ‘1’   00
                            Rising Dead-Band Block                                              ‘0’   01
              CWG Clock          clock
                                        signal out                                           High-Z   10
                                signal in                                                             11

                                            CWG                                                                1
                                                                       CWG Data A
                                            Data
     MODE<2:0>                                                                                                 0 CWG1A
                                                                          POLA
                 D   Q
       CWG           Q                                                                  LSBD<1:0>
       Data

                                         cwg data                                               ‘1’   00
                                signal in                                                       ‘0’   01
                                         signal out
              CWG Clock          clock                                                       High-Z   10

                            Falling Dead-Band Block                                                   11

                                                                                                               1
     CWG Data Input                                                    CWG Data B
                                                          CWG Data
                                                                                                               0 CWG1B
                                                                          POLB
                                D   Q

                                E                                                       LSAC<1:0>


                                                                                                ‘1’   00
         EN
                                                                                                ‘0’   01
                                                                                             High-Z   10
                                                                                                      11


                                                                      CWG Data C
                                                                                                               1
                                                                                                               0 CWG1C
                                                                          POLC
         Auto-shutdown source                         S    Q
          (CWGxAS1 register)
                                                      R                                 LSBD<1:0>


                     REN
                                                                                                ‘1’   00
            SHUTDOWN = 0
                                                                                                ‘0’   01
                                                                                             High-Z   10
                                                                                                      11


                                                                      CWG Data D
                                                                                                               1
                                                                                                               0 CWG1D
                                                                          POLD

                                                SHUTDOWN

                                                      FREEZE
                                                                                    D    Q

                                                                     CWG Data


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 411
                           PIC18(L)F26/27/45/46/47/55/56/57K42
In Forward Full Bridge mode (MODE[2:0] = 010),                           In Full Bridge mode, the dead-band period is used
CWGxA is driven to its active state, CWGxB and                           when there is a switch from forward to reverse or vice-
CWGxC are driven to their inactive state, and CWGxD                      versa. This dead-band control is described in Section
is modulated by the input signal, as shown in                            26.6 “Dead-Band Control”, with additional details in
Figure 26-7.                                                             Section 26.7 “Rising Edge and Reverse Dead
In Reverse Full Bridge mode (MODE[2:0] = 011),                           Band” and Section 26.8 “Falling Edge and Forward
CWGxC is driven to its active state, CWGxA and                           Dead Band”. Steering modes are not used with either
CWGxD are driven to their inactive states, and CWGxB                     of the Full Bridge modes. The mode selection may be
is modulated by the input signal, as shown in                            toggled between forward and reverse toggling the
Figure 26-7.                                                             MODE[0] bit of the CWGxCON0 while keeping
                                                                         MODE[2:1] static, without disabling the CWG module.

FIGURE 26-7:                    EXAMPLE OF FULL-BRIDGE OUTPUT
           Forw ard
            M ode
                                         Period


         C W G 1A (2)


         C W G 1B (2)


         C W G 1C (2)
                          Pulse W idth


         C W G 1D (2)

                          (1)                                  (1)


           R everse
            M ode
                                          Period


        C W G 1A (2)
                          Pulse W idth


        C W G 1B (2)


        C W G 1C (2)


        C W G 1D (2)

                          (1)                                  (1)


        N ote 1:        A rising C W G data inputcreates a rising eventon the m odulated output.
              2:        O utputsignals show n as active-high;allPO Ly bits are clear.


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 412
                       PIC18(L)F26/27/45/46/47/55/56/57K42
26.2.3.1      Direction Change in Full Bridge                The dead-band delay is inserted only when changing
              Mode                                           directions, and only the modulated output is affected.
                                                             The statically-configured outputs (CWGxA and
In Full Bridge mode, changing MODE[2:0] controls the
                                                             CWGxC) are not afforded dead band, and switch
forward/reverse direction. Changes to MODE[2:0]
                                                             essentially simultaneously.
change to the new direction on the next rising edge of
the modulated input.                                         Figure 26-8 shows an example of the CWG outputs
                                                             changing directions from forward to reverse, at near
A direction change is initiated in software by changing
                                                             100% duty cycle. In this example, at time t1, the output
the MODE[2:0] bits of the CWGxCON0 register. The
                                                             of CWGxA and CWGxD become inactive, while output
sequence is illustrated in Figure 26-8.
                                                             CWGxC becomes active. Since the turn-off time of the
• The associated active output CWGxA and the                 power devices is longer than the turn-on time, a shoot-
  inactive output CWGxC are switched to drive in             through current will flow through power devices QC and
  the opposite direction.                                    QD for the duration of ‘t’. The same phenomenon will
• The previously modulated output CWGxD is                   occur to power devices QA and QB for the CWG
  switched to the inactive state, and the previously         direction change from reverse to forward.
  inactive output CWGxB begins to modulate.
                                                             When changing the CWG direction at high duty cycle is
• CWG modulation resumes after the direction-
                                                             required for an application, two possible solutions for
  switch dead band has elapsed.
                                                             eliminating the shoot-through current are:
26.2.3.2      Dead-Band Delay in Full Bridge                 1. Reduce the CWG duty cycle for one period
              Mode                                                before changing directions.
                                                             2. Use switch drivers that can drive the switches off
Dead-band delay is important when either of the
                                                                  faster than they can drive them on.
following conditions is true:
1.   The direction of the CWG output changes when
     the duty cycle of the data input is at or near
     100%, or
2.   The turn-off time of the power switch, including
     the power device and driver circuit, is greater
     than the turn-on time.

FIGURE 26-8:            EXAMPLE OF PWM DIRECTION CHANGE AT NEAR 100% DUTY CYCLE
                                                              t1
                                           Forw ard Period                   R everse Period


                      C W G 1A


                      C W G 1B                                               Pulse W idth


                      C W G 1C


                      C W G 1D              Pulse W idth
                                                                   TO N

             ExternalSw itch C
                                                                     TO FF

             ExternalSw itch D


              PotentialShoot-                                                 T = TO FF -TO N
              Through C urrent


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 413
                      PIC18(L)F26/27/45/46/47/55/56/57K42
26.2.4       STEERING MODES                                26.2.4.1     Synchronous Steering Mode
In both Synchronous and Asynchronous Steering              In Synchronous Steering mode (MODE[2:0] bits = 001,
modes, the modulated input signal can be steered to        Register 26-1), changes to steering selection registers
any combination of four CWG outputs and a fixed-value      take effect on the next rising edge of the modulated
will be presented on all the outputs not used for the      data input (Figure 26-9). In Synchronous Steering
PWM output. Each output has independent polarity,          mode, the output will always produce a complete
steering, and shutdown options. Dead-band control is       waveform.
not used in either steering mode.
When       STRx = 0    (Register 26-5),       then   the
corresponding pin is held at the level defined by OVRx
(Register 26-5). When STRx = 1, then the pin is driven
by the modulated input signal.
The POLx bits (Register 26-2) control the signal
polarity only when STRx = 1.
The CWG auto-shutdown operation also applies to
steering     modes    as    described      in    Section
26.14 “Register Definitions: CWG Control”.

  Note:      Only the STRx bits are synchronized; the
             SDATx (data) bits are not synchronized.
The CWG auto-shutdown operation also applies in
Steering modes as described in Section 26.10 “Auto-
Shutdown””. An auto-shutdown event will only affect
pins that have STRx = 1.

FIGURE 26-9:           EXAMPLE OF SYNCHRONOUS STEERING (MODE[2:0] = 001)

           CW G 1
           clock

            Input
           source


          C W G 1A


          C W G 1B


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 414
                       PIC18(L)F26/27/45/46/47/55/56/57K42
26.2.4.2      Asynchronous Steering Mode
In Asynchronous mode (MODE[2:0] bits = 000,
Register 26-1), steering takes effect at the end of the
instruction cycle that writes to STR. In Asynchronous
Steering mode, the output signal may be an incomplete
waveform (Figure 26-10). This operation may be useful
when the user firmware needs to immediately remove
a signal from the output pin.

FIGURE 26-10:           EXAMPLE OF ASYNCHRONOUS STEERING (MODE[2:0] = 000)

                     CW G 1
                     IN PU T
                               End ofInstruction C ycle                                          End ofInstruction C ycle

                     STR A


                    C W G 1A


                                                          C W G 1A Follow s C W G 1 data input


26.2.4.3      Start-up Considerations
The application hardware must use the proper external
pull-up and/or pull-down resistors on the CWG output
pins. This is required because all I/O pins are forced to
high-impedance at Reset.
The POLy bits (Register 26-2) allow the user to choose
whether the output signals are active-high or active-
low.


 2017-2021 Microchip Technology Inc.                                                                                       DS40001919G-page 415
                        PIC18(L)F26/27/45/46/47/55/56/57K42

FIGURE 26-11:               SIMPLIFIED CWG BLOCK DIAGRAM (OUTPUT STEERING MODES)

                                                                                                             Rev. 10-000211D
                                                                                                                    5/30/2017

           MODE<2:0> = 000: Asynchronous                                                 LSAC<1:0>
           MODE<2:0> = 001: Synchronous

                                                                                   ‘1’      00
                                                                                   ‘0’      01
                                                                             High-Z         10
                                                                                            11

                                                     CWG Data A                                          1
                                                                               1
                                                         POLA                                            0 CWG1A
                                                                               0
                                                                  OVRA

                                                                      STRA               LSBD<1:0>


                                                                                   ‘1’      00
                                                                                   ‘0’      01
                                              CWG
            CWG Data                          Data                           High-Z         10
              Input
                                                                                            11

                               D   Q                 CWG Data B
                                                                                                         1
                               E                                               1
                                                         POLB                                            0 CWG1B
                                                                               0
                                                                  OVRB
           EN
                                                                      STRB               LSAC<1:0>


                                                                                   ‘1’      00
                                                                                   ‘0’      01
                                                                             High-Z         10
                                                                                            11

                                                     CWG Data C                                          1
     Auto-shutdown source                 S   Q                                1
      (CWGxAS1 register)                                 POLC                                            0 CWG1C
                                          R                                    0
                                                                  OVRC

                 REN                                                  STRC               LSBD<1:0>
        SHUTDOWN = 0

                                                                                   ‘1’      00
                                                                                   ‘0’      01
                                                                             High-Z         10
                                                                                            11

                                                     CWG Data D
                                                                                                         1
                                                                               1
                                                         POLD                                            0 CWG1D
                                                                               0
                                                                  OVRD
                                       SHUTDOWN
                                                                             STRD
                                          FREEZE
                                                                  D   Q
                                                     CWG Data


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 416
                      PIC18(L)F26/27/45/46/47/55/56/57K42
26.3     Clock Source                                      26.5     Output Control
The clock source is used to drive the dead-band timing     26.5.1      CWG OUTPUTS
circuits. The CWG module allows the following clock
sources to be selected:                                    Each CWG output can be routed to a Peripheral Pin
                                                           Select (PPS) output via the RxyPPS register (see Sec-
• FOSC (system clock)                                      tion 17.0 “Peripheral Pin Select (PPS) Module”).
• HFINTOSC
When the HFINTOSC is selected, the HFINTOSC will           26.5.2      POLARITY CONTROL
be kept running during Sleep. Therefore, CWG modes         The polarity of each CWG output can be selected
requiring dead band can operate in Sleep, provided         independently. When the output polarity bit is set, the
that the CWG data input is also active during Sleep.The    corresponding output is active-high. Clearing the
clock sources are selected using the CS bit of the         output polarity bit configures the corresponding output
CWGxCLKCON register (Register 26-3). The system            as active-low. However, polarity does not affect the
clock FOSC, is disabled in Sleep and thus dead-band        override levels. Output polarity is selected with the
control cannot be used.                                    POLy bits of the CWGxCON1. Auto-shutdown and
                                                           steering options are unaffected by polarity.
26.4     Selectable Input Sources
The CWG generates the output waveforms from the            26.6     Dead-Band Control
following input sources:                                   The dead-band control provides nonoverlapping PWM
                                                           signals to prevent shoot-through current in PWM
TABLE 26-1:       SELECTABLE INPUT                         switches. Dead-band operation is employed for Half-
                                                           Bridge and Full Bridge modes. The CWG contains two
                  SOURCES
                                                           6-bit dead-band counters. One is used for the rising
  Source                                                   edge of the input source control in Half Bridge mode or
                     Signal Name            ISM[2:0]
 Peripheral                                                for reverse dead-band Full Bridge mode. The other is
               Pin selected by                             used for the falling edge of the input source control in
CWGxPPS                                        000         Half Bridge mode or for forward dead band in Full
               CWGxPPS
                                                           Bridge mode.
CCP1           CCP1 Output                     001
                                                           Dead band is timed by counting CWG clock periods
CCP2           CCP2 Output                     010         from zero up to the value in the rising or falling dead-
PWM3           PWM3 Output                     011         band counter registers. See CWGxDBR and
PWM4           PWM4 Output                     100         CWGxDBF registers, respectively.

CMP1           Comparator 1 Output             101         26.6.1      DEAD-BAND FUNCTIONALITY IN
CMP2           Comparator 2 Output             110                     HALF BRIDGE MODE
               Data signal modulator                       In Half Bridge mode, the dead-band counters dictate
DSM                                            111
               output                                      the delay between the falling edge of the normal output
                                                           and the rising edge of the inverted output. This can be
The input sources are selected using the IS[4:0] bits in
                                                           seen in Figure 26-2.
the CWGxISM register (Register 26-4).
                                                           26.6.2      DEAD-BAND FUNCTIONALITY IN
                                                                       FULL BRIDGE MODE
                                                           In Full Bridge mode, the dead-band counters are used
                                                           when undergoing a direction change. The MODE[0] bit
                                                           of the CWGxCON0 register can be set or cleared while
                                                           the CWG is running, allowing for changes from
                                                           Forward to Reverse mode. The CWGxA and CWGxC
                                                           signals will change immediately upon the first rising
                                                           input edge following a direction change, but the
                                                           modulated signals (CWGxB or CWGxD, depending on
                                                           the direction of the change) will experience a delay
                                                           dictated by the dead-band counters.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 417
                        PIC18(L)F26/27/45/46/47/55/56/57K42
26.7      Rising Edge and Reverse Dead
          Band
In Half Bridge mode, the rising edge dead band delays
the turn-on of the CWGxA output after the rising edge
of the CWG data input. In Full Bridge mode, the reverse
dead-band delay is only inserted when changing
directions from Forward mode to Reverse mode, and
only the modulated output CWGxB is affected.
The CWGxDBR register determines the duration of the
dead-band interval on the rising edge of the input
source signal. This duration is from 0 to 64 periods of
the CWG clock.
Dead band is always initiated on the edge of the input
source signal. A count of zero indicates that no dead
band is present.
If the input source signal reverses polarity before the
dead-band count is completed, then no signal will be
seen on the respective output.
The CWGxDBR register value is double-buffered.
When EN = 0 (Register 26-1), the buffer is loaded
when CWGxDBR is written. If EN = 1, then the buffer
will be loaded at the rising edge following the first falling
edge of the data input, after the LD bit (Register 26-1)
is set. Refer to Figure 26-12 for an example.

26.8      Falling Edge and Forward Dead
          Band
In Half Bridge mode, the falling edge dead band delays
the turn-on of the CWGxB output at the falling edge of
the CWG data input. In Full Bridge mode, the forward
dead-band delay is only inserted when changing
directions from Reverse mode to Forward mode, and
only the modulated output CWGxD is affected.
The CWGxDBF register determines the duration of the
dead-band interval on the falling edge of the input
source signal. This duration is from zero to 64 periods
of CWG clock.
Dead-band delay is always initiated on the edge of the
input source signal. A count of zero indicates that no
dead band is present.
If the input source signal reverses polarity before the
dead-band count is completed, then no signal will be
seen on the respective output.
The CWGxDBF register value is double-buffered.
When EN = 0 (Register 26-1), the buffer is loaded
when CWGxDBF is written. If EN = 1, then the buffer
will be loaded at the rising edge following the first
falling edge of the data input after the LD (Register 26-
1) is set. Refer to Figure 26-13 for an example.


 2017-2021 Microchip Technology Inc.                           DS40001919G-page 418
                                        FIGURE 26-12:   DEAD-BAND OPERATION, CWGxDBR = 0x01, CWGxDBF = 0x02
 2017-2021 Microchip Technology Inc.


                                          cwg_clock


                                                                                                                                             PIC18(L)F26/27/45/46/47/55/56/57K42
                                        Input Source


                                             CWGxA


                                             CWGxB


                                        FIGURE 26-13:   DEAD-BAND OPERATION, CWGxDBR = 0x03, CWGxDBF = 0x06, SOURCE SHORTER THAN DEAD BAND


                                           cwg_clock


                                         Input Source


                                             CWGxA
DS40001919G-page 419


                                             CWGxB

                                                                                                source shorter than dead band
                                                   PIC18(L)F26/27/45/46/47/55/56/57K42
26.9          Dead-Band Jitter
When the rising and falling edges of the input source
are asynchronous to the CWG clock, it creates jitter in
the dead-band time delay. The maximum jitter is equal
to one CWG clock period. Refer to Equation 26-1 for
more details.

EQUATION 26-1:                                       DEAD-BAND DELAY TIME
                                                     CALCULATION
                                                                    1
  T                                           = -----------------------------------------  D Bx  4:0>
      D EAD – BAN D _M IN                       F
                                                    C W G C LO C K
                                                                1
 T                                         = ----------------------------------------- D Bx  4:0>+1
     D EA D – BAN D M AX                     F
                                                 C W G C LO C K

 T
     JITTER
               = T
                       D EA D – BAN D _M AX
                                                                     – TD EAD – BAN D _M IN
                                     1
 T            = -------------------------------------------
     JITTER     F
                    C W G _C LO C K
 T                                            = T                                           +T
     D EAD – BAN D _M A X                              D EAD – BAN D _M IN                       JITTER


 EXAM PLE

 D BR<4:0> = 0x0A = 10

 F                             = 8 M Hz
     C W G _C LO C K
                  1
 T       = --------------- = 125 ns
  JITTER   8M H z
 T                                          = 125 ns*10 = 125 s
     D EAD – BAN D _M IN

 T                                           = 1.25 s + 0.125s= 1.37s
     D E AD – BAN D _M AX


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 420
                       PIC18(L)F26/27/45/46/47/55/56/57K42
26.10 Auto-Shutdown                                           26.10.1.3    Pin Override Levels
Auto-shutdown is a method to immediately override the         The levels driven to the CWG outputs during an auto-
CWG output levels with specific overrides that allow for      shutdown event are controlled by the LSBD[1:0] and
safe shutdown of the circuit. The shutdown state can be       LSAC[1:0] bits of the CWGxAS0 register (Register 26-
either cleared automatically or held until cleared by         6). The LSBD[1:0] bits control CWGxB/D output levels,
software. The auto-shutdown circuit is illustrated in         while the LSAC[1:0] bits control the CWGxA/C output
Figure 26-14.                                                 levels.

26.10.1     SHUTDOWN                                          26.10.1.4    Auto-Shutdown Interrupts
The shutdown state can be entered by either of the            When an auto-shutdown event occurs, either by
following two methods:                                        software or hardware setting SHUTDOWN, the
                                                              CWGxIF flag bit of the respective PIR register is set.
• Software generated
• External Input                                              26.11 Auto-Shutdown Restart
26.10.1.1     Software Generated Shutdown                     After an auto-shutdown event has occurred, there are
Setting the SHUTDOWN bit of the CWGxAS0 register              two ways to resume operation:
will force the CWG into the shutdown state.                   • Software controlled
When the auto-restart is disabled, the shutdown state         • Auto-restart
will persist as long as the SHUTDOWN bit is set.              In either case, the shutdown source must be cleared
                                                              before the restart can take place. That is, either the
When auto-restart is enabled, the SHUTDOWN bit will
                                                              shutdown condition must be removed, or the
clear automatically and resume operation on the next
                                                              corresponding ASxE bit must be cleared.
rising edge event. The SHUTDOWN bit indicates when
a shutdown condition exists. The bit may be set or
                                                              26.11.1     SOFTWARE-CONTROLLED
cleared in software or by hardware.
                                                                          RESTART
26.10.1.2     External Input Source                           If the REN bit of the CWGxAS0 register is clear
External shutdown inputs provide the fastest way to safely    (REN = 0), the CWG module must be restarted after an
suspend CWG operation in the event of a Fault condition.      auto-shutdown event through software.
When any of the selected shutdown inputs goes active,         Once all auto-shutdown sources are removed, the
the CWG outputs will immediately go to the specified          software must clear SHUTDOWN. Once SHUTDOWN
override levels without software delay. The override levels   is cleared, the CWG module will resume operation
are selected by the LSBD[1:0] and LSAC[1:0] bits of the       upon the first rising edge of the CWG data input.
CWGxAS0 register (Register 26-6). Several input
sources can be selected to cause a shutdown condition.
All input sources are active-low. The sources are:              Note:     The SHUTDOWN bit cannot be cleared in
                                                                          software if the auto-shutdown condition is
• Pin selected by CWGxPPS                                                 still present.
• Timer2 postscaled output
• Timer4 postscaled output                                    26.11.2     AUTO-RESTART
• Timer6 postscaled output                                    If the REN bit of the CWGxAS0 register is set (REN = 1),
• Comparator 1 output                                         the CWG module will restart from the shutdown state
• Comparator 2 output                                         automatically.
• CLC2 output                                                 Once all auto-shutdown conditions are removed, the
Shutdown input sources are individually enabled by the        hardware will automatically clear SHUTDOWN. Once
ASxE bits of the CWGxAS1 register (Register 26-7).            SHUTDOWN is cleared, the CWG module will resume
                                                              operation upon the first rising edge of the CWG data
  Note:     Shutdown inputs are level sensitive, not          input.
            edge sensitive. The shutdown state
            cannot be cleared, except by disabling
            auto-shutdown, as long as the shutdown              Note:     The SHUTDOWN bit cannot be cleared in
            input level persists.                                         software if the auto-shutdown condition is
                                                                          still present.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 421
                      PIC18(L)F26/27/45/46/47/55/56/57K42
26.12 Operation During Sleep                                26.13    Configuring the CWG
The CWG module operates independently from the              1.  Ensure that the TRIS control bits corresponding
system clock and will continue to run during Sleep,             to CWG outputs are set so that all are
provided that the clock and input sources selected              configured as inputs, ensuring that the outputs
remain active.                                                  are inactive during setup. External hardware
The HFINTOSC remains active during Sleep when all               may ensure that pin levels are held to safe
the following conditions are met:                               levels.
                                                            2. Clear the EN bit, if not already cleared.
• CWG module is enabled
                                                            3. Configure the MODE[2:0] bits of the CWGx-
• Input source is active                                        CON0 register to set the output operating mode.
• HFINTOSC is selected as the clock source,                 4. Configure the POLy bits of the CWGxCON1
  regardless of the system clock source selected.               register to set the output polarities.
In other words, if the HFINTOSC is simultaneously           5. Configure the ISM[4:0] bits of the CWGxISM
selected as system clock and CWG clock, when the                register to select the data input source.
CWG is enabled and the input source is active, then the     6. If a steering mode is selected, configure the
CPU will go Idle during Sleep, but the HFINTOSC will            STRx bits to select the desired output on the
remain active and the CWG will continue to operate.             CWG outputs.
This will have a direct effect on the Sleep mode current.   7. Configure the LSBD[1:0] and LSAC[1:0] bits of
                                                                the CWGxASD0 register to select the auto-
                                                                shutdown output override states (this is
                                                                necessary even if not using auto-shutdown
                                                                because start-up will be from a shutdown state).
                                                            8. If auto-restart is desired, set the REN bit of
                                                                CWGxAS0.
                                                            9. If auto-shutdown is desired, configure the ASxE
                                                                bits of the CWGxAS1 register to select the
                                                                shutdown source.
                                                            10. Set the desired rising and falling dead-band
                                                                times with the CWGxDBR and CWGxDBF
                                                                registers.
                                                            11. Select the clock source in the CWGxCLKCON
                                                                register.
                                                            12. Set the EN bit to enable the module.
                                                            13. Clear the TRIS bits that correspond to the CWG
                                                                outputs to set them as outputs.
                                                            If auto-restart is to be used, set the REN bit and the
                                                            SHUTDOWN bit will be cleared automatically.
                                                            Otherwise, clear the SHUTDOWN bit in software to
                                                            start the CWG.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 422
                                        FIGURE 26-14:        CWG SHUTDOWN BLOCK DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                     Write ‘1’ to                                                                                                                                     Rev. 10-000172E
                                                                                                                                                                                                             9/13/2016

                                                 SHUTDOWN bit
                                                     PPS
                                                         AS0E
                                            CWGxINPPS
                                                     CMP1_out


                                                                                                                                                                                                                         PIC18(L)F26/27/45/46/47/55/56/57K42
                                                         AS4E
                                                      CMP2_out
                                                         AS5E
                                                TMR2_postscaled                                                                            SHUTDOWN                                 S
                                                                                                                                S   Q
                                                          AS1E                                                                                                                D         Q   CWG_shutdown
                                                TMR4_postscaled
                                                                                               REN                                              FREEZE
                                                                                                                                R
                                                          AS2E                          Write ‘0’ to
                                                                                    SHUTDOWN bit
                                                TMR6_postscaled                                                                                                   CWG_data     CK
                                                          AS3E
                                                       CLC2_out
                                                          AS6E


                                        FIGURE 26-15: SHUTDOWN FUNCTIONALITY, AUTO-RESTART DISABLED (REN = 0, LSAC = 01, LSBD = 01)


                                                                                                        Shutdown Event Ceases           REN Cleared by Software


                                                         CWG Input
                                                           Source

                                                    Shutdown Source


                                                        SHUTDOWN


                                                           CWGxA                                             Tri-State (No Pulse)
                                                           CWGxC
DS40001919G-page 423


                                                           CWGxB                                             Tri-State (No Pulse)
                                                           CWGxD
                                                                      No Shutdown
                                                                                                  Shutdown                                                             Output Resumes
                                        FIGURE 26-16:       SHUTDOWN FUNCTIONALITY, AUTO-RESTART ENABLED (REN = 1, LSAC = 01, LSBD = 01)
 2017-2021 Microchip Technology Inc.


                                                                                             Shutdown Event Ceases   REN auto-cleared by hardware


                                                         CWG Input
                                                           Source

                                                  Shutdown Source


                                                                                                                                                    PIC18(L)F26/27/45/46/47/55/56/57K42
                                                        SHUTDOWN

                                                           CWGxA                         Tri-State (No Pulse)
                                                           CWGxC

                                                           CWGxB                         Tri-State (No Pulse)
                                                           CWGxD
                                                                       No Shutdown
                                                                                         Shutdown                          Output Resumes
DS40001919G-page 424
                        PIC18(L)F26/27/45/46/47/55/56/57K42
26.14 Register Definitions: CWG Control
Long bit name prefixes for the CWG peripheral is
shown below. Refer to Section 1.3.2.2 “Long Bit
Names” for more information.


          Peripheral               Bit Name Prefix
             CWG1                        CWG1
             CWG2                        CWG2
             CWG3                        CWG3
                                                                  l
REGISTER 26-1:           CWGxCON0: CWG CONTROL REGISTER 0
   R/W-0/0         R/W/HC-0/0           U-0             U-0           U-0      R/W-0/0          R/W-0/0      R/W-0/0
        EN             LD(1)            —               —             —                     MODE[2:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         HC = Bit is cleared by hardware


bit 7              EN: CWGx Enable bit
                   1 = Module is enabled
                   0 = Module is disabled
bit 6              LD: CWGx Load Buffers bit(1)
                   1 = Dead-band count buffers to be loaded on CWG data rising edge, following first falling edge after
                       this bit is set
                   0 = Buffers remain unchanged
bit 5-3            Unimplemented: Read as ‘0’
bit 2-0            MODE[2:0]: CWGx Mode bits
                   111 = Reserved
                   110 = Reserved
                   101 = CWG outputs operate in Push Pull mode
                   100 = CWG outputs operate in Half Bridge mode
                   011 = CWG outputs operate in Reverse Full Bridge mode
                   010 = CWG outputs operate in Forward Full Bridge mode
                   001 = CWG outputs operate in Synchronous Steering mode
                   000 = CWG outputs operate in Asynchronous Steering mode

Note 1:      This bit can only be set after EN = 1; it cannot be set in the same cycle when EN is set.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 425
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 26-2:           CWGxCON1: CWG CONTROL REGISTER 1
        U-0             U-0             R-x              U-0     R/W-0/0       R/W-0/0          R/W-0/0      R/W-0/0
        —               —               IN               —        POLD          POLC            POLB          POLA
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         q = Value depends on condition


bit 7-6            Unimplemented: Read as ‘0’
bit 5              IN: CWG Input Value bit (read-only)
bit 4              Unimplemented: Read as ‘0’
bit 3              POLD: CWGxD Output Polarity bit
                   1 = Signal output is inverted polarity
                   0 = Signal output is normal polarity
bit 2              POLC: CWGxC Output Polarity bit
                   1 = Signal output is inverted polarity
                   0 = Signal output is normal polarity
bit 1              POLB: CWGxB Output Polarity bit
                   1 = Signal output is inverted polarity
                   0 = Signal output is normal polarity
bit 0              POLA: CWGxA Output Polarity bit
                   1 = Signal output is inverted polarity
                   0 = Signal output is normal polarity


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 426
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 26-3:          CWGxCLK: CWGx CLOCK INPUT SELECTION REGISTER
        U-0            U-0              U-0              U-0        U-0           U-0              U-0          R/W-0/0
        —              —                —                 —         —              —                 —            CS
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared          q = Value depends on condition


bit 7-1            Unimplemented: Read as ‘0’
bit 0              CS: CWG Clock Source Selection bits

                             CS                          CWG1                 CWG2                       CWG3
                             1                HFINTOSC (1)           HFINTOSC (1)                HFINTOSC (1)
                           0        FOSC                     FOSC                                FOSC
                   Note 1: HFINTOSC remains operating during Sleep.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 427
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 26-4:           CWGxISM: CWGx INPUT SELECTION REGISTER
        U-0            U-0              U-0          R/W-0/0       R/W-0/0      R/W-0/0          R/W-0/0        R/W-0/0
        —               —               —                                       ISM[4:0]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared           q = Value depends on condition


bit 7-5            Unimplemented Read as ‘0’
bit 4-0            ISM[4:0]: CWG Data Input Selection Multiplexer Select bits

                                                      CWG1                    CWG2                       CWG3
                          ISM[4:0]
                                                 Input Selection         Input Selection             Input Selection
                       11111-10011            Reserved               Reserved                 Reserved
                             10010            CLC4_out               CLC4_out                 CLC4_out
                             10001            CLC3_out               CLC3_out                 CLC3_out
                             10000            CLC2_out               CLC2_out                 CLC2_out
                             01111            CLC1_out               CLC1_out                 CLC1_out
                             01110            DSM_out                DSM_out                  DSM_out
                             01101            CMP2OUT                CMP2OUT                  CMP2OUT
                             01100            CMP1OUT                CMP1OUT                  CMP1OUT
                             01011            NCO1OUT                NCO1OUT                  NCO1OUT
                       01010-01001            Reserved               Reserved                 Reserved
                             01000            PWM8OUT                PWM8OUT                  PWM8OUT
                             00111            PWM7OUT                PWM7OUT                  PWM7OUT
                             00110            PWM6OUT                PWM6OUT                  PWM6OUT
                             00101            PWM5OUT                PWM5OUT                  PWM5OUT
                             00100            CCP4_out               CCP4_out                 CCP4_out
                             00011            CCP3_out               CCP3_out                 CCP3_out
                             00010            CCP2_out               CCP2_out                 CCP2_out
                             00001            CCP1_out               CCP1_out                 CCP1_out
                             00000            Pin selected by        Pin selected by          Pin selected by
                                              CWG1PPS                CWG2PPS                  CWG3PPS


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 428
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 26-5:          CWGxSTR(1): CWG STEERING CONTROL REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0      R/W-0/0       R/W-0/0          R/W-0/0     R/W-0/0
    OVRD              OVRC          OVRB               OVRA     STRD(2)       STRC(2)          STRB(2)     STRA(2)
bit 7                                                                                                           bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared          q = Value depends on condition


bit 7              OVRD: Steering Data D bit
bit 6              OVRC: Steering Data C bit
bit 5              OVRB: Steering Data B bit
bit 4              OVRA: Steering Data A bit
bit 3              STRD: Steering Enable bit D(2)
                   1 = CWGxD output has the CWG data input waveform with polarity control from POLD bit
                   0 = CWGxD output is assigned to value of OVRD bit
bit 2              STRC: Steering Enable bit C(2)
                   1 = CWGxC output has the CWG data input waveform with polarity control from POLC bit
                   0 = CWGxC output is assigned to value of OVRC bit
bit 1              STRB: Steering Enable bit B(2)
                   1 = CWGxB output has the CWG data input waveform with polarity control from POLB bit
                   0 = CWGxB output is assigned to value of OVRB bit
bit 0              STRA: Steering Enable bit A(2)
                   1 = CWGxA output has the CWG data input waveform with polarity control from POLA bit
                   0 = CWGxA output is assigned to value of OVRA bit

Note 1:      The bits in this register apply only when MODE[2:0] = 00x (Register 26-1, Steering modes).
     2:      This bit is double-buffered when MODE[2:0] = 001.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 429
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 26-6:          CWGxAS0: CWG AUTO-SHUTDOWN CONTROL REGISTER 0
 R/W/HS/HC-0/0         R/W-0/0       R/W-0/0         R/W-1/1      R/W-0/0        R/W-1/1          U-0           U-0
  SHUTDOWN              REN                LSBD[1:0]                     LSAC[1:0]                  —           —
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         HS/HC = Bit is set/cleared by hardware
q = Value depends on condition


bit 7               SHUTDOWN: Auto-Shutdown Event Status bit(1,2)
                    1 = An auto-shutdown state is in effect
                    0 = No auto-shutdown event has occurred
bit 6               REN: Auto-Restart Enable bit
                    1 = Auto-restart is enabled
                    0 = Auto-restart is disabled
bit 5-4             LSBD[1:0]: CWGxB and CWGxD Auto-Shutdown State Control bits
                    11 = A logic ‘1’ is placed on CWGxB/D when an auto-shutdown event occurs.
                    10 = A logic ‘0’ is placed on CWGxB/D when an auto-shutdown event occurs.
                    01 = Pin is tri-stated on CWGxB/D when an auto-shutdown event occurs.
                    00 = The inactive state of the pin, including polarity, is placed on CWGxB/D after the required
                         dead-band interval when an auto-shutdown event occurs.
bit 3-2             LSAC[1:0]: CWGxA and CWGxC Auto-Shutdown State Control bits
                    11 = A logic ‘1’ is placed on CWGxA/C when an auto-shutdown event occurs.
                    10 = A logic ‘0’ is placed on CWGxA/C when an auto-shutdown event occurs.
                    01 = Pin is tri-stated on CWGxA/C when an auto-shutdown event occurs.
                    00 = The inactive state of the pin, including polarity, is placed on CWGxA/C after the required
                         dead-band interval when an auto-shutdown event occurs.
bit 1-0             Unimplemented: Read as ‘0’

Note 1:      This bit may be written while EN = 0 (Register 26-1), to place the outputs into the shutdown configuration.
     2:      The outputs will remain in auto-shutdown state until the next rising edge of the CWG data input after this
             bit is cleared.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 430
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 26-7:          CWGxAS1: CWG AUTO-SHUTDOWN CONTROL REGISTER 1
        U-0          R/W-0/0       R/W-0/0          R/W-0/0       R/W-0/0       R/W-0/0          R/W-0/0       R/W-0/0
        —             AS6E           AS5E               AS4E       AS3E          AS2E             AS1E            AS0E
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared           q = Value depends on condition


bit 7              Unimplemented Read as ‘0’
bit 6              AS6E: CWG Auto-shutdown Source 6 Enable bit
                   1 = Auto-shutdown for Source 6 is enabled
                               CWG Module                       CWG1               CWG2                    CWG3
                        Auto-shutdown Source 6                 CLC2 OUT          CLC3 OUT              CLC4 OUT

                   0 = Auto-shutdown for Source 6 is disabled
bit 5              AS5E: CWG Auto-shutdown Source 5 (CMP2 OUT) Enable bit
                   1 = Auto-shutdown for CMP2 OUT is enabled
                   0 = Auto-shutdown for CMP2 OUT is disabled
bit 4              AS4E: CWG Auto-shutdown Source 4 (CMP1 OUT) Enable bit
                   1 = Auto-shutdown for CMP1 OUT is enabled
                   0 = Auto-shutdown for CMP1 OUT is disabled
bit 3              AS3E: CWG Auto-shutdown Source 3 (TMR6_Postscaled) Enable bit
                   1 = Auto-shutdown for TMR6_Postscaled is enabled
                   0 = Auto-shutdown for TMR6_Postscaled is disabled
bit 2              AS2E: CWG Auto-shutdown Source 2 (TMR4_Postscaled) Enable bit
                   1 = Auto-shutdown for TMR4_Postscaled is enabled
                   0 = Auto-shutdown for TMR4_Postscaled is disabled
bit 1              AS1E: CWG Auto-shutdown Source 1 (TMR2_Postscaled) Enable bit
                   1 = Auto-shutdown for TMR2_Postscaled is enabled
                   0 = Auto-shutdown for TMR2_Postscaled is disabled
bit 0              AS0E: CWG Auto-shutdown Source 0 (Pin selected by CWGxPPS) Enable bit
                   1 = Auto-shutdown for CWGxPPS Pin is enabled
                   0 = Auto-shutdown for CWGxPPS Pin is disabled


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 431
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 26-8:          CWGxDBR: CWG RISING DEAD-BAND COUNT REGISTER
        U-0            U-0        R/W-x/u          R/W-x/u     R/W-x/u       R/W-x/u          R/W-x/u     R/W-x/u
        —              —                                              DBR[5:0]
bit 7                                                                                                          bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared         q = Value depends on condition


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            DBR[5:0]: CWG Rising Edge Triggered Dead-Band Count bits
                   11 1111 = 63-64 CWG clock periods
                   11 1110 = 62-63 CWG clock periods
                   .
                   .
                   .
                   00 0010 = 2-3 CWG clock periods
                   00 0001 = 1-2 CWG clock periods
                   00 0000 = 0 CWG clock periods. Dead-band generation is by-passed


REGISTER 26-9:          CWGxDBF: CWG FALLING DEAD-BAND COUNT REGISTER
        U-0            U-0        R/W-x/u          R/W-x/u     R/W-x/u       R/W-x/u          R/W-x/u     R/W-x/u
        —              —                                              DBF[5:0]
bit 7                                                                                                          bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared         q = Value depends on condition


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            DBF[5:0]: CWG Falling Edge Triggered Dead-Band Count bits
                   11 1111 = 63-64 CWG clock periods
                   11 1110 = 62-63 CWG clock periods
                   .
                   .
                   .
                   00 0010 = 2-3 CWG clock periods
                   00 0001 = 1-2 CWG clock periods
                   00 0000 = 0 CWG clock periods. Dead-band generation is by-passed.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 432
                      PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 26-2:        SUMMARY OF REGISTERS ASSOCIATED WITH CWG
                                                                                                                   Register
     Name             Bit 7         Bit 6       Bit 5        Bit 4      Bit 3       Bit 2      Bit 1       Bit 0
                                                                                                                   on Page
CWGxCON0              EN             LD          —                —      —                   MODE[2:0]               426
CWGxCON1               —             —           IN               —    POLD         POLC       POLB        POLA      427
CWGxCLK                —             —           —                —      —              —       —           CS       428
CWGxISM                —             —           —                                ISM[4:0]                           429
CWGxSTR              OVRD          OVRC        OVRB          OVRA      STRD         STRC       STRB        STRA      430
CWGxAS0           SHUTDOWN          REN               LSBD[1:0]            LSAC[1:0]            —           —        431
CWGxAS1                —           AS6E        AS5E          AS4E       AS3E        AS2E       AS1E        AS0E      432
CWGxDBR                —             —                                     DBR[5:0]                                  433
CWGxDBF                —             —                                       DBF[5:0]                                433
Legend:     – = unimplemented locations read as ‘0’. Shaded cells are not used by CWG.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 433
