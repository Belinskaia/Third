import functools


def additor(cls):

    @functools.wraps(cls)
    def __getattribute__(self, name):
        if hasattr(self.__dict__, name):
            return self.__dict__[name]
        elif hasattr(cls.__dict__, name) or super().__hasattr__(cls.__dict__, name):
            return cls.__dict__[name]
        else:
            def __getattr__(self, name):
                return self.__dict__[name] = None




