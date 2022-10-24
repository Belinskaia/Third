import itertools
def get_permutations(s, n):
    M = sorted(itertools.permutations(s,n))
    for i in range(len(M)):
        M[i] = "".join(list(M[i]))
    return M

S = 'cat'
N = 2
print(list(get_permutations("cat", 2)))
