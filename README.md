# RF List

If you are a macOS user and you need to use cmake, remember to add the install prefix to avoid errors:

```
cmake -DCMAKE_INSTALL_PREFIX=/opt/local ../
```

## Mobile Communications

### 4G - LTE

- [OpenLTE](https://sourceforge.net/p/openlte/wiki/Home/): An open source implementation of the 3GPP LTE specifications. USRP recommended. [+ OpenLTE Manual](https://github.com/mgp25/RF-List/blob/master/Mobile%20Communications/4G/OpenLTE/OpenLTE%20Manual.pdf)

- [LTE Cell Scanner](https://github.com/JiaoXianjun/LTE-Cell-Scanner): OpenCL, SDR, TDD/FDD LTE cell scanner. [+ Detected cells somewhere in Madrid, Spain](https://github.com/mgp25/RF-List/blob/master/Mobile%20Communications/4G/LTE%20Cells%20detected%20in%20Madrid%20-%20Spain.pdf)

### 3G - UMTS

- [OpenUMTS](https://github.com/RangeNetworks/OpenBTS-UMTS
): An open source implementation of the 3GPP UMTS specifications. [+ OpenUMTS Manual](https://github.com/mgp25/RF-List/blob/master/Mobile%20Communications/3G/OpenUMTS/OpenUMTS%20Manual.pdf)

### 2G - GSM

- [gr-gsm](https://github.com/ptrkrysik/gr-gsm): 
Gnuradio blocks and tools for receiving GSM transmissions.

If you get the following error:

```
/usr/local/include/osmocom/core/endian.h:27:10: error: 'endian.h' file not found
      with <angled> include; use "quotes" instead
#include <endian.h>
```

You just need to replace `#include <endian.h>` to `#include "endian.h"`.

- [IMSI Catcher](https://github.com/Oros42/IMSI-catcher): This program show you IMSI numbers of cellphones around you.
 

## RF Security

- [TempestSDR](https://github.com/martinmarinov/TempestSDR): 
Remote video eavesdropping using a software-defined radio platform.


## GNURadio

- [gr-correctiq](https://github.com/ghostop14/gr-correctiq): GNURadio blocks to remove that IQ DC spike just like some software and drivers do! Three techniques available: auto, auto-tune to dc offset, and manual. 

## ADS-B

- [dump1090_sdrplus](https://github.com/itemir/dump1090_sdrplus): Dump1090_sdrplus is a Mode S decoder for Software Defined Radio (SDR) devices including RTL SDR, HackRF, Airspy and SDRplay.
