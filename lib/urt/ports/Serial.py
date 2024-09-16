import serial
from ..enums import PORTTYPE
from . import IPort

class Serial(IPort):

    __port     = "port"
    __baudrate = "baudrate"
    __parity   = "parity"
    __stopbit  = "stopbit"
    __bytesize = "bytesize"
    __xonxoff  = "xonxoff"
    __rtscts   = "rtscts"
    __dsrdtr   = "dsrdtr"

    def __init__(self):
        super().__init__()
        self._type = PORTTYPE.SERIAL

        self.__port = serial.Serial()
        self.__port.parity    = serial.PARITY_NONE
        self.__port.stopbit   = serial.STOPBITS_TWO
        self.__port.bytesize  = serial.EIGHTBITS
        self.__port.xonxoff   = False
        self.__port.rtscts    = False
        self.__port.dsrdtr    = False

    def main(self):
        super().main()

    def getPropertyNames(self):
        return[
            __port,
            __baudrate,
            __parity,
            __stopbit,
            __bytesize,
            __xonxoff,
            __rtscts,
            __dsrdtr
        ]
    
    def setProperty(self, key, value):
        if key == Serial.__port:
            self.__port.port = value
        elif key == Serial.__baudrate:
            self.__port.baudrate = value
        elif key == Serial.__parity:
            self.__port.parity = value
        elif key == Serial.__stopbit:
            self.__port.stopbit = value
        elif key == Serial.__bytesize:
            self.__port.bytesize = value
        elif key == Serial.__xonxoff:
            self.__port.xonxoff = value
        elif key == Serial.__rtscts:
            self.__port.rtscts = value
        elif key == Serial.__dsrdtr:
            self.__port.dsrdtr = value
        else:
            raise Eception("Key not recnognized!")

    def getProperty(self, key):
        if key == Serial.__port:
            return self.__port.port
        elif key == Serial.__baudrate:
            return self.__port.baudrate
        elif key == Serial.__parity:
            return self.__port.parity
        elif key == Serial.__stopbit:
            return self.__port.stopbit
        elif key == Serial.__bytesize:
            return self.__port.bytesize
        elif key == Serial.__xonxoff:
            return self.__port.xonxoff
        elif key == Serial.__rtscts:
            return self.__port.rtscts
        elif key == Serial.__dsrdtr:
            return self.__port.dsrdtr
        else:
            raise Eception("Key not recnognized!")

    def open(self):
        self.__port.open()
        
    def close(self):
        self.__port.close()
        
    @property
    def isOpen(self):
        return self.__port.is_open
    
    def write(self,data):
        if not self.isOpen:
            self.open()
        return self.__port.write(data)

    @property
    def available(self):
        return self.__port.in_waiting

    def read(self, size):
        return self.__port.read(size)
        