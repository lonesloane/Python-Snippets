from rx import Observer


class MyObserver(Observer):

    def on_next(self, value):
        print('Got: {}'.format(value))

    def on_error(self, error):
        print('Got: {}'.format(error))

    def on_completed(self):
        print('Sequence completed')


# === usage ===
from rx import Observable

xs = Observable.from_iterable(range(10))
d = xs.subscribe(MyObserver())
print('-'*15)
xs = Observable.from_(range(10))
d = xs.subscribe(print)
print('-'*15)
xs = Observable.from_(range(10))
d = xs.filter(lambda x: x % 2).subscribe(print)
print('-'*15)
xs = Observable.from_(range(10))
d = xs.map(lambda x: x * 2).subscribe(print)
print('-'*15)
xs = Observable.range(1, 5)
ys = Observable.from_('abcde')
zs = xs.merge(ys).subscribe(print)