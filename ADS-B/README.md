# ADS-B

Captured samples:

```
./dump1090 --raw --net
No supported RTLSDR devices found.
Unable to initialize RSP
HackRF successfully initialized (AMP Enable: 0, LNA Gain: 32, VGA Gain: 48).
*5d342104fbff90;
*02c1891689464d;
*02c1891689464d;
*02c1891689464d;
*a0000917acf00030a40000dd25d2;
*a0000917acf00030a40000dd25d2;
*5d342104fbff90;
*a0000917acf00030a40000dd25d2;
*a000091780179b33fffcbb6747e9;
*8d34210460497685fd1902e0b62b;
*8d342104990042b340538af7184d;
*5d342104fbff90;
*02c1891976e605;
*02c1891976e605;
*8d34210460499684c7191aff9036;
*8d342104990042b3a03b891fd092;
```

Interactive view:

<img src="https://raw.githubusercontent.com/mgp25/RF-List/master/ADS-B/dump1090.jpeg" width=700>


Decoding some data:

```
>>> import pyModeS as pms
>>> pms.df("5dbc3e7b38cff5")
11
>>> pms.df("a000029c2004e1c5332e2020bd2e")
20
>>> pms.adsb.typecode("a000029c2004e1c5332e2020bd2e")
4
>>> pms.adsb.callsign("a000029c2004e1c5332e2020bd2e")
'ANGEL28_'
```