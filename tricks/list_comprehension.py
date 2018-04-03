__author__ = 'stephane'

freshfruit = ["  banana  ", ' loganberry ', '  passion fruit   ']

print([weapon.strip() for weapon in freshfruit]) # list comprehension can be used to "clean up" elements

vec = [2, 4, 6, 8]

print( [3*x for x in vec])
print( [[x, x**2] for x in vec])
print( [(x, x**2) for x in vec])
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print( [x*y for x in vec1 for y in vec2])
print( [vec1[i]*vec2[i] for i in range(len(vec1))])
print( [str(round(355/113.0, i)) for i in range(0, 12)])