4.      Guidelines for Getting Started with PIC18-Q41 Microcontrollers
4.1     Basic Connection Requirements
        Getting started with the PIC18-Q41 family of 8-bit microcontrollers requires attention to a minimal
        set of device pin connections before proceeding with development.
        The following pins must always be connected:
        •   All VDD and VSS pins (see the Power Supply Pins section)
        •   MCLR pin (see the Master Clear (MCLR) Pin section)
        These pins must also be connected if they are being used in the end application:
        •   ICSPCLK/ICSPDAT pins used for In-Circuit Serial Programming™ (ICSP™) and debugging purposes
            (see the In-Circuit Serial Programming (ICSP) Pins section)
        •   OSCI and OSCO pins when an external oscillator source is used (see the External Oscillator Pins
            section)
        Additionally, the following pins may be required:
        •   VREF+/VREF- pins are used when external voltage reference for analog modules is implemented
        The minimum mandatory connections are shown in the figure below.

        Figure 4-1. Recommended Minimum Connections

                                                                                          Rev. 10-000249C
                                                                                                  4/1/2019


                                             VDD                               C2


                                           R1
                                                                         VDD

                                                                                    VSS


                                                     R2
                                                           MCLR
                                           C1


                                                                  PIC® MCU
                                                           VSS


                                                Key:
                                                C1: 0.1 F, 20V ceramic (recommended)
                                                R1: 10 kΩ (recommended)
                                                R2: 100Ω to 470Ω (recommended)
                                                C2: 0.1 F, 20V ceramic (required)


4.2     Power Supply Pins
4.2.1   Decoupling Capacitors
        The use of decoupling capacitors on every pair of power supply pins (VDD and VSS) is required.
        Consider the following criteria when using decoupling capacitors:
        •   Value and type of capacitor: A 0.1 μF (100 nF), 10-20V capacitor is recommended. The capacitor
            needs to be a low-ESR device, with a resonance frequency in the range of 200 MHz and higher.
            Ceramic capacitors are recommended.
        •   Placement on the printed circuit board: The decoupling capacitors need to be placed as close to
            the pins as possible. It is recommended to place the capacitors on the same side of the board as
            the device. If space is constricted, the capacitor can be placed on another layer on the PCB using


--- p17 ---
            a via; however, ensure that the trace length from the pin to the capacitor is no greater than 0.25
            inch (6 mm).
        •   Handling high-frequency noise: If the board is experiencing high-frequency noise (upward of tens
            of MHz), add a second ceramic type capacitor in parallel to the above described decoupling
            capacitor. The value of the second capacitor can be in the range of 0.01 μF to 0.001 μF. Place
            this second capacitor next to each primary decoupling capacitor. In high-speed circuit designs,
            consider implementing a decade pair of capacitances as close to the power and ground pins as
            possible (e.g., 0.1 μF in parallel with 0.001 μF).
        •   Maximizing performance: On the board layout from the power supply circuit, run the power and
            return traces to the decoupling capacitors first and then to the device pins. This ensures that the
            decoupling capacitors are first in the power chain. Equally important is to keep the trace length
            between the capacitor and the power pins to a minimum, thereby reducing PCB trace inductance.

4.2.2   Tank Capacitors
        On boards with power traces running longer than six inches in length, it is suggested to use a
        tank capacitor for integrated circuits, including microcontrollers, to supply a local power source.
        The value of the tank capacitor will be determined based on the trace resistance that connects the
        power supply source to the device and the maximum current drawn by the device in the application.
        In other words, select the tank capacitor that meets the acceptable voltage sag at the device. Typical
        values range from 4.7 μF to 47 μF.

4.3     Master Clear (MCLR) Pin
        The MCLR pin provides two specific device functions: Device Reset and Device Programming
        and Debugging. If programming and debugging are not required in the end application, a direct
        connection to VDD may be all that is required. The addition of other components, to help increase
        the application’s resistance to spurious Resets from voltage sags, may be beneficial. A typical
        configuration is shown in Figure 4-1. Other circuit designs may be implemented, depending on the
        application’s requirements.
        During programming and debugging, the resistance and capacitance that can be added to the
        pin must be considered. Device programmers and debuggers drive the MCLR pin. Consequently,
        specific voltage levels (VIH and VIL) and fast signal transitions must not be adversely affected.
        Therefore, specific values of R1 and C1 will need to be adjusted based on the application and PCB
        requirements. For example, it is recommended that the capacitor, C1, be isolated from the MCLR
        pin during programming and debugging operations by using a jumper (Figure 4-2). The jumper is
        replaced for normal run-time operations.
        Any components associated with the MCLR pin need to be placed within 0.25 inch (6 mm) of the pin.

        Figure 4-2. Example of MCLR Pin Connections
                                             VDD
                                                                               Rev. 30-000058A
                                                                                      4/5/2017


                                                R1
                                                           R2
                                                                 MCLR
                                                                 PIC® MCU
                                                JP
                                                 C1


                                                     
                                                                    

                                                    


--- p18 ---
      Notes:
      1. R1 ≤ 10 kΩ is recommended. A suggested starting value is 10 kΩ. Ensure that the MCLR pin VIH
         and VIL specifications are met.
      2. R2 ≤ 470Ω will limit any current flowing into MCLR from the extended capacitor, C1, in the
         event of MCLR pin breakdown, due to Electrostatic Discharge (ESD) or Electrical Overstress (EOS).
         Ensure that the MCLR pin VIH and VIL specifications are met.

4.4   In-Circuit Serial Programming™ (ICSP™) Pins
      The ICSPCLK and ICSPDAT pins are used for ICSP and debugging purposes. It is recommended
      to keep the trace length between the ICSP connector and the ICSP pins on the device as short
      as possible. If the ICSP connector is expected to experience an ESD event, a series resistor is
      recommended, with the value in the range of a few tens of ohms, not to exceed 100Ω.
      Pull-up resistors, series diodes and capacitors on the ICSPCLK and ICSPDAT pins are not
      recommended as they can interfere with the programmer/debugger communications to the device.
      If such discrete components are an application requirement, they need to be removed from the
      circuit during programming and debugging. Alternatively, refer to the AC/DC characteristics and
      timing requirements information in the respective device Flash programming specification for
      information on capacitive loading limits as well as pin input voltage high (VIH) and input low (VIL)
      requirements.
      For device emulation, ensure that the “Communication Channel Select” pins (i.e., ICSPCLK/ICSPDAT)
      programmed into the device match the physical connections for the ICSP to the Microchip
      debugger/emulator tool.

4.5   External Oscillator Pins
      Many microcontrollers have options for at least two oscillators: A high-frequency primary oscillator
      and a low-frequency secondary oscillator.
      The oscillator circuit needs to be placed on the same side of the board as the device. Place the
      oscillator circuit close to the respective oscillator pins with no more than 0.5 inch (12 mm) between
      the circuit components and the pins. The load capacitors have to be placed next to the oscillator
      itself, on the same side of the board.
      Use a grounded copper pour around the oscillator circuit to isolate it from surrounding circuits. The
      grounded copper pour needs to be routed directly to the MCU ground. Do not run any signal traces
      or power traces inside the ground pour. Also, if using a two-sided board, avoid any traces on the
      other side of the board where the crystal is placed.
      Layout suggestions are shown in the following figure. In-line packages may be handled with a
      single-sided layout that completely encompasses the oscillator pins. With fine-pitch packages, it is
      not always possible to completely surround the pins and components. A suitable solution is to
      tie the broken guard sections to a mirrored ground layer. In all cases, the guard trace(s) must be
      returned to ground.


--- p19 ---
Figure 4-3. Suggested Placement of the Oscillator Circuit


In planning the application’s routing and I/O assignments, ensure that adjacent PORT pins and other
signals in close proximity to the oscillator are benign (i.e., free of high frequencies, short rise and fall
times, and other similar noise).
For additional information and design guidance on oscillator circuits, refer to these Microchip
application notes, available at the corporate website (www.microchip.com):
                                                                                             ®
•   AN826, “Crystal Oscillator Basics and Crystal Selection for rfPIC™ and PICmicro Devices”
                             ®
•   AN849, “Basic PICmicro Oscillator Design”
                                 ®
•   AN943, “Practical PICmicro Oscillator Analysis and Design”
•   AN949, “Making Your Oscillator Work”


--- p20 ---
4.6   Unused I/Os
      Unused I/O pins need to be configured as outputs and driven to a Logic Low state. Alternatively,
      connect a 1 kΩ to 10 kΩ resistor to VSS on unused pins to drive the output to logic low.


--- p21 ---
