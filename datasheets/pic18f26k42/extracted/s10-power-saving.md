                      PIC18(L)F26/27/45/46/47/55/56/57K42
10.0       POWER-SAVING OPERATION                             10.1.2      INTERRUPTS DURING DOZE
           MODES                                              When an interrupt occurs during Doze, the system
                                                              behavior can be configured using the Recover-On-
The purpose of the Power Down modes is to reduce              Interrupt bit (ROI) and the Doze-On-Exit bit (DOE).
power consumption. There are three Power Down                 Refer to Table 10-2 for details about system behavior in
modes:                                                        all the cases for a transition from Main > ISR > Main.
• Doze mode                                                   For PIC18(L)F26/27/45/46/47/55/56/57 devices, the
• Sleep mode                                                  transition from Main > ISR > Main always happens in
• Idle mode                                                   Normal operation, regardless of the state of the
                                                              DOZEN or DOE bits.
10.1       Doze Mode
Doze mode saves power by reducing CPU execution
and program memory (PFM) access, without affecting
peripheral operation.

10.1.1      DOZE OPERATION
When the Doze Enable bit is set (DOZEN = 1), the CPU
executes one instruction cycle out of every N cycles as
defined by the DOZE[2:0] bits of the CPUDOZE
register. FOSC and FOSC/4 clock sources are
unaffected in Doze mode and peripherals can continue
using these sources.

TABLE 10-1:       SYSTEM BEHAVIOR FOR INTERRUPT DURING DOZE
                                                                Code Flow
  DOZEN         ROI
                                   Main                    ISR (1)                       Return to Main

       0          0          Normal operation        Normal operation and
                                                    DOE = DOZEN (in hard-
                                                      ware) DOZEN = 0
                                                        (unchanged)
       0          1          Normal operation        Normal operation and
                                                                              If DOE = 1 when If DOE = 0 when
                                                    DOE = DOZEN (in hard-
                                                                               return from inter- return from inter-
                                                     ware) DOZEN = 0 (in
                                                                              rupt; Doze opera- rupt; Normal oper-
                                                          hardware)
                                                                             tion and DOZEN = ation and DOZEN
       1          0           Doze operation       Doze operation and DOE       1 (in hardware)   = 0 (in hardware)
                                                   = DOZEN (in hardware)
                                                   DOZEN = 1 (unchanged)
       1          1           Doze operation         Normal operation and
                                                    DOE = DOZEN (in hard-
                                                     ware) DOZEN = 0 (in
                                                          hardware)
Note 1:     User software can change the DOE bit in ISR.
For example, if ROI = 1 and DOZE[2:0] = 001, the
instruction cycle ratio is 1:4. The CPU and memory
operate for one instruction cycle and stay idle for the
next three instruction cycles. The Doze operation is
illustrated in Figure 10-1.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 170
                      PIC18(L)F26/27/45/46/47/55/56/57K42
EXAMPLE 10-1:          DOZE SOFTWARE
                       EXAMPLE

//Mainline operation
bool somethingToDo = FALSE:
void main()
{
    initializeSystem();
            // DOZE = 64:1 (for example)
            // ROI = 1;
    GIE = 1; // enable interrupts
    while (1)
    {
        // If ADC completed, process data
        if (somethingToDo)
        {
            doSomething();
            DOZEN = 1; // resume low-power
        }
    }
}

// Data interrupt handler
void interrupt()
{
    // DOZEN = 0 because ROI = 1
    if (ADIF)
    {
        somethingToDo = TRUE;
        DOE = 0; // make main() go fast
        ADIF = 0;
    }
    // else check other interrupts...
    if (TMR0IF)
    {
        timerTick++;
        DOE = 1; // make main() go slow
        TMR0IF = 0;
    }
}


 2017-2021 Microchip Technology Inc.           DS40001919G-page 171
                          PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 10-1:               DOZE MODE OPERATION EXAMPLE (DOZE[2:0] = 001, 1:4)


     FOSC


     CPU Clocks         1 2 3 4
                                    DOZE = 3’b001 (1:4)   1 2 3 4                   1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4


     Program Counter                                                                             Interrupt
                          PC-2                              PC                      PC+2                      ISR    ISR+2
                                                                                                 Vectoring


     CPU Operation
                          Exec                             Exec                      Exec      FNOP    FNOP   FNOP   Exec     Exec
                                                                                    (Note 1)
                                                                                    (Note 2)
                                                                       Interrupt
                                                                         Here
                                                                      (ROI = ‘1’)
      Note 1: Multi-cycle instructions are executed to completion before fetching the interrupt vector.
           2: If the prefetched instruction clears the interrupt enable or GIEx, ISR vectoring will not occur, but DOZEN is
              cleared and the CPU will resume execution at full speed.


10.2        Sleep Mode                                                    I/O pins that are high-impedance inputs may be pulled
                                                                          to VDD or VSS externally to avoid switching currents
Sleep mode is entered by executing the SLEEP                              caused by floating inputs.
instruction, while the Idle Enable (IDLEN) bit of the
CPUDOZE register is clear (IDLEN = 0).                                    Examples of internal circuitry that might be sourcing
                                                                          current include modules such as the DAC and FVR
Upon entering Sleep mode, the following conditions                        modules. See Section 37.0 “5-Bit Digital-to-Analog
exist:                                                                    Converter (DAC) Module” and Section 34.0 “Fixed
1.     WDT will be cleared but keeps running if                           Voltage Reference (FVR)” for more information on
       enabled for operation during Sleep                                 these modules.
2.     The PD bit of the STATUS register is cleared
       (Register 4-2)
3.     The TO bit of the STATUS register is set
       (Register 4-2)
4.     The CPU clock is disabled
5.     LFINTOSC, SOSC, HFINTOSC and ADCRC
       are unaffected and peripherals using them may
       continue operation in Sleep
6.     I/O ports maintain the status they had before
       Sleep was executed (driving high, low, or high-
       impedance)
7.     Resets other than WDT are not affected by
       Sleep mode
Refer to individual chapters for more details on
peripheral operation during Sleep.
To minimize current consumption, the following
conditions may be considered:
     - I/O pins may not be floating
     - External circuitry sinking current from I/O pins
     - Internal circuitry sourcing current from I/O
       pins
     - Current draw from pins with internal weak
       pull-ups
     - Modules using any oscillator


 2017-2021 Microchip Technology Inc.                                                                          DS40001919G-page 172
                       PIC18(L)F26/27/45/46/47/55/56/57K42
10.2.1      WAKE-UP FROM SLEEP                               10.2.2       WAKE-UP USING INTERRUPTS
The device can wake up from Sleep through one of the         When any interrupt source, with the exception of the
following events:                                            clock switch interrupt, has both its interrupt enable bit
1.   External Reset input on MCLR pin, if enabled            and interrupt flag bit set, one of the following will occur:
2.   BOR Reset, if enabled                                   • If the interrupt occurs before the execution of a
3.   Low-Power Brown-Out Reset (LPBOR), if                     SLEEP instruction
     enabled                                                   - SLEEP instruction will execute as a NOP
4.   POR Reset                                                 - WDT and WDT prescaler will not be cleared
5.   Windowed Watchdog Timer, if enabled                       - TO bit of the STATUS register will not be set
6.   All interrupt sources except clock switch                 - PD bit of the STATUS register will not be
     interrupt can wake up the part.                               cleared
The first five events will cause a device Reset. The last    • If the interrupt occurs during or after the
one event is considered a continuation of program              execution of a SLEEP instruction
execution. To determine whether a device Reset or              - SLEEP instruction will be completely
wake-up event occurred, refer to Section 6.13 “Power               executed
Control (PCON0/PCON1) Register”.                               - Device will immediately wake up from Sleep
When the SLEEP instruction is being executed, the next         - WDT and WDT prescaler will be cleared
instruction (PC + 2) is prefetched. For the device to          - TO bit of the STATUS register will be set
wake up through an interrupt event, the corresponding          - PD bit of the STATUS register will be cleared
Interrupt Enable bit must be enabled. Wake-up will
                                                             Even if the flag bits were checked before executing a
occur regardless of the state of the GIE bit. If the GIE
                                                             SLEEP instruction, it may be possible for flag bits to
bit is disabled, the device continues execution at the
                                                             become set before the SLEEP instruction completes. To
instruction after the SLEEP instruction. If the GIE bit is
                                                             determine whether a SLEEP instruction executed, test
enabled, the device executes the instruction after the
                                                             the PD bit. If the PD bit is set, the SLEEP instruction
SLEEP instruction, the device will then call the Interrupt
                                                             was executed as a NOP.
Service Routine. In cases where the execution of the
instruction following SLEEP is not desirable, the user
may have a NOP after the SLEEP instruction.
The WDT is cleared when the device wakes-up from
Sleep, regardless of the source of wake-up.
Upon a wake from a Sleep event, the core will wait for
a combination of three conditions before beginning
execution. The conditions are:
• PFM Ready
• COSC-Selected Oscillator Ready
• BOR Ready (unless BOR is disabled)


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 173
                                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 10-2:                    WAKE-UP FROM SLEEP THROUGH INTERRUPT

                    Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1                                    Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4
         CLKIN(1)
    CLKOUT(2)                                                           TOST(3)


  Interrupt flag                                                                   Interrupt Latency (4)

   GIE bit
  (INTCON reg.)                                          Processor in
                                                            Sleep

Instruction Flow
            PC             PC              PC + 1                 PC + 2               PC + 2              PC + 2         0004h            0005h
   Instruction                            Inst(PC + 1)                             Inst(PC + 2)                        Inst(0004h)       Inst(0005h)
   Fetched          Inst(PC) = Sleep
   Instruction                            Sleep                                    Inst(PC + 1)      Forced NOP       Forced NOP
   Executed            Inst(PC - 1)                                                                                                       Inst(0004h)


  Note     1:      External clock. High, Medium, Low mode assumed.
           2:      CLKOUT is shown here for timing reference.
           3:      TOST = 1024 TOSC. This delay does not apply to EC and INTOSC Oscillator modes.
           4:      GIE = 1 assumed. In this case after wake-up, the processor calls the ISR at 0004h. If GIE = 0, execution will continue in-line.


10.2.3           LOW POWER SLEEP MODE                                                10.2.3.1              Sleep Current vs. Wake-up Time
The PIC18F26/27/45/46/47/55/56/57K42 device family                                   In the default operating mode, the LDO and reference
contains an internal Low Dropout (LDO) voltage                                       circuitry remain in the normal configuration while in
regulator, which allows the device I/O pins to operate at                            Sleep. The device is able to exit Sleep mode quickly
voltages up to 5.5V while the internal device logic                                  since all circuits remain active. In Low Power Sleep
operates at a lower voltage. The LDO and its                                         mode, when waking-up from Sleep, an extra delay time
associated reference circuitry must remain active when                               is required for these circuits to return to the normal
the device is in Sleep mode.                                                         configuration and stabilize.
The PIC18F26/27/45/46/47/55/56/57K42 devices allow                                   The Low-Power Sleep mode is beneficial for
the user to optimize the operating current in Sleep,                                 applications that stay in Sleep mode for long periods of
depending on the application requirements.                                           time. The Normal mode is beneficial for applications
                                                                                     that need to wake from Sleep quickly and frequently.
Low Power Sleep mode can be selected by setting the
VREGPM bit of the VREGCON register.


     2017-2021 Microchip Technology Inc.                                                                                            DS40001919G-page 174
                       PIC18(L)F26/27/45/46/47/55/56/57K42
10.2.3.2      Peripheral Usage in Sleep                      10.2.4.1      Idle and Interrupts
Some peripherals that can operate in Sleep mode will         Idle mode ends when an interrupt occurs (even if GIE
not operate properly with the Low-Power Sleep mode           = 0), but IDLEN is not changed. The device can re-
selected. The Low-Power Sleep mode is intended for           enter Idle by executing the SLEEP instruction.
use with these peripherals:                                  If Recover-On-Interrupt is enabled (ROI = 1), the
• Brown-out Reset (BOR)                                      interrupt that brings the device out of Idle also restores
• Windowed Watchdog Timer (WWDT)                             full-speed CPU execution when Doze is also enabled.
• External interrupt pin/Interrupt-On-Change pins
• Peripherals that run off external secondary clock          10.2.4.2      Idle and WWDT
  source                                                     When in Idle, the WWDT Reset is blocked and will
It is the responsibility of the end user to determine what   instead wake the device. The WWDT wake-up is not an
is acceptable for their application when setting the         interrupt, therefore ROI does not apply.
VREGPM settings in order to ensure operation in
Sleep.
                                                               Note:     The WDT can bring the device out of Idle,
                                                                         in the same way it brings the device out of
  Note:     The PIC18F26/27/45/46/47/55/56/57K42                         Sleep. The DOZEN bit is not affected.
            devices do not have a configurable Low-
            Power Sleep mode. PIC18F26/27/45/46/             10.3      Peripheral Operation in Power
            47/55/56/57K42 devices are unregulated
                                                                       Saving Modes
            and are always in the lowest power state
            when in Sleep, with no wake-up time              All selected clock sources and the peripherals running
            penalty. These devices have a lower              off them are active in both Idle and Doze mode. Only in
            maximum VDD and I/O voltage than the             Sleep mode, both the FOSC and FOSC/4 clocks are
            PIC18(L)F26/27/45/46/47/55/56/57K42.             unavailable. All the other clock sources are active, if
            See       Section        44.0 “Electrical        enabled manually or through peripheral clock selection
            Specifications” for more information.            before the part enters Sleep.

10.2.4      IDLE MODE
When IDLEN is set (IDLEN = 1), the SLEEP instruction
will put the device into Idle mode. In Idle mode, the
CPU and memory operations are halted, but the
peripheral clocks continue to run. This mode is similar
to Doze mode, except that in Idle, both the CPU and
PFM are shut off.


  Note:     If CLKOUTEN is enabled (CLKOUTEN = 0,
            Configuration Word 1H), the output will
            continue operating while in Idle.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 175
                        PIC18(L)F26/27/45/46/47/55/56/57K42
10.4        Register Definitions: Voltage Regulator Control

REGISTER 10-1:           VREGCON: VOLTAGE REGULATOR CONTROL REGISTER(1)
        U-0            U-0              U-0             U-0        U-0          U-0          R/W-0/0        R/W-1/1
        —               —               —               —          —             —          VREGPM          Reserved
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-2            Unimplemented: Read as ‘0’
bit 1              VREGPM: Voltage Regulator Power Mode Selection bit
                   1 = Low-Power Sleep mode enabled in Sleep(2)
                       Draws lowest current in Sleep, slower wake-up
                   0 = Normal Power mode enabled in Sleep(2)
                       Draws higher current in Sleep, faster wake-up
bit 0              Reserved: Read as ‘1’. Maintain this bit set.

Note 1:       Not present in LF parts.
     2:       See Section 44.0 “Electrical Specifications”.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 176
                           PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 10-2:              CPUDOZE: DOZE AND IDLE REGISTER
   R/W-0/0         R/W/HC/HS-0/0            R/W-0/0            R/W-0/0                U-0         R/W-0/0           R/W-0/0        R/W-0/0
    IDLEN                  DOZEN               ROI                DOE                 —                             DOZE[2:0]
bit 7                                                                                                                                       bit 0


Legend:
R = Readable bit                          W = Writable bit                    U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                      x = Bit is unknown                  -n/n = Value at POR and BOR/Value at all other
                                                                              Resets
‘1’ = Bit is set                          ‘0’ = Bit is cleared                HC = Bit is cleared by hardware; HS = Bit is set by
                                                                              hardware


bit 7              IDLEN: Idle Enable bit
                   1 = A SLEEP instruction places the device into Idle mode
                   0 = A SLEEP instruction places the device into Sleep mode
bit 6              DOZEN: Doze Enable bit(1)
                   1 = Places the device into Doze mode
                   0 = Places the device into Normal mode
bit 5              ROI: Recover-On-Interrupt bit(1)
                   1 = Entering the Interrupt Service Routine (ISR) makes DOZEN = 0
                   0 = Entering the Interrupt Service Routine (ISR) does not change DOZEN
bit 4              DOE: Doze-On-Exit bit(1)
                   1 = Exiting the Interrupt Service Routine (ISR) makes DOZEN = 1
                   0 = Exiting the Interrupt Service Routine (ISR) does not change DOZEN
bit 3              Unimplemented: Read as ‘0’
bit 2-0            DOZE[2:0]: Ratio of CPU Instruction Cycles to Peripheral Instruction Cycles
                   111 =1:256
                   110 =1:128
                   101 =1:64
                   100 =1:32
                   011 =1:16
                   010 =1:8
                   001 =1:4
                   000 =1:2

Note 1:      Refer Table 10-1 for more details.


TABLE 10-2:          SUMMARY OF REGISTERS ASSOCIATED WITH POWER DOWN MODE
                                                                                                                                   Register on
Name               Bit 7          Bit 6         Bit 5            Bit 4        Bit 3          Bit 2          Bit 1         Bit 0
                                                                                                                                     Page

VREGCON(1)          —              —              —               —            —              —        VREGPM           Reserved      176
CPUDOZE            IDLEN        DOZEN            ROI             DOE           —                       DOZE[2:0]                      177
Legend:      — = unimplemented location, read as ‘0’. Shaded cells are not used in Power Down mode.
Note 1:      Not present in LF parts.


 2017-2021 Microchip Technology Inc.                                                                                  DS40001919G-page 177
