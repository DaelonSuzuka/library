# PIC18F16Q41 — Summary

PIC18 Q41 family mid-range 8-bit MCU. 64KB flash, 4KB RAM, 512B EEPROM, 64 MHz max. Available in 14-pin (04/05/06) and 20-pin (14/15/16) packages. All share the same peripheral set — 16-pin parts just have more GPIO.

## Architecture

- CPU: PIC18 enhanced RISC, 16-bit instructions, 8-bit data
- Vectored Interrupt Controller (VIC) with fixed 2-cycle latency
- 4 DMA channels, 1KB DMA SRAM
- Memory Access Partition (MAP) for bootloader protection
- Device Information Area (DIA) with factory calibration values

## Key Peripherals

- 3× UART (with DMX, DALI, LIN, Auto-baud)
- 2× SPI (with FIFOs)
- 1× I2C (host/client, 10-bit addr, SMBus)
- ADCC (12-bit ADC with computation, CVD for capacitive touch)
- 2× DAC (8-bit; DAC2 has no output pin)
- 1× OPA (operational amplifier)
- 2× Comparator
- 1× ZCD (zero-cross detect)
- Timer0 (8/16-bit), Timer1 (16-bit with gate), Timer2/4/6 (with HLT)
- 1× SMT (32-bit signal measurement)
- 1× CCP, 3× PWM (16-bit, 4 outputs each)
- 1× CWG, 1× NCO, 1× DSM
- 4× CLC (configurable logic cells)
- CRC with memory scanner
- Windowed WDT

## Pin Features

- Full PPS — most digital peripherals can route to any pin
- Maximum 18 I/O pins (20-pin package), 10 I/O (14-pin)
- VDD range: 1.8V–5.5V
- Industrial temp: -40°C to +85°C, Extended: -40°C to +125°C

## Used By

- MC-200 (SWR meter/tuner)
- MC-7300 (IC-7300 backlight controller)

## Datasheet

DS40002214F, 962 pages. Full extraction in `datasheets/pic18f16q41/extracted/`.

## Register Database

833 registers parsed from XC8 header → `datasheets/pic18f16q41/registers.json`
Device headers for all 6 Q41 family members in `datasheets/pic18f16q41/headers/`