def my_range(n):
    _current = 1
    _current2 =1
    for i in range(n):
        yield _current
        _next = _current + _current2
        _current = _current2
        _current2 = _next


for i in my_range(10):
    print(i, end = " ")
print()
