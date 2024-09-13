
class URTException(Exception):
    pass

class DeviceGuardException(URTException):
    pass

class CommandNotSupportedException(URTException):
    pass

class ModulationNotSupported(URTException):
    pass