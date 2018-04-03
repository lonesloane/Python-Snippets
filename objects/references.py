__author__ = 'stephane'

"""
Beware of side-effects when passing around references of objects!
"""

a = [1, 2, 3]
print( a)
b = a  # b and a both 'pointing' to the same object
b[0] = 5    # a change to b will also affect a
            # since both are pointing to the same reference object
print( a)