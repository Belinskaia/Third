import itertools

def get_combinations(s, k):
    G = []
    for k in range(k):
        m = []
        M = itertools.combinations(s, k+1)
        for j in M:
            m.append(''.join(sorted(j)))
        m.sort()
        G.extend(m)
    return G
print((get_combinations('cat', 2)))
