17.    Power-Saving Modes
       The purpose of the Power-Saving modes is to reduce power consumption. There are three Power-
       Saving modes:
       •   Doze mode
       •   Sleep mode
       •   Idle mode

17.1   Doze Mode
       Doze mode allows for power saving by reducing CPU operation and Program Flash Memory (PFM)
       access, without affecting peripheral operation. Doze mode differs from Sleep mode because the
       band gap and system oscillators continue to operate, while only the CPU and PFM are affected. The
       reduced execution saves power by eliminating unnecessary operations within the CPU and memory.
       When the Doze Enable bit is set (DOZEN = ‘b1) the CPU executes only one instruction cycle out of
       every N cycles as defined by the DOZE bits. For example, if DOZE = 001, the instruction cycle ratio
       is 1:4. The CPU and memory execute for one instruction cycle and then lay Idle for three instruction
       cycles. During the unused cycles, the peripherals continue to operate at the system clock speed.

17.1.1 Doze Operation
       The Doze operation is illustrated in Figure 17-1. As with normal operation, the instruction is
       fetched for the next instruction cycle while the previous instruction is executed. The Q-clocks to
       the peripherals continue throughout the periods in which no instructions are fetched or executed.
       The following configuration settings apply for this example:
       •   Doze enabled (DOZEN = 1)
       •   CPU instruction cycle to peripheral instruction cycle ratio of 1:4
       •   Recover-on-Interrupt enabled (ROI = 1)


--- p283 ---
       Figure 17-1. Doze Mode Operation Example

          System
           Clock


                        1               1               1               1               1               1                1               1               1               1               1               1               1


                            2               2               2               2               2                2               2               2               2               2               2               2               2


          Instruction
                                3               3               3               3               3                3               3               3               3               3               3               3               3
            Period


                                    4               4               4               4               4                4               4               4               4               4               4               4               4


                                        1 2 3 4                                                         1 2 3 4                                          1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4
          CPU Clock

          PFM Op s                          Fetch                                                           Fetch                                            Push            0004h           Fetch           Fetch


          CPU Op s                          Exec                                                            Exec                                         Exec(1,2)           NOP             Exec            Exec            Exec


                                                                                                                                          Interrupt
                                                                                                                                         (ROI = 1)


       Notes:
       1. Multicycle instructions are executed to completion before fetching 0x0004.
       2. If the prefetched instruction clears GIE, the ISR will not occur, but DOZEN is still cleared and the
          CPU will resume execution at full speed.

17.1.2 Interrupts During Doze
       System behavior for interrupts that may occur during Doze mode are configured using the ROI and
       DOE bits. Refer to the example below for details about system behavior in all cases for a transition
       from Main to ISR back to Main.

                Example 17-1. Doze Software Example

                  // Mainline operation
                  bool somethingToDo = FALSE;

                  void main() {
                      initializeSystem();
                      // DOZE = 64:1 (for example)
                      // ROI = 1;
                      GIE = 1; // enable interrupts
                      while (1) {
                          // If ADC completed, process data
                          if (somethingToDo) {
                              doSomething();
                              DOZEN = 1; // resume low-power
                          }
                      }
                  }
                  // Data interrupt handler

                  void interrupt() {
                      // DOZEN = 0 because ROI = 1
                      if (ADIF) {
                          somethingToDo = TRUE;
                          DOE = 0; // make main() go fast
                          ADIF = 0;


--- p284 ---
                     }
                     // else check other interrupts...
                     if (TMR0IF) {
                         timerTick++;
                         DOE = 1; // make main() go slow
                         TMR0IF = 0;
                     }
                 }

               Note: User software can change the DOE bit in the ISR.


17.2   Sleep Mode
       Sleep mode provides the greatest power savings because both the CPU and selected peripherals
       cease to operate. However, some peripheral clocks continue to operate during Sleep. The
       peripherals that use those clocks also continue to operate. Sleep mode is entered by executing the
       SLEEP instruction, while the IDLEN bit is clear. Upon entering Sleep mode, the following conditions
       exist:
       1. The WDT will be cleared, but keeps running if enabled for operation during Sleep.
       2. The PD bit of the STATUS register is cleared.
       3. The TO bit of the STATUS register is set.
       4. The CPU clock is disabled.
       5. LFINTOSC, SOSC, HFINTOSC and ADCRC are unaffected. Peripherals using them may continue
          operation during Sleep.
       6. I/O ports maintain the status they had before Sleep was executed (driving high, low, or high-
          impedance).
       7. Resets other than WDT are not affected by Sleep mode.


                     Important: Refer to individual chapters for more details on peripheral operation during
                     Sleep.


       To minimize current consumption, consider the following conditions:
       •   I/O pins must not be floating
       •   External circuitry sinking current from I/O pins
       •   Internal circuitry sourcing current to I/O pins
       •   Current draw from pins with internal weak pull-ups
       •   Peripherals using clock source unaffected by Sleep
       I/O pins that are high-impedance inputs need to be pulled to VDD or VSS externally to avoid switching
       currents caused by floating inputs. Examples of internal circuitry that might be consuming current
       include modules such as the DAC and FVR peripherals.

17.2.1 Wake-Up from Sleep
       The device can wake up from Sleep through one of the following events:
       1. External Reset input on MCLR pin, if enabled.
       2. BOR Reset, if enabled.
       3. Low-Power Brown-out Reset (LPBOR), if enabled.
       4. POR Reset.


--- p285 ---
       5. Windowed Watchdog Timer, if enabled.
       6. All interrupt sources except clock switch interrupt can wake up the part.


                    Important: The first five events will cause a device Reset. The last event in the list is
                    considered a continuation of program execution. For more information about determining
                    whether a device Reset or wake-up event occurred, refer to the “Resets” chapter.


       When the SLEEP instruction is being executed, the next instruction (PC + 2) is prefetched. For the
       device to wake up through an interrupt event, the corresponding Interrupt Enable bit must be
       enabled in the PIEx register. Wake-up will occur regardless of the state of the Global Interrupt Enable
       (GIE) bit. If the GIE bit is disabled, the device will continue execution at the instruction after the
       SLEEP instruction. If the GIE bit is enabled, the device executes the instruction after the SLEEP
       instruction and then call the Interrupt Service Routine (ISR).


                    Important: It is recommended to add a NOP as the immediate instruction after the SLEEP
                    instruction.


       The WDT is cleared when the device wakes up from Sleep, regardless of the source of wake-up.
       Upon a wake-from-Sleep event, the core will wait for a combination of three conditions before
       beginning execution. The conditions are:
       •   PFM Ready
       •   System Clock Ready
       •   BOR Ready (unless BOR is disabled)

17.2.2 Wake-Up Using Interrupts
       When global interrupts are disabled (GIE cleared) and any interrupt source, with the exception of the
       clock switch interrupt, has both its interrupt enable bit and interrupt flag bit set, one of the following
       will occur:
       •   If the interrupt occurs before the execution of a SLEEP instruction:
            – The SLEEP instruction will execute as a NOP
            – WDT and WDT prescaler will not be cleared
            – The TO bit of the STATUS register will not be set
            – The PD bit of the STATUS register will not be cleared
       •   If the interrupt occurs during or after the execution of a SLEEP instruction:
            – The SLEEP instruction will be completely executed
            – Device will immediately wake up from Sleep
            – WDT and WDT prescaler will be cleared
            – The TO bit of the STATUS register will be set
            – The PD bit of the STATUS register will be cleared
       In the event where flag bits were checked before executing a SLEEP instruction, it may be possible
       for flag bits to become set before the SLEEP instruction completes. To determine whether a SLEEP
       instruction executed, test the PD bit. If the PD bit is set, the SLEEP instruction was executed as a
       NOP.


--- p286 ---
        Figure 17-2. Wake-Up from Sleep through Interrupt


                    CLKIN(1)

                 CLKOUT (2)                                                          TOS T(3)


              Inte rrupt Flag
                                                                                                Interrupt Latency(4)
             Glo bal Interru pt
                       Ena ble                                       Processor in
                                                                        Sleep

            Instruction Flo w
                          PC             PC              PC + 1             PC + 2                    PC + 2             PC + 2         0004h          0005h
                Instruction
                  Fetche d        Inst(PC) = Slee p   Inst(PC + 1)                               Inst(PC + 2)                       Inst(0x0004)   Inst(0x0005)
                Instruction        Inst(PC - 1)          Sleep                                   Inst(PC + 1)          Forced NOP   Forced NOP     Inst(0x0004)
                  Fetche d


        Notes:
        1. External clock - High, Medium, Low mode assumed.
        2. CLKOUT is shown here for timing reference.
        3. TOST = 1024 TOSC. This delay does not apply to EC and INTOSC Oscillator modes.
        4. GIE = 1 assumed. In this case after wake-up, the processor calls the ISR at 0x0004. If GIE = 0,
           execution will continue in-line.

17.2.3 Low-Power Sleep Mode
        This device family contains an internal Low Dropout (LDO) voltage regulator, which allows the
        device I/O pins to operate at voltages up to VDD while the internal device logic operates at a lower
        voltage. The LDO and its associated reference circuitry must remain active in Sleep but can operate
        in different Power modes. This allows the user to optimize the operating current in Sleep mode,
        depending on the application requirements.

17.2.3.1 Sleep Current vs. Wake-Up Time
        The Low-Power Sleep mode can be selected by setting the VREGPM bits as following:
        • VREGPM = ‘b00; the voltage regulator is in High Power mode. In this mode, the voltage regulator
          and reference circuitry remain in the normal configuration while in Sleep. Hence, there is no
          delay needed for these circuits to stabilize after wake-up (fastest wake-up from Sleep).
        •   VREGPM = ‘b01; the voltage regulator is in Low Power mode. In this mode, when waking up from
            Sleep, an extra delay time is required for the voltage regulator and reference circuitry to return to
            the normal configuration and stabilize (faster wake-up from Sleep).
        •   VREGPM = ‘b10; the voltage regulator is in Ultra-Low Power mode. In this mode, the voltage
            regulator and reference circuitry are in the lowest current consumption mode and all the
            auxiliary circuits remain shut down. Wake-up from Sleep in this mode needs the longest delay
            time for the voltage regulator and reference circuitry to stabilize (lowest current consumption).
        •   VREGPM = ‘b11; this mode is similar to the Ultra-Low Power mode (VREGPM = ‘b10) and is
            recommended ONLY for extended temperature ranges at or above 70℃.

17.2.3.2 Peripheral Usage in Sleep
        Some peripherals that can operate in High-Power Sleep mode (VREGPM = ‘b00) will not operate as
        intended in the Low-Power Sleep modes (VREGPM = ‘b01 and ‘b11). The Low-Power Sleep modes
        are intended for use with the following peripherals:
        •   Brown-out Reset (BOR)
        •   Windowed Watchdog Timer (WWDT)
        •   External interrupt pin/interrupt-on-change pins


--- p287 ---
        It is the responsibility of the end user to determine what is acceptable for their application when
        setting the VREGPM settings to ensure correct operation in Sleep.

17.3    Idle Mode
        When the IDLEN bit is clear, the SLEEP instruction will put the device into full Sleep mode. When
        IDLEN is set, the SLEEP instruction will put the device into Idle mode. In Idle mode, the CPU and
        memory operations are halted, but the peripheral clocks continue to run. This mode is similar to
        Doze mode, except that in Idle both the CPU and program memory are shut off.


                    Important:
                    1. Peripherals using FOSC will continue to operate while in Idle (but not in Sleep).
                       Peripherals using HFINTOSC:LFINTOSC will continue running in both Idle and Sleep.
                    2. When the Clock Out Enable (CLKOUTEN) Configuration bit is cleared, the CLKOUT pin
                       will continue operating while in Idle.


17.3.1 Idle and Interrupts
        Idle mode ends when an interrupt occurs (even if global interrupts are disabled), but IDLEN is not
        changed. The device can re-enter Idle by executing the SLEEP instruction. If Recover-on-Interrupt
        is enabled (ROI = 1), the interrupt that brings the device out of Idle also restores full-speed CPU
        execution when Doze is also enabled.

17.3.2 Idle and WWDT
        When in Idle, the WWDT Reset is blocked and will instead wake the device. The WWDT wake-up is not
        an interrupt, therefore ROI does not apply.


                    Important: The WWDT can bring the device out of Idle, in the same way it brings the
                    device out of Sleep. The DOZEN bit is not affected.


17.4    Peripheral Operation in Power-Saving Modes
        All selected clock sources and the peripherals running from them are active in both Idle and Doze
        modes. Only in Sleep mode, both the FOSC and FOSC/4 clocks are unavailable. However, all other
        clock sources enabled specifically or through peripheral clock selection before the part enters Sleep,
        remain operating in Sleep.

17.5    Register Definitions: Power-Savings Control


--- p288 ---
17.5.1 CPUDOZE

            Name:        CPUDOZE
            Address:     0x4F2

            Doze and Idle Register

      Bit         7            6               5               4                3               2      1             0
                IDLEN        DOZEN            ROI             DOE                                   DOZE[2:0]
  Access         R/W       R/W/HC/HS          R/W          R/W/HC/HS                         R/W      R/W          R/W
   Reset          0            0               0               0                              0        0            0

Bit 7 – IDLEN Idle Enable
            Value       Description
            1           A SLEEP instruction places device into Idle mode
            0           A SLEEP instruction places the device into Sleep mode


Bit 6 – DOZEN Doze Enable(1)
            Value       Description
            1           Places devices into Doze setting
            0           Places devices into Normal mode

Bit 5 – ROI Recover-on-Interrupt(1)
            Value       Description
            1           Entering the Interrupt Service Routine (ISR) makes DOZEN = 0
            0           Entering the Interrupt Service Routine (ISR) does not change DOZEN

Bit 4 – DOE Doze-on-Exit(1)
            Value       Description
            1           Exiting the ISR makes DOZEN = 1
            0           Exiting the ISR does not change DOZEN

Bits 2:0 – DOZE[2:0] Ratio of CPU Instruction Cycles to Peripheral Instruction Cycles
            Value       Description
            111         1:256
            110         1:128
            101         1:64
            100         1:32
            011         1:16
            010         1:8
            001         1:4
            000         1:2

            Note:
            1. When ROI = 1 or DOE = 1.


--- p289 ---
17.5.2 VREGCON

           Name:        VREGCON
           Address:     0x048

           Voltage Regulator Control Register

     Bit           7           6              5                4                  3           2            1           0
                                                  PMSYS[1:0]                                                VREGPM[1:0]
  Access                                      R                R                                          R/W        R/W
   Reset                                      q                q                                           1           0

Bits 5:4 – PMSYS[1:0] System Power Mode Status
           Value       Description
           11          Regulator in Ultra-Low Power (ULP) mode for extended temperature range is active
           10          Regulator in Ultra-Low Power (ULP) mode is active
           01          Regulator in Low Power (LP) mode is active
           00          Regulator in High Power (HP) mode is active

Bits 1:0 – VREGPM[1:0] Voltage Regulator Power Mode Selection
           Value       Description
           11          Regulator in Ultra-Low Power (ULP) mode. Use ONLY for extended temperature range
           10          Regulator in Ultra-Low Power (ULP) mode (lowest current consumption)
           01          Regulator in Low Power (LP) mode (faster wake-up from Sleep)
           00          Regulator in High Power (HP) mode (fastest wake-up from Sleep)


--- p290 ---
17.6      Register Summary - Power-Savings Control
Address     Name      Bit Pos.     7          6           5                4      3      2       1              0
 0x00
  ...      Reserved
 0x47
  0x48     VREGCON      7:0                                   PMSYS[1:0]                          VREGPM[1:0]
  0x49
   ...     Reserved
 0x04F1
 0x04F2    CPUDOZE      7:0      IDLEN      DOZEN        ROI           DOE                   DOZE[2:0]


--- p291 ---
