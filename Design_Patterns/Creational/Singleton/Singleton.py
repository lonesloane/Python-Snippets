class Singleton:
    __instance = None

    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


# === Usage ===

x = Singleton()
x.val = 'burger'
print('x val: %s ' % x.val)

y = Singleton()
y.val = 'chips'
print('y val: %s ' % y.val)

print('x val: %s ' % x.val)

print('x == y ?')
print(x == y)
