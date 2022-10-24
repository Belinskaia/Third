def my_map (func, iterable, *rest):
    for arg in zip(iterable, *rest):
        yield func(*arg)

def my_zip (it1, it2):
    itr1 = iter(it1)
    itr2 = iter(it2)
    for i in range(min(len(it1), len(it2))):
        a, b = next(itr1), next(itr2)
        yield (a,b)

def my_enumerate (it, start = 0):
    itr = iter(it)
    for i in range(len(it)):
        yield (i,next(itr))

def F (a):
    return str(a)*3


A = [6, 8, ' ', 'jfj']
B = [5, 9, 120]

print(list(my_enumerate(B)))
print(list(enumerate(B)))

print (list(zip(A,B)))
print(list(my_zip(A,B)))

print(list(map(F,A)))
print(list(my_map(F,A)))
