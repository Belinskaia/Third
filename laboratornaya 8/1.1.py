def print_map(function, iterable):
    iterator = iter(iterable)
    try:
        while True:
            print(function(next(iterator)))
    except Exception:
        pass


def F(a):
    return str(a)*3


A = [1, 'fhg', 'kh98']
print_map(F,A)
