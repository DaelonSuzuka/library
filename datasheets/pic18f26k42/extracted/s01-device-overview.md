                      PIC18(L)F26/27/45/46/47/55/56/57K42
1.0      DEVICE OVERVIEW                                 • Serial Peripheral Interface: The Serial
                                                           Peripheral Interface (SPI) module is a
This document contains device specific information for     synchronous serial data communication bus that
the following devices:                                     operates in Full Duplex mode. Devices
• PIC18F26K42                • PIC18LF26K42                communicate in a host/client environment where
                                                           the host device initiates the communication. A
• PIC18F27K42                • PIC18LF27K42                client device is controlled through a Chip Select
• PIC18F45K42                • PIC18LF45K42                known as Client Select. Example client devices
• PIC18F46K42                • PIC18LF46K42                include serial EEPROMs, shift registers, display
                                                           drivers, A/D converters, or another PIC.
• PIC18F47K42                • PIC18LF47K42
                                                         • I2C Module: The I2C module provides a
• PIC18F55K42                • PIC18LF55K42
                                                           synchronous interface between the
• PIC18F56K42                • PIC18LF56K42                microcontroller and other I2C-compatible devices
• PIC18F57K42                • PIC18LF57K42                using the two-wire I2C serial bus. Devices
                                                           communicate in a host/client environment. The
• This family offers the advantages of all PIC18
                                                           I2C bus specifies two signal connections - Serial
  microcontrollers – namely, high computational
                                                           Clock (SCL) and Serial Data (SDA). Both the SCL
  performance at an economical price – with the
                                                           and SDA connections are bidirectional open-drain
  addition of high-endurance Program Flash Mem-
                                                           lines, each requiring pull-up resistors to the
  ory, Universal Asynchronous Receiver Transmit-
                                                           supply voltage.
  ter (UART), Serial Peripheral Interface (SPI),
  Inter-integrated Circuit (I2C), Direct Memory          • 12-bit A/D Converter with Computation: This
  Access (DMA), Configurable Logic Cells (CLC),            module incorporates programmable acquisition
  Signal Measurement Timer (SMT), Numerically              time, allowing for a channel to be selected and a
  Controlled Oscillator (NCO), and Analog-to-Digital       conversion to be initiated without waiting for a
  Converter with Computation (ADC2).                       sampling period and thus, reduces code
                                                           overhead. It has a new module called ADC2 with
                                                           computation features, which provides a digital
1.1      New Features                                      filter and threshold interrupt functions.
• Direct Memory Access Controller: The Direct
  Memory Access (DMA) Controller is designed to          1.2      Details on Individual Family
  service data transfers between different memory                 Members
  regions directly without intervention from the
                                                         Devices in the PIC18(L)F26/27/45/46/47/55/56/57K42
  CPU. By eliminating the need for CPU-intensive
                                                         family are available in 28-pin and 40/44/48-pin
  management of handling interrupts intended for
                                                         packages. The block diagram for this device is shown
  data transfers, the CPU now can spend more time
                                                         in Figure 3-1.
  on other tasks.
• Vectored Interrupt Controller: The Vectored            The similarities and differences among the devices are
  Interrupt Controller module reduces the numerous       listed in the PIC18(L)F2X/4X/5XK42 Family Types
  peripheral interrupt request signals to a single       Table (page 4). The pinouts for all devices are listed in
  interrupt request signal to the CPU. It assembles      Table 1.
  all of the interrupt request signals and resolves
  the interrupts based on both a fixed natural order
  priority and a user-assigned priority, thereby
  eliminating scanning of interrupt sources.
• Universal Asynchronous Receiver
  Transmitter: The Universal Asynchronous
  Receiver Transmitter (UART) module is a serial
  I/O communications peripheral. It contains all the
  clock generators, shift registers and data buffers
  necessary to perform an input or output serial
  data transfer, independent of device program
  execution. The UART can be configured as a full-
  duplex asynchronous system or one of several
  automated protocols. Full Duplex mode is useful
  for communications with peripheral systems, with
  DMX/DALI/LIN support.


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 19
 2017-2021 Microchip Technology Inc.


                                        TABLE 1-1:           DEVICE FEATURES
                                               Features            PIC18(L)F26K42   PIC18(L)F27K42   PIC18(L)F45K42   PIC18(L)F46K42        PIC18(L)F47K42    PIC18(L)F55K42     PIC18(L)F56K42     PIC18(L)F57K42
                                        Program Memory
                                                                       65536           131072            32768             65536                131072            32768              65536              131072
                                        (Bytes)
                                        Program Memory
                                                                       32768            65536            16384             32768                 65536            16384              32768              65536
                                        (Instructions)


                                                                                                                                                                                                                       PIC18(L)F26/27/45/46/47/55/56/57K42
                                        Data Memory (Bytes)             4096             8192             2048              4096                  8192             2048               4096               8192
                                        Data EEPROM
                                                                        1024             1024             256               1024                  1024              256               1024               1024
                                        Memory (Bytes)
                                                                    28-pin SPDIP     28-pin SPDIP
                                                                                                      40-pin PDIP       40-pin PDIP           40-pin PDIP      48-pin TQFP                           48-pin TQFP
                                                                     28-pin SOIC     28-pin SOIC                                                                                  48-pin TQFP
                                                                                                      40-pin UQFN       40-pin UQFN           40-pin UQFN      48-pin UQFN                           48-pin UQFN
                                        Packages                    28-pin SSOP      28-pin SSOP                                                                                  48-pin UQFN
                                                                                                      44-pin TQFP       44-pin TQFP           44-pin TQFP      48-pin VQFN                           48-pin VQFN
                                                                     28-pin QFN       28-pin QFN                                                                                  48-pin VQFN
                                                                                                       44-pin QFN        44-pin QFN            44-pin QFN
                                                                    28-pin UQFN      28-pin UQFN
                                        I/O Ports                    A,B,C,E(1)       A,B,C,E(1)      A,B,C,D, E(1)     A,B,C,D, E(1)         A,B,C,D, E(1)   A,B,C,D, E(1), F   A,B,C,D, E(1), F   A,B,C,D, E(1), F
                                        12-Bit Analog-to-Digital
                                        Conversion Module
                                                                      5 internal       5 internal       5 internal        5 internal           5 internal        5 internal         5 internal         5 internal
                                        (ADC2) with
                                                                     24 external      24 external      35 external       35 external          35 external       43 external        43 external        43 external
                                        Computation
                                        Accelerator
                                        Capture/Compare/
                                                                                                                                        4
                                        PWM Modules (CCP)
                                        10-Bit Pulse-Width
                                                                                                                                        4
                                        Modulator (PWM)
                                        Timers (16-/8-bit)                                                                              4/3
                                        Serial Communications                                                    1 UART, 1 UART with DMX/DALI/LIN, 2 I2C, 1 SPI
                                        Complementary
                                        Waveform Generator                                                                              3
                                        (CWG)
                                        Zero-Cross Detect
                                                                                                                                        1
                                        (ZCD)
                                        Data Signal Modulator
                                                                                                                                        1
DS40001919G-page 20


                                        (DSM)
                                        Signal Measurement
                                                                                                                                        1
                                        Timer (SMT)
                                        5-bit Digital to Analog
                                                                                                                                        1
                                        Converter (DAC)
                                        Numerically Controlled
                                                                                                                                        1
                                        Oscillator (NCO)
                                        TABLE 1-1:          DEVICE FEATURES (CONTINUED)
 2017-2021 Microchip Technology Inc.


                                               Features           PIC18(L)F26K42     PIC18(L)F27K42       PIC18(L)F45K42      PIC18(L)F46K42        PIC18(L)F47K42     PIC18(L)F55K42      PIC18(L)F56K42   PIC18(L)F57K42
                                        Comparator Module                                                                                       2
                                        Direct Memory Access
                                                                                                                                                2
                                        (DMA)
                                        Configurable Logic Cell
                                                                                                                                                4
                                        (CLC)


                                                                                                                                                                                                                             PIC18(L)F26/27/45/46/47/55/56/57K42
                                        Peripheral Pin Select
                                                                                                                                               Yes
                                        (PPS)
                                        Peripheral Module
                                                                                                                                               Yes
                                        Disable (PMD)
                                        16-bit CRC with
                                                                                                                                               Yes
                                        Scanner
                                        Programmable High/
                                        Low-Voltage Detect                                                                                     Yes
                                        (HLVD)
                                                                                                                                   POR, Programmable BOR,
                                                                                                                                      RESET Instruction,
                                                                                                                                       Stack Overflow,
                                        Resets (and Delays)
                                                                                                                                       Stack Underflow
                                                                                                                                        (PWRT, OST),
                                                                                                                                     MCLR, WDT, MEMV
                                                                                                                                        81 Instructions;
                                        Instruction Set
                                                                                                                            87 with Extended Instruction Set enabled
                                        Maximum Operating
                                                                                                                                             64 MHz
                                        Frequency
                                        Note 1:     PORTE is partially implemented. Pin RE3 is an input-only pin on 28/40/44/48-pin variants. In addition to that, on 40/44/48-pin variants, PORTE also
                                                    consists of RE0, RE1 and RE2 pins.
DS40001919G-page 21
                       PIC18(L)F26/27/45/46/47/55/56/57K42
1.3       Register and Bit naming                             1.3.2.3       Bit Fields
          conventions                                         Bit fields are two or more adjacent bits in the same
                                                              register. For example, the four Least Significant bits of
1.3.1       REGISTER NAMES                                    the T0CON0 register contain the output prescaler
When there are multiple instances of the same                 select bits. The short name for this field is OUTPS and
peripheral in a device, the peripheral control registers      the long name is T0OUTPS. Bit field access is only
will be depicted as the concatenation of a peripheral         possible in C programs. The following example
identifier, peripheral instance, and control identifier.      demonstrates a C program instruction for setting the
The control registers section will show just one              Timer0 output prescaler to the 1:6 Postscaler:
instance of all the register names with an ‘x’ in the place   T0CON0bits.OUTPS = 0x5;
of the peripheral instance number. This naming
                                                              Individual bits in a bit field can also be accessed with
convention may also be applied to peripherals when
                                                              long and short bit names. Each bit is the field name
there is only one instance of that peripheral in the
                                                              appended with the number of the bit position within the
device to maintain compatibility with other devices in
                                                              field. For example, the Most Significant mode bit has
the family that contain more than one.
                                                              the short bit name OUTPS3. The following two exam-
1.3.2       BIT NAMES                                         ples demonstrate assembly program sequences for
                                                              setting the Timer0 output prescaler to 1:6 Postscaler:
There are two variants for bit names:
                                                              Example 1:
• Short name: Bit function abbreviation
                                                              MOVLW     ~(1<<OUTPS3 | 1<<OUTPS1)
• Long name: Peripheral abbreviation + short name             ANDWF     T0CON0,F
                                                              MOVLW     1<<OUTPS2 | 1<<OUTPS0
1.3.2.1       Short Bit Names                                 IORWF     T0CON0,F
Short bit names are an abbreviation for the bit function.     Example 2:
For example, some peripherals are enabled with the
                                                              BCF       T0CON0,OUTPS3
EN bit. The bit names shown in the registers are the          BSF       T0CON0,OUTPS2
short name variant.                                           BCF       T0CON0,OUTPS1
Short bit names are useful when accessing bits in C           BSF       T0CON0,OUTPS0
programs. The general format for accessing bits by the
short name is RegisterNamebits.ShortName. For                 1.3.3        REGISTER AND BIT NAMING
example, the enable bit, EN, in the T0CON0 register                        EXCEPTIONS
can be set in C programs with the instruction
T0CON0bits.EN = 1.                                            1.3.3.1       Status, Interrupt, and Mirror Bits
Short names are generally not useful in assembly              Status, interrupt enables, interrupt flags, and mirror bits
programs because the same name may be used by                 are contained in registers that span more than one
different peripherals in different bit positions. When this   peripheral. In these cases, the bit name shown is
occurs, during the include file generation, all instances     unique so there is no prefix or short name variant.
of that short bit name are appended with an underscore
plus the name of the register in which the bit resides to
avoid naming contentions.

1.3.2.2       Long Bit Names
Long bit names are constructed by adding a peripheral
abbreviation prefix to the short name. The prefix is
unique to the peripheral thereby making every long bit
name unique. The long bit name for the Timer0 enable
bit is the Timer0 prefix, T0, appended with the enable
bit short name, EN, resulting in the unique bit name
T0EN.
Long bit names are useful in both C and assembly
programs. For example, in C the T0CON0 enable bit
can be set with the T0EN = 1 instruction. In assembly,
this bit can be set with the BSF T0CON0,T0EN
instruction.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 22
