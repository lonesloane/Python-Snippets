import functools


def memoize(func):
    func.cache = dict()

    @functools.wraps(func)
    def _memoize(*args, **kwargs):
        if args not in func.cache:
            func.cache[args] = func(*args)
        return func.cache[args]

    return _memoize


@memoize
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# decorator lru_cache also implements the memoization
from functools import lru_cache


@lru_cache(128)
def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


def fibo_iter():
    a = 1
    b = 1
    yield a
    while True:
        yield b
        a, b = b, a+b


def call_fibo(n):
    for i, f_i in enumerate(fibo_iter()):
        if i == n: break
    return f_i


for i in range(1, 100):
    print('Fibonacci({}): {}'.format(i, fibonacci(i)))

for i in range(1, 100):
    print('Fibonacci decorated({}): {}'.format(i, fibo(i)))

for i in range(1, 100):
    print('Fibonacci iter({}): {}'.format(i, call_fibo(i)))
