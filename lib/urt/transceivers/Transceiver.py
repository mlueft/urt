import time
from ..enums import COMMAND
from lib.Property import Property
from .ITransceiver import ITransceiver

class Transceiver(ITransceiver):
    
    def __init__(self):
        
        super().__init__()

        self.__lastUpdateTime = None

        self.name         = Property(False,self)

        self.model        = Property(True,self)
        self.manufacturer = Property(True,self)
        self.smeter       = Property(True,self)
        self.dCentering   = Property(True,self)
        self.dcsCode      = Property(True,self)
        self.squelch      = Property(True,self)
        self.power        = Property(True,self)
        self.split        = Property(True,self)
        self.swr          = Property(True,self)
        self.ptt          = Property(True,self)
        self.frequency    = Property(True,self)
        self.modulation   = Property(True,self)
        # seconds
        self.updateInterval = 0.5

        self._device = None
        self.device = self.createDevice()
        self._deviceguard = self.createDeviceguard()
        self._deviceguard.setDevice(self)


    def __connectDevice(self,dev):
        
        self.model.overrideValue(dev.model.value)
        self.manufacturer.overrideValue(dev.manufacturer.value)
        self.frequency.overrideValue(dev.frequency.value)
        self.modulation.overrideValue(dev.modulation.value)

        dev.model.onChanged.add(self.__hndModelChanged)
        dev.manufacturer.onChanged.add(self.__hndManufacturerChanged)
        dev.frequency.onChanged.add(self.__hndFrequencyChanged)
        dev.modulation.onChanged.add(self.__hndModulationChanged)
        
        dev.power.onChanged.add(self.__hndPowerChanged)
        dev.split.onChanged.add(self.__hndSplitChanged)
        dev.swr.onChanged.add(self.__hndSWRChanged)
        dev.ptt.onChanged.add(self.__hndPTTChanged)

        dev.smeter.onChanged.add(self.__hndSMeterChanged)
        dev.dCentering.onChanged.add(self.__hndDCenteringChanged)
        dev.dcsCode.onChanged.add(self.__hnddcsCodeChanged)
        dev.squelch.onChanged.add(self.__hndSquelchChanged)

    def __disconnectDevice(self,dev):

        dev.model.onChanged.remove(self.__hndModelChanged)
        dev.manufacturer.onChanged.remove(self.__hndManufacturerChanged)
        dev.frequency.onChanged.remove(self.__hndFrequencyChanged)
        dev.modulation.onChanged.remove(self.__hndModulationChanged)

        dev.power.onChanged.remove(self.__hndPowerChanged)
        dev.split.onChanged.remove(self.__hndSplitChanged)
        dev.swr.onChanged.remove(self.__hndSWRChanged)
        dev.ptt.onChanged.remove(self.__hndPTTChanged)

        dev.smeter.onChanged.remove(self.__hndSMeterChanged)
        dev.dCentering.onChanged.remove(self.__hndDCenteringChanged)
        dev.dcsCode.onChanged.remove(self.__hnddcsCodeChanged)
        dev.squelch.onChanged.remove(self.__hndSquelchChanged)

    # =========================================
    # DEVICE
    # =========================================

    @property
    def device(self):
        return self._device
    
    @device.setter
    def device(self, value):
        if self._device != None:
            if self._device.isConnected:
                self._device.disconnect()
            self.__disconnectDevice(self._device)

        self._device = value
        self.__connectDevice(self._device)

    # =========================================
    # DEVICE HANDLERS
    # =========================================

    def __hndModelChanged(self,ev):
        self.model.overrideValue(self.device.model.value)

    def __hndManufacturerChanged(self,ev):
        self.manufacturer.overrideValue(self.device.manufacturer.value)

    def __hndFrequencyChanged(self,ev):
        self.frequency.overrideValue(self.device.frequency.value)

    def __hndModulationChanged(self,ev):
        self.modulation.overrideValue(self.device.modulation.value)

    def __hndSMeterChanged(self,ev):
        self.smeter.overrideValue(self.device.smeter.value)

    def __hndDCenteringChanged(self,ev):
        self.dCentering.overrideValue(self.device.dCentering.value)

    def __hnddcsCodeChanged(self,ev):
        self.dcsCode.overrideValue(self.device.dcsCode.value)

    def __hndSquelchChanged(self,ev):
        self.squelch.overrideValue(self.device.squelch.value)

    def __hndPowerChanged(self,ev):
        self.power.overrideValue(self.device.power.value)

    def __hndSplitChanged(self,ev):
        self.split.overrideValue(self.device.split.value)

    def __hndSWRChanged(self,ev):
        self.swr.overrideValue(self.device.swr.value)

    def __hndPTTChanged(self,ev):
        self.ptt.overrideValue(self.device.ptt.value)

    # =========================================
    # OPERATIONAL INTERFACE
    # =========================================


    def main(self):
        
        super().main()

        # Request information
        if self.__lastUpdateTime == None or time.time()-self.__lastUpdateTime > self.updateInterval:
            self.updateDeviceState()
            self.__lastUpdateTime = time.time()

    def generateCommand(self,command, value = None):
        # We generate the parameters for the command.
        parameters = self.device.prepairParameters(command,value)
        # We generate the final data packages.
        result = self.device.prepairData(command,parameters)
        return result

    def isCommandSupported(self,command):
        return self.device.isCommandSupported(command)

    def lockOn(self):
        commandlist = []
        command = COMMAND.LOCK_ON

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.lockOn()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def lockOff(self):
        commandlist = []
        command = COMMAND.LOCK_OFF

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.lockOff()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def lockToggle(self):
        commandlist = []
        command = COMMAND.LOCK_TOGGLE

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.lockToggle()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def splitOn(self):
        commandlist = []
        command = COMMAND.SPLIT_ON

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.splitOn()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def splitOff(self):
        commandlist = []
        command = COMMAND.SPLIT_OFF

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.splitOff()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def splitToggle(self):
        commandlist = []
        command = COMMAND.SPLIT_TOGGLE

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.splitToggle()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def setFrequency(self, value):
        commandlist = []
        command = COMMAND.SET_FREQUENCY

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.setFrequency(value)
        # We generate the actual command.
        commandlist += self.generateCommand(command,value)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def setModulation(self, value):
        commandlist = []
        command = COMMAND.SET_MODULATION

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if the modulation is not supported.
        self.device.assumeModulationSupport(value)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.setModulation(value)
        # We generate the actual command.
        commandlist += self.generateCommand(command,value)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def pttOn(self):
        commandlist = []
        command = COMMAND.PTT_ON

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.pttOn()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def pttOff(self):
        commandlist = []
        command = COMMAND.PTT_OFF

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.pttOff()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)