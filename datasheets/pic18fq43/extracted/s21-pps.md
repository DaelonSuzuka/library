                                                                                                             PIC18F27/47/57Q43
                                                                                               PPS - Peripheral Pin Select Module


21.    PPS - Peripheral Pin Select Module
21.1   Overview
             Filename:             PPS Block Diagram.vsdx
                Title:
       The Peripheral   Pin Select3/26/2019
                Last Edit:
                                    (PPS) module connects peripheral inputs and outputs to the device I/O
       pins. Only digital
                First Used:signals are included in the selections.
                Notes:

                    Important: All analog inputs and outputs remain fixed to their assigned pins and
                    cannot be changed through PPS.


       Input and output selections are independent as shown in the figure below.

       Figure 21-1. PPS Block Diagram


                                    abcPPS
                                                                                           RA0PPS

                   RA0
                                                         Peripheral abc
                                                                                                           RA0


                                                                                                            Rxy
                                                         Peripheral xyz
                    Rxy

                                        xyzPPS                                             RxyPPS


                      Input selections                                                 Output selections


21.2   PPS Inputs
       Each digital peripheral has a dedicated PPS Peripheral Input Selection (xxxPPS) register with which
       the input pin to the peripheral is selected. Devices that have 20 leads or less (8/14/16/20) allow PPS
       routing to any I/O pin, while devices with 28 leads or more allow PPS routing to I/Os contained within
       two ports (see the table below).


                    Important: The notation “xxx” in the generic register name is a placeholder for
                    the peripheral identifier. For example, xxx = T0CKI for the T0CKIPPS register.


       Multiple peripherals can operate from the same source simultaneously. Port reads always return the
       pin level regardless of peripheral PPS selection. If a pin also has analog functions associated, the
       ANSEL bit for that pin must be cleared to enable the digital input buffer.


--- p341 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            PPS - Peripheral Pin Select Module

Table 21-1. PPS Input Selection Table
                                         Default Pin                               Available Input Port
                          PPS Input                      Register Reset
Peripheral                               Selection at
                           Register                       Value at POR 28-Pin Devices 40-Pin Devices 48-Pin Devices
                                             POR
Interrupt 0                INT0PPS           RB0           'b001 000         A     B    —     A B — — — A B ————
Interrupt 1               INT1PPS            RB1           'b001 001         A    B     —    A B — — — — B — D ——
Interrupt 2               INT2PPS            RB2           'b001 010         A    B     —    A B — — — — B ——— F
Timer0 Clock              T0CKIPPS           RA4           'b000 100         A    B     —    A B — — — A ———— F
Timer1 Clock              T1CKIPPS           RC0           'b010 000         A    —     C    A — C — — —— C — E —
Timer1 Gate                T1GPPS            RB5           'b001 101         —    B     C    — B C — — — B C ———
Timer3 Clock              T3CKIPPS           RC0           'b010 000         —    B     C    — B C — — —— C — E —
Timer3 Gate                T3GPPS            RC0           'b010 000         A    —     C    A — C — — A — C ———
Timer5 Clock              T5CKIPPS           RC2           'b010 010         A    —     C    A — C — — —— C — E —
Timer5 Gate                T5GPPS            RB4           'b001 100         —    B     C    — B — D — — B — D ——
Timer2 Input              T2INPPS            RC3           'b010 011         A    —     C    A — C — — A — C ———
Timer4 Input              T4INPPS            RC5           'b010 101         —    B     C    — B C — — — B C ———
Timer6 Input              T6INPPS            RB7           'b001 111         —    B     C    — B — D — — B — D ——
CCP1                      CCP1PPS            RC2           'b010 010         —    B     C    — B C — — —— C —— F
CCP2                      CCP2PPS            RC1           'b010 001         —    B     C    — B C — — —— C —— F
CCP3                      CCP3PPS            RB5           'b001 101         —    B     C    — B — D — — B — D ——
SMT1 Window             SMT1WINPPS           RC0           'b010 000         —    B     C    — B C — — —— C —— F
SMT1 Signal             SMT1SIGPPS           RC1           'b010 001         —    B     C    — B C — — —— C —— F
PWM Input 0              PWMIN0PPS           RC2           'b010 010         —    B     C    — B C — — —— C —— F
PWM Input 1              PWMIN1PPS           RC6           'b010 110         A    —     C    A — — — E A ——— E —
PWM1 External           PWM1ERSPPS           RC3           'b010 011         A    —     C    A — C — — A — C —  —
Reset Source
PWM2 External           PWM2ERSPPS           RC5           'b010 101         A    —     C     A — C — — —— C — E —
Reset Source
PWM3 External           PWM3ERSPPS           RB7           'b001 111         —     B    C    — B — D — — B — D ——
Reset Source
CWG1                      CWG1PPS            RB0           'b001 000         —    B     C    — B — D — — B — D ——
CWG2                      CWG2PPS            RB1           'b001 001         —    B     C    — B — D — — B — D ——
CWG3                      CWG3PPS            RB2           'b001 010         —    B     C    — B — D — — B — D ——
DSM1 Carrier Low         MD1CARLPPS          RA3           'b000 011         A    —     C    A — — D — A —— D ——
DSM1 Carrier High       MD1CARHPPS           RA4           'b000 100         A    —     C    A — — D — A —— D ——
DSM1 Source             MD1SRCPPS            RA5           'b000 101         A    —     C    A — — D — A —— D ——
CLCx Input 1             CLCIN0PPS           RA0           'b000 000         A    —     C    A — C — — A — C ———
CLCx Input 2             CLCIN1PPS           RA1           'b000 001         A    —     C    A — C — — A — C ———
CLCx Input 3             CLCIN2PPS           RB6           'b001 110         —    B     C    — B — D — — B — D ——
CLCx Input 4             CLCIN3PPS           RB7           'b001 111         —    B     C    — B — D — — B — D ——
CLCx Input 5             CLCIN4PPS           RA0           'b000 000         A    —     C    A — C — — A — C ———
CLCx Input 6             CLCIN5PPS           RA1           'b000 001         A    —     C    A — C — — A — C ———
CLCx Input 7             CLCIN6PPS           RB6           'b001 110         —    B     C    — B — D — — B — D ——
CLCx Input 8             CLCIN7PPS           RB7           'b001 111         —    B     C    — B — D — — B — D ——
ADC Conversion           ADACTPPS            RB4           'b001 100         —    B     C    — B — D — — B — D ——
Trigger
SPI1 Clock                SPI1SCKPPS         RC3           'b010 011         —    B     C    — B C — — — B C ———
SPI1 Data                 SPI1SDIPPS         RC4           'b010 100         —    B     C    — B C — — — B C ———
SPI1 Client Select         SPI1SSPPS         RA5           'b000 101         A    —     C    A — — D — A —— D ——


--- p342 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                PPS - Peripheral Pin Select Module

  ...........continued
                                             Default Pin                               Available Input Port
                              PPS Input                      Register Reset
  Peripheral                                 Selection at
                               Register                       Value at POR 28-Pin Devices 40-Pin Devices 48-Pin Devices
                                                 POR
  SPI2 Clock                 SPI2SCKPPS          RB3           'b001 011         —     B    C    — B — D — — B — D ——
  SPI2 Data                   SPI2SDIPPS         RB2           'b001 010         —    B     C    — B — D — — B — D ——
  SPI2 Client Select          SPI2SSPPS          RA4           'b000 100         A    —     C    A — — D — A —— D ——
  I2C1 Clock                I2C1SCLPPS(1)        RC3           'b010 011         —    B     C    — B C — — — B C ———
  I2C1 Data                 I2C1SDAPPS(1)        RC4           'b010 100         —    B     C    — B C — — — B C ———
  UART1 Receive                U1RXPPS           RC7           'b010 111         —    B     C    — B C — — —— C —— F
  UART1 Clear to Send         U1CTSPPS           RC6           'b010 110         —    B     C    — B C — — —— C —— F
  UART2 Receive                U2RXPPS           RB7           'b001 111         —    B     C    — B — D — — B — D ——
  UART2 Clear to Send         U2CTSPPS           RB6           'b001 110         —    B     C    — B — D — — B — D ——
  UART3 Receive                U3RXPPS           RA7           'b000 111         A    B     —    A B — — — A ———— F
  UART3 Clear to Send         U3CTSPPS           RA6           'b000 110         A    B     —    A B — — — A ———— F
  UART4 Receive                U4RXPPS           RB5           'b001 101         —    B     C    — B — D — — B — D ——
  UART4 Clear to Send         U4CTSPPS           RB4           'b001 100         —    B     C    — B — D — — B — D ——
  UART5 Receive                U5RXPPS           RA5           'b000 101         A    —     C    A — C — — A ———— F
  UART5 Clear to Send         U5CTSPPS           RA4           'b000 100         A    —     C    A — C — — A ———— F

        Note:
        1. Bidirectional pin. The corresponding output must select the same pin.

21.3    PPS Outputs
        Each digital peripheral has a dedicated Pin Rxy Output Source Selection (RxyPPS) register with which
        the pin output source is selected. With few exceptions, the port TRIS control associated with that pin
        retains control over the pin output driver. Peripherals that control the pin output driver as part of
        the peripheral operation will override the TRIS control as needed. The I2C module is an example of
        such a peripheral.


                         Important: The notation ‘Rxy’ is a placeholder for the pin identifier. The ‘x’ holds
                         the place of the PORT letter and the ‘y’ holds the place of the bit number. For
                         example, Rxy = RA0 for the RA0PPS register.


        The table below shows the output codes for each peripheral, as well as the available Port selections.

        Table 21-2. PPS Output Selection Table
                                                                             Available Output Ports
         RxyPPS                  Output Source
                                                       28-Pin Devices           40-Pin Devices      48-Pin Devices
         0x45                       ADGRDB             A     —      C         A — C — — A — — — — F
         0x44                       ADGRDA             A     —      C         A — C — — A — — — — F
         0x43                        DSM1              A     —      C         A — — D — A — — D — —
         0x42                         CLKR             —      B     C         — B C — — — B — — E —
         0x41                         NCO3             —      B     C         — B — — E — B — — E —
         0x40                         NCO2             —      B     C         — B — D — — B — D — —
         0x3F                         NCO1             A     —      C         A — — D — A — — D — —
         0x3E - 0x3A                Reserved           —     —      —         — — — — — — — — — — —
         0x39                         TMR0             —      B     C         — B C — — — — C — — F
         0x38                      I2C1 SDA(1)         —      B     C         — B C — — — B C — — —
         0x37                      I2C1 SCL(1)         —      B     C         — B C — — — B C — — —


--- p343 ---
                                                                                                PIC18F27/47/57Q43
                                                                                  PPS - Peripheral Pin Select Module

...........continued
                                                                     Available Output Ports
RxyPPS                 Output Source
                                             28-Pin Devices             40-Pin Devices      48-Pin Devices
0x36                      SPI2 SS            A     —      C           A — — D — A — — D — —
0x35                     SPI2 SDO            —      B     C           — B — D — — B — D — —
0x34                      SPI2 SCK           —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x33                       SPI1 SS           A        —          C    A   —   —   D   —   A   —   —    D   —   —
0x32                      SPI1 SDO           —        B          C    —   B   C   —   —   —   B   C    —   —   —
0x31                      SPI1 SCK           —        B          C    —   B   C   —   —   —   B   C    —   —   —
0x30                       C2OUT             A        —          C    A   —   —   —   E   A   —   —    —   E   —
0x2F                       C1OUT             A        —          C    A   —   —   D   —   A   —   —    D   —   —
0x2E                     UART5 RTS           —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x2D                    UART5 TXDE           —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x2C                     UART5 TX            —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x2B                     UART4 RTS           A        B          —    A   —   —   D   —   A   —   —    D   —   —
0x2A                    UART4 TXDE           A        B          —    A   —   —   D   —   A   —   —    D   —   —
0x29                     UART4 TX            A        B          —    A   —   —   D   —   A   —   —    D   —   —
0x28                     UART3 RTS           A        B          —    A   B   —   —   —   A   —   —    —   —   F
0x27                    UART3 TXDE           A        B          —    A   B   —   —   —   A   —   —    —   —   F
0x26                     UART3 TX            A        B          —    A   B   —   —   —   A   —   —    —   —   F
0x25                     UART2 RTS           —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x24                    UART2 TXDE           —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x23                     UART2 TX            —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x22                     UART1 RTS           —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x21                    UART1 TXDE           —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x20                     UART1 TX            —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x1F                     Reserved            —        —          —    —   —   —   —   —   —   —   —    —   —   —
0x1E                     Reserved            —        —          —    —   —   —   —   —   —   —   —    —   —   —
0x1D                   PWM3S1P2_OUT          —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x1C                   PWM3S1P1_OUT          —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x1B                   PWM2S1P2_OUT          —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x1A                   PWM2S1P1_OUT          —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x19                   PWM1S1P2_OUT          —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x18                   PWM1S1P1_OUT          —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x17                       CCP3              —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x16                       CCP2              —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x15                       CCP1              —        B          C    —   B   C   —   —   —   —   C    —   —   F
0x14                      CWG3D              A        —          C    A   —   —   D   —   A   —   —    D   —   —
0x13                      CWG3C              A        —          C    A   —   —   D   —   A   —   —    D   —   —
0x12                      CWG3B              A        —          C    A   —   —   —   E   A   —   —    —   E   —
0x11                      CWG3A              —        B          C    —   B   C   —   —   —   B   C    —   —   —
0x10                      CWG2D              —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x0F                      CWG2C              —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x0E                      CWG2B              —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x0D                      CWG2A              —        B          C    —   B   C   —   —   —   B   C    —   —   —
0x0C                      CWG1D              —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x0B                      CWG1C              —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x0A                      CWG1B              —        B          C    —   B   —   D   —   —   B   —    D   —   —
0x09                      CWG1A              —        B          C    —   B   C   —   —   —   B   C    —   —   —


--- p344 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                        PPS - Peripheral Pin Select Module

       ...........continued
                                                                           Available Output Ports
       RxyPPS                 Output Source
                                                   28-Pin Devices             40-Pin Devices      48-Pin Devices
       0x08                     CLC8OUT            —      B     C           — B — D — — B — D — —
       0x07                     CLC7OUT            —      B     C           — B — D — — B — D — —
       0x06                     CLC6OUT            A        —          C    A   —   C   —   — A — — —            — F
       0x05                     CLC5OUT            A        —          C    A   —   C   —   — A — — —            — F
       0x04                     CLC4OUT            —        B          C    —   B   —   D   — — B — D            — —
       0x03                     CLC3OUT            —        B          C    —   B   —   D   — — B — D            — —
       0x02                     CLC2OUT            A        —          C    A   —   C   —   — A — — —            — F
       0x01                     CLC1OUT            A        —          C    A   —   C   —   — A — — —            — F
       0x00                      LATxy             A        B          C    A   B   C   D   E A B C D            E F

       Note:
       1. Bidirectional pin. The corresponding input must select the same pin.

21.4   Bidirectional Pins
       PPS selections for peripherals with bidirectional signals on a single pin must be made so that the
       PPS input and PPS output select the same pin. The I2C Serial Clock (SCL) and Serial Data (SDA) are
       examples of such pins.


                    Important: The I2C default pins and a limited number of other alternate pins
                    are I2C and SMBus compatible. SDA and SCL signals can be routed to any pin;
                    however, pins without I2C compatibility will operate at standard TTL/ST logic levels
                    as selected by the port’s INLVL register.


21.5   PPS Lock
       The PPS module provides an extra layer of protection to prevent inadvertent changes to the PPS
       selection registers. The PPSLOCKED bit is used in combination with specific code execution blocks to
       lock/unlock the PPS selection registers.


                    Important: The PPSLOCKED bit is clear by default (PPSLOCKED = 0), which allows
                    the PPS selection registers to be modified without an unlock sequence.


       PPS selection registers are locked when the PPSLOCKED bit is set (PPSLOCKED = 1). Setting the
       PPSLOCKED bit requires a specific lock sequence as shown in the examples below in both C and
       assembly languages.
       PPS selection registers are unlocked when the PPSLOCKED bit is clear (PPSLOCKED = 0). Clearing the
       PPSLOCKED bit requires a specific unlock sequence as shown in the examples below in both C and
       assembly languages.


                    Important: All interrupts must be disabled before starting the lock/unlock
                    sequence to ensure proper execution.


                Example 21-1. PPS Lock Sequence (assembly language)

                  ; suspend interrupts
                     BCF      INTCON0,GIE
                     BANKSEL PPSLOCK


--- p345 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                      PPS - Peripheral Pin Select Module
                 ; required sequence, next 5 instructions
                    MOVLW    0x55
                    MOVWF    PPSLOCK
                    MOVLW    0xAA
                    MOVWF    PPSLOCK
                 ; Set PPSLOCKED bit
                    BSF      PPSLOCK,PPSLOCKED
                 ; restore interrupts
                    BSF      INTCON0,GIE


              Example 21-2. PPS Lock Sequence (C language)

                INTCON0bits.GIE = 0;           //Suspend interrupts
                PPSLOCK = 0x55;                //Required sequence
                PPSLOCK = 0xAA;                //Required sequence
                PPSLOCKbits.PPSLOCKED = 1;     //Set PPSLOCKED bit
                INTCON0bits.GIE = 1;           //Restore interrupts


              Example 21-3. PPS Unlock Sequence (assembly language)

                 ; suspend interrupts
                    BCF      INTCON0,GIE
                    BANKSEL PPSLOCK
                 ; required sequence, next 5 instructions
                    MOVLW    0x55
                    MOVWF    PPSLOCK
                    MOVLW    0xAA
                    MOVWF    PPSLOCK
                 ; Clear PPSLOCKED bit
                    BCF      PPSLOCK,PPSLOCKED
                 ; restore interrupts
                    BSF      INTCON0,GIE


              Example 21-4. PPS Unlock Sequence (C language)

                INTCON0bits.GIE = 0;           //Suspend interrupts
                PPSLOCK = 0x55;                //Required sequence
                PPSLOCK = 0xAA;                //Required sequence
                PPSLOCKbits.PPSLOCKED = 0;     //Clear PPSLOCKED bit
                INTCON0bits.GIE = 1;           //Restore interrupts


21.5.1 PPS One-Way Lock
       The PPS1WAY Configuration bit can also be used to prevent inadvertent modification to the PPS
       selection registers.
       When the PPS1WAY bit is set (PPS1WAY = 1), the PPSLOCKED bit can only be set one time after a
       device Reset. Once the PPSLOCKED bit has been set, it cannot be cleared again unless a device Reset
       is executed.
       When the PPS1WAY bit is clear (PPS1WAY = 0), the PPSLOCKED bit can be set or cleared as needed;
       however, the PPS lock/unlock sequences must be executed.

21.6   Operation During Sleep
       PPS input and output selections are unaffected by Sleep.

21.7   Effects of a Reset
       A device Power-on Reset (POR) or Brown-out Reset (BOR) returns all PPS input selection registers
       to their default values and clears all PPS output selection registers. All other Resets leave the


--- p346 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                      PPS - Peripheral Pin Select Module

       selections unchanged. Default input selections are shown in the PPS input register details table. The
       PPSLOCKED bit is cleared in all Reset conditions.

21.8   Register Definitions: Peripheral Pin Select (PPS)


--- p347 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                    PPS - Peripheral Pin Select Module

21.8.1 xxxPPS

            Name:        xxxPPS

            Peripheral Input Selection Register

      Bit           7            6              5             4                    3            2           1               0
                                                           PORT[2:0]                                     PIN[2:0]
  Access                                      R/W            R/W                  R/W      R/W             R/W             R/W
   Reset                                       m              m                    m        m               m               m

Bits 5:3 – PORT[2:0] Peripheral Input PORT Selection(1)
          See the PPS Input Selection Table for the list of available Ports and default pin locations.
                               PORT                                                      Selection
                                101                                                       PORTF
                                100                                                       PORTE
                                011                                                       PORTD
                                010                                                       PORTC
                                001                                                       PORTB
                                000                                                       PORTA

            Reset States: POR = mmm
                          All other Resets = uuu

Bits 2:0 – PIN[2:0] Peripheral Input PORT Pin Selection(2)
          Reset States: POR = mmm
                        All other Resets = uuu
            Value       Description
            111         Peripheral input is from PORTx Pin 7 (Rx7)
            110         Peripheral input is from PORTx Pin 6 (Rx6)
            101         Peripheral input is from PORTx Pin 5 (Rx5)
            100         Peripheral input is from PORTx Pin 4 (Rx4)
            011         Peripheral input is from PORTx Pin 3 (Rx3)
            010         Peripheral input is from PORTx Pin 2 (Rx2)
            001         Peripheral input is from PORTx Pin 1 (Rx1)
            000         Peripheral input is from PORTx Pin 0 (Rx0)

            Notes:
            1. The Reset value ‘m’ is determined by device default locations for that input.
            2. Refer to the “Pin Allocation Table” for details about available pins per port.


--- p348 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              PPS - Peripheral Pin Select Module

21.8.2 RxyPPS

            Name:      RxyPPS

            Pin Rxy Output Source Selection Register

      Bit        7           6            5              4               3                2            1              0
                                                                     RxyPPS[6:0]
  Access                    R/W          R/W           R/W              R/W          R/W             R/W             R/W
   Reset                     0            0             0                0            0               0               0

Bits 6:0 – RxyPPS[6:0] Pin Rxy Output Source Selection
          See the PPS Output Selection Table for the list of RxyPPS Output Source codes
          Reset States: POR = 0000000
                        All other Resets = uuuuuuu


--- p349 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                    PPS - Peripheral Pin Select Module

21.8.3 PPSLOCK

            Name:        PPSLOCK

            PPS Lock Register

      Bit           7           6               5              4                  3            2             1               0
                                                                                                                         PPSLOCKED
  Access                                                                                                                    R/W
   Reset                                                                                                                     0

Bit 0 – PPSLOCKED PPS Locked
          Reset States: POR = 0
                        All other Resets = 0
            Value       Description
            1           PPS is locked. PPS selections cannot be changed. Writes to any PPS register are ignored.
            0           PPS is not locked. PPS selections can be changed but may require the PPS lock/unlock sequence.


--- p350 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                        PPS - Peripheral Pin Select Module

21.9      Register Summary - Peripheral Pin Select Module
Address     Name      Bit Pos.   7        6           5             4          3          2           1              0
 0x0200    PPSLOCK      7:0                                                                                      PPSLOCKED
 0x0201     RA0PPS      7:0                                              RA0PPS[6:0]
 0x0202     RA1PPS      7:0                                              RA1PPS[6:0]
0x0203      RA2PPS      7:0                                              RA2PPS[6:0]
0x0204      RA3PPS      7:0                                              RA3PPS[6:0]
0x0205      RA4PPS      7:0                                              RA4PPS[6:0]
0x0206      RA5PPS      7:0                                              RA5PPS[6:0]
0x0207      RA6PPS      7:0                                              RA6PPS[6:0]
0x0208      RA7PPS      7:0                                              RA7PPS[6:0]
0x0209      RB0PPS      7:0                                              RB0PPS[6:0]
0x020A      RB1PPS      7:0                                              RB1PPS[6:0]
0x020B      RB2PPS      7:0                                              RB2PPS[6:0]
0x020C      RB3PPS      7:0                                              RB3PPS[6:0]
0x020D      RB4PPS      7:0                                              RB4PPS[6:0]
0x020E      RB5PPS      7:0                                              RB5PPS[6:0]
0x020F      RB6PPS      7:0                                              RB6PPS[6:0]
0x0210      RB7PPS      7:0                                              RB7PPS[6:0]
0x0211      RC0PPS      7:0                                              RC0PPS[6:0]
0x0212      RC1PPS      7:0                                              RC1PPS[6:0]
0x0213      RC2PPS      7:0                                              RC2PPS[6:0]
0x0214      RC3PPS      7:0                                              RC3PPS[6:0]
0x0215      RC4PPS      7:0                                              RC4PPS[6:0]
0x0216      RC5PPS      7:0                                              RC5PPS[6:0]
0x0217      RC6PPS      7:0                                              RC6PPS[6:0]
0x0218      RC7PPS      7:0                                              RC7PPS[6:0]
0x0219      RD0PPS      7:0                                              RD0PPS[6:0]
0x021A      RD1PPS      7:0                                              RD1PPS[6:0]
0x021B      RD2PPS      7:0                                              RD2PPS[6:0]
0x021C      RD3PPS      7:0                                              RD3PPS[6:0]
0x021D      RD4PPS      7:0                                              RD4PPS[6:0]
0x021E      RD5PPS      7:0                                              RD5PPS[6:0]
0x021F      RD6PPS      7:0                                              RD6PPS[6:0]
0x0220      RD7PPS      7:0                                              RD7PPS[6:0]
0x0221      RE0PPS      7:0                                              RE0PPS[6:0]
0x0222      RE1PPS      7:0                                              RE1PPS[6:0]
0x0223      RE2PPS      7:0                                              RE2PPS[6:0]
0x0224
  ...      Reserved
0x0228
0x0229      RF0PPS      7:0                                               RF0PPS[6:0]
0x022A      RF1PPS      7:0                                               RF1PPS[6:0]
0x022B      RF2PPS      7:0                                               RF2PPS[6:0]
0x022C      RF3PPS      7:0                                               RF3PPS[6:0]
0x022D      RF4PPS      7:0                                               RF4PPS[6:0]
0x022E      RF5PPS      7:0                                               RF5PPS[6:0]
0x022F      RF6PPS      7:0                                               RF6PPS[6:0]
0x0230      RF7PPS      7:0                                               RF7PPS[6:0]
0x0231
  ...      Reserved
0x023D
0x023E     INT0PPS      7:0                                                 PORT                   PIN[2:0]
0x023F     INT1PPS      7:0                                         PORT[1:0]                      PIN[2:0]
0x0240     INT2PPS      7:0                                   PORT[2:0]                            PIN[2:0]
0x0241     T0CKIPPS     7:0                                   PORT[2:0]                            PIN[2:0]
0x0242     T1CKIPPS     7:0                                   PORT[2:0]                            PIN[2:0]
0x0243      T1GPPS      7:0                                         PORT[1:0]                      PIN[2:0]
0x0244     T3CKIPPS     7:0                                   PORT[2:0]                            PIN[2:0]
0x0245      T3GPPS      7:0                                         PORT[1:0]                      PIN[2:0]
0x0246     T5CKIPPS     7:0                                   PORT[2:0]                            PIN[2:0]


--- p351 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                 PPS - Peripheral Pin Select Module
...........continued
 Address               Name    Bit Pos.   7        6           5             4               3     2           1              0
  0x0247           T5GPPS        7:0                                             PORT[1:0]                  PIN[2:0]
  0x0248           T2INPPS       7:0                                             PORT[1:0]                  PIN[2:0]
  0x0249           T4INPPS       7:0                                             PORT[1:0]                  PIN[2:0]
  0x024A           T6INPPS       7:0                                             PORT[1:0]                  PIN[2:0]
  0x024B
    ...           Reserved
  0x024E
  0x024F           CCP1PPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0250           CCP2PPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0251           CCP3PPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x0252           Reserved
  0x0253        PWM1ERSPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x0254        PWM2ERSPPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0255        PWM3ERSPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x0256           Reserved
  0x0257         PWMIN0PPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0258         PWMIN1PPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0259        SMT1WINPPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x025A        SMT1SIGPPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x025B           CWG1PPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x025C           CWG2PPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x025D           CWG3PPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x025E        MD1CARLPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x025F        MD1CARHPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x0260         MD1SRCPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x0261          CLCIN0PPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0262          CLCIN1PPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0263          CLCIN2PPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0264          CLCIN3PPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0265          CLCIN4PPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0266          CLCIN5PPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0267          CLCIN6PPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0268          CLCIN7PPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0269          ADACTPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x026A         SPI1SCKPPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x026B          SPI1SDIPPS     7:0                                         PORT[1:0]                      PIN[2:0]
  0x026C          SPI1SSPPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x026D         SPI2SCKPPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x026E          SPI2SDIPPS     7:0                                         PORT[1:0]                      PIN[2:0]
  0x026F          SPI2SSPPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0270         I2C1SDAPPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0271         I2C1SCLPPS      7:0                                         PORT[1:0]                      PIN[2:0]
  0x0272           U1RXPPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0273          U1CTSPPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0274           U2RXPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x0275          U2CTSPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x0276           U3RXPPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0277          U3CTSPPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x0278           U4RXPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x0279          U4CTSPPS       7:0                                         PORT[1:0]                      PIN[2:0]
  0x027A           U5RXPPS       7:0                                   PORT[2:0]                            PIN[2:0]
  0x027B          U5CTSPPS       7:0                                   PORT[2:0]                            PIN[2:0]


--- p352 ---
