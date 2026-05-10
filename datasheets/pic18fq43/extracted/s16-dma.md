                                                                                               PIC18F27/47/57Q43
                                                                                       DMA - Direct Memory Access


16.    DMA - Direct Memory Access
       The Direct Memory Access (DMA) module is designed to service data transfers between different
       memory regions directly, without intervention from the CPU. By eliminating the need for CPU-
       intensive management of handling interrupts intended for data transfers, the CPU now can spend
       more time on other tasks.
       The DMA modules can be independently programmed to transfer data between different memory
       locations, move different data sizes, and use a wide range of hardware triggers to initiate transfers.
       The DMA modules can even be programmed to work together, to carry out more complex data
       transfers without CPU overhead.
       Key features of the DMA module include:
       • Support access to the following memory regions:
            – GPR and SFR space (R/W)
            – Program Flash memory (R only)
            – Data EEPROM memory (R only)
       •   Programmable priority between the DMA and CPU operations. Refer to the “System
           Arbitration” section in the “PIC18 CPU” chapter for details.
       •   Programmable Source and Destination Address modes:
            – Fixed address
            – Post-increment address
            – Post-decrement address
       •   Programmable source and destination sizes
       •   Source and Destination Pointer register, dynamically updated and reloadable
       •   Source and Destination Count register, dynamically updated and reloadable
       •   Programmable auto-stop based on source or destination counter
       •   Software triggered transfers
       •   Multiple user-selectable sources for hardware triggered transfers
       •   Multiple user-selectable sources for aborting DMA transfers

16.1   DMA Registers
       The operation of the DMA module is controlled by the following registers:
       •   DMA Instance Selection (DMASELECT) register
       •   Control (DMAnCON0, DMAnCON1) registers
       •   Data Buffer (DMAnBUF) register
       •   Source Start Address (DMAnSSA) register
       •   Source Pointer (DMAnSPTR) register
       •   Source Message Size (DMAnSSZ) register
       •   Source Count (DMAnSCNT) register
       •   Destination Start Address (DMAnDSA) register
       •   Destination Pointer (DMAnDPTR) register
       •   Destination Message Size (DMAnDSZ) register
       •   Destination Count (DMAnDCNT) register
       •   Start Interrupt Request Source (DMAnSIRQ) register


--- p263 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                       DMA - Direct Memory Access

       •   Abort Interrupt Request Source (DMAnAIRQ) register
       The registers are detailed in Register Definitions: DMA.

16.2   DMA Organization
       The DMA module is designed to move data by using the existing instruction bus and data bus
       without the need for any dual-porting of memory or peripheral systems (Figure 16-1). The DMA
       accesses the required bus when granted by the system arbiter.

       Figure 16-1. DMA Functional Block Diagram
                                                                                                  Rev. 10-000271A
                                                                                                         11/8/2018


                                    DMA1

                               Control Registers


                              Source Start Address


                                  Source Size


                            Destination Start Address

                                                                                             Program Flash
                                                                                                Memory
                                Destination Size
                                                                      System Arbiter


                                       ..                                                    Data EEPROM

                                        ..
                                         .                                                     GPR/SFR
                                                                                              RAM Space
                                    DMAn

                               Control Registers


                              Source Start Address


                                                                   Priority
                                  Source Size


                            Destination Start Address


                                Destination Size


       Depending on the priority of the DMA with respect to CPU execution (refer to the “Memory Access
       Scheme” section in the “PIC18 CPU” chapter for more information), the DMA Controller can move
       data through two methods:
       •   Stalling the CPU execution until it has completed its transfers (DMA has higher priority over the
           CPU in this mode of operation)
       •   Utilizing unused CPU cycles for DMA transfers (CPU has higher priority over the DMA in this
           mode of operation). Unused CPU cycles are referred to as bubbles, which are instruction cycles
           available for use by the DMA to perform read and write operations. In this way, the effective
           bandwidth for handling data are increased; at the same time, DMA operations can proceed
           without causing a processor stall.


--- p264 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                      DMA - Direct Memory Access

16.3    DMA Interface
        The DMA module transfers data from the source to the destination one byte at a time, this smallest
        data movement is called a DMA data transaction. A DMA message refers to one or more DMA data
        transactions.
        Each DMA data transaction consists of two separate actions:
        • Reading the source address memory and storing the value in the DMA Buffer register
        •   Writing the contents of the DMA Buffer register to the destination address memory


                    Important: DMA data movement is a two-cycle operation.


        The XIP bit is a Status bit to indicate whether or not the data in the DMAnBUF register has been
        written to the destination address. If the bit is set, then data are waiting to be written to the
        destination. If clear, it means that either data have been written to the destination or that no source
        read has occurred.
        The DMA has read access to PFM, Data EEPROM, and SFR/GPR space and has write access to
        SFR/GPR space. Based on these memory access capabilities, the DMA can support the following
        memory transactions:

        Table 16-1. DMA Memory Access
                            Read Source                                                   Write Destination
                        Program Flash Memory                                                    GPR
                        Program Flash Memory                                                    SFR
                               Data EE                                                          GPR
                               Data EE                                                          SFR
                                GPR                                                             GPR
                                GPR                                                             SFR
                                SFR                                                             GPR
                                SFR                                                             SFR


                    Important: Even though the DMA module has access to all memory and
                    peripherals that are also available to the CPU, it is recommended that the DMA
                    does not access any register that is part of the system arbitration. The DMA, as a
                    system arbitration client must not be read or written by itself or by another DMA
                    instantiation.


        The following sections discuss the various control interfaces required for DMA data transfers.

16.3.1 Special Function Registers with DMA Access only
        The DMA can transfer data to any GPR or SFR location. For better user accessibility, some of the
        more commonly used SFR spaces have their mirror registers placed in a separate data memory
        location. These mirror registers can be only accessed by the DMA module through the DMA Source
        and Destination Address registers. The figure below shows the register map for these registers.
        These registers are useful to multiple peripherals together like the Timers, PWMs and also other
        DMA modules using one of the DMA modules.


--- p265 ---
                                                                                                                                                     PIC18F27/47/57Q43
                                                                                                                                             DMA - Direct Memory Access

       Figure 16-2. Special Function Register Map (DMA Access Only)
       40FFh          -       40DFh   -   40BFh     -     409Fh         -          407Fh           -        405Fh          -         403Fh          -          401Fh          -
       40FEh          -       40DEh   -   40BEh     -     409Eh         -          407Eh           -        405Eh          -         403Eh          -          401Eh          -
       40FDh          -       40DDh   -   40BDh     -     409Dh         -          407Dh      ADRESH_M1     405Dh          -         403Dh          -          401Dh          -
       40FCh          -       40DCh   -   40BCh     -     409Ch         -          407Ch      ADRESL_M1     405Ch          -         403Ch          -          401Ch          -
       40FBh          -       40DBh   -   40BBh     -     409Bh         -          407Bh      ADPCH_M1      405Bh          -         403Bh          -          401Bh   PWM3S1P2H_M1
       40FAh          -       40DAh   -   40BAh     -     409Ah         -          407Ah       ADCLK_M1     405Ah          -         403Ah          -          401Ah   PWM3S1P2L_M1
       40F9h          -       40D9h   -   40B9h     -     4099h         -          4079h      ADACT_M1      4059h          -         4039h          -          4019h   PWM3S1P1H_M2
       40F8h          -       40D8h   -   40B8h     -     4098h         -          4078h       ADREF_M1     4058h          -         4038h          -          4018h   PWM3S1P1L_M2
       40F7h          -       40D7h   -   40B7h     -     4097h         -          4077h     ADCON3_M1      4057h          -         4037h          -          4017h   PWM2S1P2H_M1
       40F6h      ADRESH_M2   40D6h   -   40B6h     -     4096h         -          4076h     ADCON2_M1      4056h          -         4036h          -          4016h   PWM2S1P2L_M1
       40F5h      ADRESL_M2   40D5h   -   40B5h     -     4095h         -          4075h     ADCON1_M1      4055h          -         4035h          -          4015h   PWM2S1P1H_M2
       40F4h      ADPCH_M2    40D4h   -   40B4h     -     4094h         -          4074h     ADCON0_M1      4054h          -         4034h          -          4014h   PWM2S1P1L_M2
       40F3h      ADCAP_M2    40D3h   -   40B3h     -     4093h         -          4073h      ADCAP_M1      4053h          -         4033h          -          4013h   PWM1S1P2H_M1
       40F2h     ADACQH_M2    40D2h   -   40B2h     -     4092h         -          4072h     ADACQH_M1      4052h          -         4032h          -          4012h   PWM1S1P2L_M1
       40F1h     ADACQL_M2    40D1h   -   40B1h     -     4091h         -          4071h     ADACQL_M1      4051h          -         4031h      PWM3PRH_M1     4011h   PWM1S1P1H_M2
       40F0h     ADPREVH_M2   40D0h   -   40B0h     -     4090h         -          4070h     ADPREVH_M1     4050h          -         4030h      PWM3PRL_M1     4010h   PWM1S1P1L_M2
       40EFh     ADPREVL_M2   40CFh   -   40AFh     -     408Fh         -          406Fh     ADPREVL_M1     404Fh          -         402Fh     PWM3S1P2H_M2    400Fh          -
       40EEh      ADRPT_M2    40CEh   -   40AEh     -     408Eh         -          406Eh      ADRPT_M1      404Eh          -         402Eh     PWM3S1P2L_M2    400Eh          -
       40EDh      ADCNT_M2    40CDh   -   40ADh     -     408Dh         -          406Dh      ADCNT_M1      404Dh          -         402Dh     PWM3S1P1H_M3    400Dh          -
       40ECh     ADACCU_M2    40CCh   -   40ACh     -     408Ch         -          406Ch     ADACCU_M1      404Ch          -         402Ch     PWM3S1P1L_M3    400Ch          -
       40CBh     ADACCH_M2    40CBh   -   40ABh     -     408Bh         -          406Bh     ADACCH_M1      404Bh          -         402Bh      PWM2PRH_M1     400Bh   PWM3S1P1H_M1
       40EAh      ADACCL_M2   40CAh   -   40AAh     -     408Ah         -          406Ah      ADACCL_M1     404Ah          -         402Ah      PWM2PRL_M1     400Ah   PWM3S1P1L_M1
       40E9h     ADFLTRH_M2   40C9h   -   40A9h     -     4089h         -          4069h     ADFLTRH_M1     4049h          -         4029h     PWM2S1P2H_M2    4009h   PWM2S1P1H_M1
       40E8h     ADFLTRL_M2   40C8h   -   40A8h     -     4088h         -          4068h     ADFLTRL_M1     4048h      T6PR_M1       4028h     PWM2S1P2L_M2    4008h   PWM2S1P1L_M1
       40E7h     ADSTPTH_M2   40C7h   -   40A7h     -     4087h         -          4067h     ADSTPTH_M1     4047h     CCPR3H_M2      4027h     PWM2S1P1H_M3    4007h   PWM1S1P1H_M1
       40E6h     ADSTPTL_M2   40C6h   -   40A6h     -     4086h         -          4066h     ADSTPTL_M1     4046h     CCPR3L_M2      4026h     PWM2S1P1L_M3    4006h   PWM1S1P1L_M1
       40E5h     ADERRH_M2    40C5h   -   40A5h     -     4085h         -          4065h     ADERRH_M1      4045h      T4PR_M1       4025h      PWM1PRH_M1     4005h     CCPR3H_M1
       40E4h      ADERRL_M2   40C4h   -   40A4h     -     4084h         -          4064h      ADERRL_M1     4044h     CCPR2H_M2      4024h      PWM1PRL_M1     4004h     CCPR3L_M1
       40E3h     ADUTHH_M2    40C3h   -   40A3h     -     4083h         -          4063h     ADUTHH_M1      4043h     CCPR2L_M2      4023h     PWM1S1P2H_M2    4003h     CCPR2H_M1
       40E2h     ADUTHL_M2    40C2h   -   40A2h     -     4082h         -          4062h     ADUTHL_M1      4042h      T2PR_M1       4022h     PWM1S1P2L_M2    4002h     CCPR2L_M1
       40E1h     ADLTHH_M2    40C1h   -   40A1h     -     4081h         -          4061h     ADLTHH_M1      4041h     CCPR1H_M2      4021h     PWM1S1P1H_M3    4001h     CCPR1H_M1
       40E0h      ADLTHL_M2   40C0h   -   40A0h     -     4080h         -          4060h      ADLTHL_M1     4040h     CCPR1L_M2      4020h     PWM1S1P1L_M3    4000h     CCPR1L_M1


       41FFh          -       41DFh   -   41BFh     -     419Fh           -        417Fh   DMAnSPTRH_DMA6   415Fh   DMAnDPTRL_DMA5   413Fh     DMAnSSAH_DMA3   411Fh   DMAnDSAH_DMA2
       41FEh          -       41DEh   -   41BEh     -     419Eh           -        417Eh   DMAnSPTRL_DMA6   415Eh   DMAnDCNTH_DMA5   413Eh     DMAnSSAL_DMA3   411Eh    DMAnDSAL_DMA2
       41FDh          -       41DDh   -   41BDh     -     419Dh           -        417Dh   DMAnSCNTH_DMA6   415Dh   DMAnDCNTL_DMA5   413Dh     DMAnSSZH_DMA3   411Dh    DMAnDSZH_DMA2
       41FCh          -       41DCh   -   41BCh     -     419Ch           -        417Ch   DMAnSCNTL_DMA6   415Ch    DMAnBUF_DMA5    413Ch     DMAnSSZL_DMA3   411Ch    DMAnDSZL_DMA2
       41FBh     TMR5H_M1     41DBh   -   41BBh     -     419Bh           -        417Bh   DMAnDSAH_DMA6    415Bh    DMAnSIRQ_DMA4   413Bh    DMAnSPTRU_DMA3   411Bh   DMAnDPTRH_DMA2
       41FAh     TMR5L_M1     41DAh   -   41BAh     -     419Ah           -        417Ah    DMAnDSAL_DMA6   415Ah    DMAnAIRQ_DMA4   413Ah    DMAnSPTRH_DMA3   411Ah   DMAnDPTRL_DMA2
       41F9h     TMR3H_M1     41D9h   -   41B9h     -     4199h           -        4179h    DMAnDSZH_DMA6   4159h   DMAnCON1_DMA4    4139h    DMAnSPTRL_DMA3   4119h   DMAnDCNTH_DMA2
       41F8h     TMR3L_M1     41D8h   -   41B8h     -     4198h           -        4178h    DMAnDSZL_DMA6   4158h   DMAnCON0_DMA4    4138h    DMAnSCNTH_DMA3   4118h   DMAnDCNTL_DMA2
       41F7h     TMR1H_M1     41D7h   -   41B7h     -     4197h           -        4177h   DMAnDPTRH_DMA6   4157h    DMAnSSAU_DMA4   4137h    DMAnSCNTL_DMA3   4117h    DMAnBUF_DMA2
       41F6h     TMR1L_M1     41D6h   -   41B6h     -     4196h           -        4176h   DMAnDPTRL_DMA6   4156h    DMAnSSAH_DMA4   4136h    DMAnDSAH_DMA3    4116h    DMAnSIRQ_DMA1
       41F5h          -       41D5h   -   41B5h     -     4195h           -        4175h   DMAnDCNTH_DMA6   4155h    DMAnSSAL_DMA4   4135h     DMAnDSAL_DMA3   4115h    DMAnAIRQ_DMA1
       41F4h          -       41D4h   -   41B4h     -     4194h           -        4174h   DMAnDCNTL_DMA6   4154h    DMAnSSZH_DMA4   4134h     DMAnDSZH_DMA3   4114h   DMAnCON1_DMA1
       41F3h          -       41D3h   -   41B3h     -     4193h           -        4173h    DMAnBUF_DMA6    4153h    DMAnSSZL_DMA4   4133h     DMAnDSZL_DMA3   4113h   DMAnCON0_DMA1
       41F2h          -       41D2h   -   41B2h     -     4192h           -        4172h    DMAnSIRQ_DMA5   4152h   DMAnSPTRU_DMA4   4132h    DMAnDPTRH_DMA3   4112h    DMAnSSAU_DMA1
       41F1h          -       41D1h   -   41B1h     -     4191h           -        4171h    DMAnAIRQ_DMA5   4151h   DMAnSPTRH_DMA4   4131h    DMAnDPTRL_DMA3   4111h    DMAnSSAH_DMA1
       41F0h          -       41D0h   -   41B0h     -     4190h           -        4170h   DMAnCON1_DMA5    4150h   DMAnSPTRL_DMA4   4130h    DMAnDCNTH_DMA3   4110h    DMAnSSAL_DMA1
       41EFh          -       41CFh   -   41AFh     -     418Fh           -        416Fh   DMAnCON0_DMA5    414Fh   DMAnSCNTH_DMA4   412Fh    DMAnDCNTL_DMA3   410Fh    DMAnSSZH_DMA1
       41EEh          -       41CEh   -   41AEh     -     418Eh           -        416Eh    DMAnSSAU_DMA5   414Eh   DMAnSCNTL_DMA4   412Eh     DMAnBUF_DMA3    410Eh    DMAnSSZL_DMA1
       41EDh          -       41CDh   -   41ADh     -     418Dh           -        416Dh    DMAnSSAH_DMA5   414Dh   DMAnDSAH_DMA4    412Dh     DMAnSIRQ_DMA2   410Dh   DMAnSPTRU_DMA1
       41ECh          -       41CCh   -   41ACh     -     418Ch           -        416Ch    DMAnSSAL_DMA5   414Ch    DMAnDSAL_DMA4   412Ch     DMAnAIRQ_DMA2   410Ch   DMAnSPTRH_DMA1
       41CBh          -       41CBh   -   41ABh     -     418Bh           -        416Bh    DMAnSSZH_DMA5   414Bh    DMAnDSZH_DMA4   412Bh    DMAnCON1_DMA2    410Bh   DMAnSPTRL_DMA1
       41EAh          -       41CAh   -   41AAh     -     418Ah           -        416Ah    DMAnSSZL_DMA5   414Ah    DMAnDSZL_DMA4   412Ah    DMAnCON0_DMA2    410Ah   DMAnSCNTH_DMA1
       41E9h          -       41C9h   -   41A9h     -     4189h    DMAnSIRQ_DMA6   4169h   DMAnSPTRU_DMA5   4149h   DMAnDPTRH_DMA4   4129h     DMAnSSAU_DMA2   4109h   DMAnSCNTL_DMA1
       41E8h          -       41C8h   -   41A8h     -     4188h   DMAnAIRQ_DMA6    4168h   DMAnSPTRH_DMA5   4148h   DMAnDPTRL_DMA4   4128h     DMAnSSAH_DMA2   4108h   DMAnDSAH_DMA1
       41E7h          -       41C7h   -   41A7h     -     4187h   DMAnCON1_DMA6    4167h   DMAnSPTRL_DMA5   4147h   DMAnDCNTH_DMA4   4127h     DMAnSSAL_DMA2   4107h    DMAnDSAL_DMA1
       41E6h          -       41C6h   -   41A6h     -     4186h   DMAnCON0_DMA6    4166h   DMAnSCNTH_DMA5   4146h   DMAnDCNTL_DMA4   4126h     DMAnSSZH_DMA2   4106h    DMAnDSZH_DMA1
       41E5h          -       41C5h   -   41A5h     -     4185h   DMAnSSAU_DMA6    4165h   DMAnSCNTL_DMA5   4145h    DMAnBUF_DMA4    4125h     DMAnSSZL_DMA2   4105h    DMAnDSZL_DMA1
       41E4h          -       41C4h   -   41A4h     -     4184h   DMAnSSAH_DMA6    4164h   DMAnDSAH_DMA5    4144h    DMAnSIRQ_DMA3   4124h    DMAnSPTRU_DMA2   4104h   DMAnDPTRH_DMA1
       41E3h      IOCEF_M1    41C3h   -   41A3h     -     4183h    DMAnSSAL_DMA6   4163h    DMAnDSAL_DMA5   4143h    DMAnAIRQ_DMA3   4123h    DMAnSPTRH_DMA2   4103h   DMAnDPTRL_DMA1
       41E2h      IOCCF_M1    41C2h   -   41A2h     -     4182h    DMAnSSZH_DMA6   4162h    DMAnDSZH_DMA5   4142h   DMAnCON1_DMA3    4122h    DMAnSPTRL_DMA2   4102h   DMAnDCNTH_DMA1
       41E1h      IOCBF_M1    41C1h   -   41A1h     -     4181h    DMAnSSZL_DMA6   4161h    DMAnDSZL_DMA5   4141h   DMAnCON0_DMA3    4121h    DMAnSCNTH_DMA2   4101h   DMAnDCNTL_DMA1
       41E0h      IOCAF_M1    41C0h   -   41A0h     -     4180h   DMAnSPTRU_DMA6   4160h   DMAnDPTRH_DMA5   4140h    DMAnSSAU_DMA3   4120h    DMAnSCNTL_DMA2   4100h    DMAnBUF_DMA1


16.3.2 DMA Addressing
       The start addresses for the source read and destination write operations are set using the DMAnSSA
       and DMAnDSA registers, respectively.
       When the DMA message transfers are in progress, the DMAnSPTR and DMAnDPTR registers contain
       the current Address Pointers for each source read and destination write operation. These registers
       are modified after each transaction based on the Address mode selection bits.
       The SMODE and DMODE bits determine the Address modes of operation by controlling how the
       DMAnSPTR and DMAnDPTR registers are updated after every DMA data transaction (Figure 16-3).
       Each address can be separately configured to:
       • Remain unchanged
       •       Increment by 1
       •       Decrement by 1


--- p266 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                                DMA - Direct Memory Access

       Figure 16-3. DMA Pointers Block Diagram


                                       DMAnSSA                                                  DMAnDSA


                                       DMAnSPTR                                                 DMAnDPTR


                        +1                                                       +1
                         0                                                        0
                        -1                                                       -1

                               SMODE                                                    DMODE


       The DMA can initiate data transfers from the PFM, Data EEPROM or SFR/GPR space. The SMR bits are
       used to select the type of memory being pointed to by the Source Address Pointer. The SMR bits are
       required because the PFM and SFR/GPR spaces have overlapping addresses that do not allow the
       specified address to uniquely define the memory location to be accessed.


                    Important:
                    1. For proper memory read access to occur, the combination of address and
                       space selection must be valid.
                    2. The destination does not have space selection bits because it can only write to
                       the SFR/GPR space.


16.3.3 DMA Message Size/Counters
       A transaction is the transfer of one byte. A message consists of one or more transactions. A
       complete DMA process consists of one or more messages. The size registers determine how many
       transactions are in a message. The DMAnSSZ registers determine the source size and DMAnDSZ
       registers determine the destination size.
       When a DMA transfer is initiated, the size registers are copied to corresponding counter registers
       that control the duration of the message. The DMAnSCNT registers count the source transactions
       and the DMAnDCNT registers count the destination transactions. Both are simultaneously
       decremented by one after each transaction.
       A message is started by setting the DGO bit and terminates when the smaller of the two counters
       reaches zero.
       When either counter reaches zero, the DGO bit is cleared and the counter and pointer registers are
       immediately reloaded with the corresponding size and address data. If the other counter did not
       reach zero, then the next message will continue with the count and address corresponding to that
       register. Refer to Figure 16-4.


--- p267 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                                     DMA - Direct Memory Access

       When the Source and Destination Size registers are not equal, then the ratio of the largest to the
       smallest size determines how many messages are in the DMA process. For example, when the
       destination size is six and the source size is two, then each message will consist of two transactions
       and the complete DMA process will consist of three messages. When the larger size is not an even
       integer of the smaller size, then the last message in the process will terminate early when the larger
       count reaches zero. In that case, the larger counter will reset and the smaller counter will have a
       remainder skewing any subsequent messages by that amount.
       Table 16-2 has a few examples of configuring DMA Message sizes.


                     Important: Reading the DMAnSCNT or DMAnDCNT registers will never return
                     zero. When either register is decremented from ‘1’, it is immediately reloaded
                     from the corresponding size register.


       Table 16-2. Example Message Size
              Operation                     Example             SCNT         DCNT                     Comments
       Read from single SFR         UART Receive Buffer           1            N       N equals the number of bytes desired in
       location to RAM                                                                 the destination buffer. N ≥ 1.
       Write to single SFR         UART Transmit Buffer           N             1      N equals the number of bytes desired in
       location from RAM                                                               the source buffer. N ≥ 1.
       Read from multiple SFR       ADC Result registers          2           2*N      N equals the number of ADC results to be
       location                                                                        stored in memory. N ≥ 1
       Write to Multiple SFR     PWM Duty Cycle registers        2*N            2      N equals the number of PWM duty cycle
       registers                                                                       values to be loaded from a memory table.
                                                                                       N≥1

       Figure 16-4. DMA Counters Block Diagram


                                              DMAnSSZ                                         DMAnDSZ


                                             DMAnSCNT                                        DMAnDCNT


                                       1                                                1


16.3.4 DMA Message Transfers
       Once the Enable bit is set to start DMA message transfers, the Source/Destination Pointer and
       Counter registers are initialized to the conditions shown in the table below.

       Table 16-3. DMA Initial Conditions
                                 Register                                                    Value Loaded
                                DMAnSPTR                                                      DMAnSSA
                                DMAnSCNT                                                      DMAnSSZ


--- p268 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                                     DMA - Direct Memory Access

        ...........continued
                                  Register                                                   Value Loaded
                                 DMAnDPTR                                                     DMAnDSA
                                DMAnDCNT                                                      DMAnDSZ

        During the DMA operation after each transaction, Table 16-4 and Table 16-5 indicate how the
        Source/Destination Pointer and Counter registers are modified.
        The following sections discuss how to initiate and terminate DMA transfers.

        Table 16-4. DMA Source Pointer/Counter During Operation
                                  Register                                     Modified Source Counter/Pointer Value
                                                                                     DMAnSCNT = DMAnSCNT -1
                                                                                SMODE = 00: DMAnSPTR = DMAnSPTR
                               DMAnSCNT != 1
                                                                              SMODE = 01: DMAnSPTR = DMAnSPTR + 1
                                                                               SMODE = 10: DMAnSPTR = DMAnSPTR - 1
                                                                                       DMAnSCNT = DMAnSSZ
                               DMAnSCNT == 1
                                                                                       DMAnSPTR = DMAnSSA

        Table 16-5. DMA Destination Pointer/Counter During Operation
                                  Register                                   Modified Destination Counter/Pointer Value
                                                                                     DMAnDCNT = DMAnDCNT -1
                                                                                DMODE = 00: DMAnDPTR = DMAnDPTR
                               DMAnDCNT != 1
                                                                              DMODE = 01: DMAnDPTR = DMAnDPTR + 1
                                                                              DMODE = 10: DMAnDPTR = DMAnDPTR - 1
                                                                                       DMAnDCNT = DMAnDSZ
                               DMAnDCNT == 1
                                                                                       DMAnDPTR = DMAnDSA

16.3.4.1 Starting DMA Message Transfers
        The DMA can initiate data transactions by either of the following two conditions:
        • User software control
        •   Hardware trigger, SIRQ
16.3.4.1.1 User Software Control
        Software starts or stops DMA transaction by setting/clearing the DGO bit. The DGO bit is also used
        to indicate whether a DMA hardware trigger has been received and a message is in progress.


                     Important:
                     1. Software start can only occur when the EN bit is set.
                     2. If the CPU writes to the DGO bit while it is already set, there is no effect on the
                        system, the DMA will continue to operate normally.


16.3.4.1.2 Hardware Trigger, SIRQ
        A hardware trigger is an interrupt request from another module sent to the DMA with the purpose
        of starting a DMA message. The DMA start trigger source is user-selectable using the DMAnSIRQ
        register.
        The SIRQEN bit is used to enable sampling of external interrupt triggers by which a DMA transfer can
        be started. When set, the DMA will sample the selected interrupt source and when cleared, the DMA
        will ignore the interrupt source. Clearing the SIRQEN bit does not stop a DMA transaction currently
        in progress, it only stops more hardware request signals from being received.


--- p269 ---
                                                                                                PIC18F27/47/57Q43
                                                                                        DMA - Direct Memory Access

16.3.4.2 Stopping DMA Message Transfers
        The DMA controller can stop data transactions by any of the following conditions:
        •   Clearing the DGO bit
        •   Hardware abort trigger, AIRQ
        •   Source count reload
        •   Destination count reload
        •   Clearing the EN bit
16.3.4.2.1 User Software Control
        If the user clears the DGO bit, the message will be stopped and the DMA will remain in the current
        configuration.
        For example, if the user clears the DGO bit after source data have been read but before it is written
        to the destination, then the data in the DMAnBUF register will not reach its destination.
        This is also referred to as a soft-stop as the operation can resume, if desired, by setting the DGO bit
        again.
16.3.4.2.2 Hardware Trigger, AIRQ
        The AIRQEN bit is used to enable sampling of external interrupt triggers by which a DMA transaction
        can be aborted.
        Once an abort interrupt request has been received, the DMA will perform a soft-stop by clearing the
        DGO bit, as well as clearing the SIRQEN bit so overruns do not occur. The AIRQEN bit is also cleared
        to prevent additional abort signals from triggering false aborts.
        If desired, the DGO bit can be set again and the DMA will resume operation from where it left off
        after the soft stop had occurred, as none of the DMA state information is changed in the event of an
        abort.
16.3.4.2.3 Source Count Reload
        A DMA message is considered to be complete when the Source Count register is decremented from
        ‘1’ and then reloaded (i.e., once the last byte from either the source read or destination write has
        occurred). When the SSTP bit is set and the Source Count register is reloaded, then further message
        transfer is stopped.
16.3.4.2.4 Destination Count Reload
        A DMA message is considered to be complete when the Destination Count register is decremented
        from 1 and then reloaded (i.e., once the last byte from either the source read or destination write
        has occurred). When the DSTP bit is set and the Destination Count register is reloaded then further
        message transfer is stopped.


                     Important: Reading the DMAnSCNT or DMAnDCNT registers will never return
                     zero. When either register is decremented from ‘1’, it is immediately reloaded
                     from the corresponding size register.


16.3.4.2.5 Clearing the EN Bit
        If the user clears the EN bit, the message will be stopped and the DMA will return to its default
        configuration. This is also referred to as a hard stop, as the DMA cannot resume operation from
        where it was stopped.


--- p270 ---
                                                                                                PIC18F27/47/57Q43
                                                                                        DMA - Direct Memory Access

                     Important: After the DMA message transfer is stopped, it requires an extra
                     instruction cycle before the Stop condition takes effect. Thus, after the Stop
                     condition has occurred, a source read or a destination write can occur depending
                     on the source or destination bus availability.


16.4    Disable DMA Message Transfer Upon Completion
        Once the DMA message is complete, it may be desirable to disable the trigger source to prevent
        overrun or under run of data. This can be done by any of the following methods:
        • Clearing the SIRQEN bit
        •   Setting the SSTP bit
        •   Setting the DSTP bit

16.4.1 Clearing the SIRQEN Bit
        Clearing the SIRQEN bit stops the sampling of external start interrupt triggers, hence preventing
        further DMA message transfers.
        An example is a communications peripheral with a level-triggered interrupt. The peripheral will
        continue to request data (because its buffer is empty) even though there is no more data to be
        moved. Disabling the SIRQEN bit prevents the DMA from processing these requests.

16.4.2 Source/Destination Stop
        The SSTP and DSTP bits determine whether or not to disable the hardware triggers (SIRQEN = 0),
        once a DMA message has completed.
        When the SSTP bit is set and the DMAnSCNT = 0, then the SIRQEN bit will be cleared. Similarly, when
        the DSTP bit is set and the DMAnDCNT = 0, the SIRQEN bit will be cleared.


                     Important: The SSTP and DSTP bits are independent functions and do not
                     depend on each other. It is possible for a message to be stopped by either
                     counter at message end or both counters at message end.


16.5    Types of Hardware Triggers
        The DMA has two different trigger inputs, the source trigger and the abort trigger. Each of these
        trigger sources is user configurable using the DMAnSIRQ and DMAnAIRQ registers.
        Based on the source selected for each trigger, there are two types of requests that can be sent to
        the DMA:
        • Edge triggers
        •   Level triggers

16.5.1 Edge Trigger Requests
        An edge request occurs only once when a given module interrupt requirements are true. Examples
        of edge triggers are the ADC conversion complete and the interrupt-on-change interrupts.

16.5.2 Level Trigger Requests
        A level request is asserted as long as the condition that causes the interrupt is true. Examples of
        level triggers are the UART receive and transmit interrupts.


--- p271 ---
                                                                                               PIC18F27/47/57Q43
                                                                                       DMA - Direct Memory Access

16.6   Types of Data Transfers
       Based on the memory access capabilities of the DMA (see Table 16-1), the following sections discuss
       the different types of data movement between the source and destination memory regions.
       •   N:1
           This type of transfer is common when sending predefined data packets (such as strings) through
           a single interface point (such as communications modules transmit registers).
       •   N:N
           This type of transfer is useful for moving information out of the program Flash or Data EEPROM
           to SRAM for manipulation by the CPU or other peripherals.
       •   1:1
           This type of transfer is common when bridging two different modules data streams together
           (communications bridge).
       •   1:N
           This type of transfer is useful for moving information from a single data source into a memory
           buffer (communications receive registers).

16.7   DMA Interrupts
       Each DMA has its own set of four interrupt flags, used to indicate a range of conditions during data
       transfers. The interrupt flag bits can be accessed using the corresponding PIR registers (refer to the
       “VIC - Vectored Interrupt Controller Module” chapter).

16.7.1 DMA Source Count Interrupt
       The Source Count Interrupt Flag (DMAxSCNTIF) is set every time the DMAnSCNT register reaches
       zero and is reloaded to its starting value.

16.7.2 DMA Destination Count Interrupt
       The Destination Count Interrupt Flag (DMAxDCNTIF) is set every time the DMAnDCNT register
       reaches zero and is reloaded to its starting value.
       The DMA source and destination count interrupts signal the CPU when the DMA messages are
       completed.

16.7.3 Abort Interrupt
       The Abort Interrupt Flag (DMAxAIF) is used to signal that the DMA has halted activity due to an abort
       signal from one of the abort sources. This is used to indicate that the transaction has been halted by
       a hardware event.

16.7.4 Overrun Interrupt
       When the DMA receives a trigger to start a new message before the current message is completed,
       then the Overrun Interrupt Flag (DMAxORIF) bit is set.
       This condition indicates that the DMA is being requested before its current transaction is finished.
       This implies that the active DMA may not be able to keep up with the demands from the peripheral
       module being serviced, which may result in data loss.
       The DMAxORIF flag being set does not cause the current DMA transfer to terminate.
       The overrun interrupt is only available for trigger sources that are edge-based and is not available
       for sources that are level-based. Therefore, a level-based interrupt source does not trigger a DMA
       overrun error due to the potential latency issues in the system.
       An example of an interrupt that can use the overrun interrupt is a timer overflow (or period match)
       interrupt. This event only happens every time the timer rolls over and is not dependent on any other
       system conditions.


--- p272 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                          DMA - Direct Memory Access

       An example of an interrupt that does not allow the overrun interrupt is the UART TX buffer. The
       UART will continue to assert the interrupt until the DMA is able to process the message. Due to
       latency issues, the DMA may not be able to service an empty buffer immediately, but the UART
       continues to assert its transmit interrupt until it is serviced. If overrun was allowed in this case,
       the overrun would occur almost immediately, as the module samples the interrupt sources every
       instruction cycle.

16.8   DMA Setup and Operation
       The following steps illustrate how to configure the DMA for data transfer:
       1. Select the desired DMA using the DMASELECT register.
       2. Program the appropriate source and destination addresses for the transaction into the
          DMAnSSA and DMAnDSA registers.
       3. Select the source memory region that is being addressed by the DMAnSSA register, using the
          SMR bits.
       4. Program the SMODE and DMODE bits to select the Addressing mode.
       5. Program the source size (DMAnSSZ) and destination size (DMAnDSZ) registers with the number
          of bytes to be transferred. It is recommended for proper operation that the size registers be a
          multiple of each other.
       6. If the user desires to disable data transfers once the message has completed, then the SSTP and
          DSTP bits need to be set (see the Source/Destination Stop section).
       7. If using hardware triggers for data transfer, set up the hardware trigger interrupt sources for
          the starting and aborting DMA transfers (DMAnSIRQ and DMAnAIRQ), and set the corresponding
          Interrupt Request Enable (SIRQEN and AIRQEN) bits.
       8. Select the priority level for the DMA (see the “System Arbitration” section in the “PIC18 CPU”
          chapter) and lock the priorities (see the “Priority Lock” section in the “PIC18 CPU” chapter).
       9. Enable the DMA by setting the EN bit.
       10. If using software control for data transfer, set the DGO bit, else this bit will be set by the
           hardware trigger.
       Once the DMA is set up, Figure 16-5 describes the sequence of operation when the DMA uses
       hardware triggers and utilizes the unused CPU cycles (bubble) for DMA transfers.
       The following sections describe with visual reference the sequence of events for different
       configurations of the DMA module.


--- p273 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                       DMA - Direct Memory Access

Figure 16-5. DMA Operation with Hardware Trigger

                                    Configure DMA
                                       Module


                                        EN = 1


                                     DMA Source/
                                  Destination Pointers/
                                  Counters are loaded


                                     SIRQEN = 1 &          N
                                        Trigger?

                                                  Y

                                       DGO = 1

                                         Y


                                                           N
                                        Bubble?


                                         Y
                                                                                  DMAnBUF = &DMAnSPTR
                                     Source Read
                                                                                  XIP = 1


                                                           N
                                        Bubble?


                                             Y
                                                                                  &DMAnDPTR = DMABUF
                                   Destination Write
                                                                                  XIP = 0


                                                       Y         Reload
                                                                            DMAxSCNTIF
                                    DMAnSCNT = 0               DMAnSCNT &                    DGO = 0
                                                                               =1
                                                                DMAnSPTR

                                                 N
                                        Update                                           Y
                                       DMAnSSA,                             SIRQEN = 0       SSTP = 1
                                       DMAnSCNT

                                                                                                   N


                                                       Y         Reload
                                                                            DMAnDCNTIF
                                    DMAnDCNT = 0               DMAnDCNT &                    DGO = 0
                                                                               =1
                                                                DMAnDPTR

                                              N
                                                                                         Y
                                       Update                               AIRQEN = 0       DSTP = 1
                                      DMAnDSA,
                                      DMAnDCNT
                                                                                                   N


                              N
                                       DGO = 0


                                        Y

                                      End Process


--- p274 ---
                                                                                                                                           PIC18F27/47/57Q43
                                                                                                                                   DMA - Direct Memory Access

16.8.1 Source Stop
       When the Source Stop bit is set (SSTP = 1) and the DMAnSCNT register reloads, the DMA clears the
       SIRQEN bit to stop receiving new start interrupt request signals and sets the DMAnSCNTIF flag. Refer
       to the figure below for more details.

       Figure 16-6. GPR-GPR Transactions with Hardware Triggers, SSTP = 1

                              1    2     3         4      5     6           7       8    9        10    11    12     13       14    15   16   17      18   19

                Instruction
                  Clock

                        EN

                  SIRQEN

          Source Hardware
              Trigger

                      DGO

              DMAnSPTR                   0x100                      0x101                       0x102                 0x103                   0x100

              DMAnDPTR                   0x200                      0x201                       0x200                 0x201                   0x200

              DMAnSCNT                   4                            3                            2                      1                   4

              DMAnDCNT                   2                            1                            2                      1                   2


             DMA STATE            IDLE             SR(1) DW(2) SR(1) DW(2)               IDLE           SR(1) DW(2) SR(1) DW(2)               IDLE


            DMAxSCNTIF

           DMAxDCNTIF


                              DMAnSSA    0x100                DMAnDSA            0x200

                              DMAnSSZ        0x4              DMAnDSZ             0x2


       Notes:
       1. SR - Source Read
       2. DW - Destination Write


--- p275 ---
                                                                                                                                            PIC18F27/47/57Q43
                                                                                                                                    DMA - Direct Memory Access

16.8.2 Destination Stop
       When the Destination Stop bit is set (DSTP = 1) and the DMAxDCNT register reloads, the DMA clears
       the SIRQEN bit to stop receiving new start interrupt request signals and sets the DMAnDCNTIF flag.

       Figure 16-7. GPR-GPR Transactions with Hardware Triggers, DSTP = 1

                              1    2     3         4       5     6           7      8     9        10    11    12     13       14   15   16   17      18   19

                Instruction
                  Clock

                        EN

                  SIRQEN

          Source Hardware
              Trigger

                      DGO

              DMAnSPTR                   0x100                       0x101                       0x100                 0x101                  0x100

              DMAnDPTR                   0x200                       0x201                       0x202                 0x203                  0x200

              DMAnSCNT                   2                             1                            2                      1                  2

              DMAnDCNT                   4                             3                            2                      1                  4

             DMA STATE            IDLE             SR(1) DW(2) SR(1) DW(2)                IDLE           SR(1) DW(2) SR(1) DW(2)              IDLE


           DMAxSCNTIF

           DMAxDCNTIF


                              DMAnSSA    0x100                 DMAnDSA            0x200

                              DMAnSSZ        0x2               DMAnDSZ             0x4


       Notes:
       1. SR - Source Read
       2. DW - Destination Write

16.8.3 Continuous Transfer
       When the Source or the Destination Stop bit is cleared (SSTP, DSTP = 0), the transactions continue
       unless stopped by the user. The DMAxSCNTIF and DMAxDCNTIF flags are set whenever the
       respective counter registers are reloaded.


--- p276 ---
                                                                                                                                                                                PIC18F27/47/57Q43
                                                                                                                                                                        DMA - Direct Memory Access

Figure 16-8. GPR-GPR Transactions with Hardware Triggers, SSTP, DSTP = 0

                   1   2      3    4     5     6       7     8   9      10    11    12    13       14    15    16    17     18     19    20       21   22   23     24   25    26     27       28   29   30       31   32

     Instruction
       Clock


            EN

      SIRQEN
       Source
      Hardware
       Trigger
        DGO

    DMAnSPTR               0x100               0x101                 0x100                 0x101                    0x100                0x101                0x100                  0x101              0x100

    DMAnDPTR               0x200               0x201                 0x202                 0x203                    0x200                0x201                0x202                  0x203              0x202

    DMAnSCNT                  2                    1                     2                     1                     2                        1                    2                      1                  2

    DMAnDCNT                  4                    3                     2                     1                     4                        3                    2                      1                  2

       DMA                         SR(1)DW(2) SR(1) DW(2)
                       IDLE                                      IDLE         SR(1) DW(2) SR(1) DW(2)         IDLE          SR(1) DW(2) SR(1) DW(2)         IDLE        SR(1) DW(2) SR(1) DW(2)         IDLE
      STATE


   DMAxSCNTIF


  DMAxDCNTIF


                           DMAnSSA             0x100                         DMAnDSA           0x200

                           DMAnSSZ                 0x2                       DMAnDSZ               0x4


Notes:
1. SR - Source Read
2. DW - Destination Write


--- p277 ---
                                                                                                                                                PIC18F27/47/57Q43
                                                                                                                                        DMA - Direct Memory Access

16.8.4 Transfer from SFR to GPR
       The following visual reference describes the sequence of events when copying ADC results to a GPR
       location. The ADC interrupt flag can be chosen as the source hardware trigger, the source address
       can be set to point to the ADC Result registers (e.g., at 0x3EEF), and the destination address can be
       set to point to any chosen GPR location (e.g., at 0x100).

       Figure 16-9. SFR Space to GPR Space Transfer

                              1      2       3         4      5     6           7       8            N      N+1   N+2   N+3       N+4   N+5    N+6     N+7     N+x

                Instruction
                  Clock

                        EN

                  SIRQEN

          Source Hardware
              Trigger

                      DGO

              DMAnSPTR                      0x3EEF                   0x3EF0                        0x3EEF                 0x3EF0              0x3EEF

              DMAnDPTR                      0x100                       0x101                      0x102                   0x103              0x103

              DMAnSCNT                       2                            1                          2                        1                  2

              DMAnDCNT                      10                            9                          8                        7                  6

             DMA STATE               IDLE              SR(1) DW(2) SR(1) DW(2)                      IDLE     SR(1) DW(2) SR(1) DW(2)           IDLE

            DMAxSCNTIF


           DMAxDCNTIF


                              DMAnSSA       0x3EEF                DMAnDSA            0x100

                              DMAnSSZ            0x2              DMAnDSZ             0xA

                                  SMODE          0x1              DMODE               0x1


       Notes:
       1. SR - Source Read
       2. DW - Destination Write

16.8.5 Overrun Condition
       The Overrun Interrupt flag is set if the DMA receives a trigger to start a new message before the
       current message is completed.


--- p278 ---
                                                                                                                                     PIC18F27/47/57Q43
                                                                                                                             DMA - Direct Memory Access

Figure 16-10. Overrun Interrupt

                       1    2      3         4      5     6           7       8    9        10    11    12     13       14    15   16   17      18   19

         Instruction
           Clock

                 EN

           SIRQEN

   Source Hardware
       Trigger

               DGO

       DMAnSPTR                    0x100                      0x101                       0x100                 0x101                   0x100

       DMAnDPTR                    0x200                      0x201                       0x202                 0x203                   0x200

       DMAnSCNT                    2                            1                            2                      1                   2

       DMAnDCNT                    4                            3                            2                      1                   4

      DMA STATE             IDLE             SR(1) DW(2) SR(1) DW(2)               IDLE           SR(1) DW(2) SR(1) DW(2)               IDLE


     DMAxSCNTIF

    DMAxDCNTIF

       DMAxORIF


                       DMAnCON1bits.SMA = 01

                       DMAnSSA     0x100                DMAnDSA            0x200

                       DMAnSSZ         0x2              DMAnDSZ             0x20


Notes:
1. SR - Source Read
2. DW - Destination Write


--- p279 ---
                                                                                                                                  PIC18F27/47/57Q43
                                                                                                                          DMA - Direct Memory Access

16.8.6 Abort Trigger, Message Complete
       The AIRQEN needs to be set in order for the DMA to sample abort interrupt sources. When an
       abort interrupt is received, the SIRQEN bit is cleared and the AIRQEN bit is cleared to avoid receiving
       further abort triggers.

       Figure 16-11. Abort at the End of Message

                              1    2      3         4      5     6           7     8        N      N+1   N+2   N+3       N+4   N+5   N+6        N+7   N+8

                Instruction
                  Clock

                        EN

                   SIRQEN

                   AIRQEN
          Source Hardware
              Trigger
           Abort Hardware
              Trigger

                      DGO

              DMAnSPTR                   0x3EEF                   0x3EF0                  0x3EEF                 0x3EF0                    0x3EEF

              DMAnDPTR                   0x100                       0x101                0x109                   0x10A                    0x100

              DMAnSCNT                    2                            1                    2                        1                      2

              DMAnDCNT                   10                            9                    2                        1                     10

              DMA STATE           IDLE              SR(1) DW(2) SR(1) DW(2)                IDLE     SR(1) DW(2) SR(1) DW(2)                IDLE


            DMAxSCNTIF


            DMAxDCNTIF

                DMAxAIF
                              DMAnSSA    0x3EEF                DMAnDSA           0x100

                              DMAnSSZ         0x2              DMAnDSZ           0xA


       Notes:
       1. SR - Source Read
       2. DW - Destination Write


--- p280 ---
                                                                                                                         PIC18F27/47/57Q43
                                                                                                                 DMA - Direct Memory Access

16.8.7 Abort Trigger, Message in Progress
        When an abort interrupt request is received in a DMA transaction, the DMA will perform a soft-stop
        by clearing the DGO bit (i.e., if the DMA was reading the source register, it will complete the read
        operation and then clear the DGO bit).
        The SIRQEN bit is cleared to prevent any overrun and the AIRQEN bit is cleared to prevent any false
        aborts. When the DGO bit is set again, the DMA will resume operation from where it left off after the
        soft-stop.

        Figure 16-12. Abort During Message Transfer

                                   1          2       3      4       5            6     7      8   9   10       10           11      12

                   Instruction
                     Clock

                              EN

                      SIRQEN

                      AIRQEN
            Source Hardware
                Trigger
             Abort Hardware
                Trigger
                         DGO

                DMAnSPTR                                                 0x3EEF                                      0x3EF0          0x3EEF

                DMAnDPTR                                                 0x100                                       0x101            0x102

                DMAnSCNT                                                   2                                             1                2

                DMAnDCNT                                                   10                                            9                8

                DMA STATE                     IDLE           SR(1)                      IDLE            DW(2)    SR(1)       DW(2)    IDLE


            DMAnCONbits.XIP

                   DMAxAIF


                       DMAnSSA         0x3EEF             DMAnDSA         0x100

                       DMAnSSZ          0x2               DMAnDSZ          0xA


        Notes:
        1. SR - Source Read
        2. DW - Destination Write


--- p281 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                          DMA - Direct Memory Access

16.9    Reset
        The DMA registers are set to the default state on any Reset. The registers are also reset to the
        default state when the enable bit is cleared (EN = 0). User firmware needs to setup all the registers
        to resume DMA operation.

16.10 Power-Saving Mode Operation
        The DMA utilizes system clocks and it is treated as a peripheral when it comes to power-saving
        operations. Like other peripherals, the DMA also uses Peripheral Module Disable bits to further
        tailor its operation in low-power states.

16.10.1 Sleep Mode
        When the device enters Sleep mode, the system clock to the module is shut down, therefore no
        DMA operation is supported in Sleep. Once the system clock is disabled, the requisite read and write
        clocks are also disabled, without which the DMA cannot perform any of its tasks.
        Any transfers that may be in progress are resumed on exiting from Sleep mode. Register contents
        are not affected by the device entering or leaving Sleep mode. It is recommended that DMA
        transactions be allowed to finish before entering Sleep mode.

16.10.2 Idle Mode
        In Idle mode, all of the system clocks (including the read and write clocks) are still operating, but the
        CPU is not using them to save power.
        Therefore, every instruction cycle is available to the system arbiter and if the bubble is granted to
        the DMA, it may be utilized to move data.

16.10.3 Doze Mode
        Similar to the Idle mode, the CPU does not utilize all of the available instruction cycles slots that are
        available to it to save power. It only executes instructions based on its Doze mode settings.
        Therefore, every instruction not used by the CPU is available for system arbitration and may be
        utilized by the DMA, if granted by the arbiter.

16.10.4 Peripheral Module Disable
        The Peripheral Module Disable (PMD) registers provide a method to disable DMA by gating all clock
        sources supplied to it. The respective DMAxMD bit needs to be set to disable the DMA.

16.11 Example Setup Code
        This code example illustrates using DMA1 to transfer 10 bytes of data from 0x1000 in Flash memory
        to the UART transmit buffer.


--- p282 ---
                                                                                            PIC18F27/47/57Q43
                                                                                    DMA - Direct Memory Access


               void initializeDMA(){
               //Select DMA1 by setting DMASELECT register to 0x00
                   DMASELECT = 0x00;
               //DMAnCON1 - DPTR remains, Source Memory Region PFM, SPTR increments, SSTP
                   DMAnCON1 = 0x0B;
               //Source registers
               //Source size
                   DMAnSSZH = 0x00;
                   DMAnSSZL = 0x0A;
               //Source start address, 0x1000
                   DMAnSSAU = 0x00;
                   DMAnSSAH = 0x10;
                   DMAnSSAL = 0x00;
               //Destination registers
               //Destination size
                   DMAnDSZH = 0x00;
                   DMAnDSZL = 0x01;
               //Destination start address,
                   DMAnDSA = &U1TXB;
               //Start trigger source U1TX. Refer the datasheet for the correct code
                   DMAnSIRQ = 0xnn;
               //Change arbiter priority if needed and perform lock operation
                   DMA1PR = 0x01;        // Change the priority only if needed
                   PRLOCK = 0x55;             // This sequence
                   PRLOCK = 0xAA;             // is mandatory
                   PRLOCKbits.PRLOCKED = 1; // for DMA operation
               //Enable the DMA & the trigger to start DMA transfer
                   DMAnCON0 = 0xC0;
               }


16.12 Register Overlay
      All DMA instances in this device share the same set of registers. Only one DMA instance is accessible
      at a time. The value in the DMASELECT register is one less than the selected DMA instance. For
      example, a DMASELECT value of ‘0’ selects DMA1.

16.13 Register Definitions: DMA


--- p283 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                          DMA - Direct Memory Access

16.13.1 DMASELECT

            Name:        DMASELECT
            Address:     0x0E8
            DMA Instance Selection Register
            Selects which DMA instance is accessed by the DMA registers

      Bit           7           6               5              4                  3             2            1             0
                                                                                                          SLCT[2:0]
  Access                                                                                    R/W             R/W           R/W
   Reset                                                                                     0               0             0

Bits 2:0 – SLCT[2:0] DMA Instance Selection
            Value       Description
            n           Shared DMA registers of instance n+1 are selected for read and write operations


--- p284 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                        DMA - Direct Memory Access

16.13.2 DMAnCON0

            Name:       DMAnCON0
            Address:    0x0FC
            DMA Control Register 0

      Bit        7             6             5                4                  3           2               1             0
                EN          SIRQEN          DGO                                           AIRQEN                          XIP
  Access        R/W         R/W/HC       R/W/HS/HC                                        R/W/HC                        R/HS/HC
   Reset         0             0             0                                               0                             0

Bit 7 – EN DMA Module Enable
            Value      Description
            1          Enables module
            0          Disables module

Bit 6 – SIRQEN Start of Transfer Interrupt Request Enable
            Value      Description
            1          Hardware triggers are allowed to start DMA transfers
            0          Hardware triggers are not allowed to start the DMA transfers

Bit 5 – DGO DMA Transaction
            Value      Description
            1          DMA transaction is in progress
            0          DMA transaction is not in progress

Bit 2 – AIRQEN Abort of Transfer Interrupt Request Enable
            Value      Description
            1          Hardware triggers are allowed to abort DMA transfers
            0          Hardware triggers are not allowed to abort the DMA transfers

Bit 0 – XIP Transfer in Progress Status
            Value      Description
            1          The DMA buffer register currently holds contents from a read operation and has not transferred data to the
                       destination
            0          The DMA buffer register is empty or has successfully transferred data to the destination address


--- p285 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                  DMA - Direct Memory Access

16.13.3 DMAnCON1

           Name:        DMAnCON1
           Address:     0x0FD

           DMA Control Register 1

     Bit           7         6               5                4                   3           2        1           0
                  DMODE[1:0]                DSTP                    SMR[1:0]                SMODE[1:0]           SSTP
  Access       R/W         R/W              R/W             R/W                  R/W     R/W         R/W         R/W
   Reset        0            0               0               0                    0       0            0           0

Bits 7:6 – DMODE[1:0] Destination Address Mode Selection
           Value       Description
           11          Reserved, do not use
           10          Destination Pointer (DMADPTR) is decremented after each transfer
           01          Destination Pointer (DMADPTR) is incremented after each transfer
           00          Destination Pointer (DMADPTR) remains unchanged after each transfer

Bit 5 – DSTP Destination Counter Reload Stop
           Value       Description
           1           SIRQEN bit is cleared when destination counter reloads
           0           SIRQEN bit is not cleared when destination counter reloads

Bits 4:3 – SMR[1:0] Source Memory Region Selection
           Value       Description
           1x          Data EEPROM is selected as the DMA source memory
           01          Program Flash Memory is selected as the DMA source memory
           00          SFR/GPR data space is selected as the DMA source memory

Bits 2:1 – SMODE[1:0] Source Address Mode Selection
           Value       Description
           11          Reserved, do not use
           10          Source Pointer (DMASPTR) is decremented after each transfer
           01          Source Pointer (DMASPTR) is incremented after each transfer
           00          Source Pointer (DMASPTR) remains unchanged after each transfer

Bit 0 – SSTP Source Counter Reload Stop
           Value       Description
           1           SIRQEN bit is cleared when source counter reloads
           0           SIRQEN bit is not cleared when source counter reloads


--- p286 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                           DMA - Direct Memory Access

16.13.4 DMAnBUF

           Name:         DMAnBUF
           Address:      0x0E9

           DMA Data Buffer Register

     Bit         7               6              5               4                  3            2              1              0
                                                                      BUF[7:0]
  Access         R               R              R               R                  R            R              R              R
   Reset         0               0              0               0                  0            0              0              0

Bits 7:0 – BUF[7:0] DMA Data Buffer
           Description
           These bits reflect the content of the internal data buffer the DMA peripheral uses to hold the data being moved from the
           source to destination.


--- p287 ---
                                                                                                        PIC18F27/47/57Q43
                                                                                                DMA - Direct Memory Access

16.13.5 DMAnSSA

            Name:       DMAnSSA
            Address:    0x0F9

            DMA Source Start Address Register

      Bit        23           22          21             20                  19            18      17            16
                                                                                SSA[21:16]
  Access                                  R/W           R/W                  R/W         R/W      R/W           R/W
   Reset                                   0             0                    0             0      0             0

      Bit        15           14          13             12                  11           10       9             8
                                                               SSA[15:8]
  Access        R/W          R/W          R/W           R/W                  R/W         R/W      R/W           R/W
   Reset         0            0            0             0                    0           0        0             0

      Bit        7            6            5              4                   3            2       1             0
                                                                SSA[7:0]
  Access        R/W          R/W          R/W           R/W                  R/W         R/W      R/W           R/W
   Reset         0            0            0             0                    0           0        0             0

Bits 21:0 – SSA[21:0] Source Start Address

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names.
            1. DMAnSSAU: Accesses the upper most byte [23:16].
            2. DMAnSSAH: Accesses the high byte [15:8].
            3. DMAnSSAL: Access the low byte [7:0].


--- p288 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                      DMA - Direct Memory Access

16.13.6 DMAnSSZ

            Name:       DMAnSSZ
            Address:    0x0F7

            DMA Source Size Register

      Bit        15           14          13             12                  11        10                   9          8
                                                                                               SSZ[11:8]
  Access                                                                     R/W      R/W                  R/W        R/W
   Reset                                                                      0        0                    0          0

      Bit        7            6            5              4                   3            2                1          0
                                                                SSZ[7:0]
  Access        R/W          R/W          R/W           R/W                  R/W      R/W                  R/W        R/W
   Reset         0            0            0             0                    0        0                    0          0

Bits 11:0 – SSZ[11:0] Source Message Size

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names.
            1. DMAnSSZH: Accesses the high byte [15:8].
            2. DMAnSSZL: Access the low byte [7:0].


--- p289 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                              DMA - Direct Memory Access

16.13.7 DMAnSCNT

           Name:       DMAnSCNT
           Address:    0x0F2

           DMA Source Count Register

     Bit        15           14          13             12                  11        10           9           8
                                                                                        SCNT[11:8]
  Access                                                                    R/W      R/W         R/W          R/W
   Reset                                                                     0        0            0           0

     Bit        7            6            5              4                   3            2      1             0
                                                              SCNT[7:0]
  Access       R/W          R/W          R/W           R/W                  R/W      R/W        R/W           R/W
   Reset        0            0            0             0                    0        0          0             0

Bits 11:0 – SCNT[11:0] Current Source Byte Count

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names.
           1. DMAnSCNTH: Accesses the high byte [15:8].
           2. DMAnSCNTL: Access the low byte [7:0].


--- p290 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                               DMA - Direct Memory Access

16.13.8 DMAnSPTR

            Name:       DMAnSPTR
            Address:    0x0F4

            DMA Source Pointer Register

      Bit        23           22          21             20                  19           18      17            16
                                                                               SPTR[21:16]
  Access                                   R              R                  R             R      R             R
   Reset                                   0              0                  0             0      0             0

      Bit        15           14          13             12                  11          10       9             8
                                                               SPTR[15:8]
  Access         R            R            R              R                  R             R      R             R
   Reset         0            0            0              0                  0             0      0             0

      Bit        7            6            5              4                  3             2      1             0
                                                               SPTR[7:0]
  Access         R            R            R              R                  R             R      R             R
   Reset         0            0            0              0                  0             0      0             0

Bits 21:0 – SPTR[21:0] Current Source Address Pointer

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names.
            1. DMAnSPTRU: Accesses the upper most byte [23:16].
            2. DMAnSPTRH: Accesses the high byte [15:8].
            3. DMAnSPTRL: Access the low byte [7:0].


--- p291 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                               DMA - Direct Memory Access

16.13.9 DMAnDSA

            Name:       DMAnDSA
            Address:    0x0F0

            DMA Destination Start Address Register

      Bit        15           14          13             12                  11        10         9             8
                                                               DSA[15:8]
  Access        R/W          R/W          R/W           R/W                  R/W      R/W        R/W           R/W
   Reset         0            0            0             0                    0        0          0             0

      Bit        7            6            5              4                   3            2      1             0
                                                                DSA[7:0]
  Access        R/W          R/W          R/W           R/W                  R/W      R/W        R/W           R/W
   Reset         0            0            0             0                    0        0          0             0

Bits 15:0 – DSA[15:0] Destination Start Address

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names.
            1. DMAnDSAH: Accesses the high byte [15:8].
            2. DMAnDSAL: Access the low byte [7:0].


--- p292 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                      DMA - Direct Memory Access

16.13.10 DMAnDSZ

            Name:       DMAnDSZ
            Address:    0x0EE

            DMA Destination Size Register

      Bit        15           14            13            12                  11        10                   9         8
                                                                                                DSZ[11:8]
  Access                                                                      R/W      R/W                  R/W       R/W
   Reset                                                                       0        0                    0         0

      Bit        7            6             5              4                   3            2                1         0
                                                                 DSZ[7:0]
  Access        R/W          R/W          R/W            R/W                  R/W      R/W                  R/W       R/W
   Reset         0            0            0              0                    0        0                    0         0

Bits 11:0 – DSZ[11:0] Destination Message Size

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names.
            1. DMAnDSZH: Accesses the high byte [15:8].
            2. DMAnDSZL: Access the low byte [7:0].


--- p293 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                              DMA - Direct Memory Access

16.13.11 DMAnDCNT

           Name:       DMAnDCNT
           Address:    0x0EA

           DMA Destination Count Register

     Bit        15           14          13             12                  11        10           9           8
                                                                                        DCNT[11:8]
  Access                                                                    R/W      R/W         R/W          R/W
   Reset                                                                     0        0            0           0

     Bit        7            6            5              4          3                     2      1             0
                                                          DCNT[7:0]
  Access       R/W          R/W          R/W           R/W         R/W               R/W        R/W           R/W
   Reset        0            0            0             0           0                 0          0             0

Bits 11:0 – DCNT[11:0] Current Destination Byte Count

           Notes: The individual bytes in this multibyte register can be accessed with the following register
           names.
           1. DMAnDCNTH: Accesses the high byte [15:8].
           2. DMAnDCNTL: Access the low byte Destination Message Size bits [7:0].


--- p294 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                               DMA - Direct Memory Access

16.13.12 DMAnDPTR

            Name:       DMAnDPTR
            Address:    0x0EC

            DMA Destination Pointer Register

      Bit        15           14          13             12                  11        10         9             8
                                                              DPTR[15:8]
  Access         R            R            R              R                  R             R      R             R
   Reset         0            0            0              0                  0             0      0             0

      Bit        7            6            5              4                  3             2      1             0
                                                               DPTR[7:0]
  Access         R            R            R              R                  R             R      R             R
   Reset         0            0            0              0                  0             0      0             0

Bits 15:0 – DPTR[15:0] Current Destination Address Pointer

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names.
            1. DMAnDPTRH: Accesses the high byte [15:8].
            2. DMAnDPTRL: Access the low byte [7:0].


--- p295 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                                  DMA - Direct Memory Access

16.13.13 DMAnSIRQ

            Name:       DMAnSIRQ
            Address:    0x0FF

            DMA Start Interrupt Request Source Selection Register

      Bit        7             6             5                4                   3          2       1             0
                                                                   SIRQ[7:0]
  Access        R/W          R/W           R/W            R/W                    R/W    R/W         R/W           R/W
   Reset         0            0             0              0                      0      0           0             0

Bits 7:0 – SIRQ[7:0] DMA Start Interrupt Request Source Selection

  Table 16-6. DMA Start and Abort Interrupt Sources
                                                                          Vector                  Interrupt
     Vector                         Interrupt                            Number                    source
    Number                           source
                                                                          (cont.)                  (cont.)

      0x0                              -                                  0x42                      U2E
      0x1               HLVD (High/Low-Voltage Detect)                    0x43                      U2
      0x2                     OSF (Oscillator Fail)                       0x44                     TMR5
      0x3                   CSW (Clock Switching)                         0x45                    TMR5G
      0x4                              -                                  0x46                     CCP2
      0x5                CLC1 (Configurable Logic Cell)                   0x47                     SCAN
      0x6                              -                                  0x48                     U3RX
      0x7                 IOC (Interrupt-On-Change)                       0x49                     U3TX
      0x8                            INT0                                 0x4A                      U3E
      0x9                 ZCD (Zero-Cross Detection)                      0x4B                      U3
      0xA               AD (ADC Conversion Complete)                      0x4C                       -
      0xB                  ACT (Active Clock Tuning)                      0x4D                     CLC4
      0xC                      CM1 (Comparator)                        0x4E - 0x4F                   -
      0xD              SMT1 (Signal Measurement Timer)                    0x50                     INT2
       0xE                         SMT1PRA                                0x51                     CLC5
       0xF                         SMT1PWA                                0x52     CWG2 (Complementary Waveform Generator)
      0x10               ADT (ADC Threshold Interrupt)                    0x53                     NCO2
   0x11 - 0x13                           -                                 0x54                  DMA3SCNT
      0x14             DMA1SCNT (Direct Memory Access)                     0x55                  DMA3DCNT
      0x15                        DMA1DCNT                                 0x56                   DMA3OR
      0x16                          DMA1OR                                 0x57                    DMA3A
      0x17                           DMA1A                                 0x58                     CCP3
      0x18             SPI1RX (Serial Peripheral Interface)                0x59                     CLC6
      0x19                            SPI1TX                               0x5A                    CWG3
      0x1A                             SPI1                                0x5B                     TMR4
      0x1B                            TMR2                                 0x5C                  DMA4SCNT
      0x1C                            TMR1                                 0x5D                  DMA4DCNT
      0x1D                           TMR1G                                 0x5E                   DMA4OR
      0x1E              CCP1 (Capture/Compare/PWM)                         0x5F                    DMA4A
      0x1F                            TMR0                                 0x60                     U4RX
      0x20                             U1RX                                0x61                     U4TX
      0x21                             U1TX                                0x62                      U4E


--- p296 ---
                                                                                                  PIC18F27/47/57Q43
                                                                                          DMA - Direct Memory Access

...........continued
                                                             Vector                       Interrupt
  Vector                    Interrupt                       Number                         source
 Number                      source
                                                             (cont.)                       (cont.)

   0x22                        U1E                            0x63                           U4
   0x23                        U1                         0x64                          DMA5SCNT
0x24 - 0x25                     -                         0x65                          DMA5DCNT
   0x26                   PWM1RINT                        0x66                           DMA5OR
   0x27                   PWM1GINT                        0x67                            DMA5A
   0x28                     SPI2RX                        0x68                             U5RX
   0x29                     SPI2TX                        0x69                             U5TX
   0x2A                       SPI2                        0x6A                              U5E
   0x2B                         -                         0x6B                              U5
   0x2C                      TMR3                         0x6C                          DMA6SCNT
   0x2D                     TMR3G                         0x6D                          DMA6DCNT
   0x2E                   PWM2RINT                        0x6E                           DMA6OR
   0x2F                   PWM2GINT                        0x6F                            DMA6A
   0x30                       INT1                        0x70                               -
   0x31                       CLC2                        0x71                             CLC7
   0x32     CWG1 (Complementary Waveform Generator)       0x72                             CM2
   0x33       NCO1 (Numerically Controlled Oscillator)    0x73                             NCO3
   0x34                   DMA2SCNT                     0x74 - 0x77                           -
   0x35                   DMA2DCNT                        0x78                             NVM
   0x36                    DMA2OR                         0x79                             CLC8
   0x37                     DMA2A                         0x7A                CRC (Cyclic Redundancy Check)
   0x38                     I2C1RX                        0x7B                             TMR6
   0x39                     I2C1TX                     0x7C - 0x8F                           -
   0x3A                       I2C1                        0x90             PWM1.S1P1 (PWM1 Parameter 1 of Slice 1)
   0x3B                      I2C1E                        0x91             PWM1.S1P2 (PWM1 Parameter 2 of Slice 1)
   0x3C                         -                         0x92                          PWM1S2P1
   0x3D                       CLC3                        0x93                          PWM1S2P2
   0x3E                   PWM3RINT                        0x94                          PWM1S3P1
   0x3F                   PWM3GINT                        0x95                          PWM1S3P2
   0x40                       U2RX                            0x96                            -
   0x41                       U2TX                            0x97                            -


--- p297 ---
                                                                                                     PIC18F27/47/57Q43
                                                                                             DMA - Direct Memory Access

16.13.14 DMAnAIRQ

            Name:      DMAnAIRQ
            Address:   0x0FE

            DMA Abort Interrupt Request Source Selection Register

      Bit        7           6           5              4                   3            2      1             0
                                                             AIRQ[7:0]
  Access        R/W         R/W         R/W           R/W                  R/W      R/W        R/W           R/W
   Reset         0           0           0             0                    0        0          0             0

Bits 7:0 – AIRQ[7:0] DMA Abort Interrupt Request Source Selection
          Refer to the DMA Interrupt Sources table.


--- p298 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                              DMA - Direct Memory Access

16.14 Register Summary - DMA
Address     Name      Bit Pos.   7          6           5             4                3                 2                1          0
 0xE8     DMASELECT     7:0                                                                                         SLCT[2:0]
 0xE9      DMAnBUF      7:0                                                BUF[7:0]
                        7:0                                               DCNT[7:0]
 0xEA     DMAnDCNT
                        15:8                                                                                 DCNT[11:8]
                        7:0                                               DPTR[7:0]
 0xEC     DMAnDPTR
                        15:8                                              DPTR[15:8]
                        7:0                                                DSZ[7:0]
 0xEE     DMAnDSZ
                        15:8                                                                                 DSZ[11:8]
                        7:0                                                DSA[7:0]
 0xF0     DMAnDSA
                        15:8                                              DSA[15:8]
                        7:0                                               SCNT[7:0]
 0xF2     DMAnSCNT
                        15:8                                                                                 SCNT[11:8]
                        7:0                                                SPTR[7:0]
 0xF4     DMAnSPTR      15:8                                              SPTR[15:8]
                       23:16                                                               SPTR[21:16]
                        7:0                                                SSZ[7:0]
 0xF7     DMAnSSZ
                        15:8                                                                                 SSZ[11:8]
                        7:0                                                SSA[7:0]
 0xF9     DMAnSSA       15:8                                              SSA[15:8]
                       23:16                                                               SSA[21:16]
 0xFC     DMAnCON0      7:0      EN       SIRQEN      DGO                                          AIRQEN                           XIP
 0xFD     DMAnCON1      7:0        DMODE[1:0]         DSTP                SMR[1:0]                     SMODE[1:0]                  SSTP
 0xFE     DMAnAIRQ      7:0                                               AIRQ[7:0]
 0xFF     DMAnSIRQ      7:0                                               SIRQ[7:0]


--- p299 ---
