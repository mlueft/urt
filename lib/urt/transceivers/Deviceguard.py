from .ITransceiver import ITransceiver
from ..Exceptions import DeviceGuardException
from ..ENUMS import MODULATIONS, COMMANDS

# This class is just for use in this file.
class ATTRIBUTES():
    FREQUENCY  = 0x01
    TX         = 0x02
    MODULATION = 0x03

class Deviceguard(ITransceiver):

    def __init__(self):
        self.__frequencytable = []
        self.__device = None

    def addFrequencyRange(self, range):
        self.__frequencytable.append(range)

    def setDevice(self,device):
        self.__device = device

    def getFrequenciesBy(self,attribute,value):
        result = []
        for f in self.__frequencytable:
            if attribute == ATTRIBUTES.FREQUENCY:
                if f.frequencySupported(value):
                    result.append(f)
            elif attribute == ATTRIBUTES.TX:
                if f.txSupported(value):
                    result.append(f)
            elif attribute == ATTRIBUTES.MODULATION:
                if f.modulationSupported(value):
                    result.append(f)
            else:
                raise Exception("Attribute not supported in Deviceguard!")
        return result    

    def lockOn(self):
        # We assume lock allowed in any state.
        return []

    def lockOff(self):
        # We assume lock allowed in any state.
        return []

    def lockToggle(self):
        # We assume lock allowed in any state.
        return []

    def splitOn(self):
        # We assume split allowed in any state.
        return []

    def splitOff(self):
        # We assume split allowed in any state.
        return []

    def splitToggle(self):
        # We assume split allowed in any state.
        return []

    def setFrequency(self, newFrequency):
        
        # Is the new frequency allowed by the current modulation?
        # Or do we need to change modulation to allow the frequency?

        # Get get the frequency range with the new frequency
        frequency = self.getFrequenciesBy(ATTRIBUTES.FREQUENCY,newFrequency)

        # If we get no frequency newFrequency is not supported by the device
        # or range definition is not complete in device class
        if len(frequency) == 0:
            raise DeviceGuardException("Frequency not supported or frequency range definition is not complete in device class!")

        # If we get more than one frequency regions are overlapping.
        if len(frequency) > 1:
            raise DeviceGuardException("Frequency range definitions are overlapping in device class!")

        # Id there a forced modulation for this range?
        if frequency[0].forcedModulation != None:
            return self.__device.generateCommand( COMMANDS.SET_MODULATION, frequency[0].forcedModulation )

        # Is the current modulation supported by this frequency range?
        supported = frequency[0].modulationSupported(self.__device.modulation.value)

        # If supported everything is fine
        if supported:
            return []

        # Otherwise we try to find any modulation to switch to.
        modulation = frequency[0].getAnyModulation()

        # If we found any we switch and everything is OK.
        if modulation != None:
            return self.__device.generateCommand( COMMANDS.SET_MODULATION, modulation )

        # Otherwise we raise an exception.            
        raise DeviceGuardException("Frequency not allowed with current modulation!")

    def setModulation(self, newModulation):
        # Is the new modulation allowed at the current frequency?

        # Get the frequency range with the current device frequency.
        frequency = self.getFrequenciesBy(ATTRIBUTES.FREQUENCY,self.__device.frequency.value)

        # If we get not frequency, but the device is already working with it
        # frequency range definition is not complete.
        if len(frequency) == 0:
            raise DeviceGuardException("Frequency range definition is not complete in device class!")

        # If we get more than one frequency regions are overlapping.
        if len(frequency) > 1:
            raise DeviceGuardException("Frequency range definitions are overlapping in device class!")
        
        # Id the new modulation supported in this range?
        supported = frequency[0].modulationSupported(newModulation)

        # If not supported we raise an exception.
        if not supported:
            raise DeviceGuardException("Modulation not allowed at this frequency!")

        return []

    def requestRXState(self):
        # We assume OK.
        return []

    def requestTXState(self):
        # We assume OK.
        return []

    def requestFrequency(self):
        # We assume OK.
        return []
    
    def pttOn(self):
        # Is PTT in with the current frequency allowed?

        # Get the frequency range with the current device frequency.
        frequency = self.getFrequenciesBy(ATTRIBUTES.FREQUENCY,self.__device.frequency.value)

        # If we get not frequency, but the device is already working with it
        # frequency range definition is not complete.
        if len(frequency) == 0:
            raise DeviceGuardException("Frequency range definition is not complete in device class!")

        # If we get more than one frequency regions are overlapping.
        if len(frequency) > 1:
            raise DeviceGuardException("Frequency range definitions are overlapping in device class!")
        
        # If tx is not allower we raise an exception
        if not frequency[0].tx:
            raise DeviceGuardException("PTT is not allowed with the current frequency!")

        return []

    def pttOff(self):
        # We assume lock allowed in any state.
        return []


class FrequencyRange():

    def __init__(self,minHz,maxHz,tx,modulations,forcedModulation=None):
        self.min = minHz
        self.max = maxHz
        self.tx = tx
        self.modulations = modulations
        self.forcedModulation = forcedModulation

    def getAnyModulation(self):
        if self.modulations & MODULATIONS.LSB:
            return MODULATIONS.LSB

        if self.modulations & MODULATIONS.USB:
            return MODULATIONS.USB

        if self.modulations & MODULATIONS.AM:
            return MODULATIONS.AM

        if self.modulations & MODULATIONS.FM:
            return MODULATIONS.FM

        if self.modulations & MODULATIONS.FMN:
            return MODULATIONS.FMW

        if self.modulations & MODULATIONS.FMW:
            return MODULATIONS.FMW

        if self.modulations & MODULATIONS.CW:
            return MODULATIONS.CW

        if self.modulations & MODULATIONS.CWR:
            return MODULATIONS.CWR

        if self.modulations & MODULATIONS.DIG:
            return MODULATIONS.DIG

        if self.modulations & MODULATIONS.PKT:
            return MODULATIONS.PKT

        return None

    def frequencySupported(self, value):
        #print(value, self.min, self.max, value >= self.min and value <= self.max)
        return value >= self.min and value <= self.max

    def txSupported(self, value):
        return self.tx == value

    def modulationSupported(self, value):
        return value&self.modulations > 0
    

class Deviceguard_FT_817(Deviceguard):

    def __init__(self):
        super().__init__()

