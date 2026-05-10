                      PIC18(L)F26/27/45/46/47/55/56/57K42
3.0      PIC18 CPU
This family of devices contains a PIC18 8-bit CPU core
based on the modified Harvard architecture. The PIC18
CPU supports:
• System Arbitration, which decides memory
  access allocation depending on user priorities
• Vectored Interrupt capability with automatic two
  level deep context saving
• 31-level deep hardware stack with overflow and
  underflow reset capabilities
• Support Direct, Indirect, and Relative Addressing
  modes
• 8x8 Hardware Multiplier


 2017-2021 Microchip Technology Inc.                    DS40001919G-page 26
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 3-1:                 PIC18(L)F26/27/45/46/47/55/56/57K42 FAMILY BLOCK DIAGRAM

                                                           Data Bus[8]
                    Table Pointer[21]

                                                                  8        8                     Data Latch
                      inc/dec logic
                                                                                                 Data Memory
                           21                  PCLATU PCLATH
                                       20                                                       Address Latch                       Ports
                                                      PCU PCH PCL
                                                      Program Counter                                   12
                                                                                              Data Address[12]
                                                       31-Level Stack
                    Address Latch                                                         6            14       4
                                                                                        BSR      FSR0       Access
                    Program Memory                          STKPTR                                           Bank
                   (8/16/32/64 Kbytes)                                                           FSR1
                                                                                                 FSR2            12               Peripherals
                      Data Latch

                                                                                                 inc/dec
                                         8                                                        logic
                                                Table Latch


                                                ROM Latch                                       Address
                  Instruction Bus [16]                                                          Decode
                                                                                                                                     Data
                                                      IR                                                                           EEPROM


                                                                                                                      8
                                                Instruction           State machine
                                               Decode and             control signals
                                                  Control
                                                                                                  PRODH PRODL

                                                                                                       8x8 Multiply
                                                                                           3                                  8

                                                                                        BITOP           W
                                                                                            8               8             8

                 OSC1(2)                  Internal
                                         Oscillator               Power-up
                                                                   Timer                           8                      8
                                           Block
                 OSC2(2)                                          Oscillator                       ALU[8]
                                       LFINTOSC                 Start-up Timer
                  SOSCI                 Oscillator                Power-on                                  8
                                                                    Reset
                                         64 MHz
                 SOSCO                   Oscillator                   WWDT
                                                                                         Precision
                                      Single-Supply              Brown-out               Band Gap
                 MCLR(1)                                           Reset
                                      Programming                                        Reference
                                        In-Circuit                Fail-Safe
                                        Debugger                Clock Monitor


   Note   1:   RE3 is only available when MCLR functionality is disabled.
          2:   OSC1/CLKIN and OSC2/CLKOUT are only available in select oscillator modes and when these pins are not being used as digital I/O.
               Refer to Section 7.0, Oscillator Module (with Fail-Safe Clock Monitor) for additional information.


 2017-2021 Microchip Technology Inc.                                                                                               DS40001919G-page 27
                          PIC18(L)F26/27/45/46/47/55/56/57K42
3.1        System Arbitration
The System Arbiter resolves memory access between
the System Level Selections (i.e., Main, Interrupt
Service Routine) and Peripheral Selection (i.e., DMA
and Scanner) based on user-assigned priorities. Each
of the system level and peripheral selections has its
own priority selection registers. Memory access priority
is resolved using the number written to the
corresponding Priority registers, 0 being the highest
priority and 4 the lowest. The default priorities are listed
in Table 3-1.
In case the user wants to change priorities, ensure
each Priority register is written with a unique value from
0 to 4.


TABLE 3-1:           DEFAULT PRIORITIES
                                           Priority register
                 Selection
                                             Reset value
System Level                 ISR                  0
                             MAIN                 1
Peripheral                   DMA1                 2
                             DMA2                 3
                        SCANNER                   4


FIGURE 3-2:                SIMPLIFIED BLOCK DIAGRAM OF ON-CHIP RESET CIRCUIT
                                                                                                        Rev. 20-000318A
                                                                                                               11/2/2016


                                        Memory Access
                          CPU                                  Scanner          DMA 1        DMA 2
                                          NVMCON


      Priority                                                 System Arbiter


                                     Program Flash                                SFR/GPR
                                                           Data EEPROM
                                        Memory                                   SRAM Data


      Legend
                    Program Flash Memory Data
                    Data EEPROM Data
                    SFR/GPR Data


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 28
                      PIC18(L)F26/27/45/46/47/55/56/57K42
3.1.1       PRIORITY LOCK                                   3.2          Memory Access Scheme
The System arbiter grants memory access to the              The user can assign priorities to both system level and
peripheral selections (DMAx, Scanner) when the              peripheral selections based on which the system
PRLOCKED bit (PRLOCK Register) is set.                      arbiter grants memory access. Let us consider the
Priority selections are locked by setting the               following priority scenarios between ISR, MAIN, and
PRLOCKED bit of the PRLOCK register. Setting and            Peripherals.
clearing this bit requires a special sequence as an extra
precaution against inadvertent changes. Examples of
setting and clearing the PRLOCKED bit are shown in               Note:    It is always required that the ISR priority
Example 3-1 and Example 3-2.                                              be higher than Main priority.

EXAMPLE 3-1:           PRIORITY LOCK                        3.2.1         ISR PRIORITY > MAIN PRIORITY >
                       SEQUENCE                                           PERIPHERAL PRIORITY
; Disable interrupts                                        When the Peripheral Priority (DMAx, Scanner) is lower
BCF INTCON0,GIE                                             than ISR and MAIN Priority, and the peripheral
                                                            requires:
; Bank to PRLOCK register                                   1.    Access to the Program Flash Memory, then the
BANKSEL PRLOCK                                                    peripheral waits for an instruction cycle in which
MOVLW 55h                                                         the CPU does not need to access the PFM
                                                                  (such as a branch instruction) and uses that
; Required sequence, next 4                                       cycle to do its own Program Flash Memory
instructions                                                      access, unless a PFM Read/Write operation is
MOVWF PRLOCK                                                      in progress.
MOVLW AAh
                                                            2.    Access to the SFR/GPR, then the peripheral
MOVWF PRLOCK
                                                                  waits for an instruction cycle in which the CPU
; Set PRLOCKED bit to grant memory
                                                                  does not need to access the SFR/GPR (such as
access to peripherals
                                                                  MOVLW, CALL, NOP) and uses that cycle to do its
BSF PRLOCK,0
                                                                  own SFR/GPR access.
; Enable Interrupts                                         3.    Access to the Data EEPROM, then the
BSF INTCON0,GIE                                                   peripheral has access to Data EEPROM unless
                                                                  a Data EEPROM Read/Write operation is being
                                                                  performed.
EXAMPLE 3-2:           PRIORITY UNLOCK                      This results in the lowest throughput for the peripheral
                       SEQUENCE                             to access the memory, and does so without any impact
; Disable interrupts                                        on execution times.
BCF INTCON0,GIE
                                                            3.2.2         PERIPHERAL PRIORITY > ISR
; Bank to PRLOCK register                                                 PRIORITY > MAIN PRIORITY
BANKSEL PRLOCK
                                                            When the Peripheral Priority (DMAx, Scanner) is higher
MOVLW 55h
                                                            than ISR and MAIN Priority, the CPU operation is
                                                            stalled when the peripheral requests memory.
; Required sequence, next 4
instructions                                                The CPU is held in its current state until the peripheral
MOVWF PRLOCK                                                completes its operation. Since the peripheral requests
MOVLW AAh                                                   access to the bus, the peripheral cannot be disabled
MOVWF PRLOCK                                                until it completes its operation.
; Clear PRLOCKED bit to allow changing                      This results in the highest throughput for the peripheral
priority settings                                           to access the memory, but has the cost of stalling other
BCF PRLOCK,0                                                execution while it occurs.

; Enable Interrupts
BSF INTCON0,GIE


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 29
                        PIC18(L)F26/27/45/46/47/55/56/57K42
3.2.3           ISR PRIORITY > PERIPHERAL                         3.2.4       PERIPHERAL 1 PRIORITY > ISR
                PRIORITY > MAIN PRIORITY                                      PRIORITY > MAIN PRIORITY >
In this case, interrupt routines and peripheral operation                     PERIPHERAL 2 PRIORITY
(DMAx, Scanner) will stall the CPU. Interrupt will                In this case, the Peripheral 1 will stall the execution of
preempt peripheral operation. This results in lowest              the CPU. However, Peripheral 2 can access the
interrupt latency and highest throughput for the                  memory in cycles unused by Peripheral 1.
peripheral to access the memory.
                                                                  The operation of the System Arbiter is controlled
                                                                  through the following registers:

REGISTER 3-1:            ISRPR: INTERRUPT SERVICE ROUTINE PRIORITY REGISTER
        U-0            U-0              U-0           U-0          U-0             R/W-0/0      R/W-0/0        R/W-0/0
         —              —               —             —             —                         ISRPR[2:0]
        bit 7                                                                                                     bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
1 = bit is set                   0 = bit is cleared            HS = Hardware set


bit 7-3            Unimplemented: Read as ‘0’
bit 2-0            ISRPR[2:0]: Interrupt Service Routine Priority Selection bits

REGISTER 3-2:            MAINPR: MAIN ROUTINE PRIORITY REGISTER
        U-0            U-0              U-0           U-0          U-0             R/W-0/0      R/W-0/0        R/W-1/1
         —              —               —             —             —                        MAINPR[2:0]
        bit 7                                                                                                     bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
1 = bit is set                   0 = bit is cleared            HS = Hardware set


bit 7-3            Unimplemented: Read as ‘0’
bit 2-0            MAINPR[2:0]: Main Routine Priority Selection bits

REGISTER 3-3:            DMA1PR: DMA1 PRIORITY REGISTER
        U-0            U-0              U-0           U-0          U-0             R/W-0/0      R/W-1/1        R/W-0/0
         —              —               —             —             —                        DMA1PR[2:0]
        bit 7                                                                                                     bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
1 = bit is set                   0 = bit is cleared            HS = Hardware set


bit 7-3            Unimplemented: Read as ‘0’
bit 2-0            DMA1PR[2:0]: DMA1 Priority Selection bits


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 30
                       PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 3-4:           DMA2PR: DMA2 PRIORITY REGISTER
        U-0            U-0              U-0          U-0         U-0          R/W-0/0        R/W-1/1        R/W-1/1
         —             —                —            —            —                       DMA2PR[2:0]
        bit 7                                                                                                 bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
1 = bit is set                  0 = bit is cleared           HS = Hardware set


bit 7-3           Unimplemented: Read as ‘0’
bit 2-0           DMA2PR[2:0]: DMA2 Priority Selection bits

REGISTER 3-5:           SCANPR: SCANNER PRIORITY REGISTER
        U-0            U-0              U-0          U-0         U-0          R/W-1/1        R/W-0/0        R/W-0/0
         —             —                —            —            —                       SCANPR[2:0]
        bit 7                                                                                                 bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
1 = bit is set                  0 = bit is cleared           HS = Hardware set


bit 7-3           Unimplemented: Read as ‘0’
bit 2-0           SCANPR[2:0]: Scanner Priority Selection bits

REGISTER 3-6:           PRLOCK: PRIORITY LOCK REGISTER
        U-0            U-0              U-0          U-0         U-0            U-0             U-0         R/W-0/0
         —             —                —            —            —              —              —         PRLOCKED
        bit 7                                                                                                 bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
1 = bit is set                  0 = bit is cleared           HS = Hardware set


bit 7-1           Unimplemented: Read as ‘0’
bit 0             PRLOCKED: PR Register Lock bit(1, 2)
                  0 = Priority Registers can be modified by write operations; Peripherals do not have access to the
                  memory
                  1 = Priority Registers are locked and cannot be written; Peripherals have access to the memory
   Note 1: The PRLOCKED bit can only be set or cleared after the unlock sequence.
           2: If PR1WAY = 1, the PRLOCKED bit cannot be cleared after it has been set. A device Reset will clear the
              bit and allow one more set.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 31
                          PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 3-2:          SUMMARY OF REGISTERS ASSOCIATED WITH CPU
                                                                                                      Register on
    Name          Bit 7         Bit 6       Bit 5      Bit 4   Bit 3    Bit 2     Bit 1      Bit 0
                                                                                                         page

ISRPR               —            —           —          —       —      ISRPR2    ISRPR1     ISRPR0        30
MAINPR              —            —           —          —       —      MAINPR2   MAINPR1   MAINPR0        30
DMA1PR              —            —           —          —       —      DMA1PR2   DMA1PR1   DMA1PR0        30
DMA2PR              —            —           —          —       —      DMA2PR2   DMA2PR1   DMA2PR0        31
SCANPR              —            —           —          —       —      SCANPR2   SCANPR1   SCANPR0        31
PRLOCK              —            —           —          —       —        —         —       PRLOCKED       31
Legend:     — = Unimplemented location, read as ‘0’.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 32
