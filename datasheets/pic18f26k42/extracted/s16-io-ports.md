                       PIC18(L)F26/27/45/46/47/55/56/57K42
16.0      I/O PORTS                                                     FIGURE 16-1:                 GENERIC I/O PORT
                                                                                                     OPERATION
The PIC18(L)F26/27/45/46/47/55/56/57K42 devices
have six I/O ports, allocated as shown in Table 16-1.


TABLE 16-1:        PORT ALLOCATION TABLE                                                           Read LATx
                                                                                                               TRISx
                   FOR PIC18(L)F26/27/45/46/47/
                   55/56/57K42 DEVICES                                                       D        Q


                              PORTB

                                      PORTC

                                              PORTD
                                                                         Write LATx


                                                      PORTE
                      PORTA


                                                                PORTF
                                                                         Write PORTx
       Device                                                                                 CK                         VDD
                                                                                            Data Register
  PIC18(L)F26K42       •       •       •              •(1)
                                                          (1)
  PIC18(L)F27K42       •       •       •              •                      Data Bus
  PIC18(L)F45K42       •       •       •       •      •(2)                                                                     I/O pin
                                                                               Read PORTx
  PIC18(L)F46K42       •       •       •       •      •(2)
  PIC18(L)F47K42       •       •       •       •      •(2)               To digital peripherals
                                                          (2)
                                                                                                                         VSS
  PIC18(L)F55K42       •       •       •       •      •          •                                    ANSELx
                                                                         To analog peripherals
  PIC18(L)F56K42       •       •       •       •      •(2)       •
                                                          (2)
  PIC18(L)F57K42       •       •       •       •      •          •
Note 1:     Pin RE3 only.                                               16.1        I/O Priorities
     2:     Pins RE0, RE1, RE2 and RE3 only.
                                                                        Each pin defaults to the PORT data latch after Reset.
Each port has ten registers to control the operation.                   Other functions are selected with the peripheral pin
These registers are:                                                    select logic. See Section 17.0 “Peripheral Pin Select
• PORTx registers (reads the levels on the pins of                      (PPS) Module” for more information.
  the device)                                                           Analog input functions, such as ADC and comparator
• LATx registers (output latch)                                         inputs, are not shown in the peripheral pin select lists.
• TRISx registers (data direction)                                      These inputs are active when the I/O pin is set for
• ANSELx registers (analog select)                                      Analog mode using the ANSELx register. Digital output
• WPUx registers (weak pull-up)                                         functions may continue to control the pin when it is in
• INLVLx (input level control)                                          Analog mode.
• SLRCONx registers (slew rate control)                                 Analog outputs, when enabled, take priority over digital
• ODCONx registers (open-drain control)                                 outputs and force the digital output driver into a
Most port pins share functions with device peripherals,                 high-impedance state.
both analog and digital. In general, when a peripheral                  The pin function priorities are as follows:
is enabled on a port pin, that pin cannot be used as a
                                                                        1.     Configuration bits
general purpose output; however, the pin can still be
read.                                                                   2.     Analog outputs (disable the input buffers)
                                                                        3.     Analog inputs
The Data Latch (LATx registers) is useful for
read-modify-write operations on the value that the I/O                  4.     Port inputs and outputs from PPS
pins are driving.
A write operation to the LATx register has the same
                                                                        16.2        PORTx Registers
effect as a write to the corresponding PORTx register.                  In this section, the generic names such as PORTx,
A read of the LATx register reads of the values held in                 LATx, TRISx, etc. can be associated with PORTA,
the I/O PORT latches, while a read of the PORTx                         PORTB, and PORTC. The functionality of PORTE is
register reads the actual I/O pin value.                                different compared to other ports and is explained in a
Ports that support analog inputs have an associated                     separate section.
ANSELx register. When an ANSELx bit is set, the
digital input buffer associated with that bit is disabled.
Disabling the input buffer prevents analog signal levels
on the pin between a logic high and low from causing
excessive current in the logic input circuitry. A
simplified model of a generic I/O port, without the
interfaces to other peripherals, is shown in Figure 16-1.


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 260
                       PIC18(L)F26/27/45/46/47/55/56/57K42
16.2.1      DATA REGISTER                                     16.2.3      ANALOG CONTROL
PORTx is an 8-bit wide, bidirectional port. The               The ANSELx register (Register 16-4) is used to
corresponding data direction register is TRISx                configure the Input mode of an I/O pin to analog.
(Register 16-2). Setting a TRISx bit (‘1’) will make the      Setting the appropriate ANSELx bit high will cause all
corresponding PORTA pin an input (i.e., disable the           digital reads on the pin to be read as ‘0’ and allow
output driver). Clearing a TRISx bit (‘0’) will make the      analog functions on the pin to operate correctly.
corresponding PORTx pin an output (i.e., it enables           The state of the ANSELx bits has no effect on digital
output driver and puts the contents of the output latch       output functions. A pin with TRIS clear and ANSEL set
on the selected pin). Example 16-1 shows how to               will still operate as a digital output, but the Input mode
initialize PORTx.                                             will be analog. This can cause unexpected behavior
Reading the PORTx register (Register 16-1) reads the          when executing read-modify-write instructions on the
status of the pins, whereas writing to it will write to the   affected port.
PORT latch. All write operations are read-modify-write
                                                                Note:     The ANSELx bits default to the Analog
operations. Therefore, a write to a port implies that the
                                                                          mode after Reset. To use any pins as
port pins are read, this value is modified and then
                                                                          digital general purpose or peripheral
written to the PORT data latch (LATx).
                                                                          inputs, the corresponding ANSEL bits
The PORT data latch LATx (Register 16-3) holds the                        must be initialized to ‘0’ by user software.
output port data and contains the latest value of a LATx
or PORTx write.                                               16.2.4      OPEN-DRAIN CONTROL
EXAMPLE 16-1:           INITIALIZING PORTA                    The ODCONx register (Register 16-6) controls the
 ; This code example illustrates
                                                              open-drain feature of the port. Open-drain operation is
 ; initializing the PORTA register. The                       independently selected for each pin. When an
 ; other ports are initialized in the same                    ODCONx bit is set, the corresponding port output
 ; manner.                                                    becomes an open-drain driver capable of sinking
                                                              current only. When an ODCONx bit is cleared, the
 BANKSEL    PORTA           ;                                 corresponding port output pin is the standard push-pull
 CLRF       PORTA           ;Init PORTA                       drive capable of sourcing and sinking current.
 BANKSEL    LATA            ;Data Latch
 CLRF       LATA            ;
 BANKSEL    ANSELA          ;                                   Note:     It is necessary to set open-drain control
 CLRF       ANSELA          ;digital I/O                                  when using the pin for I2C.
 BANKSEL    TRISA           ;
 MOVLW      B'11111000'     ;Set RA[7:3] as inputs
 MOVWF      TRISA           ;and set RA[2:0] as
                                                              16.2.5      SLEW RATE CONTROL
                            ;outputs                          The SLRCONx register (Register 16-7) controls the
                                                              slew rate option for each port pin. Slew rate for each
                                                              port pin can be controlled independently. When an
16.2.2      DIRECTION CONTROL
                                                              SLRCONx bit is set, the corresponding port pin drive is
The TRISx register (Register 16-2) controls the PORTx         slew rate limited. When an SLRCONx bit is cleared,
pin output drivers, even when they are being used as          The corresponding port pin drive slews at the maximum
analog inputs. The user may ensure the bits in the            rate possible.
TRISx register are maintained set when using them as
analog inputs. I/O pins configured as analog inputs
always read ‘0’.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 261
                        PIC18(L)F26/27/45/46/47/55/56/57K42
16.2.6        INPUT THRESHOLD CONTROL                        16.3      PORTE Registers
The INLVLx register (Register 16-8) controls the input       Depending on the device, PORTE is implemented in
voltage threshold for each of the available PORTx input      two different ways.
pins. A selection between the Schmitt Trigger CMOS or
the TTL compatible thresholds is available. The input        16.3.1      PORTE ON 40/44/48-PIN DEVICES
threshold is important in determining the value of a read
of the PORTx register and also the level at which an         For PIC18(L)F45/46/47/55/56/57K42 devices, PORTE
interrupt-on-change occurs, if that feature is enabled.      is a 4-bit wide port. Three pins (RE0, RE1 and RE2)
See Table 44-5 for more information on threshold             are individually configurable as inputs or outputs.
levels.                                                      These pins have Schmitt Trigger input buffers. When
                                                             selected as an analog input, these pins will read as
    Note:     Changing the input threshold selection
              may be performed while all peripheral          ‘0’s. The corresponding data direction register is
              modules are disabled. Changing the             TRISE. Setting a TRISE bit (= 1) will make the
              threshold level during the time a module is    corresponding PORTE pin an input (i.e., disable the
              active may inadvertently generate a            output driver).
              transition associated with an input pin,       Clearing a TRISE bit (= 0) will make the corresponding
              regardless of the actual voltage level on      PORTE pin an output (i.e., enable the output driver
              that pin.
                                                             and put the contents of the output latch on the
16.2.7        WEAK PULL-UP CONTROL                           selected pin). TRISE controls the direction of the REx
                                                             pins, even when they are being used as analog pins.
The WPUx register (Register 16-5) controls the
                                                             The user must make sure to keep the pins configured
individual weak pull-ups for each port pin.
                                                             as inputs when using them as analog inputs. RE[2:0]
16.2.8        EDGE SELECTABLE                                bits have other registers associated with them (i.e.,
              INTERRUPT-ON-CHANGE                            ANSELE, WPUE, INLVLE, SLRCONE and ODCONE).
                                                             The functionality is similar to the other ports. The Data
An interrupt can be generated by detecting a signal at
                                                             Latch register (LATE) is also memory-mapped. Read-
the port pin that has either a rising edge or a falling
edge. Any individual pin can be configured to generate       modify-write operations on the LATE register read and
an interrupt. The interrupt-on-change module is              write the latched output value for PORTE.
present on all the pins. For further details about the IOC
module refer to Section 18.0 “Interrupt-on-Change”.            Note:     On a Power-on Reset, RE[2:0] are
                                                                         configured as analog inputs.
16.2.9        I2C PAD CONTROL
For     the     PIC18(L)F26/27/45/46/47/55/56/57K42          The fourth pin of PORTE (MCLR/VPP/RE3) is an
devices, the I2C specific pads are available on RB1,         input-only pin. Its operation is controlled by the
RB2, RC3, RC4, RD0(1) and RD1(1) pins. The I2C               MCLRE Configuration bit. When selected as a port
characteristics of each of these pins is controlled by the
                                                             pin, (MCLRE = 0), it functions as a digital input-only
RxyI2C registers (see Register 16-9). These
                                                             pin; as such, it does not have TRIS or LAT bits
characteristics include enabling I2C specific slew rate
(over standard GPIO slew rate), selecting internal pull-     associated with its operation. Otherwise, it functions
ups for I2C pins, and selecting appropriate input            as the device’s Master Clear input. In either
threshold as per I2C/SMBus specifications.                   configuration, RE3 also functions as the programming
                                                             voltage input during programming. RE3 in PORTE
                                                             register is a read-only bit and will read ‘1’ when
    Note 1: RD0 and RD1 I2C pads are not available           MCLRE = 1 (i.e., Master Clear enabled).
            in PIC18(L)F26K42 parts.
            2: Any peripheral using the I2C pins read
                                                               Note:     On a Power-on Reset, RE3 is enabled as
               the I2C ST inputs when enabled via
                                                                         a digital input only if Master Clear
               RxyI2C.
                                                                         functionality is disabled.
.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 262
                      PIC18(L)F26/27/45/46/47/55/56/57K42
EXAMPLE 16-2:          INITIALIZING PORTE
 CLRF      PORTE           ;Initialize PORTE by
                           ;clearing output
                           ;data latches
 CLRF      LATE            ;Alternate method
                           ;to clear output
                           ;data latches
 CLRF      ANSELE          ;Configure analog pins
                           ;for digital only
 MOVLW     05h             ;Value used to
                           ;initialize data
                           ;direction
 MOVWF     TRISE           ;Set RE[0] as input
                           ;RE[1] as output
                           ;RE[2] as input


16.3.2      PORTE ON 28-PIN DEVICES
For PIC18(L)F26/27K42 devices, PORTE is only
available when Master Clear functionality is disabled
(MCLRE = 0). In this case, PORTE is a single bit, input-
only port comprised of RE3 only. The pin operates as
previously described. RE3 in PORTE register is a read-
only bit and will read ‘1’ when MCLRE = 1 (i.e., Master
Clear enabled).

16.3.3      RE3 WEAK PULL-UP
The port RE3 pin has an individually controlled weak
internal pull-up. When set, the WPUE3 bit enables the
RE3 pin pull-up. When the RE3 port pin is configured
as MCLR, (CONFIG2L, MCLRE = 1 and CONFIG4H,
LVP = 0), or configured for Low-Voltage Programming,
(MCLRE = x and LVP = 1), the pull-up is always
enabled and the WPUE3 bit has no effect.

16.3.4      INTERRUPT-ON-CHANGE
The interrupt-on-change feature is available only on the
RE3 pin of PORTE for all devices. If MCLRE = 1 or
LVP = 1, RE3 port functionality is disabled and
interrupt-on-change on RE3 is not available. For further
details refer to Section 18.0 “Interrupt-on-Change”.


 2017-2021 Microchip Technology Inc.                      DS40001919G-page 263
                            PIC18(L)F26/27/45/46/47/55/56/57K42
16.4      Register Definitions: Port Control
REGISTER 16-1:              PORTx: PORTx REGISTER(1)
   R/W-x/u           R/W-x/u          R/W-x/u           R/W-x/u           R/W-x/u         R/W-x/u       R/W-x/u      R/W-x/u
        Rx7               Rx6            Rx5             Rx4               Rx3              Rx2          Rx1           Rx0
bit 7                                                                                                                        bit 0


Legend:
R = Readable bit                  W = Writable bit                     U = Unimplemented bit, read as ‘0’
‘1’ = Bit is set                  ‘0’ = Bit is cleared                 x = Bit is unknown
-n/n = Value at POR and BOR/Value at all other Resets


bit 7-0            Rx[7:0]: Rx7:Rx0 Port I/O Value bits
                   1 = Port pin is  VIH
                   0 = Port pin is  VIL

Note 1:       Writes to PORTx are actually written to the corresponding LATx register.
              Reads from PORTx register return actual I/O pin values.


TABLE 16-2:          PORT REGISTERS
   Name            Bit 7         Bit 6          Bit 5             Bit 4          Bit 3         Bit 2        Bit 1       Bit 0
PORTA              RA7           RA6            RA5               RA4            RA3           RA2           RA1        RA0
PORTB              RB7(1)       RB6(1)          RB5               RB4            RB3           RB2           RB1        RB0
PORTC               RC7          RC6            RC5               RC4             RC3             RC2        RC1        RC0
PORTD(3)            RD7          RD6            RD5               RD4             RD3             RD2        RD1        RD0
PORTE               —             —              —                 —             RE3(2)       RE2(3)        RE1(3)     RE0(3)
PORTF(4)            RF7          RF6            RF5               RF4             RF3             RF2        RF1        RF0
Note 1: Bits RB6 and RB7 read ‘1’ while in Debug mode.
     2: Bit PORTE3 is read-only, and will read ‘1’ when MCLRE = 1 (Master Clear enabled).
     3: Unimplemented in PIC18(L)F26/27K42.
     4: Unimplemented in PIC18(L)F26/27/45/46/47K42.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 264
                            PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 16-2:              TRISx: TRI-STATE CONTROL REGISTER
   R/W-1/1             R/W-1/1          R/W-1/1           R/W-1/1          R/W-1/1      R/W-1/1       R/W-1/1         R/W-1/1
    TRISx7             TRISx6           TRISx5            TRISx4           TRISx3       TRISx2         TRISx1         TRISx0
bit 7                                                                                                                        bit 0


Legend:
R = Readable bit                    W = Writable bit                    U = Unimplemented bit, read as ‘0’
‘1’ = Bit is set                    ‘0’ = Bit is cleared                x = Bit is unknown
-n/n = Value at POR and BOR/Value at all other Resets


bit 7-0             TRISx[7:0]: TRISx Port I/O Tri-state Control bits
                    1 = Port output driver is disabled
                    0 = Port output driver is enabled


TABLE 16-3:           TRIS REGISTERS
   Name             Bit 7          Bit 6          Bit 5            Bit 4        Bit 3         Bit 2          Bit 1       Bit 0
TRISA              TRISA7        TRISA6          TRISA5        TRISA4          TRISA3        TRISA2      TRISA1         TRISA0
TRISB          TRISB7(1)         TRISB6(1)       TRISB5        TRISB4          TRISB3        TRISB2      TRISB1        TRISB0
TRISC              TRISC7         TRISC6         TRISC5        TRISC4          TRISC3        TRISC2      TRISC1         TRISC0
TRISD(2)           TRISD7         TRISD6         TRISD5        TRISD4          TRISD3        TRISD2      TRISD1         TRISD0
TRISE(2)             —              —              —                —               —        TRISE2      TRISE1        TRISE0
TRISF(3)           TRISF7         TRISF6         TRISF5        TRISF4          TRISF3        TRISF2      TRISF1         TRISF0
Note 1:      Bits RB6 and RB7 read ‘1’ while in Debug mode.
     2:      Unimplemented in PIC18(L)F26/27K42.
     3:      Unimplemented in PIC18(L)F26/45/46/47K42.


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 265
                            PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 16-3:               LATx: LATx REGISTER(1)
   R/W-x/u              R/W-x/u            R/W-x/u           R/W-x/u           R/W-x/u       R/W-x/u       R/W-x/u         R/W-x/u
    LATx7                  LATx6           LATx5             LATx4              LATx3         LATx2         LATx1           LATx0
bit 7                                                                                                                             bit 0


Legend:
R = Readable bit                     W = Writable bit                        U = Unimplemented bit, read as ‘0’
‘1’ = Bit is set                     ‘0’ = Bit is cleared                    x = Bit is unknown
-n/n = Value at POR and BOR/Value at all other Resets


bit 7-0             LATx[7:0]: Rx7:Rx0 Output Latch Value bits
Note 1: Writes to LATx are equivalent with writes to the corresponding PORTx register. Reads from LATx register
        return register values, not I/O pin values.


TABLE 16-4:             LAT REGISTERS
  Name             Bit 7           Bit 6             Bit 5           Bit 4           Bit 3        Bit 2           Bit 1       Bit 0
LATA               LATA7           LATA6           LATA5          LATA4             LATA3         LATA2           LATA1      LATA0
LATB               LATB7           LATB6           LATB5          LATB4             LATB3         LATB2       LATB1          LATB0
LATC               LATC7           LATC6           LATC5          LATC4             LATC3         LATC2           LATC1      LATC0
LATD(1)            LATD7           LATD6           LATD5          LATD4             LATD3         LATD2           LATD1      LATD0
LATE(1)             —               —                 —                —                —         LATE2       LATE1          LATE0
LATF(2)            LATF7           LATF6           LATF5          LATF4             LATF3         LATF2           LATF1      LATF0
Note 1:      Unimplemented in PIC18(L)F26/27K42.
     2:      Unimplemented in PIC18(L)F26/45/46/47K42.


 2017-2021 Microchip Technology Inc.                                                                             DS40001919G-page 266
                            PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 16-4:              ANSELx: ANALOG SELECT REGISTER
   R/W-1/1            R/W-1/1       R/W-1/1             R/W-1/1           R/W-1/1       R/W-1/1       R/W-1/1        R/W-1/1
  ANSELx7            ANSELx6       ANSELx5           ANSELx4              ANSELx3       ANSELx2       ANSELx1       ANSELx0
bit 7                                                                                                                      bit 0


Legend:
R = Readable bit                  W = Writable bit                     U = Unimplemented bit, read as ‘0’
‘1’ = Bit is set                  ‘0’ = Bit is cleared                 x = Bit is unknown
-n/n = Value at POR and BOR/Value at all other Resets


bit 7-0             ANSELx[7:0]: Analog Select on Pins Rx[7:0]
                    1 = Digital Input buffers are disabled.
                    0 = ST and TTL input devices are enabled


TABLE 16-5:          ANALOG SELECT PORT REGISTERS
   Name             Bit 7        Bit 6          Bit 5             Bit 4         Bit 3        Bit 2          Bit 1       Bit 0
ANSELA             ANSELA7      ANSELA6      ANSELA5         ANSELA4          ANSELA3       ANSELA2     ANSELA1       ANSELA0
ANSELB             ANSELB7      ANSELB6      ANSELB5         ANSELB4          ANSELB3       ANSELB2     ANSELB1       ANSELB0
ANSELC             ANSELC7      ANSELC6      ANSELC5         ANSELC4          ANSELC3       ANSELC2     ANSELC1       ANSELC0
ANSELD(1)          ANSELD7      ANSELD6      ANSELD5         ANSELD4          ANSELD3       ANSELD2     ANSELD1       ANSELD0
ANSELE(1)            —            —              —                 —                —       ANSELE2     ANSELE1       ANSELE0
ANSELF(2)          ANSELF7      ANSELF6      ANSELF5         ANSELF4          ANSELF3       ANSELF2     ANSELF1       ANSELF0
Note 1:      Unimplemented in PIC18(L)F26/27K42.
     2:      Unimplemented in PIC18(L)F26/45/46/47K42.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 267
                           PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 16-5:             WPUx: WEAK PULL-UP REGISTER
   R/W-0/0            R/W-0/0        R/W-0/0            R/W-0/0         R/W-0/0        R/W-0/0        R/W-0/0       R/W-0/0
    WPUx7               WPUx6           WPUx5           WPUx4           WPUx3          WPUx2          WPUx1         WPUx0
bit 7                                                                                                                     bit 0


Legend:
R = Readable bit                  W = Writable bit                    U = Unimplemented bit, read as ‘0’
‘1’ = Bit is set                  ‘0’ = Bit is cleared                x = Bit is unknown
-n/n = Value at POR and BOR/Value at all other Resets


bit 7-0             WPUx[7:0]: Weak Pull-up PORTx Control bits
                    1 = Weak Pull-up enabled
                    0 = Weak Pull-up disabled


TABLE 16-6:          WEAK PULL-UP PORT REGISTERS
  Name             Bit 7        Bit 6           Bit 5           Bit 4          Bit 3         Bit 2         Bit 1       Bit 0
WPUA               WPUA7        WPUA6        WPUA5           WPUA4           WPUA3         WPUA2           WPUA1      WPUA0
WPUB               WPUB7        WPUB6        WPUB5           WPUB4           WPUB3         WPUB2           WPUB1      WPUB0
WPUC               WPUC7        WPUC6           WPUC5        WPUC4           WPUC3         WPUC2           WPUC1      WPUC0
WPUD(2)            WPUD7        WPUD6           WPUD5        WPUD4           WPUD3         WPUD2           WPUD1      WPUD0
WPUE                —            —               —                —         WPUE3(1)       WPUE2(2)    WPUE1(2)      WPUE0(2)
WPUF(3)            WPUF7        WPUF6           WPUF5        WPUF4            WPUF3         WPUF2          WPUF1      WPUF0
Note 1: If MCLRE = 1, the weak pull-up in RE3 is always enabled; bit WPUE3 is not affected.
     2: Unimplemented in PIC18(L)F26/27K42.
     3: Unimplemented in PIC18(L)F26/27/45/46/47K42.


 2017-2021 Microchip Technology Inc.                                                                      DS40001919G-page 268
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 16-6:              ODCONx: OPEN-DRAIN CONTROL REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0           R/W-0/0           R/W-0/0           R/W-0/0       R/W-0/0     R/W-0/0
    ODCx7            ODCx6          ODCx5            ODCx4             ODCx3             ODCx2         ODCx1        ODCx0
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                 W = Writable bit                U = Unimplemented bit, read as ‘0’
‘1’ = Bit is set                 ‘0’ = Bit is cleared            x = Bit is unknown
-n/n = Value at POR and BOR/Value at all other Resets


bit 7-0            ODCx[7:0]: Open-Drain Configuration on Pins Rx[7:0]
                   1 = Output drives only low-going signals (sink current only)
                   0 = Output drives both high-going and low-going signals (source and sink current)


TABLE 16-7:         OPEN-DRAIN CONTROL REGISTERS
    Name            Bit 7        Bit 6          Bit 5          Bit 4             Bit 3         Bit 2       Bit 1       Bit 0
ODCONA             ODCA7        ODCA6         ODCA5            ODCA4         ODCA3           ODCA2        ODCA1       ODCA0
ODCONB             ODCB7        ODCB6         ODCB5            ODCB4         ODCB3           ODCB2        ODCB1       ODCB0
ODCONC             ODCC7        ODCC6         ODCC5            ODCC4         ODCC3           ODCC2        ODCC1       ODCC0
ODCOND(1)          ODCD7        ODCD6          ODCD5           ODCD4         ODCD3            ODCD2       ODCD1       ODCD0
ODCONE(1)            —            —              —              —                 —          ODCE2        ODCE1       ODCE0
ODCONF(2)          ODCF7        ODCF6          ODCF5           ODCF4         ODCF3            ODCF2       ODCF1       ODCF0
Note 1:      Unimplemented in PIC18(L)F26/27K42.
     2:      Unimplemented in PIC18(L)F26/27/45/46/47K42.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 269
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 16-7:            SLRCONx: SLEW RATE CONTROL REGISTER
   R/W-1/1           R/W-1/1       R/W-1/1          R/W-1/1          R/W-1/1           R/W-1/1           R/W-1/1         R/W-1/1
    SLRx7             SLRx6         SLRx5               SLRx4        SLRx3             SLRx2             SLRx1           SLRx0
bit 7                                                                                                                         bit 0


Legend:
R = Readable bit                 W = Writable bit                U = Unimplemented bit, read as ‘0’
‘1’ = Bit is set                 ‘0’ = Bit is cleared            x = Bit is unknown
-n/n = Value at POR and BOR/Value at all other Resets


bit 7-0            SLRx[7:0]: Slew Rate Control on Pins Rx[7:0], respectively
                   1 = Port pin slew rate is limited
                   0 = Port pin slews at maximum rate


TABLE 16-8:         SLEW RATE CONTROL REGISTERS
    Name             Bit 7        Bit 6          Bit 5          Bit 4          Bit 3             Bit 2           Bit 1        Bit 0
SLRCONA             SLRA7        SLRA6          SLRA5           SLRA4          SLRA3             SLRA2        SLRA1          SLRA0
SLRCONB             SLRB7        SLRB6          SLRB5           SLRB4          SLRB3             SLRB2        SLRB1          SLRB0
SLRCONC             SLRC7        SLRC6          SLRC5           SLRC4          SLRC3             SLRC2         SLRC1         SLRC0
SLRCOND(1)          SLRD7        SLRD6          SLRD5           SLRD4          SLRD3             SLRD2         SLRD1         SLRD0
SLRCONE(1)            —            —                —            —              —                SLRE2         SLRE1         SLRE0
SLRCONF(2)          SLRF7        SLRF6          SLRF5           SLRF4          SLRF3             SLRF2         SLRF1         SLRF0
Note 1:      Unimplemented in PIC18(L)F26/27K42.
     2:      Unimplemented in PIC18(L)F26/27/45/46/47K42.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 270
                            PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 16-8:               INLVLx: INPUT LEVEL CONTROL REGISTER
   R/W-1/1            R/W-1/1         R/W-1/1            R/W-1/1           R/W-1/1        R/W-1/1         R/W-1/1         R/W-1/1
   INLVLx7            INLVLx6         INLVLx5            INLVLx4           INLVLx3        INLVLx2         INLVLx1         INLVLx0
bit 7                                                                                                                           bit 0


Legend:
R = Readable bit                  W = Writable bit                      U = Unimplemented bit, read as ‘0’
‘1’ = Bit is set                  ‘0’ = Bit is cleared                  x = Bit is unknown
-n/n = Value at POR and BOR/Value at all other Resets


bit 7-0             INLVLx[7:0]: Input Level Select on Pins Rx[7:0], respectively
                    1 = ST input used for port reads and interrupt-on-change
                    0 = TTL input used for port reads and interrupt-on-change


TABLE 16-9:           INPUT LEVEL PORT REGISTERS
   Name             Bit 7        Bit 6           Bit 5             Bit 4          Bit 3        Bit 2           Bit 1          Bit 0
INLVLA             INLVLA7      INLVLA6         INLVLA5        INLVLA4          INLVLA3       INLVLA2         INLVLA1       INLVLA0
INLVLB             INLVLB7      INLVLB6         INLVLB5        INLVLB4          INLVLB3      INLVLB2(1)     INLVLB1(1)      INLVLB0
INLVLC             INLVLC7      INLVLC6         INLVLC5       INLVLC4(1)       INLVLC3(1)     INLVLC2         INLVLC1        INLVLC0
          (2)
INLVLD             INLVLD7      INLVLD6         INLVLD5        INLVLD4          INLVLD3       INLVLD2        INLVLD1(1)     INLVLD0(1)
INLVLE               —            —               —                 —           INLVLE3      INLVLE2(2)     INLVLE1(2)     INLVLE0(2)
INLVLF(3)          INLVLF7      INLVLF6         INLVLF5        INLVLF4          INLVLF3       INLVLF2         INLVLF1        INLVLF0
                                    2                    2
Note 1: Any peripheral using the I C pins read the I C ST inputs when enabled via RxyI2C.
     2: Unimplemented in PIC18(L)F26/27K42.
     3: Unimplemented in PIC18(L)F26/27/45/46/47K42.


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 271
                           PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 16-9:             RxyI2C: I2C PAD Rxy CONTROL REGISTER
        U-0          R/W-0/0        R/W-0/0            R/W-0/0            U-0           U-0           R/W-0/0         R/W-0/0
        —               SLEW                PU[1:0]                       —              —                   TH[1:0]
bit 7                                                                                                                         bit 0


Legend:
R = Readable bit                 W = Writable bit                    U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                  -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared                HS = Hardware set


bit 7              Unimplemented: Read as ‘0’
bit 6              SLEW: I2C specific slew rate limiting is enabled
                   1 = I2C specific slew rate limiting is enabled. Standard pad slew limiting is disabled. The SLRxy bit
                       is ignored.
                   0 = Standard GPIO Slew Rate; enabled/disabled via SLRxy bit.
bit 5-4            PU[1:0]: I2C Pull-up Selection bits
                   11 = Reserved
                   10 = 10x current of standard weak pull-up
                   01 = 2x current of standard weak pull-up
                   00 = Standard GPIO weak pull-up, enabled via WPUxy bit
bit 3-2            Unimplemented: Read as ‘0’
bit 1-0            TH[1:0]: I2C Input Threshold Selection bits
                   11 = SMBus 3.0 (1.35 V) input threshold
                   10 = SMBus 2.0 (2.1 V) input threshold
                   01 = I2C specific input thresholds
                   00 = Standard GPIO Input pull-up, enabled via INLVLxy registers


TABLE 16-10: I2C PAD CONTROL REGISTERS
   Name            Bit 7        Bit 6          Bit 5              Bit 4         Bit 3         Bit 2        Bit 1             Bit 0
RB1I2C              —          SLEW                     PU[1:0]                  —             —                   TH[1:0]
RB2I2C              —          SLEW                     PU[1:0]                  —             —                   TH[1:0]
RC3I2C              —          SLEW                     PU[1:0]                  —             —                   TH[1:0]
RC4I2C              —          SLEW                     PU[1:0]                  —             —                   TH[1:0]
RD0I2C(1)           —          SLEW                     PU[1:0]                  —             —                   TH[1:0]
RD1I2C(1)           —          SLEW                     PU[1:0]                  —             —                   TH[1:0]
Note 1:       Unimplemented in PIC18(L)F26/27K42.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 272
                           PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 16-11: SUMMARY OF REGISTERS ASSOCIATED WITH I/O
                                                                                                                                     Register on
        Name              Bit 7         Bit 6         Bit 5          Bit 4         Bit 3           Bit 2      Bit 1         Bit 0
                                                                                                                                       Page

PORTA                     RA7           RA6            RA5           RA4           RA3              RA2        RA1          RA0         265
PORTB                    RB7(1)        RB6(1)          RB5           RB4           RB3              RB2        RB1          RB0         265
PORTC                     RC7           RC6            RC5           RC4           RC3              RC2        RC1          RC0         265
PORTD(6)                  RD7           RD6            RD5           RD4           RD3              RD2        RD1          RD0         265
PORTE                      —             —              —             —           RE3(2)           RE2(6)     RE1(6)       RE0(6)       265
PORTF(7)                  RF7            RF6           RF5           RF4           RF3              RF2        RF1          RF0         265
TRISA                   TRISA7         TRISA6        TRISA5        TRISA4        TRISA3           TRISA2     TRISA1        TRISA0       266
TRISB                  TRISB7(3)     TRISB6(3)       TRISB5        TRISB4        TRISB3           TRISB2     TRISB1        TRISB0       266
TRISC                    TRISC7        TRISC6        TRISC5        TRISC4        TRISC3           TRISC2     TRISC1        TRISC0       266
TRISD(6)                 TRISD7        TRISD6        TRISD5        TRISD4        TRISD3           TRISD2     TRISD1        TRISD0       266
TRISE(6)                   —             —              —             —             —             TRISE2     TRISE1        TRISE0       266
TRISF(7)                 TRISF7        TRISF6        TRISF5        TRISF4         TRISF3          TRISF2     TRISF1        TRISF0       266
LATA                     LATA7         LATA6          LATA5         LATA4         LATA3            LATA2      LATA1         LATA0       267
LATB                     LATB7         LATB6         LATB5          LATB4         LATB3            LATB2     LATB1         LATB0        267
LATC                     LATC7         LATC6          LATC5         LATC4         LATC3            LATC2      LATC1         LATC0       267
LATD(6)                  LATD7         LATD6          LATD5         LATD4         LATD3            LATD2      LATD1         LATD0       267
LATE(6)                    —             —              —             —             —              LATE2     LATE1         LATE0        267
LATF(7)                  LATF7         LATF6          LATF5         LATF4         LATF3            LATF2      LATF1         LATF0       267
ANSELA                 ANSELA7       ANSELA6        ANSELA5       ANSELA4       ANSELA3       ANSELA2       ANSELA1       ANSELA0       268
ANSELB                 ANSELB7       ANSELB6        ANSELB5       ANSELB4       ANSELB3       ANSELB2       ANSELB1       ANSELB0       268
ANSELC                 ANSELC7        ANSELC6       ANSELC5       ANSELC4       ANSELC3           ANSELC2   ANSELC1       ANSELC0       268
ANSELD(6)              ANSELD7        ANSELD6       ANSELD5       ANSELD4       ANSELD3           ANSELD2   ANSELD1       ANSELD0       268
ANSELE(6)                  —             —              —             —             —         ANSELE2       ANSELE1       ANSELE0       268
ANSELF(7)               ANSELF7       ANSELF6       ANSELF5       ANSELF4        ANSELF3          ANSELF2   ANSELF1        ANSELF0      268
WPUA                    WPUA7          WPUA6         WPUA5         WPUA4         WPUA3            WPUA2      WPUA1         WPUA0        269
WPUB                    WPUB7          WPUB6         WPUB5         WPUB4         WPUB3            WPUB2      WPUB1         WPUB0        269
WPUC                    WPUC7          WPUC6         WPUC5         WPUC4         WPUC3            WPUC2      WPUC1         WPUC0        269
WPUD(6)                 WPUD7          WPUD6         WPUD5         WPUD4         WPUD3            WPUD2      WPUD1         WPUD0        269
WPUE                       —             —              —             —         WPUE3(4)      WPUE2(6)      WPUE1(6)      WPUE0(6)      269
WPUF(6)                  WPUF7         WPUF6         WPUF5         WPUF4          WPUF3           WPUF2      WPUF1         WPUF0        269
ODCONA                  ODCA7          ODCA6         ODCA5         ODCA4         ODCA3            ODCA2      ODCA1         ODCA0        270
ODCONB                  ODCB7          ODCB6         ODCB5         ODCB4         ODCB3            ODCB2      ODCB1         ODCB0        270
ODCONC                  ODCC7          ODCC6         ODCC5         ODCC4         ODCC3            ODCC2      ODCC1         ODCC0        270
ODCOND(6)                ODCD7         ODCD6         ODCD5         ODCD4          ODCD3           ODCD2      ODCD1         ODCD0        270
ODCONE(6)                  —             —              —             —             —             ODCE2      ODCE1         ODCE0        270
ODCONF(7)               ODCF7          ODCF6         ODCF5         ODCF4         ODCF3            ODCF2      ODCF1         ODCF0        270
SLRCONA                  SLRA7         SLRA6         SLRA5         SLRA4          SLRA3           SLRA2      SLRA1         SLRA0        271
SLRCONB                  SLRB7         SLRB6         SLRB5         SLRB4          SLRB3           SLRB2      SLRB1         SLRB0        271
SLRCONC                  SLRC7         SLRC6         SLRC5         SLRC4          SLRC3           SLRC2      SLRC1         SLRC0        271
SLRCOND(6)               SLRD7         SLRD6         SLRD5          SLRD4         SLRD3            SLRD2      SLRD1        SLRD0        271
SLRCONE(6)                 —             —              —             —             —             SLRE2      SLRE1         SLRE0        271
SLRCONF(7)               SLRF7         SLRF6         SLRF5          SLRF4         SLRF3            SLRF2      SLRF1         SLRF0       271
INLVLA                  INLVLA7       INLVLA6       INLVLA5        INLVLA4       INLVLA3          INLVLA2    INLVLA1       INLVLA0      272
INLVLB                  INLVLB7       INLVLB6       INLVLB5        INLVLB4       INLVLB3      INLVLB2(5)    INLVLB1(5)     INLVLB0      272
Legend:        — = unimplemented location, read as ‘0’. Shaded cells are not used by I/O Ports.
Note      1:   Bits RB6 and RB7 read ‘1’ while in Debug mode.
          2:   Bit PORTE3 is read-only, and will read ‘1’ when MCLRE = 1 (Master Clear enabled).
          3:   Bits RB6 and RB7 read ‘1’ while in Debug mode.
          4:   If MCLRE = 1, the weak pull-up in RE3 is always enabled; bit WPUE3 is not affected.
          5:   Any peripheral using the I2C pins read the I2C ST inputs when enabled via RxyI2C.
          6:   Unimplemented in PIC18(L)F26/27K42.
          7:   Unimplemented in PIC18(L)F26/27/45/46/47K42 parts.


 2017-2021 Microchip Technology Inc.                                                                                    DS40001919G-page 273
                          PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 16-11: SUMMARY OF REGISTERS ASSOCIATED WITH I/O (CONTINUED)
                                                                                                                                       Register on
       Name              Bit 7         Bit 6         Bit 5             Bit 4      Bit 3           Bit 2      Bit 1             Bit 0
                                                                                                                                         Page

INLVLC                 INLVLC7       INLVLC6        INLVLC5       INLVLC4(5)   INLVLC3(5)        INLVLC2    INLVLC1        INLVLC0        272
INLVLD(6)              INLVLD7       INLVLD6        INLVLD5        INLVLD4      INLVLD3          INLVLD2   INLVLD1(5)     INLVLD0(5)      272
INLVLF(7)              INLVLF7       INLVLF6        INLVLF5        INLVLF4      INLVLF3          INLVLF2    INLVLF1        INLVLF0        272
INLVLE                    —             —              —                —       INLVLE3             —         —                 —         272
RB1I2C                    —           SLEW                   PU[1:0]               —                —                TH[1:0]              273
RB2I2C                    —           SLEW                   PU[1:0]               —                —                TH[1:0]              273
RC3I2C                    —           SLEW                   PU[1:0]               —                —                TH[1:0]              273
RC4I2C                    —           SLEW                   PU[1:0]               —                —                TH[1:0]              273
RD0I2C(6)                 —           SLEW                   PU[1:0]               —                —                TH[1:0]              273
RD1I2C(6)                 —           SLEW                   PU[1:0]               —                —                TH[1:0]              273
Legend:       — = unimplemented location, read as ‘0’. Shaded cells are not used by I/O Ports.
Note     1:   Bits RB6 and RB7 read ‘1’ while in Debug mode.
         2:   Bit PORTE3 is read-only, and will read ‘1’ when MCLRE = 1 (Master Clear enabled).
         3:   Bits RB6 and RB7 read ‘1’ while in Debug mode.
         4:   If MCLRE = 1, the weak pull-up in RE3 is always enabled; bit WPUE3 is not affected.
         5:   Any peripheral using the I2C pins read the I2C ST inputs when enabled via RxyI2C.
         6:   Unimplemented in PIC18(L)F26/27K42.
         7:   Unimplemented in PIC18(L)F26/27/45/46/47K42 parts.


 2017-2021 Microchip Technology Inc.                                                                                   DS40001919G-page 274
