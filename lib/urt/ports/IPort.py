
class IPort():

    def __init__(self):
        self._type         = None
        self.__initialized = False

    @property
    def type(self):
        return self._type
    
    def initialize(self):
        pass
    
    def main(self):
        if self.__initialized == False:
            self.initialize()
            self.__initialized = True

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