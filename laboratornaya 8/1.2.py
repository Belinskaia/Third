def my_range(n):
    _current = 1
    _current2 =1
    yield _current
    i = 1
    while True:
        if i < n:
            yield _current2
            _next = _current + _current2
            _current = _current2
            _current2 = _next
            i += 1
        else:
            break



for i in my_range(10):
    print(i, end = " ")
print()
