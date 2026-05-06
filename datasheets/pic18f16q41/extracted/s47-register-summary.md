47.       Register Summary
Address     Name      Bit Pos.     7           6            5                4                3                2                 1            0
 0x00
  ...      Reserved
 0x38
 0x39      CLKRCON      7:0        EN                                             DC[1:0]                                   DIV[2:0]
 0x3A      CLKRCLK      7:0                                                                                          CLK[3:0]
 0x3B
  ...      Reserved
 0x3F
 0x40      NVMCON0      7:0                                                                                                                  GO
 0x41      NVMCON1      7:0      WRERR                                                                                   NVMCMD[2:0]
 0x42      NVMLOCK      7:0                                                  NVMLOCK[7:0]
                        7:0                                                  NVMADR[7:0]
 0x43      NVMADR      15:8                                                  NVMADR[15:8]
                       23:16                                                            NVMADR[21:16]
                        7:0                                                  NVMDAT[7:0]
 0x46      NVMDAT
                       15:8                                                  NVMDAT[15:8]
 0x48      VREGCON      7:0                                     PMSYS[1:0]                                                         VREGPM[1:0]
 0x49       BORCON      7:0      SBOREN                                                                                                   BORRDY
 0x4A      HLVDCON0     7:0        EN                     OUT              RDY                                                  INTH        INTL
 0x4B      HLVDCON1     7:0                                                                                          SEL[3:0]
 0x4C       ZCDCON      7:0       SEN                     OUT              POL                                                  INTP        INTN
 0x4D
  ...      Reserved
 0x62
 0x63        PMD0       7:0      SYSCMD      FVRMD      HLVDMD          CRCMD           SCANMD                              CLKRMD         IOCMD
 0x64        PMD1       7:0       C1MD       ZCDMD      SMT1MD         TMR4MD           TMR3MD          TMR2MD             TMR1MD         TMR0MD
 0x65        PMD2       7:0      CCP1MD     CWG1MD      DSM1MD         NCO1MD            ACTMD          DAC1MD              ADCMD           C2MD
 0x66        PMD3       7:0       U2MD        U1MD       SPI2MD         SPI1MD           I2C1MD         PWM3MD             PWM2MD         PWM1MD
 0x67        PMD4       7:0      DMA3MD     DMA2MD      DMA1MD         CLC4MD           CLC3MD           CLC2MD             CLC1MD          U3MD
 0x68        PMD5       7:0                                                                             OPA1MD             DAC2MD         DMA4MD
 0x69      Reserved
 0x6A      MD1CON0      7:0        EN                     OUT           OPOL                                                                 BIT
 0x6B      MD1CON1      7:0                              CHPOL         CHSYNC                                               CLPOL          CLSYNC
 0x6C       MD1SRC      7:0                                                                              MS[4:0]
 0x6D      MD1CARL      7:0                                                                                     CL[3:0]
 0x6E      MD1CARH      7:0                                                                                    CH[3:0]
 0x6F       CMOUT       7:0                                                                                             C2OUT               C1OUT
 0x70      CM1CON0      7:0        EN         OUT                          POL                                           HYS                 SYNC
 0x71      CM1CON1      7:0                                                                                                  INTP           INTN
 0x72      CM1NCH       7:0                                                                                                NCH[2:0]
 0x73       CM1PCH      7:0                                                                                                PCH[2:0]
 0x74      CM2CON0      7:0        EN         OUT                          POL                                                HYS           SYNC
 0x75      CM2CON1      7:0                                                                                                  INTP           INTN
 0x76      CM2NCH       7:0                                                                                                NCH[2:0]
 0x77       CM2PCH      7:0                                                                                                PCH[2:0]
 0x78      WDTCON0      7:0                                                              PS[4:0]                                             SEN
 0x79      WDTCON1      7:0                              CS[2:0]                                                         WINDOW[2:0]
 0x7A       WDTPSL      7:0                                                  PSCNTL[7:0]
 0x7B       WDTPSH      7:0                                                  PSCNTH[7:0]
 0x7C      WDTTMR       7:0                             TMR[4:0]                                             STATE                PSCNT[17:16]
 0x7D      DAC1DATL     7:0                                                      DAC1R[7:0]
 0x7E      Reserved
 0x7F      DAC1CON     7:0         EN                            OE[1:0]                          PSS[1:0]                                   NSS
 0x80       SPI1RXB    7:0                                                        RXB[7:0]
 0x81       SPI1TXB    7:0                                                        TXB[7:0]
                       7:0                                                       TCNTL[7:0]
 0x82      SPI1TCNT
                       15:8                                                                                               TCNTH[2:0]


--- p874 ---
...........continued
 Address               Name   Bit Pos.      7              6         5              4                3            2            1               0
   0x84           SPI1CON0      7:0         EN                                                                  LSBF         MST          BMODE
   0x85           SPI1CON1      7:0        SMP         CKE         CKP             FST                           SSP         SDIP          SDOP
   0x86           SPI1CON2      7:0       BUSY        SSFLT                                                     SSET         TXR            RXR
   0x87          SPI1STATUS     7:0       TXWE                     TXBE                          RXRE           CLB                        RXBF
   0x88          SPI1TWIDTH    7:0                                                                                        TWIDTH[2:0]
   0x89           SPI1BAUD     7:0                                                 BAUD[7:0]
   0x8A            SPI1INTF    7:0        SRMTIF         TCZIF     SOSIF       EOSIF                            RXOIF       TXUIF
   0x8B            SPI1INTE    7:0        SRMTIE         TCZIE     SOSIE       EOSIE                            RXOIE       TXUIE
   0x8C            SPI1CLK     7:0                                                                                 CLKSEL[3:0]
   0x8D            SPI2RXB     7:0                                                       RXB[7:0]
   0x8E            SPI2TXB     7:0                                                       TXB[7:0]
                               7:0                                                      TCNTL[7:0]
   0x8F           SPI2TCNT
                               15:8                                                                                        TCNTH[2:0]
   0x91           SPI2CON0     7:0          EN                                                                  LSBF          MST         BMODE
   0x92           SPI2CON1     7:0         SMP         CKE         CKP             FST                           SSP          SDIP         SDOP
   0x93           SPI2CON2     7:0        BUSY        SSFLT                                                     SSET          TXR           RXR
   0x94          SPI2STATUS    7:0        TXWE                     TXBE                          RXRE           CLB                        RXBF
   0x95          SPI2TWIDTH    7:0                                                                                        TWIDTH[2:0]
   0x96           SPI2BAUD     7:0                                                 BAUD[7:0]
   0x97            SPI2INTF    7:0        SRMTIF         TCZIF     SOSIF       EOSIF                            RXOIF       TXUIF
   0x98            SPI2INTE    7:0        SRMTIE         TCZIE     SOSIE       EOSIE                            RXOIE       TXUIE
   0x99            SPI2CLK     7:0                                                                                 CLKSEL[3:0]
   0x9A
     ...          Reserved
   0x9F
   0xA0          DAC2DATL       7:0                                                     DAC2R[7:0]
   0xA1          Reserved
   0xA2          DAC2CON        7:0        EN                                                        PSS[1:0]                                 NSS
   0xA3         OPA1CON0        7:0        EN                     CPON                            UG                              SOC[1:0]
   0xA4         OPA1CON1        7:0                              GSEL[2:0]                      RESON                       NSS[2:0]
   0xA5         OPA1CON2        7:0                              NCH[2:0]                                                   PCH[2:0]
   0xA6         OPA1CON3        7:0           FMS[1:0]                                                                             PSS[1:0]
   0xA7          OPA1HWC        7:0       OREN                   HWCH[2:0]                      ORPOL                      HWCL[2:0]
   0xA8         OPA1OFFSET      7:0                                                     OFFSET[7:0]
   0xA9          OPA1ORS        7:0                                                                        ORS[4:0]
   0xAA
     ...          Reserved
   0xAB
   0xAC           ACTCON        7:0       ACTEN       ACTUD                                    ACTLOCK                       ACTORS
   0xAD           OSCCON1       7:0                              NOSC[2:0]                                            NDIV[3:0]
   0xAE           OSCCON2       7:0                              COSC[2:0]                                            CDIV[3:0]
   0xAF           OSCCON3       7:0      CSWHOLD    SOSCPWR                    ORDY             NOSCR
   0xB0           OSCTUNE       7:0                                                                 TUN[5:0]
   0xB1            OSCFRQ       7:0                                                                              FRQ[3:0]
   0xB2           OSCSTAT       7:0       EXTOR       HFOR        MFOR         LFOR             SOR          ADOR         SFOR              PLLR
   0xB3            OSCEN        7:0      EXTOEN       HFOEN       MFOEN       LFOEN            SOSCEN       ADOEN                          PLLEN
   0xB4            PRLOCK       7:0                                                                                                      PRLOCKED
   0xB5            SCANPR       7:0                                                                                         PR[2:0]
   0xB6           DMA1PR        7:0                                                                                         PR[2:0]
   0xB7           DMA2PR        7:0                                                                                         PR[2:0]
   0xB8           DMA3PR        7:0                                                                                         PR[2:0]
   0xB9           DMA4PR        7:0                                                                                         PR[2:0]
   0xBA
     ...          Reserved
   0xBD
   0xBE            MAINPR       7:0                                                                                         PR[2:0]
   0xBF             ISRPR       7:0                                                                                         PR[2:0]
   0xC0
     ...          Reserved
   0xD3
   0xD4            CLCDATA      7:0                                                            CLC4OUT     CLC3OUT         CLC2OUT       CLC1OUT


--- p875 ---
...........continued
 Address               Name   Bit Pos.     7          6           5             4                 3                 2                1            0
   0xD5          CLCSELECT      7:0                                                                                                 SLCT[1:0]
   0xD6          CLCnCON        7:0      EN                      OUT           INTP           INTN                            MODE[2:0]
   0xD7           CLCnPOL       7:0      POL                                                 G4POL            G3POL            G2POL        G1POL
   0xD8          CLCnSEL0       7:0                                                          D1S[6:0]
   0xD9           CLCnSEL1      7:0                                                          D2S[6:0]
   0xDA           CLCnSEL2      7:0                                                          D3S[6:0]
   0xDB           CLCnSEL3      7:0                                                          D4S[6:0]
   0xDC           CLCnGLS0      7:0      G1D4T      G1D4N       G1D3T       G1D3N             G1D2T           G1D2N             G1D1T           G1D1N
   0xDD           CLCnGLS1      7:0      G2D4T      G2D4N       G2D3T       G2D3N             G2D2T           G2D2N             G2D1T           G2D1N
   0xDE           CLCnGLS2      7:0      G3D4T      G3D4N       G3D3T       G3D3N             G3D2T           G3D2N             G3D1T           G3D1N
   0xDF           CLCnGLS3      7:0      G4D4T      G4D4N       G4D3T       G4D3N             G4D2T           G4D2N             G4D1T           G4D1N
   0xE0
     ...          Reserved
   0xE7
   0xE8          DMASELECT      7:0                                                                                            SLCT[2:0]
   0xE9           DMAnBUF       7:0                                                  BUF[7:0]
                                7:0                                                 DCNT[7:0]
   0xEA          DMAnDCNT
                                15:8                                                                                    DCNT[11:8]
                                7:0                                                 DPTR[7:0]
   0xEC          DMAnDPTR
                                15:8                                                DPTR[15:8]
                                7:0                                                  DSZ[7:0]
   0xEE           DMAnDSZ
                                15:8                                                                                    DSZ[11:8]
                                7:0                                                  DSA[7:0]
   0xF0           DMAnDSA
                                15:8                                                DSA[15:8]
                                7:0                                                 SCNT[7:0]
   0xF2          DMAnSCNT
                                15:8                                                                                    SCNT[11:8]
                                7:0                                                  SPTR[7:0]
   0xF4          DMAnSPTR       15:8                                                SPTR[15:8]
                               23:16                                                                  SPTR[21:16]
                                7:0                                                   SSZ[7:0]
   0xF7           DMAnSSZ
                                15:8                                                                                    SSZ[11:8]
                                7:0                                                    SSA[7:0]
   0xF9           DMAnSSA       15:8                                                  SSA[15:8]
                               23:16                                                                  SSA[21:16]
   0xFC          DMAnCON0       7:0       EN       SIRQEN       DGO                                           AIRQEN                             XIP
   0xFD          DMAnCON1       7:0         DMODE[1:0]          DSTP                  SMR[1:0]                    SMODE[1:0]                    SSTP
   0xFE          DMAnAIRQ       7:0                                                   AIRQ[7:0]
   0xFF          DMAnSIRQ       7:0                                                   SIRQ[7:0]
  0x0100
    ...           Reserved
  0x01FF
  0x0200          PPSLOCK       7:0                                                                                                           PPSLOCKED
  0x0201           RA0PPS       7:0                                                                   RA0PPS[5:0]
  0x0202           RA1PPS       7:0                                                                   RA1PPS[5:0]
  0x0203           RA2PPS       7:0                                                                   RA2PPS[5:0]
  0x0204          Reserved
  0x0205           RA4PPS       7:0                                                                   RA4PPS[5:0]
  0x0206           RA5PPS       7:0                                                                   RA5PPS[5:0]
  0x0207
    ...           Reserved
  0x020C
  0x020D           RB4PPS       7:0                                                                   RB4PPS[5:0]
  0x020E           RB5PPS       7:0                                                                   RB5PPS[5:0]
  0x020F           RB6PPS       7:0                                                                   RB6PPS[5:0]
  0x0210           RB7PPS       7:0                                                                   RB7PPS[5:0]
  0x0211           RC0PPS       7:0                                                                   RC0PPS[5:0]
  0x0212           RC1PPS       7:0                                                                   RC1PPS[5:0]
  0x0213           RC2PPS       7:0                                                                   RC2PPS[5:0]
  0x0214           RC3PPS       7:0                                                                   RC3PPS[5:0]
  0x0215           RC4PPS       7:0                                                                   RC4PPS[5:0]
  0x0216           RC5PPS       7:0                                                                   RC5PPS[5:0]


--- p876 ---
...........continued
 Address               Name    Bit Pos.   7        6           5             4           3                 2      1              0
  0x0217           RC6PPS        7:0                                                         RC6PPS[5:0]
  0x0218           RC7PPS        7:0                                                         RC7PPS[5:0]
  0x0219
    ...           Reserved
  0x023D
  0x023E          INT0PPS        7:0                                                 PORT                      PIN[2:0]
  0x023F          INT1PPS        7:0                                         PORT[1:0]                         PIN[2:0]
  0x0240          INT2PPS        7:0                                   PORT[2:0]                               PIN[2:0]
  0x0241          T0CKIPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0242          T1CKIPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0243           T1GPPS        7:0                                   PORT[2:0]                               PIN[2:0]
  0x0244          T3CKIPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0245           T3GPPS        7:0                                   PORT[2:0]                               PIN[2:0]
  0x0246
    ...           Reserved
  0x0247
  0x0248           T2INPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0249           T4INPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x024A
    ...           Reserved
  0x024E
  0x024F          CCP1PPS        7:0                                   PORT[2:0]                               PIN[2:0]
  0x0250          Reserved
  0x0251        PWM1ERSPPS       7:0                                         PORT[1:0]                         PIN[2:0]
  0x0252        PWM2ERSPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0253        PWM3ERSPPS       7:0                                         PORT[1:0]                         PIN[2:0]
  0x0254
    ...           Reserved
  0x0256
  0x0257        PWMIN0PPS        7:0                                   PORT[2:0]                               PIN[2:0]
  0x0258        PWMIN1PPS        7:0                                   PORT[2:0]                               PIN[2:0]
  0x0259        SMT1WINPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x025A        SMT1SIGPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x025B         CWG1PPS         7:0                                   PORT[2:0]                               PIN[2:0]
  0x025C
    ...           Reserved
  0x025D
  0x025E        MD1CARLPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x025F        MD1CARHPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0260        MD1SRCPPS        7:0                                   PORT[2:0]                               PIN[2:0]
  0x0261         CLCIN0PPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0262         CLCIN1PPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0263         CLCIN2PPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0264         CLCIN3PPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x0265
    ...           Reserved
  0x0268
  0x0269          ADACTPPS       7:0                                   PORT[2:0]                               PIN[2:0]
  0x026A         SPI1SCKPPS      7:0                                   PORT[2:0]                               PIN[2:0]
  0x026B          SPI1SDIPPS     7:0                                   PORT[2:0]                               PIN[2:0]
  0x026C          SPI1SSPPS      7:0                                   PORT[2:0]                               PIN[2:0]
  0x026D         SPI2SCKPPS      7:0                                   PORT[2:0]                               PIN[2:0]
  0x026E          SPI2SDIPPS     7:0                                   PORT[2:0]                               PIN[2:0]
  0x026F          SPI2SSPPS      7:0                                   PORT[2:0]                               PIN[2:0]
  0x0270         I2C1SDAPPS      7:0                                   PORT[2:0]                               PIN[2:0]
  0x0271         I2C1SCLPPS      7:0                                   PORT[2:0]                               PIN[2:0]
  0x0272           U1RXPPS       7:0                                         PORT[1:0]                         PIN[2:0]
  0x0273          U1CTSPPS       7:0                                         PORT[1:0]                         PIN[2:0]
  0x0274           UxRXPPS       7:0                                                 PORT                      PIN[2:0]
  0x0275           UxCTSPPS      7:0                                                 PORT                      PIN[2:0]
  0x0276           U3RXPPS       7:0                                         PORT[1:0]                         PIN[2:0]


--- p877 ---
...........continued
 Address               Name    Bit Pos.     7               6        5                 4                  3       2          1                0
  0x0277          U3CTSPPS       7:0                                                       PORT[1:0]                      PIN[2:0]
  0x0278
    ...           Reserved
  0x0285
  0x0286            RB6I2C      7:0             SLEW[1:0]                 PU[1:0]                                                 TH[1:0]
  0x0287            RB4I2C      7:0             SLEW[1:0]                 PU[1:0]                                                 TH[1:0]
  0x0288            RC1I2C      7:0             SLEW[1:0]                 PU[1:0]                                                 TH[1:0]
  0x0289            RC0I2C      7:0             SLEW[1:0]                 PU[1:0]                                                 TH[1:0]
  0x028A           I2C1RXB      7:0                                                    RXB[7:0]
  0x028B           I2C1TXB      7:0                                                    TXB[7:0]
                                7:0                                                    CNT[7:0]
  0x028C           I2C1CNT
                                15:8                                                  CNT[15:8]
  0x028E          I2C1ADB0      7:0                                                    ADB[7:0]
  0x028F          I2C1ADB1      7:0                                                    ADB[7:0]
  0x0290          I2C1ADR0      7:0                                                    ADR[7:0]
  0x0291          I2C1ADR1      7:0                                             ADR[6:0]
  0x0292          I2C1ADR2      7:0                                                    ADR[7:0]
  0x0293          I2C1ADR3      7:0                                             ADR[6:0]
  0x0294          I2C1CON0      7:0         EN          RSEN         S            CSTR          MDR                     MODE[2:0]
  0x0295          I2C1CON1      7:0       ACKCNT       ACKDT      ACKSTAT         ACKT            P           RXO            TXU          CSD
  0x0296          I2C1CON2      7:0        ACNT        GCEN         FME           ABD               SDAHT[1:0]                  BFRET[1:0]
  0x0297           I2C1ERR      7:0                    BTOIF       BCLIF         NACKIF                      BTOIE          BLCIE       NACKIE
  0x0298          I2C1STAT0     7:0        BFRE         SMA        MMA             R              D
  0x0299          I2C1STAT1     7:0       TXWE                     TXBE                         RXRE         CLRBF                       RXBF
  0x029A            I2C1PIR     7:0       CNTIF        ACKTIF                     WRIF          ADRIF         PCIF          RSCIF         SCIF
  0x029B            I2C1PIE     7:0       CNTIE        ACKTIE                     WRIE         ADRIE          PCIE          RSCIE        SCIE
  0x029C           I2C1BTO      7:0       TOREC        TOBY32                                       TOTIME[5:0]
  0x029D          I2C1BAUD      7:0                                                   BAUD[7:0]
  0x029E           I2C1CLK      7:0                                                                                CLK[3:0]
  0x029F          I2C1BTOC      7:0                                                                                      BTOC[2:0]
  0x02A0           Reserved
  0x02A1             U1RXB      7:0                                                         RXB[7:0]
  0x02A2           U1RXCHK      7:0                                                        RXCHK[7:0]
  0x02A3             U1TXB      7:0                                                         TXB[7:0]
  0x02A4           U1TXCHK      7:0                                                        TXCHK[7:0]
                                7:0                                                          P1[7:0]
  0x02A5               U1P1
                                15:8                                                                                                        P1[8]
                                7:0                                                          P2[7:0]
  0x02A7               U1P2
                                15:8                                                                                                        P2[8]
                                7:0                                                          P3[7:0]
  0x02A9               U1P3
                                15:8                                                                                                        P3[8]
 0x02AB            U1CON0       7:0        BRGS        ABDEN       TXEN              RXEN                           MODE[3:0]
 0x02AC            U1CON1       7:0         ON                                       WUE         RXBIMD                   BRKOVR      SENDB
 0x02AD            U1CON2       7:0       RUNOVF       RXPOL              STP[1:0]                 C0EN         TXPOL          FLO[1:0]
                                7:0                                                       BRG[7:0]
  0x02AE               U1BRG
                                15:8                                                     BRG[15:8]
  0x02B0           U1FIFO       7:0       TXWRE        STPMD       TXBE              TXBF         RXIDL          XON       RXBE             RXBF
  0x02B1           U1UIR        7:0        WUIF        ABDIF                                                    ABDIE
  0x02B2          U1ERRIR       7:0       TXMTIF        PERIF     ABDOVF             CERIF              FERIF   RXBKIF    RXFOIF            TXCIF
  0x02B3          U1ERRIE       7:0       TXMTIE        PERIE     ABDOVE             CERIE              FERIE   RXBKIE    RXFOIE            TXCIE
  0x02B4           U2RXB        7:0                                                          RXB[7:0]
  0x02B5          Reserved
  0x02B6           U2TXB         7:0                                                         TXB[7:0]
  0x02B7          Reserved
                                7:0                                                          P1[7:0]
  0x02B8               U2P1
                                15:8
                                7:0                                                          P2[7:0]
  0x02BA               U2P2
                                15:8
                                7:0                                                          P3[7:0]
  0x02BC               U2P3
                                15:8


--- p878 ---
...........continued
 Address               Name    Bit Pos.     7            6          5                 4                  3         2                1            0
  0x02BE           U2CON0        7:0       BRGS       ABDEN       TXEN              RXEN                            MODE[3:0]
  0x02BF           U2CON1        7:0        ON                                      WUE           RXBIMD                  BRKOVR      SENDB
  0x02C0           U2CON2        7:0      RUNOVF      RXPOL              STP[1:0]                               TXPOL          FLO[1:0]
                                 7:0                                                       BRG[7:0]
  0x02C1               U2BRG
                                15:8                                                    BRG[15:8]
  0x02C3           U2FIFO       7:0       TXWRE       STPMD       TXBE              TXBF        RXIDL            XON            RXBE           RXBF
  0x02C4           U2UIR        7:0        WUIF       ABDIF                                                     ABDIE
  0x02C5          U2ERRIR       7:0       TXMTIF       PERIF     ABDOVF             CERIF              FERIF    RXBKIF         RXFOIF
  0x02C6          U2ERRIE       7:0       TXMTIE       PERIE     ABDOVE             CERIE              FERIE    RXBKIE         RXFOIE
  0x02C7           U3RXB        7:0                                                         RXB[7:0]
  0x02C8          Reserved
  0x02C9           U3TXB         7:0                                                        TXB[7:0]
  0x02CA          Reserved
                                7:0                                                         P1[7:0]
  0x02CB               U3P1
                                15:8
                                7:0                                                         P2[7:0]
 0x02CD                U3P2
                                15:8
                                7:0                                                         P3[7:0]
  0x02CF               U3P3
                                15:8
  0x02D1           U3CON0       7:0        BRGS       ABDEN       TXEN              RXEN                            MODE[3:0]
  0x02D2           U3CON1       7:0         ON                                      WUE           RXBIMD                  BRKOVR      SENDB
  0x02D3           U3CON2       7:0       RUNOVF      RXPOL              STP[1:0]                               TXPOL          FLO[1:0]
                                7:0                                                      BRG[7:0]
  0x02D4               U3BRG
                                15:8                                                    BRG[15:8]
  0x02D6           U3FIFO       7:0       TXWRE       STPMD       TXBE              TXBF         RXIDL           XON            RXBE           RXBF
  0x02D7            U3UIR       7:0        WUIF       ABDIF                                                     ABDIE
  0x02D8           U3ERRIR      7:0       TXMTIF       PERIF     ABDOVF             CERIF              FERIF    RXBKIF         RXFOIF
  0x02D9           U3ERRIE      7:0       TXMTIE       PERIE     ABDOVE             CERIE              FERIE    RXBKIE         RXFOIE
  0x02DA
     ...          Reserved
  0x02FF
                                 7:0                                                     TMR[7:0]
  0x0300          SMT1TMR       15:8                                                    TMR[15:8]
                                23:16                                                  TMR[23:16]
                                 7:0                                                     CPR[7:0]
  0x0303          SMT1CPR       15:8                                                    CPR[15:8]
                                23:16                                                  CPR[23:16]
                                 7:0                                                    CPW[7:0]
  0x0306          SMT1CPW       15:8                                                   CPW[15:8]
                                23:16                                                  CPW[23:16]
                                 7:0                                                      PR[7:0]
  0x0309           SMT1PR       15:8                                                     PR[15:8]
                                23:16                                                   PR[23:16]
  0x030C         SMT1CON0        7:0        EN                     STP              WPOL          SPOL           CPOL              PS[1:0]
  0x030D         SMT1CON1        7:0       GO        REPEAT                                                          MODE[3:0]
  0x030E          SMT1STAT       7:0      CPRUP      CPWUP         RST                                            TS            WS              AS
  0x030F          SMT1CLK        7:0                                                                                  CSEL[3:0]
  0x0310           SMT1SIG       7:0                                                                           SSEL[4:0]
  0x0311          SMT1WIN        7:0                                                                           WSEL[4:0]
                                 7:0                                                       TMR1[7:0]
  0x0312               TMR1
                                15:8                                                      TMR1[15:8]
  0x0314            T1CON        7:0                                  CKPS[1:0]                                 SYNC           RD16             ON
  0x0315           T1GCON        7:0        GE        GPOL         GTM        GSPM               GGO/DONE       GVAL
  0x0316           T1GATE        7:0                                                                           GSS[4:0]
  0x0317            T1CLK        7:0                                                                           CS[4:0]
  0x0318            TMR0L        7:0                                                TMR0L[7:0]
  0x0319            TMR0H        7:0                                                TMR0H[7:0]
  0x031A           T0CON0        7:0        EN                     OUT          MD16                                   OUTPS[3:0]
  0x031B           T0CON1        7:0                  CS[2:0]                   ASYNC                                   CKPS[3:0]
  0x031C            T2TMR        7:0                                                T2TMR[7:0]


--- p879 ---
...........continued
 Address               Name    Bit Pos.     7          6            5                 4                3                 2             1                 0
  0x031D             T2PR        7:0                                                      T2PR[7:0]
  0x031E            T2CON        7:0       ON                   CKPS[2:0]                                              OUTPS[3:0]
  0x031F            T2HLT        7:0      PSYNC      CPOL        CSYNC                                            MODE[4:0]
  0x0320          T2CLKCON       7:0                                                                                     CS[3:0]
  0x0321           T2RST         7:0                                                                              RSEL[4:0]
  0x0322          Reserved
                                7:0                                                        TMR3[7:0]
  0x0323               TMR3
                                15:8                                                      TMR3[15:8]
  0x0325            T3CON       7:0                                  CKPS[1:0]                                      SYNC             RD16            ON
  0x0326           T3GCON       7:0        GE        GPOL         GTM        GSPM               GGO/DONE            GVAL
  0x0327           T3GATE       7:0                                                                                GSS[4:0]
  0x0328            T3CLK       7:0                                                                                CS[4:0]
  0x0329            T4TMR       7:0                                                       T4TMR[7:0]
  0x032A             T4PR       7:0                                                        T4PR[7:0]
  0x032B            T4CON       7:0        ON                   CKPS[2:0]                                              OUTPS[3:0]
  0x032C            T4HLT       7:0       PSYNC      CPOL        CSYNC                                            MODE[4:0]
  0x032D          T4CLKCON      7:0                                                                                       CS[3:0]
  0x032E            T4RST       7:0                                                                               RSEL[4:0]
  0x032F
    ...           Reserved
  0x033F
                                7:0                                                   CCPR[7:0]
  0x0340               CCPRx
                                15:8                                                 CCPR[15:8]
  0x0342          CCP1CON       7:0        EN                     OUT             FMT                                        MODE[3:0]
  0x0343          CCPxCAP       7:0                                                                                                CTS[2:0]
  0x0344
    ...           Reserved
  0x034B
  0x034C         CCPTMRS0        7:0                                    C3TSEL[1:0]                        C2TSEL[1:0]                     C1TSEL[1:0]
  0x034D          Reserved
                                 7:0                                               CRCDATAL[7:0]
                                 15:8                                              CRCDATAH[7:0]
  0x034E          CRCDATA
                                23:16                                              CRCDATAU[7:0]
                                31:24                                              CRCDATAT[7:0]
                                 7:0                                                CRCOUTL[7:0]
                                 15:8                                              CRCOUTH[7:0]
  0x0352           CRCOUT
                                23:16                                              CRCOUTU[7:0]
                                31:24                                               CRCOUTT[7:0]
                                 7:0                                               CRCSHIFTL[7:0]
                                 15:8                                              CRCSHIFTH[7:0]
  0x0352          CRCSHIFT
                                23:16                                              CRCSHIFTU[7:0]
                                31:24                                              CRCSHIFTT[7:0]
                                 7:0                                                CRCXORL[7:0]
                                 15:8                                               CRCXORH[7:0]
  0x0352           CRCXOR
                                23:16                                               CRCXORU[7:0]
                                31:24                                               CRCXORT[7:0]
  0x0356          CRCCON0        7:0       EN         GO         BUSY            ACCM             SETUP[1:0]                        SHIFTM          FULL
  0x0357          CRCCON1        7:0                                                                    PLEN[4:0]
  0x0358          CRCCON2        7:0                                                                    DLEN[4:0]
  0x0359          Reserved
                                 7:0                                              SCANLADRL[7:0]
  0x035A         SCANLADR       15:8                                              SCANLADRH[7:0]
                                23:16                                                        SCANLADRU[5:0]
                                 7:0                                              SCANHADRL[7:0]
  0x035D         SCANHADR       15:8                                              SCANHADRH[7:0]
                                23:16                                                        SCANHADRU[5:0]
  0x0360         SCANCON0        7:0       EN       TRIGEN        SGO                                 MREG        BURSTMD                           BUSY
  0x0361         SCANTRIG        7:0                                                                        TSEL[3:0]
  0x0362
    ...           Reserved
  0x0366


--- p880 ---
...........continued
 Address               Name    Bit Pos.       7            6           5             4                 3                  2                 1                0
  0x0367               IPR0      7:0         IOCIP       CRCIP    CLC1IP     NVMIP                CSWIP                 OSFIP          HLVDIP            SWIP
  0x0368               IPR1      7:0      SMT1PWAIP    SMT1PRAIP  SMT1IP     CM1IP                ACTIP                 ADIP           ZCDIP            INT0IP
  0x0369               IPR2      7:0       DMA1AIP     DMA1ORIP DMA1DCNTIP DMA1SCNTIP                                                                   ADTIP
  0x036A               IPR3      7:0        TMR0IP       CCP1IP  TMR1GIP     TMR1IP              TMR2IP             SPI1IP            SPI1TXIP         SPI1RXIP
  0x036B             IPR4        7:0      PWM1IP       PWM1PIP   TMR3GIP     TMR3IP                   U1IP          U1EIP              U1TXIP           U1RXIP
  0x036C             IPR5        7:0      PWM2IP       PWM2PIP    CLC2IP      CMIP                                  SPI2IP            SPI2TXIP         SPI2RXIP
  0x036D             IPR6        7:0      DMA2AIP      DMA2ORIP DMA2DCNTIP DMA2SCNTIP            NCO1IP            CWG1IP                               INT1IP
  0x036E             IPR7        7:0      PWM3IP       PWM3PIP    CLC3IP                         I2C1EIP            I2C1IP            I2C1TXIP         I2C1RXIP
  0x036F             IPR8        7:0       SCANIP                 CLC4IP                           U2IP             U2EIP              U2TXIP           U2RXIP
  0x0370             IPR9        7:0      DMA3AIP      DMA3ORIP DMA3DCNTIP DMA3SCNTIP              U3IP             U3EIP              U3TXIP           U3RXIP
  0x0371            IPR10        7:0      DMA4AIP      DMA4ORIP DMA4DCNTIP DMA4SCNTIP            TMR4IP                                                 INT2IP
  0x0372          Reserved
  0x0373       STATUS_CSHAD     7:0                       TO          PD             N                OV                 Z                 DC                C
  0x0374        WREG_CSHAD      7:0                                                      WREG[7:0]
  0x0375         BSR_CSHAD       7:0                                                                         BSR[5:0]
  0x0376          SHADCON       7:0                                                                                                                    SHADLO
  0x0377        STATUS_SHAD     7:0                       TO          PD             N                OV                 Z                 DC             C
  0x0378         WREG_SHAD      7:0                                                      WREG[7:0]
  0x0379          BSR_SHAD       7:0                                                                         BSR[5:0]
                                 7:0                                                     PCLATH[7:0]
  0x037A        PCLAT_SHAD
                                15:8                                                                             PCLATU[4:0]
                                 7:0                                                      FSRL[7:0]
  0x037C         FSR0_SHAD
                                15:8                                                                       FSRH[5:0]
                                 7:0                                                      FSRL[7:0]
  0x037E         FSR1_SHAD
                                15:8                                                                       FSRH[5:0]
                                 7:0                                                      FSRL[7:0]
  0x0380         FSR2_SHAD
                                15:8                                                                       FSRH[5:0]
                                 7:0                                                     PROD[7:0]
  0x0382         PROD_SHAD
                                15:8                                                     PROD[15:8]
 0x0384
    ...           Reserved
 0x03BB
 0x03BC           CWG1CLK        7:0                                                                                                                         CS
 0x03BD           CWG1ISM        7:0                                                                                            ISM[3:0]
 0x03BE           CWG1DBR        7:0                                                                         DBR[5:0]
 0x03BF           CWG1DBF        7:0                                                                         DBF[5:0]
 0x03C0          CWG1CON0        7:0         EN           LD                                                                         MODE[2:0]
 0x03C1          CWG1CON1        7:0                                   IN                         POLD         POLC                   POLB               POLA
 0x03C2           CWG1AS0        7:0      SHUTDOWN       REN             LSBD[1:0]                    LSAC[1:0]
 0x03C3           CWG1AS1        7:0         AS7E        AS6E        AS5E         AS4E            AS3E         AS2E                        AS1E          AS0E
 0x03C4           CWG1STR        7:0        OVRD         OVRC        OVRB        OVRA             STRD         STRC                        STRB          STRA
 0x03C5
    ...           Reserved
 0x03D6
 0x03D7            FVRCON        7:0         EN           RDY        TSEN        TSRNG                  CDAFVR[1:0]                             ADFVR[1:0]
 0x03D8             ADCP         7:0        CPON                                                                                                        CPRDY
                                 7:0                                                      LTH[7:0]
  0x03D9               ADLTH
                                 15:8                                                    LTH[15:8]
                                 7:0                                                      UTH[7:0]
 0x03DB                ADUTH
                                 15:8                                                    UTH[15:8]
                                 7:0                                                      ERR[7:0]
 0x03DD                ADERR
                                 15:8                                                    ERR[15:8]
                                 7:0                                                      STPT[7:0]
  0x03DF           ADSTPT
                                 15:8                                                    STPT[15:8]
                                 7:0                                                      FLTR[7:0]
  0x03E1           ADFLTR
                                 15:8                                                    FLTR[15:8]
                                 7:0                                                      ACC[7:0]
  0x03E3               ADACC     15:8                                                    ACC[15:8]
                                23:16                                                                                                           ACC[17:16]
  0x03E6               ADCNT     7:0                                                      CNT[7:0]


--- p881 ---
...........continued
 Address               Name    Bit Pos.      7           6            5              4                3              2                1             0
  0x03E7               ADRPT    7:0                                                       RPT[7:0]
                                7:0                                                      PREV[7:0]
  0x03E8           ADPREV
                                15:8                                                     PREV[15:8]
                                7:0                                                       RES[7:0]
  0x03EA               ADRES
                                15:8                                                      RES[15:8]
  0x03EC           ADPCH        7:0                                                       PCH[7:0]
  0x03ED          Reserved
                                7:0                                                       ACQ[7:0]
  0x03EE               ADACQ
                                15:8                                                                             ACQ[12:8]
  0x03F0               ADCAP    7:0                                                                               CAP[4:0]
                                7:0                                                       PRE[7:0]
  0x03F1               ADPRE
                                15:8                                                                             PRE[12:8]
  0x03F3           ADCON0       7:0         ON         CONT                         CS                              FM                            GO
  0x03F4           ADCON1       7:0        PPOL        IPEN        GPOL                                                                          DSEN
  0x03F5           ADCON2       7:0        PSIS                   CRS[2:0]                           ACLR                        MD[2:0]
  0x03F6           ADCON3       7:0                               CALC[2:0]                           SOI                       TMD[2:0]
  0x03F7           ADSTAT       7:0        AOV         UTHR         LTHR        MATH                                            STAT[2:0]
  0x03F8            ADREF       7:0                                             NREF                                                   PREF[1:0]
  0x03F9            ADACT       7:0                                                                               ACT[4:0]
  0x03FA            ADCLK       7:0                                                                         CS[5:0]
  0x03FB
    ...           Reserved
  0x03FF
  0x0400           ANSELA        7:0                              ANSELA5     ANSELA4                            ANSELA2        ANSELA1         ANSELA0
  0x0401            WPUA         7:0                               WPUA5       WPUA4             WPUA3            WPUA2          WPUA1           WPUA0
  0x0402          ODCONA         7:0                               ODCA5       ODCA4                              ODCA2          ODCA1           ODCA0
  0x0403          SLRCONA        7:0                                SLRA5       SLRA4                              SLRA2          SLRA1           SLRA0
  0x0404           INLVLA        7:0                              INLVLA5     INLVLA4            INLVLA3         INLVLA2        INLVLA1         INLVLA0
  0x0405            IOCAP        7:0                               IOCAP5      IOCAP4             IOCAP3          IOCAP2         IOCAP1          IOCAP0
  0x0406           IOCAN         7:0                              IOCAN5      IOCAN4             IOCAN3          IOCAN2         IOCAN1          IOCAN0
  0x0407            IOCAF        7:0                               IOCAF5      IOCAF4             IOCAF3          IOCAF2         IOCAF1          IOCAF0
  0x0408           ANSELB        7:0      ANSELB7     ANSELB6     ANSELB5     ANSELB4
  0x0409            WPUB         7:0       WPUB7       WPUB6       WPUB5       WPUB4
  0x040A          ODCONB         7:0       ODCB7       ODCB6       ODCB5       ODCB4
  0x040B          SLRCONB        7:0        SLRB7       SLRB6       SLRB5       SLRB4
  0x040C           INLVLB        7:0      INLVLB7     INLVLB6     INLVLB5     INLVLB4
  0x040D            IOCBP        7:0       IOCBP7      IOCBP6      IOCBP5      IOCBP4
  0x040E           IOCBN         7:0      IOCBN7      IOCBN6      IOCBN5      IOCBN4
  0x040F            IOCBF        7:0       IOCBF7      IOCBF6      IOCBF5      IOCBF4
  0x0410           ANSELC        7:0      ANSELC7     ANSELC6     ANSELC5     ANSELC4            ANSELC3         ANSELC2        ANSELC1         ANSELC0
  0x0411            WPUC         7:0       WPUC7       WPUC6       WPUC5       WPUC4              WPUC3           WPUC2          WPUC1           WPUC0
  0x0412          ODCONC         7:0       ODCC7       ODCC6       ODCC5       ODCC4              ODCC3           ODCC2          ODCC1           ODCC0
  0x0413          SLRCONC        7:0        SLRC7       SLRC6       SLRC5       SLRC4              SLRC3           SLRC2          SLRC1           SLRC0
  0x0414           INLVLC        7:0      INLVLC7     INLVLC6     INLVLC5     INLVLC4            INLVLC3         INLVLC2        INLVLC1         INLVLC0
  0x0415            IOCCP        7:0       IOCCP7      IOCCP6      IOCCP5      IOCCP4             IOCCP3          IOCCP2         IOCCP1          IOCCP0
  0x0416           IOCCN         7:0      IOCCN7      IOCCN6      IOCCN5      IOCCN4             IOCCN3          IOCCN2         IOCCN1          IOCCN0
  0x0417            IOCCF        7:0       IOCCF7      IOCCF6      IOCCF5      IOCCF4             IOCCF3          IOCCF2         IOCCF1          IOCCF0
  0x0418
    ...           Reserved
  0x043F
                                 7:0                                                      ACC[7:0]
  0x0440          NCO1ACC        15:8                                                     ACC[15:8]
                                23:16                                                                                    ACC[19:16]
                                 7:0                                                       INC[7:0]
  0x0443          NCO1INC        15:8                                                     INC[15:8]
                                23:16                                                                                    INC[19:16]
  0x0446          NCO1CON        7:0        EN                      OUT             POL                                                            PFM
  0x0447          NCO1CLK        7:0                  PWS[2:0]                                                            CKS[3:0]
  0x0448
    ...           Reserved
  0x0457


--- p882 ---
...........continued
 Address               Name    Bit Pos.    7          6           5             4                 3          2              1            0
  0x0458          FSCMCON       7:0                            FSCMSFI     FSCMSEV          FSCMPFI      FSCMPEV       FSCMFFI        FSCMFEV
  0x0459           IVTLOCK      7:0                                                                                                  IVTLOCKED
                                7:0                                                 IVTADL[7:0]
  0x045A               IVTAD    15:8                                                IVTADH[7:0]
                                23:16                                                                   IVTADU[4:0]
                                  7:0                                           IVTBASEL[7:0]
  0x045D           IVTBASE       15:8                                           IVTBASEH[7:0]
                                23:16                                                                  IVTBASEU[4:0]
  0x0460          PWM1ERS         7:0                                                                           ERS[3:0]
  0x0461          PWM1CLK         7:0                                                                           CLK[3:0]
  0x0462          PWM1LDS         7:0                                                                          LDS[3:0]
                                  7:0                                                 PR[7:0]
  0x0463          PWM1PR
                                 15:8                                                PR[15:8]
  0x0465        PWM1CPRE          7:0                                               CPRE[7:0]
  0x0466        PWM1PIPOS         7:0                                               PIPOS[7:0]
  0x0467         PWM1GIR          7:0                                                                                   S1P2            S1P1
  0x0468         PWM1GIE          7:0                                                                                   S1P2            S1P1
  0x0469         PWM1CON          7:0      EN                                                               LD         ERSPOL         ERSNOW
  0x046A        PWM1S1CFG         7:0     POL2      POL1                                        PPEN                  MODE[2:0]
                                  7:0                                                P1[7:0]
  0x046B         PWM1S1P1
                                 15:8                                                P1[15:8]
                                  7:0                                                P2[7:0]
  0x046D         PWM1S1P2
                                 15:8                                                P2[15:8]
  0x046F          PWM2ERS         7:0                                                                            ERS[3:0]
  0x0470          PWM2CLK         7:0                                                                            CLK[3:0]
  0x0471          PWM2LDS         7:0                                                                            LDS[3:0]
                                  7:0                                                 PR[7:0]
  0x0472          PWM2PR
                                 15:8                                                PR[15:8]
  0x0474        PWM2CPRE          7:0                                               CPRE[7:0]
  0x0475        PWM2PIPOS         7:0                                               PIPOS[7:0]
  0x0476         PWM2GIR          7:0                                                                                   S1P2            S1P1
  0x0477         PWM2GIE          7:0                                                                                   S1P2            S1P1
  0x0478         PWM2CON          7:0      EN                                                               LD         ERSPOL         ERSNOW
  0x0479        PWM2S1CFG         7:0     POL2      POL1                                        PPEN                  MODE[2:0]
                                  7:0                                                P1[7:0]
  0x047A         PWM2S1P1
                                 15:8                                                P1[15:8]
                                  7:0                                                P2[7:0]
  0x047C         PWM2S1P2
                                 15:8                                                P2[15:8]
  0x047E          PWM3ERS         7:0                                                                            ERS[3:0]
  0x047F          PWM3CLK         7:0                                                                            CLK[3:0]
  0x0480          PWM3LDS         7:0                                                                            LDS[3:0]
                                  7:0                                                 PR[7:0]
  0x0481          PWM3PR
                                 15:8                                                PR[15:8]
  0x0483        PWM3CPRE          7:0                                               CPRE[7:0]
  0x0484        PWM3PIPOS         7:0                                               PIPOS[7:0]
  0x0485         PWM3GIR          7:0                                                                                   S1P2            S1P1
  0x0486         PWM3GIE          7:0                                                                                   S1P2            S1P1
  0x0487         PWM3CON          7:0      EN                                                               LD         ERSPOL         ERSNOW
  0x0488        PWM3S1CFG         7:0     POL2      POL1                                        PPEN                  MODE[2:0]
                                  7:0                                                P1[7:0]
  0x0489         PWM3S1P1
                                 15:8                                                P1[15:8]
                                  7:0                                                P2[7:0]
  0x048B         PWM3S1P2
                                 15:8                                                P2[15:8]
  0x048D
    ...           Reserved
  0x049B
  0x049C         PWMLOAD         7:0                                                                    MPWM3LD       MPWM2LD        MPWM1LD
  0x049D          PWMEN          7:0                                                                    MPWM3EN       MPWM2EN        MPWM1EN


--- p883 ---
...........continued
 Address               Name    Bit Pos.        7             6         5              4                 3                 2        1              0
  0x049E
    ...           Reserved
  0x04A7
  0x04A8               PIE0      7:0        IOCIE         CRCIE      CLC1IE      NVMIE             CSWIE                OSFIE   HLVDIE          SWIE
 0x04A9                 PIE1     7:0      SMT1PWAIE     SMT1PRAIE  SMT1IE     CM1IE                ACTIE                ADIE     ZCDIE         INT0IE
 0x04AA                 PIE2     7:0       DMA1AIE      DMA1ORIE DMA1DCNTIE DMA1SCNTIE                                                          ADTIE
 0x04AB                 PIE3     7:0        TMR0IE        CCP1IE  TMR1GIE     TMR1IE              TMR2IE             SPI1IE     SPI1TXIE      SPI1RXIE
 0x04AC                 PIE4     7:0       PWM1IE        PWM1PIE  TMR3GIE     TMR3IE               U1IE              U1EIE       U1TXIE        U1RXIE
 0x04AD                 PIE5     7:0       PWM2IE        PWM2PIE   CLC2IE     CM2IE                                  SPI2IE     SPI2TXIE      SPI2RXIE
 0x04AE                 PIE6     7:0       DMA2AIE      DMA2ORIE DMA2DCNTIE DMA2SCNTIE            NCO1IE            CWG1IE                     INT1IE
 0x04AF                 PIE7     7:0       PWM3IE        PWM3PIE   CLC3IE                         I2C1EIE            I2C1IE     I2C1TXIE      I2C1RXIE
 0x04B0                 PIE8     7:0        SCANIE                 CLC4IE                           U2IE             U2EIE       U2TXIE        U2RXIE
 0x04B1                 PIE9     7:0       DMA3AIE      DMA3ORIE DMA3DCNTIE DMA3SCNTIE              U3IE             U3EIE       U3TXIE        U3RXIE
 0x04B2                PIE10     7:0       DMA4AIE      DMA4ORIE DMA4DCNTIE DMA4SCNTIE            TMR4IE                                       INT2IE
 0x04B3                PIR0      7:0         IOCIF        CRCIF    CLC1IF     NVMIF                CSWIF                OSFIF   HLVDIF           SWIF
 0x04B4                PIR1      7:0      SMT1PWAIF     SMT1PRAIF  SMT1IF      CM1IF               ACTIF                ADIF    ZCDIF           INT0IF
 0x04B5                PIR2      7:0       DMA1AIF      DMA1ORIF DMA1DCNTIF DMA1SCNTIF                                                          ADTIF
 0x04B6                PIR3      7:0        TMR0IF        CCP1IF  TMR1GIF     TMR1IF              TMR2IF             SPI1IF     SPI1TXIF      SPI1RXIF
 0x04B7                PIR4      7:0       PWM1IF        PWM1PIF  TMR3GIF     TMR3IF               U1IF              U1EIF       U1TXIF        U1RXIF
 0x04B8                PIR5      7:0       PWM2IF        PWM2PIF   CLC2IF      CM2IF                                 SPI2IF     SPI2TXIF      SPI2RXIF
 0x04B9                PIR6      7:0       DMA2AIF      DMA2ORIF DMA2DCNTIF DMA2SCNTIF            NCO1IF            CWG1IF                      INT1IF
 0x04BA                PIR7      7:0       PWM3IF        PWM3PIF   CLC3IF                         I2C1EIF            I2C1IF     I2C1TXIF      I2C1RXIF
 0x04BB                PIR8      7:0        SCANIF                 CLC4IF                           U2IF             U2EIF       U2TXIF        U2RXIF
 0x04BC                PIR9      7:0       DMA3AIF      DMA3ORIF DMA3DCNTIF DMA3SCNTIF              U3IF             U3EIF       U3TXIF        U3RXIF
 0x04BD                PIR10     7:0       DMA4AIF      DMA4ORIF DMA4DCNTIF DMA4SCNTIF            TMR4IF                                        INT2IF
 0x04BE                LATA      7:0                                LATA5      LATA4                                 LATA2       LATA1          LATA0
 0x04BF                LATB      7:0        LATB7         LATB6     LATB5      LATB4
 0x04C0                LATC      7:0        LATC7         LATC6     LATC5      LATC4               LATC3             LATC2       LATC1          LATC0
 0x04C1
    ...           Reserved
 0x04C5
 0x04C6                TRISA     7:0                                 TRISA5      TRISA4          Reserved           TRISA2      TRISA1         TRISA0
 0x04C7                TRISB     7:0        TRISB7        TRISB6     TRISB5      TRISB4
 0x04C8                TRISC     7:0        TRISC7        TRISC6     TRISC5      TRISC4            TRISC3           TRISC2      TRISC1         TRISC0
 0x04C9
    ...           Reserved
 0x04CD
 0x04CE                PORTA     7:0                                  RA5            RA4               RA3               RA2      RA1           RA0
 0x04CF                PORTB     7:0         RB7           RB6        RB5            RB4
 0x04D0                PORTC     7:0         RC7           RC6        RC5            RC4               RC3               RC2      RC1           RC0
 0x04D1
    ...           Reserved
 0x04D5
 0x04D6           INTCON0       7:0        GIE/GIEH         GIEL      IPEN                                         INT2EDG      INT1EDG       INT0EDG
 0x04D7           INTCON1       7:0               STAT[1:0]
 0x04D8            STATUS       7:0                          TO       PD             N                 OV                 Z       DC             C
                                7:0                                                        FSRL[7:0]
  0x04D9               FSR2
                                15:8                                                                         FSRH[5:0]
 0x04DB            PLUSW2       7:0                                                    PLUSW[7:0]
 0x04DC            PREINC2      7:0                                                    PREINC[7:0]
 0x04DD           POSTDEC2      7:0                                                   POSTDEC[7:0]
 0x04DE           POSTINC2      7:0                                                   POSTINC[7:0]
 0x04DF             INDF2       7:0                                                     INDF[7:0]
 0x04E0              BSR        7:0                                                                          BSR[5:0]
                                7:0                                                        FSRL[7:0]
  0x04E1               FSR1
                                15:8                                                                         FSRH[5:0]
  0x04E3           PLUSW1       7:0                                                    PLUSW[7:0]
  0x04E4           PREINC1      7:0                                                    PREINC[7:0]
  0x04E5          POSTDEC1      7:0                                                   POSTDEC[7:0]
  0x04E6          POSTINC1      7:0                                                   POSTINC[7:0]
  0x04E7            INDF1       7:0                                                     INDF[7:0]


--- p884 ---
...........continued
 Address               Name    Bit Pos.      7                 6                5             4                 3               2                 1            0
  0x04E8               WREG     7:0                                                               WREG[7:0]
                                7:0                                                               FSRL[7:0]
  0x04E9               FSR0
                                15:8                                                                                FSRH[5:0]
  0x04EB           PLUSW0       7:0                                                               PLUSW[7:0]
  0x04EC           PREINC0       7:0                                                         PREINC[7:0]
  0x04ED          POSTDEC0       7:0                                                        POSTDEC[7:0]
  0x04EE          POSTINC0       7:0                                                        POSTINC[7:0]
  0x04EF            INDF0        7:0                                                          INDF[7:0]
  0x04F0            PCON0        7:0      STKOVF         STKUNF           WDTWV           RWDT        RMCLR                   RI             POR              BOR
  0x04F1            PCON1        7:0                                                                                        RVREG           MEMV              RCM
  0x04F2          CPUDOZE        7:0      IDLEN          DOZEN                 ROI          DOE                                            DOZE[2:0]
                                 7:0                                                            PROD[7:0]
  0x04F3               PROD
                                15:8                                                           PROD[15:8]
  0x04F5           TABLAT        7:0                                                           TABLAT[7:0]
                                 7:0                                                           TBLPTR[7:0]
  0x04F6           TBLPTR       15:8                                                          TBLPTR[15:8]
                                23:16                                    TBLPTR21                                       TBLPTR[20:16]
  0x04F9               PCL       7:0                                                                PCL[7:0]
                                 7:0                                                              PCLATH[7:0]
  0x04FA               PCLAT
                                15:8                                                                                     PCLATU[4:0]
  0x04FC           STKPTR        7:0                                                                     STKPTR[6:0]
                                 7:0                                                                TOS[7:0]
  0x04FD               TOS      15:8                                                               TOS[15:8]
                                23:16                                                                                     TOS[20:16]
 0x0500
   ...            Reserved
0x2FFFFF
0x300000          CONFIG1        7:0                          RSTOSC[2:0]                                                            FEXTOSC[2:0]
0x300001          CONFIG2        7:0      FCMENS      FCMENP     FCMEN                                    CSWEN                        PR1WAY     CLKOUTEN
0x300002          CONFIG3        7:0           BOREN[1:0]       LPBOREN                  IVT1WAY         MVECEN                PWRTS[1:0]           MCLRE
0x300003          CONFIG4        7:0       XINST                    LVP                   STVREN         PPS1WAY            ZCD              BORV[1:0]
0x300004          CONFIG5        7:0                      WDTE[1:0]                                                      WDTCPS[4:0]
0x300005          CONFIG6        7:0                                                   WDTCCS[2:0]                                   WDTCWS[2:0]
0x300006          CONFIG7        7:0                                      DEBUG          SAFEN             BBEN                       BBSIZE[2:0]
0x300007          CONFIG8        7:0      WRTAPP                                                          WRTSAF           WRTD         WRTC         WRTB
0x300008          CONFIG9        7:0                                                                                                                   CP
0x300009
   ...            Reserved
0x3FFFFB
                                 7:0             MJRREV[1:0]                                                    MNRREV[5:0]
 0x3FFFFC        REVISIONID
                                15:8                               1010[3:0]                                                        MJRREV[5:2]
                                 7:0                                                               DEV[7:0]
 0x3FFFFE         DEVICEID
                                15:8                                                               DEV[15:8]


--- p885 ---
