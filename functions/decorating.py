import functools


def eggs(func):
    @functools.wraps(func)
    def _eggs(*args, **kwargs):
        print('{} got args: {} and kwargs: {}'.format(
            func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return _eggs


@eggs
def spam(a, b, c):
    return a * b + c


print(spam(1, 2, 3))
