                      PIC18(L)F26/27/45/46/47/55/56/57K42
40.0     IN-CIRCUIT SERIAL                                40.3     Common Programming Interfaces
         PROGRAMMING™ (ICSP™)                             Connection to a target device is typically done through
ICSP™ programming allows customers to manufacture         an ICSP™ header. A commonly found connector on
circuit boards with unprogrammed devices. Programming     development tools is the RJ-11 in the 6P6C (6-pin, 6-
can be done after the assembly process, allowing the      connector) configuration. See Figure 40-1.
device to be programmed with the most recent firmware
or a custom firmware. Five pins are needed for ICSP™      FIGURE 40-1:                 ICD RJ-11 STYLE
programming:                                                                           CONNECTOR INTERFACE
• ICSPCLK
• ICSPDAT
• MCLR/VPP
• VDD
                                                                                  ICSPDAT
• VSS
                                                                              2 4 6    NC
                                                                  VDD
In Program/Verify mode the program memory, User IDs                                   ICSPCLK
and the Configuration Words are programmed through                          1 3 5
                                                                                          Target
serial communications. The ICSPDAT pin is a                      VPP/MCLR                  PC Board
                                                                                  VSS
bidirectional I/O used for transferring the serial data                                    Bottom Side
and the ICSPCLK pin is the clock input. For more
information on ICSP™ refer to the “PIC18F26/27/45/
46/47/55/56/57K42         Memory          Programming               Pin Description*
Specification” (DS40001886).
                                                                    1 = VPP/MCLR
                                                                    2 = VDD Target
40.1     High-Voltage Programming Entry                             3 = VSS (ground)
         Mode                                                       4 = ICSPDAT

The device is placed into High-Voltage Programming                  5 = ICSPCLK
Entry mode by holding the ICSPCLK and ICSPDAT                       6 = No Connect
pins low then raising the voltage on MCLR/VPP to VIHH.
                                                          Another connector often found in use with the PICkit™
40.2     Low-Voltage Programming Entry                    programmers is a standard 6-pin header with 0.1 inch
         Mode                                             spacing. Refer to Figure 40-2.
The Low-Voltage Programming Entry mode allows the         For additional interface recommendations, refer to your
PIC® Flash MCUs to be programmed using VDD only,          specific device programmer manual prior to PCB
without high voltage. When the LVP bit of Configuration   design.
Words is set to ‘1’, the low-voltage ICSP™                It is recommended that isolation devices be used to
programming entry is enabled. To disable the Low-         separate the programming pins from other circuitry.
Voltage ICSP mode, the LVP bit must be programmed         The type of isolation is highly dependent on the specific
to ‘0’.                                                   application and may include devices such as resistors,
Entry into the Low-Voltage Programming Entry mode         diodes, or even jumpers. See Figure 40-3 for more
requires the following steps:                             information.
1.   MCLR is brought to VIL.
2.   A 32-bit key sequence is presented on
     ICSPDAT, while clocking ICSPCLK.
Once the key sequence is complete, MCLR must be
held at VIL for as long as Program/Verify mode is to be
maintained.
If low-voltage programming is enabled (LVP = 1), the
MCLR Reset function is automatically enabled and
cannot be disabled. See Section 6.5 “MCLR” for more
information.
The LVP bit can only be reprogrammed to ‘0’ by using
the High-Voltage Programming mode.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 661
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 40-2:           PICkit™ PROGRAMMER STYLE CONNECTOR INTERFACE

                                                       Pin 1 Indicator

                                                                         Pin Description*
                                                             1           1 = VPP/MCLR
                                                             2
                                                                         2 = VDD Target
                                                             3
                                                             4           3 = VSS (ground)
                                                             5
                                                             6           4 = ICSPDAT
                                                                         5 = ICSPCLK
                                                                         6 = No Connect


                      *   The 6-pin header (0.100" spacing) accepts 0.025" square pins.


FIGURE 40-3:           TYPICAL CONNECTION FOR ICSP™ PROGRAMMING


                    External
                    Programming                           VDD                     Device to be
                    Signals                                                       Programmed

                           VDD                                                   VDD


                           VPP                                                   MCLR/VPP
                           VSS                                                   VSS


                          Data                                                   ICSPDAT
                          Clock                                                  ICSPCLK


                                          *           *           *


                                           To Normal Connections


                                                                            * Isolation devices (as required).


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 662
