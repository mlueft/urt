from .B5 import B5
from ...protocols.b5 import FT_817 as PFT_817
from ..Deviceguard import Deviceguard_FT_817
from ..Deviceguard import FrequencyRange
from ...enums import MODULATION

class FT_817(B5):

    def __init__(self):
        super().__init__()
    
    def createDevice(self):
        dev = PFT_817()
        return dev

    def createDeviceguard(self):
        m = MODULATION        
        result = Deviceguard_FT_817()
        result.addFrequencyRange(FrequencyRange(    100000,  33000000,  True, m.LSB|m.USB|m.CW|m.CWR|m.AM|m.FM|m.DIG|m.PKT))
        result.addFrequencyRange(FrequencyRange(  33000000,  56000000,  True, m.LSB|m.USB|m.CW|m.CWR|m.AM|m.FM|m.DIG|m.PKT))
        result.addFrequencyRange(FrequencyRange(  76000000, 108000000, False, m.FMW, m.FM))
        result.addFrequencyRange(FrequencyRange( 108000000, 137000000,  True, m.LSB|m.USB|m.CW|m.CWR|m.AM|m.FM|m.DIG|m.PKT))
        result.addFrequencyRange(FrequencyRange( 137000000, 154000000,  True, m.LSB|m.USB|m.CW|m.CWR|m.AM|m.FM|m.DIG|m.PKT))
        result.addFrequencyRange(FrequencyRange( 420000000, 470000000,  True, m.LSB|m.USB|m.CW|m.CWR|m.AM|m.FM|m.DIG|m.PKT))
        return result

