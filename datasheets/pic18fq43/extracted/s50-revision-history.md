                                                                                                          PIC18F27/47/57Q43
                                                                                                   Appendix A: Revision History


50.   Appendix A: Revision History
      Doc Rev. Date    Comments
      H       02/2024 Update IPD Electrical Specifications D200 through D208; minor editorial corrections.
      G       03/2023 Added DC and AC Characteristics Graphs and Tables; updated Tables 47-8, 47-15, 47-16 and 47-17; minor
                      editorial corrections.
      F       05/2021 Updated Package Details section; updated Peripheral Interrupt registers; minor editorial corrections
      E       12/2020 Updated Section 17.2.3.1; minor editorial corrections.
      D       07/2020 Updated Tables: 40-3, 47-7 and 47-15; minor editorial corrections.
      C       02/2020 Minor editorial corrections.
      B       12/2019 Updated Features: Low-Power Mode Sleep; updated Tables: Electrical Section.
      A       10/2019 Initial document release.


--- p963 ---
                                                                                        PIC18F27/47/57Q43


Microchip Information
The Microchip Website
Microchip provides online support via our website at www.microchip.com/. This website is used to
make files and information easily available to customers. Some of the content available includes:
•   Product Support – Data sheets and errata, application notes and sample programs, design
    resources, user’s guides and hardware support documents, latest software releases and archived
    software
•   General Technical Support – Frequently Asked Questions (FAQs), technical support requests,
    online discussion groups, Microchip design partner program member listing
•   Business of Microchip – Product selector and ordering guides, latest Microchip press releases,
    listing of seminars and events, listings of Microchip sales offices, distributors and factory
    representatives

Product Change Notification Service
Microchip’s product change notification service helps keep customers current on Microchip
products. Subscribers will receive email notification whenever there are changes, updates, revisions
or errata related to a specified product family or development tool of interest.
To register, go to www.microchip.com/pcn and follow the registration instructions.

Customer Support
Users of Microchip products can receive assistance through several channels:
•   Distributor or Representative
•   Local Sales Office
•   Embedded Solutions Engineer (ESE)
•   Technical Support
Customers should contact their distributor, representative or ESE for support. Local sales offices are
also available to help customers. A listing of sales offices and locations is included in this document.
Technical support is available through the website at: www.microchip.com/support


--- p964 ---
                                                                                                    PIC18F27/47/57Q43


Product Identification System
To order or obtain information, e.g., on pricing or delivery, refer to the factory or the listed sales
office.

    PART NO.      [X](1)     –X                /XX
Device          Tape Temperature              Package
              and Reel Range
Device:                               PIC18F25Q43, PIC18F45Q43, PIC18F55Q43, PIC18F26Q43, PIC18F46Q43,
                                      PIC18F56Q43, PIC18F27Q43, PIC18F47Q43, PIC18F57Q43
Tape & Reel Option:                   Blank                                   = Standard Packaging (Tube or Tray)
                                      T                                       = Tape & Reel
Temperature Range:                    I                                       = -40°C to +85°C (Industrial)
                                      E                                       = -40°C to +125°C (Extended)
Package:                              SP                                      = 28-lead SPDIP
                                      SO                                      = 28-lead SOIC
                                      SS                                      = 28-lead SSOP
                                      STX                                     = 28-lead VQFN
                                      P                                       = 40-lead PDIP
                                      MP                                      = 40-lead QFN
                                      PT                                      = 44-lead TQFP
                                      PT                                      = 48-lead TQFP
                                      6LX                                     = 48-lead VQFN

Examples:
• PIC18F27Q43 T-E/SP: Tape and Reel, Extended temperature, 28-lead SPDIP
•    PIC18F46Q43 T-I/PT: Tape and Reel, Industrial temperature, 44-lead TQFP
•    PIC18F55Q43 T-I/6LX: Tape and Reel, Industrial temperature, 48-lead VQFN
Notes:
1. Tape and Reel identifier only appears in the catalog part number description. This identifier is
   used for ordering purposes and is not printed on the device package. Check with your Microchip
   Sales Office for package availability with the Tape and Reel option.
2. Small form-factor packaging options may be available. Please check www.microchip.com/
   packaging for small-form factor package availability, or contact your local Sales Office.

Microchip Devices Code Protection Feature
Note the following details of the code protection feature on Microchip products:
•    Microchip products meet the specifications contained in their particular Microchip Data Sheet.
•    Microchip believes that its family of products is secure when used in the intended manner, within
     operating specifications, and under normal conditions.
•    Microchip values and aggressively protects its intellectual property rights. Attempts to breach the
     code protection features of Microchip product is strictly prohibited and may violate the Digital
     Millennium Copyright Act.
•    Neither Microchip nor any other semiconductor manufacturer can guarantee the security of its
     code. Code protection does not mean that we are guaranteeing the product is “unbreakable”.
     Code protection is constantly evolving. Microchip is committed to continuously improving the
     code protection features of our products.


--- p965 ---
                                                                                       PIC18F27/47/57Q43


Legal Notice
This publication and the information herein may be used only with Microchip products, including
to design, test, and integrate Microchip products with your application. Use of this information
in any other manner violates these terms. Information regarding device applications is provided
only for your convenience and may be superseded by updates. It is your responsibility to ensure
that your application meets with your specifications. Contact your local Microchip sales office for
additional support or, obtain additional support at www.microchip.com/en-us/support/design-help/
client-support-services.
THIS INFORMATION IS PROVIDED BY MICROCHIP "AS IS". MICROCHIP MAKES NO REPRESENTATIONS
OR WARRANTIES OF ANY KIND WHETHER EXPRESS OR IMPLIED, WRITTEN OR ORAL, STATUTORY
OR OTHERWISE, RELATED TO THE INFORMATION INCLUDING BUT NOT LIMITED TO ANY IMPLIED
WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
PURPOSE, OR WARRANTIES RELATED TO ITS CONDITION, QUALITY, OR PERFORMANCE.
IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, INCIDENTAL, OR
CONSEQUENTIAL LOSS, DAMAGE, COST, OR EXPENSE OF ANY KIND WHATSOEVER RELATED TO THE
INFORMATION OR ITS USE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS BEEN ADVISED OF THE
POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE FULLEST EXTENT ALLOWED BY LAW,
MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN ANY WAY RELATED TO THE INFORMATION OR
ITS USE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO
MICROCHIP FOR THE INFORMATION.
Use of Microchip devices in life support and/or safety applications is entirely at the buyer's risk,
and the buyer agrees to defend, indemnify and hold harmless Microchip from any and all damages,
claims, suits, or expenses resulting from such use. No licenses are conveyed, implicitly or otherwise,
under any Microchip intellectual property rights unless otherwise stated.

Trademarks
The Microchip name and logo, the Microchip logo, Adaptec, AVR, AVR logo, AVR Freaks, BesTime,
BitCloud, CryptoMemory, CryptoRF, dsPIC, flexPWR, HELDO, IGLOO, JukeBlox, KeeLoq, Kleer,
LANCheck, LinkMD, maXStylus, maXTouch, MediaLB, megaAVR, Microsemi, Microsemi logo, MOST,
MOST logo, MPLAB, OptoLyzer, PIC, picoPower, PICSTART, PIC32 logo, PolarFire, Prochip Designer,
QTouch, SAM-BA, SenGenuity, SpyNIC, SST, SST Logo, SuperFlash, Symmetricom, SyncServer,
Tachyon, TimeSource, tinyAVR, UNI/O, Vectron, and XMEGA are registered trademarks of Microchip
Technology Incorporated in the U.S.A. and other countries.
AgileSwitch, ClockWorks, The Embedded Control Solutions Company, EtherSynch, Flashtec, Hyper
Speed Control, HyperLight Load, Libero, motorBench, mTouch, Powermite 3, Precision Edge,
ProASIC, ProASIC Plus, ProASIC Plus logo, Quiet-Wire, SmartFusion, SyncWorld, TimeCesium,
TimeHub, TimePictra, TimeProvider, and ZL are registered trademarks of Microchip Technology
Incorporated in the U.S.A.
Adjacent Key Suppression, AKS, Analog-for-the-Digital Age, Any Capacitor, AnyIn, AnyOut,
Augmented Switching, BlueSky, BodyCom, Clockstudio, CodeGuard, CryptoAuthentication,
CryptoAutomotive, CryptoCompanion, CryptoController, dsPICDEM, dsPICDEM.net, Dynamic
Average Matching, DAM, ECAN, Espresso T1S, EtherGREEN, EyeOpen, GridTime, IdealBridge,
IGaT, In-Circuit Serial Programming, ICSP, INICnet, Intelligent Paralleling, IntelliMOS, Inter-Chip
Connectivity, JitterBlocker, Knob-on-Display, MarginLink, maxCrypto, maxView, memBrain, Mindi,
MiWi, MPASM, MPF, MPLAB Certified logo, MPLIB, MPLINK, mSiC, MultiTRAK, NetDetach, Omniscient
Code Generation, PICDEM, PICDEM.net, PICkit, PICtail, Power MOS IV, Power MOS 7, PowerSmart,
PureSilicon, QMatrix, REAL ICE, Ripple Blocker, RTAX, RTG4, SAM-ICE, Serial Quad I/O, simpleMAP,
SimpliPHY, SmartBuffer, SmartHLS, SMART-I.S., storClad, SQI, SuperSwitcher, SuperSwitcher II,
Switchtec, SynchroPHY, Total Endurance, Trusted Time, TSHARC, Turing, USBCheck, VariSense,
VectorBlox, VeriPHY, ViewSpan, WiperLock, XpressConnect, and ZENA are trademarks of Microchip
Technology Incorporated in the U.S.A. and other countries.
SQTP is a service mark of Microchip Technology Incorporated in the U.S.A.


--- p966 ---
                                                                                    PIC18F27/47/57Q43


The Adaptec logo, Frequency on Demand, Silicon Storage Technology, and Symmcom are registered
trademarks of Microchip Technology Inc. in other countries.
GestIC is a registered trademark of Microchip Technology Germany II GmbH & Co. KG, a subsidiary
of Microchip Technology Inc., in other countries.
All other trademarks mentioned herein are property of their respective companies.

ISBN: 978-1-6683-4088-2

Quality Management System
For information regarding Microchip’s Quality Management Systems, please visit
www.microchip.com/quality.


--- p967 ---
Worldwide Sales and Service
AMERICAS                    ASIA/PACIFIC                   ASIA/PACIFIC              EUROPE

Corporate Office            Australia - Sydney             India - Bangalore         Austria - Wels
2355 West Chandler Blvd.    Tel: 61-2-9868-6733            Tel: 91-80-3090-4444      Tel: 43-7242-2244-39
Chandler, AZ 85224-6199     China - Beijing                India - New Delhi         Fax: 43-7242-2244-393
Tel: 480-792-7200           Tel: 86-10-8569-7000           Tel: 91-11-4160-8631      Denmark - Copenhagen
Fax: 480-792-7277           China - Chengdu                India - Pune              Tel: 45-4485-5910
Technical Support:          Tel: 86-28-8665-5511           Tel: 91-20-4121-0141      Fax: 45-4485-2829
www.microchip.com/support   China - Chongqing              Japan - Osaka             Finland - Espoo
Web Address:                Tel: 86-23-8980-9588           Tel: 81-6-6152-7160       Tel: 358-9-4520-820
www.microchip.com           China - Dongguan               Japan - Tokyo             France - Paris
Atlanta                     Tel: 86-769-8702-9880          Tel: 81-3-6880- 3770      Tel: 33-1-69-53-63-20
Duluth, GA                  China - Guangzhou              Korea - Daegu             Fax: 33-1-69-30-90-79
Tel: 678-957-9614           Tel: 86-20-8755-8029           Tel: 82-53-744-4301       Germany - Garching
Fax: 678-957-1455           China - Hangzhou               Korea - Seoul             Tel: 49-8931-9700
Austin, TX                  Tel: 86-571-8792-8115          Tel: 82-2-554-7200        Germany - Haan
Tel: 512-257-3370           China - Hong Kong SAR          Malaysia - Kuala Lumpur   Tel: 49-2129-3766400
Boston                      Tel: 852-2943-5100             Tel: 60-3-7651-7906       Germany - Heilbronn
Westborough, MA             China - Nanjing                Malaysia - Penang         Tel: 49-7131-72400
Tel: 774-760-0087           Tel: 86-25-8473-2460           Tel: 60-4-227-8870        Germany - Karlsruhe
Fax: 774-760-0088           China - Qingdao                Philippines - Manila      Tel: 49-721-625370
Chicago                     Tel: 86-532-8502-7355          Tel: 63-2-634-9065        Germany - Munich
Itasca, IL                  China - Shanghai               Singapore                 Tel: 49-89-627-144-0
Tel: 630-285-0071           Tel: 86-21-3326-8000           Tel: 65-6334-8870         Fax: 49-89-627-144-44
Fax: 630-285-0075           China - Shenyang               Taiwan - Hsin Chu         Germany - Rosenheim
Dallas                      Tel: 86-24-2334-2829           Tel: 886-3-577-8366       Tel: 49-8031-354-560
Addison, TX                 China - Shenzhen               Taiwan - Kaohsiung        Israel - Ra’anana
Tel: 972-818-7423           Tel: 86-755-8864-2200          Tel: 886-7-213-7830       Tel: 972-9-744-7705
Fax: 972-818-2924           China - Suzhou                 Taiwan - Taipei           Italy - Milan
Detroit                     Tel: 86-186-6233-1526          Tel: 886-2-2508-8600      Tel: 39-0331-742611
Novi, MI                    China - Wuhan                  Thailand - Bangkok        Fax: 39-0331-466781
Tel: 248-848-4000           Tel: 86-27-5980-5300           Tel: 66-2-694-1351        Italy - Padova
Houston, TX                 China - Xian                   Vietnam - Ho Chi Minh     Tel: 39-049-7625286
Tel: 281-894-5983           Tel: 86-29-8833-7252           Tel: 84-28-5448-2100      Netherlands - Drunen
Indianapolis                China - Xiamen                                           Tel: 31-416-690399
Noblesville, IN             Tel: 86-592-2388138                                      Fax: 31-416-690340
Tel: 317-773-8323           China - Zhuhai                                           Norway - Trondheim
Fax: 317-773-5453           Tel: 86-756-3210040                                      Tel: 47-72884388
Tel: 317-536-2380                                                                    Poland - Warsaw
Los Angeles                                                                          Tel: 48-22-3325737
Mission Viejo, CA                                                                    Romania - Bucharest
Tel: 949-462-9523                                                                    Tel: 40-21-407-87-50
Fax: 949-462-9608                                                                    Spain - Madrid
Tel: 951-273-7800                                                                    Tel: 34-91-708-08-90
Raleigh, NC                                                                          Fax: 34-91-708-08-91
Tel: 919-844-7510                                                                    Sweden - Gothenberg
New York, NY                                                                         Tel: 46-31-704-60-40
Tel: 631-435-6000                                                                    Sweden - Stockholm
San Jose, CA                                                                         Tel: 46-8-5090-4654
Tel: 408-735-9110                                                                    UK - Wokingham
Tel: 408-436-4270                                                                    Tel: 44-118-921-5800
Canada - Toronto                                                                     Fax: 44-118-921-5820
Tel: 905-695-1980
Fax: 905-695-2078


--- p968 ---
