gen = (x ** 2 for x in range(20))  # Same as list comprehension but () indicate a generator

for x in gen:
    print(x)
