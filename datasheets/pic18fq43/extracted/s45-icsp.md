                                                                                              PIC18F27/47/57Q43
                                                                                           ICSP™ - In-Circuit Serial
                                                                                                   Programming™

45.    ICSP™ - In-Circuit Serial Programming™
       ICSP programming allows customers to manufacture circuit boards with unprogrammed devices.
       Programming can be done after the assembly process, allowing the device to be programmed with
       the most recent firmware or a custom firmware. Five pins are needed for ICSP programming:
       •   ICSPCLK
       •   ICSPDAT
       •   MCLR/VPP
       •   VDD
       •   VSS
       In Program/Verify mode, the program memory, User IDs and the Configuration bits are programmed
       through serial communications. The ICSPDAT pin is a bidirectional I/O used for transferring the serial
       data and the ICSPCLK pin is the clock input. For more information on ICSP, refer to the appropriate
       Family Programming Specification.

45.1   High-Voltage Programming Entry Mode
       The device is placed into High-Voltage Programming Entry mode by holding the ICSPCLK and
       ICSPDAT pins low, then raising the voltage on MCLR/VPP to VIH.

45.2   Low-Voltage Programming Entry Mode
                                                                      ®
       The Low-Voltage Programming Entry mode allows the PIC Flash MCUs to be programmed using
       VDD only, without high voltage. When the LVP Configuration bit is set to ‘1’, the low-voltage
       ICSP programming entry is enabled. To disable the Low-Voltage ICSP mode, the LVP bit must be
       programmed to ‘0’.
       Entry into the Low-Voltage Programming Entry mode requires the following steps:
       1. MCLR is brought to VIL.
       2. A 32-bit key sequence is presented on ICSPDAT, while clocking ICSPCLK.
       Once the key sequence is complete, MCLR must be held at VIL for as long as Program/Verify mode is
       to be maintained.
       If low-voltage programming is enabled (LVP = 1), the MCLR Reset function is automatically enabled
       and cannot be disabled. See the MCLR section for more information.
       The LVP bit can only be reprogrammed to ‘0’ by using the High-Voltage Programming mode.

45.3   Common Programming Interfaces
       Connection to a target device is typically done through an ICSP header. A commonly found
       connector on development tools is the RJ-11 in the 6P6C (6-pin, 6-connector) configuration. See
       Figure 45-1.


--- p874 ---
                                                                                        PIC18F27/47/57Q43
                                                                                     ICSP™ - In-Circuit Serial
                                                                                             Programming™
Figure 45-1. ICD RJ-11 Style Connector Interface


                                                     ICSPDAT
                                      VDD        2 4 6    NC
                                                         ICSPCLK
                                               1 3 5         Target
                                    VPP/MCLR       VSS       PC Board
                                                             Bottom Side


Pin Description
1 = VPP/MCLR
2 = VDD Target
3 = VSS (ground)
4 = ICSPDAT
5 = ICSPCLK
6 = No Connect
Another connector often found in use with the PICkit™ programmers is a standard 6-pin header with
0.1 inch spacing. Refer to Figure 45-2.
For additional interface recommendations, refer to the specific device programming manual prior to
PCB design.
It is recommended that isolation devices be used to separate the programming pins from other
circuitry. The type of isolation is highly dependent on the specific application and may include
devices such as resistors, diodes, or even jumpers. See Figure 45-3 for more information.

Figure 45-2. PICkit™ Programmer Style Connector Interface

                                                                   Pin 1 Indicator


                                                                        1
                                                                        2
                                                                        3
                                                                        4
                                                                        5
                                                                        6


--- p875 ---
                                                                                                 PIC18F27/47/57Q43
                                                                                              ICSP™ - In-Circuit Serial
                                                                                                      Programming™
Pin Description(1):
1 = VPP/MCLR
2 = VDD Target
3 = VSS (ground)
4 = ICSPDAT
5 = ICSPCLK
6 = No Connect
Note:
1. The 6-pin header (0.100" spacing) accepts 0.025" square pins.

Figure 45-3. Typical Connection for ICSP™ Programming
            External
            Programming                          VDD                       Device to be
            Signals                                                        Programmed

                    VDD                                                   VDD


                    VPP                                                   MCLR/VPP
                    VSS                                                   VSS


                   Data                                                   ICSPDAT
                   Clock                                                  ICSPCLK


                                  *          *            *


                                   To Normal Connections


                                                                     * Isolation devices (as required).


--- p876 ---
