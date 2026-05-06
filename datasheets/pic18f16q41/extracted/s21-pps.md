21.    PPS - Peripheral Pin Select Module
21.1   Overview
             Filename:           PPS Block Diagram.vsdx
       The Peripheral
                Title:    Pin Select (PPS) module connects peripheral inputs and outputs to the device I/O
       pins. Only digital
                Last   Edit: signals 3/26/2019
                                     are included in the selections.
                First Used:
                Notes:
                    Important: All analog inputs and outputs remain fixed to their assigned pins and cannot
                    be changed through PPS.


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


                       Input selections                                                Output selections


21.2   PPS Inputs
       Each digital peripheral has a dedicated PPS Peripheral Input Selection (xxxPPS) register with which
       the input pin to the peripheral is selected. Devices that have 20 leads or less (8/14/16/20) allow PPS
       routing to any I/O pin, while devices with 28 leads or more allow PPS routing to I/Os contained within
       two ports (see the table below).


                    Important: The notation “xxx” in the generic register name is a placeholder for the
                    peripheral identifier. For example, xxx = T0CKI for the T0CKIPPS register.


       Multiple peripherals can operate from the same source simultaneously. Port reads always return the
       pin level regardless of peripheral PPS selection. If a pin also has analog functions associated, the
       ANSEL bit for that pin must be cleared to enable the digital input buffer.


--- p321 ---
Table 21-1. PPS Input Selection Table
  Peripheral       PPS Input               14-Pin Devices                             20-Pin Devices
                    Register       Default   Register    Available            Default   Register    Available
                                     Pin      Reset     Input Port              Pin      Reset     Input Port
                                  Selection Value at                         Selection Value at
                                   at POR      POR                            at POR      POR
  Interrupt 0      INT0PPS           RA2    ‘b000 010 A     —     C             RC0    ‘b010 000 A     B     C
  Interrupt 1      INT1PPS           RA4    ‘b000 100 A     —     C             RC1    ‘b010 001 A     B     C
  Interrupt 2      INT2PPS           RA5    ‘b000 101 A     —     C             RC2    ‘b010 010 A     B     C
 Timer0 Clock      T0CKIPPS          RA2    ‘b000 010 A     —     C             RC5    ‘b010 101 A     B     C
 Timer1 Clock      T1CKIPPS          RA5    ‘b000 101 A     —     C             RC6    ‘b010 110 A     B     C
 Timer1 Gate        T1GPPS           RA4    ‘b000 100 A     —     C             RA4    ‘b000 100 A     B     C
 Timer3 Clock      T3CKIPPS          RC5    ‘b010 101 A     —     C             RC5    ‘b010 101 A     B     C
 Timer3 Gate        T3GPPS           RC4    ‘b010  100  A   —     C             RC4    ‘b010  100  A   B     C
 Timer2 Input      T2INPPS           RA5    ‘b000 101 A     —     C             RA5    ‘b000 101 A     B     C
 Timer4 Input      T4INPPS           RC1    ‘b010 001 A     —     C             RC1    ‘b010 001 A     B     C
     CCP1          CCP1PPS           RC5    ‘b010 101 A     —     C             RC5    ‘b010 101 A     B     C
SMT1 Window      SMT1WINPPS          RA5    ‘b000 101 A     —     C             RA5    ‘b000 101 A     B     C
 SMT1 Signal     SMT1SIGPPS          RC0    ‘b010 000 A     —     C             RA4    ‘b000 100 A     B     C
 PWM Input 0      PWMIN0PPS          RC5    ‘b010 101 A     —     C             RC5    ‘b010 101 A     B     C
 PWM Input 1      PWMIN1PPS          RC3    ‘b010 011 A     —     C             RC3    ‘b010 011 A     B     C
    PWM1         PWM1ERSPPS          RA5    ‘b000  101  A   —     C             RA5    ‘b000  101  A   B     C
External Reset
    Source
    PWM2         PWM2ERSPPS             RC1   ‘b010 001      A    —     C          RC1     ‘b010 001       A    B     C
External Reset
    Source
    PWM3         PWM3ERSPPS             RC2   ‘b010 010      A    —     C          RC2     ‘b010 010       A    B     C
External Reset
    Source
     CWG1         CWG1PPS               RA2   ‘b000 010      A    —     C          RA2     ‘b000 010       A    B     C
DSM1 Carrier     MD1CARLPPS             RC2   ‘b010 010      A    —     C          RC2     ‘b010 010       A    B     C
      Low
DSM1 Carrier     MD1CARHPPS             RC5   ‘b010 101      A    —     C          RC5     ‘b010 101       A    B     C
      High
 DSM1 Source      MD1SRCPPS             RA1   ‘b000 001      A    —     C          RA1     ‘b000 001       A    B     C
 CLCx Input 1     CLCIN0PPS             RC3   ‘b010 011      A    —     C          RA2     ‘b000 010       A    B     C
 CLCx Input 2     CLCIN1PPS             RC4   ‘b010 100      A    —     C          RC3     ‘b010 011       A    B     C
 CLCx Input 3     CLCIN2PPS             RC1   ‘b010 001      A    —     C          RB4     ‘b001 100       A    B     C
 CLCx Input 4     CLCIN3PPS             RA4   ‘b000 100      A    —     C          RB5     ‘b001 101       A    B     C
      ADC         ADACTPPS              RC2   ‘b010 010      A    —     C          RC2     ‘b010 010       A    B     C
  Conversion
    Trigger
  SPI1 Clock      SPI1SCKPPS            RC0   ‘b010 000      A    —     C          RB6     ‘b001 110       A    B     C
   SPI1 Data      SPI1SDIPPS            RC1   ‘b010 001      A    —     C          RB4     ‘b001 100       A    B     C
  SPI1 Client      SPI1SSPPS            RC3   ‘b010 011      A    —     C          RC6     ‘b010 110       A    B     C
     Select
  SPI2 Clock      SPI2SCKPPS            RC4   ‘b010 100      A    —     C          RB7     ‘b001 111       A    B     C
   SPI2 Data      SPI2SDIPPS            RC5   ‘b010 101      A    —     C          RB5     ‘b001 101       A    B     C


--- p322 ---
       ...........continued
         Peripheral        PPS Input                 14-Pin Devices                               20-Pin Devices
                            Register      Default     Register     Available         Default       Register     Available
                                            Pin         Reset     Input Port           Pin           Reset     Input Port
                                         Selection    Value at                      Selection      Value at
                                          at POR         POR                         at POR           POR
         SPI2 Client       SPI2SSPPS        RA0      ‘b000 000 A      —     C             RA1     ‘b000 001 A      B     C
           Select
         I2C1 Clock  I2C1SCLPPS(1)          RC0      ‘b010 000      A    —     C          RB6     ‘b001 110       A    B       C
          I2C1 Data  I2C1SDAPPS(1)          RC1      ‘b010 001      A    —     C          RB4     ‘b001 100       A    B       C
       UART1 Receive    U1RXPPS             RC5      ‘b010 101      A    —     C          RB5     ‘b001 101       A    B       C
        UART1 Clear    U1CTSPPS             RC4      ‘b010 100      A    —     C          RB7     ‘b001 111       A    B       C
           to Send
       UART2 Receive       U2RXPPS          RC1      ‘b010 001      A    —     C          RC1     ‘b010 001       A    B       C
        UART2 Clear        U2CTSPPS         RC2      ‘b010 010      A    —     C          RC2     ‘b010 010       A    B       C
          to Send
       UART3 Receive       U3RXPPS          RA4      ‘b000 100      A    —     C          RC3     ‘b010 011       A    B       C
        UART3 Clear        U3CTSPPS         RA5      ‘b000 101      A    —     C          RC5     ‘b010 101       A    B       C
          to Send

       Note:
       1. Bidirectional pin. The corresponding output must select the same pin.

21.3   PPS Outputs
       Each digital peripheral has a dedicated Pin Rxy Output Source Selection (RxyPPS) register with which
       the pin output source is selected. With few exceptions, the port TRIS control associated with that pin
       retains control over the pin output driver. Peripherals that control the pin output driver as part of
       the peripheral operation will override the TRIS control as needed. The I2C module is an example of
       such a peripheral.


                       Important: The notation ‘Rxy’ is a placeholder for the pin identifier. The ‘x’ holds the place
                       of the PORT letter and the ‘y’ holds the place of the bit number. For example, Rxy = RA0 for
                       the RA0PPS register.


       The table below shows the output codes for each peripheral, as well as the available Port selections.

       Table 21-2. PPS Output Selection Table
                                                                            Available Output Ports
       RxyPPS                    Output Source
                                                                   14-Pin Devices              20-Pin Devices
       0x28                         ADGRDB                    A          —         C        A         B                    C
       0x27                         ADGRDA                    A          —         C        A         B                    C
       0x26                           DSM1                    A          —         C        A         B                    C
       0x25                           CLKR                    A          —         C        A         B                    C
       0x24                           NCO1                    A          —         C        A         B                    C
       0x23                           TMR0                    A          —         C        A         B                    C
       0x22                        I2C1 SDA(1)                A          —         C        A         B                    C
       0x21                        I2C1 SCL(1)                A          —         C        A         B                    C
       0x20                          SPI2 SS                  A          —         C        A         B                    C
       0x1F                         SPI2 SDO                  A          —         C        A         B                    C
       0x1E                         SPI2 SCK                  A          —         C        A         B                    C
       0x1D                          SPI1 SS                  A          —         C        A         B                    C


--- p323 ---
       ...........continued
                                                                         Available Output Ports
       RxyPPS                 Output Source
                                                                14-Pin Devices              20-Pin Devices
       0x1C                      SPI1 SDO                  A          —         C        A         B       C
       0x1B                      SPI1 SCK                  A          —         C        A         B       C
       0x1A                      C2OUT                     A           —               C       A          B          C
       0x19                      C1OUT                     A           —               C       A          B          C
       0x18                     UART3 RTS                  A           —               C       A          B          C
       0x17                    UART3 TXDE                  A           —               C       A          B          C
       0x16                     UART3 TX                   A           —               C       A          B          C
       0x15                     UART2 RTS                  A           —               C       A          B          C
       0x14                    UART2 TXDE                  A           —               C       A          B          C
       0x13                     UART2 TX                   A           —               C       A          B          C
       0x12                     UART1 RTS                  A           —               C       A          B          C
       0x11                    UART1 TXDE                  A           —               C       A          B          C
       0x10                     UART1 TX                   A           —               C       A          B          C
       0x0F                   PWM3S1P2_OUT                 A           —               C       A          B          C
       0x0E                   PWM3S1P1_OUT                 A           —               C       A          B          C
       0x0D                   PWM2S1P2_OUT                 A           —               C       A          B          C
       0x0C                   PWM2S1P1_OUT                 A           —               C       A          B          C
       0x0B                   PWM1S1P2_OUT                 A           —               C       A          B          C
       0x0A                   PWM1S1P1_OUT                 A           —               C       A          B          C
       0x09                       CCP1                     A           —               C       A          B          C
       0x08                      CWG1D                     A           —               C       A          B          C
       0x07                      CWG1C                     A           —               C       A          B          C
       0x06                      CWG1B                     A           —               C       A          B          C
       0x05                      CWG1A                     A           —               C       A          B          C
       0x04                     CLC4OUT                    A           —               C       A          B          C
       0x03                     CLC3OUT                    A           —               C       A          B          C
       0x02                     CLC2OUT                    A           —               C       A          B          C
       0x01                     CLC1OUT                    A           —               C       A          B          C
       0x00                       LATxy                    A           —               C       A          B          C

       Note:
       1. Bidirectional pin. The corresponding input must select the same pin.

21.4   Bidirectional Pins
       PPS selections for peripherals with bidirectional signals on a single pin must be made so that the
       PPS input and PPS output select the same pin. The I2C Serial Clock (SCL) and Serial Data (SDA) are
       examples of such pins.


                    Important: The I2C default pins and a limited number of other alternate pins are I2C and
                    SMBus compatible. SDA and SCL signals can be routed to any pin; however, pins without
                    I2C compatibility will operate at standard TTL/ST logic levels as selected by the port’s INLVL
                    register.


--- p324 ---
21.5   PPS Lock
       The PPS module provides an extra layer of protection to prevent inadvertent changes to the PPS
       selection registers. The PPSLOCKED bit is used in combination with specific code execution blocks to
       lock/unlock the PPS selection registers.


                   Important: The PPSLOCKED bit is clear by default (PPSLOCKED = 0), which allows the PPS
                   selection registers to be modified without an unlock sequence.


       PPS selection registers are locked when the PPSLOCKED bit is set (PPSLOCKED = 1). Setting the
       PPSLOCKED bit requires a specific lock sequence as shown in the examples below in both C and
       assembly languages.
       PPS selection registers are unlocked when the PPSLOCKED bit is clear (PPSLOCKED = 0). Clearing the
       PPSLOCKED bit requires a specific unlock sequence as shown in the examples below in both C and
       assembly languages.


                   Important: All interrupts must be disabled before starting the lock/unlock sequence to
                   ensure proper execution.


              Example 21-1. PPS Lock Sequence (assembly language)

                 ; suspend interrupts
                    BCF      INTCON0,GIE
                    BANKSEL PPSLOCK
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


--- p325 ---
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
       selections unchanged. Default input selections are shown in the PPS input register details table. The
       PPSLOCKED bit is cleared in all Reset conditions.

21.8   Register Definitions: Peripheral Pin Select (PPS)


--- p326 ---
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


--- p327 ---
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


--- p328 ---
21.8.3 PPSLOCK

            Name:        PPSLOCK

            PPS Lock Register

      Bit           7           6               5              4                  3             2            1                0
                                                                                                                          PPSLOCKED
  Access                                                                                                                     R/W
   Reset                                                                                                                      0

Bit 0 – PPSLOCKED PPS Locked
          Reset States: POR = 0
                        All other Resets = 0
            Value       Description
            1           PPS is locked. PPS selections cannot be changed. Writes to any PPS register are ignored.
            0           PPS is not locked. PPS selections can be changed, but may require the PPS lock/unlock sequence.


--- p329 ---
21.9      Register Summary - Peripheral Pin Select Module
Address     Name       Bit Pos.   7        6           5             4           3                 2        1              0
  0x00
   ...     Reserved
 0x01FF
0x0200     PPSLOCK       7:0                                                                                          PPSLOCKED
0x0201      RA0PPS       7:0                                                         RA0PPS[5:0]
0x0202      RA1PPS       7:0                                                         RA1PPS[5:0]
0x0203      RA2PPS       7:0                                                         RA2PPS[5:0]
0x0204     Reserved
0x0205      RA4PPS       7:0                                                         RA4PPS[5:0]
0x0206      RA5PPS       7:0                                                         RA5PPS[5:0]
0x0207
  ...      Reserved
0x020C
0x020D      RB4PPS       7:0                                                         RB4PPS[5:0]
0x020E      RB5PPS       7:0                                                         RB5PPS[5:0]
0x020F      RB6PPS       7:0                                                         RB6PPS[5:0]
0x0210      RB7PPS       7:0                                                         RB7PPS[5:0]
0x0211      RC0PPS       7:0                                                         RC0PPS[5:0]
0x0212      RC1PPS       7:0                                                         RC1PPS[5:0]
0x0213      RC2PPS       7:0                                                         RC2PPS[5:0]
0x0214      RC3PPS       7:0                                                         RC3PPS[5:0]
0x0215      RC4PPS       7:0                                                         RC4PPS[5:0]
0x0216      RC5PPS       7:0                                                         RC5PPS[5:0]
0x0217      RC6PPS       7:0                                                         RC6PPS[5:0]
0x0218      RC7PPS       7:0                                                         RC7PPS[5:0]
0x0219
  ...      Reserved
0x023D
0x023E     INT0PPS       7:0                                                 PORT                        PIN[2:0]
0x023F     INT1PPS       7:0                                         PORT[1:0]                           PIN[2:0]
0x0240     INT2PPS       7:0                                   PORT[2:0]                                 PIN[2:0]
0x0241     T0CKIPPS      7:0                                   PORT[2:0]                                 PIN[2:0]
0x0242     T1CKIPPS      7:0                                   PORT[2:0]                                 PIN[2:0]
0x0243      T1GPPS       7:0                                   PORT[2:0]                                 PIN[2:0]
0x0244     T3CKIPPS      7:0                                   PORT[2:0]                                 PIN[2:0]
0x0245      T3GPPS       7:0                                   PORT[2:0]                                 PIN[2:0]
0x0246
  ...      Reserved
0x0247
0x0248      T2INPPS      7:0                                   PORT[2:0]                                 PIN[2:0]
0x0249      T4INPPS      7:0                                   PORT[2:0]                                 PIN[2:0]
0x024A
  ...      Reserved
0x024E
0x024F      CCP1PPS      7:0                                   PORT[2:0]                                 PIN[2:0]
0x0250      Reserved
0x0251    PWM1ERSPPS     7:0                                         PORT[1:0]                           PIN[2:0]
0x0252    PWM2ERSPPS     7:0                                   PORT[2:0]                                 PIN[2:0]
0x0253    PWM3ERSPPS     7:0                                         PORT[1:0]                           PIN[2:0]
0x0254
  ...      Reserved
0x0256
0x0257    PWMIN0PPS      7:0                                   PORT[2:0]                                 PIN[2:0]
0x0258    PWMIN1PPS      7:0                                   PORT[2:0]                                 PIN[2:0]
0x0259    SMT1WINPPS     7:0                                   PORT[2:0]                                 PIN[2:0]
0x025A    SMT1SIGPPS     7:0                                   PORT[2:0]                                 PIN[2:0]
0x025B     CWG1PPS       7:0                                   PORT[2:0]                                 PIN[2:0]
0x025C
  ...      Reserved
0x025D


--- p330 ---
...........continued
 Address               Name    Bit Pos.   7        6           5             4         3        2           1              0
  0x025E        MD1CARLPPS       7:0                                   PORT[2:0]                         PIN[2:0]
  0x025F        MD1CARHPPS       7:0                                   PORT[2:0]                         PIN[2:0]
  0x0260        MD1SRCPPS        7:0                                   PORT[2:0]                         PIN[2:0]
  0x0261         CLCIN0PPS       7:0                                   PORT[2:0]                         PIN[2:0]
  0x0262         CLCIN1PPS       7:0                                   PORT[2:0]                         PIN[2:0]
  0x0263         CLCIN2PPS       7:0                                   PORT[2:0]                         PIN[2:0]
  0x0264         CLCIN3PPS       7:0                                   PORT[2:0]                         PIN[2:0]
  0x0265
    ...           Reserved
  0x0268
  0x0269          ADACTPPS       7:0                                   PORT[2:0]                         PIN[2:0]
  0x026A         SPI1SCKPPS      7:0                                   PORT[2:0]                         PIN[2:0]
  0x026B          SPI1SDIPPS     7:0                                   PORT[2:0]                         PIN[2:0]
  0x026C          SPI1SSPPS      7:0                                   PORT[2:0]                         PIN[2:0]
  0x026D         SPI2SCKPPS      7:0                                   PORT[2:0]                         PIN[2:0]
  0x026E          SPI2SDIPPS     7:0                                   PORT[2:0]                         PIN[2:0]
  0x026F          SPI2SSPPS      7:0                                   PORT[2:0]                         PIN[2:0]
  0x0270         I2C1SDAPPS      7:0                                   PORT[2:0]                         PIN[2:0]
  0x0271         I2C1SCLPPS      7:0                                   PORT[2:0]                         PIN[2:0]
  0x0272           U1RXPPS       7:0                                         PORT[1:0]                   PIN[2:0]
  0x0273          U1CTSPPS       7:0                                         PORT[1:0]                   PIN[2:0]
  0x0274           UxRXPPS       7:0                                                 PORT                PIN[2:0]
  0x0275           UxCTSPPS      7:0                                                 PORT                PIN[2:0]
  0x0276           U3RXPPS       7:0                                         PORT[1:0]                   PIN[2:0]
  0x0277          U3CTSPPS       7:0                                         PORT[1:0]                   PIN[2:0]


--- p331 ---
