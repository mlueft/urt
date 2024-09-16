
class URTException(Exception):
    pass

class CommandNotSupportedException(URTException):
    pass

class ModulationNotSupported(URTException):
    pass

#
# DEVICEGUARD
#
class DeviceGuardException(URTException):
    pass

class ModulationException(DeviceGuardException):
    pass

class FrequencyException(DeviceGuardException):
    pass

class PTTException(DeviceGuardException):
    pass