# MAP

# 1 - generator
(m(x) for x in S)

# 2 - yield
def map(m, S):
    for x in S:
        yield m(x)

# 3 - built-in map
def mapper(x):
    return m(x)

map(mapper, S)
# or
map(lambda x: m(x), S)

# FILTER

# 1 - generator
(x for x in S if f(x))

# 2 - yield
def filter(f, S):
    for x in S:
        if f(x): yield x

# 3 - built-in filter
def filtering(x):
    if f(x): return x

filter(filtering, S)
# or
filter(lamda x: f(x), S)

# REDUCE

# 1 - generator
sum(x for x in S)

# 3 - built-in reduce
from functools import reduce

def mul(a, b):
    return a * b

def prod(S):
    return reduce(mul, S, 1)

# or
def prod2(S):
    return reduce(lambda a, b: a * b, S, 1)

