class Borg:

    __shared_state = {}

    def __init__(self):
        self.val = None
        self.__dict__ = self.__shared_state


# === usage ===

b1 = Borg()
b2 = Borg()

b1.val = 'milkshake'

print('b1 val: {}'.format(b1.val))
print('b2 val: {}'.format(b2.val))
print('b1 == b2 ?')
print(b1 == b2)
