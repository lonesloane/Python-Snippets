import functools


def debug(function):
    @functools.wraps(function)
    def _debug(*args, **kwargs):
        output = function(*args, **kwargs)
        print('{function_name}({args}, {kwargs}) = {output}'.format(
            function_name=function.__name__, args=args, kwargs=kwargs, output=output))
        return output

    return _debug


@debug
def spam(eggs):
    return 'spam' * (eggs % 5)


output = spam(3)

print(output)
