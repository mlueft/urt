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
## Properties

Properties are Attributes of the transceiver class representing the transceiver's state. All properties implement an onChange event. So it's easy to notice every change. e.g: If the frequency is changed at the device itself.

A Property has the following Attributes:
* value - The actual value represented by the property. Setting this value isn't possible on each property. It may raise an Exception .
* hasChanged - True or False to check if the value has Changed.
* equals() - To check to values are equal.
* onChanged - Event manager to organize change messages.

### EventManager
The EventManager has the following attributes and functions:
* add() - To add an event handler.
* remove() - To remove an event handler.
* has() - To check if an event handler has been added.

The transceiver class implements the following properties:
* name - The individual name.
* model - The model.
* manufacturer - The manufacturer.
* ptt - The PTT state.
* frequency - The current working frequency.
* modulation - The current modulation.
* squelch - The squelch state.
* power - The power state.

These properties are likely to change. Not yet properly implemented.
* smeter - The smeter value.
* dCentering - The dCentering state.
* dcsCode - The DCS state.
* split - The split mode.
* swr - The swr state.


```python

# The event handler for frequency changes.
def hndFrequency( ev ):
    # frequency.value is the actual value of the property frequency.
    print( "frequency : " + str(t.frequency.value))

# We add an event handler to the property frequency.
t.frequency.onChanged.add(hndFrequency)

# We set the frequency. The new value is sent to the transceiver.
t.setFrequency(99000000)

# This is not possible:
# This will raise an exception saying: "Property value can't be changed."
# t.frequency.value = 99000000

# In the main loop we receive the new frequency from the transceiver
# and the frequency.onChanged event will be provoked.
while True:
    t.main()
```