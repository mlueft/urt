from ..Transceiver import Transceiver
from ...protocols.b5 import FT_817 as PFT_817
from ..Deviceguard import Deviceguard_FT_817
from ..Deviceguard import FrequencyRange
from ...ENUMS import MODULATIONS
from ...ENUMS import COMMANDS

class B5(Transceiver):

    def YaesuB5(self):
        super().__init__()

    def updateDeviceState(self):
        self.requestFrequency()
        self.requestRXState()
        self.requestTXState()

    def requestRXState(self):
        commandlist = []
        command = COMMANDS.READ_RX_STATE

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.requestRXState()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def requestTXState(self):
        commandlist = []
        command = COMMANDS.READ_TX_STATE

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.requestTXState()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)

    def requestFrequency(self):
        commandlist = []
        command = COMMANDS.READ_FREQ_MODE

        # We raise an Exception if the command is not supported.
        self.device.assumeCommandSupport(command)
        # We raise an Exception if this device constellation is not allowed.
        # Or we generate some commands to keep device consistancy.
        commandlist += self._deviceguard.requestFrequency()
        # We generate the actual command.
        commandlist += self.generateCommand(command)
        # We send the final data packages to the device.
        self.device.write(commandlist)
