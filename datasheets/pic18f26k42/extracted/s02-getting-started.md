                      PIC18(L)F26/27/45/46/47/55/56/57K42
2.0      2017-2021GUIDELINES FOR                                            2.2      Power Supply Pins
         GETTING STARTED WITH
                                                                            2.2.1       DECOUPLING CAPACITORS
         PIC18(L)F26/27/45/46/47/55/56/
                                                                            The use of decoupling capacitors on every pair of
         57K42 MICROCONTROLLERS                                             power supply pins (VDD and VSS) is required.
                                                                            Consider the following criteria when using decoupling
2.1      Basic Connection Requirements
                                                                            capacitors:
Getting started with the PIC18(L)F26/27/45/46/47/55/                        • Value and type of capacitor: A 0.1 F (100 nF),
56/57K42 family of 8-bit microcontrollers requires                            10-20V capacitor is recommended. The capacitor
attention to a minimal set of device pin connections                          may be a low-ESR device, with a resonance
before proceeding with development.                                           frequency in the range of 200 MHz and higher.
The following pins must always be connected:                                  Ceramic capacitors are recommended.
• All VDD and VSS pins (see Section 2.2 “Power                              • Placement on the printed circuit board: The
  Supply Pins”)                                                               decoupling capacitors may be placed as close to
                                                                              the pins as possible. It is recommended to place
• MCLR pin (see Section 2.3 “Master Clear (MCLR)
                                                                              the capacitors on the same side of the board as
  Pin”)
                                                                              the device. If space is constricted, the capacitor
These pins must also be connected if they are being                           can be placed on another layer on the PCB using
used in the end application:                                                  a via; however, make sure that the trace length
• ICSPCLK/ICSPDAT pins used for In-Circuit Serial                             from the pin to the capacitor is no greater than
  Programming™ (ICSP™) and debugging purposes                                 0.25 inch (6 mm).
  (see Section 2.4 “ICSP™ Pins”)                                            • Handling high-frequency noise: If the board is
• OSCI and OSCO pins when an external oscillator                              experiencing high-frequency noise (upward of
  source is used (see Section 2.5 “External                                   tens of MHz), add a second ceramic type
  Oscillator Pins”)                                                           capacitor in parallel to the above described
                                                                              decoupling capacitor. The value of the second
Additionally, the following pins may be required:
                                                                              capacitor can be in the range of 0.01 F to
• VREF+/VREF- pins are used when external voltage                             0.001 F. Place this second capacitor next to
  reference for analog modules is implemented                                 each primary decoupling capacitor. In high-speed
The minimum mandatory connections are shown in                                circuit designs, consider implementing a decade
Figure 2-1.                                                                   pair of capacitances as close to the power and
                                                                              ground pins as possible (e.g., 0.1 F in parallel
                                                                              with 0.001 F).
FIGURE 2-1:            RECOMMENDED
                       MINIMUM CONNECTIONS                                  • Maximizing performance: On the board layout
                                                                              from the power supply circuit, run the power and
                                                         Rev. 10-000249A
                                                                 9/1/2015
                                                                              return traces to the decoupling capacitors first,
           VDD                                C2                              and then to the device pins. This ensures that the
                                                                              decoupling capacitors are first in the power chain.
         R1
                                                                              Equally important is to keep the trace length
                                        VDD

                                                   Vss


                 R2
                        MCLR                                                  between the capacitor and the power pins to a
         C1                                                                   minimum, thereby reducing PCB trace
                                                                              inductance.
                               PIC18(L)Fxxxxx
                        Vss                                                 2.2.2       TANK CAPACITORS
                                                                            On boards with power traces running longer than
                                                                            six inches in length, it is suggested to use a tank
        Key (all values are recommendations):                               capacitor     for    integrated    circuits,   including
        C1 and C2 : 0.1 PF, 20V ceramic                                     microcontrollers, to supply a local power source. The
        R1: 10 kΩ                                                           value of the tank capacitor may be determined based
        R2: 100Ω to 470Ω                                                    on the trace resistance that connects the power supply
                                                                            source to the device, and the maximum current drawn
                                                                            by the device in the application. In other words, select
                                                                            the tank capacitor so that it meets the acceptable
                                                                            voltage sag at the device. Typical values range from
                                                                            4.7 F to 47 F.


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 23
                       PIC18(L)F26/27/45/46/47/55/56/57K42
2.3      Master Clear (MCLR) Pin                              2.4     ICSP™ Pins
The MCLR pin provides two specific device                     The ICSPCLK and ICSPDAT pins are used for In-
functions: Device Reset, and Device Programming               Circuit Serial Programming™ (ICSP™) and debugging
and Debugging. If programming and debugging are               purposes. It is recommended to keep the trace length
not required in the end application, a direct                 between the ICSP connector and the ICSP pins on the
connection to VDD may be all that is required. The            device as short as possible. If the ICSP connector is
addition of other components, to help increase the            expected to experience an ESD event, a series resistor
application’s resistance to spurious Resets from              is recommended, with the value in the range of a few
voltage sags, may be beneficial. A typical                    tens of ohms, not to exceed 100Ω.
configuration is shown in Figure 2-1. Other circuit           Pull-up resistors, series diodes and capacitors on the
designs may be implemented, depending on the                  ICSPCLK and ICSPDAT pins are not recommended as
application requirements.                                     they will interfere with the programmer/debugger
During programming and debugging, the resistance              communications to the device. If such discrete
and capacitance that can be added to the pin must             components are an application requirement, they may
be considered. Device programmers and debuggers               be removed from the circuit during programming and
drive the MCLR pin. Consequently, specific voltage            debugging. Alternatively, refer to the AC/DC
levels (VIH and VIL) and fast signal transitions must         characteristics and timing requirements information in
not be adversely affected. Therefore, specific values         the respective device Flash programming specification
of R1 and C1 will need to be adjusted based on the            for information on capacitive loading limits, and pin
application and PCB requirements. For example, it is          input voltage high (VIH) and input low (VIL)
recommended that the capacitor, C1, be isolated               requirements.
from the MCLR pin during programming and                      For device emulation, ensure that the “Communication
debugging operations by using a jumper (Figure 2-2).          Channel Select” (i.e., ICSPCLK/ICSPDAT pins),
The jumper is replaced for normal run-time                    programmed into the device, matches the physical
operations.                                                   connections for the ICSP to the Microchip debugger/
Any components associated with the MCLR pin may               emulator tool.
be placed within 0.25 inch (6 mm) of the pin.                 For more information on available Microchip
                                                              development tools connection requirements, refer to
FIGURE 2-2:             EXAMPLE OF MCLR PIN                   Section 43.0 “Development Support”.
                        CONNECTIONS
             VDD


                R1
                         R2
                                 MCLR
                                PIC18(L)Fxxxxx
                JP
                 C1


  Note 1:    R1  10 k is recommended. A suggested
             starting value is 10 k. Ensure that the
             MCLR pin VIH and VIL specifications are met.
        2:   R2  470 will limit any current flowing into
             MCLR from the external capacitor, C1, in the
             event of MCLR pin breakdown, due to
             Electrostatic Discharge (ESD) or Electrical
             Overstress (EOS). Ensure that the MCLR pin
             VIH and VIL specifications are met.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 24
                       PIC18(L)F26/27/45/46/47/55/56/57K42
2.5      External Oscillator Pins                             2.6         Unused I/Os
Many microcontrollers have options for at least two           Unused I/O pins may be configured as outputs and
oscillators: a high-frequency primary oscillator and a        driven to a logic low state. Alternatively, connect a 1 kΩ
low-frequency secondary oscillator (refer to Section          to 10 kΩ resistor to VSS on unused pins and drive the
7.0 “Oscillator Module (with Fail-Safe Clock                  output to logic low.
Monitor)” for details).
The oscillator circuit may be placed on the same side         FIGURE 2-3:                       SUGGESTED
of the board as the device. Place the oscillator circuit                                        PLACEMENT OF THE
close to the respective oscillator pins with no more                                            OSCILLATOR CIRCUIT
than 0.5 inch (12 mm) between the circuit
                                                                             Single-Sided and In-Line Layouts:
components and the pins. The load capacitors may be
placed next to the oscillator itself, on the same side of                          Copper Pour          Primary Oscillator
the board.                                                                       (tied to ground)            Crystal

Use a grounded copper pour around the oscillator                                                                   DEVICE PINS
circuit to isolate it from surrounding circuits. The
grounded copper pour may be routed directly to the
MCU ground. Do not run any signal traces or power
                                                                    Primary                                                       OSC1
traces inside the ground pour. Also, if using a two-sided           Oscillator
board, avoid any traces on the other side of the board                 C1                   `                                     OSC2
where the crystal is placed.
                                                                       C2                                                         GND
Layout suggestions are shown in Figure 2-3. In-line                                         `
packages may be handled with a single-sided layout
                                                                                                                                  SOSCO
that completely encompasses the oscillator pins. With
fine-pitch packages, it is not always possible to com-                                                                            SOSCI
                                                              Secondary Oscillator
pletely surround the pins and components. A suitable               (SOSC)
solution is to tie the broken guard sections to a mirrored             Crystal                      `
ground layer. In all cases, the guard trace(s) must be
returned to ground.
                                                                                  SOSC: C1                  SOSC: C2
In planning the application’s routing and I/O
assignments, ensure that adjacent port pins, and other
signals in close proximity to the oscillator, are benign
(i.e., free of high frequencies, short rise and fall times,                      Fine-Pitch (Dual-Sided) Layouts:
and other similar noise).                                                                  Top Layer Copper Pour
                                                                                              (tied to ground)
For additional information and design guidance on
oscillator circuits, refer to these Microchip application
notes,     available     at    the  corporate website           Bottom Layer
                                                                 Copper Pour
(www.microchip.com):                                           (tied to ground)
• AN826, “Crystal Oscillator Basics and Crystal
  Selection for rfPIC™ and PICmicro® Devices”                        OSCO

• AN849, “Basic PICmicro® Oscillator Design”
                                                                                                                             C2
• AN943, “Practical PICmicro® Oscillator Analysis
                                                                                                                              Oscillator
  and Design”                                                       GND                                                        Crystal
• AN949, “Making Your Oscillator Work”
                                                                                                                             C1


                                                                     OSCI


                                                                            DEVICE PINS


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 25
