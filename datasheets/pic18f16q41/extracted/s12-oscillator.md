12.   OSC - Oscillator Module (With Fail-Safe Clock Monitor)
      The oscillator module contains multiple clock sources and selection features that allow it to be used
      in a wide range of applications while maximizing performance and minimizing power consumption.
      Clock sources can be supplied either internally or externally. External sources include:
      • External clock oscillators
      •   Quartz crystal resonators
      •   Ceramic resonators
      •   Secondary Oscillator (SOSC)
      Internal sources include:
      • High-Frequency Internal Oscillator (HFINTOSC)
      •   Low-Frequency Internal Oscillator (LFINTOSC)
      •   Analog-to-Digital Converter RC Oscillator (ADCRC)
      Special features of the oscillator module include:
      • Oscillator Start-up Timer (OST): Ensures stability of quartz crystal or ceramic resonators
      •   4x Phase-Locked Loop (PLL): Frequency multiplier for external clock sources
      •   HFINTOSC Frequency Adjustment: Provides the ability to adjust the HFINTOSC frequency
      •   Clock switching: Allows the system clock to switch between internal or external sources via
          software during run time
      •   Fail-Safe Clock Monitor (FSCM): Designed to detect a failure of the system clock (FOSC), primary
          external clock (EXTOSC) or secondary external clock (SOSC) sources. The FSCM automatically
          switches to an internal clock source upon detection of a FOSC failure.
      The Reset Oscillator (RSTOSC) Configuration bits determine the type of oscillator that will be used
      when the device runs after a Reset, including when the device is first powered up (see the table
      below).

      Table 12-1. RSTOSC Selection Table
                                               SFR Reset Values
          RSTOSC                                                                                           Clock Source
                        NOSC / COSC              NDIV / CDIV                  OSCFRQ
           111               111                  0000 (1:1)                                           EXTOSC per FEXTOSC
           110               110                  0010 (4:1)                                            HFINTOSC @ 1 MHz
                                                                            0010 (4 MHz)
           101               101                  0000 (1:1)                                                 LFINTOSC
           100               100                  0000 (1:1)                                                   SOSC
           011                                                         Reserved
           010               010                  0000 (1:1)                0010 (4 MHz)                EXTOSC + 4x PLL(1)
           001                                                         Reserved
           000               000                  0000 (1:1)                1000 (64 MHz)              HFINTOSC @ 64 MHz

      Note:
      1. EXTOSC must meet the PLL specifications (see the data sheet Electrical Specifications).
      If an external clock source is selected by the RSTOSC bits, the External Oscillator Mode Select
      (FEXTOSC) Configuration bits must be used to select the External Clock mode. These modes include:
      • ECL: External Clock Low Power mode
      •   ECM: External Clock Medium Power mode
      •   ECH: External Clock High Power mode


--- p175 ---
       •   LP: 32 kHz Low-Gain Crystal mode
       •   XT: Medium-Gain Crystal or Ceramic Resonator mode
       •   HS: High-Gain Crystal or Ceramic Resonator mode
       The ECH, ECM and ECL modes rely on an external logic-level signal as the device clock source. The LP,
       XT and HS modes rely on an external quartz crystal or ceramic resonator as the device clock source.
       Each mode is optimized for a specific frequency range. The internal oscillator block produces both
       low-frequency and high-frequency clock signals, designated LFINTOSC and HFINTOSC, respectively.
       Multiple system operating frequencies may be derived from these clock sources.
       The figure below illustrates a block diagram of the oscillator module.

       Figure 12-1. Clock Source Block Diagram


                                                                 PLLEN


            CLKIN/OSC1                                             1
                                                                                                                    To Peripherals
                                                                   0
                           External
                           Oscillator
                          (EXTOSC)

           CLKOUT/OSC2                                                                                      NDIV/
                                                                                                           CDIV[4:0]
                                        4x PLL                          NOSC/
                                                                       COSC[2:0]
           SOSCIN/SOSCI

                          Secondary                                                                  512
                          Oscillator                                                                         1001
                           (SOSC)                                                                    256
                                                                         111                                 1000
                                                                                                     128                  Sleep
              SOSCO                                                      010                                 0111                                    CPU
                                                                                                     64
                                                                         100                                 0110
                                                                                      Post Divider


                   LFINTOSC                                                                          32
                                                                         101                                 0101
                     31 kHz                                                                          16
                                                                         110                                 0100                    SYSCMD           FOSC
                    Oscillator
                                                                                                      8
                                                           Reserved      011                                 0011
                                                                                                      4
                                                           Reserved      001                                 0010      Sleep
                                                                                                      2
                   HFINTOSC                                Reserved      000                                 0001       Idle
                                                                                                      1
                                                                                                             0000
                    FRQ[3:0]
              1,2,4,8,12,16,32,48,64
                       MHz
                     Oscillator                         LFINTOSC is used to
                                                                               FSCM
                                                        monitor system clock

                                                                                                                    To Peripherals
                   MFINTOSC                                                                                         To Peripherals
                                                                                                                    To Peripherals
              31.25 kHz and 500 kHz
                     Oscillator                                                                                     To Peripherals


12.1   Clock Source Types
       Clock sources can be classified as external or internal.
       External clock sources rely on external circuitry for the clock source to function. Examples of
       external clock sources include:
       • Digital oscillator modules
       •   Quartz crystal resonators
       •   Ceramic resonators
       A 4x PLL is provided for use with external clock sources.


--- p176 ---
        Internal clock sources are contained within the oscillator module. The internal oscillator block
        features two internal oscillators that are used to generate internal system clock sources. The
        High-Frequency Internal Oscillator (HFINTOSC) can produce a wide range of frequencies which are
        determined via the HFINTOSC Frequency Selection (OSCFRQ) register. The Low-Frequency Internal
        Oscillator (LFINTOSC) generates a fixed nominal 31 kHz clock signal. The internal oscillator block also
        features an RC oscillator which is dedicated to the Analog-to-Digital Converter (ADC).
        The oscillator module allows the system clock source or system clock frequency to be changed
        through clock switching. Clock source selections are made via the New Oscillator Source Request
        (NOSC) bits. Once the clock source has been selected, the clock source base frequency can be
        divided (post-scaled) via the New Divider Selection Request (NDIV) bits.
        The instruction clock (FOSC/4) can be routed to the OSC2/CLKOUT pin when the pin is not in use.
        The Clock Out Enable (CLKOUTEN) Configuration bit controls the functionality of the CLKOUT signal.
        When CLKOUTEN is clear (CLKOUTEN = 0), the CLKOUT signal is routed to the OSC2/CLKOUT pin.
        When CLKOUTEN is set (CLKOUTEN = 1), the OSC2/CLKOUT pin functions as an I/O pin.

12.1.1 External Clock Sources
        An external clock source can be used as the device system clock by performing one of the following
        actions:
        • Program the RSTOSC and FEXTOSC Configuration bits to select an external clock source that will
           be used as the default system clock upon a device Reset.
        •   Write the NOSC and NDIV bits to switch the system clock source during run time.
12.1.1.1 EC Mode
        The External Clock (EC) mode allows an externally generated logic level signal to be the system clock
        source. When operating in EC mode, an external clock source is connected to the OSC1/CLKIN input
        pin. The OSC2/CLKOUT pin is available as a general purpose I/O pin or as the CLKOUT signal pin.
        EC mode provides three Power mode selections:
        • ECH: High Power mode
        •   ECM: Medium Power mode
        •   ECL: Low Power mode
        The Oscillator Start-up Timer (OST) is disabled when EC mode is selected; therefore, there is no
                                                                                                       ®
        delay in operation after a Power-on Reset (POR) or wake-up from Sleep. Because the PIC MCU
        design is fully static, stopping the external clock input will have the effect of halting the device while
        leaving all data intact. Upon restarting the external clock, the device will resume operation as if no
        time had elapsed.
        The figure below shows the pin connections for EC mode.


--- p177 ---
        Figure 12-2. External Clock (EC) Mode Operation


                                     External clock                         PIC® MCU
                                        source

                                                                         OSC1/CLKIN


                              CLKOUT (FOSC/4)                            OSC2/CLKOUT
                                 or I/O(1)


        Note:
        1. Output depends on the setting of the CLKOUTEN Configuration bit.
12.1.1.2 LP, XT, HS Modes
        The LP, XT and HS modes support the use of quartz crystals or ceramic resonators connected to the
        OSC1 and OSC2 pins, as shown in the figures below. These three modes select a low, medium, or
        high-gain setting of the internal inverter-amplifier to support various resonator types and speeds.
        The LP Oscillator mode selects the lowest gain setting of the internal inverter-amplifier, and
        consumes the least amount of current. LP mode is designed to drive 32.768 kHz tuning-fork type
        crystals (watch crystals), but can operate up to 100 kHz.
        The XT Oscillator mode selects the intermediate gain setting of the internal inverter-amplifier.
        Current consumption is at a medium level when compared to the other two modes. XT mode is
        best suited to drive crystal and ceramic resonators with a frequency range up to 4 MHz.
        The HS Oscillator mode selects the highest gain setting of the internal inverter-amplifier, and
        consumes the most current. This mode is best suited for crystal and ceramic resonators that require
        operating frequencies up to 20 MHz.
        The figures below show typical circuits for quartz crystal and ceramic resonators.


--- p178 ---
     Figure 12-3. Quartz Crystal Operation                                                                                             Rev. Quart z Cry
                                                                                                                                             2/7/2019


                                                                                       PIC® MCU
                                                            OSC1/
                    C1                                      CLKIN

                                                                                                          To internal
                                                                                                             logic
                       Quartz
                       Crystal                                               RF(2)             Sleep

                                                   RS(1)

                    C2                                      OSC2/
                                                           CLKOUT


Filename:       Ceramic Resonator Operation.vsdx
Title:
Last Edit:      2/7/2019
First Used:
Notes: Notes:
     1. A series resistor (RS) may be required for quartz crystals with low drive level.
     2. The value of RF varies with the Oscillator mode selected (typically between 2 MΩ and 10 MΩ).

     Figure 12-4. Ceramic Resonator Operation

                                                                                                                                              Rev. Ceramic
                                                                                                                                                     2/7/2


                                                                                        PIC® MCU
                                                            OSC1/
                  C1                                        CLKIN

                                                                                                            To internal
                                                                                                               logic
                   Resonator
                    Ceramic


                                        RP(3)                                 RF(2)             Sleep

                                                   RS(1)

                  C2                                        OSC2/
                                                           CLKOUT


     Notes:
     1. A series resistor (RS) may be required for ceramic resonators with low drive level.
     2. The value of RF varies with the Oscillator mode selected (typically between 2 MΩ and 10 MΩ).
     3. An additional parallel feedback resistor (RP) may be required for proper ceramic resonator
        operation.


--- p179 ---
  12.1.1.3 Oscillator Start-Up Timer (OST)
              The Oscillator Start-up Timer (OST) ensures that the oscillator circuit has started and is providing
              a stable system clock to the oscillator module. Quartz crystals or ceramic resonators do not
              start immediately and may take a few hundred cycles before the oscillator becomes stable. The
              oscillations must build up until sufficient amplitude is generated to properly toggle between logic
              states. The OST counts 1024 oscillation periods from the OSC1 input following a Power-on Reset
              (POR), Brown-out Reset (BOR), or wake-up from Sleep event to ensure that the oscillator has
              enough time to reach stable and accurate operation. Once the OST has completed its count, module
              hardware sets the External Oscillator Ready (EXTOR) bit, indicating that the oscillator is stable and
              ready to use.
  12.1.1.4 4x PLL
              The oscillator module contains a 4x Phase-Locked Loop (PLL) circuit that can be used with the
              external clock sources to provide a system clock source. The input frequency for the PLL must fall
              within a specified range. See the “PLL Specifications” table found in the “Electrical Specifications”
              chapter for more information.
Filename:     The Quartz
                  PLL can   be Operation.vsdx
                         Crystal enabled for use through one of two methods:
Title:
Last Edit:    1. Program
                 2/8/2019 the RSTOSC Configuration bits to select the “EXTOSC with 4x PLL” option.
First Used:
Notes:        2. Write the NOSC bits to select the ”EXTOSC with 4x PLL” option.
  12.1.1.5 Secondary Oscillator
              The Secondary Oscillator (SOSC) is a separate external oscillator block that can be used as an
              alternate system clock source or as a Timer clock source. The SOSC is optimized for 32.768 kHz and
              can be used with either an external quartz crystal connected to the SOSCI and SOSCO pins or with
              an external clock source connected to the SOSCI pin, as shown in the figures below.
                                                                                                                                           Rev. Quart z Cry
                                                                                                                                                 2/8/2019


              Figure 12-5. SOSC 32.768 kHz Quartz Crystal Oscillator Operation


                                                                                        PIC® MCU
                           C1                          SOSCI

                                                                                                             To internal
                                                                                                                logic
                            32.768 kHz
                              Quartz                                           RF               Sleep
                              Crystal


                           C2                         SOSCO


--- p180 ---
            Notes:


        Figure 12-6. SOSC 32.768 kHz External Clock Operation


                                       32.768 kHz
                                      external clock
                                         source                              PIC® MCU


                                                                         SOSCI


                               General Purpose                           SOSCO
                                     I/O


        The SOSC can be enabled through one of two methods:
        •   Programming the RSTOSC Configuration bits to select the SOSC as the system clock.
        •   Programming the NOSC bits to select the SOSC during run time.
        Two Power modes are available for the secondary oscillator and are selected using the Secondary
        Oscillator Power Mode Select (SOSCPWR) bit. When SOSCPWR is clear (SOSCPWR = 0), the oscillator
        operates in Low Power mode, which is ideal for crystal oscillators with low drive strength. When
        SOSCPWR is set (SOSCPWR = 1), the oscillator operates in High Power mode, which is ideal for crystal
        oscillators with high drive strength or high Equivalent Series Resistance (ESR).


                     Important: The SOSC module must be disabled before changing Power modes. Changes
                     to the Power mode during operation may result in undefined oscillator behavior.


12.1.1.5.1 SOSC Start-Up Timing
        The SOSC utilizes the Oscillator Start-up Timer (OST) to ensure that the 32.768 kHz crystal oscillator
        has started and is available for use. Since crystal oscillators do not start immediately and may take a
        few hundred cycles before achieving stable operation, the OST counts 1024 oscillation periods from
        the SOSCI input. Once the OST completes its count, module hardware sets the Secondary Oscillator
        Ready (SOR) bit, indicating that the SOSC is stable and ready to use.

12.1.2 Internal Clock Sources
        The internal oscillator block contains two independent oscillators that can produce two internal
        system clock sources:
        • High-Frequency Internal Oscillator (HFINTOSC)
        •   Low-Frequency Internal Oscillator (LFINTOSC)
        Internal oscillator selection is performed one of two ways:
        1. Program the RSTOSC Configuration bits to select one of the INTOSC sources which will be used
            upon a device Reset.
        2. Write the New Oscillator Source Request (NOSC) bits to select an internal oscillator during run
           time.


--- p181 ---
        In INTOSC mode, the OSC1/CLKIN and OSC2/CLKOUT pins are available for use as a general purpose
        I/Os, provided that no external oscillator is connected. The function of the OSC2/CLKOUT pin is
        determined by the CLKOUTEN Configuration bit. When CLKOUTEN is set (CLKOUTEN = 1), the pin
        functions as a general-purpose I/O. When CLKOUTEN is clear (CLKOUTEN = 0), the system instruction
        clock (FOSC/4) is available as an output signal on the pin.

12.1.2.1 HFINTOSC
        The High-Frequency Internal Oscillator (HFINTOSC) is a factory-calibrated, precision digitally-
        controlled internal clock source that produces a wide range of stable clock frequencies. The
        HFINTOSC can be enabled through one of the following methods:
        • Program the RSTOSC Configuration bits to select the HFINTOSC upon device Reset or power-up.
        •   Write to the New Oscillator Source Request (NOSC) bits to select the HFINTOSC during run time.
        The HFINTOSC frequency is selected via the HFINTOSC Frequency Selection (FRQ) bits. Fine-tuning
        of the HFINTOSC is done via the HFINTOSC Frequency Tuning (TUN) bits. The HFINTOSC output
        frequency can be divided (post-scaled) via the New Divider Selection Request (NDIV) bits.

12.1.2.1.1 HFINTOSC Frequency Tuning
        The HFINTOSC frequency can be fine-tuned via the HFINTOSC Tuning (OSCTUNE) register. The
        OSCTUNE register is used by Active Clock Tuning hardware or user software to provide small
        adjustments to the HFINTOSC nominal frequency.
        The OSCTUNE register contains the HFINTOSC Frequency Tuning (TUN) bits. The TUN bits default
        to a 6-bit, two’s compliment value of 0x00, which indicates that the oscillator is operating at the
        selected frequency. When a value between 0x01 and 0x1F is written to the TUN bits, the HFINTOSC
        frequency is increased. When a value between 0x3F and 0x20 is written to the TUN bits, the
        HFINTOSC frequency is decreased.
        When the OSCTUNE register is modified, the oscillator will begin to shift to the new frequency. Code
        execution continues during this shift. There is no indication that the frequency shift occurred.


                     Important: OSCTUNE tuning does not affect the LFINTOSC frequency.


12.1.2.2 MFINTOSC
        The Medium-Frequency Internal Oscillator (MFINTOSC) generates two constant clock outputs (500
        kHz and 31.25 kHz). The MFINTOSC clock signals are created from the HFINTOSC using dynamic
        divider logic, which provides constant MFINTOSC clock rates regardless of selected HFINTOSC
        frequency.
        The MFINTOSC cannot be used as the system clock, but can be used as a clock source for certain
        peripherals, such as a Timer.

12.1.2.3 LFINTOSC
        The Low-Frequency Internal Oscillator (LFINTOSC) is a factory-calibrated 31 kHz internal clock
        source.
        The LFINTOSC can be used as a system clock source and may be used by certain peripheral modules
        as a clock source. Additionally, the LFINTOSC provides a time base for the following:
        •   Power-up Timer (PWRT)
        •   Watchdog Timer (WDT)/Windowed Watchdog Timer (WWDT)
        •   Fail-Safe Clock Monitor (FSCM)
        The LFINTOSC is enabled through one of the following methods:


--- p182 ---
        •   Program the RSTOSC Configuration bits to select LFINTOSC
        •   Write the NOSC bits to select LFINTOSC during run time

12.1.2.4 ADCRC
        The Analog-to-Digital RC (ADCRC) oscillator is dedicated to the ADC module. ADCRC operates at a
        fixed frequency of approximately 600 kHz and is used as a conversion clock source. The ADCRC
        allows the ADC module to operate in Sleep mode, which can reduce system noise during the ADC
        conversion. The ADCRC is automatically enabled when it is selected as the clock source for the ADC
        module or when selected as the clock source of any peripheral that may use it. The ADCRC may also
        be manually enabled via the ADC Oscillator Enable (ADOEN) bit, thereby avoiding start-up delays
        when this source is used intermittently.

12.1.3 Oscillator Status and Manual Enable
        The Oscillator Status (OSCSTAT) register displays the Ready status for each of the following
        oscillators:
        • External oscillator
        •   HFINTOSC
        •   MFINTOSC
        •   LFINTOSC
        •   SOSC
        •   ADCRC
        The OSCSTAT register also displays the Ready status for the 4xPLL.
        The HFINTOSC Oscillator Ready (HFOR) and MFINTOSC Oscillator Ready (MFOR) Status bits indicate
        whether the respective oscillators are ready for use. Both clock sources are available for use at any
        time but may require a finite amount of time before they have reached the specified accuracy levels.
        When the HFINTOSC or MFINTOSC are ready and achieved the specified accuracy, module hardware
        sets the HFOR/MFOR bits, respectively.
        When a new value is loaded into the OSCFRQ register, the HFOR and MFOR bits are cleared by
        hardware and will be set again once the respective oscillator is ready. During pending OSCFRQ
        changes, the MFINTOSC will stall at either a high or a low state until the HFINTOSC locks in the new
        frequency and resumes operation.
        The Oscillator Enable (OSCEN) register can be used to manually enable the following oscillators:
        • External oscillator
        •   HFINTOSC
        •   MFINTOSC
        •   LFINTOSC
        •   SOSC
        •   ADCRC


                    Important: OSCEN cannot be used to manually enable the 4xPLL.


12.2    Clock Switching
        The system clock source can be switched between external and internal clock sources via software
        using the New Oscillator Source Request (NOSC) and New Divider Selection Request (NDIV) bits. The
        following sources can be selected:


--- p183 ---
       •   External Oscillator (EXTOSC)
       •   EXTOSC with 4x PLL
       •   High-Frequency Internal Oscillator (HFINTOSC)
       •   Low-Frequency Internal Oscillator (LFINTOSC)
       •   Secondary Oscillator (SOSC)
       The Clock Switch Enable (CSWEN) Configuration bit can be used to enable or disable the clock
       switching capability. When CSWEN is set (CSWEN = 1), writes to NOSC and NDIV by user software will
       allow the system clock to switch between sources or frequencies. When CSWEN is clear (CSWEN = 0),
       writes to NOSC and NDIV are ignored, preventing the system clock from switching from one source
       to another.

12.2.1 NOSC and NDIV Bits
       The New Oscillator Source Request (NOSC) and New Divider Selection Request (NDIV) bits are used
       to select the system clock source and clock frequency divider that will be used by the CPU and
       peripherals (see the tables below).
       When new values are written into NOSC and/or NDIV, the current oscillator selection will continue
       to operate as the system clock while waiting for the new source to indicate that it is ready. Writes
       to NDIV without changing the clock source (e.g., changing the HFINTOSC frequency from 1 MHz to 2
       MHz) are handled in the same manner as a clock switch.
       When the new oscillator selection is ready, the New Oscillator is Ready (NOSCR) bit and the Clock
       Switch Interrupt Flag (CSWIF) are set by module hardware. If the Clock Switch Interrupt Enable
       (CSWIE) bit is set (CSWIE = 1), an interrupt will be generated when CSWIF is set. Additionally, the
       Oscillator Ready (ORDY) bit can be polled to determine that the clock switch has completed and the
       new oscillator source has replaced the old source as the system clock.


                    Important: The CSWIF interrupt does not wake the device from Sleep.


       Table 12-2. NOSC/COSC Clock Source Selection Table
                         NOSC / COSC                                                 Clock Source
                              111                                                         EXTOSC(1)
                              110                                                     HFINTOSC(2)
                              101                                                         LFINTOSC
                              100                                                           SOSC
                              011                                                         Reserved
                              010                                                  EXTOSC + 4xPLL(3)
                              001                                                         Reserved
                              000                                                         Reserved

       Notes:
       1. EXTOSC is configured via the FEXTOSC Configuration bits.
       2. HFINTOSC frequency is determined by the FRQ bits.
       3. EXTOSC must meet the PLL specifications (see the data sheet Electrical Specifications).

       Table 12-3. NDIV/CDIV Clock Divider Selection Table
                            NDIV / CDIV                                                   Clock Divider
                            1111-1010                                                       Reserved


--- p184 ---
       ...........continued
                              NDIV / CDIV                                                   Clock Divider
                                 1001                                                           512
                                 1000                                                           256
                                 0111                                                           128
                                 0110                                                            64
                                 0101                                                            32
                                 0100                                                            16
                                 0011                                                            8
                                 0010                                                            4
                                 0001                                                            2
                                 0000                                                            1


12.2.2 COSC and CDIV Bits
       The Current Oscillator Source Select (COSC) bits and the Current Divider Select (CDIV) bits indicate
       the current oscillator source and clock divider, respectively. When a new oscillator or divider is
       requested via the NOSC/NDIV bits, the COSC and CDIV bits remain unchanged until the clock switch
       actually occurs. When the switch actually occurs, hardware copies the NOSC and NDIV values into
       COSC and CDIV, the Oscillator Ready (ORDY) bit is set, and the NOSCR bit is cleared by hardware,
       indicating that the clock switch is complete.

12.2.3 CSWHOLD
       When the system oscillator changes frequencies, peripherals using the system clock may be
       affected. For example, if the I2C module is actively using the system clock as its Serial Clock (SCL)
       time base, changing the system clock frequency will change the SCL frequency. The Clock Switch
       Hold (CSWHOLD) bit can be used to suspend a requested clock switch. In this example, software can
       request a new clock source, use the CSWHOLD bit to suspend the switch, wait for the I2C bus to
       become Idle, then reconfigure the SCL frequency based on the new clock source. Once the I2C has
       been reconfigured, software can use CSWHOLD to complete the clock switch without causing any
       issues with the I2C bus.
       When CSWHOLD is set (CSWHOLD = 1), a write to NOSC and/or NDIV is accepted, but the clock
       switch is suspended and does not automatically complete. While the switch is suspended, code
       execution continues using the old (current) clock source. Module hardware will still enable the new
       oscillator selection and set the NOSCR bit. Once the NOSCR bit is set, software will either:
       • clear CSWHOLD so that the clock switch can complete, or
       •   copy the Current Oscillator Source Select (COSC) value into NOSC to abandon the clock switch.
       When CSWHOLD is clear (CSWHOLD = 0), the clock switch will occur when the NOSCR bit is set.
       When NOSCR is set, the CSWIF is also set, and if CSWIE is set, the generated interrupt will be serviced
       using the new oscillator.

12.2.4 PLL Input Switch
       Switching between the PLL and any non-PLL source is handled in the same manner as any other
       clock source change.
       When the NOSC selects a source with a PLL, the system continues to operate using the current
       oscillator until the new oscillator is ready. When the new source is ready, the associated Status bit in
       the Oscillator Status (OSCSTAT) register is set, and once the PLL is locked and ready for use, the PLL
       is Ready (PLLR) bit is set. Once both the source and PLL are ready, the switch will complete.

12.2.5 Clock Switch and Sleep
       If the NOSC/NDIV bits are written with new values and the device is put to Sleep before the clock
       switch completes, the switch will not take place and the device will enter Sleep mode.


--- p185 ---
When the device wakes up from Sleep and CSWHOLD is clear (CSWHOLD = 0), the clock switch will
complete  and the device
     Filename:       Clockwill wake
                           Switch    with the
                                  (CSWHOLD    new clock active, setting CSWIF.
                                            = 0).vsdx
      Title:
When Last
       theEdit:
            device wakes   from Sleep and CSWHOLD is set (CSWHOLD = 1), the device will wake up
                        3/5/2019
      First Used:
with the  old clock active, and the new clock source will be requested again.
      Notes:
If Doze mode is in effect, the clock switch occurs on the next clock cycle regardless of whether or not
the CPU is active during that clock cycle.

Figure 12-7. Clock Switch (CSWHOLD = 0)


                               OSC #1                                 OSC #2

                            NOSC written

                                                                 Switch
               ORDY                                             complete


                                                                     Cleared by
               NOSCR                                                 hardware(2)


                                                                       Cleared by
               CSWIF                                                   software(1)


                                             Cleared by
         CSWHOLD                              software


Notes:
1. CSWIF is asserted coincident with NOSCR; interrupt is serviced at OSC#2 speed.
2. The assertion of NOSCR may not be seen by the user as it is only set for the duration of the
   switch.


--- p186 ---
Figure 12-8. Clock Switch (CSWHOLD = 1)


                                               OSC #1                                 OSC #2

                           NOSC written

                                                                                          Switch
           ORDY                                                                          complete


                                                                                         Cleared by
          NOSCR                                                                          hardware
                         New oscillator                    Cleared by
                           is ready                        software(1)

          CSWIF


                                                                                 Cleared by
        CSWHOLD                                                                   software


Note:
1. CSWIF may be cleared before or after clearing CSWHOLD.


--- p187 ---
           Notes:


       Figure 12-9. Clock Switch Abandoned


                                                                OSC #1

                              NOSC written                                       NOSC written


                ORDY


                                                                                                   Cleared by
               NOSCR                                                                               hardware
                            New oscillator                  Cleared by
                              is ready                      software(1)

                CSWIF


                                                                                                     Cleared by
             CSWHOLD                               New oscillator
                                                                                                      software
                                                    is ready, but
                                                     held while
                                                                                                New value
                                                   CSWHOLD = 1
                                                                                                 written to
                                                                                                NOSC, old
                                                                                               clock switch
                                                                                                 request is
                                                                                                abandoned


       Note:
       1. CSWIF may be cleared before or after rewriting NOSC; CSWIF is not automatically cleared.

12.3   Fail-Safe Clock Monitor (FSCM)
       The Fail-Safe Clock Monitor (FSCM) allows the device to continue operating in the event of an
       oscillator failure. The FSCM also provides diagnostic data pertaining to potential primary and
       secondary oscillator failures. The FSCM serves three separate functions:
       •    Monitoring of FOSC using the FSCMFEV bit
       •    Monitoring of EXTOSC (primary external oscillator) using the FSCMPEV bit
       •    Monitoring of SOSC (secondary external oscillator) using the FSCMSEV bit
       The primary external oscillator FSCM (FSCMP) is enabled by setting the Fail-Safe Clock Monitor
       for Primary Crystal Oscillator (FCMENP) Configuration bit. The secondary external oscillator FSCM
       (FSCMS) is enabled by setting the Fail-Safe Clock Monitor for Secondary Crystal Oscillator (FCMENS)
       Configuration bit. The FOSC FSCM is enabled by setting the Fail-Safe Clock Monitor Enable for FOSC
       (FCMEN) Configuration bit. The figure below shows the FSCM block diagram.


--- p188 ---
        Figure 12-10. FSCM Block Diagram

                                                          Clock Monitor
                                                              Latch
                                                            S         Q


                                                                             FSCMEN
                     System Oscillator
                          (FOSC)                            R         Q                                       FOSC Failure
                                                                                                                Detected
                      Primary External
                         Oscillator                         S         Q

                         (EXTOSC)
                                                                             FSCMENP
                        Secondary
                         External                           R         Q                                     EXTOSC Failure
                     Oscillator (SOSC)                                                                         Detected

                                                            S         Q


               LFINTOSC                  ÷ 64                                FSCMENS

                  31 kHz             484 Hz                 R         Q
                 (~32 µs)            (~2 ms)                                                                 SOSC Failure
                                                                                                               Detected
                      Sample Clock


12.3.1 Fail-Safe Detection
        Each FSCM detects a failed oscillator by comparing the external oscillator to the FSCM sample clock.
        The sample clock is generated by dividing the LFINTOSC by 64. The fail detector logic block contains
        a latch that is set upon each falling edge of the external clock. The latch is cleared on the rising edge
        of the sample clock. A failure is detected when a half-period of the sample clock elapses before the
        external clock goes low and the corresponding FSCM failure status bit will be set.

12.3.2 Fail-Safe Operation - FOSC Fail-Safe Clock Monitor
        When the system clock (FOSC) fails, the Oscillator Fail Interrupt Flag (OSFIF) bit of the PIR registers,
        as well as the corresponding FSCM failure status (FSCMFEV) bit, will be set. If the Oscillator Fail
        Interrupt Enable (OSFIE) bit was set, an interrupt will be generated when OSFIF is high. If enabled,
        the FOSC Fail-Safe Clock Monitor will switch the system clock to HFINTOSC when a failure is detected
        by overwriting the NOSC/COSC bits. The frequency of HFINTOSC will depend on the previous state
        of the FRQ bits and the state of the NDIV/CDIV bits. Once a failure is detected, software can be
        used to take steps to mitigate the repercussions of the oscillator failure. The FSCM will switch the
        system clock to HFINTOSC, and the device will continue to operate from HFINTOSC until the external
        oscillator has been restarted. Once the external source is operational, it is up to the user to confirm
        that the clock source is stable and to switch the system clock back to the external oscillator using the
        NOSC/NDIV bits.

12.3.3 Fail-Safe Operation - Primary and Secondary Fail-Safe Clock Monitors
        When the primary external clock (EXTOSC) or the secondary external clock (SOSC) fail, the Oscillator
        Fail Interrupt Flag (OSFIF) bit of the PIR registers will be set. Additionally, the corresponding FSCM
        failure status bit (FSCMPEV or FSCMSEV, respectively) will be set. If the Oscillator Fail Interrupt
        Enable (OSFIE) bit has been set, an interrupt will be generated when OSFIF is high. It is important
        to note that neither the primary or secondary Fail-Safe Clock Monitors will cause a clock switch to
        occur in the event of a failure, and it is up to the user to address the clock fail event.


--- p189 ---
12.3.4 Fail-Safe Clock Monitor Fault Injection
        Each of the Fail-Safe Clock monitors on this device has its own respective Fault Injection bit. The
        Fault Injection bit is used to verify in the software that the FSCM functions work properly and that
        they will detect a clock failure during normal operation. If the FSCM Fault Injection bit is set, the
        FSCM sample clock input will be blocked, forcing a clock failure. Writing to the FOSC FSCM Fault
        Injection (FSCMFFI) bit will result in the system clock switching to HFINTOSC and the FSCMFEV bit
        as well as the Oscillator Fail Interrupt Flag (OSFIF) of the PIR registers being set. Writing to the
        primary and secondary external FSCM Fault Injection (FSCMPFI and FSCMSFI) bits will result in the
        respective FSCM Fault Status (FSCMPEV and FSCMSEV) bits being set but the system clock will not
        switch. Additionally, the Oscillator Fail Interrupt Flag (OSFIF) of the PIR registers will also be set.

12.3.5 Fail-Safe Condition Clearing
        For the FOSC FSCM, the Fail-Safe condition is cleared after either a device Reset, execution of a
        SLEEP instruction, or a change to the NOSC/NDIV bits. When switching to the external oscillator
        or PLL, the Oscillator Start-up Timer (OST) is restarted. While the OST is running, the device
        continues to operate from HFINTOSC. When the OST expires, the Fail-Safe condition is cleared after
        successfully switching to the external clock source.


                    Important: Software must clear the OSFIF bit before switching to the external oscillator. If
                    the Fail-Safe condition still exists, the OSFIF bit will be set again by module hardware.


12.3.6 Reset or Wake-Up from Sleep
        The FSCM is designed to detect an oscillator failure after the OST has expired. The OST is used after
        waking up from Sleep or after any type of Reset, when in either LP, XT or HS mode. If the device is
        using the EC mode, the FSCM will be active as soon as the Reset or wake-up event has completed.

12.4    Active Clock Tuning (ACT)
        Many applications, such as those using UART communication, require an oscillator with an accuracy
        of ± 1% over the full temperature and voltage range. To meet this level of accuracy, the Active
        Clock Tuning (ACT) feature utilizes the SOSC frequency of 32.768 kHz to adjust the frequency of the
        HFINTOSC over voltage and temperature.


                    Important: Active Clock Tuning requires the use of a 32.768 kHz external oscillator
                    connected to the SOSCI/SOSCO pins.


        Active Clock Tuning is enabled via the Active Clock Tuning Enable (ACTEN) bit. When ACTEN is set
        (ACTEN = 1), the ACT module uses the SOSC time base to measure the HFINTOSC frequency and
        uses the HFINTOSC Frequency Tuning (TUN) bits to adjust the HFINTOSC frequency. When ACTEN is
        clear (ACTEN = 0), the ACT feature is disabled, and user software can utilize the TUN bits to adjust
        the HFINTOSC frequency.


                    Important: When the ACT feature is enabled, the TUN bits are controlled directly through
                    module hardware and become read-only bits to user software. Writes to the TUN bits when
                    the ACT feature is enabled are ignored.


        The figure below shows the Active Clock Tuning block diagram.


--- p190 ---
                                                                                                                          2/25/2019


                                                                          OSC - Oscillator Module (With Fail-Safe Clock Monitor)

       Figure 12-11. Active Clock Tuning (ACT) Block Diagram


                                             ACTEN

                              ACT clock
              SOSC                                                       HFINTOSC

                                           Active Clock
                                           Tuning Block
                                                             ACT data                 SFR data

                                                                                                           Software write
                                                                                                            to OSCTUNE

                      ACTUD                                              TUN[5:0]
                                                                                                                   ACTEN

                           ACTEN


12.4.1 ACT Lock Status
       The Active Clock Tuning Lock Status (ACTLOCK) bit can be used to determine when the HFINTOSC
       has been tuned. When ACTLOCK is set (ACTLOCK = 1), the HFINTOSC frequency has been locked
       to within ± 1% of the nominal frequency. When ACTLOCK is clear (ACTLOCK = 0), the following
       conditions may be true:
       • The HFINTOSC frequency has not been locked to within ± 1%
       •   A device Reset occurred
       •   The ACT feature is disabled


                     Important: The ACTLOCK bit is read-only. Writes to ACTLOCK are ignored.


12.4.2 ACT Out-of-Range Status
       When Active Clock Tuning is enabled, module hardware uses the TUN bits to achieve high accuracy
       levels. If the module requires a TUN value outside of its range, the ACT Out-of-Range Status
       (ACTORS) bit is set by hardware (ACTORS = 1).
       The ACTORS bit will be set when:
       • The HFINTOSC is tuned to its lowest frequency as determined by the TUN bits and will require a
         value lower than the TUN bits can provide to achieve accuracy within ± 1%.
       •   The HFINTOSC is tuned to its highest frequency as determined by the TUN bits and will require a
           value higher than the TUN bits can provide to achieve accuracy within ± 1%.
       When an ACT out-of-range event occurs, the HFINTOSC will continue to use the last TUN value until
       the HFINTOSC frequency returns to the tunable range. Once the HFINTOSC returns to the tunable
       range, module hardware clears the ACTORS bit.


                     Important: The ACTORS bit is read-only. Writes to ACTORS are ignored.


--- p191 ---
12.4.3 ACT Update Disable
       When Active Clock Tuning is enabled, the OSCTUNE register is continuously updated every ACT
       clock cycle. The ACT Update Disable (ACTUD) bit can be used to suspend updates to the OSCTUNE
       register. When ACTUD is set (ACTUD = 1), updates to OSCTUNE are suspended, although the module
       continues to operate. The last value written to OSCTUNE is used for tuning, and the ACTLOCK bit
       is continually updated for each ACT cycle. When ACTUD is clear (ACTUD = 0), the module updates
       OSCTUNE register every ACT cycle.

12.4.4 ACT Interrupts
       When Active Clock Tuning is enabled (ACTEN = 1) and the ACTLOCK or ACTORS bit changes state
       (e.g., from a Locked to an Unlocked state), the ACT Interrupt Flag (ACTIF) of the PIR registers is set
       (ACTIF = 1). If the ACT Interrupt Enable (ACTIE) bit is set (ACTIE = 1), an interrupt will be generated
       when ACTIF becomes set. No interrupts are generated for each OSCTUNE update unless the update
       results in a change of Lock status or Out-of-Range status.

12.5   Register Definitions: Oscillator Module


--- p192 ---
12.5.1 ACTCON

           Name:        ACTCON
           Address:     0x0AC

           Active Clock Tuning Control Register

     Bit         7            6                5              4               3               2              1               0
               ACTEN        ACTUD                                          ACTLOCK                        ACTORS
  Access        R/W          R/W                                              R                              R
   Reset         0            0                                               0                              0

Bit 7 – ACTEN Active Clock Tuning Enable
           Value       Description
           1           ACT enabled: HFINTOSC tuning is controlled by the ACT
           0           ACT disabled: HFINTOSC tuning is controlled by the OSCTUNE register via user software

Bit 6 – ACTUD Active Clock Tuning Update Disable
           Value       Condition      Description
           1           ACTEN = 1      Updates to the OSCTUNE register from ACT hardware are disabled
           0           ACTEN = 1       Updates to the OSCTUNE register from ACT hardware are allowed
           x           ACTEN = 0       Updates to the OSCTUNE register through user software are allowed


Bit 3 – ACTLOCK Active Clock Tuning Lock Status
           Value       Description
           1           Locked: HFINTOSC is within ± 1% of its nominal value
           0           Not locked: HFINTOSC may or may not be within ± 1% of its nominal value

Bit 1 – ACTORS Active Clock Tuning Out-of-Range Status
           Value       Description
           1           Value required for tuning is outside of the OSCTUNE range
           0           Value required for tuning is within the OSCTUNE range


--- p193 ---
12.5.2 OSCCON1

            Name:       OSCCON1
            Address:    0x0AD

            Oscillator Control Register 1

      Bit        7            6           5                4                   3                2                1             0
                                       NOSC[2:0]                                                    NDIV[3:0]
  Access                     R/W         R/W             R/W                  R/W             R/W               R/W           R/W
   Reset                      f           f               f                    q               q                 q             q

Bits 6:4 – NOSC[2:0] New Oscillator Source Request(1,2,3)
          Requests a new oscillator source per the NOSC/COSC Clock Source Selection Table.

Bits 3:0 – NDIV[3:0] New Divider Selection Request
          Requests the new postscaler division ratio per the NDIV/CDIV Clock Divider Selection Table.

            Notes:
            1. The default value is determined by the RSTOSC Configuration bits. See the Reset Oscillator
               (RSTOSC) selection table for the RSTOSC selections.
            2. If NOSC is written with a reserved value, the operation is ignored and neither NOSC nor NDIV is
               written.
            3. When CSWEN = 0, these bits are read-only and cannot be changed from the RSTOSC value.


--- p194 ---
12.5.3 OSCCON2

            Name:       OSCCON2
            Address:    0x0AE

            Oscillator Control Register 2

      Bit        7            6           5                4                  3                2               1              0
                                       COSC[2:0]                                                   CDIV[3:0]
  Access                      R           R                R                  R                R               R              R
   Reset                      f           f                f                  f                f               f              f

Bits 6:4 – COSC[2:0] Current Oscillator Source Select (read-only)(1)
          Indicates the current oscillator source per the NOSC/COSC Clock Source Selection Table.

Bits 3:0 – CDIV[3:0] Current Divider Select (read-only)
          Indicates the current postscaler divider ratio per the NDIV/CDIV Clock Divider Table.

            Note:
            1. The RSTOSC value is the value present when user code execution begins. Refer to the RSTOSC
               Configuration bits or the RSTOSC selection table for the Reset Oscillator selections.


--- p195 ---
12.5.4 OSCCON3

            Name:       OSCCON3
            Address:    0x0AF

            Oscillator Control Register 3

      Bit        7            6                 5             4               3                2               1             0
             CSWHOLD       SOSCPWR                           ORDY           NOSCR
  Access      R/W/HC         R/W                              R               R
   Reset         0            1                               0               0

Bit 7 – CSWHOLD Clock Switch Hold Control
            Value      Description
            1          Clock switch (and interrupt) will hold when the oscillator selected by NOSC is ready
            0          Clock switch will proceed when the oscillator selected by NOSC is ready

Bit 6 – SOSCPWR Secondary Oscillator Power Mode Select
            Value      Description
            1          Secondary Oscillator operates in High Power mode
            0          Secondary Oscillator operates in Low Power mode

Bit 4 – ORDY Oscillator Ready (read-only)
            Value      Description
            1          OSCCON1 = OSCCON2; the current system clock is the clock specified by NOSC
            0          A clock switch is in progress

Bit 3 – NOSCR New Oscillator is Ready (read-only)(1)
            Value      Description
            1          A clock switch is in progress and the oscillator selected by NOSC indicates a Ready condition
            0          A clock switch is not in progress, or the NOSC-selected oscillator is not ready

            Note:
            1. If CSWHOLD = 0, the user may not see this bit set (NOSCR = 1). When the oscillator becomes
               ready, there may be a delay of one instruction cycle before NOSCR is set. The clock switch occurs
               in the next instruction cycle and NOSCR is cleared.


--- p196 ---
12.5.5 OSCTUNE

           Name:       OSCTUNE
           Address:    0x0B0

           HFINTOSC Frequency Tuning Register

     Bit        7              6               5               4                   3                2               1              0
                                                                                        TUN[5:0]
  Access                                     R/W             R/W                  R/W              R/W            R/W             R/W
   Reset                                      0               0                    0                0              0               0

Bits 5:0 – TUN[5:0] HFINTOSC Frequency Tuning
              TUN                                                          Condition
           01 1111    Maximum frequency
           •          •
           •          •
           •          •
           00 0000    Center frequency. Oscillator is operating at the selected nominal frequency. (Default value)
           •          •
           •          •
           •          •
           10 0000    Minimum frequency


--- p197 ---
12.5.6 OSCFRQ

           Name:      OSCFRQ
           Address:   0x0B1

           HFINTOSC Frequency Selection Register

     Bit        7           6          5              4                   3                2               1              0
                                                                                               FRQ[3:0]
  Access                                                                 R/W             R/W              R/W            R/W
   Reset                                                                  0               0                0              0

Bits 3:0 – FRQ[3:0] HFINTOSC Frequency Selection
                           FRQ                                                    Nominal Freq (MHz)
                        1111-1001                                                      Reserved
                           1000                                                           64
                          0111                                                            48
                          0110                                                            32
                          0101                                                            16
                          0100                                                            12
                          0011                                                            8
                          0010                                                            4
                          0001                                                            2
                          0000                                                            1


--- p198 ---
12.5.7 OSCSTAT

            Name:       OSCSTAT
            Address:    0x0B2

            Oscillator Status Register

      Bit        7             6               5                4                 3            2                1             0
               EXTOR         HFOR             MFOR            LFOR               SOR         ADOR             SFOR           PLLR
  Access         R             R               R                R                 R            R                R             R
   Reset         0             0               0                0                 0            0                0             0

Bit 7 – EXTOR External Oscillator Ready
            Value      Description
            1          The External oscillator is ready for use
            0          The External oscillator is not enabled, or is not ready for use

Bit 6 – HFOR HFINTOSC Ready
            Value      Description
            1          The HFINTOSC is ready for use
            0          The HFINTOSC is not enabled, or it is not ready for use

Bit 5 – MFOR MFINTOSC Ready
            Value      Description
            1          The MFINTOSC is ready for use
            0          The MFINTOSC is not enabled, or it is not ready for use

Bit 4 – LFOR LFINTOSC Ready
            Value      Description
            1          The LFINTOSC is ready for use
            0          The LFINTOSC is not enabled, or is not ready for use

Bit 3 – SOR Secondary Oscillator (SOSC) Ready
            Value      Description
            1          The Secondary oscillator is ready for use
            0          The Secondary oscillator is not enabled, or is not ready for use

Bit 2 – ADOR ADCRC Oscillator Ready
            Value      Description
            1          The ADCRC oscillator is ready for use
            0          The ADCRC oscillator is not enabled, or is not ready for use

Bit 1 – SFOR SFINTOSC Ready
            Value      Description
            1          The SFINTOSC is ready for use
            0          The SFINTOSC is not enabled, or is not ready for use

Bit 0 – PLLR PLL is Ready
            Value      Description
            1          The PLL is ready for use
            0          The PLL is not enabled, the required input source is not ready, or the PLL is not locked


--- p199 ---
12.5.8 OSCEN

            Name:       OSCEN
            Address:    0x0B3

            Oscillator Enable Register

      Bit        7            6               5               4              3              2                1             0
              EXTOEN        HFOEN           MFOEN           LFOEN         SOSCEN          ADOEN                          PLLEN
  Access        R/W          R/W             R/W             R/W            R/W            R/W                            R/W
   Reset         0            0               0               0              0              0                              0

Bit 7 – EXTOEN External Oscillator Enable
            Value      Description
            1          EXTOSC is explicitly enabled, operating as specified by FEXTOSC
            0          EXTOSC can be enabled by a peripheral request

Bit 6 – HFOEN HFINTOSC Enable
            Value      Description
            1          HFINTOSC is explicitly enabled, operating as specified by OSCFRQ
            0          HFINTOSC can be enabled by a peripheral request

Bit 5 – MFOEN MFINTOSC Enable
            Value      Description
            1          MFINTOSC is explicitly enabled
            0          MFINTOSC can be enabled by a peripheral request

Bit 4 – LFOEN LFINTOSC Enable
            Value      Description
            1          LFINTOSC is explicitly enabled
            0          LFINTOSC can be enabled by a peripheral request

Bit 3 – SOSCEN Secondary Oscillator Enable
            Value      Description
            1          SOSC is explicitly enabled, operating as specified by SOSCPWR
            0          SOSC can be enabled by a peripheral request

Bit 2 – ADOEN ADCRC Oscillator Enable
            Value      Description
            1          ADCRC is explicitly enabled
            0          ADCRC may be enabled by a peripheral request

Bit 0 – PLLEN PLL Enable(1)
            Value      Description
            1          EXTOSC multiplied by the 4x system PLL is used by a peripheral request
            0          EXTOSC is used by a peripheral request

            Note:
            1. This bit only controls external clock source supplied to the peripherals and has no effect on the
               system clock.


--- p200 ---
12.5.9 FSCMCON

            Name:        FSCMCON
            Address:     0x458

            Fail-Safe Clock Monitor Control and Status Register

      Bit           7            6              5              4                3              2                   1          0
                                             FSCMSFI        FSCMSEV          FSCMPFI        FSCMPEV             FSCMFFI    FSCMFEV
  Access                                       R/W            R/W              R/W            R/W                 R/W        R/W
   Reset                                        0              0                0              0                   0          0

Bit 5 – FSCMSFI SOSC Fail-Safe Clock Monitor Fault Injection(1)
            Value       Description
            1           SOSC FSCM clock input is blocked; FSCM will time-out
            0           SOSC FSCM clock input is enabled; FSCM functions as indicated

Bit 4 – FSCMSEV SOSC Fail-Safe Clock Monitor Status(2)
            Value       Description
            1           SOSC clock showed a failure
            0           FSCM is detecting SOSC input clocks, or the bit was cleared by the user

Bit 3 – FSCMPFI Primary Oscillator Fail-Safe Clock Monitor Fault Injection(1)
            Value       Description
            1           Primary Oscillator FSCM clock input is blocked; FSCM will time-out
            0           Primary Oscillator FSCM clock input is enabled; FSCM functions as indicated

Bit 2 – FSCMPEV Primary Oscillator Fail-Safe Clock Monitor Status(2)
            Value       Description
            1           Primary Oscillator clock showed a failure
            0           FSCM is detecting primary oscillator input clocks, or the bit was cleared by the user

Bit 1 – FSCMFFI FOSC Fail-Safe Clock Monitor Fault Injection(1)
            Value       Description
            1           FOSC FSCM clock input is blocked; FSCM will time-out
            0           FOSC FSCM clock input is enabled; FSCM functions as indicated

Bit 0 – FSCMFEV FOSC Fail-Safe Clock Monitor Status(2)
            Value       Description
            1           FOSC clock showed a failure
            0           FSCM is detecting FOSC input clocks, or the bit was cleared by the user

            Notes:
            1. This bit is used to demonstrate that FSCM can detect clock failure; the bit must be cleared for
               normal operation.
            2. This bit will not be cleared by hardware upon clock recovery; the bit must be cleared by the user.


--- p201 ---
12.6      Register Summary - Oscillator Module

Address     Name      Bit Pos.      7           6           5             4            3           2            1             0
 0x00
  ...      Reserved
 0xAB
  0xAC     ACTCON       7:0       ACTEN       ACTUD                                ACTLOCK                    ACTORS
  0xAD     OSCCON1      7:0                             NOSC[2:0]                                      NDIV[3:0]
  0xAE     OSCCON2      7:0                             COSC[2:0]                                      CDIV[3:0]
  0xAF     OSCCON3      7:0      CSWHOLD    SOSCPWR                   ORDY          NOSCR
  0xB0     OSCTUNE      7:0                                                             TUN[5:0]
  0xB1      OSCFRQ      7:0                                                                           FRQ[3:0]
  0xB2     OSCSTAT      7:0       EXTOR       HFOR       MFOR          LFOR          SOR          ADOR         SFOR         PLLR
  0xB3      OSCEN       7:0      EXTOEN       HFOEN      MFOEN        LFOEN         SOSCEN       ADOEN                     PLLEN
  0xB4
   ...     Reserved
 0x0457
 0x0458    FSCMCON      7:0                              FSCMSFI     FSCMSEV        FSCMPFI     FSCMPEV      FSCMFFI      FSCMFEV


--- p202 ---
