import functools

class tik:

    def __init__(self, path):
        self.path = path

    def __call__(self, func):
        @functools.wraps(func)
        def intro(*args):
            from time import time
            start = time()
            result = func(*args)
            if result is None:
                result = '-'
            finish = time()
            t = finish - start
            args = list(args)
            with open(self.path, 'w') as file:
                file.write(str(start)+'\n'+str(args)+'\n'+str(result)+'\n'+str(finish)+'\n'+str(t))
            return result
        return intro

way = input()
N = int(input())
M = int(input())
@tik(way)
def f(n,m):   #просто рандомная функция чтобы проверить работу декоратора
    if n == 1 or m == 2:
        return 1
    return n+m
f(N,M)

