__author__ = 'stephane'


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

# generator expressions:
print(sum(i*i for i in range(10)))  # sum of squares
x_vec = [10, 20, 30]
y_vec = [7, 5, 3]

print(sum(x*y for x,y in zip(x_vec, y_vec)))  # dot product

entry = 'golf'

print(''.join(list(entry[i] for i in range(len(entry) - 1, -1, -1))))
