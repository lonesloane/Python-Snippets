my_list = range(16)
print(filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda x: x == "Python", languages))

squares = [i**2 for i in range(1, 11)]
print(filter(lambda x: 30 <= x <= 70, squares))

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = list(filter(lambda x: x != 'X', garbled))
print(message)
print(''.join(message))

threes_and_fives = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, [i for i in range(1, 16)]))
print(threes_and_fives)


def make_incrementer(n):
    return lambda x: x+n


f = make_incrementer(40)

print(f(1))
print(f(3))
