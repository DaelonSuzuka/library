# PIC18F26K42 — Pin Diagrams & Allocation Tables

Source: DS40001919G Sections 1, 16, 17 (pages 19-22, 260-285). Vision extraction needed for pin diagrams.

## Package Variants

| Device | Program (bytes) | RAM (bytes) | Packages | I/O Ports |
|--------|----------------|-------------|----------|-----------|
| PIC18F26K42 | 65536 | 4096 | 28-pin SPDIP/SOIC/SSOP/QFN/UQFN | A, B, C, E(1) |
| PIC18F27K42 | 131072 | 8192 | 28-pin SPDIP/SOIC/SSOP/QFN/UQFN | A, B, C, E(1) |
| PIC18F45K42 | 32768 | 2048 | 40-pin PDIP/UQFN, 44-pin TQFP/QFN | A, B, C, D, E(2) |
| PIC18F46K42 | 65536 | 4096 | 40-pin PDIP/UQFN, 44-pin TQFP/QFN | A, B, C, D, E(2) |
| PIC18F47K42 | 131072 | 8192 | 40-pin PDIP/UQFN, 44-pin TQFP/QFN | A, B, C, D, E(2) |
| PIC18F55K42 | 32768 | 2048 | 48-pin TQFP/UQFN/VQFN | A, B, C, D, E(2), F |
| PIC18F56K42 | 65536 | 4096 | 48-pin TQFP/UQFN/VQFN | A, B, C, D, E(2), F |
| PIC18F57K42 | 131072 | 8192 | 48-pin TQFP/UQFN/VQFN | A, B, C, D, E(2), F |

(1) RE3 only. (2) RE0-RE2 + RE3.

## 28-Pin SPDIP/SOIC/SSOP (PIC18F26/27K42) [needs vision extraction]

### Pin Diagram

```
[needs vision extraction — 28-pin SPDIP/SOIC/SSOP pinout diagram]
```

### Pin Allocation Table (28-pin)

| I/O | Pin | A/D | Reference | Timers/SMT | CCP/PWM | CWG | CLC | SPI | I2C | UART | DSM | IOC | Int | Basic |
|-----|-----|-----|-----------|------------|---------|-----|-----|-----|-----|------|-----|-----|-----|-------|
| RA0 | 2 | ANA0 | — | — | — | — | — | — | — | — | — | IOCA0 | — | ICSPDAT |
| RA1 | 3 | ANA1 | VREF+ | — | — | — | — | SS1(1) | — | — | MDSRC(1) | IOCA1 | — | ICSPCLK |
| RA2 | 4 | ANA2 | VREF- DAC1 | — | — | CWGIN(1) | CLCIN0(1) | — | — | — | — | IOCA2 | — | — |
| RA3 | 5 | — | — | — | — | — | — | — | — | — | — | IOCA3 | — | MCLR/VPP |
| RA4 | 6 | ANA4 | — | T1G(1) SMT1SIG(1) | — | — | — | — | — | — | MD1CARL(1) MD1CARH(1) | IOCA4 | — | CLKOUT/SOSCO |
| RA5 | 7 | ANA5 | — | T2IN(1) SMT1WIN(1) | PWM1ERS(1) | — | — | — | — | — | MD1SRC(1) | IOCA5 | — | CLKIN/SOSCI |
| RB0 | 21 | ANB0 | — | — | CCP4IN(1) | CWG1IN(1) | CLCIN(1) | — | — | — | — | IOCB0 | INT0(1) | — |
| RB1 | 22 | ANB1 | — | — | — | CWG2IN(1) | — | — | SCL2(3,4) | — | — | IOCB1 | INT1(1) | — |
| RB2 | 23 | ANB2 | — | — | — | CWG3IN(1) | — | — | SDA2(3,4) | — | — | IOCB2 | INT2(1) | — |
| RB3 | 24 | ANB3 | — | — | — | — | — | — | — | — | — | IOCB3 | — | — |
| RB4 | 25 | ANB4 | — | T5G(1) | — | — | CLCIN2(1) | SDI1(1) | SDA1(3,4) | — | — | IOCB4 | — | — |
| RB5 | 26 | ANB5 | — | — | CCP3IN(1) | — | CLCIN3(1) | SDI2(1) | — | RX2(1) | — | IOCB5 | — | — |
| RB6 | 27 | ANB6 | — | — | — | — | — | SCK1(1) | SCL1(3,4) | — | — | IOCB6 | — | PGC |
| RB7 | 28 | ANB7 | — | — | — | — | — | SCK2(1) | — | — | — | IOCB7 | — | PGD |
| RC0 | 11 | ANC0 | — | T1CKI(1) T3CKI(1) | — | — | — | — | — | — | — | IOCC0 | — | — |
| RC1 | 12 | ANC1 | — | — | CCP2IN(1) | — | — | — | — | RX1(1) | — | IOCC1 | — | — |
| RC2 | 13 | ANC2 | — | — | CCP1IN(1) PWMIN(1) | — | — | — | — | CTS1(1) | — | IOCC2 | — | — |
| RC3 | 14 | ANC3 | — | T2IN(1) | — | — | CLCIN1(1) | SCK1(1) | SCL1(3,4) | — | — | IOCC3 | — | — |
| RC4 | 15 | ANC4 | — | — | — | — | — | SDI1(1) | SDA1(3,4) | — | — | IOCC4 | — | — |
| RC5 | 16 | ANC5 | — | T0CKI(1) T3G(1) | CCP1IN(1) PWMIN1(1) | — | — | — | — | CTS3(1) | MD1CARH(1) | IOCC5 | — | — |
| RC6 | 17 | ANC6 | — | T1G(1) | — | — | — | SS1(1) | — | — | — | IOCC6 | — | — |
| RC7 | 18 | ANC7 | — | — | — | — | — | — | — | RX1(1) | — | IOCC7 | — | — |
| RE3 | 1 | — | — | — | — | — | — | — | — | — | — | IOCE3 | — | MCLR/VPP |
| VDD | 20 | — | — | — | — | — | — | — | — | — | — | — | — | VDD |
| VSS | 8,19 | — | — | — | — | — | — | — | — | — | — | — | — | VSS |

## 40-Pin PDIP (PIC18F45/46/47K42) [needs vision extraction]

```
[needs vision extraction — 40-pin PDIP pinout diagram]
```

Adds PORTD (RD0-RD7) and RE0-RE2. Same pin functions as 28-pin for PORTA/B/C with additional PORTD and full PORTE.

## 44-Pin TQFP (PIC18F45/46/47K42) [needs vision extraction]

```
[needs vision extraction — 44-pin TQFP pinout diagram]
```

Same pin allocation as 40-pin PDIP with additional VDD/VSS pins.

## 48-Pin TQFP/QFN (PIC18F55/56/57K42) [needs vision extraction]

```
[needs vision extraction — 48-pin TQFP/QFN pinout diagram]
```

Adds PORTF (RF0-RF7). All PORTA-E pins plus PORTF with dedicated PPS routing to port F.

## PPS-Remappable Pins

### PPS Input Selections (Table 17-1)

| Peripheral | Register | Default Pin | 26/27K42 Ports | 45/46/47K42 Ports | 55/56/57K42 Ports |
|-----------|----------|-------------|-----------------|-------------------|-------------------|
| INT0 | INT0PPS | RB0 | A, B, C | A, B, C, —, — | A, B, —, —, —, F |
| INT1 | INT1PPS | RB1 | A, B, C | A, B, C, —, — | —, B, —, D, —, — |
| INT2 | INT2PPS | RB2 | A, B, C | A, B, C, —, — | —, B, —, —, —, F |
| T0CKI | T0CKIPPS | RA4 | A, B, C | A, B, C, —, — | A, —, —, —, —, F |
| T1CKI | T1CKIPPS | RC0 | A, —, C | A, —, C, —, — | —, —, C, —, E, — |
| T1G | T1GPPS | RB5 | —, B, C | —, B, C, —, — | —, B, C, —, —, — |
| T3CKI | T3CKIPPS | RC0 | —, B, C | —, B, C, —, — | —, —, C, —, E, — |
| T3G | T3GPPS | RC0 | A, —, C | A, —, C, —, — | A, —, C, —, —, — |
| T5CKI | T5CKIPPS | RC2 | A, —, C | A, —, C, —, — | —, —, C, —, E, — |
| T5G | T5GPPS | RB4 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| T2IN | T2INPPS | RC3 | A, —, C | A, —, C, —, — | A, —, C, —, —, — |
| T4IN | T4INPPS | RC5 | —, B, C | —, B, C, —, — | —, B, C, —, —, — |
| T6IN | T6INPPS | RB7 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| CCP1 | CCP1PPS | RC2 | —, B, C | —, B, C, —, — | —, —, C, —, —, F |
| CCP2 | CCP2PPS | RC1 | —, B, C | —, B, C, —, — | —, —, C, —, —, F |
| CCP3 | CCP3PPS | RB5 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| CCP4 | CCP4PPS | RB0 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| SMT1WIN | SMT1WINPPS | RC0 | —, B, C | —, B, C, —, — | —, —, C, —, —, F |
| SMT1SIG | SMT1SIGPPS | RC1 | —, B, C | —, B, C, —, — | —, —, C, —, —, F |
| CWG1 | CWG1PPS | RB0 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| CWG2 | CWG2PPS | RB1 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| CWG3 | CWG3PPS | RB2 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| MD1CARL | MD1CARLPPS | RA3 | A, —, C | A, —, —, D, — | A, —, —, —, D, — |
| MD1CARH | MD1CARHPPS | RA4 | A, —, C | A, —, —, D, — | A, —, —, —, D, — |
| MD1SRC | MD1SRCPPS | RA5 | A, —, C | A, —, —, D, — | A, —, —, —, D, — |
| CLCIN0 | CLCIN0PPS | RA0 | A, —, C | A, —, C, —, — | A, —, C, —, —, — |
| CLCIN1 | CLCIN1PPS | RA1 | A, —, C | A, —, C, —, — | A, —, C, —, —, — |
| CLCIN2 | CLCIN2PPS | RB6 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| CLCIN3 | CLCIN3PPS | RB7 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| ADACT | ADACTPPS | RB4 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| SPI1SCK | SPI1SCKPPS | RC3 | —, B, C | —, B, C, —, — | —, B, C, —, —, — |
| SPI1SDI | SPI1SDIPPS | RC4 | —, B, C | —, B, C, —, — | —, B, C, —, —, — |
| SPI1SS | SPI1SSPPS | RA5 | A, —, C | A, —, —, D, — | A, —, —, —, D, — |
| I2C1SCL | I2C1SCLPPS | RC3 | —, B, C | —, B, C, —, — | —, B, C, —, —, — |
| I2C1SDA | I2C1SDAPPS | RC4 | —, B, C | —, B, C, —, — | —, B, C, —, —, — |
| I2C2SCL | I2C2SCLPPS | RB1 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| I2C2SDA | I2C2SDAPPS | RB2 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| U1RX | U1RXPPS | RC7 | —, B, C | —, B, C, —, — | —, —, C, —, —, F |
| U1CTS | U1CTSPPS | RC6 | —, B, C | —, B, C, —, — | —, —, C, —, —, F |
| U2RX | U2RXPPS | RB7 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |
| U2CTS | U2CTSPPS | RB6 | —, B, C | —, B, —, D, — | —, B, —, D, —, — |

Port columns = A, B, C, D, E, F. "—" = not available for that port on that device subset.

### PPS Output Selections (Table 17-2)

| RxyPPS Value | Output | 26K42 Ports | 45/46/47K42 Ports | 55/56/57K42 Ports |
|-------------|--------|-------------|-------------------|-------------------|
| 0b000000 | LATxy | A,B,C | A,B,C,D,E | A,B,C,D,E,F |
| 0b000001 | CLC1OUT | A,–,C | A,–,C,–,–,– | A,–,–,–,–,F |
| 0b000010 | CLC2OUT | A,–,C | A,–,C,–,–,– | A,–,–,–,–,F |
| 0b000011 | CLC3OUT | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b000100 | CLC4OUT | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b000101 | CWG1A | –,B,C | –,B,C,–,–,– | –,B,C,–,–,– |
| 0b000110 | CWG1B | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b000111 | CWG1C | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b001000 | CWG1D | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b001001 | CCP1 | –,B,C | –,B,C,–,–,– | –,–,C,–,–,F |
| 0b001010 | CCP2 | –,B,C | –,B,C,–,–,– | –,–,C,–,–,F |
| 0b001011 | CCP3 | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b001100 | CCP4 | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b001101 | PWM5 | A,–,C | A,–,C,–,–,– | A,–,–,–,–,F |
| 0b001110 | PWM6 | A,–,C | A,–,–,D,–,– | A,–,–,–,D,– |
| 0b001111 | PWM7 | A,–,C | A,–,C,–,–,– | –,–,C,–,–,F |
| 0b010000 | PWM8 | A,–,C | A,–,–,D,–,– | A,–,–,–,D,– |
| 0b010011 | UART1 TX | –,B,C | –,B,C,–,–,– | –,–,C,–,–,F |
| 0b010100 | UART1 TXDE | –,B,C | –,B,C,–,–,– | –,–,C,–,–,F |
| 0b010101 | UART1 RTS | –,B,C | –,B,C,–,–,– | –,–,C,–,–,F |
| 0b010110 | UART2 TX | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b010111 | UART2 TXDE | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b011000 | UART2 RTS | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b011100 | C1OUT | A,–,C | A,–,–,D,–,– | A,–,–,–,D,– |
| 0b011101 | C2OUT | A,–,C | A,–,–,–,E,– | A,–,–,–,E,– |
| 0b011110 | SPI1 SCK | –,B,C | –,B,C,–,–,– | –,B,C,–,–,– |
| 0b011111 | SPI1 SDO | –,B,C | –,B,C,–,–,– | –,B,C,–,–,– |
| 0b100000 | SPI1 SS | A,–,C | A,–,–,D,–,– | A,–,–,–,D,– |
| 0b100001 | I2C1 SCL | –,B,C | –,B,C,–,–,– | –,B,C,–,–,– |
| 0b100010 | I2C1 SDA | –,B,C | –,B,C,–,–,– | –,B,C,–,–,– |
| 0b100011 | I2C2 SCL | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b100100 | I2C2 SDA | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b100101 | TMR0 | –,B,C | –,B,C,–,–,– | –,–,C,–,–,F |
| 0b100110 | NCO1 | A,–,C | A,–,–,D,–,– | A,–,–,–,D,– |
| 0b100111 | CLKR | –,B,C | –,B,C,–,–,– | –,B,–,–,E,– |
| 0b100000 | DSM1 | A,–,C | A,–,–,D,–,– | A,–,–,–,D,– |
| 0b101001 | CWG2A | –,B,C | –,B,C,–,–,– | –,B,C,–,–,– |
| 0b101010 | CWG2B | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b101011 | CWG2C | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b101100 | CWG2D | –,B,C | –,B,–,D,–,– | –,B,–,D,–,– |
| 0b101101 | CWG3A | –,B,C | –,B,C,–,–,– | –,B,C,–,–,– |
| 0b101110 | CWG3B | A,–,C | A,–,–,–,E,– | A,–,–,–,E,– |
| 0b101111 | CWG3C | A,–,C | A,–,–,D,–,– | A,–,–,–,D,– |
| 0b110000 | CWG3D | A,–,C | A,–,–,D,–,– | A,–,–,–,D,– |
| 0b110001 | ADGRDA | A,–,C | A,–,C,–,–,– | A,–,–,–,–,F |
| 0b110010 | ADGRDB | A,–,C | A,–,C,–,–,– | A,–,–,–,–,F |

## Key Peripheral Pin Assignments

### Fixed Pins (not PPS-remappable)

| Function | Pin(s) | Notes |
|----------|--------|-------|
| MCLR/VPP | RA3(28-pin: pin 1) | Input-only when MCLRE=1 |
| T0CKI | RA4 / RC5 | Default PPS to RA4 |
| T1CKI/T3CKI | RC0 | Default |
| SOSCI/CLKIN | RA5 | |
| SOSCO/CLKOUT | RA4 | |
| ICSPDAT | RA0 | |
| ICSPCLK | RA1 | |
| PGC | RB6 | Debug clock |
| PGD | RB7 | Debug data |
| DAC1OUT | RA2 | Analog output |
| VREF+ | RA1 | ADC/DAC reference |
| VREF- | RA2 | ADC/DAC reference |

### I2C-Capable Pads (hardware I2C levels)

28-pin devices: RB1, RB2, RC3, RC4
40/44-pin devices: RB1, RB2, RC3, RC4, RD0, RD1
48-pin devices: RB1, RB2, RC3, RC4, RD0, RD1

### PORTE Summary

| Device | PORTE Pins |
|--------|------------|
| 28-pin (26/27K42) | RE3 only (input-only, MCLR/VPP when MCLRE=1) |
| 40/44-pin (45/46/47K42) | RE0, RE1, RE2 (I/O) + RE3 (input-only) |
| 48-pin (55/56/57K42) | RE0, RE1, RE2 (I/O) + RE3 (input-only) |

## Notes

- (1) = PPS remappable input signal
- (3,4) = I2C bidirectional; I2C logic levels available on these pads only
- RE3 is always input-only; functions as MCLR/VPP when MCLRE=1
- PORTD unavailable on 28-pin devices (PIC18F26/27K42)
- PORTF only available on 48-pin devices (PIC18F55/56/57K42)
- All digital outputs are PPS-remappable; analog I/O remains fixed
- POR on reset clears all PPS selections to defaults