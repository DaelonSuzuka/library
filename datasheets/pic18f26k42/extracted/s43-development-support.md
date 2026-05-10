                      PIC18(L)F26/27/45/46/47/55/56/57K42
43.0     DEVELOPMENT SUPPORT                               43.1     MPLAB X Integrated Development
                                                                    Environment Software
The PIC® microcontrollers (MCU) and dsPIC® digital
signal controllers (DSC) are supported with a full range   The MPLAB X IDE is a single, unified graphical user
of software and hardware development tools:                interface for Microchip and third-party software, and
• Integrated Development Environment                       hardware development tool that runs on Windows®,
                                                           Linux and Mac OS® X. Based on the NetBeans IDE,
  - MPLAB® X IDE Software
                                                           MPLAB X IDE is an entirely new IDE with a host of free
• Compilers/Assemblers/Linkers                             software components and plug-ins for high-
  - MPLAB XC Compiler                                      performance application development and debugging.
  - MPASMTM Assembler                                      Moving between tools and upgrading from software
  - MPLINKTM Object Linker/                                simulators to hardware debugging and programming
     MPLIBTM Object Librarian                              tools is simple with the seamless user interface.
  - MPLAB Assembler/Linker/Librarian for                   With complete project management, visual call graphs,
     Various Device Families                               a configurable watch window and a feature-rich editor
• Simulators                                               that includes code completion and context menus,
  - MPLAB X SIM Software Simulator                         MPLAB X IDE is flexible and friendly enough for new
                                                           users. With the ability to support multiple tools on
• Emulators
                                                           multiple projects with simultaneous debugging, MPLAB
  - MPLAB REAL ICE™ In-Circuit Emulator                    X IDE is also suitable for the needs of experienced
• In-Circuit Debuggers/Programmers                         users.
  - MPLAB ICD 3                                            Feature-Rich Editor:
  - PICkit™ 3
                                                           • Color syntax highlighting
• Device Programmers
                                                           • Smart code completion makes suggestions and
  - MPLAB PM3 Device Programmer                              provides hints as you type
• Low-Cost Demonstration/Development Boards,               • Automatic code formatting based on user-defined
  Evaluation Kits and Starter Kits                           rules
• Third-party development tools                            • Live parsing
                                                           User-Friendly, Customizable Interface:
                                                           • Fully customizable interface: toolbars, toolbar
                                                             buttons, windows, window placement, etc.
                                                           • Call graph window
                                                           Project-Based Workspaces:
                                                           • Multiple projects
                                                           • Multiple tools
                                                           • Multiple configurations
                                                           • Simultaneous debugging sessions
                                                           File History and Bug Tracking:
                                                           • Local file history feature
                                                           • Built-in support for Bugzilla issue tracker


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 734
                      PIC18(L)F26/27/45/46/47/55/56/57K42
43.2     MPLAB XC Compilers                                 43.4     MPLINK Object Linker/
The MPLAB XC Compilers are complete ANSI C
                                                                     MPLIB Object Librarian
compilers for all of Microchip’s 8, 16, and 32-bit MCU      The MPLINK Object Linker combines relocatable
and DSC devices. These compilers provide powerful           objects created by the MPASM Assembler. It can link
integration capabilities, superior code optimization and    relocatable objects from precompiled libraries, using
ease of use. MPLAB XC Compilers run on Windows,             directives from a linker script.
Linux or MAC OS X.
                                                            The MPLIB Object Librarian manages the creation and
For easy source level debugging, the compilers provide      modification of library files of precompiled code. When
debug information that is optimized to the MPLAB X          a routine from a library is called from a source file, only
IDE.                                                        the modules that contain that routine will be linked in
The free MPLAB XC Compiler editions support all             with the application. This allows large libraries to be
devices and commands, with no time or memory                used efficiently in many different applications.
restrictions, and offer sufficient code optimization for    The object linker/library features include:
most applications.
                                                            • Efficient linking of single libraries instead of many
MPLAB XC Compilers include an assembler, linker and           smaller files
utilities. The assembler generates relocatable object       • Enhanced code maintainability by grouping
files that can then be archived or linked with other          related modules together
relocatable object files and archives to create an
                                                            • Flexible creation of libraries with easy module
executable file. MPLAB XC Compiler uses the
                                                              listing, replacement, deletion and extraction
assembler to produce its object file. Notable features of
the assembler include:
                                                            43.5     MPLAB Assembler, Linker and
• Support for the entire device instruction set
                                                                     Librarian for Various Device
• Support for fixed-point and floating-point data
                                                                     Families
• Command-line interface
• Rich directive set                                        MPLAB Assembler produces relocatable machine
• Flexible macro language                                   code from symbolic assembly language for PIC24,
                                                            PIC32 and dsPIC DSC devices. MPLAB XC Compiler
• MPLAB X IDE compatibility
                                                            uses the assembler to produce its object file. The
                                                            assembler generates relocatable object files that can
43.3     MPASM Assembler                                    then be archived or linked with other relocatable object
The MPASM Assembler is a full-featured, universal           files and archives to create an executable file. Notable
macro assembler for PIC10/12/16/18 MCUs.                    features of the assembler include:

The MPASM Assembler generates relocatable object            • Support for the entire device instruction set
files for the MPLINK Object Linker, Intel® standard HEX     • Support for fixed-point and floating-point data
files, MAP files to detail memory usage and symbol          • Command-line interface
reference, absolute LST files that contain source lines     • Rich directive set
and generated machine code, and COFF files for              • Flexible macro language
debugging.
                                                            • MPLAB X IDE compatibility
The MPASM Assembler features include:
• Integration into MPLAB X IDE projects
• User-defined macros to streamline
  assembly code
• Conditional assembly for multipurpose
  source files
• Directives that allow complete control over the
  assembly process


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 735
                       PIC18(L)F26/27/45/46/47/55/56/57K42
43.6     MPLAB X SIM Software Simulator                      43.8     MPLAB ICD 3 In-Circuit Debugger
The MPLAB X SIM Software Simulator allows code
                                                                      System
development in a PC-hosted environment by                    The MPLAB ICD 3 In-Circuit Debugger System is
simulating the PIC MCUs and dsPIC DSCs on an                 Microchip’s most cost-effective, high-speed hardware
instruction level. On any given instruction, the data        debugger/programmer for Microchip Flash DSC and
areas can be examined or modified and stimuli can be         MCU devices. It debugs and programs PIC Flash
applied from a comprehensive stimulus controller.            microcontrollers and dsPIC DSCs with the powerful,
Registers can be logged to files for further run-time        yet easy-to-use graphical user interface of the MPLAB
analysis. The trace buffer and logic analyzer display        IDE.
extend the power of the simulator to record and track
                                                             The MPLAB ICD 3 In-Circuit Debugger probe is
program execution, actions on I/O, most peripherals
                                                             connected to the design engineer’s PC using a high-
and internal registers.
                                                             speed USB 2.0 interface and is connected to the target
The MPLAB X SIM Software Simulator fully supports            with a connector compatible with the MPLAB ICD 2 or
symbolic debugging using the MPLAB XC Compilers,             MPLAB REAL ICE systems (RJ-11). MPLAB ICD 3
and the MPASM and MPLAB Assemblers. The                      supports all MPLAB ICD 2 headers.
software simulator offers the flexibility to develop and
debug code outside of the hardware laboratory                43.9     PICkit 3 In-Circuit Debugger/
environment, making it an excellent, economical
software development tool.
                                                                      Programmer
                                                             The MPLAB PICkit 3 allows debugging and
43.7     MPLAB REAL ICE In-Circuit                           programming of PIC and dsPIC Flash microcontrollers
         Emulator System                                     at a most affordable price point using the powerful
                                                             graphical user interface of the MPLAB IDE. The
The MPLAB REAL ICE In-Circuit Emulator System is             MPLAB PICkit 3 is connected to the design engineer’s
Microchip’s next generation high-speed emulator for          PC using a full-speed USB interface and can be
Microchip Flash DSC and MCU devices. It debugs and           connected to the target via a Microchip debug (RJ-11)
programs all 8, 16 and 32-bit MCU, and DSC devices           connector (compatible with MPLAB ICD 3 and MPLAB
with the easy-to-use, powerful graphical user interface of   REAL ICE). The connector uses two device I/O pins
the MPLAB X IDE.                                             and the Reset line to implement in-circuit debugging
The emulator is connected to the design engineer’s           and In-Circuit Serial Programming™ (ICSP™).
PC using a high-speed USB 2.0 interface and is
connected to the target with either a connector              43.10 MPLAB PM3 Device Programmer
compatible with in-circuit debugger systems (RJ-11)
or with the new high-speed, noise tolerant, Low-             The MPLAB PM3 Device Programmer is a universal,
Voltage Differential Signal (LVDS) interconnection           CE compliant device programmer with programmable
(CAT5).                                                      voltage verification at VDDMIN and VDDMAX for
                                                             maximum reliability. It features a large LCD display
The emulator is field upgradable through future firmware     (128 x 64) for menus and error messages, and a mod-
downloads in MPLAB X IDE. MPLAB REAL ICE offers              ular, detachable socket assembly to support various
significant advantages over competitive emulators            package types. The ICSP cable assembly is included
including full-speed emulation, run-time variable            as a standard item. In Stand Alone mode, the MPLAB
watches, trace analysis, complex breakpoints, logic          PM3 Device Programmer can read, verify and program
probes, a ruggedized probe interface and long (up to         PIC devices without a PC connection. It can also set
three meters) interconnection cables.                        code protection in this mode. The MPLAB PM3
                                                             connects to the host PC via an RS-232 or USB cable.
                                                             The MPLAB PM3 has high-speed communications and
                                                             optimized algorithms for quick programming of large
                                                             memory devices, and incorporates an MMC card for file
                                                             storage and data applications.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 736
                      PIC18(L)F26/27/45/46/47/55/56/57K42
43.11 Demonstration/Development                             43.12 Third-Party Development Tools
      Boards, Evaluation Kits, and                          Microchip also offers a great collection of tools from
      Starter Kits                                          third-party vendors. These tools are carefully selected
A wide variety of demonstration, development and            to offer good value and unique functionality.
evaluation boards for various PIC MCUs and dsPIC            • Device Programmers and Gang Programmers
DSCs allows quick application development on fully            from companies, such as SoftLog and CCS
functional systems. Most boards include prototyping         • Software Tools from companies, such as Gimpel
areas for adding custom circuitry and provide                 and Trace Systems
application firmware and source code for examination        • Protocol Analyzers from companies, such as
and modification.                                             Saleae and Total Phase
The boards support a variety of features, including LEDs,   • Demonstration Boards from companies, such as
temperature sensors, switches, speakers, RS-232               MikroElektronika, Digilent® and Olimex
interfaces, LCD displays, potentiometers and additional     • Embedded Ethernet Solutions from companies,
EEPROM memory.                                                such as EZ Web Lynx, WIZnet and IPLogika®
The demonstration and development boards can be
used in teaching environments, for prototyping custom
circuits and for learning about various microcontroller
applications.
In addition to the PICDEM™ and dsPICDEM™
demonstration/development board series of circuits,
Microchip has a line of evaluation kits and
demonstration software for analog filter design,
KEELOQ® security ICs, CAN, IrDA®, PowerSmart
battery management, SEEVAL® evaluation system,
Sigma-Delta ADC, flow rate sensing, plus many more.
Also available are starter kits that contain everything
needed to experience the specified device. This usually
includes a single application and debug capability, all
on one board.
Check the Microchip web page (www.microchip.com)
for the complete list of demonstration, development
and evaluation kits.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 737
