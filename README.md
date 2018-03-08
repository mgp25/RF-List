# RFSec List

If you are a macOS user and you need to use cmake, remember to add the install prefix to avoid errors:

```
cmake -DCMAKE_INSTALL_PREFIX=/opt/local ../
```

# Index

## Hardware

- [HackRF](https://greatscottgadgets.com): low cost software radio platform.
	- [Opera cake](https://github.com/mossmann/hackrf/wiki/Opera-Cake): (sometimes operacake) is an antenna switching add on board for HackRF.

- [USRP](https://github.com/EttusResearch/uhd): The USRP software defined radio products are designed for RF applications from DC to 6 GHz, including multiple antenna (MIMO) systems.

## Software

- [Mobile Communications](#mobile-communications)
	- [4G - LTE](4g---lte)
	- [3G - UMTS](#3g---umts)
	- [2G - GSM](#2g---gsm)
	- [SIM/USIM](#simusim)
- [RF Tools](#rf-tools)
- [ADB-S](#adb-s)
- [GNURadio](#gnuradio)

## Mobile Communications

### 4G - LTE

- [OpenLTE](https://sourceforge.net/p/openlte/wiki/Home/): An open source implementation of the 3GPP LTE specifications. USRP recommended. [+ OpenLTE Manual](https://github.com/mgp25/OpenLTE#contents)

- [OpenAirInterface](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home#welcome-to-the-openairinterface-project): a separate legal entity from EURECOM, which aims to provide an open-source ecosystem for the core (EPC) and access-network (EUTRAN) protocols of 3GPP cellular systems with the possibility of interoperating with closed-source equipment in either portion of the network.

- [OpenAirInterface5G](https://gitlab.eurecom.fr/oai/openairinterface5g): OpenAirInterface 5G Wireless Implementation.

- [srsLTE](https://github.com/srsLTE/srsLTE): Open source SDR LTE software suite.

- [IMDEA-OWL](https://git.networks.imdea.org/nicola_bui/imdeaowl/tree/master): OWL stands for Online Watcher of LTE. imdeaOWL is a free and open-source LTE control channel decoder developed by IMDEA Networks Institute and based on srsLTE, an LTE library for SDR UE and eNodeB developed by SRS

- [LTE Cell Scanner](https://github.com/JiaoXianjun/LTE-Cell-Scanner): OpenCL, SDR, TDD/FDD LTE cell scanner. [+ Detected cells somewhere in Madrid, Spain](https://github.com/mgp25/RF-List/blob/master/Mobile%20Communications/4G/LTE%20Cells%20detected%20in%20Madrid%20-%20Spain.pdf)

### 3G - UMTS

- [OpenUMTS](https://github.com/mgp25/OpenBTS-UMTS
): An open source implementation of the 3GPP UMTS specifications. [+ OpenUMTS Manual](https://github.com/mgp25/OpenBTS-UMTS#contents)

### 2G - GSM

- [OpenBTS](https://github.com/RangeNetworks/openbts): GSM+GPRS Radio Access Network Node.

- [FakeBTS](http://fakebts.com/): The aim of FakeBTS project is to detect fake BTS stations and prevent attacks, using a Linux computer and hardware that allows us to scan the frequencies of GSM/GPRS.

- [IMSI Catcher](https://github.com/Oros42/IMSI-catcher): This program show you IMSI numbers of cellphones around you.

### SIM/USIM

- [pySim](https://git.osmocom.org/pysim): Python-language program that can be used to program (write) certain fields/parameters on so-called programmable SIM/USIM cards.

- [sysmo-usim-tool](https://git.sysmocom.de/sysmo-usim-tool/about/): Python language utility to configure the vendor-specific parameters of sysmoUSIM-SJS1 programmable USIM cards.
 

## RF Tools

- [Audacity](http://www.audacityteam.org/): Audacity is free, open source, cross-platform audio software for multi-track recording and editing.

- [Baudline](http://www.baudline.com/): Baudline is a time-frequency browser designed for scientific visualization of the spectral domain. Signal analysis is performed by Fourier, correlation, and raster transforms that create colorful spectrograms with vibrant detail.

- [Inspectrum](https://github.com/miek/inspectrum): Inspectrum is a tool for analysing captured signals, primarily from software-defined radio receivers.

- [Dspectrum](https://github.com/tresacton/dspectrum): Automated RF/SDR Signal Analysis.

- [rtl_433](https://github.com/merbanan/rtl_433) :Application using librtlsdr to decode the temperature from a wireless temperature sensor.

- [ooktools](https://github.com/leonjza/ooktools) :On-off keying tools for your SDR.

- [TempestSDR](https://github.com/martinmarinov/TempestSDR): 
Remote video eavesdropping using a software-defined radio platform.


## ADS-B

- [dump1090_sdrplus](https://github.com/itemir/dump1090_sdrplus): Dump1090_sdrplus is a Mode S decoder for Software Defined Radio (SDR) devices including RTL SDR, HackRF, Airspy and SDRplay.

- [pyModeS](https://github.com/junzis/pyModeS):  The Python Decoder for ADS-B (DF17) and Enhance Mode-S (DF20/21).

- [Mode S](http://mode-s.org/decode/adsb/introduction.html): An Open access book on Mode-S/ADS-B decoding and related topics.



## GNURadio

- [gr-gsm](https://github.com/ptrkrysik/gr-gsm): 
GNUradio blocks and tools for receiving GSM transmissions.

- [gr-lte](https://github.com/kit-cel/gr-lte): The gr-lte project is an Open Source Software Package which aims to provide a GNU Radio LTE Receiver to receive, synchronize and decode LTE signals.

- [gps-sdr-sim](https://github.com/osqzss/gps-sdr-sim): GPS-SDR-SIM generates GPS baseband signal data streams, which can be converted to RF using software-defined radio (SDR) platforms, such as bladeRF, HackRF, and USRP.

- [gr-correctiq](https://github.com/ghostop14/gr-correctiq): GNURadio blocks to remove that IQ DC spike just like some software and drivers do! Three techniques available: auto, auto-tune to dc offset, and manual. 

