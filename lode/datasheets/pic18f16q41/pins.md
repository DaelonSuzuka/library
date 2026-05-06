# PIC18F16Q41 — Pin Diagrams & Allocation Tables

Source: DS40002214F Sections 1-3 (pages 10-16). Vision-extracted at 600 DPI.

## Package Variants

The PIC18F16Q41 is available in 20-pin PDIP, SOIC, SSOP, and VQFN packages.
The PIC18F04/05/06Q41 devices use 14-pin TSSOP/SOIC packages.

## 20-Pin PDIP/SOIC/SSOP (PIC18F16Q41)

### Pin Diagram

```
Pin  Name          Name  Pin
 1   VDD           VSS   20
 2   RA5           RA0   19
 3   RA4           RA1   18
 4   MCLR/VPP/RA3  RA2   17
 5   RC5           RC0   16
 6   RC4           RC1   15
 7   RC3           RC2   14
 8   RC6           RB4   13
 9   RC7           RB5   12
10   RB7           RB6   11
```

### Pin Allocation Table

| I/O | Pin# | A/D   | Reference              | Op Amp        | Comp          | ZCD   | Timers/SMT            | PWM/CCP        | CWG        | CLC        | SPI     | I2C     | UART    | DSM       | IOC   | Int     | Basic       |
|-----|------|-------|------------------------|---------------|---------------|-------|-----------------------|----------------|------------|------------|---------|---------|---------|-----------|-------|---------|-------------|
| RA0 | 19   | ANA0  | DAC1OUT1               | OPA1IN3+/-    | C1IN0+        | —     | —                     | —              | —          | —          | —       | —       | —       | —         | IOCA0 | —       | ICSPDAT     |
| RA1 | 18   | ANA1  | VREF+(ADC/DAC1/DAC2)   | —             | C1IN0-/C2IN0- | —     | —                     | —              | —          | —          | SS2(1)  | —       | —       | MDSRC(1)  | IOCA1 | —       | ICSPCLK     |
| RA2 | 17   | ANA2  | VREF-(ADC/DAC1/DAC2) DAC1OUT2 | OPA1IN2+/- | —            | ZCDIN | —                     | —              | CWGIN(1)  | CLCIN0(1) | —       | —       | —       | —         | IOCA2 | —       | —           |
| RA3 | 4    | —     | —                      | —             | —             | —     | —                     | —              | —          | —          | —       | —       | —       | —         | IOCA3 | —       | MCLR/VPP    |
| RA4 | 3    | ANA4  | —                      | —             | —             | —     | T1G(1) SMT1SIG(1)     | —              | —          | —          | —       | —       | —       | —         | IOCA4 | —       | CLKOUT/SOSCO|
| RA5 | 2    | ANA5  | —                      | —             | —             | —     | T2IN(1) SMT1WIN(1)    | PWM1ERS(1)     | —          | —          | —       | —       | —       | —         | IOCA5 | —       | CLKIN/SOSCI |
| RB4 | 13   | ANB4  | —                      | OPA1IN0-      | —             | —     | —                     | —              | —          | CLCIN2(1) | SDI1(1) | SDA1(3,4)| —      | —         | IOCB4 | —       | —           |
| RB5 | 12   | ANB5  | —                      | OPA1IN0+      | —             | —     | —                     | —              | —          | CLCIN3(1) | SDI2(1) | —       | RX1(1)  | —         | IOCB5 | —       | —           |
| RB6 | 11   | ANB6  | —                      | —             | —             | —     | —                     | —              | —          | —          | SCK1(1) | SCL1(3,4)| —      | —         | IOCB6 | —       | —           |
| RB7 | 10   | ANB7  | —                      | —             | —             | —     | —                     | —              | —          | —          | SCK2(1) | —       | CTS1(1) | —         | IOCB7 | —       | —           |
| RC0 | 16   | ANC0  | —                      | —             | C2IN0+        | —     | —                     | —              | —          | —          | —       | —       | —       | —         | IOCC0 | INT0(1) | —           |
| RC1 | 15   | ANC1  | —                      | —             | C1IN1-/C2IN1- | —     | T4IN(1)               | PWM2ERS(1)     | —          | —          | —       | —       | RX2(1)  | —         | IOCC1 | INT1(1) | —           |
| RC2 | 14   | ANC2  | —                      | OPA1OUT       | C1IN2-/C2IN2- | —     | —                     | PWM3ERS(1)     | —          | —          | —       | —       | CTS2(1) | MDCARL(1) | IOCC2 | INT2(1) | —           |
| RC3 | 7    | ANC3  | —                      | OPA1IN1+/-    | C1IN3-/C2IN3- | —     | —                     | PWMIN2(1)      | —          | CLCIN1(1) | —       | —       | RX3(1)  | —         | IOCC3 | —       | —           |
| RC4 | 6    | ANC4  | —                      | —             | —             | —     | T3G(1)                | —              | —          | —          | —       | —       | —       | —         | IOCC4 | —       | —           |
| RC5 | 5    | ANC5  | —                      | —             | —             | —     | T3CKI(1) T0CKI(1)     | CCP1IN(1) PWMIN1(1) | —       | —          | —       | —       | CTS3(1) | MDCARH(1) | IOCC5 | —       | —           |
| RC6 | 8    | ANC6  | —                      | —             | —             | —     | T1CKI(1)              | —              | —          | —          | SS1(1)  | —       | —       | —         | IOCC6 | —       | —           |
| RC7 | 9    | ANC7  | —                      | —             | —             | —     | —                     | —              | —          | —          | —       | —       | —       | —         | IOCC7 | —       | —           |

## 20-Pin VQFN (PIC18F16Q41)

### Pin Diagram

```
Pin  Name           Name  Pin
 1   MCLR/VPP/RA3   RC2   11
 2   RC5            RC1   12
 3   RC4            RC0   13
 4   RC3            RA2   14
 5   RC6            RA1   15
 6   RC7            RA0   16
 7   RB7            VSS   17
 8   RB6            VDD   18
 9   RB5            RA5   19
10   RB4            RA4   20
```

Pin allocation is identical to PDIP/SOIC/SSOP — same Table 3-2 applies. Exposed pad → VSS (must not be only VSS connection).

## PPS Output Allocations

All digital output signals below can be remapped to any PORTx pin via PPS:

| Signal Group | Available PPS Outputs |
|-------------|----------------------|
| A/D         | ADCGRDA, ADCGRDB |
| Comparator  | C1OUT, C2OUT |
| Timers/SMT  | TMR0 |
| PWM/CCP     | PWM11, PWM12, PWM21, PWM22, PWM31, PWM32, CCP1 |
| CWG         | CWG1A, CWG1B, CWG1C, CWG1D |
| CLC         | CLC1OUT, CLC2OUT, CLC3OUT, CLC4OUT |
| SPI         | SS1, SCK1, SDO1, SS2, SCK2, SDO2 |
| I2C         | SDA1, SCL1 |
| UART        | DTR1, RTS1, TX1, DTR2, RTS2, TX2, DTR3, RTS3, TX3 |
| DSM         | DSM1 |

## Notes

- (1) = PPS remappable input signal
- (3,4) = I2C bidirectional; configured for I2C logic levels on these pins only
- DAC1OUT1 on RA0, DAC1OUT2 on RA2
- OPA1OUT on RC2
- ADCC auto-trigger output (ADACT) on RC2
