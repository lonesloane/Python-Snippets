__author__ = 'stephane'


def oddn(n):
    return 2*n+1


def f(x): return x % 2 != 0 and x % 3 != 0


def cube(x): return x*x*x


def add(x, y): return x+y


def example():
    for i in range(10):
        sq = reduce(add, map(oddn, range(i)), 0)
        print(i, sq)

seq = range(8)

print 'filter'
print filter(f, range(2, 25))
print 'map 1'
print map(cube, range(1, 11))
print 'map 2'
print map(add, seq, seq)
print 'reduce'
print reduce(add, range(1, 11))
print 'example'
print example()
