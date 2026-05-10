                      PIC18(L)F26/27/45/46/47/55/56/57K42
7.0      OSCILLATOR MODULE (WITH                           The external oscillator module can be configured in one
                                                           of the following clock modes, by setting the
         FAIL-SAFE CLOCK MONITOR)
                                                           FEXTOSC[2:0] Configuration bits:

7.1      Overview                                          1.   ECL – External Clock Low Power mode
                                                           2.   ECM – External Clock Medium Power mode
The oscillator module has multiple clock sources and       3.   ECH – External Clock High Power mode
selection features that allow it to be used in a wide
                                                           4.   LP – 32 kHz Low Power Crystal mode
range of applications while maximizing performance
and minimizing power consumption. Figure 7-1               5.   XT – Medium Gain Crystal or Ceramic Resonator
illustrates a block diagram of the oscillator module.           Oscillator mode (between 100 kHz and 4 MHz)
                                                           6.   HS – High Gain Crystal or Ceramic Resonator
Clock sources can be supplied from external oscillators,
                                                                mode (above 4 MHz)
quartz-crystal resonators and ceramic resonators. In
addition, the system clock source can be supplied from     The ECH, ECM, and ECL Clock modes rely on an
one of two internal oscillators and PLL circuits, with a   external logic level signal as the device clock source.
choice of speeds selectable via software. Additional       The LP, XT, and HS Clock modes require an external
clock features include:                                    crystal or resonator to be connected to the device.
                                                           Each mode is optimized for a different frequency range.
• Selectable system clock source between external
                                                           The internal oscillator block produces low and high-
  or internal sources via software.
                                                           frequency clock sources, designated LFINTOSC and
• Fail-Safe Clock Monitor (FSCM) designed to               HFINTOSC. (see Internal Oscillator Block, Figure 7-1).
  detect a failure of the external clock source (LP,       Multiple device clock frequencies may be derived from
  XT, HS, ECH, ECM, ECL) and switch                        these clock sources.
  automatically to the internal oscillator.
• Oscillator Start-up Timer (OST) ensures stability
  of crystal oscillator sources.
The RSTOSC bits of Configuration Word 1 (Register 5-
1) determine the type of oscillator that will be used
when the device runs after Reset, including when it is
first powered up.
If an external clock source is selected, the FEXTOSC
bits of Configuration Word 1 must be used in
conjunction with the RSTOSC bits to select the
External Clock mode.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 92
                                        FIGURE 7-1:          SIMPLIFIED PIC® MCU CLOCK SOURCE BLOCK DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                                       Rev. 10-000208D
                                                                                                                                                                                              5/10/2016


                                              CLKIN/OSC1

                                                             External
                                                             Oscillator
                                                            (EXTOSC)


                                                                                                                                                                                                          PIC18(L)F26/27/45/46/47/55/56/57K42
                                             CLKOUT/OSC2
                                                                                                                                     CDIV<4:0>
                                                                          4x PLL
                                                                                                 COSC<2:0>
                                             SOSCIN/SOSCI

                                                            Secondary                                                           512
                                                            Oscillator                                                                 1001
                                                                                                                                256
                                                             (SOSC)                                 111                                1000
                                                                                                                                128                 Sleep
                                               SOSCO                                                010                                0111                             System Clock
                                                                                                                                64
                                                                                                    100                                0110


                                                                                                                 Post Divider
                                                      LFINTOSC                                                                  32
                                                                                                    101                                0101
                                                        31 kHz                                                                  16
                                                                                                    110                                0100                    SYSCMD          Peripheral Clock
                                                       Oscillator
                                                                                                                                 8
                                                                                      Reserved      011                                0011
                                                                                                                                 4
                                                                                      Reserved      001                                0010      Sleep
                                                                                                                                 2
                                                      HFINTOSC                        Reserved      000                                0001       Idle
                                                                                                                                 1
                                                                                                                                       0000
                                                      HFFRQ<3:0>
                                                1,2,4,8,12,16,32,48,64
                                                         MHz
                                                       Oscillator
                                                                                   LFINTOSC is used to
                                                                                                          FSCM
                                                                                   monitor system clock


                                                      MFINTOSC
                                                                                                                                              To Peripherals
                                                31.25 kHz and 500 kHz                                                                         To Peripherals
                                                       Oscillator                                                                             To Peripherals
DS40001919G-page 93


                                                                                                                                              To Peripherals
                      PIC18(L)F26/27/45/46/47/55/56/57K42
7.2       Clock Source Types                                EC mode has three power modes to select from through
                                                            Configuration Words:
Clock sources can be classified as external or internal.
                                                            • ECH – High power
External clock sources rely on external circuitry for the
                                                            • ECM – Medium power
clock source to function. Examples are: oscillator
modules (ECH, ECM, ECL mode), quartz crystal                • ECL – Low power
resonators or ceramic resonators (LP, XT and HS             Refer to Table 44-8 for External Clock/Oscillator Timing
modes).                                                     Requirements. The Oscillator Start-up Timer (OST) is
Internal clock sources are contained within the             disabled when EC mode is selected. Therefore, there
oscillator module. The internal oscillator block has two    is no delay in operation after a Power-on Reset (POR)
internal oscillators that are used to generate internal     or wake-up from Sleep. Because the PIC® MCU design
system clock sources. The High-Frequency Internal           is fully static, stopping the external clock input will have
Oscillator (HFINTOSC) can produce 1, 2, 4, 8, 12, 16,       the effect of halting the device while leaving all data
32, 48 and 64 MHz clock. The frequency can be               intact. Upon restarting the external clock, the device
controlled through the OSCFRQ register (Register 7-         will resume operation as if no time had elapsed.
5). The Low-Frequency Internal Oscillator (LFINTOSC)
generates a fixed 31 kHz frequency.                         FIGURE 7-2:             EXTERNAL CLOCK (EC)
                                                                                    MODE OPERATION
A 4x PLL is provided that can be used with an external
clock. When used with the HFINTOSC the 4x PLL has
input frequency limitations.See Section 7.2.1.4 “4x           Clock from                   OSC1/CLKIN
PLL” for more details.                                        Ext. System
                                                                                                  PIC® MCU
The system clock can be selected between external or
internal clock sources via the NOSC bits in the                                            OSC2/CLKOUT
OSCCON1 register. See Section 7.3 “Clock                         FOSC/4 or I/O(1)
Switching” for additional information. The system
clock can be made available on the OSC2/CLKOUT pin           Note 1:     Output depends upon CLKOUTEN bit of the
for any of the modes that do not use the OSC2 pin. The                   Configuration Words (CONFIG1H).
clock out functionality is governed by the CLKOUTEN
bit in the CONFIG1H register (Register 5-2). If enabled,
the clock out signal is always at a frequency of FOSC/4.    7.2.1.2         LP, XT, HS Modes
                                                            The LP, XT and HS modes support the use of quartz
7.2.1       EXTERNAL CLOCK SOURCES                          crystal resonators or ceramic resonators connected to
An external clock source can be used as the device          OSC1 and OSC2 (Figure 7-3). The three modes select
system clock by performing one of the following             a low, medium or high gain setting of the internal
actions:                                                    inverter-amplifier to support various resonator types
                                                            and speed.
• Program the RSTOSC[2:0] and FEXTOSC[2:0]
  bits in the Configuration Words to select an              LP Oscillator mode selects the lowest gain setting of the
  external clock source that will be used as the            internal inverter-amplifier. LP mode current consumption
  default system clock upon a device Reset.                 is the least of the three modes. This mode is designed to
• Write the NOSC[2:0] and NDIV[3:0] bits in the             drive only 32.768 kHz tuning-fork type crystals (watch
  OSCCON1 register to switch the system clock               crystals), but can operate up to 100 kHz.
  source.                                                   XT Oscillator mode selects the intermediate gain
See Section      7.3 “Clock    Switching”     for   more    setting of the internal inverter-amplifier. XT mode
information.                                                current consumption is the medium of the three modes.
                                                            This mode is best suited to drive crystals and
7.2.1.1       EC Mode                                       resonators with a frequency range up to 4 MHz.

The External Clock (EC) mode allows an externally           HS Oscillator mode selects the highest gain setting of the
generated logic level signal to be the system clock         internal inverter-amplifier. HS mode current consumption
source. When operating in this mode, an external clock      is the highest of the three modes. This mode is best
source is connected to the OSC1 input. OSC2/                suited for resonators that require an operating frequency
CLKOUT is available for general purpose I/O or              up to 20 MHz.
CLKOUT. Figure 7-2 shows the pin connections for EC         Figure 7-3 and Figure 7-4 show typical circuits for
mode.                                                       quartz crystal and ceramic resonators, respectively.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 94
                         PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 7-3:                 QUARTZ CRYSTAL                    7.2.1.3      Oscillator Start-up Timer (OST)
                            OPERATION (LP, XT OR              If the oscillator module is configured for LP, XT or HS
                            HS MODE)                          modes, the Oscillator Start-up Timer (OST) counts
                                                              1024 oscillations from OSC1. This occurs following a
                                  PIC® MCU                    Power-on Reset (POR), Brown-out Reset (BOR), or a
                                                              wake-up from Sleep. The OST ensures that the
                              OSC1/CLKIN                      oscillator circuit, using a quartz crystal resonator or
       C1
                                                              ceramic resonator, has started and is providing a stable
                                               To Internal
                                               Logic          system clock to the oscillator module.
               Quartz
                                 RF(2)         Sleep          7.2.1.4       4x PLL
               Crystal
                                                              The oscillator module contains a 4x PLL that can be
                                                              used with the external clock sources to provide a
                              OSC2/CLKOUT
       C2        RS(1)                                        system clock source. The input frequency for the PLL
                                                              must fall within specifications. See the PLL Clock
 Note 1:    A series resistor (RS) may be required for        Timing Specifications in Table 44-10.
            quartz crystals with low drive level.
                                                              The PLL can be enabled for use by one of two
       2:   The value of RF varies with the Oscillator mode   methods:
            selected (typically between 2 M to 10 M.
                                                              1.   Program the RSTOSC bits in the Configuration
                                                                   Word 1 to 010 (enable EXTOSC with 4x PLL).
FIGURE 7-4:                 CERAMIC RESONATOR                 2.   Write the NOSC bits in the OSCCON1 register
                            OPERATION                              to 010 (enable EXTOSC with 4x PLL).
                            (XT OR HS MODE)

                                    PIC® MCU

                               OSC1/CLKIN

      C1                                        To Internal
                                                Logic

                    RP(3)         RF(2)         Sleep


       C2 Ceramic   RS(1)      OSC2/CLKOUT
          Resonator

 Note 1:    A series resistor (RS) may be required for
            ceramic resonators with low drive level.
        2: The value of RF varies with the Oscillator mode
           selected (typically between 2 M to 10 M.
        3: An additional parallel feedback resistor (RP)
           may be required for proper ceramic resonator
           operation.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 95
                      PIC18(L)F26/27/45/46/47/55/56/57K42
7.2.1.5       Secondary Oscillator
                                                           Note 1: Quartz   crystal   characteristics     vary
The secondary oscillator is a separate oscillator block            according to type, package and
that can be used as an alternate system clock source.              manufacturer. The user may consult the
The secondary oscillator is optimized for 32.768 kHz,              manufacturer data sheets for specifications
and can be used with an external crystal oscillator con-           and recommended application.
nected to the SOSCI and SOSCO device pins, or an
                                                                2: Always verify oscillator performance over
external clock source connected to the SOSCIN pin.
                                                                   the VDD and temperature range that is
The secondary oscillator can be selected during run-
                                                                   expected for the application.
time using clock switching. Refer to Section
7.3 “Clock Switching” for more information.                     3: For oscillator design assistance, reference
                                                                   the following Microchip Application Notes:
Two power modes are available for the secondary
oscillator. These modes are selected with the                       • AN826, “Crystal Oscillator Basics and
SOSCPWR (OSCCON3[6]). Clearing this bit selects                       Crystal Selection for PIC® and PIC®
the lower Crystal Gain mode which provides lowest                     Devices” (DS00826)
microcontroller power consumption. Setting this bit                 • AN849, “Basic PIC® Oscillator Design”
enables a higher Gain mode to support faster crystal                  (DS00849)
start-up or crystals with higher ESR.                               • AN943, “Practical PIC® Oscillator
                                                                      Analysis and Design” (DS00943)
FIGURE 7-5:            QUARTZ CRYSTAL                               • AN949, “Making Your Oscillator Work”
                       OPERATION                                      (DS00949)
                       (SECONDARY                                   • TB097, “Interfacing a Micro Crystal
                       OSCILLATOR)                                    MS1V-T1K 32.768 kHz Tuning Fork
                                                                      Crystal to a PIC16F690/SS” (DS91097)
                                                                    • AN1288, “Design Practices for Low-
                               PIC® MCU
                                                                      Power External Oscillators” (DS01288)
                           SOSCI

       C1                                 To Internal
                                          Logic
              32.768 kHz
              Quartz
              Crystal


       C2                  SOSCO


 2017-2021 Microchip Technology Inc.                                                    DS40001919G-page 96
                      PIC18(L)F26/27/45/46/47/55/56/57K42
7.2.2       INTERNAL CLOCK SOURCES                       7.2.2.1      HFINTOSC
The device may be configured to use the internal         The High-Frequency Internal Oscillator (HFINTOSC) is
oscillator block as the system clock by performing one   a precision digitally-controlled internal clock source
of the following actions:                                that produces a stable clock up to 64 MHz. The
• Program the RSTOSC[2:0] bits in Configuration          HFINTOSC can be enabled through one of the
  Words to select the INTOSC clock source, which         following methods:
  will be used as the default system clock upon a        • Programming the RSTOSC[2:0] bits in
  device Reset.                                            Configuration Word 1 to ‘110’ (FOSC = 1 MHz) or
• Write the NOSC[2:0] bits in the OSCCON1                  ‘000’ (FOSC = 64 MHz) to set the oscillator upon
  register to switch the system clock source to the        device Power-up or Reset.
  internal oscillator during run-time. See Section       • Write to the NOSC[2:0] bits of the OSCCON1
  7.3 “Clock Switching” for more information.              register during run-time. See Section 7.3 “Clock
In INTOSC mode, OSC1/CLKIN is available for general        Switching” for more information.
purpose I/O. OSC2/CLKOUT is available for general        The HFINTOSC frequency can be selected by setting
purpose I/O or CLKOUT.                                   the FRQ[3:0] bits of the OSCFRQ register.
The function of the OSC2/CLKOUT pin is determined        The NDIV[3:0] bits of the OSCCON1 register allow for
by the CLKOUTEN bit in Configuration Words.              division of the HFINTOSC output from a range between
The internal oscillator block has two independent        1:1 and 1:512.
oscillators that can produce two internal system clock
                                                         7.2.2.2      MFINTOSC
sources.
                                                         The module provides two (500 kHz and 31.25 kHz)
1.   The HFINTOSC (High-Frequency Internal
                                                         constant clock outputs. These clocks are digital
     Oscillator) is factory-calibrated and operates
                                                         divisors of the HFINTOSC clock. Dynamic divider logic
     from 1 to 64 MHz. The frequency of HFINTOSC
                                                         is used to provide constant MFINTOSC clock rates for
     can be selected through the OSCFRQ
                                                         all settings of HFINTOSC.
     Frequency Selection register, and fine-tuning
     can be done via the OSCTUNE register.               The MFINTOSC cannot be used to drive the system
2.   The LFINTOSC (Low-Frequency Internal                but it is used to clock certain modules such as the
     Oscillator) is factory-calibrated and operates at   Timers and WWDT.
     31 kHz.


 2017-2021 Microchip Technology Inc.                                                    DS40001919G-page 97
                      PIC18(L)F26/27/45/46/47/55/56/57K42
7.2.2.3       Internal Oscillator Frequency
              Adjustment
The HFINTOSC is factory-calibrated. This internal
oscillator can be adjusted in software by writing to the
OSCTUNE register (Register 7-3).
The default value of the OSCTUNE register is 00h. The
value is a 6-bit two’s complement number. A value of
1Fh will provide an adjustment to the maximum
frequency. A value of 20h will provide an adjustment to
the minimum frequency.
When the OSCTUNE register is modified, the oscillator
frequency will begin shifting to the new frequency. Code
execution continues during this shift. There is no
indication that the shift has occurred.
OSCTUNE does not affect the LFINTOSC frequency.
Operation of features that depend on the LFINTOSC
clock source frequency, such as the Power-up Timer
(PWRT), WWDT, Fail-Safe Clock Monitor (FSCM) and
peripherals, are not affected by the change in frequency.

7.2.2.4       LFINTOSC
The Low-Frequency Internal Oscillator (LFINTOSC) is
a factory-calibrated 31 kHz internal clock source.
The LFINTOSC is the frequency for the Power-up
Timer (PWRT), Windowed Watchdog Timer (WWDT)
and Fail-Safe Clock Monitor (FSCM). The LFINTOSC
can also be used as the system clock, or as a clock or
input source to other peripherals.
The LFINTOSC is enabled through one of the following
methods:
• Programming the RSTOSC[2:0] bits of
  Configuration Word 1 to enable LFINTOSC.
• Write to the NOSC[2:0] bits of the OSCCON1 reg-
  ister during run-time. See Section 7.3, Clock
  Switching for more information.

7.2.2.5       ADCRC
The ADCRC is an oscillator dedicated to the ADC2
module. The ADCRC oscillator can be manually
enabled using the ADOEN bit of the OSCEN register.
The ADCRC runs at a fixed frequency of 600 kHz.
ADCRC is automatically enabled if it is selected as the
clock source for the ADC2 module.


 2017-2021 Microchip Technology Inc.                       DS40001919G-page 98
                        PIC18(L)F26/27/45/46/47/55/56/57K42
7.2.2.6       Oscillator Status and Manual Enable              When the new oscillator is ready, the New Oscillator
                                                               Ready (NOSCR) bit of OSCCON3 and the Clock
The Ready status of each oscillator (including the
                                                               Switch Interrupt Flag (CSWIF) bit of the respective PIR
ADCRC oscillator) is displayed in OSCSTAT
                                                               register are set. If Clock Switch Interrupts are enabled
(Register 7-4). The oscillators (but not the PLL) may be
                                                               (CSWIE = 1), an interrupt will be generated at that time.
explicitly enabled through OSCEN (Register 7-7).
                                                               The Oscillator Ready (ORDY) bit of OSCCON3 can
7.2.2.7       HFOR and MFOR Bits                               also be polled to determine when the oscillator is ready
                                                               in lieu of an interrupt.
The HFOR and MFOR bits indicate that the HFINTOSC
and MFINTOSC is ready. These clocks are always
valid for use at all times, but only accurate after they are     Note:     The CSWIF interrupt will not wake the
ready.                                                                     system from Sleep.
When a new value is loaded into the OSCFRQ register,           If the Clock Switch Hold (CSWHOLD) bit of OSCCON3
the HFOR and MFOR bits will clear, and set again               is clear, the oscillator switch will occur when the New
when the oscillator is ready. During pending OSCFRQ            Oscillator is Ready bit (NOSCR) is set, and the
changes the MFINTOSC clock will stall at a high or a           interrupt (if enabled) will be serviced at the new
low state, until the HFINTOSC resumes operation.               oscillator setting.
                                                               If CSWHOLD is set, the oscillator switch is suspended,
7.3       Clock Switching                                      while execution continues using the current (old) clock
                                                               source. When the NOSCR bit is set, software may:
The system clock source can be switched between
external and internal clock sources via software using         • Set CSWHOLD = 0 so the switch can complete,
the New Oscillator Source (NOSC) bits of the                      or
OSCCON1 register. The following clock sources can be           • Copy COSC into NOSC to abandon the switch.
selected using the following:                                  If Doze is in effect, the switch occurs on the next clock
• External oscillator                                          cycle, whether or not the CPU is operating during that
• Internal Oscillator Block (INTOSC)                           cycle.
                                                               Changing the clock post-divider without changing the
                                                               clock source (i.e., changing FOSC from 1 MHz to
  Note:     The Clock Switch Enable bit in                     2 MHz) is handled in the same manner as a clock
            Configuration Word 1 can be used to                source change, as described previously. The clock
            enable or disable the clock switching              source will already be active, so the switch is relatively
            capability. When cleared, the NOSC and             quick. CSWHOLD must be clear (CSWHOLD = 0) for
            NDIV bits cannot be changed by user                the switch to complete.
            software. When set, writing to NOSC and
                                                               The current COSC and CDIV are indicated in the
            NDIV is allowed and would switch the
                                                               OSCCON2 register up to the moment when the switch
            clock frequency.
                                                               actually occurs, at which time OSCCON2 is updated
                                                               and ORDY is set. NOSCR is cleared by hardware to
7.3.1       NEW OSCILLATOR SOURCE
                                                               indicate that the switch is complete.
            (NOSC) AND NEW DIVIDER
            SELECTION REQUEST (NDIV) BITS
The New Oscillator Source (NOSC) and New Divider
Selection Request (NDIV) bits of the OSCCON1
register select the system clock source and frequency
that are used for the CPU and peripherals.
When new values of NOSC and NDIV are written to
OSCCON1, the current oscillator selection will
continue to operate while waiting for the new clock
source to indicate that it is stable and ready. In some
cases, the newly requested source may already be in
use, and is ready immediately. In the case of a divider-
only change, the new and old sources are the same, so
the old source will be ready immediately. The device
may enter Sleep while waiting for the switch as
described in Section 7.3.2 “Clock Switch and
Sleep”.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 99
                       PIC18(L)F26/27/45/46/47/55/56/57K42
7.3.2       CLOCK SWITCH AND SLEEP
If OSCCON1 is written with a new value and the device
is put to Sleep before the switch completes, the switch
will not take place and the device will enter Sleep
mode.
When the device wakes from Sleep and the
CSWHOLD bit is clear, the device will wake with the
‘new’ clock active, and the Clock Switch Interrupt flag
bit (CSWIF) will be set.
When the device wakes from Sleep and the
CSWHOLD bit is set, the device will wake with the ‘old’
clock active and the new clock will be requested again.


FIGURE 7-6:             CLOCK SWITCH (CSWHOLD = 0)
                           OSCCON1
                           WRITTEN

                                   OSC #1                OSC #2


        ORDY


                                                         NOTE 2
        NOSCR


                                                NOTE 1
        CSWIF


                              USER
    CSWHOLD                   CLEAR


  Note 1: CSWIF is asserted coincident with NOSCR; interrupt is serviced at OSC#2 speed.
       2: The assertion of NOSCR is hidden from the user because it appears only for the duration of the switch.


FIGURE 7-7:             CLOCK SWITCH (CSWHOLD = 1)
                           OSCCON1
                           WRITTEN

                                                                       OSC #1                OSC #2


         ORDY


        NOSCR


                                                      NOTE 1
        CSWIF


                                                                             USER
     CSWHOLD                                                                CLEAR


  Note 1: CSWIF is asserted coincident with NOSCR, and may be cleared before or after clearing CSWHOLD = 0.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 100
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 7-8:            CLOCK SWITCH ABANDONED
                          OSCCON1                                          OSCCON1
                          WRITTEN                                          WRITTEN

                                                   OSC #1

         ORDY
                                                                                 NOTE 2


       NOSCR


                                                    NOTE 1
        CSWIF


     CSWHOLD


  Note 1: CSWIF may be cleared before or after rewriting OSCCON1; CSWIF is not automatically cleared.
       2: ORDY = 0 if OSCCON1 does not match OSCCON2; a new switch will begin.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 101
                         PIC18(L)F26/27/45/46/47/55/56/57K42
7.4       Fail-Safe Clock Monitor                            7.4.3       FAIL-SAFE CONDITION CLEARING
The Fail-Safe Clock Monitor (FSCM) allows the device         The Fail-Safe condition is cleared after a Reset,
to continue operating may the external oscillator fail.      executing a SLEEP instruction or changing the NOSC
The FSCM is enabled by setting the FCMEN bit in the          and NDIV bits of the OSCCON1 register. When
Configuration Words. The FSCM is applicable to all           switching to the external oscillator or PLL, the OST is
external Oscillator modes (LP, XT, HS, ECL/M/H and           restarted. While the OST is running, the device
Secondary Oscillator).                                       continues to operate from the INTOSC selected in
                                                             OSCCON1. When the OST times out, the Fail-Safe
                                                             condition is cleared after successfully switching to the
FIGURE 7-9:              FSCM BLOCK DIAGRAM
                                                             external clock source. The OSCFIF bit may be cleared
                                Clock Monitor                prior to switching to the external clock source. If the
                                    Latch                    Fail-Safe condition still exists, the OSCFIF flag will
      External                                               again become set by hardware.
                                   S     Q
       Clock


   LFINTOSC
                     ÷ 64         R      Q
    Oscillator

       31 kHz      488 Hz
      (~32 s)     (~2 ms)

          Sample Clock                             Clock
                                                 Failure
                                                Detected


7.4.1        FAIL-SAFE DETECTION
The FSCM module detects a failed oscillator by
comparing the external oscillator to the FSCM sample
clock. The sample clock is generated by dividing the
LFINTOSC by 64. See Figure 7-9. Inside the fail
detector block is a latch. The external clock sets the
latch on each falling edge of the external clock. The
sample clock clears the latch on each rising edge of the
sample clock. A failure is detected when an entire half-
cycle of the sample clock elapses before the external
clock goes low.

7.4.2        FAIL-SAFE OPERATION
When the external clock fails, the FSCM overwrites the
COSC bits to select HFINTOSC (3'b110). The
frequency of HFINTOSC would be determined by the
previous state of the FRQ bits and the NDIV/CDIV bits.
The bit flag OSFIF of the respective PIR register is set.
Setting this flag will generate an interrupt if the OSFIE
bit of the respective PIR register is also set. The device
firmware can then take steps to mitigate the problems
that may arise from a failed clock. The system clock will
continue to be sourced from the internal clock source
until the device firmware successfully restarts the
external oscillator and switches back to external
operation, by writing to the NOSC and NDIV bits of the
OSCCON1 register.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 102
                        PIC18(L)F26/27/45/46/47/55/56/57K42
7.4.4       RESET OR WAKE-UP FROM SLEEP
The FSCM is designed to detect an oscillator failure
after the Oscillator Start-up Timer (OST) has expired.
The OST is used after waking up from Sleep and after
any type of Reset. The OST is not used with the EC
Clock modes so that the FSCM will be active as soon
as the Reset or wake-up has completed.

FIGURE 7-10:            FSCM TIMING DIAGRAM

        Sample Clock

              System                                                          Oscillator
               Clock                                                          Failure
              Output


 Clock Monitor Output
                  (Q)
                                                                                                   Failure
                                                                                                  Detected
             OSCFIF


                                           Test                            Test                            Test

         Note:     The system clock is normally at a much higher frequency than the sample clock. The relative frequencies in
                   this example have been chosen for clarity.


TABLE 7-1:        NOSC/COSC AND NDIV/CDIV BIT SETTINGS
        NOSC[2:0]                                                                 NDIV[3:0]
                                        Clock Source                                                      Clock Divider
        COSC[2:0]                                                                 CDIV[3:0]
           111                           EXTOSC(1)                                1111-1010                  Reserved
           110                          HFINTOSC(2)                                 1001                          512
           101                           LFINTOSC                                   1000                          256
           100                             SOSC                                     0111                          128
           011                            Reserved                                  0110                          64
           010                     EXTOSC + 4x PLL(3)                               0101                          32
           001                            Reserved                                  0100                          16
           000                            Reserved                                  0011                           8
                                                                                    0010                           4
                                                                                    0001                           2
                                                                                    0000                           1

Note 1:     EXTOSC configured by the FEXTOSC bits of Configuration Word 1 (Register 5-1).
     2:     HFINTOSC frequency is set with the FRQ bits of the OSCFRQ register (Register 7-5).
     3:     EXTOSC must meet the PLL specifications (Table 44-10).


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 103
                         PIC18(L)F26/27/45/46/47/55/56/57K42
7.5         Register Definitions: Oscillator Control
REGISTER 7-1:             OSCCON1: OSCILLATOR CONTROL REGISTER 1
        U-0            R/W-f/f        R/W-f/f           R/W-f/f     R/W-q/q        R/W-q/q        R/W-q/q        R/W-q/q
        —                           NOSC[2:0]                                             NDIV[3:0]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit                   W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared           f = determined by Configuration bit setting
                                                                  q = Reset value is determined by hardware


bit 7               Unimplemented: Read as ‘0’
bit 6-4             NOSC[2:0]: New Oscillator Source Request bits(1,2,3)
                    The setting requests a source oscillator and PLL combination per Table 7-1.
                    POR value = RSTOSC (Register 5-1).
bit 3-0             NDIV[3:0]: New Divider Selection Request bits(2,3)
                    The setting determines the new postscaler division ratio per Table 7-1.

Note 1: The default value (f/f) is determined by the RSTOSC Configuration bits. See Table 7-2 below.
     2: If NOSC is written with a reserved value (Table 7-1), the operation is ignored and neither NOSC nor NDIV is
        written.
     3: When CSWEN = 0, this register is read-only and cannot be changed from the POR value.

TABLE 7-2:            DEFAULT OSCILLATOR SETTINGS
                                        SFR Reset Values
      RSTOSC                                                                             Initial FOSC Frequency
                        NOSC/COSC                CDIV             OSCFRQ
          111                111                  1:1                                     EXTOSC per FEXTOSC
          110                110                  4:1                                     FOSC = 1 MHz (4 MHz/4)
                                                                   4 MHz
          101                101                  1:1                                           LFINTOSC
          100                100                  1:1                                              SOSC
          011                                                        Reserved
          010                010                  1:1              4 MHz                     EXTOSC + 4xPLL(1)
          001                                                        Reserved
          000                110                  1:1             64 MHz                      FOSC = 64 MHZ
Note 1:         EXTOSC must meet the PLL specifications (Table 44-10).


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 104
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 7-2:            OSCCON2: OSCILLATOR CONTROL REGISTER 2
        U-0            R-f/f           R-f/f             R-f/f       R-f/f           R-f/f               R-f/f       R-f/f
        —                          COSC[2:0]                                                 CDIV[3:0]
bit 7                                                                                                                      bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              Unimplemented: Read as ‘0’
bit 6-4            COSC[2:0]: Current Oscillator Source Select bits (read-only)(1)
                   Indicates the current source oscillator and PLL combination per Table 7-1.
bit 3-0            CDIV[3:0]: Current Divider Select bits (read-only)(1)
                   Indicates the current postscaler division ratio per Table 7-1.

Note 1: The POR value is the value present when user code execution begins.


REGISTER 7-3:            OSCCON3: OSCILLATOR CONTROL REGISTER 3
 R/W/HC-0/0          R/W-0/0           U-0               R-0/0       R-0/0           U-0                 U-0         U-0
  CSWHOLD          SOSCPWR              —                ORDY      NOSCR              —                   —           —
bit 7                                                                                                                      bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared           HC = Bit is cleared by hardware


bit 7              CSWHOLD: Clock Switch Hold bit
                   1 = Clock switch will hold (with interrupt) when the oscillator selected by NOSC is ready
                   0 = Clock switch may proceed when the oscillator selected by NOSC is ready; NOSCR
                       becomes ‘1’, the switch will occur
bit 6              SOSCPWR: Secondary Oscillator Power Mode Select bit
                   1 = Secondary oscillator operating in High Power mode
                   0 = Secondary oscillator operating in Low Power mode
bit 5              Unimplemented: Read as ‘0’
bit 4              ORDY: Oscillator Ready bit (read-only)
                   1 = OSCCON1 = OSCCON2; the current system clock is the clock specified by NOSC
                   0 = A clock switch is in progress
bit 3              NOSCR: New Oscillator is Ready bit (read-only)(1)
                   1 = A clock switch is in progress and the oscillator selected by NOSC indicates a “ready” condition
                   0 = A clock switch is not in progress, or the NOSC-selected oscillator is not yet ready
bit 2-0            Unimplemented: Read as ‘0’

Note 1:       If CSWHOLD = 0, the user may not see this bit set because, when the oscillator becomes ready there
              may be a delay of one instruction clock before this bit is set. The clock switch occurs in the next instruction
              cycle and this bit is cleared.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 105
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 7-4:            OSCSTAT: OSCILLATOR STATUS REGISTER 1
     R-q/q            R-q/q          R-q/q              R-q/q      R-q/q          R-q/q          U-0           R-q/q
    EXTOR             HFOR           MFOR               LFOR       SOR           ADOR            —             PLLR
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared           q = Reset value is determined by hardware


bit 7              EXTOR: EXTOSC (external) Oscillator Ready bit
                   1 = The oscillator is ready to be used
                   0 = The oscillator is not enabled, or is not yet ready to be used
bit 6              HFOR: HFINTOSC Oscillator Ready bit
                   1 = The oscillator is ready to be used
                   0 = The oscillator is not enabled, or is not yet ready to be used
bit 5              MFOR: MFINTOSC Oscillator Ready
                   1 = The oscillator is ready to be used
                   0 = The oscillator is not enabled, or is not yet ready to be used
bit 4              LFOR: LFINTOSC Oscillator Ready bit
                   1 = The oscillator is ready to be used
                   0 = The oscillator is not enabled, or is not yet ready to be used
bit 3              SOR: Secondary (Timer1) Oscillator Ready bit
                   1 = The oscillator is ready to be used
                   0 = The oscillator is not enabled, or is not yet ready to be used
bit 2              ADOR: ADC Oscillator Ready bit
                   1 = The oscillator is ready to be used
                   0 = The oscillator is not enabled, or is not yet ready to be used
bit 1              Unimplemented: Read as ‘0’
bit 0              PLLR: PLL is Ready bit
                   1 = The PLL is ready to be used
                   0 = The PLL is not enabled, the required input source is not ready, or the PLL is not locked.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 106
                        PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 7-5:            OSCFRQ: HFINTOSC FREQUENCY SELECTION REGISTER
        U-0            U-0             U-0               U-0     R/W-q/q       R/W-q/q       R/W-q/q         R/W-q/q
        —               —               —                —                            FRQ[3:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         q = Reset value is determined by hardware


bit 7-4            Unimplemented: Read as ‘0’
bit 3-0            FRQ[3:0]: HFINTOSC Frequency Selection bits(1)

                       FRQ[3:0]         Nominal Freq (MHz)
                         1001
                         1010
                         1111
                         1110                 Reserved
                         1101
                         1100
                         1011
                         1000                     64
                         0111                     48
                         0110                     32
                         0101                     16
                         0100                     12
                         0011                      8
                         0010                      4
                         0001                      2
                         0000                      1

Note 1:       Refer to Table 7-2 for more information.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 107
                        PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 7-6:            OSCTUNE: HFINTOSC TUNING REGISTER
        U-0            U-0         R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
        —               —                                             TUN[5:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            TUN[5:0]: HFINTOSC Frequency Tuning bits
                   01 1111 = Maximum frequency
                   •
                   •
                   •
                   00 0000 = Center frequency. Oscillator module is running at the calibrated frequency
                              (default value).
                   •
                   •
                   •
                   10 0000 = Minimum frequency


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 108
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 7-7:            OSCEN: OSCILLATOR MANUAL ENABLE REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0     R/W-0/0       R/W-0/0          U-0            U-0
   EXTOEN            HFOEN         MFOEN           LFOEN      SOSCEN         ADOEN            —               —


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7              EXTOEN: External Oscillator Manual Request Enable bit
                   1 = EXTOSC is explicitly enabled, operating as specified by FEXTOSC
                   0 = EXTOSC could be enabled by requesting peripheral
bit 6              HFOEN: HFINTOSC Oscillator Manual Request Enable bit
                   1 = HFINTOSC is explicitly enabled, operating as specified by OSCFRQ (Register 7-5)
                   0 = HFINTOSC could be enabled by requesting peripheral
bit 5              MFOEN: MFINTOSC (500 kHz/31.25 kHz) Oscillator Manual Request Enable bit (Derived from
                   HFINTOSC)
                   1 = MFINTOSC is explicitly enabled
                   0 = MFINTOSC could be enabled by requesting peripheral
bit 4              LFOEN: LFINTOSC (31 kHz) Oscillator Manual Request Enable bit
                   1 = LFINTOSC is explicitly enabled
                   0 = LFINTOSC could be enabled by requesting peripheral
bit 3              SOSCEN: Secondary Oscillator Manual Request Enable bit
                   1 = Secondary Oscillator is explicitly enabled, operating as specified by SOSCPWR
                   0 = Secondary Oscillator could be enabled by requesting peripheral
bit 2              ADOEN: ADC Oscillator Manual Request Enable bit
                   1 = ADC oscillator is explicitly enabled
                   0 = ADC oscillator could be enabled by requesting peripheral
bit 1-0            Unimplemented: Read as ‘0’


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 109
                       PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 7-3:        SUMMARY OF REGISTERS ASSOCIATED WITH CLOCK SOURCES
                                                                                                       Register
   Name           Bit 7         Bit 6      Bit 5    Bit 4    Bit 3       Bit 2     Bit 1       Bit 0
                                                                                                       on Page
OSCCON1            —                    NOSC[2:0]                          NDIV[3:0]                     104
OSCCON2            —                    COSC[2:0]                          CDIV[3:0]                     105
OSCCON3       CSWHOLD SOSCPWR               —       ORDY    NOSCR          —           —        —        105
OSCSTAT         EXTOR          HFOR       MFOR      LFOR     SOR        ADOR           —       PLLR      106
OSCTUNE            —             —                              TUN[5:0]                                 108
OSCFRQ             —             —          —        —                     FRQ[3:0]                      107
OSCEN           EXTOEN        HFOEN       MFOEN     LFOEN   SOSCEN     ADOEN           —        —        109
Legend: — = unimplemented location, read as ‘0’. Shaded cells are not used by clock sources.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 110
