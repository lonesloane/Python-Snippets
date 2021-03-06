class A(object):
    def __init__(self):
        print('A')

    @staticmethod
    def foo():
        print('foo')

class B(object):
    def __init__(self):
        print('B')

    @staticmethod
    def bar():
        print('bar')

class C(A,B):
    def foobar(self):
        self.foo()
        self.bar()

a = A() # print 'A'
a.foo()
b = B() # print 'B'
b.bar()
c = C() # prints only 'A' because of the m.r.o. method resolution order, it runs only the first occurrence of the method
c.foobar()