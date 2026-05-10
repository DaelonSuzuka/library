                                                                                                                                 PIC18F27/47/57Q43
                                                                                                                                           I/O Ports


19.    I/O Ports
19.1   Overview
       Table 19-1. Port Availability per Device
                     Device                    PORTA              PORTB             PORTC                        PORTD   PORTE           PORTF
       28-pin devices                             ●                    ●              ●                                   ●(1)
       40/44-pin devices                          ●                    ●              ●                              ●    ●(2)
       48-pin devices                             ●                    ●              ●                              ●    ●(2)             ●
       Notes:
       1.    Pin RE3 only
       2.    Pins RE0, RE1, RE2 and RE3 only


       Each port has eight registers to control the operation. These registers are:
       •    PORTx registers (reads the levels on the pins of the device)
       •    LATx registers (output latch)
       •    TRISx registers (data direction)
       •    ANSELx registers (analog select)
       •    WPUx registers (weak pull-up)
       •    INLVLx (input level control)
       •    SLRCONx registers (slew rate control)
       •    ODCONx registers (open-drain control)
       In this section, the generic names such as PORTx, LATx, TRISx, etc. can be associated with PORTA,
       PORTB, PORTC, etc., depending on availability per device.
       A simplified model of a generic I/O port, without the interfaces to other peripherals, is shown in the
       following figure:

       Figure 19-1. Generic I/O Port Operation

                                                                                              Re v. 10 -00 00 52 A

                                                                       Read LATx                      2/11 /20 19


                                                                                    TRISx

                                                                   D           Q

                                               Write LATx
                                               Write PORTx                                    VDD
                                                                   CK


                                                                  Data Register

                                                   Data bus
                                                                                                       I/O pin
                                                      Read PORTx

                                                      To digital peripherals

                                                                  ANSELx

                                                      To analog peripherals

                                                                                            VSS


--- p319 ---
                                                                                               PIC18F27/47/57Q43
                                                                                                         I/O Ports

19.2   PORTx - Data Register
       PORTx is a bidirectional port and its corresponding data direction register is TRISx.
       Reading the PORTx register reads the status of the pins, whereas writing to it will write to the PORT
       latch. All write operations are Read-Modify-Write operations. Therefore, a write to a port implies that
       the PORT pins are read, and this value is modified and then written to the PORT data latch (LATx).
       The PORT data latch LATx holds the output port data and contains the latest value of a LATx or
       PORTx write. The example below shows how to initialize PORTA.

               Example 19-1. Initializing PORTA in Assembly

                ; This code example illustrates initializing the PORTA register.
                ; The other ports are initialized in the same manner.

                     BANKSEL      PORTA          ;
                     CLRF         PORTA          ;Clear PORTA
                     BANKSEL      LATA           ;
                     CLRF         LATA           ;Clear Data Latch
                     BANKSEL      ANSELA         ;
                     CLRF         ANSELA         ;Enable digital drivers
                     BANKSEL      TRISA          ;
                     MOVLW        B'00111000'    ;Set RA[5:3] as inputs
                     MOVWF        TRISA          ;and set others as outputs


               Example 19-2. Initializing PORTA in C

                // This code example illustrates initializing the PORTA register.
                // The other ports are initialized in the same manner.

                     PORTA = 0x00;            // Clear PORTA
                     LATA   = 0x00;           // Clear Data Latch
                     ANSELA = 0x00;           // Enable digital drivers
                     TRISA = 0x38;            // Set RA[5:3] as inputs and set others as outputs


                    Important: Most PORT pins share functions with device peripherals, both analog
                    and digital. In general, when a peripheral is enabled on a PORT pin, that pin
                    cannot be used as a general purpose output; however, the pin can still be read.


19.3   LATx - Output Latch
       The Data Latch (LATx registers) is useful for Read-Modify-Write operations on the value that the I/O
       pins are driving.
       A write operation to the LATx register has the same effect as a write to the corresponding PORTx
       register. A read of the LATx register reads the values held in the I/O PORT latches, while a read of the
       PORTx register reads the actual I/O pin value.


--- p320 ---
                                                                                               PIC18F27/47/57Q43
                                                                                                         I/O Ports

                   Important: As a general rule, output operations to a port must use the LAT
                   register to avoid Read-Modify-Write issues. For example, a bit set or clear
                   operation reads the port, modifies the bit, and writes the result back to the
                   port. When two bit operations are executed in succession, output loading on
                   the changed bit may delay the change at the output in which case the bit will
                   be misread in the second bit operation and written to an unexpected level. The
                   LAT registers are isolated from the port loading and therefore changes are not
                   delayed.


19.4   TRISx - Direction Control
       The TRISx register controls the PORTx pin output drivers, even when the pins are being used as
       analog inputs. The user must ensure the bits in the TRISx register are set when using the pins as
       analog inputs. I/O pins configured as analog inputs always read ‘0’.
       Setting a TRISx bit (TRISx = 1) will make the corresponding PORTx pin an input (i.e., disable the
       output driver). Clearing a TRISx bit (TRISx = 0) will make the corresponding PORTx pin an output (i.e.,
       it enables output driver and puts the contents of the output latch on the selected pin).

19.5   ANSELx - Analog Control
       Ports that support analog inputs have an associated ANSELx register. The ANSELx register is used to
       configure the Input mode of an I/O pin to analog. Setting an ANSELx bit high will disable the digital
       input buffer associated with that bit and cause the corresponding input value to always read ‘0’,
       whether the value is read in PORTx register or selected by PPS as a peripheral input.
       Disabling the input buffer prevents analog signal levels on the pin between a logic high and low from
       causing excessive current in the logic input circuitry.
       The state of the ANSELx bits has no effect on digital or analog output functions. A pin with TRIS clear
       and ANSEL set will still operate as a digital output, but the Input mode will be analog. This can cause
       unexpected behavior when executing Read-Modify-Write instructions on the PORTx register.


                   Important: The ANSELx bits default to the Analog mode after Reset. To use any
                   pins as digital general purpose or peripheral inputs, the corresponding ANSEL bits
                   must be changed to ‘0’ by the user.


19.6   WPUx - Weak Pull-Up Control
       The WPUx register controls the individual weak pull-ups for each PORT pin. When a WPUx bit is set
       (WPUx = 1), the weak pull-up will be enabled for the corresponding pin. When a WPUx bit is cleared
       (WPUx = 0), the weak pull-up will be disabled for the corresponding pin.

19.7   INLVLx - Input Threshold Control
       The INLVLx register controls the input voltage threshold for each of the available PORTx input pins.
       A selection between the Schmitt Trigger CMOS and the TTL compatible thresholds is available. The
       input threshold is important in determining the value of a read of the PORTx register and also the
       level at which an interrupt-on-change occurs, if that feature is enabled. Refer to the I/O Ports table in
       the “Electrical Specifications” chapter for more details on threshold levels.


--- p321 ---
                                                                                               PIC18F27/47/57Q43
                                                                                                         I/O Ports

                   Important: Changing the input threshold selection must be performed while all
                   peripheral modules are disabled. Changing the threshold level during the time a
                   module is active may inadvertently generate a transition associated with an input
                   pin, regardless of the actual voltage level on that pin.


19.8   SLRCONx - Slew Rate Control
       The SLRCONx register controls the slew rate option for each PORT pin. Slew rate for each PORT pin
       can be controlled independently. When a SLRCONx bit is set (SLRCONx = 1), the corresponding PORT
       pin drive is slew rate limited. When a SLRCONx bit is cleared (SLRCONx = 0), the corresponding PORT
       pin drive slews at the maximum rate possible.

19.9   ODCONx - Open-Drain Control
       The ODCONx register controls the open-drain feature of the port. Open-drain operation is
       independently selected for each pin. When a ODCONx bit is set (ODCONx = 1), the corresponding
       port output becomes an open-drain driver capable of sinking current only. When a ODCONx bit is
       cleared (ODCONx = 0), the corresponding port output pin is the standard push-pull drive capable of
       sourcing and sinking current.


                   Important: It is necessary to set open-drain control when using the pin for I2C.


19.10 Edge Selectable Interrupt-on-Change
       An interrupt can be generated by detecting a signal at the PORT pin that has either a rising edge or
       a falling edge. Individual pins can be independently configured to generate an interrupt. Refer to the
       “IOC - Interrupt-on-Change” chapter for more details.

19.11 I2C Pad Control
       For this family of devices, the I2C specific pads are available on RB1, RB2, RC3 and RC4 pins. The
       I2C characteristics of each of these pins is controlled by the RxyI2C registers. These characteristics
       include enabling I2C specific slew rate (over standard GPIO slew rate), selecting internal pull-ups for
       I2C pins, and selecting appropriate input threshold as per SMBus specifications.


                   Important: Any peripheral using the I2C pins reads the I2C input levels when
                   enabled via RxyI2C.


19.12 I/O Priorities
       Each pin defaults to the data latch after Reset. Other functions are selected with the Peripheral Pin
       Select logic. Refer to the “PPS - Peripheral Pin Select Module” chapter for more details.
       Analog input functions, such as ADC and comparator inputs, are not shown in the Peripheral Pin
       Select lists. These inputs are active when the I/O pin is set for Analog mode using the ANSELx
       register. Digital output functions may continue to control the pin when it is in Analog mode.
       Analog outputs, when enabled, take priority over digital outputs and force the digital output driver
       into a High-Impedance state.
       The pin function priorities are as follows:
       1. Port functions determined by the Configuration bits.
       2. Analog outputs (input buffers must be disabled).


--- p322 ---
                                                                                              PIC18F27/47/57Q43
                                                                                                        I/O Ports

       3. Analog inputs.
       4. Port inputs and outputs from PPS.

19.13 MCLR/VPP/RE3 Pin
       The MCLR/VPP pin is an input-only pin. Its operation is controlled by the MCLRE Configuration bit.
       When selected as a PORT pin (MCLRE = 0), it functions as a digital input-only pin; as such, it does not
       have TRISx and LATx bits associated with its operation. Otherwise, it functions as the device’s Master
       Clear input. In either configuration, the MCLR/VPP pin also functions as the programming voltage
       input pin during high-voltage programming.
       The MCLR/VPP pin is a read-only bit and will read ‘1’ when MCLRE = 1 (i.e., Master Clear enabled).


                   Important: On a Power-on Reset (POR), the MCLR/VPP pin is enabled as a digital
                   input-only if Master Clear functionality is disabled.


       The MCLR/VPP pin has an individually controlled internal weak pull-up. When set, the corresponding
       WPU bit enables the pull-up. When the MCLR/VPP pin is configured as MCLR (MCLRE = 1 and LVP = 0)
       or configured for Low-Voltage Programming (MCLRE = x and LVP = 1), the pull-up is always enabled,
       and the WPU bit has no effect.

19.14 Register Definitions: Port Control


--- p323 ---
                                                                                                 PIC18F27/47/57Q43
                                                                                                           I/O Ports

19.14.1 PORTx

            Name:      PORTx

            PORTx Register

      Bit        7            6            5            4                 3           2     1               0
                Rx7          Rx6          Rx5          Rx4               Rx3         Rx2   Rx1             Rx0
  Access        R/W          R/W          R/W          R/W               R/W         R/W   R/W             R/W
   Reset         x            x            x            x                 x           x     x               x

Bits 0, 1, 2, 3, 4, 5, 6, 7 – Rxn Port I/O Value
          Reset States: POR/BOR = xxxxxxxx
                           All Other Resets = uuuuuuuu
            Value     Description
            1         PORT pin is ≥ VIH
            0         PORT pin is ≤ VIL


                       Important:
                       • Writes to PORTx are actually written to the corresponding LATx register. Reads
                         from PORTx register return actual I/O pin values.
                       •   The PORT bit associated with the MCLR pin is read-only and will read ‘1’ when
                           the MCLR function is enabled (LVP = 1 or (LVP = 0 and MCLRE = 1))
                       •   Refer to the “Pin Allocation Table” for details about MCLR pin and pin
                           availability per port
                       •   Unimplemented bits will read back as ‘0’
                       •   Bits RB6 and RB7 read ‘1’ while in Debug mode


--- p324 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                                                I/O Ports

19.14.2 LATx

            Name:      LATx

            Output Latch Register

      Bit        7            6            5             4              3               2       1              0
               LATx7        LATx6        LATx5         LATx4          LATx3           LATx2   LATx1          LATx0
  Access        R/W          R/W          R/W           R/W            R/W             R/W     R/W            R/W
   Reset         x            x            x             x              x               x       x              x

Bits 0, 1, 2, 3, 4, 5, 6, 7 – LATxn Output Latch Value
          Reset States: POR/BOR = xxxxxxxx
                           All Other Resets = uuuuuuuu


                       Important:
                       • Writes to LATx are equivalent to writes to the corresponding PORTx register.
                         Reads from LATx register return register values, not I/O pin values.
                       •   Refer to the “Pin Allocation Table” for details about pin availability per port
                       •   Unimplemented bits will read back as ‘0’


--- p325 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                                             I/O Ports

19.14.3 TRISx

            Name:        TRISx

            Tri-State Control Register

      Bit        7              6               5              4               3               2            1               0
               TRISx7         TRISx6          TRISx5         TRISx4          TRISx3          TRISx2       TRISx1          TRISx0
  Access        R/W            R/W             R/W            R/W             R/W             R/W          R/W             R/W
   Reset         1              1               1              1               1               1            1               1

Bits 0, 1, 2, 3, 4, 5, 6, 7 – TRISxn Port I/O Tri-state Control
            Value       Description
            1           PORTx output driver is disabled. PORTx pin configured as an input (tri-stated).
            0           PORTx output driver is enabled. PORTx pin configured as an output.


                         Important:
                         • The TRIS bit associated with the MCLR pin is read-only and the value is ‘1’
                         •   Refer to the “Pin Allocation Table” for details about MCLR pin and pin
                             availability per port
                         •   Unimplemented bits will read back as ‘0’


--- p326 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                                        I/O Ports

19.14.4 ANSELx

            Name:        ANSELx

            Analog Select Register

      Bit        7              6               5               4               3               2          1           0
              ANSELx7        ANSELx6         ANSELx5         ANSELx4         ANSELx3         ANSELx2    ANSELx1     ANSELx0
  Access        R/W            R/W             R/W             R/W             R/W             R/W        R/W         R/W
   Reset         1              1               1               1               1               1          1           1

Bits 0, 1, 2, 3, 4, 5, 6, 7 – ANSELxn Analog Select on RX Pin
            Value       Description
            1           Analog input. Pin is assigned as analog input. Digital input buffer disabled.
            0           Digital I/O. Pin is assigned to port or digital special function.


                         Important:
                         • When setting a pin as an analog input, the corresponding TRIS bit must be set
                           to Input mode to allow external control of the voltage on the pin
                         •   Refer to the “Pin Allocation Table” for details about pin availability per port
                         •   Unimplemented bits will read back as ‘0’


--- p327 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                                                   I/O Ports

19.14.5 WPUx

            Name:       WPUx

            Weak Pull-Up Register

      Bit        7            6             5                4              3              2       1              0
               WPUx7        WPUx6         WPUx5            WPUx4          WPUx3          WPUx2   WPUx1          WPUx0
  Access        R/W          R/W           R/W              R/W            R/W            R/W     R/W            R/W
   Reset         0            0             0                0              0              0       0              0

Bits 0, 1, 2, 3, 4, 5, 6, 7 – WPUxn Weak Pull-up PORTx Control
            Value      Description
            1          Weak pull-up enabled
            0          Weak pull-up disabled


                        Important:
                        • The weak pull-up device is automatically disabled if the pin is configured as an
                          output, but this register remains unchanged
                        •   If MCLRE = 1, the weak pull-up on MCLR pin is always enabled and the
                            corresponding WPU bit is not affected
                        •   Refer to the “Pin Allocation Table” for details about pin availability per port
                        •   Unimplemented bits will read back as ‘0’


--- p328 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                                                  I/O Ports

19.14.6 INLVLx

            Name:        INLVLx

            Input Level Control Register

      Bit        7              6              5              4              3             2         1           0
              INLVLx7        INLVLx6        INLVLx5        INLVLx4        INLVLx3       INLVLx2   INLVLx1     INLVLx0
  Access        R/W            R/W            R/W            R/W            R/W           R/W       R/W         R/W
   Reset         1              1              1              1              1             1         1           1

Bits 0, 1, 2, 3, 4, 5, 6, 7 – INLVLxn Input Level Select on RX Pin
            Value       Description
            1           ST input used for port reads and interrupt-on-change
            0           TTL input used for port reads and interrupt-on-change


                         Important:
                         • Refer to the “Pin Allocation Table” for details about pin availability per port
                         •   Unimplemented bits will read back as ‘0’
                         •   Any peripheral using the I2C pins read the I2C ST inputs when enabled via
                             RxyI2C


--- p329 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                                                I/O Ports

19.14.7 SLRCONx

            Name:       SLRCONx

            Slew Rate Control Register

      Bit        7            6             5             4              3              2       1              0
               SLRx7        SLRx6         SLRx5         SLRx4          SLRx3          SLRx2   SLRx1          SLRx0
  Access        R/W          R/W           R/W           R/W            R/W            R/W     R/W            R/W
   Reset         1            1             1             1              1              1       1              1

Bits 0, 1, 2, 3, 4, 5, 6, 7 – SLRxn Slew Rate Control on RX Pin
            Value      Description
            1          PORT pin slew rate is limited
            0          PORT pin slews at maximum rate


                        Important:
                        • Refer to the “Pin Allocation Table” for details about pin availability per port
                        •   Unimplemented bits will read back as ‘0’


--- p330 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                                    I/O Ports

19.14.8 ODCONx

            Name:       ODCONx

            Open-Drain Control Register

      Bit        7            6               5              4               3              2       1              0
               ODCx7        ODCx6           ODCx5          ODCx4           ODCx3          ODCx2   ODCx1          ODCx0
  Access        R/W          R/W             R/W            R/W             R/W            R/W     R/W            R/W
   Reset         0            0               0              0               0              0       0              0

Bits 0, 1, 2, 3, 4, 5, 6, 7 – ODCxn Open-Drain Configuration on Rx Pin
            Value      Description
            1          PORT pin operates as open-drain drive (sink current only)
            0          PORT pin operates as standard push-pull drive (source and sink current)


                        Important:
                        • Refer to the “Pin Allocation Table” for details about pin availability per port
                        •   Unimplemented bits will read back as ‘0’


--- p331 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                                            I/O Ports

19.14.9 RxyI2C

            Name:        RxyI2C

            I2C Pad Rxy Control Register

      Bit           7        6                  5               4                  3              2          1               0
                   SLEW[1:0]                         PU[1:0]                                                      TH[1:0]
  Access        R/W         R/W                R/W             R/W                                          R/W             R/W
   Reset         0           0                  0               0                                            0               0

Bits 7:6 – SLEW[1:0] I2C Specific Slew Rate Limiting Control
            Value       Description
            11          I2C Fast mode Plus (1 MHz) slew rate enabled. The SLRxy bit is ignored.
            10          Reserved
            01          I2C Fast mode (400 kHz) slew rate enabled. The SLRxy bit is ignored.
            00          Standard GPIO Slew Rate; enabled/disabled via the SLRxy bit

Bits 5:4 – PU[1:0] I2C Pull-Up Selection
                                                                         Description
             Value
                                           FME = 0x                                                   FME = 10
              11                            Reserved                            20x current of standard weak pull-up
              10             10x current of standard weak pull-up               10x current of standard weak pull-up
              01              2x current of standard weak pull-up                5x current of standard weak pull-up
              00                               Standard GPIO weak pull-up, enabled via the WPUxy bit

Bits 1:0 – TH[1:0] I2C Input Threshold Selection
            Value       Description
            11          SMBus 3.0 (1.35V) input threshold
            10          SMBus 2.0 (2.1V) input threshold
            01          I2C-specific input thresholds
            00          Standard GPIO Input pull-up, enabled via the INLVLxy registers


                         Important:
                         • Refer to the “Pin Allocation Table” for details about pin availability per port
                         •   Unimplemented bits will read back as ‘0’


--- p332 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                                    I/O Ports

19.15 Register Summary - I/O Ports
Address    Name      Bit Pos.      7               6        5                 4        3         2         1                 0
 0x0286   RC4I2C       7:0             SLEW[1:0]                  PU[1:0]                                        TH[1:0]
 0x0287   RC3I2C       7:0             SLEW[1:0]                  PU[1:0]                                        TH[1:0]
 0x0288   RB2I2C       7:0             SLEW[1:0]                  PU[1:0]                                        TH[1:0]
0x0289    RB1I2C       7:0             SLEW[1:0]                  PU[1:0]                                        TH[1:0]
0x028A
   ...    Reserved
0x03FF
0x0400     ANSELA      7:0      ANSELA7      ANSELA6     ANSELA5       ANSELA4      ANSELA3   ANSELA2   ANSELA1        ANSELA0
0x0401      WPUA       7:0       WPUA7        WPUA6       WPUA5         WPUA4        WPUA3     WPUA2     WPUA1          WPUA0
0x0402    ODCONA       7:0       ODCA7        ODCA6       ODCA5         ODCA4        ODCA3     ODCA2     ODCA1          ODCA0
0x0403    SLRCONA      7:0       SLRA7        SLRA6       SLRA5         SLRA4        SLRA3     SLRA2     SLRA1          SLRA0
0x0404     INLVLA      7:0      INLVLA7      INLVLA6     INLVLA5       INLVLA4      INLVLA3   INLVLA2   INLVLA1        INLVLA0
0x0405
   ...    Reserved
0x0407
0x0408     ANSELB      7:0      ANSELB7      ANSELB6     ANSELB5       ANSELB4      ANSELB3   ANSELB2   ANSELB1       ANSELB0
0x0409      WPUB       7:0       WPUB7        WPUB6       WPUB5         WPUB4        WPUB3     WPUB2     WPUB1         WPUB0
0x040A    ODCONB       7:0       ODCB7        ODCB6       ODCB5         ODCB4        ODCB3     ODCB2     ODCB1         ODCB0
0x040B    SLRCONB      7:0       SLRB7        SLRB6       SLRB5         SLRB4        SLRB3     SLRB2     SLRB1         SLRB0
0x040C     INLVLB      7:0      INLVLB7      INLVLB6     INLVLB5       INLVLB4      INLVLB3   INLVLB2   INLVLB1       INLVLB0
0x040D
   ...    Reserved
0x040F
0x0410     ANSELC      7:0      ANSELC7      ANSELC6     ANSELC5        ANSELC4     ANSELC3   ANSELC2   ANSELC1        ANSELC0
0x0411      WPUC       7:0       WPUC7        WPUC6       WPUC5          WPUC4       WPUC3     WPUC2     WPUC1          WPUC0
0x0412    ODCONC       7:0       ODCC7        ODCC6       ODCC5          ODCC4       ODCC3     ODCC2     ODCC1          ODCC0
0x0413    SLRCONC      7:0       SLRC7        SLRC6       SLRC5          SLRC4       SLRC3     SLRC2     SLRC1          SLRC0
0x0414     INLVLC      7:0      INLVLC7      INLVLC6     INLVLC5        INLVLC4     INLVLC3   INLVLC2   INLVLC1        INLVLC0
0x0415
   ...    Reserved
0x0417
0x0418     ANSELD      7:0      ANSELD7      ANSELD6     ANSELD5       ANSELD4      ANSELD3   ANSELD2   ANSELD1       ANSELD0
0x0419      WPUD       7:0       WPUD7        WPUD6       WPUD5         WPUD4        WPUD3     WPUD2     WPUD1         WPUD0
0x041A    ODCOND       7:0       ODCD7        ODCD6       ODCD5         ODCD4        ODCD3     ODCD2     ODCD1         ODCD0
0x041B    SLRCOND      7:0       SLRD7        SLRD6       SLRD5         SLRD4        SLRD3     SLRD2     SLRD1         SLRD0
0x041C     INLVLD      7:0      INLVLD7      INLVLD6     INLVLD5       INLVLD4      INLVLD3   INLVLD2   INLVLD1       INLVLD0
0x041D
   ...    Reserved
0x041F
0x0420     ANSELE      7:0                                                                    ANSELE2   ANSELE1        ANSELE0
0x0421      WPUE       7:0                                                          WPUE3      WPUE2     WPUE1          WPUE0
0x0422    ODCONE       7:0                                                                     ODCE2     ODCE1          ODCE0
0x0423    SLRCONE      7:0                                                                     SLRE2     SLRE1          SLRE0
0x0424     INLVLE      7:0                                                          INLVLE3   INLVLE2   INLVLE1        INLVLE0
0x0425
   ...    Reserved
0x0427
0x0428     ANSELF      7:0      ANSELF7      ANSELF6     ANSELF5        ANSELF4     ANSELF3   ANSELF2   ANSELF1        ANSELF0
0x0429      WPUF       7:0       WPUF7        WPUF6       WPUF5          WPUF4       WPUF3     WPUF2     WPUF1          WPUF0
0x042A    ODCONF       7:0       ODCF7        ODCF6       ODCF5          ODCF4       ODCF3     ODCF2     ODCF1          ODCF0
0x042B    SLRCONF      7:0       SLRF7        SLRF6       SLRF5          SLRF4       SLRF3     SLRF2     SLRF1          SLRF0
0x042C     INLVLF      7:0      INLVLF7      INLVLF6     INLVLF5        INLVLF4     INLVLF3   INLVLF2   INLVLF1        INLVLF0
0x042D
   ...    Reserved
0x04BD
0x04BE     LATA        7:0       LATA7         LATA6      LATA5             LATA4    LATA3     LATA2     LATA1             LATA0
0x04BF     LATB        7:0       LATB7         LATB6      LATB5             LATB4    LATB3     LATB2     LATB1             LATB0
0x04C0     LATC        7:0       LATC7         LATC6      LATC5             LATC4    LATC3     LATC2     LATC1             LATC0
0x04C1     LATD        7:0       LATD7         LATD6      LATD5             LATD4    LATD3     LATD2     LATD1             LATD0
0x04C2     LATE        7:0                                                                     LATE2     LATE1             LATE0


--- p333 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                                         I/O Ports
...........continued
 Address               Name    Bit Pos.     7           6           5              4        3         2        1             0
  0x04C3               LATF      7:0      LATF7       LATF6       LATF5       LATF4       LATF3     LATF2    LATF1         LATF0
  0x04C4
    ...           Reserved
  0x04C5
 0x04C6                TRISA     7:0      TRISA7      TRISA6      TRISA5      TRISA4      TRISA3    TRISA2   TRISA1       TRISA0
 0x04C7                TRISB     7:0      TRISB7      TRISB6      TRISB5      TRISB4      TRISB3    TRISB2   TRISB1       TRISB0
 0x04C8                TRISC     7:0      TRISC7      TRISC6      TRISC5      TRISC4      TRISC3    TRISC2   TRISC1       TRISC0
 0x04C9                TRISD     7:0      TRISD7      TRISD6      TRISD5      TRISD4      TRISD3    TRISD2   TRISD1       TRISD0
 0x04CA                TRISE     7:0                                                     Reserved   TRISE2   TRISE1       TRISE0
 0x04CB                TRISF     7:0      TRISF7      TRISF6      TRISF5      TRISF4      TRISF3    TRISF2   TRISF1       TRISF0
 0x04CC
    ...           Reserved
 0x04CD
 0x04CE                PORTA     7:0       RA7         RA6         RA5            RA4      RA3       RA2      RA1           RA0
 0x04CF                PORTB     7:0       RB7         RB6         RB5            RB4      RB3       RB2      RB1           RB0
 0x04D0                PORTC     7:0       RC7         RC6         RC5            RC4      RC3       RC2      RC1           RC0
 0x04D1                PORTD     7:0       RD7         RD6         RD5            RD4      RD3       RD2      RD1           RD0
 0x04D2                PORTE     7:0                                                       RE3       RE2      RE1           RE0
 0x04D3                PORTF     7:0       RF7         RF6         RF5            RF4      RF3       RF2      RF1           RF0


--- p334 ---
