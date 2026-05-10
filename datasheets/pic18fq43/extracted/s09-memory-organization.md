                                                                                            PIC18F27/47/57Q43
                                                                                           Memory Organization


9.    Memory Organization
      There are three types of memory in PIC18 microcontroller devices:
      •   Program Memory
      •   Data RAM
      •   Data EEPROM
      In Harvard architecture devices, the data and program memories use separate buses that allow for
      concurrent access of the two memory spaces. The data EEPROM, for practical purposes, can be
      regarded as a peripheral device, since it is addressed and accessed through a set of control registers.
      Additional detailed information on the operation of the Program Flash Memory and data EEPROM
      memory is provided in the “NVM - Nonvolatile Memory Module” chapter.

9.1   Program Memory Organization
      PIC18 microcontrollers implement a 21-bit Program Counter, which is capable of addressing a 2
      Mbyte program memory space. Accessing a location between the upper boundary of the physically
      implemented memory and the 2 Mbyte address will return all ‘0’s (a NOP instruction).
      Refer to the following tables for device memory maps and code protection Configuration bits
      associated with the various sections of PFM.
      The Reset vector address is at 000000h. The PIC18-Q43 devices feature a vectored interrupt
      controller with a dedicated interrupt vector table stored in the program memory. Refer to the “VIC -
      Vectored Interrupt Controller Module” chapter for more details.


--- p61 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                                   Memory Organization

Figure 9-1. Program and Data Memory Map
                                                                                                                    Rev. 40-000101E
                                                                                                                           4/20/2017


                                                                         Device
               Address
                                      PIC18Fx5Q43                   PIC18Fx6Q43                    PIC18Fx7Q43
               00 0000h
                   to
               00 3FFFh              Program Flash
                                        Memory
               00 4000h                                             Program Flash
                                       (16 KW) (1)
                   to                                                  Memory
               00 7FFFh                                               (32 KW) (1)                  Program Flash
                                                                                                      Memory
               00 8000h
                                                                                                     (64 KW) (1)
                   to
               00 FFFFh
               01 0000h
                                           Not
                   to
                                        Present(2)
               01 FFFFh                                                   Not
              02 0000h                                                 Present(2)
                                                                                                        Not
                  to
                                                                                                     Present(2)
              1F FFFFh
              20 0000h
                  to                                            User IDs (32 Words) (3)
              20 003Fh
              20 0040h
                  to                                                   Reserved
              2B FFFFh
              2C 0000h
                  to                                      Device Information Area (DIA)(3,5)
              2C 00FFh
              2C 0100h
                  to                                                   Reserved
              2F FFFFh
              30 0000h
                  to                                            Configuration Bytes(3)
              30 0009h
              30 000Ah
                  to                                                   Reserved
              37 FFFFh
              38 0000h
                  to                                         Data EEPROM (1024 Bytes)
              38 03FFh
              38 0400h
                  to                                                   Reserved
              3B FFFFh
              3C 0000h
                  to                                    Device Configuration Information (3,4,5)
              3C 0009h
              3C 000Ah
                  to                                                   Reserved
              3F FFFBh
              3F FFFCh
                  to                                          Revision ID (1 Word) (3,4,5)
              3F FFFDh
              3F FFFEh
                  to                                           Device ID (1 Word) (3,4,5)
              3F FFFFh

                 Notes: 1.     Storage Area Flash is implemented as the last 128 Words of User Flash, if enabled.
                          2.   The addresses do not roll over. The region is read as ‘0’.
                          3.   Not code-protected.
                          4.   Hard-coded in silicon.
                          5.   This region cannot be written by the user and it is not affected by a Bulk Erase.


--- p62 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                               Memory Organization

9.1.1   Memory Access Partition
        In the PIC18-Q43 devices, the program memory can be further partitioned into the following sub-
        blocks:
        • Application block
        •   Boot block
        •   Storage Area Flash (SAF) block
        Refer to the "Program Flash Memory Partition" table for more details.
9.1.1.1 Application Block
        Application block is where the user’s firmware resides by default. Default settings of the
        Configuration bits (BBEN = 1 and SAFEN = 1) assign all memory in the program Flash memory area
        to the application block. The WRTAPP Configuration bit is used to write-protect the application block.
9.1.1.2 Boot Block
        Boot block is an area in program memory that is ideal for storing bootloader code. Code placed in
        this area can be executed by the CPU. The boot block can be write-protected, independent of the
        main application block. The Boot Block is enabled by the BBEN Configuration bit and size is based on
        the value of the BBSIZE Configuration bits. The WRTB Configuration bit is used to write-protect the
        Boot Block.
9.1.1.3 Storage Area Flash
        Storage Area Flash (SAF) is the area in program memory that can be used as data storage. SAF is
        enabled by the SAFEN Configuration bit. If enabled, the code placed in this area cannot be executed
        by the CPU. The SAF block is placed at the end of memory and spans 128 Words. The WRTSAF
        Configuration bit is used to write-protect the Storage Area Flash.


                        Important: If write-protected locations are written to, memory is not changed
                        and the WRERR bit is set.


        Table 9-1. Program Flash Memory Partition
                                                                                   Partition(3)
               Region            Address            BBEN = 1               BBEN = 1           BBEN = 0              BBEN = 0
                                                    SAFEN = 1              SAFEN = 0          SAFEN = 1             SAFEN = 0

                                00 0000h
                                  ....
                                                                                              Boot Block            Boot Block
                              Last Boot Block
                              Memory Address

                              Last Boot Block
                             Memory Address(1)                       Application Block
                                    +1
                                   ....                                                                          Application Block
            Program Flash
                               Last Program      Application Block
               Memory
                             Memory Address(2)
                                  - 100h                                                   Application Block
                               Last Program
                             Memory Address(2)
                                  - FEh(4)                           Storage Area Flash                         Storage Area Flash
                                    ....                                   Block                                      Block
                               Last Program
                             Memory Address(2)


--- p63 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                                 Memory Organization

        Notes:
        1. Last Boot Block address is based on BBSIZE bits. Refer to the “Device Configuration” chapter
           for more details.
        2. For Last Program Memory address refer the table above.
        3. Refer to the “Device Configuration” chapter for BBEN and SAFEN bit definitions.
        4. Storage Area Flash is implemented as the last 128 Words of user Flash memory.

9.1.2   Program Counter
        The Program Counter (PC) specifies the address of the instruction to fetch for execution. The PC
        is 21 bits wide and is contained in three separate 8-bit registers. The low byte, known as the PCL
        register, is both readable and writable. The high byte, or PCH register, contains the PC[15:8] bits; it
        is not directly readable or writable. Updates to the PCH register are performed through the PCLATH
        register. The upper byte is called PCU. This register contains the PC[20:16] bits; it is also not directly
        readable or writable. Updates to the PCU register are performed through the PCLATU register.
        The contents of PCLATH and PCLATU are transferred to the Program Counter by any operation that
        writes PCL. Similarly, the upper two bytes of the Program Counter are transferred to PCLATH and
        PCLATU by an operation that reads PCL. This is useful for computed offsets to the PC (see the
        Computed GOTO section).
        The PC addresses bytes in the program memory. To prevent the PC from becoming misaligned with
        word instructions, the Least Significant bit of PCL is fixed to a value of ‘0’. The PC increments by two
        to address sequential instructions in the program memory.
        The CALL, RCALL, GOTO and program branch instructions write to the Program Counter directly. For
        these instructions, the contents of PCLATH and PCLATU are not transferred to the Program Counter.

9.1.3   Return Address Stack
        The return address stack allows any combination of up to 127 program calls and interrupts to occur.
        The PC is pushed onto the stack when a CALL or RCALL instruction is executed or an interrupt is
        Acknowledged. The PC value is pulled off the stack on a RETURN, RETLW or a RETFIE instruction.
        PCLATU and PCLATH are not affected by any of the RETURN or CALL instructions.
        The Stack Pointer is readable and writable and the address on the top of the stack is readable and
        writable through the Top-of-Stack (TOS) Special File registers. Data can also be pushed to or popped
        from the stack using these registers.
        A CALL type instruction causes a push onto the stack; the Stack Pointer is first incremented and
        the location pointed to by the Stack Pointer is written with the contents of the PC (already pointing
        to the instruction following the CALL). A RETURN type instruction causes a pop from the stack; the
        contents of the location pointed to by the STKPTR are transferred to the PC and then the Stack
        Pointer is decremented.
        The Stack Pointer is initialized to 0x00 after all Resets.

9.1.3.1 Top-of-Stack Access
        Only the top of the return address stack (TOS) is readable and writable. A set of three registers,
        TOSU:TOSH:TOSL, hold the contents of the stack location pointed to by the STKPTR register (see
        Figure 9-2). This allows users to implement a software stack if necessary. After a CALL, RCALL or
        interrupt, the software can read the pushed value by reading the TOSU:TOSH:TOSL registers. These
        values can be placed on a user defined software stack. At return time, the software can return these
        values to TOSU:TOSH:TOSL and do a return.
        The user must disable the Global Interrupt Enable (GIE) bits while accessing the stack to prevent
        inadvertent stack corruption.


--- p64 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                                        Memory Organization

        Figure 9-2. Return Address Stack and Associated Registers

                                                            Return Address Stack <20:0>
                                                                                          1111111
                                                                                          1111110
                                                                                          1111101


                                                                                                    STKPTR<6:0>
                           Top-of-Stack Registers
                                                                                                      0000010
                      TOSU        TOSH         TOSL
                       00h         1Ah          34h
                                                                                          0000011

                                                Top-of-Stack             001A34h          0000010
                                                                         000D58h          0000001
                                                                                          0000000


9.1.3.2 Return Stack Pointer
        The STKPTR register contains the Stack Pointer value. The Stack Overflow (STKOVF) Status bit and
        the Stack Underflow (STKUNF) Status bit can be accessed using the PCON0 register. The value of the
        Stack Pointer can be zero through 127. On Reset, the Stack Pointer value will be zero. The user may
        read and write the Stack Pointer value. After the PC is pushed onto the stack 128 times (without
        popping any values off the stack), the STKOVF bit is set. The STKOVF bit is cleared by software or by
        a POR. The action that takes place when the stack becomes full depends on the state of the Stack
        Overflow Reset Enable (STVREN) Configuration bit.
        If STVREN is set (default), a Reset will be generated and a Stack Overflow will be indicated by the
        STKOVF bit. This includes CALL and CALLW instructions, as well as stacking the return address during
        an interrupt response. The STKOVF bit will remain set and the Stack Pointer will be set to zero.
        If STVREN is cleared, the STKOVF bit will be set on the 128th push, and the Stack Pointer will remain
        at 127, but no Reset will occur. Any additional pushes will overwrite the 127th push, but the STKPTR
        will remain unchanged.
        Setting STKOVF = 1 in software will change the bit but will not generate a Reset.
        The STKUNF bit is set when a stack pop returns a value of ‘0’. The STKUNF bit is cleared by software
        or by POR. The action that takes place when the stack becomes full depends on the state of the
        Stack Overflow Reset Enable (STVREN) Configuration bit.
        If STVREN is set (default) and the stack has been popped enough times to unload the stack, the next
        pop will return a value of ‘0’ to the PC, it will set the STKUNF bit, and a Reset will be generated. This
        condition can be generated by the RETURN, RETLW and RETFIE instructions.
        If STVREN is cleared, the STKUNF bit will be set, but no Reset will occur.


                     Important: Returning a value of ‘0’ to the PC on an underflow has the effect of
                     vectoring the program to the Reset vector, where the stack conditions can be
                     verified and appropriate actions can be taken. This is not the same as a Reset, as
                     the contents of the SFRs are not affected.


9.1.3.3 PUSH and POP Instructions
        Since the Top-of-Stack is readable and writable, the ability to push values onto the stack and pull
        values off the stack without disturbing normal program execution is a desirable feature. The PIC18
        instruction set includes two instructions, PUSH and POP, that permit the TOS to be manipulated


--- p65 ---
                                                                                               PIC18F27/47/57Q43
                                                                                              Memory Organization

        under software control. TOSU, TOSH and TOSL can be modified to place data or a return address on
        the stack.
        The PUSH instruction places the current PC value onto the stack. This increments the Stack Pointer
        and loads the current PC value onto the stack.
        The POP instruction discards the current TOS by decrementing the Stack Pointer. The previous value
        pushed onto the stack then becomes the TOS value.
9.1.3.4 Fast Register Stack
        There are three levels of fast stack registers available - one for CALL type instructions and two for
        interrupts. A fast register stack is provided for the STATUS, WREG and BSR registers, to provide a
        “fast return” option for interrupts. It is loaded with the current value of the corresponding register
        when the processor vectors for an interrupt. All interrupt sources will push values into the stack
        registers. The values in the registers are then loaded back into their associated registers if the
        RETFIE, FAST instruction is used to return from the interrupt. Refer to the “Call Shadow Register”
        section for interrupt call shadow registers.
        The following example shows a source code example that uses the Fast Register Stack during a
        subroutine call and return.

                Example 9-1. Fast Register Stack Code Example

                 CALL SUB1, FAST ;STATUS, WREG, BSR SAVED IN FAST REGISTER STACK
                           •
                           •
                 SUB1:
                           •
                           •
                       RETURN, FAST   ;RESTORE VALUES SAVED IN FAST REGISTER STACK


9.1.4   Look-up Tables in Program Memory
        There may be programming situations that require the creation of data structures, or Look-up
        Tables, in program memory. For PIC18 devices, Look-up Tables can be implemented in two ways:
        •   Computed GOTO
        •   Table reads
9.1.4.1 Computed GOTO
        A computed GOTO is accomplished by adding an offset to the Program Counter. An example is
        shown in the following code example.
        A Look-up Table can be formed with an ADDWF PCL instruction and a group of RETLW nn
        instructions. The W register is loaded with an offset into the table before executing a call to that
        table. The first instruction of the called routine is the ADDWF PCL instruction. The next instruction
        executed will be one of the RETLW nn instructions that returns the value ‘nn’ to the calling function.
        The offset value (in WREG) specifies the number of bytes that the Program Counter will advance and
        must be multiples of two (LSb = 0).
        In this method, only one data byte may be stored in each instruction location and room on the
        return address stack is required.

                Example 9-2. Computed GOTO Using an Offset Value

                      RLNCF    OFFSET, W     ; W must be an even number, Max OFFSET = 127
                      CALL     TABLE

                      ORG      nn00h      ; 00 in LSByte ensures no addition overflow
                 TABLE:
                      ADDWF    PCL        ; Add OFFSET to program counter


--- p66 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                                Memory Organization
                      RETLW      A           ; Value @ OFFSET=0
                      RETLW      B           ; Value @ OFFSET=1
                      RETLW      C           ; Value @ OFFSET=2
                        .
                        .
                        .


9.1.4.2 Program Flash Memory Access
       A more compact method of storing data in program memory allows two bytes of data to be stored in
       each instruction location.
       Look-up Table data may be stored two bytes per program word by using table reads and writes.
       The Table Pointer (TBLPTR) register specifies the byte address and the Table Latch (TABLAT) register
       contains the data that are read from or written to program memory. Data are transferred to or from
       program memory one byte at a time.
       Table read and table write operations are discussed further in the “Table Read Operations” and
       “Table Write Operations” sections in the “NVM - Nonvolatile Memory Module” chapter.

9.2    Device Information Area
       The Device Information Area (DIA) is a dedicated region in the program memory space. The DIA
       contains the calibration data for the internal temperature indicator module, the Microchip Unique
       Identifier words, and the Fixed Voltage Reference voltage readings measured in mV.
       The complete DIA table is shown below, followed by a description of each region and its
       functionality. The data are mapped from 2C0000h to 2C003Fh. These locations are read-only and
       cannot be erased or modified. The data are programmed into the device during manufacturing.

       Table 9-2. Device Information Area
                 Address Range                  Name of Region                         Standard Device Information
                                                      MUI0
                                                      MUI1
                                                      MUI2
                                                      MUI3
               2C0000h-2C0011h                        MUI4              Microchip Unique Identifier (9 Words)
                                                      MUI5
                                                      MUI6
                                                      MUI7
                                                      MUI8
               2C0012h-2C0013h                        MUI9              Reserved (1 Word)
                                                      EUI0
                                                      EUI1
                                                      EUI2
                                                      EUI3
               2C0014h-2C0023h                                          Optional External Unique Identifier (8 Words)
                                                      EUI4
                                                      EUI5
                                                      EUI6
                                                      EUI7

               2C0024h-2C0025h                      TSLR1(1)                     0.1C × 256
                                                                        Gain =      count (low range setting)
                                                                        Temperature indicator ADC reading at 90°C (low range
               2C0026h-2C0027h                      TSLR2(1)
                                                                        setting)
               2C0028h-2C0029h                      TSLR3(1)            Offset (low range setting)


--- p67 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                                  Memory Organization

        ...........continued
                   Address Range                 Name of Region                         Standard Device Information

                  2C002Ah-2C002Bh                    TSHR1(2)                     0.1C × 256
                                                                         Gain =      count (high range setting)
                                                                         Temperature indicator ADC reading at 90°C (high range
                  2C002Ch-2C002Dh                    TSHR2(2)
                                                                         setting)
                  2C002Eh-2C002Fh                    TSHR3(2)            Offset (high range setting)
                  2C0030h-2C0031h                     FVRA1X             ADC FVR1 Output voltage for 1x setting (in mV)
                  2C0032h-2C0033h                     FVRA2X             ADC FVR1 Output Voltage for 2x setting (in mV)
                  2C0034h-2C0035h                     FVRA4X             ADC FVR1 Output Voltage for 4x setting (in mV)
                  2C0036h-2C0037h                     FVRC1X             Comparator FVR2 output voltage for 1x setting (in mV)
                  2C0038h-2C0039h                     FVRC2X             Comparator FVR2 output voltage for 2x setting (in mV)
                  2C003Ah-2C003Bh                     FVRC4X             Comparator FVR2 output voltage for 4x setting (in mV)
                  2C003Ch-2C003Fh                                        Unassigned (2 Words)
        Notes:
        1.    TSLR: Address 2C0024h-2C0029h store the measurements for the low range setting of the temperature sensor at VDD =
              3V, VREF+ = 2.048V from FVR1.
        2.    TSHR: Address 2C002Ah-2C002Fh store the measurements for the high range setting of the temperature sensor at VDD
              = 3V, VREF+ = 2.048V from FVR1.


9.2.1   Microchip Unique Identifier (MUI)
        This family of devices is individually encoded during final manufacturing with a Microchip Unique
        Identifier (MUI). The MUI cannot be user-erased. This feature allows for manufacturing traceability
        of Microchip Technology devices in applications where this is required. It may also be used by the
        application manufacturer for a number of functions that require unverified unique identification,
        such as:
        • Tracking the device
        •    Unique serial number
        The MUI is stored in read-only locations, located between 2C0000h to 2C0013h in the DIA space. The
        DIA table lists the addresses of the identifier words.


                       Important: For applications that require verified unique identification, contact
                       the Microchip Technology sales office to create a Serialized Quick Turn
                       Programming option.


9.2.2   External Unique Identifier (EUI)
        The EUI data are stored at locations 2C0014h-2C0023h in the program memory region. This region
        is an optional space for placing application specific information. The data are coded per customer
        requirements during manufacturing. The EUI cannot be erased by a Bulk Erase command.


                       Important: Data are stored in this address range on receiving a request from
                       the customer. The customer may contact the local sales representative or Field
                       Applications Engineer and provide them the unique identifier information that is
                       required to be stored in this region.


9.2.3   Standard Parameters for the Temperature Sensor
        The purpose of the temperature indicator module is to provide a temperature-dependent voltage
        that can be measured by an analog module. The DIA table contains standard parameters for the


--- p68 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                              Memory Organization

            temperature sensor for low and high range. The values are measured during test and are unique to
            each device. The calibration data can be used to plot the approximate sensor output voltage, VTSENSE
            vs. Temperature curve. The “Temperature Indicator Module” chapter explains the operation of the
            Temperature Indicator module and defines terms such as the low range and high range settings of
            the sensor.

9.2.4       Fixed Voltage Reference Data
            The DIA stores measured FVR voltages for this device in mV for different buffer settings of 1x, 2x
            or 4x at program memory locations. For more information on the FVR, refer to the “FVR - Fixed
            Voltage Reference” chapter.

9.3         Device Configuration Information
            The Device Configuration Information (DCI) is a dedicated region in the program memory mapped
            from 3C0000h to 3C0009h. The data stored in these location is read-only and cannot be erased.
            Refer to the table below for the complete DCI table address and description. The DCI holds
            information about the device, which is useful for programming and Bootloader applications.
            The erase size is the minimum erasable unit in the PFM, expressed as rows. The total device Flash
            memory capacity is (Erase size * Number of user-erasable pages).

  Table 9-3. Device Configuration Information for PIC18FxxQ43 Devices
                                                                                          VALUE
           ADDRESS            NAME        DESCRIPTION                                                                        UNITS
                                                            PIC18F25/45/55Q43       PIC18F26/46/56Q43   PIC18F27/47/57Q43
        3C0000h-3C0001h        ERSIZ     Erase page size            128                     128               128            Words
                                        Number of write
        3C0002h-3C0003h        WLSIZ                                 0                       0                 0             Words
                                        latches per row
                                        Number of user-
        3C0004h-3C0005h        URSIZ                                128                     256               512            Pages
                                        erasable pages
                                          Data EEPROM
        3C0006h-3C0007h        EESIZ                                1024                    1024              1024           Bytes
                                          memory size
        3C0008h-3C0009h        PCNT         Pin count            28/40(1)/48             28/40(1)/48       28/40(1)/48        Pins
   Note:
   1.     Pin count of 40 is also used for 44-pin part.


9.4         Data Memory Organization

                            Important: The operation of some aspects of data memory are changed when
                            the PIC18 extended instruction set is enabled. See the PIC18 Instruction Execution
                            and the Extended Instruction Set section for more information.


            The data memory in PIC18 devices is implemented as static RAM. The memory space is divided
            into as many as 64 banks with 256 bytes each. The Data Memory Map table below shows the data
            memory organization for all devices in the device family.
            The data memory contains Special Function Registers (SFRs) and General Purpose Registers (GPRs).
            The SFRs are used for control and status of the controller and peripheral functions, while GPRs
            are used for data storage and scratchpad operations in the user’s application. Any read of an
            unimplemented location will read as ‘0’.
            The value in the Bank Select Register (BSR) determines which bank is being accessed. The instruction
            set and architecture allow operations across all banks. The entire data memory may be accessed
            by Direct, Indirect or Indexed Addressing modes. Addressing modes are discussed later in this
            subsection.


--- p69 ---
                                                                                   PIC18F27/47/57Q43
                                                                                  Memory Organization

To ensure that commonly used registers (SFRs and select GPRs) can be accessed in a single cycle,
PIC18 devices implement an Access Bank. This is a virtual 256-byte memory space that provides fast
access to SFRs and the top half of GPR Bank 5 without using the Bank Select Register. The Access
Bank section provides a detailed description of the Access RAM.


--- p70 ---
                                                                                                PIC18F27/47/57Q43
                                                                                               Memory Organization

Figure 9-3. Data Memory Map

              BSR                                 PIC18F
    BanK                 addr[7:0]
            addr[13:8]                  x5Q43     x6Q43      x7Q43
      0    'b00 0000     0x00-0xFF
      1    'b00 0001     0x00-0xFF
      2    'b00 0010     0x00-0xFF
      3    'b00 0011     0x00-0xFF
           'b00 0100     0x00-0x5F                                                Virtual Access Bank
      4
           'b00 0100     0x60-0xFF                                                Access RAM       0x00-0x5F
           'b00 0101     0x00-0x5F                                                Fast SFR         0x60-0xFF
      5
           'b00 0101     0x60-0xFF
      6    'b00 0110     0x00-0xFF
      7    'b00 0111     0x00-0xFF
      8    'b00 1000     0x00-0xFF
      9    'b00 1001     0x00-0xFF
      10   'b00 1010     0x00-0xFF
      11   'b00 1011     0x00-0xFF
      12   'b00 1100     0x00-0xFF
      13   'b00 1101     0x00-0xFF
      14   'b00 1110     0x00-0xFF
      15   'b00 1111     0x00-0xFF
      16   'b01 0000     0x00-0xFF
      17   'b01 0001     0x00-0xFF
      18   'b01 0010     0x00-0xFF
      19   'b01 0011     0x00-0xFF
      20   'b01 0100     0x00-0xFF
      21   'b01 0101     0x00-0xFF
      22   'b01 0110     0x00-0xFF
      23   'b01 0111     0x00-0xFF
      24   'b01 1000     0x00-0xFF
      25   'b01 1001     0x00-0xFF
      26   'b01 1010     0x00-0xFF
      27   'b01 1011     0x00-0xFF
      28   'b01 1100     0x00-0xFF
      29   'b01 1101     0x00-0xFF
      30   'b01 1110     0x00-0xFF
      31   'b01 1111     0x00-0xFF
      32   'b10 0000     0x00-0xFF
      33   'b10 0001     0x00-0xFF
      34   'b10 0010     0x00-0xFF
      35   'b10 0011     0x00-0xFF
      36   'b10 0100     0x00-0xFF
      37   'b10 0101     0x00-0xFF                                                           GPR
      38   'b10 0110     0x00-0xFF                                                           SFR
      to        -             -                                                          Buffer RAM
      63   'b11 1111     0x00-0xFF                                                     Unimplemented


--- p71 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                                   Memory Organization

9.4.1   Bank Select Register
        To rapidly access the RAM space in PIC18 devices, the memory is split using the banking scheme.
        This divides the memory space into contiguous banks of 256 bytes each. Depending on the
        instruction, each location can be addressed directly by its full address or by an 8-bit low-order
        address and a bank pointer.
        Most instructions in the PIC18 instruction set make use of the bank pointer known as the Bank
        Select Register (BSR). This SFR holds the Most Significant bits of a location’s address; the instruction
        itself includes the eight Least Significant bits. The BSR can be loaded directly by using the MOVLB
        instruction.
        The value of the BSR indicates the bank in data memory being accessed; the eight bits in the
        instruction show the location in the bank and can be thought of as an offset from the bank’s lower
        boundary. The relationship between the BSR’s value and the bank division in data memory is shown
        in Figure 9-4.
        When writing the firmware in assembly, the user must ensure that the proper bank is selected
        before performing a data read or write. When using the C compiler to write the firmware, the BSR is
        tracked and maintained by the compiler.
        While any bank can be selected, only those banks that are actually implemented can be read or
        written to. Writes to unimplemented banks are ignored, while reads from unimplemented banks will
        return ‘0’. Refer to Figure 9-3 for a list of implemented banks.

        Figure 9-4. Use of the Bank Select Register (Direct Addressing)
                                                                                                                             Rev. 30-000108B
                                                                                                                                   02/28/2019


                             BSR(1)                         Data Memory                               From Opcode
               7                              0    0000h                        00h          7                              0
                0   0   0    0   0    0   1   0                 Bank 0                        1   1   1    1   1    1   1   1
                                                                                FFh
                                                  0100h                         00h
                                                                 Bank 1
               Bank Select                                                      FFh
                                                  0200h                         00h
                                                                 Bank 2
                                                                                FFh
                                                  0300h

                                                                 Bank 3
                                                                 through
                                                                 Bank 61


                                                  3E00h                         00h
                                                                Bank 62
                                                                                FFh
                                                  3F00h                         00h
                                                                Bank 63
                                                  3FFFh                         FFh

             Note 1:    The Access RAM bit of the instruction can be used to force an override of the selected bank (BSR value) to
                        the registers of the Access Bank.


9.4.2   Access Bank
        While the use of the BSR with an embedded 8-bit address allows users to address the entire range of
        data memory, it also means that the user must ensure that the correct bank is selected. Otherwise,
        data may be read from or written to the wrong location. Verifying and/or changing the BSR for each
        read or write to data memory can become inefficient.
        To streamline access for the most commonly used data memory locations, the data memory is
        configured with a virtual Access Bank, which allows users to access a mapped block of memory


--- p72 ---
                                                                                                PIC18F27/47/57Q43
                                                                                               Memory Organization

        without specifying a BSR. The Access Bank consists of the first 96 bytes of memory in Bank 5
        (0500h-055Fh) and the last 160 bytes of memory in Bank 4 (0460h-04FFh). The upper half is
        known as the “Access RAM” and is composed of GPRs. The lower half is where the device’s SFRs
        are mapped. These two areas are mapped contiguously as the virtual Access Bank and can be
        addressed in a linear fashion by an 8-bit address (see the Data Memory Map section).
        The Access Bank is used by core PIC18 instructions that include the Access RAM bit (the ‘a’ parameter
        in the instruction). When ‘a’ is equal to ‘1’, the instruction uses the BSR and the 8-bit address
        included in the opcode for the data memory address. When ‘a’ is ‘0’, the instruction ignores the BSR
        and uses the Access Bank address map.
        Using this “forced” addressing allows the instruction to operate on a data address in a single cycle
        without updating the BSR first. Access RAM also allows for faster and more code efficient context
        saving and switching of variables.
        The mapping of the Access Bank is slightly different when the extended instruction set is enabled
        (XINST Configuration bit = 1). This is discussed in more detail in the Mapping the Access Bank in
        Indexed Liberal Offset Mode section.

9.5     Data Addressing Modes

                       Important: The execution of some instructions in the core PIC18 instruction set
                       are changed when the PIC18 extended instruction set is enabled. See the Data
                       Memory and the Extended Instruction Set section for more information.


        Information in the data memory space can be addressed in several ways. For most instructions,
        the Addressing mode is fixed. Other instructions may use up to three modes, depending on which
        operands are used and whether or not the extended instruction set is enabled.
        The Addressing modes are:
        •   Inherent
        •   Literal
        •   Direct
        •   Indirect
        An additional Addressing mode, Indexed Literal Offset, is available when the extended instruction
        set is enabled (XINST Configuration bit = 1). Its operation is discussed in greater detail in the Indexed
        Addressing with Literal Offset section.

9.5.1   Inherent and Literal Addressing
        Many PIC18 control instructions do not need any argument at all; they either perform an operation
        that globally affects the device or they operate implicitly on one register. This Addressing mode is
        known as Inherent Addressing. Examples include SLEEP, RESET and DAW.
        Other instructions work in a similar way but require an additional explicit argument in the opcode.
        This is known as Literal Addressing mode because they require some literal value as an argument.
        Examples include ADDLW and MOVLW, which, respectively, add or move a literal value to the W
        register. Other examples include CALL and GOTO, which include a program memory address.

9.5.2   Direct Addressing
        Direct Addressing specifies all or part of the source and/or destination address of the operation
        within the opcode itself. The options are specified by the arguments accompanying the instruction.
        In the core PIC18 instruction set, bit-oriented and byte-oriented instructions use some version of
        Direct Addressing by default. All of these instructions include some 8-bit literal address as their Least


--- p73 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                                 Memory Organization

        Significant Byte. This address specifies either a register address in one of the banks of data RAM
        (see the Data Memory Organization section) or a location in the Access Bank (see the Access Bank
        section) as the data source for the instruction.
        The Access RAM bit ‘a’ determines how the address is interpreted. When ‘a’ is ‘1’, the contents of
        the BSR (see the Bank Select Register section) are used with the address to determine the complete
        12-bit address of the register. When ‘a’ is ‘0’, the address is interpreted as being a register in the
        Access Bank.
        The destination of the operation’s results is determined by the destination bit ‘d’. When ‘d’ is ‘1’, the
        results are stored back in the source register, overwriting its original contents. When ‘d’ is ‘0’, the
        results are stored in the W register. Instructions without the ‘d’ argument have a destination that is
        implicit in the instruction; their destination is either the target register being operated on or the W
        register.

9.5.3   Indirect Addressing
        Indirect Addressing allows the user to access a location in data memory without giving a fixed
        address in the instruction. This is done by using File Select Registers (FSRs) as pointers to the
        locations which are to be read or written. Since the FSRs are themselves located in RAM as Special
        File Registers, they can also be directly manipulated under program control. This makes FSRs very
        useful in implementing data structures, such as tables and arrays in data memory.
        The registers for Indirect Addressing are also implemented with Indirect File Operands (INDFs) that
        permit automatic manipulation of the pointer value with auto-incrementing, auto-decrementing
        or offsetting with another value. This allows for efficient code, using loops, such as the following
        example of clearing an entire RAM bank.

                Example 9-3. How to Clear RAM (Bank 1) Using Indirect Addressing

                       LFSR     FSR0,100h      ; Set FSR0 to beginning of Bank1
                 NEXT:
                       CLRF     POSTINC0       ; Clear location in Bank1 then increment FSR0

                       BTFSS    FSR0H,1        ; Has high FSR0 byte incremented to next bank?
                       BRA      NEXT           ; NO, clear next byte in Bank1

                 CONTINUE:                     ; YES, continue


9.5.3.1 FSR Registers and the INDF Operand
        At the core of Indirect Addressing are three sets of registers: FSR0, FSR1 and FSR2. Each represent
        a pair of 8-bit registers, FSRnH and FSRnL. Each FSR pair holds the full address of the RAM location.
        The FSR value can address the entire range of the data memory in a linear fashion. The FSR register
        pairs, then, serve as pointers to data memory locations.
        Indirect Addressing is accomplished with a set of Indirect File Operands, INDF0 through INDF2.
        These can be thought of as “virtual” registers; they are mapped in the SFR space but are not
        physically implemented. Reading or writing to a particular INDF register actually accesses its
        corresponding FSR register pair. A read from INDF1, for example, reads the data at the address
        indicated by FSR1H:FSR1L. Instructions that use the INDF registers as operands actually use the
        contents of their corresponding FSR as a pointer to the instruction’s target. The INDF operand is just
        a convenient way of using the pointer.
        Because Indirect Addressing uses a full address, the FSR value can target any location in any bank
        regardless of the BSR value. However, the Access RAM bit must be cleared to zero to ensure that the
        INDF register in Access space is the object of the operation instead of a register in one of the other
        banks. The assembler default value for the Access RAM bit is zero when targeting any of the indirect
        operands.


--- p74 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                                 Memory Organization

9.5.3.2 FSR Registers and POSTINC, POSTDEC, PREINC and PLUSW
       In addition to the INDF operand, each FSR register pair also has four additional indirect operands.
       Like INDF, these are “virtual” registers that cannot be directly read or written. Accessing these
       registers actually accesses the location to which the associated FSR register pair points and also
       performs a specific action on the FSR value. They are:
       •     POSTDEC: Accesses the location to which the FSR points, then automatically decrements the FSR
             by 1 afterwards
       •     POSTINC: Accesses the location to which the FSR points, then automatically increments the FSR
             by 1 afterwards
       •     PREINC: Automatically increments the FSR by one, then uses the location to which the FSR points
             in the operation
       •     PLUSW: Adds the signed value of the W register (range of -127 to 128) to that of the FSR and uses
             the location to which the result points in the operation.
       In this context, accessing an INDF register uses the value in the associated FSR register without
       changing it. Similarly, accessing a PLUSW register gives the FSR value an offset in the W register;
       however, neither W nor the FSR is actually changed in the operation. Accessing the other virtual
       registers changes the value of the FSR register.

       Figure 9-5. Indirect Addressing
                                                                                                                               Rev. 30-000109A
                                                                                                                                      4/18/2017

                                                                                                             Data Memory
                                                                                                     0000h                    00h
            Using an instruction with one of the                 ADDWF, INDF1, 0                               Bank 0
            indirect addressing registers as the                                                                              FFh
                                                                                                     0100h                    00h
                         operand....                                                                            Bank 1
                                                                                                                              FFh
                                                                                                     0200h                    00h
                                                                                                                Bank 2
            ...uses the 14-bit address stored in                     FSR1H:FSR1L                                              FFh
             the FSR pair associated with that                                                       0300h
                         register....                   7                0   7                0
                                                                                                                Bank 3
                                                       x x 11 1 1 1 0        1 1 0 0 1 1 0 0
                                                                                                                through
                                                                                                                Bank 61

               ...to determine the data memory
            location to be used in that operation.
             In this case, the FSR1 pair contains
             3ECCh. This means the contents of
            location 3ECCh will be added to that                                                     3E00h                    00h
             of the W register and stored back in                                                              Bank 62
                            3ECCh.                                                                                            FFh
                                                                                                     3F00h                    00h
                                                                                                               Bank 63
                                                                                                     3FFFh                    FFh


       Operations on the FSRs with POSTDEC, POSTINC and PREINC affect the entire register pair; that is,
       rollovers of the FSRnL register from FFh to 00h carry over to the FSRnH register. On the other hand,
       results of these operations do not change the value of any flags in the STATUS register (e.g., Z, N, OV,
       etc.).
        
       The PLUSW register can be used to implement a form of Indexed Addressing in the data memory
       space. By manipulating the value in the W register, users can reach addresses that are fixed
       offsets from pointer addresses. In some applications, this can be used to implement some powerful
       program control structure, such as software stacks, inside of data memory.


--- p75 ---
                                                                                               PIC18F27/47/57Q43
                                                                                              Memory Organization

9.5.3.3 Operations by FSRs on FSRs
        Indirect Addressing operations that target other FSRs or virtual registers represent special cases. For
        example, using an FSR to point to one of the virtual registers will not result in successful operations.
        As a specific case, assume that FSR0H:FSR0L contains the address of INDF1. Attempts to read the
        value of the INDF1 using INDF0 as an operand will return 00h. Attempts to write to INDF1 using
        INDF0 as the operand will result in a NOP.
        On the other hand, using the virtual registers to write to an FSR pair may not occur as planned. In
        these cases, the value will be written to the FSR pair but without any incrementing or decrementing.
        Thus, writing to either the INDF2 or POSTDEC2 register will write the same value to FSR2H:FSR2L.
        Since the FSRs are physical registers mapped in the SFR space, they can be manipulated through all
        direct operations. Users need to proceed cautiously when working on these registers, particularly if
        their code uses Indirect Addressing.
        Similarly, operations by Indirect Addressing are permitted on all other SFRs. Users need to exercise
        the appropriate caution that they do not inadvertently change settings that might affect the
        operation of the device.

9.6     Data Memory and the Extended Instruction Set
        Enabling the PIC18 extended instruction set (XINST Configuration bit = 1) significantly changes
        certain aspects of data memory and its addressing. Specifically, the use of the Access Bank for many
        of the core PIC18 instructions is different; this is due to the introduction of a new Addressing mode
        for the data memory space.
        What does not change is just as important. The size of the data memory space is unchanged, as well
        as its linear addressing. The SFR map remains the same. Core PIC18 instructions can still operate
        in both Direct and Indirect Addressing mode; inherent and literal instructions do not change at all.
        Indirect addressing with FSR0 and FSR1 also remain unchanged.

9.6.1   Indexed Addressing with Literal Offset
        Enabling the PIC18 extended instruction set changes the behavior of Indirect Addressing using the
        FSR2 register pair within Access RAM. Under the proper conditions, instructions that use the Access
        Bank – that is, most bit-oriented and byte-oriented instructions – can invoke a form of Indexed
        Addressing using an offset specified in the instruction. This special Addressing mode is known as
        Indexed Addressing with Literal Offset or Indexed Literal Offset mode.
        When using the extended instruction set, this Addressing mode requires the following:
        •   The use of the Access Bank is forced (‘a’ = 0) and
        •   The file address argument is less than or equal to 5Fh.
        Under these conditions, the file address of the instruction is not interpreted as the lower byte of an
        address (used with the BSR in Direct Addressing) or as an 8-bit address in the Access Bank. Instead,
        the value is interpreted as an offset value to an Address Pointer, specified by FSR2. The offset and
        the contents of FSR2 are added to obtain the target address of the operation.

9.6.2   Instructions Affected by Indexed Literal Offset Mode
        Any of the core PIC18 instructions that can use Direct Addressing are potentially affected by the
        Indexed Literal Offset Addressing mode. This includes all byte-oriented and bit-oriented instructions
        or almost one-half of the standard PIC18 instruction set. Instructions that only use Inherent or
        Literal Addressing modes are unaffected.
        Additionally, byte-oriented and bit-oriented instructions are not affected if they do not use the
        Access Bank (Access RAM bit is ‘1’) or include a file address of 60h or above. Instructions meeting
        these criteria will continue to execute as before. A comparison of the different possible Addressing
        modes when the extended instruction set is enabled is shown in the following figure.


--- p76 ---
                                                                                                                           PIC18F27/47/57Q43
                                                                                                                          Memory Organization

        Those who desire to use byte-oriented or bit-oriented instructions in the Indexed Literal Offset
        mode need to note the changes to assembler syntax for this mode. This is described in more detail
        in the “Extended Instruction Syntax” section.

        Figure 9-6. Comparing Addressing Options for Bit-Oriented and Byte-Oriented Instructions (Extended Instruction
        Set Enabled)
                        EXAMPLE INSTRUCTION: ADDWF, f, d, a (Opcode: 0010 01da ffff ffff)
                                                                    0000h
                           When ‘a’ = 0 and f ≥ 60h                          Bank 0 - 3

                            The instruction executes in             0400h
                          Direct Forced mode. ‘f’ is inter-                     Bank 4            00h
                            preted as a location in the             0460h
                           Access RAM between 060h                              Access            60h
                                                                                 SFRs
                          and 0FFh. This is the same as             04FFh
                              locations 460h to 4FFh
                             (Bank4) of data memory.                                              FFh
                           Locations below 60h are not                       Bank 5-63
                                                                                                         Access RAM
                            available in this Addressing
                                       mode.
                                                                   3FFFh
                                                                            Data Memory


                            When ‘a’ = 0 and f ≤ 5 Fh               0000h
                                                                             Bank 0 - 3
                            The instruction executes in
                          Indexed Literal Offset mode. ‘f’          0400h
                         is interpreted as an offset to the                     Bank 4
                            address value in FSR2. The              0460h
                             two are added together to                          Access
                                                                   04FFh         SFRs
                         obtain the address of the target
                                                                   0500h        Access
                          register for the instruction. The
                                                                                 GPR
                           address can be anywhere in               0560h
                              the data memory space.                         Bank 5-63           0010 01da       ffff ffff

                                                                                                    +
                           Note that in this mode, the
                             correct syntax is now:
                                                                                                   FSR2H          FSR2L
                                                                   3FFFh
                               ADDWF [k], d                                 Data Memory
                           where ‘k’ is the same as ‘f’.


                                                                    0000h
                            When ‘a’ = 1 (all values of f)                   Bank 0 - 3
                                                                    0400h
                            The instruction executes in
                            Direct mode (also known as                          Bank 4
                           Direct Long mode). ‘f’ is inter-         0460h
                                                                                Access
                           preted as a location in one of
                                                                    04FFh        SFRs
                              the 63 banks of the data                                                     BSR
                            memory space. The bank is                                                   0000 1010
                               designated by the Bank                                        Bank 10
                            Select Register (BSR). The                       Bank 5-63
                                address can be in any                                            0010 01da    ffff ffff
                           implemented bank in the data            3FFFh
                                   memory space.                            Data Memory


9.6.3   Mapping the Access Bank in Indexed Literal Offset Mode
        The use of Indexed Literal Offset Addressing mode effectively changes how the first 96 locations of
        Access RAM (00h to 5Fh) are mapped. Rather than containing just the contents of the top section of
        Bank 5, this mode maps the contents from a user defined “window” that can be located anywhere in
        the data memory space. The value of FSR2 establishes the lower boundary of the addresses mapped
        into the window, while the upper boundary is defined by FSR2 plus 95 (5Fh). Addresses in the Access
        RAM above 5Fh are mapped as previously described (see the Access Bank section). An example of
        Access Bank remapping in this Addressing mode is shown in the following figure.


--- p77 ---
                                                                                                   PIC18F27/47/57Q43
                                                                                                  Memory Organization

        Figure 9-7. Remapping the Access Bank with Indexed Literal Offset Addressing


                                                      0000h
                                                                   Bank 0 - 3
              EXAMPLE:
              ADDWF, f, d, a                          0400h

              FSR2H:FSR2L = 0x0A20                                   Bank 4
                                                      0460h
               Locations in the region                               Access
                                                                      SFRs
               from the FSR2 pointer                                                                       00h
                                                       0500h
             (A20h) to the pointer plus                                                   Bank 10 Window
                                                                    Bank 5-9                                60h
             05Fh (A7Fh) are mapped
                 to the Access RAM                                                            SFRs
                                                                    Bank 10
                     (000h-05Fh).                    0A20h
                                                                    Window                                  FFh
              Special File Registers at                                                   Access RAM
                                                     0A7Fh
               460h through 4FFh are                                Bank 10
              mapped to 60h through
                    FFh, as usual.
              Bank 4 addresses below                              Bank 11 - 63
             5Fh can still be addressed
                  by using the BSR.
                                                      3FFFh
                                                                  Data Memory


        Remapping of the Access Bank applies only to operations using the Indexed Literal Offset mode.
        Operations that use the BSR (Access RAM bit is ‘1’) will continue to use Direct Addressing as before.

9.6.4   PIC18 Instruction Execution and the Extended Instruction Set
        Enabling the extended instruction set adds additional commands to the existing PIC18 instruction
        set. These instructions are executed as described in the “Extended Instruction Set” section.

9.7     Register Definitions: Memory Organization


--- p78 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                                     Memory Organization

9.7.1         PCL

              Name:       PCL
              Address:    0x4F9

              Low byte of the Program Counter Register

        Bit          7            6        5              4                   3            2    1              0
                                                                PCL[7:0]
  Access            R/W       R/W         R/W            R/W                 R/W      R/W      R/W            R/W
   Reset             0         0           0              0                   0        0        0              0

Bits 7:0 – PCL[7:0] Provides direct read and write access to the Program Counter


--- p79 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                         Memory Organization

9.7.2         PCLAT

              Name:       PCLAT
              Address:    0x4FA
              Program Counter Latches
              Holding register for bits [21:9] of the Program Counter (PC). Reads of the PCL register transfer the
              upper PC bits to the PCLAT register. Writes to PCL register transfer the PCLAT value to the PC.

        Bit        15           14           13            12                  11        10         9              8
                                                                                     PCLATU[4:0]
  Access                                                  R/W                  R/W      R/W        R/W            R/W
   Reset                                                   0                    0         0         0              0

        Bit        7              6          5              4            3                   2      1              0
                                                             PCLATH[7:0]
  Access          R/W          R/W          R/W           R/W          R/W              R/W        R/W            R/W
   Reset           0            0            0             0             0               0          0              0

Bits 12:8 – PCLATU[4:0] Upper PC Latch Register
         Holding register for Program Counter [21:17]

Bits 7:0 – PCLATH[7:0] High PC Latch Register
          Holding register for Program Counter [16:8]


--- p80 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                                        Memory Organization

9.7.3         TOS

              Name:       TOS
              Address:    0x4FD
              Top-of-Stack Register
              Contents of the stack pointed to by the STKPTR register. This is the value that will be loaded into the
              Program Counter upon a RETURN or RETFIE instruction.

        Bit         23          22           21            20                  19       18        17              16
                                                                                     TOS[20:16]
  Access                                                  R/W                  R/W     R/W        R/W            R/W
   Reset                                                   0                    0        0         0              0

        Bit         15          14           13            12                  11        10        9              8
                                                                 TOS[15:8]
  Access            R/W        R/W          R/W           R/W                  R/W      R/W       R/W            R/W
   Reset             0          0            0             0                    0        0         0              0

        Bit          7          6            5              4                   3            2     1              0
                                                                  TOS[7:0]
  Access            R/W        R/W          R/W           R/W                  R/W      R/W       R/W            R/W
   Reset             0          0            0             0                    0        0         0              0

Bits 20:0 – TOS[20:0] Top-of-Stack

              Notes: The individual bytes in this multibyte register can be accessed with the following register
              names:
              • TOSU: Accesses the upper byte TOS[20:16]
              •   TOSH: Accesses the high byte TOS[15:8]
              •   TOSL: Accesses the low byte TOS[7:0]


--- p81 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                                 Memory Organization

9.7.4         STKPTR

              Name:       STKPTR
              Address:    0x4FC

              Stack Pointer Register

        Bit        7            6       5             4               3                2    1              0
                                                                  STKPTR[6:0]
  Access                       R/W     R/W          R/W              R/W          R/W      R/W            R/W
   Reset                        0       0            0                0            0        0              0

Bits 6:0 – STKPTR[6:0] Stack Pointer Location


--- p82 ---
                                                                                                 PIC18F27/47/57Q43
                                                                                                Memory Organization

9.7.5         WREG

              Name:      WREG
              Address:   0x4E8

              Working Data Register

        Bit        7             6     5             4          3                     2    1              0
                                                      WREG[7:0]
  Access          R/W         R/W     R/W          R/W         R/W               R/W      R/W            R/W
   Reset           x           x       x            x           x                 x        x              x

Bits 7:0 – WREG[7:0]


--- p83 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                                        Memory Organization

9.7.6         INDF

              Name:       INDFx
              Address:    0x4EF,0x4E7,0x4DF
              Indirect Data Register
              This is a virtual register. The GPR/SFR register addressed by the FSRx register is the target for all
              operations involving the INDFx register.

        Bit          7           6            5              4                   3            2    1              0
                                                                  INDF[7:0]
  Access          R/W           R/W          R/W           R/W                  R/W      R/W      R/W            R/W
   Reset           0             0            0             0                    0        0        0              0

Bits 7:0 – INDF[7:0] Indirect data pointed to by the FSRx register


--- p84 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                                       Memory Organization

9.7.7         POSTDEC

              Name:       POSTDECx
              Address:    0x4ED,0x4E5,0x4DD
              Indirect Data Register with post decrement
              This is a virtual register. The GPR/SFR register addressed by the FSRx register is the target for all
              operations involving the POSTDECx register. FSRx is decrememted after the read or write operation.

        Bit        7            6            5             4           3                     2    1              0
                                                            POSTDEC[7:0]
  Access          R/W          R/W         R/W            R/W         R/W               R/W      R/W            R/W
   Reset           0            0           0              0           0                 0        0              0

Bits 7:0 – POSTDEC[7:0]


--- p85 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                                       Memory Organization

9.7.8         POSTINC

              Name:       POSTINCx
              Address:    0x4EE,0x4E6,0x4DE
              Indirect Data Register with post increment
              This is a virtual register. The GPR/SFR register addressed by the FSRx register is the target for all
              operations involving the POSTINCx register. FSRx is incremented after the read or write operation.

        Bit        7            6            5             4            3                    2    1              0
                                                            POSTINC[7:0]
  Access          R/W          R/W          R/W           R/W         R/W               R/W      R/W            R/W
   Reset           0            0            0             0            0                0        0              0

Bits 7:0 – POSTINC[7:0]


--- p86 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                                        Memory Organization

9.7.9         PREINC

              Name:       PREINCx
              Address:    0x4EC,0x4E4,0x4DC
              Indirect Data Register with pre-increment
              This is a virtual register. The GPR/SFR register addressed by the FSRx register plus 1 is the target
              for all operations involving the PREINCx register. FSRx is incremented before the read or write
              operation.

        Bit        7             6            5              4            3                   2    1              0
                                                              PREINC[7:0]
  Access          R/W          R/W          R/W            R/W          R/W              R/W      R/W            R/W
   Reset           0            0            0              0             0               0        0              0

Bits 7:0 – PREINC[7:0]


--- p87 ---
                                                                                                     PIC18F27/47/57Q43
                                                                                                    Memory Organization

9.7.10 PLUSW

           Name:       PLUSWx
           Address:    0x4EB,0x4E3,0x4DB
           Indirect Data Register with WREG offset
           This is a virtual register. The GPR/SFR register addressed by the sum of the FSRx register plus the
           signed value of the W register is the target for all operations involving the PLUSWx register.

     Bit        7            6            5              4           3                    2    1              0
                                                          PLUSW[7:0]
  Access       R/W          R/W          R/W           R/W         R/W               R/W      R/W            R/W
   Reset        0            0            0             0            0                0        0              0

Bits 7:0 – PLUSW[7:0]


--- p88 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                                           Memory Organization

9.7.11 FSR

            Name:       FSRx
            Address:    0x4E9,0x4E1,0x4D9
            Indirect Address Register
            The FSR value is the address of the data to which the INDF register points.

      Bit        15           14          13             12                  11                10     9              8
                                                                                   FSRH[5:0]
  Access                                  R/W           R/W                  R/W               R/W   R/W            R/W
   Reset                                   0             0                    0                 0     0              0

      Bit        7            6            5              4                   3                 2     1              0
                                                               FSRL[7:0]
  Access        R/W          R/W          R/W           R/W                  R/W               R/W   R/W            R/W
   Reset         0            0            0             0                    0                 0     0              0

Bits 13:8 – FSRH[5:0] Most Significant address of INDF data

Bits 7:0 – FSRL[7:0] Least Significant address of INDF data


--- p89 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                                       Memory Organization

9.7.12 BSR

            Name:      BSR
            Address:   0x4E0
            Bank Select Register
            The BSR indicates the data memory bank of the GPR address.

      Bit        7             6         5             4                   3                2     1              0
                                                                                BSR[5:0]
  Access                               R/W           R/W                  R/W              R/W   R/W            R/W
   Reset                                0             0                    0                0     0              0

Bits 5:0 – BSR[5:0] Most Significant bits of the data memory address


--- p90 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                             Memory Organization

9.8       Register Summary - Memory Organization
Address     Name      Bit Pos.   7        6           5             4                 3               2       1          0
                       7:0                                               FSRL[7:0]
 0x04D9      FSR2
                       15:8                                                               FSRH[5:0]
0x04DB      PLUSW2     7:0                                              PLUSW[7:0]
0x04DC      PREINC2    7:0                                           PREINC[7:0]
0x04DD     POSTDEC2    7:0                                          POSTDEC[7:0]
0x04DE     POSTINC2    7:0                                          POSTINC[7:0]
0x04DF       INDF2     7:0                                            INDF[7:0]
0x04E0        BSR      7:0                                                                BSR[5:0]
                       7:0                                               FSRL[7:0]
 0x04E1      FSR1
                       15:8                                                               FSRH[5:0]
 0x04E3     PLUSW1     7:0                                           PLUSW[7:0]
 0x04E4     PREINC1    7:0                                           PREINC[7:0]
 0x04E5    POSTDEC1    7:0                                          POSTDEC[7:0]
 0x04E6    POSTINC1    7:0                                          POSTINC[7:0]
 0x04E7      INDF1     7:0                                            INDF[7:0]
 0x04E8      WREG      7:0                                            WREG[7:0]
                       7:0                                            FSRL[7:0]
 0x04E9      FSR0
                       15:8                                                               FSRH[5:0]
 0x04EB     PLUSW0     7:0                                           PLUSW[7:0]
 0x04EC     PREINC0    7:0                                           PREINC[7:0]
 0x04ED    POSTDEC0    7:0                                          POSTDEC[7:0]
 0x04EE    POSTINC0    7:0                                          POSTINC[7:0]
 0x04EF      INDF0     7:0                                            INDF[7:0]
 0x04F0
   ...     Reserved
 0x04F8
 0x04F9      PCL        7:0                                               PCL[7:0]
                        7:0                                             PCLATH[7:0]
 0x04FA     PCLAT
                       15:8                                                                    PCLATU[4:0]
 0x04FC     STKPTR      7:0                                                    STKPTR[6:0]
                        7:0                                               TOS[7:0]
 0x04FD      TOS       15:8                                              TOS[15:8]
                       23:16                                                                    TOS[20:16]


--- p91 ---
