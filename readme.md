# URT
URT stands for universal RX TX. It is a pure python library that aims to build a standardizes API for radio transceivers.
It is designed to support different manufacturers and protocols.

# Protocols
Protocols are implemented in /urt/protocol/

## Supported Protocols
* B5 - The B5 protocol represents the old Yaesu 5 byte protocol.

# Transceivers
Transceivers are implemented in /urt/transceiver

## Supported transceivers
* Yaesu FT-812

# API
The API is object oriented and eventdriven.

## Basic example
```python
# This is the most basic example of using URT.

# Makes classes available.
from lib.urt.transceivers.yaesu.FT_817 import FT_817
from lib.urt.ENUMS import MODULATIONS

# Creates a FT-817 transceiver
t = FT_817()

# Sets serial port properties
t.device.port.setProperty("port","/dev/rfcomm0")
t.device.port.setProperty("baudrate",9600)

# Sets the working frequency of the transveiver.
t.setFrequency(14101000)

# Sets the working modulation of the transceiver.
t.setModulation(MODULATIONS.LSB)

# Runs the main loop.
# The main loop makes the serial connection working
# and receives data comming from the transceiver.
while True:
    t.main()
```
