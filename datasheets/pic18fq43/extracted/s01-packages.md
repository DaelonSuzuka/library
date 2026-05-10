                                                                                                           PIC18F27/47/57Q43
                                                                                                                     Packages


1.   Packages
     Table 1-1. Packages
                     28-pin   28-pin   28-pin     28-pin      40-pin      40-pin         44-pin     48-pin        48-pin
         Device      SPDIP     SOIC    SSOP     VQFN 4x4x1     PDIP     QFN 5x5x0.9      TQFP     TQFP 7x7x1   VQFN 6x6x0.9

      PIC18F25Q43      ●        ●        ●           ●
      PIC18F26Q43      ●        ●        ●           ●
      PIC18F27Q43      ●        ●        ●           ●
      PIC18F45Q43                                               ●           ●              ●
      PIC18F46Q43                                               ●           ●              ●
      PIC18F47Q43                                               ●           ●              ●
      PIC18F55Q43                                                                                     ●             ●
      PIC18F56Q43                                                                                     ●             ●
      PIC18F57Q43                                                                                     ●             ●


--- p10 ---
                                                                                      PIC18F27/47/57Q43
                                                                                            Pin Diagrams


2.   Pin Diagrams
     Figure 2-1.
     28-Pin SPDIP
     28-Pin SSOP
     28-Pin SOIC

                                MCLR/VPP/RE3    1                  28   RB7/ICSPDAT
                                         RA0    2                  27   RB6/ICSPCLK
                                         RA1    3                  26   RB5
                                         RA2    4                  25   RB4
                                         RA3    5                  24   RB3
                                         RA4    6                  23   RB2
                                         RA5    7                  22   RB1
                                         VSS    8                  21   RB0
                                         RA7    9                  20   VDD
                                         RA6    10                 19   VSS
                                         RC0    11                 18   RC7
                                         RC1    12                 17   RC6
                                         RC2    13                 16   RC5
                                         RC3    14                 15   RC4


     Figure 2-2.
     28-Pin VQFN
                                                RE3/MCLR/VPP
                                                RB7/ICSPDAT
                                                RB6/ICSPCLK
                                                RB5
                                                RA1
                                                RA0


                                                RB4


                                                28 27 26 25 24 23 22

                                       RA2 1                            21 RB3
                                       RA3 2                            20 RB2
                                       RA4 3                            19 RB1
                                       RA5 4                            18 RB0
                                       VSS 5                            17 VDD
                                       RA7 6                            16 VSS
                                       RA6 7                            15 RC7
                                                8    9 10 11 12 13 14
                                                RC4

                                                RC6
                                                RC0
                                                RC1
                                                RC2
                                                RC3

                                                RC5


     Note: It is recommended that the exposed bottom pad be connected to VSS; however, it must not
     be the only VSS connection to the device.

     Figure 2-3.
     40-Pin PDIP


--- p11 ---
                                                                                PIC18F27/47/57Q43
                                                                                      Pin Diagrams


                           MCLR/VPP/RE3    1                 40   RB7/ICSPDAT
                                    RA0    2                 39   RB6/ICSPCLK
                                    RA1    3                 38   RB5
                                    RA2    4                 37   RB4
                                    RA3    5                 36   RB3
                                    RA4    6                 35   RB2
                                    RA5    7                 34   RB1
                                    RE0    8                 33   RB0
                                    RE1    9                 32   VDD
                                    RE2    10                31   VSS
                                    VDD    11                30   RD7
                                    VSS    12                29   RD6
                                    RA7    13                28   RD5
                                    RA6    14                27   RD4
                                    RC0    15                26   RC7
                                    RC1    16                25   RC6
                                    RC2    17                24   RC5
                                    RC3    18                23   RC4
                                    RD0    19                22   RD3
                                    RD1    20                21   RD2


Figure 2-4.
40-Pin QFN
                                       RC5
                                       RC4
                                       RC6


                                       RD3
                                       RD2
                                       RD1
                                       RD0
                                       RC3
                                       RC2
                                       RC1

                                       40 39 38 37 36 35 34 33 32 31

                              RC7 1                                    30 RC0
                              RD4 2                                    29 RA6
                              RD5 3                                    28 RA7
                              RD6 4                                    27 VSS
                              RD7 5                                    26 VDD
                              VSS 6                                    25 RE2
                              VDD 7                                    24 RE1
                              RB0 8                                    23 RE0
                              RB1 9                                    22 RA5
                              RB2 10                                   21 RA4
                                       11 12 13 14 15 16 17 18 19 20
                                                RB3
                                                RB4
                                                RB5
                                        ICSPCLK/RB6
                                        ICSPDAT/RB7
                                       VPP/MCLR/RE3
                                                RA0
                                                RA1
                                                RA2
                                                RA3


Note: It is recommended that the exposed bottom pad be connected to VSS; however, it must not
be the only VSS connection to the device.

Figure 2-5.
44-Pin TQFP


--- p12 ---
                                                                                               PIC18F27/47/57Q43
                                                                                                     Pin Diagrams


                                          RC6
                                          RC5

                                          RD3
                                          RD2
                                          RD1
                                          RD0
                                          RC3
                                          RC2
                                          RC1
                                          RC4


                                          NC
                                         44 43 42 41 40 39 38 37 36 35 34

                         RC7        1                                        33          NC
                         RD4        2                                        32          RC0
                         RD5        3                                        31          RA6
                         RD6        4                                        30          RA7
                         RD7        5                                        29          VSS
                         VSS        6                                        28          VDD
                         VDD        7                                        27          RE2
                         RB0        8                                        26          RE1
                         RB1        9                                        25          RE0
                         RB2        10                                       24          RA5
                         RB3        11                                       23          RA4
                                         12 13 14 15 16 17 18 19 20 21 22


                                                    NC
                                                    NC

                                                   RB4
                                                   RB5
                                           ICSPCLK/RB6
                                           ICSPDAT/RB7
                                          VPP/MCLR/RE3
                                                   RA0
                                                   RA1
                                                   RA2
                                                   RA3
Figure 2-6.
48-Pin VQFN
                                        RD3
                                        RC6
                                        RC5
                                        RC4

                                        RD2
                                        RD1
                                        RD0
                                        RC3
                                        RC2
                                        RF3

                                                                            RF1
                                        RF2


                                        48 47 46 45 44 43 42 41 40 39 38 37
                            RC7 1                                          36 RF0
                            RD4 2                                             35 RC1
                            RD5 3                                             34   RC0
                            RD6 4                                             33 RA6
                            RD7 5                                             32 RA7
                            VSS 6                                             31 VSS
                            VDD 7                                             30 VDD
                               RB0 8                                          29 RE2
                               RB1 9                                          28 RE1
                               RB2 10                                         27 RE0
                               RB3 11                                         26 RA5

                               RF4 12                                      25 RA4
                                        13 14 15 16 17 18 19 20 21 22 23 24
                                                 RA1
                                                 RA0

                                                 RA2
                                                                            RA3
                                                 RF7


                                         ICSPCLK/RB6
                                                 RF6

                                                 RB4
                                                 RB5

                                         ICSPDAT/RB7
                                        VPP/MCLR/RE3
                                                 RF5


Note: It is recommended that the exposed bottom pad be connected to VSS; however, it must not
be the only VSS connection to the device.

Figure 2-7.
48-Pin TQFP


--- p13 ---
                                                              PIC18F27/47/57Q43
                                                                    Pin Diagrams


                RC6
                RC5
                RC4
                RD3

                RD1

                RC3
                RD2

                RD0

                RC2
                RF3

                                                 RF1
                RF2
                48 47 46 45 44 43 42 41 40 39 38 37
RC7       1                                        36   RF0
RD4       2                                        35   RC1
RD5       3                                        34   RC0
RD6       4                                        33   RA6
RD7       5                                        32   RA7
VSS       6                                        31   VSS
VDD       7                                        30   VDD
RB0       8                                        29   RE2
RB1       9                                        28   RE1
RB2       10                                       27   RE0
RB3        11                                      26   RA5
RF4        12                                     25    RA4
               13 14 15 16 17 18 19 20 21 22 23 24


                         RA1
                         RA0


                                                 RA3
                         RA2
                         RF7
                         RF6

                         RB4
                         RB5
                 ICSPCLK/RB6
                 ICSPDAT/RB7
                VPP/MCLR/RE3
                         RF5


--- p14 ---
