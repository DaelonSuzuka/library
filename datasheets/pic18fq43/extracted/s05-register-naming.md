                                                                                                         PIC18F27/47/57Q43
                                                                                        Register and Bit Naming Conventions


5.      Register and Bit Naming Conventions
5.1     Register Names
        When there are multiple instances of the same peripheral in a device, the Peripheral Control
        registers will be depicted as the concatenation of a peripheral identifier, peripheral instance, and
        control identifier. The Control registers section will show just one instance of all the register names
        with an ‘x’ in the place of the peripheral instance number. This naming convention may also be
        applied to peripherals when there is only one instance of that peripheral in the device to maintain
        compatibility with other devices in the family that contain more than one.

5.2     Bit Names
        There are two variants for bit names:
        •   Short name: Bit function abbreviation
        •   Long name: Peripheral abbreviation + short name

5.2.1   Short Bit Names
        Short bit names are an abbreviation for the bit function. For example, some peripherals are enabled
        with the EN bit. The bit names shown in the registers are the short name variant.
        Short bit names are useful when accessing bits in C programs. The general format for accessing bits
        by the short name is RegisterNamebits.ShortName. For example, the enable bit, ON, in the ADCON0
        register can be set in C programs with the instruction ADCON0bits.ON = 1.
        Short names are not useful in assembly programs because the same name may be used by different
        peripherals in different bit positions. When it occurs, during the include file generation, the short
        bit name instances are appended with an underscore plus the name of the register where the bit
        resides, to avoid naming contentions.

5.2.2   Long Bit Names
        Long bit names are constructed by adding a peripheral abbreviation prefix to the short name. The
        prefix is unique to the peripheral, thereby making every long bit name unique. The long bit name for
        the ADC enable bit is the ADC prefix, AD, appended with the enable bit short name, ON, resulting in
        the unique bit name ADON.
        Long bit names are useful in both C and assembly programs. For example, in C the ADCON0
        enable bit can be set with the ADON = 1 instruction. In assembly, this bit can be set with the BSF
        ADCON0,ADON instruction.

5.2.3   Bit Fields
        Bit fields are two or more adjacent bits in the same register. Bit fields adhere only to the short bit
        naming convention. For example, the three Least Significant bits of the ADCON2 register contain the
        ADC Operating Mode Selection bit. The short name for this field is MD and the long name is ADMD.
        Bit field access is only possible in C programs. The following example demonstrates a C program
        instruction for setting the ADC to operate in Accumulate mode:
        ADCON2bits.MD = 0b001;
        Individual bits in a bit field can also be accessed with long and short bit names. Each bit is
        the field name appended with the number of the bit position within the field. For example, the
        Most Significant MODE bit has the short bit name MD2 and the long bit name is ADMD2. The
        following two examples demonstrate assembly program sequences for setting the ADC to operate in
        Accumulate mode:

                 MOVLW   ~(1<<MD2 | 1<<MD1)
                 ANDWF   ADCON2,F


--- p25 ---
                                                                                                         PIC18F27/47/57Q43
                                                                                        Register and Bit Naming Conventions
                 MOVLW   1<<MD0
                 IORWF   ADCON2,F


                 BCF     ADCON2,ADMD2
                 BCF     ADCON2,ADMD1
                 BSF     ADCON2,ADMD0


5.3     Register and Bit Naming Exceptions
5.3.1   Status, Interrupt and Mirror Bits
        Status, Interrupt enables, Interrupt flags and Mirror bits are contained in registers that span more
        than one peripheral. In these cases, the bit name shown is unique so there is no prefix or short
        name variant.


--- p26 ---
