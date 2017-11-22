# RF List

If you are a macOS user and you need to use cmake, remember to add the install prefix to avoid erros:

```
cmake -DCMAKE_INSTALL_PREFIX=/opt/local ../
```

## Mobile Communications

### 4G - LTE

- [LTE Cell Scanner](https://github.com/JiaoXianjun/LTE-Cell-Scanner): OpenCL, SDR, TDD/FDD LTE cell scanner.

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
 

## GNURadio

- [gr-correctiq](https://github.com/ghostop14/gr-correctiq): GNURadio blocks to remove that IQ DC spike just like some software and drivers do! Three techniques available: auto, auto-tune to dc offset, and manual. 

## ADS-B

- [dump1090_sdrplus](https://github.com/itemir/dump1090_sdrplus): Dump1090_sdrplus is a Mode S decoder for Software Defined Radio (SDR) devices including RTL SDR, HackRF, Airspy and SDRplay.
