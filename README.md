# PyDMX
Python based DMX control demo program.

## Requirement
- USB-RS485 Converter
- PySerial
- wxPython (only for fader)

I used [DTECH USB-RS485 Converter](https://www.amazon.co.jp/DTECH-USB%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB%E3%83%9D%E3%83%BC%E3%83%88%E3%82%B3%E3%83%B3%E3%83%90%E3%83%BC%E3%82%BF%E3%83%BC-RS422%E3%81%AB%E6%8E%A5%E7%B6%9A-FTDI%E3%83%81%E3%83%83%E3%83%97%E4%BB%98%E3%81%8D%E3%82%A2%E3%83%80%E3%83%97%E3%82%BF%E3%83%BC%E3%82%B1%E3%83%BC%E3%83%96%E3%83%ABWindows-Xp%E3%81%8A%E3%82%88%E3%81%B3Mac%E3%81%AB%E5%AF%BE%E5%BF%9C/dp/B076WVFXN8/ref=sr_1_1?ie=UTF8&qid=1533279683&sr=8-1&keywords=Dtech+USB+RS485).

to instal pyserial, try

```
pip install pyserial
```

for the GUI fader, wxPython is used.

```
pip install wxPython
```

# How to use 

## PyDMX.py

`PyDMX.py` contains simple DMX control class.

For the instance create the connection like below:

```python
from PyDMX.py import *

dmx = PyDMX('COM3') # for Linux use '/dev/ttyUSB0' or something
```

then, you can set '255' value in the address '1' as following:

```python
dmx.set_data(1,255)
```

Finally use `send()` function to send dmx signals.

```
dmx.send()
```

### Option

Here shows option in the constructor.

- `Option Name` (Default Value)
  - COM (COM8): Comport device name.  Check it on your device manager.
  - Cnumber (512): DMX channels number. DMX512 protocol uses 512 channel. 
  - Brate (250000): Baudrate. Usually do not need change.
  - Bsize (8): Bite size decided by DMX512 protocol.
  - StopB (2): Stop bit number decided by DMX512 protocol.


You can add these options like a following example.

```python
mydmx = PyDMX('/dev/ttyUSB0',Cnumber=1,Brate=9600)
```

## PyDMX_fader.py

`PyDMX_fader.py` contains the GUI fader class named `Controller()`. 

You can just run this program as a fader.

```
python PyDMX_fader.py <fader channel number>
```

The default fader channel number is 4.

You may see following window after putting the COM port.
![](https://i.imgur.com/Z1E0KOP.png)


# Program flow

DMX is a kind of serial communication.
See Japanese explanation [here](https://qiita.com/ossyaritoori/items/53c3dd438d4232515c18).

![](https://camo.qiitausercontent.com/bd9629642e937d38c088b68cd2711a7cc5a8a4fd/687474703a2f2f7777772e74616d61746563682e636f2e6a702f74616d6164612f646d78312e676966)

You need,

- 250kbps baudrate, 1 startbit, 2 stopbit
- Break(LOW) Longer than 88us 
- MAB(High) Longer than 8us 
- startcode before data


# For Debugging

DMX Break length and MAB length are not rigidly defined.
You'll need to change these parameter depends on your devices.
