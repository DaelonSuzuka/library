                      PIC18(L)F26/27/45/46/47/55/56/57K42
6.0      RESETS                                                      To allow VDD to stabilize, an optional Power-up Timer
                                                                     can be enabled to extend the Reset time after a BOR
There are multiple ways to reset this device:                        or POR event.
• Power-on Reset (POR)                                               A simplified block diagram of the On-Chip Reset Circuit
• Brown-out Reset (BOR)                                              is shown in Figure 6-1.
• Low-Power Brown-Out Reset (LPBOR)
• MCLR Reset
• WDT Reset
• RESET instruction
• Stack Overflow
• Stack Underflow
• Programming mode exit
• Memory Execution Violation Reset (MEMV)

FIGURE 6-1:            SIMPLIFIED BLOCK DIAGRAM OF ON-CHIP RESET CIRCUIT
                                                                                                                  Rev. 10-000006G
                                                                                                                          4/6/2017


                    ICSP™ Programming Mode Exit
                    RESET Instruction
                    Memory Violation

                   Stack Underflow
                   Stack Overflow


VPP /MCLR                 MCLRE


                                       WWDT Time-out/
                                       Window violation                                                           Device
                                                                                                                  Reset

               Power-on
                Reset
  VDD

               Brown-out
                 Reset                                                         Power-up
                                                                                Timer

                                                          LFINTOSC
                                                                                    2
                LPBOR
                                                               PWRTS<1:0>
                 Reset


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 81
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 6-2:            LPBOR, BOR, POR RELATIONSHIP


                                           BOR
                                         BOR Event

             REARM POR
               Event                                    To PCON0
                                                        indicator bit
                   POR
                                          LPBOR
               POR Event
                                        LPBOR Event


                                                        Reset
                                                        logic


 2017-2021 Microchip Technology Inc.                 DS40001919G-page 82
                      PIC18(L)F26/27/45/46/47/55/56/57K42
6.1      Power-on Reset (POR)                             6.2.3       BOR CONTROLLED BY SOFTWARE
The POR circuit holds the device in Reset until VDD has   When the BOREN bits of Configuration Words are
reached an acceptable level for minimum operation.        programmed to ‘01’, the BOR is controlled by the
Slow rising VDD, fast operating speeds or analog          SBOREN bit of the BORCON register. The device start-
performance may require greater than minimum VDD.         up is not delayed by the BOR ready condition or the
The PWRT, BOR or MCLR features can be used to             VDD level.
extend the start-up period until all device operation     BOR protection begins as soon as the BOR circuit is
conditions have been met.                                 ready. The status of the BOR circuit is reflected in the
                                                          BORRDY bit of the BORCON register.
6.2      Brown-out Reset (BOR)                            BOR protection is unchanged by Sleep.
The BOR circuit holds the device in Reset when VDD
                                                          6.2.4       BOR AND BULK ERASE
reaches a selectable minimum level. Between the
POR and BOR, complete voltage range coverage for          BOR is forced ON during PFM Bulk Erase operations
execution protection can be implemented.                  to make sure that a safe erase voltage is maintained for
                                                          a successful erase cycle.
The Brown-out Reset module has four operating
modes controlled by the BOREN[1:0] bits in                During Bulk Erase, the BOR is enabled at 2.45V for F
Configuration Words. The four operating modes are:        and LF devices, even if it is configured to some other
                                                          value. If VDD falls, the erase cycle will be aborted, but
• BOR is always on
                                                          the device will not be reset.
• BOR is off when in Sleep
• BOR is controlled by software
• BOR is always off
Refer to Table 6-1 for more information.
The Brown-out Reset voltage level is selectable by
configuring the BORV[1:0] bits in Configuration Words.
A VDD noise rejection filter prevents the BOR from
triggering on small events. If VDD falls below VBOR for
a duration greater than parameter TBORDC, the device
will reset. See Table 44-12 for more information.

6.2.1       BOR IS ALWAYS ON
When the BOREN bits of Configuration Words are
programmed to ‘11’, the BOR is always on. The device
start-up will be delayed until the BOR is ready and VDD
is higher than the BOR threshold.
BOR protection is active during Sleep. The BOR does
not delay wake-up from Sleep.

6.2.2       BOR IS OFF IN SLEEP
When the BOREN bits of Configuration Words are
programmed to ‘10’, the BOR is on, except in Sleep.
The device start-up will be delayed until the BOR is
ready and VDD is higher than the BOR threshold.
BOR protection is not active during Sleep. The device
wake-up will be delayed until the BOR is ready.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 83
                            PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 6-1:          BOR OPERATING MODES
                                                                                 Instruction Execution upon:
  BOREN[1:0]         SBOREN       Device Mode       BOR Mode
                                                                           Release of POR        Wake-up from Sleep
                                                                    Wait for release of BOR
       11                   X            X             Active                                     Begins immediately
                                                                        (BORRDY = 1)
                                                                    Wait for release of BOR
                                        Awake          Active                                              N/A
                                                                        (BORRDY = 1)
       10                   X
                                                                                                Wait for release of BOR
                                        Sleep        Hibernate                  N/A
                                                                                                    (BORRDY = 1)
                            1            X             Active       Wait for release of BOR
       01                                                                                         Begins immediately
                            0            X           Hibernate          (BORRDY = 1)
       00                   X            X            Disabled                        Begins immediately

FIGURE 6-3:                 BROWN-OUT SITUATIONS

                    VDD
                                                                                                VBOR


                 Internal
                   Reset                                     TPWRT(1)


                    VDD
                                                                                                VBOR


                 Internal                                 < TPWRT
                   Reset                                             TPWRT(1)


                    VDD
                                                                                                VBOR


                 Internal
                   Reset                                             TPWRT(1)


       Note 1:     TPWRT delay depends on PWRTS[1:0] Configuration bits.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 84
                        PIC18(L)F26/27/45/46/47/55/56/57K42
6.3       Register Definitions: BOR Control
REGISTER 6-1:           BORCON: BROWN-OUT RESET CONTROL REGISTER
   R/W-1/u             U-0              U-0             U-0       U-0             U-0          U-0           R-q/u
   SBOREN               —               —               —         —               —                —       BORRDY
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         q = Value depends on condition


bit 7              SBOREN: Software Brown-out Reset Enable bit
                   If BOREN  01:
                   SBOREN is read/write, but has no effect on the BOR.
                   If BOREN = 01:
                   1 = BOR Enabled
                   0 = BOR Disabled
bit 6-1            Unimplemented: Read as ‘0’
bit 0              BORRDY: Brown-out Reset Circuit Ready Status bit
                   1 = The Brown-out Reset Circuit is active and armed
                   0 = The Brown-out Reset Circuit is disabled or is warming up


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 85
                      PIC18(L)F26/27/45/46/47/55/56/57K42
6.4       Low-Power Brown-out Reset                        6.6      Windowed Watchdog Timer
          (LPBOR)                                                   (WWDT) Reset
The Low-Power Brown-out Reset (LPBOR) provides             The Windowed Watchdog Timer generates a Reset if
an additional BOR circuit for low power operation.         the firmware does not issue a CLRWDT instruction
Refer to Figure 6-2 to see how the BOR interacts with      within the time-out period or window set. The TO and
other modules.                                             PD bits in the STATUS register and the RWDT bit in the
The LPBOR is used to monitor the external VDD pin.         PCON0 register are changed to indicate a WWDT
When too low of a voltage is detected, the device is       Reset. The WDTWV bit in the PCON0 register indicates
held in Reset.                                             if the WDT Reset has occurred due to a time out or a
                                                           window violation. See Section 11.0 “Windowed
6.4.1         ENABLING LPBOR                               Watchdog Timer (WWDT)” for more information.
The LPBOR is controlled by the LPBOREN bit of
Configuration Word 2L. When the device is erased, the
                                                           6.7      RESET Instruction
LPBOR module defaults to disabled.                         A RESET instruction will cause a device Reset. The RI
                                                           bit in the PCON0 register will be set to ‘0’. See Table 6-
6.4.1.1        LPBOR Module Output                         3 for default conditions after a RESET instruction has
The output of the LPBOR module is a signal indicating      occurred.
whether or not a Reset is to be asserted. This signal is
OR’d together with the Reset signal of the BOR             6.8      Stack Overflow/Underflow Reset
module to provide the generic BOR signal, which goes
to the PCON0 register and to the power control block.      The device can reset when the Stack Overflows or
                                                           Underflows. The STKOVF or STKUNF bits of the
                                                           PCON0 register indicate the Reset condition. These
6.5       MCLR
                                                           Resets are enabled by setting the STVREN bit in
The MCLR is an optional external input that can reset      Configuration Words. See Section 4.2.5 “Return
the device. The MCLR function is controlled by the         Address Stack” for more information.
MCLRE bit of Configuration Words and the LVP bit of
Configuration Words (Table 6-2). The RMCLR bit in the      6.9      Programming Mode Exit
PCON0 register will be set to ‘0’ if a MCLR Reset has
occurred.                                                  Upon exit of Programming mode, the device will
                                                           behave as if a POR occurred.

TABLE 6-2:         MCLR CONFIGURATION                      6.10     Power-up Timer (PWRT)
      MCLRE              LVP               MCLR
                                                           The Power-up Timer provides a selected time-out
          x                1              Enabled          duration on POR or Brown-out Reset.
          1                0              Enabled          The device is held in Reset as long as PWRT is active.
          0                0              Disabled         The PWRT delay allows additional time for the VDD to
                                                           rise to an acceptable level. The Power-up Timer is
6.5.1         MCLR ENABLED                                 selected by setting the PWRTS[1:0] Configuration bits,
                                                           appropriately.
When MCLR is enabled and the pin is held low, the
device is held in Reset. The MCLR pin is connected to      The Power-up Timer starts after the release of the POR
VDD through an internal weak pull-up.                      and BOR/LPBOR if enabled, as shown in Figure 6-1.
The device has a noise filter in the MCLR Reset path.
The filter will detect and ignore small pulses.
  Note:       An internal Reset event (RESET
              instruction, BOR, WWDT, POR stack),
              does not drive the MCLR pin low.

6.5.2         MCLR DISABLED
When MCLR is disabled, the MCLR pin becomes input-
only and pin functions such as internal weak pull-ups
are under software control. See Section 16.1 “I/O
Priorities” for more information.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 86
                              PIC18(L)F26/27/45/46/47/55/56/57K42
6.11        Start-up Sequence                             The total time-out will vary based on oscillator
                                                          configuration and Power-up Timer configuration. See
Upon the release of a POR or BOR, the following must      Section 7.0 “Oscillator Module (with Fail-Safe
occur before the device will begin executing:             Clock Monitor)” for more information.
1.     Power-up Timer runs to completion (if enabled).    The Power-up Timer and oscillator start-up timer run
2.     Oscillator start-up timer runs to completion (if   independently of MCLR Reset. If MCLR is kept low
       required for selected oscillator source).          long enough, the Power-up Timer and oscillator Start-
3.     MCLR must be released (if enabled).                up Timer will expire. Upon bringing MCLR high, the
                                                          device will begin execution after 10 FOSC cycles (see
                                                          Figure 6-4). This is useful for testing purposes or to
                                                          synchronize more than one device operating in parallel.

FIGURE 6-4:                    RESET START-UP SEQUENCE


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


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 87
                      PIC18(L)F26/27/45/46/47/55/56/57K42
6.11.1      MEMORY EXECUTION VIOLATION
If the CPU executes outside the valid execution area, a
memory execution violation reset occurs.
The invalid execution areas are:
1.   Addresses outside implemented program
     memory (see Table 5-1).
2.   Storage Area Flash (SAF) inside program
     memory, if it is enabled.
When a memory execution violation is generated, flag
MEMV is cleared in PCON1 (Register 6-3) to signal the
cause of Reset. It needs to be set in the user code after
a memory execution violation Reset has occurred to
detect further violation Resets.

6.12     Determining the Cause of a Reset
Upon any Reset, multiple bits in the STATUS and
PCON0 registers are updated to indicate the cause of
the Reset. Table 6-3 shows the Reset conditions of
these registers.

TABLE 6-3:        RESET CONDITION FOR SPECIAL REGISTERS
                                                    Program    STATUS            PCON0            PCON1
                  Condition
                                                    Counter   Register(1,2)      Register         Register
Power-on Reset                                          0     -110 0000        0011 110x         ---- --1-
Brown-out Reset                                         0     -110 0000        0011 11u0         ---- --1-
MCLR Reset during normal operation                      0     -uuu uuuu        uuuu 0uuu         ---- --u-
MCLR Reset during Sleep                                 0     -10u uuuu        uuuu 0uuu         ---- --u-
WWDT Time-out Reset                                     0     -0uu uuuu        uuu0 uuuu         ---- --u-
WWDT Window Violation Reset                             0     -uuu uuuu        uu0u uuuu         ---- --u-
RESET Instruction Executed                              0     -uuu uuuu        uuuu u0uu         ---- --u-
Stack Overflow Reset (STVREN = 1)                       0     -uuu uuuu        1uuu uuuu         ---- --u-
Stack Underflow Reset (STVREN = 1)                      0     -uuu uuuu        u1uu uuuu         ---- --u-
Memory Violation Reset                                  0     -uuu uuuu        uuuu uuuu         ---- --0-
Legend: u = unchanged, x = unknown, — = unimplemented bit, reads as ‘0’.
Note 1: If a Status bit is not implemented, that bit will be read as ‘0’.
     2: Status bits Z, C, DC are reset by POR/BOR, but not defined by the Resets module (Register 4-2).


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 88
                      PIC18(L)F26/27/45/46/47/55/56/57K42
6.13     Power Control (PCON0/PCON1)                The PCON0/1 register bits are shown in Register 6-2
         Register                                   and Register 6-3. Hardware will change the
                                                    corresponding register bit during the Reset process; if
The Power Control (PCON0/PCON1) register contains   the Reset was not caused by the condition, the bit
flag bits to differentiate between a:               remains unchanged (Table 6-3).
• Brown-out Reset (BOR)                             Software may reset the bit to the inactive state after
• Power-on Reset (POR)                              restart (hardware will not reset the bit). Software may
• Reset Instruction Reset (RI)                      also set any PCON0 bit to the active state, so that user
                                                    code may be tested, but no Reset action will be
• MCLR Reset (RMCLR)
                                                    generated.
• Watchdog Timer Reset (RWDT)
• Watchdog Window Violation (WDTWV)
• Stack Underflow Reset (STKUNF)
• Stack Overflow Reset (STKOVF)
• Memory Violation Reset (MEMV)


 2017-2021 Microchip Technology Inc.                                                DS40001919G-page 89
                        PIC18(L)F26/27/45/46/47/55/56/57K42
6.14     Register Definitions: Power Control

REGISTER 6-2:           PCON0: POWER CONTROL REGISTER 0
 R/W/HS-0/q        R/W/HS-0/q    R/W/HC-1/q R/W/HC-1/q R/W/HC-1/q          R/W/HC-1/q     R/W/HC-0/u    R/W/HC-q/u

   STKOVF           STKUNF         WDTWV            RWDT       RMCLR            RI           POR           BOR
bit 7                                                                                                          bit 0


Legend:
HC = Bit is cleared by hardware                             HS = Bit is set by hardware
R = Readable bit                 W = Writable bit           U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown         -m/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared       q = Value depends on condition


bit 7              STKOVF: Stack Overflow Flag bit
                   1 = A Stack Overflow occurred (more CALLs than fit on the stack)
                   0 = A Stack Overflow has not occurred or set to ‘0’ by firmware
bit 6              STKUNF: Stack Underflow Flag bit
                   1 = A Stack Underflow occurred (more RETURNs than CALLs)
                   0 = A Stack Underflow has not occurred or set to ‘0’ by firmware
bit 5              WDTWV: Watchdog Window Violation bit
                   1 = A WDT window violation has not occurred or set to ‘1’ by firmware
                   0 = A CLRWDT instruction was issued when the WDT Reset window was closed (set to ‘0’ in hardware
                       when a WDT window violation Reset occurs)
bit 4              RWDT: WDT Reset Flag bit
                   1 = A WDT overflow/time-out Reset has not occurred or set to ‘1’ by firmware
                   0 = A WDT overflow/time-out Reset has occurred (set to ‘0’ in hardware when a WDT Reset occurs)
bit 3              RMCLR: MCLR Reset Flag bit
                   1 = A MCLR Reset has not occurred or set to ‘1’ by firmware
                   0 = A MCLR Reset has occurred (set to ‘0’ in hardware when a MCLR Reset occurs)
bit 2              RI: RESET Instruction Flag bit
                   1 = A RESET instruction has not been executed or set to ‘1’ by firmware
                   0 = A RESET instruction has been executed (set to ‘0’ in hardware upon executing a RESET
                        instruction)
bit 1              POR: Power-on Reset Status bit
                   1 = No Power-on Reset occurred or set to ‘1’ by firmware
                   0 = A Power-on Reset occurred (set to ‘0’ in hardware when a Power-on Reset occurs)
bit 0              BOR: Brown-out Reset Status bit
                   1 = No Brown-out Reset occurred or set to ‘1’ by firmware
                   0 = A Brown-out Reset occurred (set to ‘0’ in hardware when a Brown-out Reset occurs)


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 90
                            PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 6-3:               PCON1: POWER CONTROL REGISTER 1
        U-0              U-0             U-0              U-0         U-0             U-0        R/W/HC-1/u       U-0

        —                   —            —                —           —                 —           MEMV          —
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                   W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown             -m/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared           q = Value depends on condition


bit 7-2             Unimplemented: Read as ‘0’
bit 1               MEMV: Memory Violation Flag bit
                    1 = No memory violation Reset occurred or set to ‘1’ by firmware
                    0 = A memory violation Reset occurred (set to ‘0’ in hardware when a Memory Violation occurs)
bit 0               Unimplemented: Read as ‘0’


TABLE 6-4:           SUMMARY OF REGISTERS ASSOCIATED WITH RESETS
                                                                                                                 Register
   Name             Bit 7        Bit 6         Bit 5      Bit 4     Bit 3       Bit 2       Bit 1       Bit 0
                                                                                                                 on Page
BORCON             SBOREN         —             —           —         —          —           —         BORRDY       85
PCON0              STKOVF       STKUNF    WDTWV           RWDT     RMCLR         RI         POR         BOR         90
PCON1                —            —             —           —         —          —          MEMV         —          91
Legend: — = unimplemented location, read as ‘0’. Shaded cells are not used by Resets.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 91
