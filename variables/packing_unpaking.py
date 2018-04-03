a, b, c = 1, 2, 3

print('a: {}'.format(a))

spam = a, (b, c)

print('spam: {}'.format(spam))

a, b = spam

print('a: {}'.format(a))
print('b {}'.format(b))

# unpacking with variable length object will create a list:
print('')
print('Unpacking with variable length object will create a list')
spam, *eggs = 1, 2, 3, 4

print('spam: {}'.format(spam))
print('eggs: {}'.format(eggs))
