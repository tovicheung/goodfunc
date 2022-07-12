class Func:
    def __init__(self, function):
        self.function = function

    def call(self, other):
        if isinstance(other, tuple):
            try:
                return self.function(other)
            except TypeError:
                return self.function(*other)
        return self.function(other)

    def __ror__(self, other):
        return self.call(other)

    def __or__(self, other):
        return self.call(other)
        
    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

def goodfunc(func):
    return Func(func)