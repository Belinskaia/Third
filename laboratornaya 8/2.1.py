import itertools
def get_cartesian_product(a, b):
    return itertools.product(a,b)
print(list(get_cartesian_product([1, 2], [3, 4])))
