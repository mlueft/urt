from ..b5 import B5
from ...enums import COMMAND
from ...enums import MODULATION
from ...enums import PILOTTONE

class FT_817(B5):

    def __init__(self):
        super().__init__()

    def initialize(self):
        self.model.overrideValue("FT-817(ND)")
        self.manufacturer.overrideValue("Yaesu")

    def createModulations(self):
        # These are the codes of the
        # cat protocol!
        result = MODULATION()
        result.LSB = 0x00
        result.USB = 0x01
        result.CW  = 0x02
        result.CWR = 0x03
        result.AM  = 0x04
        result.FM  = 0x08
        result.DIG = 0x0A
        result.PKT = 0x0C
        result.FMW = 0x06
        return result

    def createCommands(self):
        # These are the codes of the
        # cat protocol!
        result = COMMAND()
        result.LOCK_ON        = 0x00
        result.LOCK_OFF       = 0x80
        result.SPLIT_ON       = 0x02
        result.SPLIT_OFF      = 0x82
        result.SET_FREQUENCY  = 0x01
        result.SET_MODULATION = 0x07
        result.READ_RX_STATE  = 0xE7
        result.READ_TX_STATE  = 0xF7
        result.READ_FREQ_MODE = 0x03
        result.PTT_ON         = 0x08
        result.PTT_OFF        = 0x88
        return result

    def createPilottones(self):
        result = PILOTTONE()
        result.OFF   = 0x8A
        result.DCS   = 0x0A
        result.CTCSS = 0x2A

    def prepairParameters(self, command, value=None):
        if command == COMMAND.LOCK_ON:
            return [0x00,0x00,0x00,0x00]
        if command == COMMAND.LOCK_OFF:
            return [0x00,0x00,0x00,0x00]
        if command == COMMAND.SPLIT_ON:
            return [0x00,0x00,0x00,0x00]
        if command == COMMAND.SPLIT_OFF:
            return [0x00,0x00,0x00,0x00]
        if command == COMMAND.SET_FREQUENCY:
            result = [0x00,0x00,0x00,0x00]
            data = "{:>08d}".format(int(value/10))
            # int 99000000  Hz
            #     09900000 dHz  deziherz            
            #=>
            # 0x09 0x90 0x00 0x00  HEX
            result[0] = int(data[0:2],16)
            result[1] = int(data[2:4],16)
            result[2] = int(data[4:6],16)
            result[3] = int(data[6:8],16)
            return result
        if command == COMMAND.SET_MODULATION:
            opMode = self.encodeModulation(value)
            return [opMode,0x00,0x00,0x00]
        if command == COMMAND.READ_RX_STATE:
            return [0x00,0x00,0x00,0x00]
        if command == COMMAND.READ_TX_STATE:
            return [0x00,0x00,0x00,0x00]
        if command == COMMAND.READ_FREQ_MODE:
            return [0x00,0x00,0x00,0x00]
        if command == COMMAND.PTT_ON:
            return [0x00,0x00,0x00,0x00]
        if command == COMMAND.PTT_OFF:
            return [0x00,0x00,0x00,0x00]

    def prepairData(self, command, parameters = [0,0,0,0]):

        result = []
        # Check data

        # Here we convert the ENUM value of the command
        # to the protocol spesific token
        cmd = self.encodeCommand(command)

        # Here we build the device specific data
        # structure to be sent.
        result.append( [command,parameters + [cmd]] )
    
        return result
    
    def _getAnswerSize(self,command):
        if command == COMMAND.READ_FREQ_MODE:
            return 5

        return 1

    def _decodeAnswer(self, command,data):
        
        #print("<="+ str(command) +" = "+str(data))
        if command == COMMAND.READ_RX_STATE:
            smeter     = int((0b00001111 & data[0])>0)
            dCentering = int((0b00100000 & data[0])>5)==0
            dcsCode    = int((0b01000000 & data[0])>6)
            squelch    = int((0b10000000 & data[0])>7)==1
            self.smeter.overrideValue(smeter)
            self.dCentering.overrideValue(dCentering)
            self.dcsCode.overrideValue(dcsCode)
            self.squelch.overrideValue(squelch)

        elif command == COMMAND.READ_TX_STATE:
            pometer = int((0b00001111 & data[0])>0)
            split   = int((0b00100000 & data[0])>5)==0
            swr     = int((0b01000000 & data[0])>6)==0
            ptt     = int((0b10000000 & data[0])>7)==0
            self.power.overrideValue(pometer)
            self.split.overrideValue(split)
            self.swr.overrideValue(swr)
            self.ptt.overrideValue(ptt)

        elif command == COMMAND.READ_FREQ_MODE:
            frequency = "{:02X}{:02X}{:02X}{:02X}".format(data[0],data[1],data[2],data[3])
            modulation = self.decodeModulation(data[4])
            self.frequency.overrideValue(int(frequency)*10)
            self.modulation.overrideValue(modulation)

        else:
            #print("<="+ str(command) +" = "+str(data))
            pass