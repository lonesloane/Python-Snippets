__author__ = 'stephane'


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def countdown(n):
    if n <= 0:
        print "BOUM!!!"
    else:
        print n
        countdown(n-1)

def print_n(s, n):
    if n<=0:
        return
    else:
        print(s*n)
        print_n(s, n-1)

print "Fibonacci(20): ", fibonacci(20)

countdown(10)

print_n("Hello, World!", 10)