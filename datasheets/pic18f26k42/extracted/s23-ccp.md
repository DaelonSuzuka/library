                       PIC18(L)F26/27/45/46/47/55/56/57K42
23.0     CAPTURE/COMPARE/PWM                                 23.1      CCP Module Configuration
         MODULE                                              Each Capture/Compare/PWM module is associated
The Capture/Compare/PWM module is a peripheral               with a control register (CCPxCON), a capture input
that allows the user to time and control different events,   selection register (CCPxCAP) and a data register
and to generate Pulse-Width Modulation (PWM)                 (CCPRx). The data register, in turn, is comprised of two
signals. In Capture mode, the peripheral allows the          8-bit registers: CCPRxL (low byte) and CCPRxH (high
timing of the duration of an event. The Compare mode         byte).
allows the user to trigger an external event when a
                                                             23.1.1      CCP MODULES AND TIMER
predetermined amount of time has expired. The PWM
mode can generate pulse-width modulated signals of                       RESOURCES
varying frequency and duty cycle.                            The CCP modules utilize Timers 1 through 6 that vary
This family of devices contains four standard Capture/       with the selected mode. Various timers are available to
Compare/PWM modules (CCP1, CCP2, CCP3 and                    the CCP modules in Capture, Compare or PWM
CCP4). Each individual CCP module can select the             modes, as shown in Table 23-1.
timer source that controls the module. Each module
has an independent timer selection which can be              TABLE 23-1:        CCP MODE – TIMER
accessed using the CxTSEL bits in the CCPTMRS                                   RESOURCE
register (Register 23-2). The default timer selection is      CCP Mode                   Timer Resource
TMR1 when using Capture/Compare mode and TMR2
when using PWM mode in the CCPx module.                      Capture
                                                                                    Timer1, Timer3 or Timer5
Please note that the Capture/Compare mode operation          Compare
is described with respect to TMR1 and the PWM mode
                                                             PWM                    Timer2, Timer4 or Timer6
operation is described with respect to TMR2 in the
following sections.                                          The assignment of a particular timer to a module is
The Capture and Compare functions are identical for all      determined by the timer to CCP enable bits in the
CCP modules.                                                 CCPTMRS register (see Register 23-2) All of the
                                                             modules may be active at once and may share the
   Note 1: In devices with more than one CCP                 same timer resource if they are configured to operate
           module, it is very important to pay close         in the same mode (Capture/Compare or PWM) at the
           attention to the register names used. A           same time.
           number placed after the module acronym
           is used to distinguish between separate           23.1.2      OPEN-DRAIN OUTPUT OPTION
           modules. For example, the CCP1CON
                                                             When operating in Output mode (the Compare or PWM
           and CCP2CON control the same
                                                             modes), the drivers for the CCPx pins can be optionally
           operational aspects of two completely
                                                             configured as open-drain outputs. This feature allows
           different CCP modules.
                                                             the voltage level on the pin to be pulled to a higher level
         2: Throughout      this   section,     generic      through an external pull-up resistor and allows the
            references to a CCP module in any of its         output to communicate with external circuits without the
            operating modes may be interpreted as            need for additional level shifters.
            being equally applicable to CCPx module.
            Register names, module signals, I/O pins,          Note:     The voltage on the pin may not exceed the
            and bit names may use the generic                            maximum recommended voltage level for
            designator ‘x’ to indicate the use of a                      that pin.
            numeral to distinguish a particular module,
            when required.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 342
                      PIC18(L)F26/27/45/46/47/55/56/57K42
23.2      Capture Mode                                     23.2.1     CAPTURE SOURCES
Capture mode makes use of the 16-bit Timer1                In Capture mode, the CCPx pin may be configured as
resource. When an event occurs on the capture              an input by setting the associated TRIS control bit.
source, the 16-bit CCPRxH:CCPRxL register pair               Note:    If the CCPx pin is configured as an output,
captures and stores the 16-bit value of the                           a write to the port can cause a capture
TMRxH:TMRxL register pair, respectively. An event is                  condition.
defined as one of the following and is configured by the
MODE[3:0] bits of the CCPxCON register:                    The capture source is selected by configuring the
                                                           CTS[2:0] bits of the CCPxCAP register. Refer to
• Every falling edge of CCPx input
                                                           CCPxCAP register (Register 23-3) for a list of sources
• Every rising edge of CCPx input                          that can be selected.
• Every 4th rising edge of CCPx input
• Every 16th rising edge of CCPx input                     23.2.2     TIMER1 MODE RESOURCE
• Every edge of CCPx input (rising or falling)             Timer1 must be running in Timer mode or Synchronized
When a capture is made, the Interrupt Request Flag bit     Counter mode for the CCP module to use the capture
CCPxIF of the respective PIR register is set. The          feature. In Asynchronous Counter mode, the capture
interrupt flag must be cleared in software. If another     operation may not work.
capture occurs before the value in the                     • See Section 21.0 “Timer1/3/5 Module with Gate
CCPRxH:CCPRxL register pair is read, the old                 Control” for more information on configuring
captured value is overwritten by the new captured            Timer1.
value.

                                                             Note:    Clocking Timer1 from the system clock
  Note:     If an event occurs during a 2-byte read,                  (FOSC) may not be used in Capture mode.
            the high and low-byte data will be from                   In order for Capture mode to recognize
            different events. It is recommended while                 the trigger event on the CCPx pin, Timer1
            reading the CCPRxH:CCPRxL register                        must be clocked from the instruction clock
            pair to either disable the module or read                 (FOSC/4) or from an external clock source.
            the register pair twice for data integrity.
Figure 23-1 shows a simplified diagram of the capture
operation.


 2017-2021 Microchip Technology Inc.                                                     DS40001919G-page 343
                         PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 23-1:             CAPTURE MODE OPERATION BLOCK DIAGRAM


                                                                                                   Rev. 10-000158J
                                                                                                         9/13/2016
                                                                                RxyPPS
                                                                                                   CCPx
                          CTS<2:0>

                                                                                         TRIS Control
            CLC4_out        111
            CLC3_out        110                                                   CCPRxH     CCPRxL
            CLC2_out        101                                                             16
                                                                   set CCPxIF
            CLC1_out        100         Prescaler       and
         IOC_interrupt      011          1,4,16      Edge Detect
                                                                                            16
            CMP2_out        010
            CMP1_out        001               MODE <3:0>                          TMR1H       TMR1L
 CCPx            PPS        000


              CCPxPPS


 2017-2021 Microchip Technology Inc.                                               DS40001919G-page 344
                       PIC18(L)F26/27/45/46/47/55/56/57K42
23.2.3      SOFTWARE INTERRUPT MODE                            23.3        Compare Mode
When the Capture mode is changed, a false capture              Compare mode makes use of the 16-bit Timer1
interrupt may be generated. The user may keep the              resource. The 16-bit value of the CCPRxH:CCPRxL
CCPxIE Interrupt Priority bit of the respective PIE            register pair is constantly compared against the 16-bit
register clear to avoid false interrupts. Additionally, the    value of the TMRxH:TMRxL register pair. When a
user may clear the CCPxIF interrupt flag bit of the            match occurs, one of the following events can occur:
respective PIR register following any change in
Operating mode.                                                • Toggle the CCPx output, clear TMRx
                                                               • Toggle the CCPx output
23.2.4      CAPTURE DURING SLEEP                               • Set the CCPx output
Capture mode depends upon the Timer1 module for                • Clear the CCPx output
proper operation. There are two options for driving the        • Pulse output(1)
Timer1 module in Capture mode. It can be driven by the         • Pulse output, clear TMRx
instruction clock (FOSC/4), or by an external clock source.
                                                                    Note 1: The pulse output goes high at the rising
When Timer1 is clocked by FOSC/4, Timer1 will not                           edge of the timer clock where the CCP
increment during Sleep. When the device wakes from                          match occurs and lasts until the rising
Sleep, Timer1 will continue from its previous state.                        edge of the next timer clock. The pulse
Capture mode will operate during Sleep as long as the                       output also goes low if the timer is written
clock source for Timer1 is active in Sleep.                                 to before the second clock edge occurs.
                                                               The action on the pin is based on the value of the
                                                               MODE[3:0] control bits of the CCPxCON register. At
                                                               the same time, the interrupt flag CCPxIF bit is set, and
                                                               an ADC conversion can be triggered, if selected.
                                                               All Compare modes can generate an interrupt and
                                                               trigger an ADC conversion. When MODE = 0b0001 or
                                                               0b1011, the CCP resets the TMR register pair.
                                                               Figure 23-2 shows a simplified diagram of the compare
                                                               operation.

FIGURE 23-2:            COMPARE MODE OPERATION BLOCK DIAGRAM

                                                                                                            Rev. 10-000159C
                                                                                                                   5/26/2016


                                                                            To Peripherals
            CCPRxH      CCPRxL
                                                                                                        CCPx_out
                                      set CCPxIF
                                                     Output     S      Q       PPS                      CCPx Pin
                 Comparator
                                                     Logic
                                                                R                            TRIS Control
                                                      4                      RxyPPS
             TMR1H       TMR1L                     MODE<3:0>


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 345
                      PIC18(L)F26/27/45/46/47/55/56/57K42
23.3.1      CCPx PIN CONFIGURATION                        23.4      PWM Overview
The software must configure the CCPx pin as an output     Pulse-Width Modulation (PWM) is a scheme that
by clearing the associated TRIS bit and defining the      provides power to a load by switching quickly between
appropriate output pin through the RxyPPS registers.      fully ON and fully OFF states. The PWM signal
See Section 17.0 “Peripheral Pin Select (PPS)             resembles a square wave where the high portion of the
Module” for more details.                                 signal is considered the ON state and the low portion of
                                                          the signal is considered the OFF state. The high portion,
                                                          also known as the pulse width, can vary in time and is
  Note:     Clearing the CCPxCON register will force      defined in steps. A larger number of steps applied, which
            the CCPx compare output latch to the          lengthens the pulse width, also supplies more power to
            default low level. This is not the PORT I/O   the load. Lowering the number of steps applied, which
            data latch.                                   shortens the pulse width, supplies less power. The PWM
                                                          period is defined as the duration of one complete cycle
23.3.2      TIMER1 MODE RESOURCE                          or the total amount of on and off time combined.
In Compare mode, Timer1 must be running in either         PWM resolution defines the maximum number of steps
Timer mode or Synchronized Counter mode. The              that can be present in a single PWM period. A higher
compare operation may not work in Asynchronous            resolution allows for more precise control of the pulse-
Counter mode.                                             width time and in turn the power that is applied to the
See Section 21.0 “Timer1/3/5 Module with Gate             load.
Control” for more information on configuring Timer1.      The term duty cycle describes the proportion of the on
  Note:     Clocking Timer1 from the system clock         time to the off time and is expressed in percentages,
            (FOSC) may not be used in Compare             where 0% is fully off and 100% is fully on. A lower duty
            mode. In order for Compare mode to            cycle corresponds to less power applied and a higher
            recognize the trigger event on the CCPx       duty cycle corresponds to more power applied.
            pin, TImer1 must be clocked from the          Figure 23-3 shows a typical waveform of the PWM
            instruction clock (FOSC/4) or from an         signal.
            external clock source.
                                                          23.4.1        STANDARD PWM OPERATION
23.3.3      AUTO-CONVERSION TRIGGER                       The standard PWM mode generates a Pulse-Width
All CCPx modes set the CCP interrupt flag (CCPxIF).       Modulation (PWM) signal on the CCPx pin with up to
When this flag is set and a match occurs, an auto-        ten bits of resolution. The period, duty cycle, and
conversion trigger can take place if the CCP module is    resolution are controlled by the following registers:
selected as the conversion trigger source.                • T2PR registers
Refer to Section 36.2.5 “Auto-Conversion Trigger”         • T2CON registers
for more information.                                     • CCPRxL and CCPRxH registers
  Note:     Removing the match condition by               • CCPxCON registers
            changing the contents of the CCPRxH           It is required to have FOSC/4 as the clock input to
            and CCPRxL register pair, between the         TMR2/4/6 for correct PWM operation. Figure 23-4
            clock edge that generates the Auto-           shows a simplified block diagram of PWM operation.
            conversion Trigger and the clock edge
            that generates the Timer1 Reset, will           Note:       The corresponding TRIS bit must be
            preclude the Reset from occurring                           cleared to enable the PWM output on the
                                                                        CCPx pin.
23.3.4      COMPARE DURING SLEEP
Since FOSC is shut down during Sleep mode, the            FIGURE 23-3:                 CCP PWM OUTPUT SIGNAL
Compare mode will not function properly during Sleep,                              Period                                  Rev. 10-000023E


unless the timer is running. The device will wake on
                                                                                                                                  9/13/2016


interrupt (if enabled).                                             Pulse Width
                                                                                                          T2TMR = T2PR
                                                                                                          T2TMR reloaded with 0

                                                                                     T2TMR = Duty Cycle =
                                                                                     PWMxDCH<7:0>:PWMxDCL<7:6>
                                                                     T2TMR = T2PR
                                                                     T2TMR reloaded with 0


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 346
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 23-4:           SIMPLIFIED PWM BLOCK DIAGRAM

                                                                                                                                 Rev. 10-000157D

                               Duty cycle registers                                                                                     9/13/2016


                           CCPRxH           CCPRxL
                                                                                                CCPx_out
                                                                                                                   To Peripherals
                                                                                                           set CCPxIF
                                10-bit Latch(2)
                           (Not accessible by user)


                                  Comparator                           R       Q                PPS                           CCPx


                                                                       S                      RxyPPS
                      TMR2 Module                                                                                   TRIS Control

                                              R
                                  T2TMR               (1)


                                            ERS logic
                                Comparator                         CCPx_pset


                                    T2PR


                      Notes:     1. 8-bit timer is concatenated with two bits generated by Fosc or two bits of the internal prescaler to
                                    create 10-bit time-base.
                                 2. The alignment of the 10 bits from the CCPR register is determined by the CCPxFMT bit.


 2017-2021 Microchip Technology Inc.                                                                                 DS40001919G-page 347
                        PIC18(L)F26/27/45/46/47/55/56/57K42
23.4.2       SETUP FOR PWM OPERATION                           23.4.4     PWM PERIOD
The following steps may be taken when configuring the          The PWM period is specified by the T2PR register of
CCP module for standard PWM operation:                         Timer2. The PWM period can be calculated using the
1.    Use the desired output pin RxyPPS control to             formula of Equation 23-1.
      select CCPx as the source and disable the
      CCPx pin output driver by setting the associated         EQUATION 23-1:        PWM PERIOD
      TRIS bit.
                                                                    PW M Period =   T2PR  + 1  4  TO SC 
2.    Load the T2PR register with the PWM period
      value.                                                                        (TM R2 Prescale Value)
3.    Configure the CCP module for the PWM mode
      by loading the CCPxCON register with the                      Note 1:    TOSC = 1/FOSC
      appropriate values.
                                                               When T2TMR is equal to T2PR, the following three
4.    Load the CCPRxL register, and the CCPRxH
                                                               events occur on the next increment cycle:
      register with the PWM duty cycle value and
      configure the FMT bit of the CCPxCON register            • T2TMR is cleared
      to set the proper register alignment.                    • The CCPx pin is set. (Exception: If the PWM duty
5.    Configure and start Timer2:                                cycle = 0%, the pin will not be set.)
      • Clear the TMR2IF interrupt flag bit of the             • The PWM duty cycle is transferred from the
         respective PIR register. See Note below.                CCPRxL/H register pair into a 10-bit buffer.
      • Select the timer clock source to be as
         FOSC/4 using the T2CLK register. This is                Note:    The Timer postscaler (see Section
         required for correct operation of the PWM                        22.3 “External Reset Sources”) is not
         module.                                                          used in the determination of the PWM
      • Configure the CKPS bits of the T2CON                              frequency.
         register with the Timer prescale value.
      • Enable the Timer by setting the ON bit of
         the T2CON register.
6.    Enable PWM output pin:
      • Wait until the Timer overflows and the
         TMR2IF bit of the PIR4 register is set. See
         Note below.
      • Enable the CCPx pin output driver by
         clearing the associated TRIS bit.


     Note:   In order to send a complete duty cycle and
             period on the first PWM output, the above
             steps must be included in the setup
             sequence. If it is not critical to start with a
             complete PWM signal on the first output,
             then step 6 may be ignored.

23.4.3       TIMER2 TIMER RESOURCE
The PWM standard mode makes use of the 8-bit
Timer2 timer resources to specify the PWM period.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 348
                                         PIC18(L)F26/27/45/46/47/55/56/57K42
23.4.5               PWM DUTY CYCLE                                                                      23.4.6         PWM RESOLUTION
The PWM duty cycle is specified by writing a 10-bit                                                      The resolution determines the number of available duty
value to the CCPRxH:CCPRxL register pair. The                                                            cycles for a given period. For example, a 10-bit resolution
alignment of the 10-bit value is determined by the FMT                                                   will result in 1024 discrete duty cycles, whereas an 8-bit
bit of the CCPxCON register (see Figure 23-5). The                                                       resolution will result in 256 discrete duty cycles.
CCPRxH:CCPRxL register pair can be written to at any                                                     The maximum PWM resolution is ten bits when T2PR
time; however the duty cycle value is not latched into                                                   is 255. The resolution is a function of the T2PR register
the 10-bit buffer until after a match between T2PR and                                                   value as shown by Equation 23-4.
T2TMR.
Equation 23-2 is used to calculate the PWM pulse                                                         EQUATION 23-4:                    PWM RESOLUTION
width. Equation 23-3 is used to calculate the PWM duty
cycle ratio.
                                                                                                                                log 4 T2PR + 1 
                                                                                                                   Resolution = --------------------------------------------- bits
                                                                                                                                               log 2
FIGURE 23-5:                               PWM 10-BIT ALIGNMENT
                                                                                Rev. 10-000 160A
                                                                                       12/9/201 3


                CCPRxH                              CCPRxL                                                 Note:        If the pulse-width value is greater than the
           7 6 5 4 3 2 1 0                     7 6 5 4 3 2 1 0                   FMT = 0                                period, the assigned PWM pin(s) will
                                                                                                                        remain unchanged.
                                      CCPRxH                              CCPRxL
          FMT = 1               7 6 5 4 3 2 1 0                     7 6 5 4 3 2 1 0


                                      10-bit Duty Cycle
                                    9 8 7 6 5 4 3 2 1 0


EQUATION 23-2:                             PULSE WIDTH

   Pulse W idth =  CCPRxH :CCPRxL register pair 
                                     TO SC  (TM R2 Prescale Value)


EQUATION 23-3:                             DUTY CYCLE RATIO

                      CCPRxH :CCPRxL register pair
 D uty Cycle Ratio = ---------------------------------------------------------------------------------
                                              4 T2PR + 1


CCPRxH:CCPRxL register pair are used to double
buffer the PWM duty cycle. This double buffering
provides glitchless PWM operation.
The 8-bit timer T2TMR register is concatenated with
either the 2-bit internal system clock (FOSC), or two bits
of the prescaler, to create the 10-bit time base. The
system clock is used if the Timer2 prescaler is set to 1:1.
When the 10-bit time base matches the
CCPRxH:CCPRxL register pair, then the CCPx pin is
cleared (see Figure 23-4).


 2017-2021 Microchip Technology Inc.                                                                                                                     DS40001919G-page 349
                        PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 23-2:         EXAMPLE PWM FREQUENCIES AND RESOLUTIONS (FOSC = 20 MHz)
       PWM Frequency                  1.22 kHz        4.88 kHz   19.53 kHz   78.12 kHz   156.3 kHz    208.3 kHz
Timer Prescale                           16               4         1           1            1           1
T2PR Value                              0xFF            0xFF       0xFF        0x3F        0x1F         0x17
Maximum Resolution (bits)                10               10        10          8            7           6.6

TABLE 23-3:         EXAMPLE PWM FREQUENCIES AND RESOLUTIONS (FOSC = 8 MHz)
       PWM Frequency                  1.22 kHz        4.90 kHz   19.61 kHz   76.92 kHz   153.85 kHz   200.0 kHz
Timer Prescale                           16               4         1           1            1           1
T2PR Value                              0x65            0x65       0x65        0x19        0x0C         0x09
Maximum Resolution (bits)                 8               8         8           6            5           5

23.4.7       OPERATION IN SLEEP MODE
In Sleep mode, the T2TMR register will not increment
and the state of the module will not change. If the CCPx
pin is driving a value, it will continue to drive that value.
When the device wakes up, T2TMR will continue from
its previous state.

23.4.8       CHANGES IN SYSTEM CLOCK
             FREQUENCY
The PWM frequency is derived from the system clock
frequency. Any changes in the system clock frequency
will result in changes to the PWM frequency. See Sec-
tion 7.0 “Oscillator Module (with Fail-Safe Clock
Monitor)” for additional details.

23.4.9       EFFECTS OF RESET
Any Reset will force all ports to Input mode and the
CCP registers to their Reset states.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 350
                         PIC18(L)F26/27/45/46/47/55/56/57K42
23.5       Register Definitions: CCP Control
Long bit name prefixes for the CCP peripherals are
shown below. Refer to Section 1.3.2.2 “Long Bit
Names” for more information.


           Peripheral                  Bit Name Prefix
               CCP1                           CCP1
               CCP2                           CCP2
               CCP3                           CCP3
               CCP4                           CCP4

REGISTER 23-1:            CCPxCON: CCPx CONTROL REGISTER
    R/W-0/0              U-0               R-x               R/W-0/0         R/W-0/0             R/W-0/0         R/W-0/0           R/W-0/0
          EN              —               OUT                 FMT                                        MODE[3:0]
bit 7                                                                                                                                    bit 0


Legend:
R = Readable bit                     W = Writable bit                    U = Unimplemented bit, read as ‘0’
-n = Value at POR                    ‘1’ = Bit is set                    ‘0’ = Bit is cleared                 x = Bit is unknown


bit 7               EN: CCP Module Enable bit
                    1 = CCP is enabled
                    0 = CCP is disabled
bit 6               Unimplemented: Read as ‘0’
bit 5               OUT: CCPx Output Data bit (read-only)
bit 4               FMT: CCPW (pulse-width) Alignment bit
                    MODE = Capture mode:
                    Unused
                    MODE = Compare mode:
                    Unused
                    MODE = PWM mode:
                    1 = Left-aligned format
                    0 = Right-aligned format
bit 3-0             MODE[3:0]: CCPx Mode Select bits

                            MODE              Operating Mode                              Operation                           Set CCPxIF
                              11xx                  PWM           PWM operation                                                    Yes
                              1011                                Pulse output; clear TMR1(2)                                      Yes
                              1010                                Pulse output                                                     Yes
                                                  Compare
                              1001                                Clear output(1)                                                  Yes
                              1000                                Set output(1)                                                    Yes
                              0111                                Every 16th rising edge of CCPx input                             Yes
                              0110                                Every 4th rising edge of CCPx input                              Yes
                              0101                 Capture        Every rising edge of CCPx input                                  Yes
                              0100                                Every falling edge of CCPx input                                 Yes
                              0011                                Every edge of CCPx input                                         Yes
                              0010                                Toggle output                                                    Yes
                                                  Compare
                              0001                                Toggle output; clear TMR1(2)                                     Yes
                              0000                 Disabled                                                                         —


Note 1:        The set and clear operations of the Compare mode are reset by setting MODE = 4’b0000 or EN = 0.
     2:        When MODE = 0001 or 1011, then the timer associated with the CCP module is cleared. TMR1 is the default selection
               for the CCP module, so it is used for indication purpose only.


 2017-2021 Microchip Technology Inc.                                                                                DS40001919G-page 351
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 23-2:          CCPTMRS0: CCP TIMERS CONTROL REGISTER 0
   R/W-0/0         R/W-1/1        R/W-0/0          R/W-1/1     R/W-0/0          R/W-1/1     R/W-0/0        R/W-1/1
          C4TSEL[1:0]                   C3TSEL[1:0]                  C2TSEL[1:0]                   C1TSEL[1:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
-n = Value at POR               ‘1’ = Bit is set             ‘0’ = Bit is cleared         x = Bit is unknown


bit 7-6          C4TSEL[1:0]: CCP4 Timer Selection bits
                 11 = CCP4 is based off Timer5 in Capture/Compare mode and Timer6 in PWM mode
                 10 = CCP4 is based off Timer3 in Capture/Compare mode and Timer4 in PWM mode
                 01 = CCP4 is based off Timer1 in Capture/Compare mode and Timer2 in PWM mode
                 00 = Reserved
bit 5-4          C3TSEL[1:0]: CCP3 Timer Selection bits
                 11 = CCP3 is based off Timer5 in Capture/Compare mode and Timer6 in PWM mode
                 10 = CCP3 is based off Timer3 in Capture/Compare mode and Timer4 in PWM mode
                 01 = CCP3 is based off Timer1 in Capture/Compare mode and Timer2 in PWM mode
                 00 = Reserved
bit 3-2          C2TSEL[1:0]: CCP2 Timer Selection bits
                 11 = CCP2 is based off Timer5 in Capture/Compare mode and Timer6 in PWM mode
                 10 = CCP2 is based off Timer3 in Capture/Compare mode and Timer4 in PWM mode
                 01 = CCP2 is based off Timer1 in Capture/Compare mode and Timer2 in PWM mode
                 00 = Reserved
bit 1-0          C1TSEL[1:0]: CCP1 Timer Selection bits
                 11 = CCP1 is based off Timer5 in Capture/Compare mode and Timer6 in PWM mode
                 10 = CCP1 is based off Timer3 in Capture/Compare mode and Timer4 in PWM mode
                 01 = CCP1 is based off Timer1 in Capture/Compare mode and Timer2 in PWM mode
                 00 = Reserved


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 352
                      PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 23-3:         CCPxCAP: CAPTURE INPUT SELECTION MULTIPLEXER REGISTER
        U-0           U-0               U-0            U-0               U-0             R/W-0/x         R/W-0/x          R/W-0/x
        —             —                 —               —                 —                              CTS[2:0]
bit 7                                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit                     U = Unimplemented bit, read as ‘0’
-n = Value at POR               ‘1’ = Bit is set                     ‘0’ = Bit is cleared             x = Bit is unknown


bit 7-3          Unimplemented: Read as ‘0’
bit 2-0          CTS[2:0]: Capture Trigger Input Selection bits

                                                                                     Connection
                            CTS[1:0]
                                                       CCP1                   CCP2                CCP3               CCP4

                              111                                                     CLC4_out
                              110                                                     CLC3_out
                              101                                                     CLC2_out
                              100                                                     CLC1_out
                              011                                                    IOC_Interrupt
                              010                                                    CMP2_output
                              001                                                    CMP1_output
                                                   Pin selected by      Pin selected by      Pin selected by     Pin selected by
                              000
                                                     CCP1PPS              CCP2PPS              CCP3PPS             CCP4PPS


REGISTER 23-4:         CCPRxL: CCPx REGISTER LOW BYTE
    R/W-x/x         R/W-x/x         R/W-x/x          R/W-x/x           R/W-x/x           R/W-x/x         R/W-x/x          R/W-x/x
                                                             RL[7:0]
bit 7                                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit                     U = Unimplemented bit, read as ‘0’
-n = Value at POR               ‘1’ = Bit is set                     ‘0’ = Bit is cleared             x = Bit is unknown


bit 7-0          MODE = Capture Mode:
                 RL[7:0]: LSB of captured TMR1 value
                 MODE = Compare Mode:
                 RL[7:0]: LSB compared to TMR1 value
                 MODE = PWM Mode && FMT = 0:
                 RL[7:0]: CCPW[7:0] – Pulse-Width LS 8 bits
                 MODE = PWM Mode && FMT = 1:
                 RL[7:6]: CCPW[1:0] – Pulse-Width LS 2 bits
                 RL[5:0]: Not used


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 353
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 23-5:           CCPRxH: CCPx REGISTER HIGH BYTE
    R/W-x/x           R/W-x/x            R/W-x/x         R/W-x/x         R/W-x/x               R/W-x/x              R/W-x/x            R/W-x/x
                                                                 RH[7:0]
bit 7                                                                                                                                       bit 0


Legend:
R = Readable bit                      W = Writable bit                 U = Unimplemented bit, read as ‘0’
-n = Value at POR                     ‘1’ = Bit is set                 ‘0’ = Bit is cleared                   x = Bit is unknown


bit 7-0           MODE = Capture Mode:
                  RH[7:0]: MSB of captured TMR1 value
                  MODE = Compare Mode:
                  RH[7:0]: MSB compared to TMR1 value
                  MODE = PWM Mode && FMT = 0:
                  RH[7:2]: Not used
                  RH[1:0]: CCPW[9:8] – Pulse-Width MS 2 bits
                  MODE = PWM Mode && FMT = 1:
                  RH[7:0]: CCPW[9:2] – Pulse-Width MS 8 bits


TABLE 23-4:         SUMMARY OF REGISTERS ASSOCIATED WITH CCPx
                                                                                                                                          Register
   Name          Bit 7        Bit 6          Bit 5       Bit 4          Bit 3           Bit 2               Bit 1              Bit 0
                                                                                                                                          on Page
CCPxCON          EN             —            OUT         FMT                                    MODE[3:0]                                   352
CCPxCAP           —             —             —           —              —                 —                        CTS[1:0]                354
CCPRxL                                                             CCPRx[7:0]                                                               354
CCPRxH                                                            CCPRx[15:8]                                                               355
CCPTMRS0           C4TSEL[1:0]                  C3TSEL[1:0]                  C2TSEL[1:0]                        C1TSEL[1:0]                 353
Legend:     — = Unimplemented location, read as ‘0’. Shaded cells are not used by the CCP module.


 2017-2021 Microchip Technology Inc.                                                                                  DS40001919G-page 354
