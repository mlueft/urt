
class IPort():

    def __init__(self):
        self._type = None
    
    @property
    def type(self):
        return self._type
    
    def main(self):
        pass

    def getPropertyNames(self):
        pass

    def setProperty(self, key, value):
        pass

    def getProperty(self, key):
        pass

    def open(self):
        pass

    def close(self):
        pass
    
    @property
    def isOpen(self):
        pass

    def write(self,data):
        pass

    @property
    def available(self):
        pass

    def read(self, size):
        pass