from .ITransceiver import ITransceiver
from ..Exceptions import DeviceGuardException
from ..Exceptions import ModulationException
from ..Exceptions import FrequencyException
from ..Exceptions import PTTException
from ..enums import MODULATION, COMMAND

# This enum class is just for use in this file.
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
                raise DeviceGuardException("Attribute not supported in Deviceguard!")
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
            raise FrequencyException("Frequency not supported or frequency range definition is not complete in device class!")

        # If we get more than one frequency regions are overlapping.
        if len(frequency) > 1:
            raise FrequencyException("Frequency range definitions are overlapping in device class!")

        # Id there a forced modulation for this range?
        if frequency[0].forcedModulation != None:
            return self.__device.generateCommand( COMMAND.SET_MODULATION, frequency[0].forcedModulation )

        # Is the current modulation supported by this frequency range?
        supported = frequency[0].modulationSupported(self.__device.modulation.value)

        # If supported everything is fine
        if supported:
            return []

        # Otherwise we try to find any modulation to switch to.
        modulation = frequency[0].getAnyModulation()

        # If we found any we switch and everything is OK.
        if modulation != None:
            return self.__device.generateCommand( COMMAND.SET_MODULATION, modulation )

        # Otherwise we raise an exception.            
        raise FrequencyException("Frequency not allowed with current modulation!")

    def setModulation(self, newModulation):
        # Is the new modulation allowed at the current frequency?

        # Get the frequency range with the current device frequency.
        frequency = self.getFrequenciesBy(ATTRIBUTES.FREQUENCY,self.__device.frequency.value)

        # If we get not frequency, but the device is already working with it
        # frequency range definition is not complete.
        if len(frequency) == 0:
            raise FrequencyException("Frequency range definition is not complete in device class!")

        # If we get more than one frequency regions are overlapping.
        if len(frequency) > 1:
            raise FrequencyException("Frequency range definitions are overlapping in device class!")
        
        # Id the new modulation supported in this range?
        supported = frequency[0].modulationSupported(newModulation)

        # If not supported we raise an exception.
        if not supported:
            raise ModulationException("Modulation not allowed at this frequency!")

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
            raise FrequencyException("Frequency range definition is not complete in device class!")

        # If we get more than one frequency regions are overlapping.
        if len(frequency) > 1:
            raise FrequencyException("Frequency range definitions are overlapping in device class!")
        
        # If tx is not allower we raise an exception
        if not frequency[0].tx:
            raise PTTException("PTT is not allowed with the current frequency!")

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
        if self.modulations & MODULATION.LSB:
            return MODULATION.LSB

        if self.modulations & MODULATION.USB:
            return MODULATION.USB

        if self.modulations & MODULATION.AM:
            return MODULATION.AM

        if self.modulations & MODULATION.FM:
            return MODULATION.FM

        if self.modulations & MODULATION.FMN:
            return MODULATION.FMW

        if self.modulations & MODULATION.FMW:
            return MODULATION.FMW

        if self.modulations & MODULATION.CW:
            return MODULATION.CW

        if self.modulations & MODULATION.CWR:
            return MODULATION.CWR

        if self.modulations & MODULATION.DIG:
            return MODULATION.DIG

        if self.modulations & MODULATION.PKT:
            return MODULATION.PKT

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

