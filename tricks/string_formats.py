__author__ = 'stephane'

#rjust ljust

for x in range(1, 11):
    print repr(x).rjust(2), repr(x**2).rjust(3), repr(x**3).rjust(4)

for x in range(1, 11):
    print "{0:2d} {1:3d} {2:4d}".format(x, x**2, x**3)

# fancy format
print "This {food} is {adjective}".format(food='spam', adjective='absolutely delicious')

# format dictionary arguments
table = {'Han Solo': 4231, 'Luke Skywalker': 5690, 'Princess Leia': 5683}
print "Han: {0[Han Solo]:d}; Luke: {0[Luke Skywalker]:d}; Leia: {0[Princess Leia]:d}".format(table)
print "Han: {Han Solo:d}; Luke: {Luke Skywalker:d}; Leia: {Princess Leia:d}".format(**table)
