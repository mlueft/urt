
class ITransceiver():

    def __init__(self):
        pass

    # =========================================
    # DEVICE
    # =========================================

    def createDevice(self):
        raise("createDevice() not implemented in transceiver class!")
    
    @property
    def device(self):
        pass
    
    @device.setter
    def device(self, value):
        pass

    def main(self):
        pass
    
    def updateDeviceState(self):
        raise("updateDeviceState() not implemented in transceiver class!");

    def generateCommand(self,command, value = None):
        pass
    
    def isCommandSupported(self,command):
        pass
    
    # =========================================
    # OPERATIONAL INTERFACE
    # =========================================

    def generateCommand(self,command, value = None):
        pass

    def isCommandSupported(self,command):
        pass

    def lockOn(self):
        pass

    def lockOff(self):
        pass

    def lockToggle(self):
        pass

    def splitOn(self):
        pass

    def splitOff(self):
        pass

    def splitToggle(self):
        pass

    def setFrequency(self, value):
        pass

    def setModulation(self, value):
        pass

    def pttOn(self):
        pass

    def pttOff(self):
        pass
