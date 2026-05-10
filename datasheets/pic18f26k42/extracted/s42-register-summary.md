                         PIC18(L)F26/27/45/46/47/55/56/57K42
42.0       REGISTER SUMMARY
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                              Register
 Address         Name          Bit 7           Bit 6        Bit 5          Bit 4         Bit 3           Bit 2          Bit 1      Bit 0
                                                                                                                                              on page

3FFFh      TOSU                 —               —            —                                    Top of Stack Upper byte                       38
3FFEh      TOSH                                                          Top of Stack High byte                                                 38
3FFDh      TOSL                                                          Top of Stack Low byte                                                  38
3FFCh      STKPTR               —               —            —                                         Stack Pointer                            39
3FFBh      PCLATU               —               —            —                            Holding Register for PC Upper byte                    36
3FFAh      PCLATH                                                   Holding Register for PC High byte                                           36
3FF9h      PCL                                                                PC Low byte                                                       36
3FF8h      TBLPTRU              —               —                               Program Memory Table Pointer Upper byte                         192
3FF7h      TBLPTRH                                            Program Memory Table Pointer High byte                                            192
3FF6h      TBLPTRL                                             Program Memory Table Pointer Low byte                                            192
3FF5h      TABLAT                                                               Table Latch                                                     192
3FF4h      PRODH                                                       Product Register High byte                                               187
3FF3h      PRODL                                                       Product Register Low byte                                                187
3FF2h              —                                                        Unimplemented
3FF1h      PCON1                —               —            —              —                 —            —            MEMV        —           91
3FF0h      PCON0             STKOVF           STKUNF      WDTWV           RWDT          RMCLR              RI           POR        BOR          90
3FEFh      INDF0           Uses contents of FSR0 to address data memory – value of FSR0 not changed                                             60
3FEEh      POSTINC0        Uses contents of FSR0 to address data memory – value of FSR0 post-incremented                                        61
3FEDh      POSTDEC0        Uses contents of FSR0 to address data memory – value of FSR0 post-decremented                                        61
3FECh      PREINC0         Uses contents of FSR0 to address data memory – value of FSR0 pre-incremented                                         61
3FEBh      PLUSW0          Uses contents of FSR0 to address data memory – value of FSR0 pre-incremented – value of FSR0 offset by W             61
3FEAh      FSR0H                —               —                             Indirect Data Memory Address Pointer 0 High                       61
3FE9h      FSR0L                                             Indirect Data Memory Address Pointer 0 Low                                         61
3FE8h      WREG                                                             Working Register
3FE7h      INDF1           Uses contents of FSR1 to address data memory – value of FSR1 not changed                                             61
3FE6h      POSTINC1        Uses contents of FSR1 to address data memory – value of FSR1 post-incremented                                        61
3FE5h      POSTDEC1        Uses contents of FSR1 to address data memory – value of FSR1 post-decremented                                        61
3FE4h      PREINC1         Uses contents of FSR1 to address data memory – value of FSR1 pre-incremented                                         61
3FE3h      PLUSW1          Uses contents of FSR1 to address data memory – value of FSR1 pre-incremented – value of FSR1 offset by W             61
3FE2h      FSR1H                —               —                             Indirect Data Memory Address Pointer 1 High                       61
3FE1h      FSR1L                                             Indirect Data Memory Address Pointer 1 Low                                         61
3FE0h      BSR                  —               —                                         Bank Select Register                                  44
3FDFh      INDF2           Uses contents of FSR2 to address data memory – value of FSR2 not changed                                             61
3FDEh      POSTINC2        Uses contents of FSR2 to address data memory – value of FSR2 post-incremented                                        61
3FDDh      POSTDEC2        Uses contents of FSR2 to address data memory – value of FSR2 post-decremented                                        61
3FDCh      PREINC2         Uses contents of FSR2 to address data memory – value of FSR2 pre-incremented                                         61
3FDBh      PLUSW2          Uses contents of FSR2 to address data memory – value of FSR2 pre-incremented – value of FSR2 offset by W             61
3FDAh      FSR2H                —               —                             Indirect Data Memory Address Pointer 2 High                       61
3FD9h      FSR2L                                             Indirect Data Memory Address Pointer 2 Low                                         61
3FD8h      STATUS               —              TO            PD             N             OV               Z             DC         C           58
3FD7h      IVTBASEU             —               —            —           BASE20         BASE19          BASE18         BASE17     BASE16        166
3FD6h      IVTBASEH          BASE15           BASE14      BASE13         BASE12         BASE11          BASE10         BASE9      BASE8         166
3FD5h      IVTBASEL           BASE7           BASE6        BASE5          BASE4         BASE3           BASE2          BASE1      BASE0         166
3FD4h      IVTLOCK              —               —            —              —                 —            —                —    IVTLOCKED      168
3FD3h      INTCON1                     STAT                  —              —                 —            —                —       —           136
3FD2h      INTCON0             GIE             GIEL         IPEN            —                 —        INT2EDG         INT1EDG    INT0EDG       135
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                                  DS40001919G-page 717
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                             Register
 Address       Name            Bit 7          Bit 6         Bit 5           Bit 4           Bit 3     Bit 2            Bit 1     Bit 0
                                                                                                                                             on page

3FD1h -            —                                                         Unimplemented
3FD0h
3FCFh      PORTF(3)             RF7            RF6          RF5             RF4             RF3       RF2              RF1       RF0           265
3FCEh      PORTE                 —             —             —               —              RE0      RE2(2)           RE1(2)    RE1(2)         265
3FCDh      PORTD(2)             RD7           RD6           RD5             RD4             RD3       RD2              RD1       RD0           265
3FCCh      PORTC                RC7           RC6           RC5             RC4             RC3       RC2              RC1       RC0           265
3FCBh      PORTB                RB7           RB6           RB5             RB4             RB3       RB2              RB1       RB0           265
3FCAh      PORTA                RA7           RA6           RA5             RA4             RA3       RA2              RA1       RA0           265
3FC9h -            —                                                         Unimplemented
3FC8h
3FB7h      TRISF(3)           TRISF7         TRISF6        TRISF5          TRISF4          TRISF3    TRISF2           TRISF1    TRISF0         266
3FB6h      TRISE(2)           TRISE7         TRISE6        TRISE5          TRISE4          TRISE3    TRISE2           TRISE1    TRISE0         266
3FB5h      TRISD(2)           TRISD7         TRISD6        TRISD5       TRISD4             TRISD3    TRISD2           TRISD1    TRISD0         266
3FC4h      TRISC              TRISC7         TRISC6        TRISC5       TRISC4             TRISC3    TRISC2           TRISC1    TRISC0         266
3FC3h      TRISB              TRISB7         TRISB6        TRISB5          TRISB4          TRISB3    TRISB2           TRISB1    TRISB0         266
3FC2h      TRISA              TRISA7         TRISA6        TRISA5          TRISA4          TRISA3    TRISA2           TRISA1    TRISA0         266
3FC1h -            —                                                         Unimplemented
3FC0h
3FBFh      LATF(3)             LATF7         LATF6         LATF5           LATF4            LATF3    LATF2            LATF1     LATF0          267
3FBEh      LATE(2)             LATE7         LATE7         LATE7           LATE7            LATE7    LATE7            LATE7     LATE7          267
3FBDh      LATD(2)            LATD7          LATD6         LATD5           LATD4           LATD3     LATD2            LATD1     LATD0          267
3FBCh      LATC               LATC7          LATC6         LATC5           LATC4           LATC3     LATC2            LATC1     LATC0          267
3FBBh      LATB                LATB7         LATB6         LATB5           LATB4            LATB3    LATB2            LATB1     LATB0          267
3FBAh      LATA                LATA7         LATA6         LATA5           LATA4            LATA3    LATA2            LATA1     LATA0          267
3FB9h      T0CON1                           CS[2:0]                        ASYNC                              CKPS[3:0]                        304
3FB8h      T0CON0               EN             —            OUT            MD16                                OUTPS                           303
3FB7h      TMR0H                                                                    TMR0H                                                      305
3FB6h      TMR0L                                                                    TMR0L                                                      305
3FB5h      T1CLK                                                                     CS                                                        317
3FB4h      T1GATE                                                                   GSS                                                        318
3FB3h      T1GCON               GE            GPOL          GTM            GSPM             GGO       GVAL              —         —            316
3FB2h      T1CON                 —             —                 CKPS[1:0]                   —       SYNC             RD16        ON           340
3FB1h      TMR1H                                                                    TMR1H                                                      319
3FB0h      TMR1L                                                                    TMR1L                                                      319
3FAFh      T2RST                 —             —             —                                        RSEL                                     338
3FAEh      T2CLK                 —             —             —               —                                   CS                            317
3FADh      T2HLT              PSYNC          CKPOL        CKSYNC                                      MODE                                     341
3FACh      T2CON                ON                         CKPS                                                OUTPS                           315
3FABh      T2PR                                                                      PR2                                                       339
3FAAh      T2TMR                                                                    TMR2                                                       339
3FA9h      T3CLK                                                                     CS                                                        317
3FA8h      T3GATE                                                                   GSS                                                        318
3FA7h      T3GCON               GE            GPOL          GTM            GSPM             GGO       GVAL              —         —            316
3FA6h      T3CON                 —             —                    CKPS                     —      NOT_SYNC          RD16        ON           340
3FA5h      TMR3H                                                                    TMR3H                                                      319
3FA4h      TMR3L                                                                    TMR3L                                                      319
3FA3h      T4RST                 —             —             —                                        RSEL                                     338
3FA2h      T4CLK                 —             —             —               —                                   CS                            337
Legend:      x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:      Unimplemented in LF devices.
      2:     Unimplemented in PIC18(L)F26K42.
      3:     Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:     Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                                 DS40001919G-page 718
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                         Register
 Address      Name            Bit 7          Bit 6         Bit 5          Bit 4           Bit 3     Bit 2           Bit 1    Bit 0
                                                                                                                                         on page

3FA1h      T4HLT             PSYNC          CKPOL        CKSYNC                                     MODE                                   341
3FA0h      T4CON               ON                         CKPS                                              OUTPS                          340
3F9Fh      T4PR                                                                    PR4                                                     339
3F9Eh      T4TMR                                                                  TMR4                                                     339
3F9Dh      T5CLK                                                                   CS                                                      337
3F9Ch      T5GATE                                                                 GSS                                                      318
3F9Bh      T5GCON              GE            GPOL          GTM            GSPM            GGO       GVAL             —        —            316
3F9Ah      T5CON                —             —                    CKPS                    —      NOT_SYNC         RD16       ON           340
3F99h      TMR5H                                                                  TMR5H                                                    319
3F98h      TMR5L                                                                  TMR5L                                                    319
3F97h      T6RST                —             —             —                                       RSEL                                   338
3F96h      T6CLK                —             —             —              —                                 CS                            317
3F95h      T6HLT             PSYNC          CKPOL        CKSYNC                                     MODE                                   341
3F94h      T6CON               ON                         CKPS                                              OUTPS                          340
3F93h      T6PR                                                                    PR6                                                     339
3F92h      T6TMR                                                                  TMR6                                                     339
3F91h -            —                                                       Unimplemented
3F80h
3F7Fh      CCP1CAP                                                                 CTS                                                     354
3F7Eh      CCP1CON             EN             —            OUT            FMT                               MODE                           352
3F7Dh      CCPR1H                                                                  RH                                                      355
3F7Ch      CCPR1L                                                                  RL                                                      354
3F7Bh      CCP2CAP                                                                 CTS                                                     354
3F7Ah      CCP2CON             EN             —            OUT            FMT                               MODE                           352
3F79h      CCPR2H                                                                  RH                                                      355
3F78h      CCPR2L                                                                  RL                                                      354
3F77h      CCP3CAP                                                                 CTS                                                     354
3F76h      CCP3CON             EN             —            OUT            FMT                               MODE                           352
3F75h      CCPR3H                                                                  RH                                                      355
3F74h      CCPR3L                                                                  RL                                                      354
3F73h      CCP4CAP                                                                 CTS                                                     354
3F72h      CCP4CON             EN             —            OUT            FMT                               MODE                           352
3F71h      CCPR4H                                                                  RH                                                      355
3F70h      CCPR4L                                                                  RL                                                      354
3F6Fh              —                                                       Unimplemented
3F6Eh      PWM5CON             EN             —            OUT            POL              —         —               —        —            360
3F6Dh      PWM5DCH             DC9           DC8           DC7            DC6             DC5       DC4             DC3      DC2           362
3F6Dh      PWM5DCH                                                                 DC8                                                     362
3F6Ch      PWM5DCL             DC1           DC0            —              —               —         —               —        —            362
3F6Ch      PWM5DCL                     DC                   —              —               —         —               —        —            362
3F6Bh              —                                                       Unimplemented
3F6Ah      PWM6CON             EN             —            OUT            POL              —         —               —        —            360
3F69h      PWM6DCH                    DC9                  DC7            DC6             DC5       DC4             DC3      DC2           362
3F69h      PWM6DCH                                                                 DC                                                      362
3F68h      PWM6DCL             DC1           DC0            —              —               —         —               —        —            362
3F68h      PWM6DCL                     DC                   —              —               —         —               —        —            362
3F67h              —                                                       Unimplemented
3F66h      PWM7CON             EN             —            OUT            POL              —         —               —        —            360
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                             DS40001919G-page 719
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:          REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                                  Register
 Address      Name            Bit 7            Bit 6       Bit 5            Bit 4         Bit 3            Bit 2         Bit 1            Bit 0
                                                                                                                                                  on page

3F65h      PWM7DCH             DC9             DC8         DC7              DC6           DC5              DC4            DC3             DC2       362
3F65h      PWM7DCH                                                                  DC                                                              362
3F64h      PWM7DCL             DC1             DC0          —                —             —                —             —                —        362
3F64h      PWM7DCL             DC                           —                —             —                —             —                —        362
3F63h           —                                                            Unimplemented
3F62h      PWM8CON             EN               —          OUT              POL            —                —             —                —        360
3F61h      PWM8DCH             DC9             DC8         DC7              DC6           DC5              DC4            DC3             DC2       362
3F61h      PWM8DCH                                                                  DC                                                              362
3F60h      PWM8DCL             DC1             DC0          —                —             —                —             —                —        362
3F60h      PWM8DCL                     DC                   —                —             —                —             —                —        362
3F5Fh      CCPTMRS1                   P8TSEL                       P7TSEL                         P6TSEL                         P5TSEL             361
3F5Eh      CCPTMRS0                   C4TSEL                       C3TSEL                         C2TSEL                         C1TSEL             361
3F5Dh -         —                                                            Unimplemented
3F5Bh
3F5Ah      CWG1STR            OVRD             OVRC       OVRB            OVRA            STRD            STRC           STRB         STRA          430
3F59h      CWG1AS1              —              AS6E        AS5E           AS4E            AS3E            AS2E           AS1E         AS0E          432
3F58h      CWG1AS0         SHUTDOWN            REN                 LSBD                           LSAC                    —                —        431
3F57h      CWG1CON1             —               —           IN               —            POLD            POLC           POLB         POLA          427
3F56h      CWG1CON0            EN               LD          —                —             —                             MODE                       426
3F55h      CWG1DBF              —               —                                                   DBF                                             433
3F54h      CWG1DBR              —               —                                                   DBR                                             433
3F53h      CWG1ISM              —               —           —                —                                     IS                               429
3F52h      CWG1CLK              —               —           —                —             —                —             —               CS        428
3F51h      CWG2STR            OVRD             OVRC       OVRB            OVRA            STRD            STRC           STRB         STRA          430
3F50h      CWG2AS1              —              AS6E        AS5E           AS4E            AS3E            AS2E           AS1E         AS0E          432
3F4Fh      CWG2AS0         SHUTDOWN            REN                 LSBD                           LSAC                    —                —        431
3F4Eh      CWG2CON1             —               —           IN               —            POLD            POLC           POLB         POLA          427
3F4Dh      CWG2CON0            EN               LD          —                —             —                             MODE                       426
3F4Ch      CWG2DBF              —               —                                                   DBF                                             433
3F4Bh      CWG2DBR              —               —                                                   DBR                                             433
3F4Ah      CWG2ISM              —               —           —                —                                     IS                               429
3F49h      CWG2CLK              —               —           —                —             —                —             —               CS        428
3F48h      CWG3STR            OVRD             OVRC       OVRB            OVRA            STRD            STRC           STRB         STRA          430
3F47h      CWG3AS1              —              AS6E        AS5E           AS4E            AS3E            AS2E           AS1E         AS0E          432
3F46h      CWG3AS0         SHUTDOWN            REN                 LSBD                           LSAC                    —                —        431
3F45h      CWG3CON1             —               —           IN               —            POLD            POLC           POLB         POLA          427
3F44h      CWG3CON0            EN               LD          —                —             —                             MODE                       426
3F43h      CWG3DBF              —               —                                                   DBF                                             433
3F42h      CWG3DBR              —               —                                                   DBR                                             433
3F41h      CWG3ISM              —               —           —                —                                     IS                               429
3F40h      CWG3CLK              —               —           —                —             —                —             —               CS        428
3F3Fh      NCO1CLK                             PWS                           —                                     CKS                              456
3F3Eh      NCO1CON             EN               —          OUT              POL            —                —             —               PFM       455
3F3Dh      NCO1INCU                                                                 INC                                                             459
3F3Ch      NCO1INCH                                                                 INC                                                             458
3F3Bh      NCO1INCL                                                                 INC                                                             458
3F3Ah      NCO1ACCU                                                                 ACC                                                             458
3F39h      NCO1ACCH                                                                 ACC                                                             457
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                                    DS40001919G-page 720
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:          REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                             Register
 Address      Name            Bit 7          Bit 6            Bit 5     Bit 4           Bit 3          Bit 2           Bit 1         Bit 0
                                                                                                                                             on page

3F38h      NCO1ACCL                                                              ACC                                                           457
3F37h -         —                                                         Unimplemented
3F24h
3F23h      SMT1WIN              —             —                —                                       WSEL                                    400
3F22h      SMT1SIG              —             —                —                                        SSEL                                   401
3F21h      SMT1CLK              —             —                —         —               —                             CSEL                    399
3F20h      SMT1STAT          CPRUP          CPWUP             RST        —               —              TS             WS             AS       398
3F1Fh      SMT1CON1            GO          REPEAT              —         —                                      MODE                           397
3F1Eh      SMT1CON0            EN             —               STP      WPOL             SPOL           CPOL                    PS              396
3F1Dh      SMT1PRU                                                               PR                                                            405
3F1Ch      SMT1PRH                                                               PR                                                            405
3F1Bh      SMT1PRL                                                               PR                                                            405
3F1Ah      SMT1CPWU                                                              CPW                                                           404
3F19h      SMT1CPWH                                                              CPW                                                           404
3F18h      SMT1CPWL                                                              CPW                                                           404
3F17h      SMT1CPRU                                                              CPR                                                           403
3F16h      SMT1CPRH                                                              CPR                                                           403
3F15h      SMT1CPRL                                                              CPR                                                           403
3F14h      SMT1TMRU                                                              TMR                                                           402
3F13h      SMT1TMRH                                                              TMR                                                           402
3F12h      SMT1TMRL                                                              TMR                                                           402
3F11h -         —                                                         Unimplemented
3F00h
3EFFh      ADCLK                —             —                                                  CS                                            625
3EFEh      ADACT                —             —                —                                        ACT                                    638
3EFDh      ADREF                                      NREF                                                      PREF                           625
3EFCh      ADSTAT            ADAOV           UTHR            LTHR       MATH             —                             STAT                    624
3EFBh      ADCON3               —                            CALC                       SOI                            TMD                     623
3EFAh      ADCON2             PSIS                           CRS                        ACLR                           MODE                    622
3EF9h      ADCON1             PPOL           IPEN            GPOL        —               —              —               —            DSEN      621
3EF8h      ADCON0              ON            CONT              —         CS                      FM                     —            GO        620
3EF7h      ADPREH               —             —                —                                        PRE                                    627
3EF6h      ADPREL                                                                PRE                                                           627
3EF5h      ADCAP                —             —                —                                        CAP                                    629
3EF4h      ADACQH               —             —                —                                        ACQ                                    628
3EF3h      ADACQL                                                                ACQ                                                           628
3EF2h           —                                                         Unimplemented
3EF1h      ADPCH                —             —                                                  PCH                                           626
3EF0h      ADRESH                                                                RES                                                           631
3EEFh      ADRESL                                                                RES                                                           631
3EEEh      ADPREVH                                                               PREV                                                          633
3EEDh      ADPREVL                                                               PREV                                                          633
3EECh      ADRPT                                                                 RPT                                                           629
3EEBh      ADCNT                                                                 CNT                                                           630
3EEAh      ADACCU             (sign)         (sign)          (sign)     (sign)          (sign)         (sign)                  ACC             634
3EE9h      ADACCH                                                                ACC                                                           634
3EE8h      ADACCL                                                                ACC                                                           635
3EE7h      ADFLTRH                                                               FLTR                                                          630
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                              DS40001919G-page 721
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                                Register
 Address      Name            Bit 7          Bit 6         Bit 5         Bit 4           Bit 3           Bit 2          Bit 1           Bit 0
                                                                                                                                                on page

3EE6h      ADFLTRL                                                               FLTR                                                             630
3EE5h      ADSTPTH                                                               STPT                                                             635
3EE4h      ADSTPTL                                                               STPT                                                             635
3EE3h      ADERRH                                                                ERR                                                              636
3EE2h      ADERRL                                                                ERR                                                              636
3EE1h      ADUTHH                                                                UTH                                                              637
3EE0h      ADUTHL                                                                UTH                                                              637
3EDFh      ADLTHH                                                                LTH                                                              636
3EDEh      ADLTHL                                                                LTH                                                              637
3EDDh -            —                                                      Unimplemented
3ED8h
3ED7h      ADCP                ON             —             —             —               —               —              —             CPRDY      639
3ED6h -            —                                                      Unimplemented
3ECBh
3ECAh      HLVDCON1             —             —             —             —                                      SEL                              661
3EC9h      HLVDCON0            EN             —            OUT           RDY              —               —             INTH            INTL      660
3EC8h -            —                                                      Unimplemented
3EC4h
3EC3h      ZCDCON              SEN            —            OUT            POL             —               —             INTP            INTN      464
3EC2h              —                                                      Unimplemented
3EC1h      FVRCON              EN            RDY           TSEN          TSRNG                   CDAFVR                         ADFVR             600
3EC0h      CMOUT                —             —             —             —               —               —            C2OUT           C1OUT      653
3EBFh      CM1PCH               —             —             —             —               —                             PCH                       653
3EBEh      CM1NCH               —             —             —             —               —                             NCH                       652
3EBDh      CM1CON1              —             —             —             —               —               —             INTP            INTN      652
3EBCh      CM1CON0             EN            OUT            —             POL             —               —             HYS             SYNC      651
3EBBh      CM2PCH               —             —             —             —               —                             PCH                       653
3EBAh      CM2NCH               —             —             —             —               —                             NCH                       652
3EB9h      CM2CON1              —             —             —             —               —               —             INTP            INTN      652
3EB8h      CM2CON0             EN            OUT            —             POL             —               —             HYS             SYNC      651
3EB7h -            —                                                      Unimplemented
3E9Fh
3E9Eh      DAC1CON0            EN             —            OE1            OE2                     PSS                    —              NSS       643
3E9Dh              —                                                      Unimplemented
3E9Ch      DAC1CON1             —             —             —                                             DATA                                    644
3E9Bh -            —                                                      Unimplemented
3DFBh
3DFAh      U1ERRIE           TXMTIE         PERIE        ABDOVE          CERIE          FERIE           RXBKIE      RXFOIE             TXCIE      504
3DF9h      U1ERRIR           TXMTIF         PERIF        ABDOVF          CERIF          FERIF           RXBKIF         RXFOIF          TXCIF      503
3DF8h      U1UIR              WUIF          ABDIF           —             —               —             ABDIE            —               —        505
3DF7h      U1FIFO            TXWRE          STPMD          TXBE          TXBF           RXIDL            XON           RXBE             RXBF      506
3DF6h      U1BRGH                                                                BRGH                                                             507
3DF5h      U1BRGL                                                                BRGL                                                             507
3DF4h      U1CON2           RUNOVF          RXPOL                  STP                  C0EN            TXPOL                    FLO              502
3DF3h      U1CON1              ON             —             —            WUE            RXBIMD            —        BRKOVR              SENDB      501
3DF2h      U1CON0             BRGS          ABDEN          TXEN          RXEN                                    MODE                             500
3DF1h      U1P3H                —             —             —             —               —               —              —              P3H       511
3DF0h      U1P3L                                                                 P3L                                                              511
3DEFh      U1P2H                —             —             —             —               —               —              —              P2H       510
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                                  DS40001919G-page 722
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                                  Register
 Address       Name            Bit 7          Bit 6         Bit 5          Bit 4           Bit 3           Bit 2          Bit 1           Bit 0
                                                                                                                                                  on page

3DEEh      U1P2L                                                                    P2L                                                             510
3DEDh      U1P1H                 —             —             —              —               —               —              —              P1H       509
3DECh      U1P1L                                                                    P1L                                                             509
3DEBh      U1TXCHK                                                                 TXCHK                                                            512
3DEAh      U1TXB                                                                    TXB                                                             508
3DE9h      U1RXCHK                                                                 RXCHK                                                            512
3DE8h      U1RXB                                                                    RXB                                                             508
3DE7h -            —                                                        Unimplemented
3DE3h
3DE2h      U2ERRIE            TXMTIE         PERIE        ABDOVE          CERIE            FERIE       RXBKIE         RXFOIE             TXCIE      504
3DE1h      U2ERRIR            TXMTIF         PERIF        ABDOVF          CERIF            FERIF       RXBKIF         RXFOIF              TXCIF     503
3DE0h      U2UIR               WUIF          ABDIF           —              —               —          ABDIE               —               —        505
3DDFh      U2FIFO             TXWRE          STPMD          TXBE          TXBF            RXIDL            XON        RXBE                RXBF      506
3DDEh      U2BRGH                                                                  BRGH                                                             507
3DDDh      U2BRGL                                                                  BRGL                                                             507
3DDCh      U2CON2            RUNOVF          RXPOL                  STP                     —          TXPOL                       FLO              502
3DDBh      U2CON1               ON             —             —             WUE            RXBIMD            —        BRKOVR              SENDB      501
3DDAh      U2CON0              BRGS          ABDEN          TXEN          RXEN                                     MODE                             500
3DD9h              —                                                        Unimplemented
3DD8h      U2P3L                                                                    P3L                                                             510
3DD7h              —                                                        Unimplemented
3DD6h      U2P2L                                                                    P2L                                                             510
3DD5h              —                                                        Unimplemented
3DD4h      U2P1L                                                                    P1L                                                             509
3DD3h              —                                                        Unimplemented
3DD2h      U2TXB                                                                    TXB                                                             508
3DD1h              —                                                        Unimplemented
3DD0h      U2RXB                                                                    RXB                                                             508
3DCFh -            —                                                        Unimplemented
3D7Dh
3D7Ch      I2C1BTO                                                                  BTO                                                             585
3D7Bh      I2C1CLK                                                                  CLK                                                             584
3D7Ah      I2C1PIE             CNTIE         ACKTIE          —            WRIE            ADRIE            PCIE       RSCIE               SCIE      591
3D79h      I2C1PIR             CNTIF         ACKTIF          —            WRIF            ADRIF            PCIF       RSCIF               SCIF      590
3D78h      I2C1STAT1           TXWE            —            TXBE            —              RXRE        CLRBF               —              RXBF      587
3D77h      I2C1STAT0           BFRE           SMA           MMA             R               D               —              —               —        586
3D76h      I2C1ERR               —           BTOIF         BCLIF          NACKIF            —          BTOIE          BCLIE              NACKIE     588
3D75h      I2C1CON2            ACNT          GCEN           FME            ABD                     SDAHT                          BFRET             583
3D74h      I2C1CON1          ACKCNT          ACKDT        ACKSTAT         ACKT              —              RXO            TXU             CSD       582
3D73h      I2C1CON0             EN            RSEN            S           CSTR             MDR                            MODE                      580
3D72h      I2C1ADR3                                                       ADR                                                              —        595
3D71h      I2C1ADR2                                                                ADR                                                              594
3D70h      I2C1ADR1                                                       ADR                                                              —        593
3D6Fh      I2C1ADR0                                                                ADR                                                              592
3D6Eh      I2C1ADB1                                                                 ADB                                                             597
3D6Dh      I2C1ADB0                                                                 ADB                                                             596
3D6Ch      I2C1CNT                                                                  CNT                                                             589
3D6Bh      I2C1TXB                                                                  TXB
Legend:      x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:      Unimplemented in LF devices.
      2:     Unimplemented in PIC18(L)F26K42.
      3:     Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:     Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                                 DS40001919G-page 723
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:           REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                                Register
 Address       Name            Bit 7          Bit 6         Bit 5        Bit 4            Bit 3           Bit 2         Bit 1           Bit 0
                                                                                                                                                on page

3D6Ah      I2C1RXB                                                                RXB
3D69h -          —                                                         Unimplemented
3D67h
3D66h      I2C2BTO                                                                BTO                                                             585
3D65h      I2C2CLK                                                                CLK                                                             584
3D64h      I2C2PIE             CNTIE         ACKTIE          —           WRIE            ADRIE            PCIE          RSCIE           SCIE      591
3D63h      I2C2PIR             CNTIF         ACKTIF          —           WRIF            ADRIF            PCIF          RSCIF           SCIF      590
3D62h      I2C2STAT1           TXWE            —             —            —              RXRE         CLRBF              —              RXBF      587
3D61h      I2C2STAT0           BFRE            —            MMA           —                D               —             —               —        586
3D60h      I2C2ERR               —           BTOIF         BCLIF        NACKIF             —          BTOIE             BCLIE       NACKIE        588
3D5Fh      I2C2CON2            ACNT          GCEN           FME          ABD                      SDAHT                         BFRET             583
3D5Eh      I2C2CON1          ACKCNT          ACKDT        ACKSTAT        ACKT              —              RXO            TXU            CSD       582
3D5Dh      I2C2CON0             EN            RSEN            S          CSTR             MDR                           MODE                      580
3D5Ch      I2C2ADR3                                                     ADR                                                              —        595
3D5Bh      I2C2ADR2                                                               ADR                                                             594
3D5Ah      I2C2ADR1                                                     ADR                                                              —        593
3D59h      I2C2ADR0                                                               ADR                                                             592
3D58h      I2C2ADB1                                                               ADB                                                             597
3D57h      I2C2ADB0                                                               ADB                                                             596
3D56h      I2C2CNT                                                                CNT                                                             589
3D55h      I2C2TXB                                                                TXB
3D54h      I2C2RXB                                                                RXB
3D53h -          —                                                         Unimplemented
3D1Dh
3D1Ch      SPI1CLK                                                               CLKSEL                                                           544
3D1Bh      SPI1INTE           SRMTIE         TCZIE         SOSIE        EOSIE              —          RXOIE             TXUIE            —        538
3D1Ah      SPI1INTF           SRMTIF          TCZIF        SOSIF        EOSIF              —          RXOIF             TXUIF            —        537
3D19h      SPI1BAUD                                                              BAUD                                                             540
3D18h      SPI1TWIDTH            —             —             —            —                —                            TWIDTH                    539
3D17h      SPI1STATUS          TXWE            —            TXBE          —              RXRE         CLRBF              —              RXBF      543
3D16h      SPI1CON2            BUSY          SSFLT           —            —                —              SSET           TXR            RXR       542
3D15h      SPI1CON1            SMP            CKE           CKP          FST               —              SSP           SDIP            SDOP      541
3D14h      SPI1CON0             EN             —             —            —                —              LSBF           MST        BMODE         540
3D13h      SPI1TCNTH             —             —             —            —                —                            TCNTH                     539
3D12h      SPI1TCNTL                                                             TCNTL                                                            538
3D11h      SPI1TXB                                                                TXB                                                             544
3D10h      SPI1RXB                                                                RXB                                                             543
3D0Fh -          —                                                         Unimplemented
3CFFh
3CFEh      MD1CARH               —             —             —                                              CH                                    473
3CFDh      MD1CARL               —             —             —                                              CL                                    473
3CFCh      MD1SRC                —             —             —                                              MS                                    474
3CFBh      MD1CON1               —             —           CHPOL       CHSYNC              —               —            CLPOL       CLSYNC        472
3CFAh      MD1CON0              EN             —            OUT          OPOL              —               —             —              BIT       471
3CF9h -          —                                                         Unimplemented
3CE7h
3CE6h      CLKRCON              EN             —             —                    DC                                     DIV                      113
3CE5h      CLKRCLK               —             —             —            —                                       CLK                             114
Legend:      x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:      Unimplemented in LF devices.
      2:     Unimplemented in PIC18(L)F26K42.
      3:     Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:     Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                                   DS40001919G-page 724
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:          REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                               Register
 Address      Name            Bit 7          Bit 6         Bit 5        Bit 4         Bit 3    Bit 2     Bit 1     Bit 0
                                                                                                                               on page

3CE4h -         —                                                         Unimplemented
3C7Fh
3C7Eh      CLCDATA0             —             —             —            —         CLC4OUT    CLC3OUT   CLC2OUT   CLC1OUT        449
3C7Dh      CLC1GLS3          G4D4T          G4D4N         G4D3T        G4D3N          G4D2T    G4D2N     G4D1T     G4D1N         448
3C7Ch      CLC1GLS2          G3D4T          G3D4N         G3D3T        G3D3N          G3D2T    G3D2N     G3D1T     G3D1N         447
3C7Bh      CLC1GLS1          G2D4T          G2D4N         G2D3T        G2D3N          G2D2T    G2D2N     G2D1T     G2D1N         446
3C7Ah      CLC1GLS0          G1D4T          G1D4N         G1D3T        G1D3N          G1D2T    G1D2N     G1D1T     G1D1N         445
3C79h      CLC1SEL3                                                             D4S                                              444
3C78h      CLC1SEL2                                                             D3S                                              444
3C77h      CLC1SEL1                                                             D2S                                              444
3C76h      CLC1SEL0                                                             D1S                                              444
3C75h      CLC1POL             POL            —             —            —            G4POL    G3POL     G2POL     G1POL         443
3C74h      CLC1CON             EN             OE           OUT          INTP          INTN               MODE                    442
3C73h      CLC2GLS3          G4D4T          G4D4N         G4D3T        G4D3N          G4D2T    G4D2N     G4D1T     G4D1N         448
3C72h      CLC2GLS2          G3D4T          G3D4N         G3D3T        G3D3N          G3D2T    G3D2N     G3D1T     G3D1N         447
3C71h      CLC2GLS1          G2D4T          G2D4N         G2D3T        G2D3N          G2D2T    G2D2N     G2D1T     G2D1N         446
3C70h      CLC2GLS0          G1D4T          G1D4N         G1D3T        G1D3N          G1D2T    G1D2N     G1D1T     G1D1N         445
3C6Fh      CLC2SEL3                                                             D4S                                              444
3C6Eh      CLC2SEL2                                                             D3S                                              444
3C6Dh      CLC2SEL1                                                             D2S                                              444
3C6Ch      CLC2SEL0                                                             D1S                                              444
3C6Bh      CLC2POL             POL            —             —            —            G4POL    G3POL     G2POL     G1POL         443
3C6Ah      CLC2CON             EN             OE           OUT          INTP          INTN               MODE                    442
3C69h      CLC3GLS3          G4D4T          G4D4N         G4D3T        G4D3N          G4D2T    G4D2N     G4D1T     G4D1N         448
3C68h      CLC3GLS2          G3D4T          G3D4N         G3D3T        G3D3N          G3D2T    G3D2N     G3D1T     G3D1N         447
3C67h      CLC3GLS1          G2D4T          G2D4N         G2D3T        G2D3N          G2D2T    G2D2N     G2D1T     G2D1N         446
3C66h      CLC3GLS0          G1D4T          G1D4N         G1D3T        G1D3N          G1D2T    G1D2N     G1D1T     G1D1N         445
3C65h      CLC3SEL3                                                             D4S                                              444
3C64h      CLC3SEL2                                                             D3S                                              444
3C63h      CLC3SEL1                                                             D2S                                              444
3C62h      CLC3SEL0                                                             D1S                                              445
3C61h      CLC3POL             POL            —             —            —            G4POL    G3POL     G2POL     G1POL         443
3C60h      CLC3CON             EN             OE           OUT          INTP          INTN               MODE                    442
3C5Fh      CLC4GLS3          G4D4T          G4D4N         G4D3T        G4D3N          G4D2T    G4D2N     G4D1T     G4D1N         448
3C5Eh      CLC4GLS2          G3D4T          G3D4N         G3D3T        G3D3N          G3D2T    G3D2N     G3D1T     G3D1N         447
3C5Dh      CLC4GLS1          G2D4T          G2D4N         G2D3T        G2D3N          G2D2T    G2D2N     G2D1T     G2D1N         446
3C5Ch      CLC4GLS0          G1D4T          G1D4N         G1D3T        G1D3N          G1D2T    G1D2N     G1D1T     G1D1N         445
3C5Bh      CLC4SEL3                                                             D4S                                              444
3C5Ah      CLC4SEL2                                                             D3S                                              444
3C59h      CLC4SEL1                                                             D2S                                              444
3C58h      CLC4SEL0                                                             D1S                                              445
3C57h      CLC4POL             POL            —             —            —            G4POL    G3POL     G2POL     G1POL         443
3C56h      CLC4CON             EN             OE           OUT          INTP          INTN               MODE                    442
3C55h -         —                                                         Unimplemented
3C00h
3BFFh      DMA1SIRQ             —                                                      SIRQ                                      258
3BFEh      DMA1AIRQ             —                                                      AIRQ                                      258
3BFDh      DMA1CON1            EN           SIRQEN         DGO           —             —      AIRQEN      —         XIP          251
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 725
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:         REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                             Register
 Address      Name            Bit 7           Bit 6        Bit 5        Bit 4          Bit 3           Bit 2           Bit 1     Bit 0
                                                                                                                                             on page

3BFCh      DMA1CON0                   DMODE                DSTP                 SMR                            SMODE             SSTP          250
3BFBh      DMA1SSAU             —              —                                                 SSA                                           253
3BFAh      DMA1SSAH                                                             SSA                                                            252
3BF9h      DMA1SSAL                                                             SSA                                                            252
3BF8h      DMA1SSZH             —              —            —            —                                      SSZ                            254
3BF7h      DMA1SSZL                                                             SSZ                                                            254
3BF6h      DMA1SPTRU            —              —                                                SPTR                                           254
3BF5h      DMA1SPTRH                                                            SPTR                                                           253
3BF4h      DMA1SPTRL                                                            SPTR                                                           253
3BF3h      DMA1SCNTH            —              —            —            —                                      SCNT                           255
3BF2h      DMA1SCNTL                                                            SCNT                                                           255
3BF1h      DMA1DSAH                                                             DSA                                                            256
3BF0h      DMA1DSAL                                                             SSA                                                            255
3BEFh      DMA1DSZH             —              —            —            —                                      DSZ                            257
3BEEh      DMA1DSZL                                                             DSZ                                                            257
3BEDh      DMA1DPTRH                                                            DPTR                                                           256
3BECh      DMA1DPTRL                                                            DPTR                                                           256
3BEBh      DMA1DCNTH            —              —            —            —                                      DCNT                           258
3BEAh      DMA1DCNTL                                                            DCNT                                                           257
3BE9h      DMA1BUF                                                              BUF                                                            252
3BE8h -         —                                                         Unimplemented
3BE0h
3BDFh      DMA2SIRQ             —                                                      SIRQ                                                    258
3BDEh      DMA2AIRQ             —                                                      AIRQ                                                    258
3BDDh      DMA2CON1            EN           SIRQEN         DGO           —              —          AIRQEN               —        XIP           251
3BDCh      DMA2CON0                   DMODE                DSTP                 SMR                            SMODE             SSTP          250
3BDBh      DMA2SSAU             —              —                                                 SSA                                           253
3BDAh      DMA2SSAH                                                             SSA                                                            252
3BD9h      DMA2SSAL                                                             SSA                                                            252
3BD8h      DMA2SSZH             —              —            —            —                                      SSZ                            254
3BD7h      DMA2SSZL                                                             SSZ                                                            254
3BD6h      DMA2SPTRU            —              —                                                SPTR                                           254
3BD5h      DMA2SPTRH                                                            SPTR                                                           253
3BD4h      DMA2SPTRL                                                            SPTR                                                           253
3BD3h      DMA2SCNTH            —              —            —            —                                      SCNT                           255
3BD2h      DMA2SCNTL                                                            SCNT                                                           255
3BD1h      DMA2DSAH                                                             DSA                                                            256
3BD0h      DMA2DSAL                                                             SSA                                                            255
3BCFh      DMA2DSZH             —              —            —            —                                      DSZ                            257
3BCEh      DMA2DSZL                                                             DSZ                                                            257
3BCDh      DMA2DPTRH                                                            DPTR                                                           256
3BCCh      DMA2DPTRL                                                            DPTR                                                           256
3BCBh      DMA2DCNTH            —              —            —            —                                      DCNT                           258
3BCAh      DMA2DCNTL                                                            DCNT                                                           257
3BC9h      DMA2BUF                                                              BUF                                                            252
3BC8h -         —                                                         Unimplemented
3AEBh
3AEAh      U2CTSPPS             —              —                                               U2CTSPPS                                        279
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                                 DS40001919G-page 726
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:          REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                    Register
 Address      Name            Bit 7          Bit 6         Bit 5        Bit 4        Bit 3         Bit 2      Bit 1      Bit 0
                                                                                                                                    on page

3AE8h      U2RXPPS              —             —                                              U2RXPPS                                  279
3AE7h      U1CTSPPS             —             —                                              U1CTSPPS                                 279
3AE5h      U1RXPPS              —             —                                              U1RXPPS                                  279
3AE4h      I2C2SDAPPS           —             —                                             I2C2SDAPPS                                279
3AE3h      I2C2SCLPPS           —             —                                             I2C2SCLPPS                                279
3AE2h      I2C1SDAPPS           —             —                                             I2C1SDAPPS                                279
3AE1h      I2C1SCLPPS           —             —                                             I2C1SCLPPS                                279
3AE0h      SPI1SSPPS            —             —                                              SPI1SSPPS                                279
3ADFh      SPI1SDIPPS           —             —                                             SPI1SDIPPS                                279
3ADEh      SPI1SCKPPS           —             —                                             SPI1SCKPPS                                279
3ADDh      ADACTPPS             —             —                                              ADACTPPS                                 279
3ADCh      CLCIN3PPS            —             —                                              CLCIN3PPS                                279
3ADBh      CLCIN2PPS            —             —                                              CLCIN2PPS                                279
3ADAh      CLCIN1PPS            —             —                                              CLCIN1PPS                                279
3AD9h      CLCIN0PPS            —             —                                              CLCIN0PPS                                279
3AD8h      MD1SRCPPS            —             —                                             MD1SRCPPS                                 279
3AD7h      MD1CARHPPS           —             —                                           MD1CARHPPS                                  279
3AD6h      MD1CARLPPS           —             —                                             MD1CARLPPS                                279
3AD5h      CWG3INPPS            —             —                                             CWG3INPPS                                 279
3AD4h      CWG2INPPS            —             —                                             CWG2INPPS                                 279
3AD3h      CWG1INPPS            —             —                                             CWG1INPPS                                 279
3AD2h      SMT1SIGPPS           —             —                                             SMT1SIGPPS                                279
3AD1h      SMT1WINPPS           —             —                                             SMT1WINPPS                                279
3AD0h      CCP4PPS              —             —                                              CCP4PPS                                  279
3ACFh      CCP3PPS              —             —                                              CCP3PPS                                  279
3ACEh      CCP2PPS              —             —                                              CCP2PPS                                  279
3ACDh      CCP1PPS              —             —                                              CCP1PPS                                  279
3ACCh      T6INPPS              —             —                                               T6INPPS                                 279
3ACBh      T4INPPS              —             —                                               T4INPPS                                 279
3ACAh      T2INPPS              —             —                                               T2INPPS                                 279
3AC9h      T5GPPS               —             —                                               T5GPPS                                  279
3AC8h      T5CLKIPPS            —             —                                              T5CLKIPPS                                279
3AC7h      T3GPPS               —             —                                               T3GPPS                                  279
3AC6h      T3CLKIPPS            —             —                                              T3CLKIPPS                                279
3AC5h      T1GPPS               —             —                                               T1GPPS                                  279
3AC4h      T1CLKIPPS            —             —                                              T1CLKIPPS                                279
3AC3h      T0CLKIPPS            —             —                                              T0CLKIPPS                                279
3AC2h      INT2PPS              —             —                                               INT2PPS                                 279
3AC1h      INT1PPS              —             —                                               INT1PPS                                 279
3AC0h      INT0PPS              —             —                                               INT0PPS                                 279
3ABFh      PPSLOCK              —             —             —            —            —                —       —       PPSLOCKED      285
3ABEh-          —                                                         Unimplemented
3A95h
3A94h        INLVLF(3)       INLVLF7       INLVLF6       INLVLF5      INLVLF4      INLVLF3        INLVLF2    INLVLF1    INLVLF0       272
3A93h       SLRCONF(3)     SLRCONF7       SLRCONF6      SLRCONF5 SLRCONF4 SLRCONF3               SLRCONF2   SLRCONF1   SLRCONF0       271
3A92h       ODCONF(3)       ODCONF7       ODCONF6       ODCONF5      ODCONF4      ODCONF3        ODCONF2    ODCONF1    ODCONF0        270
3A91h        WPUF(3)         WPUF7          WPUF6         WPUF5        WPUF4        WPUF3         WPUF2      WPUF1      WPUF0         269
3A90h        ANSELF(3)      ANSELF7        ANSELF6       ANSELF5      ANSELF4      ANSELF3        ANSELF2   ANSELF1     ANSELF0       268
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                        DS40001919G-page 727
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                        Register
 Address       Name            Bit 7          Bit 6         Bit 5         Bit 4       Bit 3     Bit 2        Bit 1             Bit 0
                                                                                                                                        on page

3A8Fh-             —                                                       Unimplemented
3A88h
3A87h      IOCEF                 —             —             —             —         IOCEF3      —            —                 —         289
3A86h      IOCEN                 —             —             —             —         IOCEN3      —            —                 —         289
3A85h      IOCEP                 —             —             —             —         IOCEP3      —            —                 —         289
3A84h      INLVLE                —             —             —             —        INLVLE3   INLVLE2(2)   INLVLE1(2)    INLVLE0(2)       272
3A83h      SLRCONE(2)            —             —             —             —           —      SRLE2(2)     SRLE1(2)          SRLE0(2)     271
3A82h      ODCONE(2)             —             —             —             —           —      ODCE2(2)     ODCE1(2)          ODCE0(2)     270
3A81h      WPUE                  —             —             —             —         WPUE3    WPUE2(2)     WPUE1(2)          WPUE0(2)     269
3A80h      ANSELE(2)         ANSELE7        ANSELE6       ANSELE5        ANSELE4    ANSELE3   ANSELE2      ANSELE1           ANSELE0      268
3A7Fh-             —                                                       Unimplemented
3A7CH
3A7Bh      RD1I2C(2)             —           IOCEN3                 PU                 —         —                      TH                265
3A7Ah      RD0I2C(2)             —           IOCEN3                 PU                 —         —                      TH                265
3A79h-             —                                                       Unimplemented
3A75h
3A74h      INLVLD(2)         INLVLD7        INLVLD6       INLVLD5        INLVLD4    INLVLD3   INLVLD2      INLVLD1           INLVLD0      272
3A73h      SLRCOND(2)         SRLD7          SRLD6         SRLD5          SRLD4      SRLD3     SRLD2        SRLD1             SRLD0       271
3A72h      ODCOND(2)          ODCD7          ODCD6         ODCD5         ODCD4       ODCD3     ODCD2        ODCD1            ODCD0        270
3A71h      WPUD(2)            WPUD7          WPUD6         WPUD5         WPUD4       WPUD3     WPUD2        WPUD1            WPUD0        269
3A70h      ANSELD(2)         ANSELD7        ANSELD6       ANSELD5        ANSELD4    ANSELD3   ANSELD2      ANSELD1           ANSELD0      268
3A6Fh-             —                                                       Unimplemented
3A6Ch
3A6Bh      RC4I2C                —            SLEW                  PU                 —         —                      TH                265
3A6Ah      RC3I2C                —            SLEW                  PU                 —         —                      TH                265
3A69h              —                                                       Unimplemented
3A68h              —                                                       Unimplemented
3A67h      IOCCF              IOCCF7         IOCCF6        IOCCF5        IOCCF4      IOCCF3    IOCCF2       IOCCF1           IOCCF0       289
3A66h      IOCCN              IOCCN7         IOCCN6       IOCCN5         IOCCN4     IOCCN3     IOCCN2       IOCCN1           IOCCN0       289
3A65h      IOCCP              IOCCP7         IOCCP6        IOCCP5        IOCCP4      IOCCP3    IOCCP2       IOCCP1           IOCCP0       289
3A64h      INLVLC            INLVLC7        INLVLC6       INLVLC5        INLVLC4    INLVLC3   INLVLC2      INLVLC1           INLVLC0      272
3A63h      SLRCONC            SLRC7          SLRC6         SLRC5          SLRC4      SLRC3     SLRC2        SLRC1             SLRC0       271
3A62h      ODCONC             ODCC7          ODCC6         ODCC5         ODCC4       ODCC3     ODCC2        ODCC1            ODCC0        270
3A61h      WPUC               WPUC7          WPUC6         WPUC5         WPUC4       WPUC3     WPUC2        WPUC1            WPUC0        269
3A60h      ANSELC            ANSELC7        ANSELC6       ANSELC5        ANSELC4    ANSELC3   ANSELC2      ANSELC1           ANSELC0      268
3A5Fh -            —                                                       Unimplemented
3A5Ch
3A5Bh      RB2I2C                —            SLEW                  PU                 —         —                      TH                265
3A5Ah      RB1I2C                —            SLEW                  PU                 —         —                      TH                265
3A59h              —                                                       Unimplemented
3A58h              —                                                       Unimplemented
3A57h      IOCBF              IOCBF7         IOCBF6        IOCBF5        IOCBF4      IOCBF3    IOCBF2       IOCBF1           IOCBF0       289
3A56h      IOCBN              IOCBN7         IOCBN6        IOCBN5        IOCBN4      IOCBN3    IOCBN2       IOCBN1           IOCBN0       289
3A55h      IOCBP              IOCBP7         IOCBP6        IOCBP5        IOCBP4      IOCBP3    IOCBP2       IOCBP1           IOCBP0       289
3A54h      INLVLB             INLVLB7       INLVLB6       INLVLB5        INLVLB4    INLVLB3    INLVLB2      INLVLB1          INLVLB0      272
3A53h      SLRCONB            SLRB7          SLRB6         SLRB5          SLRB4      SLRB3     SLRB2        SLRB1             SLRB0       271
3A52h      ODCONB             ODCB7          ODCB6         ODCB5         ODCB4       ODCB3     ODCB2        ODCB1            ODCB0        270
3A51h      WPUB               WPUB7          WPUB6         WPUB5         WPUB4       WPUB3     WPUB2        WPUB1            WPUB0        269
3A50h      ANSELB            ANSELB7        ANSELB6       ANSELB5        ANSELB4    ANSELB3   ANSELB2      ANSELB1           ANSELB0      268
Legend:      x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:      Unimplemented in LF devices.
      2:     Unimplemented in PIC18(L)F26K42.
      3:     Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:     Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 728
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                               Register
 Address       Name            Bit 7          Bit 6         Bit 5        Bit 4        Bit 3    Bit 2     Bit 1     Bit 0
                                                                                                                               on page

3A4Fh -            —                                                       Unimplemented
3A48h
3A47h      IOCAF              IOCAF7         IOCAF6        IOCAF5       IOCAF4       IOCAF3   IOCAF2    IOCAF1    IOCAF0         289
3A46h      IOCAN              IOCAN7         IOCAN6        IOCAN5       IOCAN4       IOCAN3   IOCAN2    IOCAN1    IOCAN0         289
3A45h      IOCAP              IOCAP7         IOCAP6        IOCAP5       IOCAP4       IOCAP3   IOCAP2    IOCAP1    IOCAP0         289
3A44h      INLVLA             INLVLA7       INLVLA6       INLVLA5      INLVLA4      INLVLA3   INLVLA2   INLVLA1   INLVLA0        272
3A43h      SLRCONA            SLRA7          SLRA6         SLRA5        SLRA4        SLRA3     SLRA2     SLRA1     SLRA0         271
3A42h      ODCONA             ODCA7          ODCA6         ODCA5        ODCA4        ODCA3    ODCA2     ODCA1     ODCA0          270
3A41h      WPUA               WPUA7          WPUA6         WPUA5        WPUA4        WPUA3    WPUA2     WPUA1     WPUA0          269
3A40h      ANSELA            ANSELA7        ANSELA6       ANSELA5      ANSELA4      ANSELA3   ANSELA2   ANSELA1   ANSELA0        268
3A3Fh -            —                                                       Unimplemented
3A30h
3A2Fh      RF7PPS(3)             —             —          RF7PPS5      RF7PPS4      RF7PPS3   RF7PPS2   RF7PPS1   RF7PPS0        282
3A2Eh      RF6PPS(3)             —             —          RF6PPS5      RF6PPS4      RF6PPS3   RF6PPS2   RF6PPS1   RF6PPS0        282
3A2Dh      RF5PPS(3)             —             —          RF5PPS5      RF5PPS4      RF5PPS3   RF5PPS2   RF5PPS1   RF5PPS0        282
3A2Ch      RF4PPS(3)             —             —          RF4PPS5      RF4PPS4      RF4PPS3   RF4PPS2   RF4PPS1   RF4PPS0        282
3A2Bh      RF3PPS(3)             —             —          RF3PPS5      RF3PPS4      RF3PPS3   RF3PPS2   RF3PPS1   RF3PPS0        282
3A2Ah      RF2PPS(3)             —             —          RF2PPS5      RF2PPS4      RF2PPS3   RF2PPS2   RF2PPS1   RF2PPS0        282
3A29h      RF1PPS(3)             —             —          RF1PPS5      RF1PPS4      RF1PPS3   RF1PPS2   RF1PPS1   RF1PPS0        282
3A28h      RF0PPS(3)             —             —          RF0PPS5      RF0PPS4      RF0PPS3   RF0PPS2   RF0PPS1   RF0PPS0        282
3A27h-             —                                                       Unimplemented
3A23h
3A22h      RE2PPS(2)             —             —          RE2PPS5      RE2PPS4      RE2PPS3   RE2PPS2   RE2PPS1   RE2PPS0        282
3A21h      RE1PPS(2)             —             —          RE1PPS5      RE1PPS4      RE1PPS3   RE1PPS2   RE1PPS1   RE1PPS0        282
3A20h      RE0PPS(2)             —             —          RE0PPS5      RE0PPS4      RE0PPS3   RE0PPS2   RE0PPS1   RE0PPS0        282
3A1Fh      RD7PPS(2)             —             —          RD7PPS5      RD7PPS4      RD7PPS3   RD7PPS2   RD7PPS1   RD7PPS0        282
3A1Eh      RD6PPS(2)             —             —          RD6PPS5      RD6PPS4      RD6PPS3   RD6PPS2   RD6PPS1   RD6PPS0        282
3A1Dh      RD5PPS(2)             —             —          RD5PPS5      RD5PPS4      RD5PPS3   RD5PPS2   RD5PPS1   RD5PPS0        282
3A1Ch      RD4PPS(2)             —             —          RD4PPS5      RD4PPS4      RD4PPS3   RD4PPS2   RD4PPS1   RD4PPS0        282
3A1Bh      RD3PPS(2)             —             —          RD3PPS5      RD3PPS4      RD3PPS3   RD3PPS2   RD3PPS1   RD3PPS0        282
3A1Ah      RD2PPS(2)             —             —          RD2PPS5      RD2PPS4      RD2PPS3   RD2PPS2   RD2PPS1   RD2PPS0        282
3A19h      RD1PPS(2)             —             —          RD1PPS5      RD1PPS4      RD1PPS3   RD1PPS2   RD1PPS1   RD1PPS0        282
3A18h      RD0PPS(2)             —             —          RD0PPS5      RD0PPS4      RD0PPS3   RD0PPS2   RD0PPS1   RD0PPS0        282
3A17h      RC7PPS                —             —          RC7PPS5      RC7PPS4      RC7PPS3   RC7PPS2   RC7PPS1   RC7PPS0        282
3A16h      RC6PPS                —             —          RC6PPS5      RC6PPS4      RC6PPS3   RC6PPS2   RC6PPS1   RC6PPS0        282
3A15h      RC5PPS                —             —          RC5PPS5      RC5PPS4      RC5PPS3   RC5PPS2   RC5PPS1   RC5PPS0        282
3A14h      RC4PPS                —             —          RC4PPS5      RC4PPS4      RC4PPS3   RC4PPS2   RC4PPS1   RC4PPS0        282
3A13h      RC3PPS                —             —          RC3PPS5      RC3PPS4      RC3PPS3   RC3PPS2   RC3PPS1   RC3PPS0        282
3A12h      RC2PPS                —             —          RC2PPS5      RC2PPS4      RC2PPS3   RC2PPS2   RC2PPS1   RC2PPS0        282
3A11h      RC1PPS                —             —          RC1PPS5      RC1PPS4      RC1PPS3   RC1PPS2   RC1PPS1   RC1PPS0        282
3A10h      RC0PPS                —             —          RC0PPS5      RC0PPS4      RC0PPS3   RC0PPS2   RC0PPS1   RC0PPS0        282
3A0Fh      RB7PPS                —             —          RB7PPS5      RB7PPS4      RB7PPS3   RB7PPS2   RB7PPS1   RB7PPS0        282
3A0Eh      RB6PPS                —             —          RB6PPS5      RB6PPS4      RB6PPS3   RB6PPS2   RB6PPS1   RB6PPS0        282
3A0Dh      RB5PPS                —             —          RB5PPS5      RB5PPS4      RB5PPS3   RB5PPS2   RB5PPS1   RB5PPS0        282
3A0Ch      RB4PPS                —             —          RB4PPS5      RB4PPS4      RB4PPS3   RB4PPS2   RB4PPS1   RB4PPS0        282
3A0Bh      RB3PPS                —             —          RB3PPS5      RB3PPS4      RB3PPS3   RB3PPS2   RB3PPS1   RB3PPS0        282
3A0Ah      RB2PPS                —             —          RB2PPS5      RB2PPS4      RB2PPS3   RB2PPS2   RB2PPS1   RB2PPS0        282
3A09h      RB1PPS                —             —          RB1PPS5      RB1PPS4      RB1PPS3   RB1PPS2   RB1PPS1   RB1PPS0        282
Legend:      x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:      Unimplemented in LF devices.
      2:     Unimplemented in PIC18(L)F26K42.
      3:     Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:     Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 729
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                           Register
 Address      Name            Bit 7          Bit 6         Bit 5        Bit 4          Bit 3         Bit 2          Bit 1          Bit 0
                                                                                                                                           on page

3A08h      RB0PPS               —             —          RB0PPS5      RB0PPS4      RB0PPS3      RB0PPS2        RB0PPS1        RB0PPS0        282
3A07h      RA7PPS               —             —          RA7PPS5      RA7PPS4      RA7PPS3      RA7PPS2        RA7PPS1        RA7PPS0        282
3A06h      RA6PPS               —             —          RA6PPS5      RA6PPS4      RA6PPS3      RA6PPS2        RA6PPS1        RA6PPS0        282
3A05h      RA5PPS               —             —          RA5PPS5      RA5PPS4      RA5PPS3      RA5PPS2        RA5PPS1        RA5PPS0        282
3A04h      RA4PPS               —             —          RA4PPS5      RA4PPS4      RA4PPS3      RA4PPS2        RA4PPS1        RA4PPS0        282
3A03h      RA3PPS               —             —          RA3PPS5      RA3PPS4      RA3PPS3      RA3PPS2        RA3PPS1        RA3PPS0        282
3A02h      RA2PPS               —             —          RA2PPS5      RA2PPS4      RA2PPS3      RA2PPS2        RA2PPS1        RA2PPS0        282
3A01h      RA1PPS               —             —          RA1PPS5      RA1PPS4      RA1PPS3      RA1PPS2        RA1PPS1        RA1PPS0        282
3A00h      RA0PPS               —             —          RA0PPS5      RA0PPS4      RA0PPS3      RA0PPS2        RA0PPS1        RA0PPS0        282
39FFh -            —                                                      Unimplemented
39F8h
39F7h      SCANPR               —             —             —            —              —                            PR                      31
39F6h -            —                                                      Unimplemented
39F5h
39F4h      DMA2PR               —             —             —            —              —                            PR                      31
39F3h      DMA1PR               —             —             —            —              —                            PR                      30
39F2h      MAINPR               —             —             —            —              —                            PR                      30
39F1h      ISRPR                —             —             —            —              —                            PR                      30
39F0h              —                                                      Unimplemented
39EFh      PRLOCK               —             —             —            —              —             —              —        PRLOCKED       31
39EEh -            —                                                      Unimplemented
39E7h
39E6h      NVMCON2                                                           NVMCON2                                                         211
39E5h      NVMCON1                    REG                   —           FREE          WRERR          WREN           WR             RD        210
39E4h              —                                                      Unimplemented
39E3h      NVMDAT                                                               DAT                                                          212
39E2h              —                                                      Unimplemented
39E1h      NVMADRH(4)           —             —             —            —              —             —                     ADR              211
39E0h      NVMADRL                                                              ADR                                                          211
39DFh      OSCFRQ               —             —             —            —                                   FRQ                             107
39DEh      OSCTUNE              —             —                                                TUN                                           108
39DDh      OSCEN            EXTOEN          HFOEN         MFOEN        LFOEN          SOSCEN     ADOEN               —              —        109
39DCh      OSCSTAT           EXTOR           HFOR         MFOR          LFOR           SOR           ADOR            —            PLLR       106
39DBh      OSCCON3         CSWHOLD        SOSCPWR           —          ORDY           NOSCR           —              —              —        105
39DAh      OSCCON2              —                        COSC                                                CDIV                            105
39D9h      OSCCON1              —                        NOSC                                                NDIV                            104
39D8h      CPUDOZE            IDLEN         DOZEN           ROI         DOE             —                           DOZE                     177
39D7h -            —                                                      Unimplemented
39D2h
39D1h      VREGCON(1)           —             —             —            —              —             —         VREGPM              —        176
39D0h      BORCON           SBOREN            —             —            —              —             —              —        BORRDY         85
39CFh -            —                                                      Unimplemented
39C8h
39C7h      PMD7                 —             —             —            —              —             —         DMA2MD        DMA1MD         299
39C6h      PMD6                 —             —          SMT1MD       CLC4MD          CLC3MD     CLC2MD         CLC1MD            DSMMD      298
39C5h      PMD5                 —             —           U2MD         U1MD             —        SPI1MD         I2C2MD            I2C1MD     297
39C4h      PMD4             CWG3MD          CWG2MD       CWG1MD          —              —             —              —              —        296
39C3h      PMD3             PWM8MD          PWM7MD       PWM6MD       PWM5MD          CCP4MD     CCP3MD         CCP2MD        CCP1MD         295
39C2h      PMD2                 —           DACMD         ADCMD          —              —        CMP2MD         CMP1MD            ZCDMD      294
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                              DS40001919G-page 730
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:            REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                    Register
 Address          Name         Bit 7          Bit 6         Bit 5        Bit 4        Bit 3     Bit 2           Bit 1      Bit 0
                                                                                                                                    on page

39C1h      PMD1              NCO1MD         TMR6MD        TMR5MD       TMR4MD       TMR3MD    TMR2MD        TMR1MD       TMR0MD       293
39C0h      PMD0              SYSCMD          FVRMD        HLVDMD        CRCMD       SCANMD     NVMMD        CLKRMD       IOCMD        292
39BFh -            —                                                       Unimplemented
39ABh
39AAh      PIR10                 —             —             —            —            —         —          CLC4IF       CCP4IF       146
39A9h      PIR9                  —             —             —            —          CLC3IF    CWG3IF       CCP3IF       TMR6IF       145
39A8h      PIR8              TMR5GIF         TMR5IF          —            —            —         —                —         —         145
39A7h      PIR7                  —             —           INT2IF       CLC2IF      CWG2IF       —          CCP2IF       TMR4IF       144
39A6h      PIR6              TMR3GIF         TMR3IF         U2IF        U2EIF        U2TXIF    U2RXIF       I2C2EIF       I2C2IF      143
39A5h      PIR5              I2C2TXIF       I2C2RXIF      DMA2AIF     DMA2ORIF     DMA2DCN- DMA2SCN-            C2IF      INT1IF      142
                                                                                      TIF     TIF
39A4h      PIR4               CLC1IF        CWG1IF         NCO1IF         —          CCP1IF    TMR2IF      TMR1GIF       TMR1IF       141
39A3h      PIR3               TMR0IF          U1IF         U1EIF        U1TXIF       U1RXIF    I2C1EIF          I2C1IF   I2C1TXIF     140
39A2h      PIR2              I2C1RXIF        SPI1IF       SPI1TXIF     SPI1RXIF     DMA1AIF   DMA1ORIF     DMA1DCN- DMA1SCNTIF        138
                                                                                                             TIF
39A1h      PIR1             SMT1PWAIF      SMT1PRAIF       SMT1IF        C1IF        ADTIF      ADIF            ZCDIF     INT0IF      138
39A0h      PIR0                IOCIF         CRCIF         SCANIF       NVMIF        CSWIF     OSFIF        HLVDIF        SWIF        137
399Fh -            —                                                       Unimplemented
399Bh
399Ah      PIE10                 —             —             —            —            —         —          CLC4IE       CCP4IE       156
3999h      PIE9                  —             —             —            —          CLC3IE   CWG3IE        CCP3IE       TMR6IE       155
3998h      PIE8              TMR5GIE         TMR5IE          —            —            —         —                —         —         155
3997h      PIE7                  —             —           INT2IE       CLC2IE      CWG2IE       —          CCP2IE       TMR4IE       154
3996h      PIE6              TMR3GIE         TMR3IE         U2IE        U2EIE        U2TXIE    U2RXIE       I2C2EIE       I2C2IE      153
3995h      PIE5              I2C2TXIE       I2C2RXIE      DMA2AIE     DMA2ORIE DMA2DCN- DMA2SCN-                C2IE      INT1IE      152
                                                                                 TIE      TIE
3994h      PIE4               CLC1IE        CWG1IE         NCO1IE         —          CCP1IE    TMR2IE      TMR1GIE       TMR1IE       151
3993h      PIE3               TMR0IE          U1IE         U1EIE        U1TXIE       U1RXIE    I2C1EIE          I2C1IE   I2C1TXIE     150
3992h      PIE2              I2C1RXIE        SPI1IE       SPI1TXIE     SPI1RXIE     DMA1AIE   DMA1ORIE     DMA1DCN- DMA1SCNTIE        149
                                                                                                             TIE
3991h      PIE1             SMT1PWAIE      SMT1PRAIE       SMT1IE        C1IE        ADTIE      ADIE            ZCDIE     INT0IE      148
3990h      PIE0                IOCIE         CRCIE         SCANIE       NVMIE        CSWIE     OSFIE        HLVDIE        SWIE        147
398Fh -            —                                                       Unimplemented
398Bh
398Ah      IPR10                 —             —             —            —            —         —          CLC4IP       CCP4IP       165
3989h      IPR9                  —             —             —            —          CLC3IP   CWG3IP        CCP3IP       TMR6IP       165
3988h      IPR8              TMR5GIP         TMR5IP          —            —            —         —                —         —         164
3987h      IPR7                  —             —           INT2IP       CLC2IP      CWG2IP        -         CCP2IP       TMR4IP       164
3986h      IPR6              TMR3GIP         TMR3IP         U2IP        U2EIP        U2TXIP    U2RXIP       I2C2EIP       I2C2IP      163
3985h      IPR5              I2C2TXIP       I2C2RXIP      DMA2AIP     DMA2ORIP DMA2DCN- DMA2SCN-                C2IP      INT1IP      162
                                                                                 TIP      TIP
3984h      IPR4               CLC1IP        CWG1IP         NCO1IP         —          CCP1IP    TMR2IP      TMR1GIP       TMR1IP       161
3983h      IPR3               TMR0IP          U1IP         U1EIP        U1TXIP       U1RXIP    I2C1EIP          I2C1IP   I2C1TXIP     160
3982h      IPR2              I2C1RXIP        SPI1IP       SPI1TXIP     SPI1RXIP     DMA1AIP   DMA1ORIP     DMA1DCN- DMA1SCNTIP        159
                                                                                                             TIP
3981h      IPR1             SMT1PWAIP      SMT1PRAIP       SMT1IP        C1IP        ADTIP      ADIP            ZCDIP     INT0IP      158
3980h      IPR0                IOCIP         CRCIP         SCANIP       NVMIP        CSWIP     OSFIP        HLVDIP        SWIP        157
397Fh -            —                                                       Unimplemented
397Eh
397Dh      SCANTRIG              —             —             —            —                              TSEL                         227
397Ch      SCANCON0             EN           TRIGEN         SGO           —            —       MREG        BURSTMD        BUSY        223
Legend:      x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:      Unimplemented in LF devices.
      2:     Unimplemented in PIC18(L)F26K42.
      3:     Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:     Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                       DS40001919G-page 731
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:          REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                                              Register
 Address      Name            Bit 7          Bit 6           Bit 5      Bit 4           Bit 3          Bit 2          Bit 1           Bit 0
                                                                                                                                              on page

397Bh      SCANHADRU            —             —                                                 HADR                                            225
397Ah      SCANHADRH                                                            HADR                                                            226
3979h      SCANHADRL                                                            HADR                                                            226
3978h      SCANLADRU            —             —                                                 LADR                                            224
3977h      SCANLADRH                                                            LADR                                                            224
3976h      SCANLADRL                                                            LADR                                                            225
3975h -         —                                                         Unimplemented
396Ah
3969h      CRCCON1                                   DLEN                                                      PLEN                             219
3968h      CRCCON0             EN           CRCGO           BUSY       ACCM              —              —         SHIFTM              FULL      219
3967h      CRCXORH             X15            X14            X13         X12             X11            X10            X9              X8       222
3966h      CRCXORL             X7             X6              X5         X4              X3             X2             X1              —        222
3965h      CRCSHIFTH         SHFT15         SHFT14          SHFT13     SHFT12          SHFT11      SHFT10         SHFT9           SHFT8         221
3964h      CRCSHIFTL         SHFT7          SHFT6           SHFT5      SHFT4            SHFT3      SHFT2          SHFT1           SHFT0         221
3963h      CRCACCH           ACC15          ACC14           ACC13      ACC12            ACC11      ACC10              ACC9            ACC8      220
3962h      CRCACCL            ACC7           ACC6           ACC5        ACC4            ACC3          ACC2            ACC1            ACC0      221
3961h      CRCDATH           DATA15         DATA14          DATA13     DATA12          DATA11      DATA10         DATA9           DATA8         220
3960h      CRCDATL           DATA7          DATA6           DATA5      DATA4            DATA3       DATA2         DATA1           DATA0         220
395Fh      WDTTMR                                       WDTTMR                                      STATE                     PSCNT             185
395Eh      WDTPSH                                                               PSCNT                                                           184
395Dh      WDTPSL                                                               PSCNT                                                           184
395Ch      WDTCON1              —                            CS                          —                        WINDOW                        183
395Bh      WDTCON0              —             —                                          PS                                           SEN       182
395Ah -         —                                                         Unimplemented
38A0h
389Fh      IVTADU                                                                AD                                                             167
389Eh      IVTADH                                                                AD                                                             167
389Dh      IVTADL                                                                AD                                                             167
389Ch -         —                                                         Unimplemented
3891h
3890h      PRODH_SHAD                                                           PRODH                                                           125
388Fh      PRODL_SHAD                                                           PRODL                                                           125
388Eh      FSR2H_SHAD           —             —                                                 FSR2H                                           125
388Dh      FSR2L_SHAD                                                           FSR2L                                                           125
388Ch      FSR1H_SHAD           —             —                                                 FSR1H                                           125
388Bh      FSR1L_SHAD                                                           FSR1L                                                           125
388Ah      FSR0H_SHAD           —             —                                                 FSR0H                                           125
3889h      FSR0L_SHAD                                                           FSR0L                                                           125
3888h      PCLATU_SHAD          —             —               —                                         PCU                                     125
3887h      PCLATH_SHAD                                                           PCH                                                            125
3886h      BSR_SHAD             —             —                                                 BSR                                             125
3885h      WREG_SHAD                                                            WREG                                                            125
3884h      STATUS_SHAD          —             TO             PD           N              OV             Z             DC               C        125
3883h      SHADCON              —             —               —          —               —              —              —          SHADLO        168
3882h      BSR_CSHAD            —             —                                                 BSR                                             57
3881h      WREG_CSHAD                                                           WREG                                                            57
3880h      STATUS_C-            —             TO             PD           N              OV             Z             DC               C        57
           SHAD
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                             DS40001919G-page 732
                        PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 42-1:         REGISTER FILE SUMMARY FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
                                                                                                                            Register
 Address      Name            Bit 7          Bit 6         Bit 5        Bit 4        Bit 3   Bit 2   Bit 1      Bit 0
                                                                                                                            on page

387Fh -         —                                                         Unimplemented
3800h
Legend:     x = unknown, u = unchanged, — = unimplemented, q = value depends on condition
Note 1:     Unimplemented in LF devices.
      2:    Unimplemented in PIC18(L)F26K42.
      3:    Unimplemented on PIC18(L)F26/27/45/46/47K42 devices.
      4:    Unimplemented in PIC18(L)F45/55K42.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 733
