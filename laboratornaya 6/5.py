
import functools


def additor(cls):
    def new_getattr(self, name):
        self.__dict__[name] = None
        
    cls.__getattr__ = new_getattr()
    return cls



