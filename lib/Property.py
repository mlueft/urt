###
##
##
class EventManager():

    ###
    ##
    ##
    def __init__(self):
        self.__handlers= []

    ### Adds a function handler.
    ##
    ##
    def add(self, handler):
        self.__handlers.append(handler)

    ### Removes a function handler.
    ##
    ##
    def remove(self, handler):
        if handler not in self.__handlers:
            return
        self.__handlers.remove(handler)

    ### Checks if a handler has been added.
    ##
    ##
    def has(self,handler):
        return handler in self.__handlers
    
    ### Calls all added handlers.
    ##
    ##
    def provoke(self, event):
        for handler in self.__handlers:
            handler(event)
            
class ChangeEvent():
    def __init__(self):
        pass

class Property():

    def __init__(self,readonly = False):
        #print("__init__()")
        self._value = None
        self.onChanged = EventManager()
        self._hasChanged = False
        self.__readonly = readonly

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,value):
        if self.__readonly:
            raise Exception("Property value can't be changed.")
        self.overrideValue(value)
    
    @property
    def hasChanged(self):
        result = self._hasChanged
        self._hasChanged = false
        return result

    def equals(self,cValue):
        return self._value == cValue

    def overrideValue(self, value):
        self._hasChanged = not self.equals(value)
        self._value = value
        if self._hasChanged:
            self.onChanged.provoke(ChangeEvent())
        
    """
    def __eq__(self,cValue):
        print("__eq__")
        return self._value == cValue.value

    
    def __get__(self,instance,value):
        print("__get__()")
    
    def __set__(self,instance,type=None):
        print("__set__()")

    def __setattr__(self, name, value):
        print("__setattr__()")
        print("{}={}".format(name,value))

    def __str__(self):
        print("__str__()")
        return self._value

    def __repr__(self):
        print("__repr__()")
        return self._value
    
    def __add__(self,other):
        print("__add__()")

    def __sub__(self,other):
        print("__sub__()")

    def __mul__(self,other):
        print("__mul__()")

    def __truediv__(self,other):
        print("__truediv__()")

    def __floordiv__(self,other):
        print("__floordiv__()")

    def __mod__(self,other):
        print("__mod__()")

    def __pow__(self,other):
        print("__pow__()")


    def __radd__(self,other):
        print("__radd__()")

    def __rsub__(self,other):
        print("__rsub__()")

    def __rmul__(self,other):
        print("__rmul__()")

    def __rtruediv__(self,other):
        print("__rtruediv__()")

    def __rfloordiv__(self,other):
        print("__rfloordiv__()")

    def __rmod__(self,other):
        print("__rmod__()")

    def __rpow__(self,other):
        print("__rpow__()")


    def __neg__(self,other):
        print("__neg__()")

    def __pos__(self,other):
        print("__pos__()")

    
    def __lt__(self,other):
        print("__lt__()")

    def __le__(self,other):
        print("__le__()")

    def __eq__(self,other):
        print("__eq__()")

    def __ne__(self,other):
        print("__ne__()")

    def __ge__(self,other):
        print("__ge__()")

    def __gt__(self,other):
        print("__gt__()")


    def __and__(self,other):
        print("__and__()")

    def __or__(self,other):
        print("__or__()")    

    def __xor__(self,other):
        print("__xor__()")

    def __lshift__(self,other):
        print("__lshift__()")

    def __rshift__(self,other):
        print("__rshift__()")

    def __invert__(self,other):
        print("__invert__()")

    
    def __iadd__(self,other):
        print("__iadd__()")

    def __isub__(self,other):
        print("__isub__()")

    def __imul__(self,other):
        print("__imul__()")

    def __itruediv__(self,other):
        print("__itruediv__()")

    def __ifloordiv__(self,other):
        print("__ifloordiv__()")

    def __imod__(self,other):
        print("__imod__()")

    def __ipow__(self,other,modulo):
        print("__ipow__()")

    
    def __iand__(self,other,modulo):
        print("__iand__()")

    def __ior__(self,other,modulo):
        print("__ior__()")

    def __ixor__(self,other,modulo):
        print("__ixor__()")

    def __ilshift__(self,other,modulo):
        print("__ilshift__()")

    def __irshift__(self,other,modulo):
        print("__irshift__()")

    
    def __dir__(self,other,modulo):
        print("__dir__()")

    def __instancecheck__(self,other,modulo):
        print("__instancecheck__()")

    def __subclasscheck__(self,other,modulo):
        print("__subclasscheck__()")

    """