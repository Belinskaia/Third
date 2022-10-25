import itertools

def maximize(lists, m):
    G = itertools.starmap(max,lists)
    S = 0
    for i in G:
        S += i*i
    return S%m


lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000))
