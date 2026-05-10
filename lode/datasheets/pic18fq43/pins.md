# PIC18F27/47/57Q43 — Pin Allocation Tables

Source: Q43 datasheet Sections 1, 16, 17.

## Package Variants

| Device | Program (bytes) | RAM (bytes) | Packages | I/O Ports |
|---|---|---|---|---|
| PIC18F27Q43 | 131072 | 8192 | 28-pin SPDIP/SOIC/SSOP/QFN/UQFN | A, B, C, E(1) |
| PIC18F47Q43 | 32768 | 2048 | 40-pin PDIP/UQFN, 44-pin TQFP/QFN | A, B, C, D, E(2) |
| PIC18F57Q43 | 131072 | 8192 | 48-pin TQFP/UQFN/VQFN | A, B, C, D, E, F |

(1) RE3 only. (2) RE0-RE2 + RE3.

## 28-Pin (PIC18F27Q43)

| I/O | Pin | A/D | Reference | Timers/SMT | CCP/PWM | CWG | CLC | DSM | IOC | Int | Basic |
|-----|-----|-----|-----------|------------|---------|-----|-----|-----|-----|-----|-------|
| RA0 | 2 | ANA0 | — | — | — | — | — | — | — | IOCA0 | — | ICSPDAT |
| RA1 | 3 | ANA1 | VREF+ | — | — | — | CLCIN1(1) | SS1(1) | — | MDSRC(1) | IOCA1 | — | ICSPCLK |
| RA2 | 4 | ANA2 | VREF- DAC1 | — | — | — | CLCIN0(1) | — | — | — | IOCA2 | — | — |
| RA3 | 5 | — | — | — | — | — | — | — | — | — | IOCA3 | — | MCLR/VPP |
| RA4 | 6 | ANA4 | — | T1G(1) SMT1SIG(1) | — | — | — | — | MD1CARL(1) MD1CARH(1) | IOCA4 | — | CLKOUT/SOSCO |
| RA5 | 7 | ANA5 | — | T2IN(1) SMT1WIN(1) | — | — | — | — | — | MD1SRC(1) | IOCA5 | — | CLKIN/SOSCI |
| RB0 | 21 | ANB0 | — | — | CCP4IN(1) | CWG1IN(1) | CLCIN4(1) | — | SDA2(3,4) | — | IOCB0 | INT0(1) | — |
| RB1 | 22 | ANB1 | — | — | — | CWG2IN(1) | — | — | SCL2(3,4) | — | IOCB1 | INT1(1) | — |
| RB2 | 23 | ANB2 | — | — | — | CWG3IN(1) | — | — | SDA2(3,4) | — | IOCB2 | INT2(1) | — |
| RB3 | 24 | ANB3 | — | — | — | — | — | — | — | — | IOCB3 | — | — |
| RB4 | 25 | ANB4 | — | T5G(1) | — | — | CLCIN2(1) | SDI1(1) | SDA1(3,4) | — | IOCB4 | — | — |
| RB5 | 26 | ANB5 | — | — | CCP3IN(1) | — | CLCIN3(1) | SDI2(1) | — | — | IOCB5 | — | — |
| RB6 | 27 | ANB6 | — | — | — | — | — | SCK1(1) | SCL1(3,4) | — | IOCB6 | — | PGC |
| RB7 | 28 | ANB7 | — | — | — | — | — | SCK2(1) | — | — | IOCB7 | — | PGD |
| RC0 | 11 | ANC0 | — | T1CKI(1) T3CKI(1) | — | — | — | — | — | — | IOCC0 | — | — |
| RC1 | 12 | ANC1 | — | — | CCP2IN(1) | — | — | — | — | RX1(1) | — | IOCC1 | — | — |
| RC2 | 13 | ANC2 | — | — | CCP1IN(1) | — | — | — | — | CTS1(1) | — | IOCC2 | — | — |
| RC3 | 14 | ANC3 | — | T2IN(1) | — | — | CLCIN1(1) | SCK1(1) | SCL1(3,4) | — | IOCC3 | — | — |
| RC4 | 15 | ANC4 | — | — | — | — | — | SDI1(1) | SDA1(3,4) | — | IOCC4 | — | — |
| RC5 | 16 | ANC5 | — | T0CKI(1) T3G(1) | — | — | — | — | MD1CARH(1) | — | IOCC5 | — | — |
| RC6 | 17 | ANC6 | — | T1G(1) | — | — | — | SS1(1) | — | — | IOCC6 | — | — |
| RC7 | 18 | ANC7 | — | — | — | — | — | — | — | RX1(1) | — | IOCC7 | — | — |
| RE3 | 1 | — | — | — | — | — | — | — | — | — | IOCE3 | — | MCLR/VPP |
| VDD | 20 | — | — | — | — | — | — | — | — | — | — | — | VDD |
| VSS | 8,19 | — | — | — | — | — | — | — | — | — | — | — | VSS |

## PPS Output Selections (RxyPPS values)

| RxyPPS Value | Output | 27Q43 Ports | 47Q43 Ports | 57Q43 Ports |
|---|---|---|---|---|
| 0x000000 | LATxy | A,B,C | A,B,C,D,E | A,B,C,D,E,F |
| 0x000001 | CLC1OUT | A,–,C | A,–,C,–,– | A,–,–,–,–,F |
| 0x000010 | CLC2OUT | –,B,C | –,B,C,–,– | –,B,–,D,–,– |
| 0x000011 | CLC3OUT | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x000100 | CLC4OUT | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x000101 | CLC5OUT | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x000110 | CLC6OUT | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x000111 | CLC7OUT | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x001000 | CLC8OUT | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x001001 | CWG1A | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x001010 | CWG1B | –,B,C | –,B,–,D,– | –,–,–,D,–,– |
| 0x001011 | CWG1C | –,B,C | –,B,–,D,– | –,–,–,D,–,– |
| 0x001100 | CWG1D | –,B,C | –,B,–,D,– | –,–,–,D,–,– |
| 0x001101 | CWG2A | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x001110 | CWG2B | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x001111 | CWG2C | –,B,C | –,B,–,D,– | –,–,–,D,–,– |
| 0x010000 | CWG2D | –,B,C | –,B,–,D,– | –,–,–,D,–,– |
| 0x010001 | CWG3A | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x010010 | CWG3B | A,–,C | A,–,–,–,E | A,–,–,–,E,– |
| 0x010011 | CCP1 | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x010100 | CCP2 | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x010101 | CCP3 | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x010110 | PWM1S1P1_OUT | A,–,C | A,–,C,–,– | A,–,–,–,–,F |
| 0x010111 | PWM1S1P2_OUT | –,B,C | –,B,–,D,– | –,–,–,D,–,– |
| 0x011000 | PWM2S1P1_OUT | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x011001 | PWM2S1P2_OUT | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x011010 | PWM3S1P1_OUT | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x011011 | PWM3S1P2_OUT | –,B,C | –,B,–,D,– | –,–,–,D,–,– |
| 0x011100 | NCO1 | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x011101 | NCO2 | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x011110 | NCO3 | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x011111 | DSM1 | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x100000 | CLKR | –,B,C | –,B,C,–,– | –,B,–,–,E,– |
| 0x100001 | UART1 TX | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x100010 | UART1 TXDE | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x100011 | UART1 RTS | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x100100 | UART2 TX | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x100101 | UART2 TXDE | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x100110 | UART2 RTS | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x100111 | UART3 TX | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x101000 | UART3 TXDE | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x101001 | UART3 RTS | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x101010 | UART4 TX | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x101011 | UART4 TXDE | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x101100 | UART4 RTS | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x101101 | UART5 TX | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x101110 | UART5 TXDE | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x101111 | UART5 RTS | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x110000 | C1OUT | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x110001 | C2OUT | A,–,C | A,–,–,–,E | A,–,–,–,E,– |
| 0x110010 | SPI1 SCK | –,B,C | –,B,C,–,– | –,B,C,–,–,– |
| 0x110011 | SPI1 SDO | –,B,C | –,B,C,–,– | –,B,C,–,–,– |
| 0x110100 | SPI1 SS | A,–,C | A,–,–,D,– | A,–,–,–,D,– |
| 0x110101 | SPI2 SCK | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x110110 | SPI2 SDO | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x110111 | SPI2 SS | –,B,C | –,B,–,D,– | –,B,–,D,–,– |
| 0x111000 | I2C1 SCL | –,B,C | –,B,C,–,– | –,B,C,–,–,– |
| 0x111001 | I2C1 SDA | –,B,C | –,B,C,–,– | –,B,C,–,–,– |
| 0x111010 | TMR0 | –,B,C | –,B,C,–,– | –,–,C,–,–,F |
| 0x111011 | ADGRDA | A,–,C | A,–,C,–,– | A,–,–,–,–,F |
| 0x111100 | ADGRDB | A,–,C | A,–,C,–,– | A,–,–,–,–,F |

## Key Peripheral Pin Assignments

### I2C-Capable Pads (hardware I2C levels)

28-pin devices: RB1, RB2, RC3, RC4
40/44-pin devices: RB1, RB2, RC3, RC4, RD0, RD1
48-pin devices: RB1, RB2, RC3, RC4, RD0, RD1

### PORTE Summary

| Device | PORTE Pins |
|---|---|
| 28-pin (27Q43) | RE3 only (input-only, MCLR/VPP when MCLRE=1) |
| 40/44-pin (47Q43) | RE0, RE1, RE2 (I/O) + RE3 (input-only) |
| 48-pin (57Q43) | RE0, RE1, RE2 (I/O) + RE3 (input-only) |

## Notes

- (1) = PPS remappable input signal
- (3,4) = I2C bidirectional; I2C logic levels available on these pads only
- RE3 is always input-only; functions as MCLR/VPP when MCLRE=1
- PORTD unavailable on 28-pin devices (PIC18F27Q43)
- PORTF only available on 48-pin devices (PIC18F57Q43)
- All digital outputs are PPS-remappable; analog I/O remains fixed
- POR on reset clears all PPS selections to defaults
- Q43 PWM uses slice-based outputs (PWM1S1P1, PWM1S1P2, etc.) instead of K42's PWM5–8