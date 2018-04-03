def guard_this(a, b):
    print("a =", a)
    print("b =", b)
    divide = a/b if b != 0 else "Are you out of your freakin' mind!!!"
    print("result =", divide)
    print('-'*15)


guard_this(15, 3)
guard_this(15, 2)
guard_this(15, 1)
guard_this(15, 0)
