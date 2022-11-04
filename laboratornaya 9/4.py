import numpy as np
import functools

class PrintDispersion(Exception):
    pass

class PrintAverage(Exception):
    pass

class PrintAmount(Exception):
    pass

def handling():
    print('Starting handling')
    information = []
    while True:
        try:
            extra_inf = yield
            information.extend(list(extra_inf))
        except PrintDispersion:
            yield 'Dispersion: {}'.format(np.var(information))
        except PrintAverage:
            yield 'Average: {}'.format(np.mean(information))
        except PrintAmount:
            yield 'Number of elements: {}'.format(len(information))

            
def Coroutine(h):
    @functools.wraps(h)
    def inner(*args, **kwargs):
        hen = h()
        next(hen)
        return hen
    return inner
  
  
if __name__ == '__main__':
    handling = Coroutine(handling)
    coroutine = handling()
    coroutine.send((56, 78, 100, 41220, 18))
    print(coroutine.throw(PrintDispersion))
    next(coroutine)
    coroutine.send((59, 61, 71, 74, 81, 95, 2))
    print(coroutine.throw(PrintAverage))
    next(coroutine)
    coroutine.send((72, 51, 48, 41, 27, 20))
    print(coroutine.throw(PrintAmount))
    
    
    
