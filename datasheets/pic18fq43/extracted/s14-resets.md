                                                                                              PIC18F27/47/57Q43
                                                                                                          Resets


14.    Resets
       There are multiple ways to reset the device:
       •   Power-on Reset (POR)
       •   Brown-out Reset (BOR)
       •   Low-Power Brown-out Reset (LPBOR)
       •   MCLR Reset
       •   WDT Reset
       •   RESET instruction
       •   Stack Overflow
       •   Stack Underflow
       •   Programming mode exit
       •   Memory Execution Violation Reset
       •   Main LDO Voltage Regulator Reset
       •   Configuration Memory Reset
       A simplified block diagram of the On-Chip Reset Circuit is shown in the block diagram below.

       Figure 14-1. Simplified Block Diagram of On-Chip Reset Circuit

                                                                                                       Re v. 10 -00 00 06 G

                           ICSP Programming Mode Exit                                                             3/7/20 19


                           RESET Instruction
                           Memory Violation
                           Main LDO Voltage Regulator
                           Configuration Memory

                           Stack Underflow
                           Stack Overflow


           VPP /MCLR             MCLRE


                                         WWDT Time-out/
                                         Window violation
                                                                                                      Device
                                                                                                      Reset
                       Power-on
                        Reset
            VDD

                       Brown-out
                         Reset                                                   Power-up
                                                                                  Timer

                                                            LFINTOSC
                                                                                     2
                        LPBOR
                                                                       PWRTS
                         Reset


       Note:
       1. See the BOR Operating Modes table for BOR active conditions.

14.1   Power-on Reset (POR)
       The POR circuit holds the device in Reset until VDD has reached an acceptable level for minimum
       operation. Slow rising VDD, fast operating speeds or analog performance may require greater than


--- p239 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                                                Resets

        minimum VDD. The PWRT, BOR or MCLR features can be used to extend the start-up period until all
        device operation conditions have been met. The POR bit will be set to ‘0’ if a Power-on Reset has
        occurred.

14.2    Brown-out Reset (BOR)
        The BOR circuit holds the device in Reset when VDD reaches a selectable minimum level. Between
        the POR and BOR, complete voltage range coverage for execution protection can be implemented.
        The BOR bit will be set to ‘0’ if a BOR has occurred.
        The BOR module has four operating modes controlled by the BOREN Configuration bits. The four
        operating modes are:
        •   BOR is always on
        •   BOR is off when in Sleep
        •   BOR is controlled by software
        •   BOR is always off
        Refer to the BOR Operating Modes table for more information.
        A VDD noise rejection filter prevents the BOR from triggering on small events. If VDD falls below
        VBOR for a duration greater than parameter TBORDC, the device will reset. Refer to the “Electrical
        Specifications” chapter for more details.

14.2.1 BOR Is Always On
        When the BOREN Configuration bits are programmed to ‘b11, the BOR is always on. The device
        start-up will be delayed until the BOR is ready and VDD is higher than the BOR threshold.
        BOR protection is active during Sleep. The BOR does not delay wake-up from Sleep.

14.2.2 BOR Is Off in Sleep
        When the BOREN Configuration bits are programmed to ‘b10, the BOR is on, except in Sleep. The
        device start-up will be delayed until the BOR is ready and VDD is higher than the BOR threshold.
        BOR protection is not active during Sleep. The device wake-up will be delayed until the BOR is ready.

14.2.3 BOR Controlled by Software
        When the BOREN Configuration bits are programmed to ‘b01, the BOR is controlled by the SBOREN
        bit. The device start-up is not delayed by the BOR Ready condition or the VDD level.
        BOR protection begins as soon as the BOR circuit is ready. The status of the BOR circuit is reflected
        in the BORRDY bit.
        BOR protection selected by SBOREN bit is unchanged by Sleep.

14.2.4 BOR Is Always Off
        When the BOREN Configuration bits are programmed to ‘b00, the BOR is off at all times. The device
        start-up is not delayed by the BOR Ready condition or the VDD level.

        Table 14-1. Reset Condition for Special Registers
                                       Program
               Condition                                    STATUS Register(1,2)   PCON0 Register   PCON1 Register
                                       Counter
        Power-on Reset                    0                     -110 0000            0011 110x        ---- -111
        Brown-out Reset                   0                     -110 0000            0011 11u0        ---- -u1u
        MCLR Reset during
                                          0                     -uuu uuuu            uuuu 0uuu        ---- -uuu
        normal operation


--- p240 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                                           Resets

...........continued
                                    Program
          Condition                                       STATUS Register(1,2)      PCON0 Register            PCON1 Register
                                    Counter
MCLR Reset during
                                        0                     -10u uuuu               uuuu 0uuu                 ---- -uuu
Sleep
WDT Time-out Reset                      0                     -0uu uuuu               uuu0 uuuu                 ---- -uuu
WDT Wake-up from
                                      PC + 2                  -00u uuuu               uuuu uuuu                 ---- -uuu
Sleep
WWDT Window
                                        0                     -uuu uuuu               uu0u uuuu                 ---- -uuu
Violation Reset
Interrupt Wake-up from
                                     PC + 2(3)                -10u uuuu               uuuu uuuu                 ---- -uuu
Sleep
RESET Instruction
                                        0                     -uuu uuuu               uuuu u0uu                 ---- -uuu
Executed
Stack Overflow Reset
                                        0                     -uuu uuuu               1uuu uuuu                 ---- -uuu
(STVREN = 1)
Stack Underflow Reset
                                        0                     -uuu uuuu               u1uu uuuu                 ---- -uuu
(STVREN = 1)
Data Protection (Fuse
                                        0                     -uuu uuuu               uuuu uuuu                 ---- -uu0
Fault)
VREG or ULP Ready
                                        0                     -110 0000               0011 110u                 ---- -0u1
Fault
Memory Violation Reset                  0                     -uuu uuuu               uuuu uuuu                 ---- -u0u
Legend: u = unchanged, x = unknown, - = unimplemented bit, reads as ‘0’.
Notes:
1.    If a Status bit is not implemented, that bit will be read as ‘0’.
2.    Status bits Z, C, DC are reset by POR/BOR.
3.    When the wake-up is due to an interrupt and Global Interrupt Enable (GIE) bit is set, the return address is pushed on
      the stack and PC is loaded with the corresponding interrupt vector (depending on source, high or low priority) after
      execution of PC + 2.


Table 14-2. BOR Operating Modes
                                                                            Instruction Execution upon:
BOREN SBOREN Device Mode BOR Mode
                                                                Release of POR                    Wake-up from Sleep
  11(1)        X            X           Active      Wait for release of BOR (BORRDY = 1)              Begins immediately
                         Awake          Active      Wait for release of BOR (BORRDY = 1)                     N/A
     10        X
                          Sleep       Hibernate                       N/A                  Wait for release of BOR (BORRDY = 1)
               1            X           Active
     01                                             Wait for release of BOR (BORRDY = 1)              Begins immediately
               0            X         Hibernate
     00        X            X          Disabled                                  Begins immediately

Note:
1. In this specific case, “Release of POR” and “Wake-up from Sleep”, there is no BOR ready delay
   in start-up. The BOR ready flag, (BORRDY = 1), will be set before the CPU is ready to execute
   instructions because the BOR circuit is forced on by the BOREN bits


--- p241 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                                                     Resets

       Figure 14-2. Brown-Out Situations
                                                                                            Rev. 30-000092A
                                                                                                   4/12/2017


                          VDD
                                                                                           VBOR


                       Internal
                         Reset                                      TPWRT(1)


                          VDD
                                                                                           VBOR


                       Internal                                  < TPWRT
                         Reset                                             TPWRT(1)


                          VDD
                                                                                           VBOR


                       Internal
                         Reset                                             TPWRT(1)


       Note:
       1. TPWRT delay only if the Configuration bits enable the Power-up Timer.

14.2.5 BOR and Bulk Erase
       BOR is forced ON during PFM Bulk Erase operations to make sure that the system code protection
       cannot be compromised by reducing VDD.
       During Bulk Erase, the BOR is enabled at the lowest BOR threshold level, even if it is configured to
       some other value. If VDD falls, the erase cycle will be aborted, but the device will not be reset.

14.3   Low-Power Brown-out Reset (LPBOR)
       The Low-Power Brown-out Reset (LPBOR) provides an additional BOR circuit for low-power
       operation. Refer to the figure below to see how the BOR interacts with other modules.
       The LPBOR is used to monitor the external VDD pin. When too low of a voltage is detected, the device
       is held in Reset.


--- p242 ---
                                                                                                     PIC18F27/47/57Q43
                                                                                                                 Resets

       Figure 14-3. LPBOR, BOR, POR Relationship

                                                                                                           Rev. 30-000091B
                                                                                                                  6/21/2017


                 Any Reset

                                            BOR
                                          BOR Event

                 REARM POR
                   Event                                                                          To PCON
                                                                                                  indicator bit
                     POR
                                            LPBOR
                  POR Event
                                         LPBOR Event


                                                                                                   Reset
                                                                                                   logic


14.3.1 Enabling LPBOR
       The LPBOR is controlled by the LPBOREN Configuration bit. When the device is erased, the LPBOR
       module defaults to disabled.

14.3.2 LPBOR Module Output
       The output of the LPBOR module indicates whether or not a Reset is to be asserted. This signal is
       OR’d with the Reset signal of the BOR module to provide the generic BOR signal, which goes to the
       PCON0 register and to the power control block.

14.4   MCLR Reset
       MCLR is an optional external input that can reset the device. The MCLR function is controlled by the
       MCLRE and LVP Configuration bits (see the table below). The RMCLR bit will be set to ‘0’ if a MCLR
       has occurred.

       Table 14-3. MCLR Configuration
                       MCLRE                             LVP                             MCLR
                          x                               1                             Enabled
                          1                               0                             Enabled
                          0                               0                             Disabled


14.4.1 MCLR Enabled
       When MCLR is enabled and the pin is held low, the device is held in Reset. The MCLR pin is
       connected to VDD through an internal weak pull-up.
       The device has a noise filter in the MCLR Reset path. The filter will detect and ignore small pulses.


                    Important: An internal Reset event (RESET instruction, BOR, WWDT, POR,
                    STKOVF, STKUNF) does not drive the MCLR pin low.


--- p243 ---
                                                                                               PIC18F27/47/57Q43
                                                                                                           Resets

14.4.2 MCLR Disabled
       When MCLR is disabled, the MCLR pin becomes input-only and pin functions such as internal weak
       pull-ups are under software control.

14.5   Windowed Watchdog Timer (WWDT) Reset
       The Windowed Watchdog Timer generates a Reset if the firmware does not issue a CLRWDT
       instruction within the time-out period or window set. The TO and PD bits in the STATUS register
       and the RWDT bit are changed to indicate a WDT Reset. The WDTWV bit indicates if the WDT Reset
       has occurred due to a time-out or a window violation.

14.6   RESET Instruction
       A RESET instruction will cause a device Reset. The RI bit will be set to ‘0’. See Determining the Cause
       of a Reset for default conditions after a RESET instruction has occurred.

14.7   Stack Overflow/Underflow Reset
       The device can be reset when the Stack Overflows or Underflows. The STKOVF or STKUNF bits
       indicate the Reset condition. These Resets are enabled by setting the STVREN Configuration bit.

14.8   Programming Mode Exit
       Upon exit of Programming mode, the device will operate as if a POR had just occurred.

14.9   Power-up Timer (PWRT)
       The Power-up Timer provides a selected time-out duration on POR or Brown-out Reset.
       The device is held in Reset as long as PWRT is active. The PWRT delay allows additional time for VDD
       to rise to an acceptable level. The Power-up Timer is selected by setting the PWRTS Configuration
       bits accordingly.
       The Power-up Timer starts after the release of the POR and BOR/LPBOR if enabled, as shown in
       Figure 14-4.

14.10 Start-Up Sequence
       Upon the release of a POR or BOR, the following must occur before the device will begin executing:
       1. Power-up Timer runs to completion (if enabled).
       2. Oscillator Start-up Timer runs to completion (if required for selected oscillator source).
       3. MCLR must be released (if enabled).
       The total time-out will vary based on the oscillator configuration and Power-up Timer configuration.
       The Power-up Timer and Oscillator Start-up Timer run independently of MCLR Reset. If MCLR is kept
       low long enough, the Power-up Timer and Oscillator Start-up Timer will expire. Upon bringing MCLR
       high, the device will begin execution after 10 FOSC cycles (see the figure below). This is useful for
       testing purposes or to synchronize more than one device operating in parallel.


--- p244 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                                                        Resets

       Figure 14-4. Reset Start-Up Sequence
                                                                                                                          Rev. 30-000093A
                                                                                                                                 4/12/2017


                           VDD

                  Internal POR

                                                            TPWRT
               Power-up Timer

                         MCLR

                                                                               TMCLR
               Internal RESET


                                    Oscillator Modes
              External Crystal
                                                                                        TOST
        Oscillator Start-up Timer

                      Oscillator

                           FOSC

           Internal Oscillator

                      Oscillator

                          FOSC

          External Clock (EC)

                         CLKIN

                          FOSC


14.10.1 Memory Execution Violation
       A memory execution violation Reset occurs if executing an instruction being fetched from outside
       the valid execution area. The invalid execution areas are:
       1. Addresses outside implemented program memory.
       2. Storage Area Flash (SAF) inside program memory, if it is enabled.
       When a memory execution violation is generated, the device is reset and the MEMV bit is cleared to
       signal the cause of the Reset. The MEMV bit must be set in the user code after a memory execution
       violation Reset has occurred to detect further violation Resets.

14.11 Determining the Cause of a Reset
       Upon any Reset, multiple bits in the STATUS, PCON0 and PCON1 registers are updated to indicate
       the cause of the Reset. The following table shows the Reset conditions of these registers.

       Table 14-4. Reset Condition for Special Registers
                                               Program
                Condition                                        STATUS Register(1,2)      PCON0 Register   PCON1 Register
                                               Counter
        Power-on Reset                            0                  -110 0000                 0011 110x      ---- -111
        Brown-out Reset                           0                  -110 0000                 0011 11u0      ---- -u1u
        MCLR Reset during
                                                  0                  -uuu uuuu                 uuuu 0uuu      ---- -uuu
        normal operation


--- p245 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                                              Resets

      ...........continued
                                           Program
               Condition                                         STATUS Register(1,2)   PCON0 Register           PCON1 Register
                                           Counter
       MCLR Reset during
                                               0                     -10u uuuu            uuuu 0uuu                ---- -uuu
       Sleep
       WDT Time-out Reset                      0                     -0uu uuuu            uuu0 uuuu                ---- -uuu
       WDT Wake-up from
                                             PC + 2                  -00u uuuu            uuuu uuuu                ---- -uuu
       Sleep
       WWDT Window
                                               0                     -uuu uuuu            uu0u uuuu                ---- -uuu
       Violation Reset
       Interrupt Wake-up from
                                            PC + 2(3)                -10u uuuu            uuuu uuuu                ---- -uuu
       Sleep
       RESET Instruction
                                               0                     -uuu uuuu            uuuu u0uu                ---- -uuu
       Executed
       Stack Overflow Reset
                                               0                     -uuu uuuu            1uuu uuuu                ---- -uuu
       (STVREN = 1)
       Stack Underflow Reset
                                               0                     -uuu uuuu            u1uu uuuu                ---- -uuu
       (STVREN = 1)
       Data Protection (Fuse
                                               0                     -uuu uuuu            uuuu uuuu                ---- -uu0
       Fault)
       VREG or ULP Ready
                                               0                     -110 0000            0011 110u                ---- -0u1
       Fault
       Memory Violation Reset                  0                     -uuu uuuu            uuuu uuuu                ---- -u0u
       Legend: u = unchanged, x = unknown, - = unimplemented bit, reads as ‘0’.
       Notes:
       1.    If a Status bit is not implemented, that bit will be read as ‘0’.
       2.    Status bits Z, C, DC are reset by POR/BOR.
       3.    When the wake-up is due to an interrupt and Global Interrupt Enable (GIE) bit is set, the return address is pushed on
             the stack and PC is loaded with the corresponding interrupt vector (depending on source, high or low priority) after
             execution of PC + 2.


14.12 Power Control (PCON0/PCON1) Registers
      The Power Control (PCON0/PCON1) registers contain flag bits to differentiate between the following
      Reset events:
      •     Brown-out Reset (BOR)
      •     Power-on Reset (POR)
      •     Reset Instruction Reset (RI)
      •     MCLR Reset (RMCLR)
      •     Watchdog Timer Reset (RWDT)
      •     Watchdog Window Violation (WDTWV)
      •     Stack Underflow Reset (STKUNF)
      •     Stack Overflow Reset (STKOVF)
      •     Configuration Memory Reset (RCM)
      •     Memory Violation Reset (MEMV)
      •     Main LDO Voltage Regulator Reset (RVREG)
      Hardware will change the corresponding register bit or bits as a result of the Reset event. Bits for
      other Reset events remain unchanged. See Determining the Cause of a Reset for more details.
      Software will reset the bit to the Inactive state after restart (hardware will not reset the bit).


--- p246 ---
                                                                                           PIC18F27/47/57Q43
                                                                                                       Resets

       Software may also set any PCON0 bit to the Active state so that user code may be tested, but no
       Reset action will be generated.

14.13 Register Definitions: Power Control


--- p247 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                                                    Resets

14.13.1 BORCON

           Name:         BORCON
           Address:      0x049

           Brown-out Reset Control Register

     Bit          7             6               5               4                  3            2   1           0
               SBOREN                                                                                         BORRDY
  Access         R/W                                                                                            R
   Reset          1                                                                                             q

Bit 7 – SBOREN Software Brown-out Reset Enable
          Reset States: POR/BOR = 1
                        All Other Resets = u
           Value        Condition               Description
           —            If BOREN ≠ 01           SBOREN is read/write but has no effect on the BOR
           1            If BOREN = 01            BOR Enabled
           0            If BOREN = 01            BOR Disabled


Bit 0 – BORRDY Brown-out Reset Circuit Ready Status
         Reset States: POR/BOR = q
                       All Other Resets = u
           Value        Description
           1            The Brown-out Reset Circuit is active and armed
           0            The Brown-out Reset Circuit is disabled or is warming up


--- p248 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                                                Resets

14.13.2 PCON0

            Name:         PCON0
            Address:      0x4F0

            Power Control Register 0

      Bit          7             6              5               4               3                 2           1                 0
                STKOVF        STKUNF         WDTWV            RWDT           RMCLR               RI          POR              BOR
  Access        R/W/HS        R/W/HS         R/W/HC          R/W/HC          R/W/HC            R/W/HC      R/W/HC            R/W/HC
   Reset           0             0              1               1               1                 1           0                 q

Bit 7 – STKOVF Stack Overflow Flag
          Reset States: POR/BOR = 0
                        All Other Resets = q
            Value        Description
            1            A Stack Overflow occurred (more CALLs than fit on the stack)
            0            A Stack Overflow has not occurred or set to ‘0’ by firmware


Bit 6 – STKUNF Stack Underflow Flag
          Reset States: POR/BOR = 0
                        All Other Resets = q
            Value        Description
            1            A Stack Underflow occurred (more RETURNs than CALLs)
            0            A Stack Underflow has not occurred or set to ‘0’ by firmware


Bit 5 – WDTWV Watchdog Window Violation Flag
         Reset States: POR/BOR = 1
                       All Other Resets = q
            Value        Description
            1            A WDT window violation has not occurred or set to ‘1’ by firmware
            0            A CLRWDT instruction was issued when the WDT Reset window was closed (set to ‘0’ in hardware when a WDT
                         window violation Reset occurs)

Bit 4 – RWDT WDT Reset Flag
         Reset States: POR/BOR = 1
                       All Other Resets = q
            Value        Description
            1            A WDT overflow/Time-out Reset has not occurred or set to ‘1’ by firmware
            0            A WDT overflow/Time-out Reset has occurred (set to ‘0’ in hardware when a WDT Reset occurs)


Bit 3 – RMCLR MCLR Reset Flag
         Reset States: POR/BOR = 1
                       All Other Resets = q
            Value        Description
            1            A MCLR Reset has not occurred or set to ‘1’ by firmware
            0            A MCLR Reset has occurred (set to ‘0’ in hardware when a MCLR Reset occurs)


Bit 2 – RI RESET Instruction Flag
          Reset States: POR/BOR = 1
                        All Other Resets = q
            Value        Description
            1            A RESET instruction has not been executed or set to ‘1’ by firmware
            0            A RESET instruction has been executed (set to ‘0’ in hardware upon executing a RESET instruction)


--- p249 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                                                        Resets

Bit 1 – POR Power-on Reset Status
         Reset States: POR/BOR = 0
                       All Other Resets = u
         Value      Description
         1          No VDD Power-on Reset occurred or set to ‘1’ by firmware
         0          A VDD Power-on Reset occurred (set to ‘0’ in hardware when a Power-on Reset occurs)


Bit 0 – BOR Brown-out Reset Status
         Reset States: POR/BOR = q
                       All Other Resets = u
         Value      Description
         1          No VDD Brown-out Reset occurred or set to ‘1’ by firmware
         0          A VDD Brown-out Reset occurred (set to ‘0’ in hardware when a Brown-out Reset occurs)


--- p250 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                                                Resets

14.13.3 PCON1

            Name:        PCON1
            Address:     0x4F1

            Power Control Register 1

      Bit           7            6              5               4                  3            2             1              0
                                                                                             RVREG          MEMV           RCM
  Access                                                                                     R/W/HC        R/W/HC         R/W/HC
   Reset                                                                                        1             0              q

Bit 2 – RVREG Main LDO Voltage Regulator Reset Flag
          Reset States: POR/BOR = 1
                        All Other Resets = q
            Value       Description
            1           No LDO or ULP “ready” Reset has occurred or set to ‘1’ by firmware
            0           LDO or ULP “ready” Reset has occurred (VDDCORE reached its minimum spec)

Bit 1 – MEMV Memory Violation Reset Flag
         Reset States: POR/BOR = 0
                       All Other Resets = u
            Value       Description
            1           No memory violation Reset occurred or set to ‘1’ by firmware
            0           A memory violation Reset occurred (set to ‘0’ in hardware when a Memory Violation occurs)


Bit 0 – RCM Configuration Memory Reset Flag
          Reset States: POR/BOR = q
                        All Other Resets = u
            Value       Description
            1           A Reset occurred due to corruption of the configuration and/or calibration data latches
            0           The configuration and calibration latches have not been corrupted


--- p251 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                                              Resets

14.14 Register Summary - BOR Control and Power Control
Address    Name      Bit Pos.     7           6           5             4         3        2      1            0
  0x49    BORCON       7:0      SBOREN                                                                      BORRDY
  0x4A
   ...    Reserved
 0x04EF
 0x04F0   PCON0        7:0      STKOVF     STKUNF      WDTWV        RWDT        RMCLR      RI     POR        BOR
 0x04F1   PCON1        7:0                                                               RVREG   MEMV        RCM


--- p252 ---
