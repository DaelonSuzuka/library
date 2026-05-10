                       PIC18(L)F26/27/45/46/47/55/56/57K42
12.0     8x8 HARDWARE MULTIPLIER                               EXAMPLE 12-1:         8x8 UNSIGNED MULTIPLY
                                                                                     ROUTINE
12.1     Introduction                                          MOVF     ARG1, W       ;
                                                               MULWF    ARG2          ; ARG1 * ARG2 ->
All PIC18 devices include an 8x8 hardware multiplier                                  ; PRODH:PRODL
as part of the ALU. The multiplier performs an unsigned
operation and yields a 16-bit result that is stored in the
product register pair, PRODH:PRODL. The multiplier’s           EXAMPLE 12-2:         8x8 SIGNED MULTIPLY
operation does not affect any flags in the STATUS                                    ROUTINE
register.
                                                               MOVF  ARG1, W
Making multiplication a hardware operation allows it to        MULWF ARG2             ; ARG1 * ARG2 ->
be completed in a single instruction cycle. This has the                              ; PRODH:PRODL
advantages of higher computational throughput and              BTFSC ARG2, SB         ; Test Sign Bit
reduced code size for multiplication algorithms and            SUBWF PRODH, F         ; PRODH = PRODH
allows the PIC18 devices to be used in many applica-                                  ;         - ARG1
tions previously reserved for digital signal processors.       MOVF     ARG2, W
                                                               BTFSC    ARG1, SB      ; Test Sign Bit
A comparison of various hardware and software
                                                               SUBWF    PRODH, F      ; PRODH = PRODH
multiply operations, along with the savings in memory                                 ;         - ARG2
and execution time, is shown in Table 12-1.

12.2     Operation
Example 12-1 shows the instruction sequence for an
8x8 unsigned multiplication. Only one instruction is
required when one of the arguments is already loaded in
the WREG register.
Example 12-2 shows the sequence to do an 8x8 signed
multiplication. To account for the sign bits of the
arguments, each argument’s Most Significant bit (MSb)
is tested and the appropriate subtractions are done.


TABLE 12-1:        PERFORMANCE COMPARISON FOR VARIOUS MULTIPLY OPERATIONS
                                                   Program                         Time
                                                             Cycles
     Routine              Multiply Method          Memory
                                                             (Max) @ 64 MHz @ 40 MHz @ 10 MHz @ 4 MHz
                                                   (Words)
                    Without hardware multiply          13     69       4.3 s      6.9 s    27.6 s     69 s
8x8 unsigned
                    Hardware multiply                  1       1       62.5 ns     100 ns     400 ns      1 s
                    Without hardware multiply          33     91       5.7 s      9.1 s    36.4 s     91 s
8x8 signed
                    Hardware multiply                   6      6       375 ns      600 ns     2.4 s      6 s
                    Without hardware multiply          21     242      15.1 s     24.2 s   96.8 s     242 s
16x16 unsigned
                    Hardware multiply                  28     28       1.8 s      2.8 s    11.2 s     28 s
                    Without hardware multiply          52     254      15.9 s     25.4 s   102.6 s    254 s
16x16 signed
                    Hardware multiply                  35     40       2.5 s      4.0 s    16.0 s     40 s


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 187
                       PIC18(L)F26/27/45/46/47/55/56/57K42
Example 12-3 shows the sequence to do a 16 x 16               EXAMPLE 12-4:       16 x 16 SIGNED
unsigned multiplication. Equation 12-1 shows the                                  MULTIPLY ROUTINE
algorithm that is used. The 32-bit result is stored in four       MOVF     ARG1L, W
registers (RES[3:0]).                                             MULWF    ARG2L         ; ARG1L * ARG2L ->
                                                                                         ; PRODH:PRODL
                                                                  MOVFF    PRODH, RES1   ;
EQUATION 12-1:          16 x 16 UNSIGNED                          MOVFF    PRODL, RES0   ;
                                                              ;
                        MULTIPLICATION                            MOVF     ARG1H, W
                        ALGORITHM                                 MULWF    ARG2H         ; ARG1H * ARG2H ->
                                                                                         ; PRODH:PRODL
 RES3:RES0     =    ARG1H:ARG1L  ARG2H:ARG2L                     MOVFF    PRODH, RES3   ;
               =    (ARG1H  ARG2H  216) +                       MOVFF    PRODL, RES2   ;
                    (ARG1H  ARG2L  28) +                    ;
                    (ARG1L  ARG2H  28) +                        MOVF     ARG1L, W
                                                                  MULWF    ARG2H         ; ARG1L * ARG2H ->
                    (ARG1L  ARG2L)                                                      ; PRODH:PRODL
                                                                  MOVF     PRODL, W      ;
                                                                  ADDWF    RES1, F       ; Add cross
EXAMPLE 12-3:           16 x 16 UNSIGNED                          MOVF     PRODH, W      ; products
                                                                  ADDWFC   RES2, F       ;
                        MULTIPLY ROUTINE                          CLRF     WREG          ;
     MOVF      ARG1L, W                                           ADDWFC   RES3, F       ;
     MULWF     ARG2L               ; ARG1L * ARG2L->          ;
                                   ; PRODH:PRODL                  MOVF     ARG1H, W      ;
     MOVFF     PRODH, RES1         ;                              MULWF    ARG2L         ; ARG1H * ARG2L ->
     MOVFF     PRODL, RES0         ;                                                     ; PRODH:PRODL
 ;                                                                MOVF     PRODL, W      ;
     MOVF      ARG1H, W                                           ADDWF    RES1, F       ; Add cross
     MULWF     ARG2H               ; ARG1H * ARG2H->              MOVF     PRODH, W      ; products
                                   ; PRODH:PRODL                  ADDWFC   RES2, F       ;
     MOVFF     PRODH, RES3         ;                              CLRF     WREG          ;
     MOVFF     PRODL, RES2         ;                              ADDWFC   RES3, F       ;
 ;                                                            ;
     MOVF      ARG1L, W                                           BTFSS    ARG2H, 7      ; ARG2H:ARG2L neg?
     MULWF     ARG2H               ; ARG1L * ARG2H->              BRA      SIGN_ARG1     ; no, check ARG1
                                   ; PRODH:PRODL                  MOVF     ARG1L, W      ;
     MOVF      PRODL, W            ;                              SUBWF    RES2          ;
     ADDWF     RES1, F             ; Add cross                    MOVF     ARG1H, W      ;
     MOVF      PRODH, W            ; products                     SUBWFB   RES3
     ADDWFC    RES2, F             ;                          ;
     CLRF      WREG                ;                          SIGN_ARG1
     ADDWFC    RES3, F             ;                              BTFSS    ARG1H, 7      ; ARG1H:ARG1L neg?
 ;                                                                BRA      CONT_CODE     ; no, done
     MOVF      ARG1H, W            ;                              MOVF     ARG2L, W      ;
     MULWF     ARG2L               ; ARG1H * ARG2L->              SUBWF    RES2          ;
                                   ; PRODH:PRODL                  MOVF     ARG2H, W      ;
     MOVF      PRODL, W            ;                              SUBWFB   RES3
     ADDWF     RES1, F             ; Add cross                ;
     MOVF      PRODH, W            ; products                 CONT_CODE
     ADDWFC    RES2, F             ;                              :
     CLRF      WREG                ;
     ADDWFC    RES3, F             ;


Example 12-4 shows the sequence to do a 16 x 16
signed multiply. Equation 12-2 shows the algorithm
used. The 32-bit result is stored in four registers
(RES[3:0]). To account for the sign bits of the
arguments, the MSb for each argument pair is tested
and the appropriate subtractions are done.

EQUATION 12-2:          16 x 16 SIGNED
                        MULTIPLICATION
                        ALGORITHM
RES3:RES0 = ARG1H:ARG1L  ARG2H:ARG2L
          = (ARG1H  ARG2H  216) +
            (ARG1H  ARG2L  28) +
            (ARG1L  ARG2H  28) +
            (ARG1L  ARG2L) +
            (-1  ARG2H[7]  ARG1H:ARG1L  216) +
            (-1  ARG1H[7]  ARG2H:ARG2L  216)


 2017-2021 Microchip Technology Inc.                                                     DS40001919G-page 188
