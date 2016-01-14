def guard_this(a, b):
    print "a =", a
    print "b =", b
    divide = b != 0 and a/b or "Are you out of you freakin' mind!!!"
    print "result =", divide
    print '--------------------'

guard_this(15, 3)
guard_this(15, 2)
guard_this(15, 1)
guard_this(15, 0)
