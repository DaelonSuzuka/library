                       PIC18(L)F26/27/45/46/47/55/56/57K42
17.0      PERIPHERAL PIN SELECT
          (PPS) MODULE
The Peripheral Pin Select (PPS) module connects
peripheral inputs and outputs to the device I/O pins. Only
digital signals are included in the selections. All analog
inputs and outputs remain fixed to their assigned pins.
Input and output selections are independent as shown in
the simplified block diagram Figure 17-1.
The peripheral input is selected with the peripheral
xxxPPS register (Register 17-1), and the peripheral
output is selected with the PORT RxyPPS register
(Register 17-2). For example, to select PORTC[7] as
the UART1 RX input, set U1RXPPS to 0b1 0111, and
to select PORTC[6] as the UART1 TX output set
RC6PPS to 0b01 0011.

17.1      PPS Inputs
Each peripheral has a PPS register with which the
inputs to the peripheral are selected. Inputs include the
device pins.
Multiple peripherals can operate from the same source
simultaneously. Port reads always return the pin level
regardless of peripheral PPS selection. If a pin also has
analog functions associated, the ANSEL bit for that pin
must be cleared to enable the digital input buffer.
Although every peripheral has its own PPS input
selection register, the selections are identical for every
peripheral as shown in Register 17-1.
  Note:     The notation “xxx” in the register name is
            a place holder for the peripheral identifier.
            For example, INT0PPS.

17.2      PPS Outputs
Each I/O pin has a PPS register with which the pin
output source is selected. With few exceptions, the port
TRIS control associated with that pin retains control
over the pin output driver. Peripherals that control the
pin output driver as part of the peripheral operation will
override the TRIS control as needed. These
peripherals include:
• UART I2C
Although every pin has its own PPS peripheral
selection register, the selections are identical for every
pin as shown in Register 17-2.
  Note:     The notation “Rxy” is a place holder for the
            pin identifier. For example, RA0PPS.


 2017-2021 Microchip Technology Inc.                        DS40001919G-page 275
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 17-1:           SIMPLIFIED PPS BLOCK DIAGRAM

                                                                            Rev. 10-000262D
                                                                                   3/27/2017


                                                         RxyPPS

      abcPPS
                                                                             Rxy
   Rxy
                                        Peripheral abc


                                                         RxyPPS


                                                                             Rxy


                                        Peripheral xyz
                                                         RxyPPS
   Rxy

       xyzPPS
                                                                             Rxy


 2017-2021 Microchip Technology Inc.                             DS40001919G-page 276
                      PIC18(L)F26/27/45/46/47/55/56/57K42
17.3      Bidirectional Pins                                EXAMPLE 17-2:           PPS UNLOCK SEQUENCE
                                                             ; Disable interrupts:
PPS selections for peripherals with bidirectional                BCF     INTCON0,GIE
signals on a single pin must be made so that the PPS
input and PPS output select the same pin. Peripherals        ; Bank to PPSLOCK register
that have bidirectional signals include:                         BANKSEL PPSLOCK
                                                                 MOVLB   PPSLOCK
• I2C
                                                                 MOVLW   55h

                                                             ; Required sequence, next 4 instructions
  Note:     Refer to Table 17-1 for pins that are I2C
                                                                 MOVWF   PPSLOCK
            compatible. Clock and data signals can be
                                                                 MOVLW   AAh
            routed to any pin, however pins without              MOVWF   PPSLOCK
            I2C compatibility will operate at standard
            TTL/ST logic levels as selected by the           ; Clear PPSLOCKED bit to enable writes
            INVLV register.                                  ; Only a BCF instruction will work
                                                                 BCF     PPSLOCK,0
17.4      PPS Lock                                           ; Enable Interrupts
The PPS includes a mode in which all input and output            BSF     INTCON0,GIE
selections can be locked to prevent inadvertent
changes. PPS selections are locked by setting the           17.5     PPS One-way Lock
PPSLOCKED bit of the PPSLOCK register. Setting and
clearing this bit requires a special sequence as an extra   When the PPS1WAY Configuration bit is set, the
precaution against inadvertent changes. Examples of         PPSLOCKED bit can only be cleared and set one time
setting and clearing the PPSLOCKED bit are shown in         after a device Reset. This allows for clearing the
Example 17-1.                                               PPSLOCKED bit so that the input and output selections
                                                            can be made during initialization. When the
EXAMPLE 17-1:          PPS LOCK SEQUENCE                    PPSLOCKED bit is set after all selections have been
 ; Disable interrupts:                                      made, it will remain set and cannot be cleared until after
     BCF     INTCON0,GIE                                    the next device Reset event.

 ; Bank to PPSLOCK register                                 17.6     Operation During Sleep
     BANKSEL PPSLOCK
     MOVLB   PPSLOCK                                        PPS input and output selections are unaffected by
     MOVLW   55h                                            Sleep.

 ; Required sequence, next 4 instructions
                                                            17.7     Effects of a Reset
     MOVWF   PPSLOCK
     MOVLW   AAh                                            A device Power-on-Reset (POR) clears all PPS input
     MOVWF   PPSLOCK                                        and output selections to their default values. All other
                                                            Resets leave the selections unchanged. Default input
 ; Set PPSLOCKED bit to disable writes
                                                            selections are shown in pin allocation Table 1. The PPS
 ; Only a BSF instruction will work
     BSF     PPSLOCK,0                                      one-way lock is also removed.

 ; Enable Interrupts
     BSF     INTCON0,GIE


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 277
                        PIC18(L)F26/27/45/46/47/55/56/57K42
17.8        Register Definitions: PPS Input Selection
REGISTER 17-1:           xxxPPS: PERIPHERAL xxx INPUT SELECTION
        U-0             U-0       R/W-m/u(1,3)    R/W-m/u(1)     R/W-m/u(1)      R/W-m/u(1)     R/W-m/u(1)     R/W-m/u(1)
        —               —                                                xxxPPS[5:0]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit              -n/n = Value at POR and BOR/Value at all other Resets
u = Bit is unchanged              x = Bit is unknown            q = value depends on peripheral
‘1’ = Bit is set                  U = Unimplemented bit,        m = value depends on default location for that input
‘0’ = Bit is cleared                  read as ‘0’


bit 7-6            Unimplemented: Read as ‘0’
bit 5-3            xxxPPS[5:3]: Peripheral xxx Input PORTx Pin Selection bits
                   See Table 17-1 for the list of available ports and default pin locations.
                   101 = PORTF(2)
                   100 = PORTE(3)
                   011 = PORTD(3)
                   010 = PORTC
                   001 = PORTB
                   000 = PORTA
bit 2-0            xxxPPS[2:0]: Peripheral xxx Input PORTx Pin Selection bits
                   111 = Peripheral input is from PORTx Pin 7 (Rx7)
                   110 = Peripheral input is from PORTx Pin 6 (Rx6)
                   101 = Peripheral input is from PORTx Pin 5 (Rx5)
                   100 = Peripheral input is from PORTx Pin 4 (Rx4)
                   011 = Peripheral input is from PORTx Pin 3 (Rx3)
                   010 = Peripheral input is from PORTx Pin 2 (Rx2)
                   001 = Peripheral input is from PORTx Pin 1 (Rx1)
                   000 = Peripheral input is from PORTx Pin 0 (Rx0)

Note 1:       The Reset value ‘m’ of this register is determined by device default locations for that input.
     2:       Reserved on PIC18LF26/27/45/46/47K42 parts.
     3:       Reserved on PIC18LF26K42 parts.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 278
 2017-2021 Microchip Technology Inc.


                                        TABLE 17-1:      PPS INPUT REGISTER DETAILS
                                                                      Default Pin     Register                                  Input Available from Selected PORTx
                                                          PPS Input
                                           Peripheral                 Selection at   Reset Value
                                                           Register                                PIC18(L)F26/27K42       PIC18(L)F45/46/47K42                           PIC18(L)F55/56/57K42
                                                                         POR           at POR
                                        Interrupt 0     INT0PPS          RB0         0b0 1000      A       B       —   A    B       —       —        —      A         B       —       —      —       —
                                        Interrupt 1     INT1PPS          RB1         0b0 1001      A       B       —   A    B       —       —        —      —         B       —       D      —       —


                                                                                                                                                                                                         PIC18(L)F26/27/45/46/47/55/56/57K42
                                        Interrupt 2     INT2PPS          RB2         0b0 1010      A       B       —   A    B       —       —        —      —         B       —       —      —       F
                                        Timer0 Clock    T0CKIPPS         RA4         0b0 0100      A       B       —   A    B       —       —        —      A         —       —       —      —       F
                                        Timer1 Clock    T1CKIPPS         RC0         0b1 0000      A       —       C   A    —       C       —        —      —         —       C       —          E   —
                                        Timer1 Gate     T1GPPS           RB5         0b0 1101      —       B       C   —    B       C       —        —      —         B       C       —      —       —
                                        Timer3 Clock    T3CKIPPS         RC0         0b1 0000      —       B       C   —    B       C       —        —       -        —       C       —          E   —
                                        Timer3 Gate     T3GPPS           RC0         0b1 0000      A       —       C   A    —       C       —        —      A         —       C       —      —       —
                                        Timer5 Clock    T5CKIPPS         RC2         0b1 0010      A       —       C   A    —       C       —        —      —         —       C       —          E   —
                                        Timer5 Gate     T5GPPS           RB4         0b0 1100      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        Timer2 Clock    T2INPPS          RC3         0b1 0011      A       —       C   A    —       C       —        —      A         —       C       —      —       —
                                        Timer4 Clock    T4INPPS          RC5         0b1 0101      —       B       C   —    B       C       —        —      —         B       C       —      —       —
                                        Timer6 Clock    T6INPPS          RB7         0b0 1111      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        CCP1            CCP1PPS          RC2         0b1 0010      —       B       C   —    B       C       —        —      —         —       C       —      —       F
                                        CCP2            CCP2PPS          RC1         0b1 0001      —       B       C   —    B       C       —        —      —         —       C       —      —       F
                                        CCP3            CCP3PPS          RB5         0b0 1101      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        CCP4            CCP4PPS          RB0         0b0 1000      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        SMT1 Window     SMT1WINPPS       RC0         0b1 0000      —       B       C   —    B       C       —        —      —         —       C       —      —       F
                                        SMT1 Signal     SMT1SIGPPS       RC1         0b1 0001      —       B       C   —    B       C       —        —      —         —       C       —      —       F
                                        CWG1            CWG1PPS          RB0         0b0 1000      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        CWG2            CWG2PPS          RB1         0b0 1001      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        CWG3            CWG3PPS          RB2         0b0 1010      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        DSM1 Carrier    MD1CARLPPS       RA3         0b0 0011      A       —       C   A    —       —        D       —      A         —       —       D      —       —
                                        Low
                                        DSM1 Carrier    MD1CARHPPS       RA4         0b0 0100      A       —       C   A    —       —        D       —      A         —       —       D      —       —
                                        High
DS40001919G-page 279


                                        DSM1 Source     MD1SRCPPS        RA5         0b0 0101      A       —       C   A    —       —        D       —      A         —       —       D      —       —
                                        CLCx Input 1    CLCIN0PPS        RA0         0b0 0000      A       —       C   A    —       C       —        —      A         —       C       —      —       —
                                        CLCx Input 2    CLCIN1PPS        RA1         0b0 0001      A       —       C   A    —       C       —        —      A         —       C       —      —       —
                                        CLCx Input 3    CLCIN2PPS        RB6         0b0 1110      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        CLCx Input 4    CLCIN3PPS        RB7         0b0 1111      —       B       C   —    B       —        D       —      —         B       —       D      —       —
                                        TABLE 17-1:       PPS INPUT REGISTER DETAILS
 2017-2021 Microchip Technology Inc.


                                                                       Default Pin     Register                                  Input Available from Selected PORTx
                                                           PPS Input
                                           Peripheral                  Selection at   Reset Value
                                                            Register                                PIC18(L)F26/27K42       PIC18(L)F45/46/47K42                           PIC18(L)F55/56/57K42
                                                                          POR           at POR
                                        ADC Conversion   ADACTPPS         RB4         0b0 1100      —       B       C   —    B       —        D       —      —         B       —       D      —   —
                                        Trigger
                                        SPI1 Clock       SPI1SCKPPS       RC3         0b1 0011      —       B       C   —    B       C       —        —      —         B       C       —      —   —
                                        SPI1 Data        SPI1SDIPPS       RC4         0b1 0100      —       B       C   —    B       C       —        —      —         B       C       —      —   —


                                                                                                                                                                                                      PIC18(L)F26/27/45/46/47/55/56/57K42
                                        SPI1 Client      SPI1SSPPS        RA5         0b0 0101      A       —       C   A    —       —        D       —      A         —       —       D      —   —
                                        Select
                                        I2C1 Clock       I2C1SCLPPS       RC3         0b1 0011      —       B       C   —    B       C       —        —      —         B       C       —      —   —
                                        I2C1 Data        I2C1SDAPPS       RC4         0b1 0100      —       B       C   —    B       C       —        —      —         B       C       —      —   —
                                        I2C2 Clock       I2C2SCLPPS       RB1         0b0 1001      —       B       C   —    B       —        D       —      —         B       —       D      —   —
                                        I2C2 Data        I2C2SDAPPS       RB2         0b0 1010      —       B       C   —    B       —        D       —      —         B       —       D      —   —
                                        UART1 Receive    U1RXPPS          RC7         0b1 0111      —       B       C   —    B       C       —        —      —         —       C       —      —   F
                                        UART1 Clear To   U1CTSPPS         RC6         0b1 0110      —       B       C   —    B       C       —        —      —         —       C       —      —   F
                                        Send
                                        UART2 Receive    U2RXPPS          RB7         0b0 1111      —       B       C   —    B       —        D       —      —         B       —       D      —   —
                                        UART2 Clear To   U2CTSPPS         RB6         0b0 1110      —       B       C   —    B       —        D       —      —         B       —       D      —   —
                                        Send
DS40001919G-page 280
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 17-2:          RxyPPS: PIN Rxy OUTPUT SOURCE SELECTION REGISTER
        U-0            U-0          R/W-0/u             R/W-0/u    R/W-0/u       R/W-0/u        R/W-0/u      R/W-0/u
        —               —                                               RxyPPS[5:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5-0            RxyPPS[5:0]: Pin Rxy Output Source Selection bits
                   See Table 17-2 for the list of available ports.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 281
 2017-2021 Microchip Technology Inc.


                                        TABLE 17-2:     PPS OUTPUT REGISTER DETAILS
                                                                                                                           Device Configuration
                                          RxyPPS[5:0]      Pin Rxy Output Source
                                                                                       PIC18(L)F26K42           PIC18(L)F45/46/47K42                          PIC18(L)F55/56/57K42

                                         0b11 1111 -                                                            Reserved
                                          0b11 0011
                                          0b11 0010     ADGRDB                     A         —          C   A   —           C         —           —   A   —       —       —          —   F
                                          0b11 0001     ADGRDA                     A         —          C   A   —           C         —           —   A   —       —       —          —   F


                                                                                                                                                                                             PIC18(L)F26/27/45/46/47/55/56/57K42
                                          0b11 0000     CWG3D                      A         —          C   A   —          —          D           —   A   —       —       D          —   —
                                          0b10 1111     CWG3C                      A         —          C   A   —          —          D           —   A   —       —       D          —   —
                                          0b10 1110     CWG3B                      A         —          C   A   —          —          —           E   A   —       —       —          E   —
                                          0b10 1101     CWG3A                      —         B          C   —   B           C         —           —   —   B       C       —          —   —
                                          0b10 1100     CWG2D                      —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b10 1011     CWG2C                      —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b10 1010     CWG2B                      —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b10 1001     CWG2A                      —         B          C   —   B           C         —           —   —   B       C       —          —   —
                                          0b10 1000     DSM1                       A         —          C   A   —          —          D           —   A   —       —       D          -   —
                                          0b10 0111     CLKR                       —         B          C   —   B           C         —           —   —   B       —       —          E   —
                                          0b10 0110     NCO1                       A         —          C   A   —          —          D           —   A   —       —       D          —   —
                                          0b10 0101     TMR0                       —         B          C   —   B           C         —           —   —   —       C       —          —   F
                                          0b10 0100     I2C2 (SDA)                 —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b10 0011     I2C2 (SCL)                 —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b10 0010     I2C1 (SDA)                 —         B          C   —   B           C         —           —   —   B       C       —          —   —
                                          0b10 0001     I2C1 (SCL)                 —         B          C   —   B           C         —           —   —   B       C       —          —   —
                                          0b10 0000     SPI1 (SS)                  A         —          C   A   —          —          D           —   A   —       —       D          —   —
                                          0b01 1111     SPI1 (SDO)                 —         B          C   —   B           C         —           —   —   B       C       —          —   —
                                          0b01 1110     SPI1 (SCK)                 —         B          C   —   B           C         —           —   —   B       C       —          —   —
                                          0b01 1101     C2OUT                      A         —          C   A   —          —          —           E   A   —       —       —          E   —
                                          0b01 1100     C1OUT                      A         —          C   A   —          —          D           —   A   —       —       D          —   —
                                         0b01 1011 -                                                            Reserved
                                          0b01 1001
                                                        UART2 (RTS)                —         B          C   —   B          —          D           —   —   B       —       D          —   —
DS40001919G-page 282


                                          0b01 1000
                                          0b01 0111     UART2 (TXDE)               —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b01 0110     UART2 (TX)                 —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b01 0101     UART1 (RTS)                —         B          C   —   B           C         —           —   —   —       C       —          —   F
                                          0b01 0100     UART1 (TXDE)               —         B          C   —   B           C         —           —   —   —       C       —          —   F
                                          0b01 0011     UART1 (TX)                 —         B          C   —   B           C         —           —   —   —       C       —          —   F
                                        TABLE 17-2:     PPS OUTPUT REGISTER DETAILS
 2017-2021 Microchip Technology Inc.


                                                                                                                          Device Configuration
                                          RxyPPS[5:0]     Pin Rxy Output Source
                                                                                      PIC18(L)F26K42           PIC18(L)F45/46/47K42                          PIC18(L)F55/56/57K42

                                         0b01 0010 -                                                           Reserved
                                          0b01 0001
                                          0b01 0000     PWM8                      A         —          C   A   —          —          D           —   A   —       —       D          —   —
                                          0b00 1111     PWM7                      A         —          C   A   —           C         —           —   —   —       C       —          —   F


                                                                                                                                                                                            PIC18(L)F26/27/45/46/47/55/56/57K42
                                          0b00 1110     PWM6                      A         —          C   A   —          —          D           —   A   —       —       D          —   —
                                          0b00 1101     PWM5                      A         —          C   A   —           C         —           —   A   —       —       —          —   F
                                          0b00 1100     CCP4                      —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b00 1011     CCP3                      —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b00 1010     CCP2                      —         B          C   —   B           C         —           —   —   —       C       —          —   F
                                          0b00 1001     CCP1                      —         B          C   —   B           C         —           —   —   —       C       —          —   F
                                          0b00 1000     CWG1D                     —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b00 0111     CWG1C                     —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b00 0110     CWG1B                     —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b00 0101     CWG1A                     —         B          C   —   B           C         —           —   —   B       C       —          —   —
                                          0b00 0100     CLC4OUT                   —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b00 0011     CLC3OUT                   —         B          C   —   B          —          D           —   —   B       —       D          —   —
                                          0b00 0010     CLC2OUT                   A         —          C   A   —           C         —           —   A   —       —       —          —   F
                                          0b00 0001     CLC1OUT                   A         —          C   A   —           C         —           —   A   —       —       —          —   F
                                          0b00 0000     LATxy                     A         B          C   A   B           C         D           E   A   B       C       D          E   F
DS40001919G-page 283
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 17-3:           PPSLOCK: PPS LOCK REGISTER
        U-0            U-0           U-0               U-0       U-0           U-0            U-0          R/W-0/0
        —               —             —                —          —             —             —          PPSLOCKED
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-1            Unimplemented: Read as ‘0’
bit 0              PPSLOCKED: PPS Locked bit
                   1 = PPS is locked.
                   0 = PPS is not locked. PPS selections can be changed.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 284
                         PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 17-3:         SUMMARY OF REGISTERS ASSOCIATED WITH THE PPS MODULE
                                                                                                                      Register
      Name             Bit 7        Bit 6       Bit 5        Bit 4        Bit 3           Bit 2   Bit 1     Bit 0
                                                                                                                      on page

PPSLOCK                 —            —           —            —            —               —       —      PPSLOCKED     285
INT0PPS                 —            —                                            INT0PPS[5:0]                          279
INT1PPS                 —            —                                            INT1PPS[5:0]                          279
INT2PPS                 —            —                                            INT2PPS[5:0]                          279
T0CKIPPS                —            —                                            T0CKPPS[5:0]                          279
T1CKIPPS                —            —                                            T1CKPPS[5:0]                          279
T1GPPS                  —            —                                            T1GPPS[5:0]                           279
T3CKIPPS                —            —                                            T3CKIPPS[5:0]                         279
T3GPPS                  —            —                                            T3GPPS[5:0]                           279
T5CKIPPS                —            —                                            T5CKPPS[5:0]                          279
T5GPPS                  —            —                                            T5GPPS[5:0]                           279
T2INPPS                 —            —                                            T2INPPS[5:0]                          279
T4INPPS                 —            —                                            T4INPPS[5:0]                          279
T6INPPS                 —            —                                            T6INPPS[5:0]                          279
CCP1PPS                 —            —                                            CCP1PPS[5:0]                          279
CCP2PPS                 —            —                                            CCP2PPS[5:0]                          279
CCP3PPS                 —            —                                            CCP3PPS[5:0]                          279
CCP4PPS                 —            —                                            CCP4PPS[5:0]                          279
SMT1WINPPS              —            —                                       SMT1WINPPS[5:0]                            279
SMT1SIGPPS              —            —                                       SMT1SIGPPS[5:0]                            279
CWG1PPS                 —            —                                            CWG1PPS[5:0]                          279
CWG2PPS                 —            —                                            CWG2PPS[5:0]                          279
CWG3PPS                 —            —                                            CWG3PPS[5:0]                          279
MD1CARLPPS              —            —                                       MD1CARLPPS[5:0]                            279
MD1CARHPPS              —            —                                       MD1CARHPPS[5:0]                            279
MD1SRCPPS               —            —                                         MD1SRCPPS[5:0]                           279
CLCIN0PPS               —            —                                         CLCIN0PPS[5:0]                           279
CLCIN1PPS               —            —                                         CLCIN1PPS[5:0]                           279
CLCIN2PPS               —            —                                         CLCIN2PPS[5:0]                           279
CLCIN3PPS               —            —                                         CLCIN3PPS[5:0]                           279
ADACTPPS                —            —                                         ADACTPPS[5:0]                            279
SPI1SCKPPS              —            —                                         SPI1SCKPPS[5:0]                          279
SPI1SDIPPS              —            —                                         SPI1SDIPPS[5:0]                          279
SPI1SSPPS               —            —                                         SPI1SSPPS[5:0]                           279
I2C1SCLPPS              —            —                                         I2C1SCLPPS[5:0]                          279
I2C1SDAPPS              —            —                                         I2C1SDAPPS[5:0]                          279
I2C2SCLPPS              —            —                                         I2C2SCLPPS[5:0]                          279
I2C2SDAPPS              —            —                                         I2C2SDAPPS[5:0]                          279
U1RXPPS                 —            —                                            U1RXPPS[5:0]                          279
U1CTSPPS                —            —                                         U1CTSPPS[5:0]                            279
U2RXPPS                 —            —                                            U2RXPPS[5:0]                          279
U2CTSPPS                —            —                                         U2CTSPPS[5:0]                            279
RxyPPS                  —            —                                             RxyPPS[5:0]                          282
Legend:      — = unimplemented, read as ‘0’. Shaded cells are unused by the PPS module.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 285
