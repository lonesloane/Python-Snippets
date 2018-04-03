def count(start=0, step=1, stop=10):
    n = start
    while n <= stop:
        yield n
        n += step


def count_return(start=0, step=1, stop=10):
    n = start
    while n <= stop:
        yield n
        n += step
    return 'This is the end...'


print('-' * 30)
print('Generator without return')
print('-' * 30)
for x in count(10, 2.5, 20):
    print(x)
print('-' * 30)
print('Generator with return')
print('-' * 30)
g = count_return(10, 2.5, 20)
for x in g:
    print(x)
next(g)
