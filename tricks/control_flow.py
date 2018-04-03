__author__ = 'stephane'

a = ["La", "Nature", "Est", "Un", "Temple"]

"""
!!! BAD !!! Creates an infinite loop !!!
for i in a:
    print i
    a.append(str(len(i)))
"""

# ! GOOD :
for i in a[:]:  # create a slice copy of the list
    print(i)
    a.append(str(len(i)))
print(a)
